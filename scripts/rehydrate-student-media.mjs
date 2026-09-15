#!/usr/bin/env node
/**
 * Rehydrate student-deck assets from reviewed Profield run manifests.
 * Priority may be marked as asset.priority, asset.rank, or review.priority.
 * Only explicitly accepted records are copied into public deck JSON.
 */
import { existsSync, readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const root = process.cwd();
const home = process.env.HOME || process.env.USERPROFILE || '';
const defaultProfieldRoot = home
  ? `${home}/src/profield/runs/media-prospector`
  : '/Users/ruvebal/src/profield/runs/media-prospector';
const profieldRoot = process.env.PROFIELD_MEDIA_ROOT || defaultProfieldRoot;
const profieldIndex = process.env.PROFIELD_MEDIA_INDEX || null;
const deckRoot = resolve(root, 'docs/tracks/en/uem/2627-dci');

if (!existsSync(profieldRoot)) {
  console.warn(
    `media:rehydrate: skip — Profield media root missing (${profieldRoot}). `
    + 'Keeping committed deck content.json (CI / machines without studio mount).',
  );
  process.exit(0);
}

function filesUnder(directory) {
  if (!existsSync(directory)) return [];
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    return entry.isDirectory() ? filesUnder(path) : (entry.name === 'manifest.json' ? [path] : []);
  });
}

function priority(asset) {
  const value = asset.review_rank ?? asset.review?.priority ?? asset.priority ?? asset.rank ?? 999;
  const number = Number(value);
  return Number.isFinite(number) ? number : 999;
}

function selectionScore(asset) {
  return asset.review_rank != null ? Number(asset.review_rank) : -priority(asset);
}

function publicAsset(asset, slot, existing) {
  return {
    media_slot_id: slot,
    asset_url: asset.asset_url,
    canonical_source_url: asset.canonical_source_url,
    alt_text: asset.accessibility?.alt_text || asset.title || 'Teaching image',
    title: asset.title || asset.name || existing?.title || asset.asset_id,
    provider: asset.provider || asset.source_provider || existing?.provider,
    credit_line: asset.rights?.credit_line,
    licence: asset.rights?.spdx || asset.rights?.class,
    studio_semantics: asset.studio_semantics,
    priority: priority(asset),
    selection_rank: priority(asset),
    collection: asset._collection || 'unit-accepted',
  };
}

function unitFromPath(path, manifest) {
  return manifest.unit_id || path.split('/').at(-3);
}

function slotsFor(unit, content) {
  return content.slides
    .map((slide) => slide.media_slot_id)
    .filter((slot) => slot && slot.startsWith(`${unit}.`) && !slot.includes('.default.'));
}

const manifests = filesUnder(profieldRoot);
const acceptedByUnit = new Map();
let acceptedCount = 0;
const reviewOverrides = new Map();
const reviewIndexPaths = profieldIndex
  ? [profieldIndex]
  : readdirSync(profieldRoot)
    .filter((name) => name.startsWith('media-index') && name.endsWith('.json'))
    .map((name) => join(profieldRoot, name));

for (const reviewIndexPath of reviewIndexPaths) {
if (existsSync(reviewIndexPath)) {
  try {
    const index = JSON.parse(readFileSync(reviewIndexPath, 'utf8'));
    for (const entry of index.queries || []) {
      for (const candidate of entry.candidates || []) {
        if (!candidate.asset_id) continue;
        const incoming = {
          ...candidate,
          review_status: candidate.review_status || '',
          review_rank: candidate.review_rank ?? null,
          review_collections: candidate.review_collections || [],
          review_units: candidate.review_units || [entry.query?.unit_id].filter(Boolean),
        };
        const previous = reviewOverrides.get(candidate.asset_id);
        reviewOverrides.set(candidate.asset_id, previous ? {
          ...previous,
          ...incoming,
          review_status: previous.review_status === 'accepted' || incoming.review_status === 'accepted'
            ? 'accepted' : (previous.review_status || incoming.review_status),
          review_rank: Math.max(previous.review_rank ?? 0, incoming.review_rank ?? 0) || null,
          review_collections: [...new Set([...(previous.review_collections || []), ...(incoming.review_collections || [])])],
          review_units: [...new Set([...(previous.review_units || []), ...(incoming.review_units || [])])],
        } : incoming);
      }
    }
  } catch { /* Keep the reviewed manifests as the safe fallback. */ }
}
}

function reviewStatus(asset) {
  return String(asset.review_status ?? asset.review?.status ?? asset.status ?? '').toLowerCase();
}

function addAccepted(unit, asset, sourcePath, collection) {
  const override = reviewOverrides.get(asset.asset_id) || {};
  const reviewedAsset = { ...asset, ...override };
  const resolvedUnit = unit || reviewedAsset.unit_id || reviewedAsset.collection_query?.unit_id || reviewedAsset.review_units?.[0];
  if (reviewStatus(reviewedAsset) !== 'accepted') return;
  const assetUrl = reviewedAsset.asset_url || reviewedAsset.preview_url;
  const sourceUrl = reviewedAsset.canonical_source_url || reviewedAsset.source;
  if (!assetUrl || !sourceUrl || !resolvedUnit) return;
  acceptedCount += 1;
  const list = acceptedByUnit.get(resolvedUnit) || [];
  list.push({
    ...reviewedAsset,
    asset_url: assetUrl,
    canonical_source_url: sourceUrl,
    _manifest: sourcePath,
    _collection: collection || asset.collection_id || asset.collection || 'unit-accepted',
  });
  acceptedByUnit.set(resolvedUnit, list);
}

const collectionDirectory = join(profieldRoot, 'collections');
if (existsSync(collectionDirectory)) {
  for (const name of readdirSync(collectionDirectory).filter((entry) => entry.endsWith('.json'))) {
    const path = join(collectionDirectory, name);
    let collection;
    try { collection = JSON.parse(readFileSync(path, 'utf8')); } catch { continue; }
    for (const asset of collection.assets || []) addAccepted(asset.unit_id, asset, path, collection.collection_id);
  }
}

for (const path of manifests) {
  let manifest;
  try { manifest = JSON.parse(readFileSync(path, 'utf8')); } catch { continue; }
  const unit = unitFromPath(path, manifest);
  for (const asset of manifest.assets || []) {
    addAccepted(unit, asset, path, manifest.query?.collection || manifest.collection);
  }
}

let processed = 0;
let changed = 0;
for (const unitDirectory of readdirSync(deckRoot, { withFileTypes: true }).filter((entry) => entry.isDirectory())) {
  const unit = unitDirectory.name.startsWith('i-') ? `I.${unitDirectory.name.split('-')[1]}` : null;
  if (!unit) continue;
  const contentPath = join(deckRoot, unitDirectory.name, 'data/content.json');
  if (!existsSync(contentPath)) continue;
  processed += 1;
  let content;
  try { content = JSON.parse(readFileSync(contentPath, 'utf8').replace(/^---[\s\S]*?---\s*/m, '')); } catch { continue; }
  const slots = slotsFor(unit, content);
  const selection = content.media_selection || {};
  const deduped = new Map();
  for (const asset of acceptedByUnit.get(unit) || []) {
    const existing = deduped.get(asset.asset_id);
    if (!existing || selectionScore(asset) > selectionScore(existing)) deduped.set(asset.asset_id, asset);
  }
  for (const [slot, assetId] of Object.entries(selection.media_overrides || {})) {
    const reviewed = reviewOverrides.get(assetId);
    if (!reviewed || reviewStatus(reviewed) !== 'accepted') continue;
    const assetUrl = reviewed.asset_url || reviewed.preview_url;
    const sourceUrl = reviewed.canonical_source_url || reviewed.source;
    if (!assetUrl || !sourceUrl) continue;
    deduped.set(assetId, { ...reviewed, asset_url: assetUrl, canonical_source_url: sourceUrl, _collection: selection.collection || 'unit-accepted', media_slot_id: slot });
  }
  const selected = [...deduped.values()]
    .filter((asset) => !selection.collection || selection.collection === 'unit-accepted' || asset._collection === selection.collection)
    .filter((asset) => !Object.entries(selection.media_overrides || {}).some(([slot, assetId]) => slot === asset.media_slot_id && assetId !== asset.asset_id))
    .sort((a, b) => selectionScore(b) - selectionScore(a) || String(a.asset_id).localeCompare(String(b.asset_id)));
  const assets = selected.map((asset, index) => {
    const existing = (content.assets || []).find((candidate) => candidate.canonical_source_url === asset.canonical_source_url);
    // Reassign the reviewed collection in rank order to distinct slideshow slots.
    // Upstream slot IDs can be stale or duplicated across older deck versions.
    const overrideSlot = Object.entries(selection.media_overrides || {}).find(([, assetId]) => assetId === asset.asset_id)?.[0];
    return publicAsset(asset, overrideSlot || slots[index] || existing?.media_slot_id || asset.media_slot_id || `${unit}.still.profield-${index + 1}`, existing);
  });
  const frontMatter = '---\nlayout: null\n---\n';
  const output = `${frontMatter}${JSON.stringify({ ...content, assets }, null, 2)}\n`;
  if (output !== readFileSync(contentPath, 'utf8')) {
    writeFileSync(contentPath, output, 'utf8');
    changed += 1;
  }
}
console.log(`Media rehydration: scanned ${manifests.length} manifest(s), accepted ${acceptedCount} asset(s), processed ${processed} deck data file(s), changed ${changed}.`);
