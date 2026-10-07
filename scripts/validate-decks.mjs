#!/usr/bin/env node
/**
 * Deck validator (PHASE-EX3). Node stdlib only.
 *
 *   node scripts/validate-decks.mjs [--strict] [--rights=block|flag]
 *
 * Strict rules apply to Wave-1 decks with "schema_version": 2 (CD I +
 * fashion-image-analysis). Legacy decks and decks outside Wave-1 only produce
 * warnings (Amendment A1 / FINDINGS A5). Errors on v2: dangling slots, curated
 * slides without image_brief/asset_id, missing or > 600 KB files, non-whitelisted
 * extensions, raw SVG in deck-media, bound assets without a private registry
 * raw_title, orphan deck-media files, duplicate asset use, "profield" in public
 * JSON values, flagged asset captioned "Public domain".
 *
 * Cache policy (DC):
 *   - deck-media/ orphans → errors (new rendition cache)
 *   - profield-cache/ orphans → warnings only (do not delete; EX4 may reclaim)
 *
 * Assets failing rightsVerdict are errors under --rights=block (default) and
 * warnings under --rights=flag; --rights=flag also writes
 * digital-creativity-pedagogy/excellence/curation/rights-report.json.
 * AUTOPILOT.md §0: build and gates use --strict --rights=flag.
 *
 * Exit 1 when --strict and any error is found.
 */
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { basename, dirname, join, relative } from 'node:path';

import { captionHtml } from './lib/deck-caption.mjs';
import { cacheFileOf, deckProblems, DECK_SCHEMA_VERSION, rightsVerdict } from './lib/media-rules.mjs';

const root = process.cwd();
const args = new Set(process.argv.slice(2));
const strict = args.has('--strict');
const rightsMode = args.has('--rights=flag') ? 'flag' : 'block';
const year = new Date().getFullYear();
const deckRoots = [join(root, 'docs/tracks')];
const cacheSegment = 'deck-media';
const legacyCacheSegment = 'profield-cache';
const cacheDir = join(root, 'docs/assets/images', cacheSegment);
const legacyCacheDir = join(root, 'docs/assets/images', legacyCacheSegment);
const registryPath = join(root, 'digital-creativity-pedagogy/excellence/curation/autopilot-assets.json');
const reportPath = join(root, 'digital-creativity-pedagogy/excellence/curation/rights-report.json');

/** Wave-1 (A1): Creación Digital I track + fashion-image-analysis special. */
function isWave1Deck(rel) {
  return /\/2627-dci\//.test(rel) || /\/fashion-image-analysis\//.test(rel);
}

function filesUnder(directory, predicate) {
  if (!existsSync(directory)) return [];
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) return filesUnder(path, predicate);
    return predicate(entry.name, path) ? [path] : [];
  });
}

function listing(directory) {
  const files = new Map();
  if (!existsSync(directory)) return files;
  for (const name of readdirSync(directory)) {
    const path = join(directory, name);
    if (!name.startsWith('.') && statSync(path).isFile()) files.set(name, statSync(path).size);
  }
  return files;
}

const registry = new Map();
if (existsSync(registryPath)) {
  for (const record of JSON.parse(readFileSync(registryPath, 'utf8')).assets || []) {
    registry.set(record.asset_id, record);
  }
}

const cacheFiles = listing(cacheDir);
const legacyFiles = listing(legacyCacheDir);
const deckPaths = deckRoots
  .flatMap((dir) => filesUnder(dir, (name, path) => name === 'content.json' && /\/data\/content\.json$/.test(path)))
  .sort();

const errors = [];
const warnings = [];
const report = [];
let rawAll = '';

for (const path of deckPaths) {
  const rel = relative(root, path);
  const raw = readFileSync(path, 'utf8');
  rawAll += raw;
  let content;
  try {
    content = JSON.parse(raw.replace(/^---[\s\S]*?---\s*/, ''));
  } catch (error) {
    errors.push(`${rel}: invalid JSON (${error.message})`);
    continue;
  }
  if (!Array.isArray(content.slides) || !content.slides.some((s) => s.slide_role)) {
    // Not a media deck (e.g. How to Pass: HTML slides, fixed geometrical backgrounds).
    continue;
  }

  const wave1 = isWave1Deck(rel);
  // Outside Wave-1: always warn (A1 / FINDINGS A5). Inside Wave-1: schema_version 2 is strict.
  const legacy = !wave1 || content.schema_version !== DECK_SCHEMA_VERSION;
  const unit = content.media_selection?.unit_id || basename(dirname(dirname(path)));
  const result = deckProblems(content, {
    unit,
    cacheFiles,
    cacheSegment,
    registry,
    requireRegistry: !legacy,
    year,
  });

  // Outside Wave-1 (or pre-v2 Wave-1): every deckProblems finding is a warning only.
  if (legacy) {
    warnings.push(...result.errors.map((m) => `${rel}: ${m}`));
    warnings.push(...result.warnings.map((m) => `${rel}: ${m}`));
  } else {
    errors.push(...result.errors.map((m) => `${rel}: ${m}`));
    warnings.push(...result.warnings.map((m) => `${rel}: ${m}`));
  }

  if (!wave1) {
    warnings.push(`${rel}: outside Wave-1 (CD II / NM / other) — validator warns only (A1)`);
  }

  // Legacy / current Wave-1 decks still point at profield-cache: check those files as warnings.
  for (const asset of content.assets || []) {
    const file = cacheFileOf(asset.asset_url, legacyCacheSegment);
    if (!file) continue;
    if (!legacyFiles.has(file)) warnings.push(`${rel}: legacy asset file missing ${legacyCacheSegment}/${file}`);
    else if (legacyFiles.get(file) > 600 * 1024) warnings.push(`${rel}: legacy asset ${file} > 600 KB`);
    if (/\.php$/i.test(file)) warnings.push(`${rel}: legacy asset ${file} has a .php extension`);
  }

  // A12/F8: flagged asset public caption never says "Public domain".
  for (const asset of content.assets || []) {
    if (asset.rights_status === 'flagged' && /public domain/i.test(captionHtml(asset).replace(/<[^>]+>/g, ' '))) {
      const message = `${rel}: ${asset.media_slot_id}: flagged asset captioned "Public domain" (A12/F8)`;
      (legacy ? warnings : errors).push(message);
    }
  }

  const slideOf = new Map((content.slides || []).filter((s) => s.media_slot_id).map((s) => [s.media_slot_id, s]));
  for (const entry of result.rights) {
    const asset = (content.assets || []).find((a) => a.asset_id === entry.asset_id && a.media_slot_id === entry.slot) || {};
    const record = { ...asset, ...(registry.get(entry.asset_id) || {}) };
    const verdict = rightsVerdict(record, { year });
    if (!legacy && !verdict.ok) {
      const message = `${rel}: rights: ${entry.asset_id} (${entry.slot}) fails rightsVerdict: ${verdict.reasons.join('; ')}`;
      (rightsMode === 'block' ? errors : warnings).push(message);
    } else if (legacy && !verdict.ok) {
      warnings.push(`${rel}: rights: ${entry.asset_id} (${entry.slot}) fails rightsVerdict: ${verdict.reasons.join('; ')}`);
    }
    report.push({
      deck: rel,
      schema_version: content.schema_version ?? null,
      wave1,
      legacy,
      slide_id: slideOf.get(entry.slot)?.slide_id ?? null,
      heading: slideOf.get(entry.slot)?.heading ?? null,
      media_slot_id: entry.slot,
      asset_id: entry.asset_id,
      title: asset.title ?? null,
      author: record.author || null,
      licence: record.licence || null,
      licence_url: record.licence_url || null,
      canonical_source_url: record.canonical_source_url || null,
      author_death_year: record.author_death_year ?? null,
      eu_term_ok: record.eu_term_ok === true,
      eu_term_reason: record.eu_term_reason || null,
      rights_status: asset.rights_status ?? null,
      verdict: verdict.ok ? 'pass' : 'fail',
      reasons: verdict.reasons,
    });
  }
}

// Orphan: deck-media → error; profield-cache → warning (do not delete; FINDINGS B2).
for (const name of cacheFiles.keys()) {
  if (!rawAll.includes(`/assets/images/${cacheSegment}/${name}`)) {
    errors.push(`orphan cache file ${cacheSegment}/${name} (referenced by no deck)`);
  }
}
for (const name of legacyFiles.keys()) {
  if (!rawAll.includes(`/assets/images/${legacyCacheSegment}/${name}`)) {
    warnings.push(`orphan cache file ${legacyCacheSegment}/${name} (referenced by no deck; kept until EX4)`);
  }
}
for (const name of cacheFiles.keys()) {
  if (/\.svg$/i.test(name)) errors.push(`${cacheSegment}/${name}: raw SVG in deck-media (rasterise it; A6/F6)`);
  else if (!/\.(jpg|png|webp|gif)$/i.test(name)) errors.push(`${cacheSegment}/${name}: extension not whitelisted`);
}

if (rightsMode === 'flag') {
  const failing = report.filter((r) => r.verdict === 'fail');
  const curatorFlagged = report.filter((r) => r.rights_status === 'flagged');
  const payload = {
    schema: 'deck-rights-report/v1',
    mode: 'flag',
    policy: 'AUTOPILOT.md §0: rights recorded and flagged, not blocking; rightsVerdict stays strict. Professor reviews every flagged asset before release.',
    year,
    generated_at: new Date().toISOString(),
    summary: {
      assets: report.length,
      pass: report.length - failing.length,
      flagged: failing.length,
      curator_flagged: curatorFlagged.length,
      v2_flagged: failing.filter((r) => !r.legacy).length,
      legacy_flagged: failing.filter((r) => r.legacy).length,
      wave1_flagged: failing.filter((r) => r.wave1).length,
      v2_curator_flagged: curatorFlagged.filter((r) => !r.legacy).length,
    },
    assets: report,
  };
  mkdirSync(dirname(reportPath), { recursive: true });
  writeFileSync(reportPath, `${JSON.stringify(payload, null, 2)}\n`);
}

for (const w of warnings) console.warn(`WARN  ${w}`);
for (const e of errors) console.error(`ERROR ${e}`);
console.log(
  `validate-decks: ${deckPaths.length} deck file(s), ${errors.length} error(s), ${warnings.length} warning(s) [${strict ? 'strict' : 'report'}; rights=${rightsMode}]`,
);
process.exit(strict && errors.length ? 1 : 0);
