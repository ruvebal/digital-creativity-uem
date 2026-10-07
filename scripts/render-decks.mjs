#!/usr/bin/env node
/**
 * Pre-render student decks (PHASE-EX5). Node stdlib only.
 *
 *   node scripts/render-decks.mjs [--check]
 *
 * Reads every v2 deck under docs/tracks/en/uem/2627-dci and 2627-ml and writes
 * docs/_includes/decks/<slug>.html. Legacy decks (no schema_version 2) are skipped.
 *
 * Geometric backgrounds: docs/assets/images/fractal-pass-track/uem-henon-pass-NN-<name>-<hash>.svg
 * Diagram fallback: docs/assets/images/fractal-triangles/<asset>.svg from current.json
 *
 * --check: exit 1 if any include (or lesson_figures.json) is stale (no writes).
 */
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, relative } from 'node:path';

import { DECK_SCHEMA_VERSION } from './lib/media-rules.mjs';
import { lessonFigures, parseHashedSvgName, renderDeck } from './lib/deck-render.mjs';

const root = process.cwd();
const checkOnly = process.argv.includes('--check');
const deckRoots = ['docs/tracks/en/uem/2627-dci', 'docs/tracks/en/uem/2627-ml'].map((p) => join(root, p));
const outDir = join(root, 'docs/_includes/decks');
const geometricDir = join(root, 'docs/assets/images/fractal-pass-track');
const diagramDir = join(root, 'docs/assets/images/fractal-triangles');
const base = (readFileSync(join(root, '_config.yml'), 'utf8').match(/^baseurl:\s*['"]?([^'"\n]*)['"]?/m) || [])[1] ?? '';

const shaPrefix = (path, len) => createHash('sha256').update(readFileSync(path)).digest('hex').slice(0, len);

// Geometric cycle: henon SVGs only (classroom opener law); hash must match content.
const geometric = readdirSync(geometricDir)
  .filter((n) => /^uem-henon-pass-\d+-.*\.svg$/.test(n))
  .sort();
const problems = [];
if (!geometric.length) problems.push('no uem-henon-pass-*.svg geometric backgrounds');
for (const name of geometric) {
  const parsed = parseHashedSvgName(name);
  if (!parsed) problems.push(`fractal-pass-track/${name}: name carries no content hash`);
  else {
    const expected = shaPrefix(join(geometricDir, name), parsed.hash.length);
    if (parsed.hash !== expected) problems.push(`fractal-pass-track/${name}: hash does not match content (${expected})`);
  }
}
const diagramMeta = JSON.parse(readFileSync(join(diagramDir, 'current.json'), 'utf8'));
const kochAsset = String(diagramMeta.asset || '');
const koch = `${kochAsset}.svg`;
if (!kochAsset || !existsSync(join(diagramDir, koch))) {
  problems.push(`diagram fallback missing: fractal-triangles/${koch || '(empty)'}`);
} else {
  const hash = (koch.match(/-([0-9a-f]{8,})\.svg$/) || [])[1];
  if (!hash) problems.push(`fractal-triangles/${koch}: name carries no content hash`);
  else if (hash !== shaPrefix(join(diagramDir, koch), hash.length)) {
    problems.push(`fractal-triangles/${koch}: hash does not match content`);
  }
}
if (problems.length) {
  for (const p of problems) console.error(`ERROR ${p}`);
  process.exit(1);
}

const decks = deckRoots.flatMap((dir) => (existsSync(dir) ? readdirSync(dir) : [])
  .map((slug) => ({ slug, path: join(dir, slug, 'data/content.json') }))
  .filter(({ path }) => existsSync(path)));

mkdirSync(outDir, { recursive: true });
let written = 0;
let stale = 0;
let rendered = 0;
const figures = {};
for (const { slug, path } of decks) {
  const content = JSON.parse(readFileSync(path, 'utf8').replace(/^---[\s\S]*?---\s*/, ''));
  if (content.schema_version !== DECK_SCHEMA_VERSION) {
    if (Array.isArray(content.slides) && content.slides.some((s) => s.slide_role)) {
      console.log(`skip legacy deck (schema_version ${content.schema_version ?? 'missing'}): ${slug} keeps the runtime path`);
    }
    continue;
  }
  figures[slug] = lessonFigures(content, { base });
  const html = renderDeck(content, { base, geometric, koch, source: relative(root, path) });
  const out = join(outDir, `${slug}.html`);
  rendered += 1;
  const current = existsSync(out) ? readFileSync(out, 'utf8') : null;
  if (current === html) continue;
  if (checkOnly) {
    stale += 1;
    console.error(`stale: ${relative(root, out)}`);
    continue;
  }
  writeFileSync(out, html, 'utf8');
  written += 1;
  console.log(`rendered ${content.slides.length} slide(s) → ${relative(root, out)}`);
}
const figuresPath = join(root, 'docs/_data/lesson_figures.json');
const figuresJson = `${JSON.stringify(Object.fromEntries(Object.keys(figures).sort().map((k) => [k, figures[k]])), null, 2)}\n`;
const figuresCurrent = existsSync(figuresPath) ? readFileSync(figuresPath, 'utf8') : null;
if (figuresCurrent !== figuresJson) {
  if (checkOnly) {
    stale += 1;
    console.error(`stale: ${relative(root, figuresPath)}`);
  } else {
    writeFileSync(figuresPath, figuresJson, 'utf8');
    written += 1;
    console.log(`lesson figures → ${relative(root, figuresPath)}`);
  }
}
console.log(`render-decks: ${rendered} deck(s), ${checkOnly ? `${stale} stale` : `${written} written`}.`);
process.exit(checkOnly && stale ? 1 : 0);
