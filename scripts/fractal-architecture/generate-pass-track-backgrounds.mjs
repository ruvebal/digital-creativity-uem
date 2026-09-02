#!/usr/bin/env node

import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { basename, dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const GENERATOR_VERSION = '1.4.0';

const [glossaryArg, outputArg, privateGlossaryArg, proofArg, archiveArg, originalRootArg, brandArg] = process.argv.slice(2);
if (!glossaryArg || !outputArg || !privateGlossaryArg || !proofArg || !archiveArg || !originalRootArg || !['udit', 'uem'].includes(brandArg)) {
  throw new Error('Usage: generate-pass-track-backgrounds.mjs <public-glossary.json> <delivery-dir> <private-glossary.json> <private-proof.json> <archive-root> <original-root> <udit|uem>');
}

const glossaryPath = resolve(glossaryArg);
const outputDir = resolve(outputArg);
const proofPath = resolve(proofArg);
const archiveRoot = resolve(archiveArg);
const originalRoot = resolve(originalRootArg);
const publicIndexPath = join(outputDir, 'index.json');
const captionManifestDir = join(outputDir, 'caption-manifests');
const currentCaptionPath = join(outputDir, 'figcaption-data.json');
const citationPath = join(dirname(proofPath), 'formula-citation.public.json');
const glossaryBytes = readFileSync(glossaryPath);
const glossary = JSON.parse(glossaryBytes.toString('utf8'));
const canonicalLatex = 'p_c(z)=z^2+c,\\quad c\\in\\mathbb{C}';
const formula = glossary.entries?.find((entry) => entry.latex === canonicalLatex);
let privateAnchor = null;

if (glossary.public_safe !== true) throw new Error('Formula glossary is not public-safe.');
if (!formula) throw new Error(`Verified recurrence not found: ${canonicalLatex}`);
if (formula.fidelity_status !== 'EXACT') throw new Error('Recurrence must be EXACT.');
if (!formula.mathml?.startsWith('<math')) throw new Error('Verified MathML is required.');

if (!existsSync(citationPath)) throw new Error(`Evaluator-safe citation contract is required: ${citationPath}`);
const citation = JSON.parse(readFileSync(citationPath, 'utf8'));
if (citation.formula_id !== formula.formula_id || citation.evaluator_safe !== true || citation.style !== 'chicago-author-date') {
  throw new Error('Citation contract must match the formula and be evaluator-safe Chicago author-date.');
}

if (privateGlossaryArg) {
  const privateGlossary = JSON.parse(readFileSync(resolve(privateGlossaryArg), 'utf8'));
  const privateFormula = privateGlossary.entries?.find((entry) => entry.latex === canonicalLatex);
  if (!privateFormula || privateFormula.fidelity_status !== formula.fidelity_status) {
    throw new Error('Private/public formula join failed.');
  }
  const occurrence = privateGlossary.occurrences?.find((item) => item.formula_id === privateFormula.formula_id);
  if (!occurrence?.crop_sha256 || !Number.isInteger(occurrence.page_index)) {
    throw new Error('Private formula occurrence lacks page/crop proof.');
  }
  privateAnchor = {
    formula_id: privateFormula.formula_id,
    document_id: occurrence.document_id,
    node_id: occurrence.node_id,
    page_index: occurrence.page_index,
    printed_page: occurrence.printed_page,
    crop_relpath: occurrence.crop_relpath,
    crop_sha256: occurrence.crop_sha256,
    audit_notes: occurrence.audit_notes,
  };
}

mkdirSync(outputDir, { recursive: true });
mkdirSync(dirname(proofPath), { recursive: true });

const families = [
  { key: 'structure', c: [-0.745, 0.113], phase: 0.13, density: 0.92 },
  { key: 'threshold', c: [-0.8, 0.156], phase: 0.27, density: 1.05 },
  { key: 'branching', c: [-0.123, 0.745], phase: 0.41, density: 0.82 },
  { key: 'practice', c: [0.285, 0.01], phase: 0.56, density: 0.96 },
  { key: 'feedback', c: [-0.4, 0.6], phase: 0.72, density: 0.88 },
  { key: 'coherence', c: [-0.835, -0.2321], phase: 0.89, density: 1.0 },
];

const brands = {
  udit: { background: '#0f172a', primary: '#3b82f6', accent: '#10b981', tertiary: '#8b5cf6' },
  uem: { background: '#0f172a', primary: '#ff3b30', accent: '#00d4ff', tertiary: '#a855f7' },
};

function mulberry32(seed) {
  let state = seed >>> 0;
  return () => {
    state += 0x6d2b79f5;
    let value = state;
    value = Math.imul(value ^ (value >>> 15), value | 1);
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
    return ((value ^ (value >>> 14)) >>> 0) / 4294967296;
  };
}

function hashSeed(text) {
  return Number.parseInt(createHash('sha256').update(text).digest('hex').slice(0, 8), 16);
}

function sha256(value) {
  return createHash('sha256').update(value).digest('hex');
}

function uuidFromHash(value) {
  const hash = sha256(value);
  return `${hash.slice(0, 8)}-${hash.slice(8, 12)}-5${hash.slice(13, 16)}-${((Number.parseInt(hash.slice(16, 18), 16) & 0x3f) | 0x80).toString(16)}${hash.slice(18, 20)}-${hash.slice(20, 32)}`;
}

function writeImmutable(path, bytes) {
  if (existsSync(path)) {
    if (sha256(readFileSync(path)) !== sha256(bytes)) throw new Error(`Immutable asset collision: ${path}`);
    return;
  }
  writeFileSync(path, bytes);
}

function copyImmutable(source, destination) {
  if (existsSync(destination)) {
    if (sha256(readFileSync(source)) !== sha256(readFileSync(destination))) {
      throw new Error(`Immutable delivery collision: ${destination}`);
    }
    return;
  }
  copyFileSync(source, destination);
}

function polygonPoints(cx, cy, radius, sides, rotation) {
  return Array.from({ length: sides }, (_, index) => {
    const angle = rotation + (Math.PI * 2 * index) / sides;
    return `${(cx + Math.cos(angle) * radius).toFixed(2)},${(cy + Math.sin(angle) * radius).toFixed(2)}`;
  }).join(' ');
}

function iterateJulia(x0, y0, cReal, cImag, maxIterations) {
  let x = x0;
  let y = y0;
  for (let iteration = 0; iteration < maxIterations; iteration += 1) {
    const xx = x * x - y * y + cReal;
    const yy = 2 * x * y + cImag;
    x = xx;
    y = yy;
    if (x * x + y * y > 4) return iteration;
  }
  return maxIterations;
}

function fractalField(family, palette) {
  const [cReal, cImag] = family.c;
  const cells = [];
  const cols = 108;
  const rows = 62;
  const cellWidth = 1600 / cols;
  const cellHeight = 900 / rows;
  const maxIterations = Math.round(58 * family.density);

  for (let row = 0; row < rows; row += 1) {
    for (let col = 0; col < cols; col += 1) {
      const screenX = col / (cols - 1);
      const screenY = row / (rows - 1);
      const planeX = (screenX - 0.54) * 3.25;
      const planeY = (screenY - 0.5) * 2.15;
      const escapeAt = iterateJulia(planeX, planeY, cReal, cImag, maxIterations);
      if (escapeAt >= maxIterations) continue;

      const edge = escapeAt / maxIterations;
      if (edge < 0.12 || edge > 0.97) continue;
      const color = edge < 0.42 ? palette.primary : edge < 0.72 ? palette.accent : palette.tertiary;
      const rightBias = 0.68 + screenX * 0.36;
      const opacity = ((0.08 + edge * 0.42) * rightBias).toFixed(3);
      cells.push(`<rect x="${(col * cellWidth).toFixed(2)}" y="${(row * cellHeight).toFixed(2)}" width="${(cellWidth + 0.85).toFixed(2)}" height="${(cellHeight + 0.85).toFixed(2)}" fill="${color}" opacity="${opacity}"/>`);
    }
  }

  return cells.join('');
}

function nebulaDefs(id, palette, seed) {
  return `
    <radialGradient id="${id}-neb-a" cx="18%" cy="34%" r="62%"><stop offset="0" stop-color="${palette.primary}" stop-opacity="0.48"/><stop offset="1" stop-color="${palette.background}" stop-opacity="0"/></radialGradient>
    <radialGradient id="${id}-neb-b" cx="82%" cy="68%" r="56%"><stop offset="0" stop-color="${palette.accent}" stop-opacity="0.42"/><stop offset="1" stop-color="${palette.background}" stop-opacity="0"/></radialGradient>
    <radialGradient id="${id}-neb-c" cx="54%" cy="12%" r="48%"><stop offset="0" stop-color="${palette.tertiary}" stop-opacity="0.34"/><stop offset="1" stop-color="${palette.background}" stop-opacity="0"/></radialGradient>
    <filter id="${id}-nebula" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.006 0.01" numOctaves="4" seed="${seed % 997}" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0.14  0 0 0 0 0.1  0 0 0 0 0.28  0 0 0 0.9 0" result="cloud"/>
      <feGaussianBlur in="cloud" stdDeviation="11" result="blur"/>
      <feBlend in="SourceGraphic" in2="blur" mode="screen"/>
    </filter>`;
}

function renderSvg(brandKey, family, familyIndex) {
  const palette = brands[brandKey];
  const seed = hashSeed(`${brandKey}:${family.key}:julia-geometric-v1`);
  const id = `${brandKey}-pass-${String(familyIndex + 1).padStart(2, '0')}-${family.key}`;
  const random = mulberry32(seed);

  const accents = [];
  for (let depth = 0; depth < 5; depth += 1) {
    const radius = 280 * 0.74 ** depth;
    const cx = 1290 - depth * 38;
    const cy = 445 + Math.sin(family.phase * Math.PI * 2 + depth) * 36;
    const color = depth % 2 ? palette.accent : palette.primary;
    accents.push(`<polygon points="${polygonPoints(cx, cy, radius, 6, family.phase * Math.PI + depth * 0.17)}" fill="none" stroke="${color}" stroke-width="${Math.max(0.7, 2.2 - depth * 0.24).toFixed(2)}" opacity="${(0.22 - depth * 0.02).toFixed(3)}"/>`);
  }
  for (let index = 0; index < 18; index += 1) {
    const cx = 760 + random() * 760;
    const cy = 80 + random() * 740;
    const radius = 2.4 + random() * 4.2;
    const sides = 3 + (index % 4);
    const color = index % 3 === 0 ? palette.primary : index % 3 === 1 ? palette.accent : palette.tertiary;
    accents.push(`<polygon points="${polygonPoints(cx, cy, radius, sides, family.phase * Math.PI + random() * 0.35)}" fill="none" stroke="${color}" stroke-width="0.85" opacity="${(0.08 + random() * 0.14).toFixed(3)}"/>`);
  }

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" width="1600" height="900" role="img" aria-labelledby="title desc">
  <title id="title">Julia pass-track backdrop</title>
  <desc id="desc">A text-free Julia-set field sampled from p_c(z)=z²+c, with low-contrast rhythmic geometric accents.</desc>
  <defs>
    ${nebulaDefs(id, palette, seed)}
    <linearGradient id="${id}-veil" x1="0" x2="1"><stop offset="0" stop-color="${palette.background}" stop-opacity="0.98"/><stop offset="0.42" stop-color="${palette.background}" stop-opacity="0.88"/><stop offset="1" stop-color="${palette.background}" stop-opacity="0.24"/></linearGradient>
    <filter id="${id}-glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>
  <rect width="1600" height="900" fill="${palette.background}"/>
  <rect width="1600" height="900" fill="url(#${id}-neb-a)"/>
  <rect width="1600" height="900" fill="url(#${id}-neb-b)"/>
  <rect width="1600" height="900" fill="url(#${id}-neb-c)"/>
  <rect width="1600" height="900" filter="url(#${id}-nebula)" opacity="0.58"/>
  <g opacity="1">${fractalField(family, palette)}</g>
  <g filter="url(#${id}-glow)" opacity="0.72">${accents.slice(0, 2).join('')}</g>
  <g opacity="0.88">${accents.join('')}</g>
  <rect width="1600" height="900" fill="url(#${id}-veil)"/>
</svg>`;
}

const outputs = [];
for (const brandKey of [brandArg]) {
  for (const [familyIndex, family] of families.entries()) {
    const svg = renderSvg(brandKey, family, familyIndex);
    const svgSha256 = sha256(svg);
    const stem = `${brandKey}-pass-${String(familyIndex + 1).padStart(2, '0')}-${family.key}-${svgSha256.slice(0, 12)}`;
    const fileName = `${stem}.svg`;
    const pngName = `${stem}.png`;
    outputs.push({ svg, file: fileName, png: pngName, sha256: svgSha256, brand: brandKey, family: family.key, seed: hashSeed(`${brandKey}:${family.key}:julia-geometric-v1`), backdrop: 'julia-geometric-v1', viewport: [1600, 900], title_safe_region: { x: 0, y: 0, width: 690, height: 900 } });
  }
}

const publicStack = [
  { kind: 'skill', name: 'curriculum-forger', version: '1.1.0' },
  { kind: 'skill', name: 'visual-forger', version: '1.1.0' },
  { kind: 'agent+skill', name: 'fractal-architect', version: '1.2.1' },
  { kind: 'renderer', name: 'pass-track-backgrounds', version: GENERATOR_VERSION },
];
const releaseId = createHash('sha256')
  .update(JSON.stringify({ brand: brandArg, formula: canonicalLatex, outputs: outputs.map((item) => item.sha256), stack: publicStack }))
  .digest('hex')
  .slice(0, 16);
const existingCaptionPath = join(captionManifestDir, `${releaseId}.json`);
const createdAt = existsSync(existingCaptionPath)
  ? JSON.parse(readFileSync(existingCaptionPath, 'utf8')).created_at
  : new Date().toISOString();
if (!createdAt || Number.isNaN(Date.parse(createdAt))) throw new Error(`Invalid existing release date: ${existingCaptionPath}`);
const originalReleaseDir = join(originalRoot, `release-${releaseId}`);
mkdirSync(originalReleaseDir, { recursive: true });
for (const output of outputs) {
  const originalSvgPath = join(originalReleaseDir, output.file);
  const originalPngPath = join(originalReleaseDir, output.png);
  writeImmutable(originalSvgPath, output.svg);
  if (!existsSync(originalPngPath)) {
    const raster = spawnSync('rsvg-convert', ['-w', '1600', '-h', '900', '-o', originalPngPath, originalSvgPath], { encoding: 'utf8' });
    if (raster.status !== 0) throw new Error(`PNG export failed for ${output.file}: ${raster.stderr || raster.stdout}`);
  }
  copyImmutable(originalSvgPath, join(outputDir, output.file));
  copyImmutable(originalPngPath, join(outputDir, output.png));
  output.png_sha256 = sha256(readFileSync(originalPngPath));
  output.uuid = uuidFromHash(`fractal-asset:${output.sha256}`);
  output.original_paths = { svg: originalSvgPath, png: originalPngPath };
}

const formulaRecord = {
  uuid: formula.formula_id,
  fractal_hash256: sha256(canonicalLatex),
  title: 'Complex quadratic Julia recurrence',
  display: 'p_c(z) = z² + c, c ∈ C',
  latex: canonicalLatex,
  mathml: formula.mathml,
  basic_explanation: 'For each pixel, the complex value z is repeatedly squared and shifted by the fixed complex parameter c. Escape speed controls the visible Julia field.',
  citation: { inline: citation.inline, chicago: citation.chicago },
};
const figcaptionManifest = {
  schema_version: '1.0.0',
  kind: 'fractal-architect.figcaption-data',
  release_id: releaseId,
  created_at: createdAt,
  authorship: { name: 'Ruvebal', email: 'ruvebal@crea-comm.net' },
  formulae: [formulaRecord],
  figures: outputs.map((output) => ({
    uuid: output.uuid,
    title: `Julia recurrence backdrop: ${output.family}`,
    description: `A ${output.family} variation of a Julia-set field with rhythmic geometric accents.`,
    figcaption: `Julia recurrence backdrop. ${formulaRecord.display}. ${formulaRecord.basic_explanation} ${citation.inline}.`,
    fractal_hash256: output.sha256,
    created_at: createdAt,
    authorship: { name: 'Ruvebal', email: 'ruvebal@crea-comm.net' },
    formulae: [formulaRecord],
    delivery: { svg: output.file, png: output.png, svg_sha256: output.sha256, png_sha256: output.png_sha256 },
  })),
};
mkdirSync(captionManifestDir, { recursive: true });
const captionManifestPath = existingCaptionPath;
writeImmutable(captionManifestPath, `${JSON.stringify(figcaptionManifest, null, 2)}\n`);
writeFileSync(currentCaptionPath, `${JSON.stringify(figcaptionManifest, null, 2)}\n`);
const priorIndex = existsSync(publicIndexPath)
  ? JSON.parse(readFileSync(publicIndexPath, 'utf8'))
  : { schema_version: 1, releases: [] };
const release = {
  release_id: releaseId,
  created_at: createdAt,
  brand: brandArg,
  formula: { text: 'p_c(z)=z²+c', latex: canonicalLatex, fidelity_status: formula.fidelity_status },
  caption: {
    source: citation.chicago,
    source_evaluator_safe: true,
    credit: 'Image by @ruvebal with curriculum-forger 1.1.0, visual-forger 1.1.0, fractal-architect 1.2.0, and pass-track-backgrounds 1.4.0.',
  },
  figcaption_manifest: `caption-manifests/${releaseId}.json`,
  studio_stack: publicStack,
  assets: outputs.map(({ file, png, sha256, png_sha256, family, uuid }) => ({ family, uuid, svg: file, png, sha256, png_sha256 })),
};
const releases = Array.isArray(priorIndex.releases) ? priorIndex.releases : [];
if (!releases.some((item) => item.release_id === releaseId)) releases.push(release);
const publicIndex = { schema_version: 1, current_release: releaseId, releases };
writeFileSync(publicIndexPath, `${JSON.stringify(publicIndex, null, 2)}\n`);

function stackReceipt(kind, name, version, path, suppliedSha256 = null) {
  const absolutePath = resolve(path);
  if (!existsSync(absolutePath)) {
    if (!suppliedSha256) throw new Error(`Version receipt source unavailable: ${absolutePath}`);
    return { kind, name, version, path: null, sha256: suppliedSha256, git_commit: null };
  }
  const bytes = readFileSync(absolutePath);
  const git = spawnSync('git', ['-C', dirname(absolutePath), 'rev-parse', 'HEAD'], { encoding: 'utf8' });
  return {
    kind,
    name,
    version,
    path: absolutePath,
    sha256: createHash('sha256').update(bytes).digest('hex'),
    git_commit: git.status === 0 ? git.stdout.trim() : null,
  };
}

const privateStack = [
  stackReceipt('skill', 'curriculum-forger', '1.1.0', process.env.CURRICULUM_FORGER_SKILL || '/Users/ruvebal/src/.cursor/skills/curriculum-forger/SKILL.md'),
  stackReceipt('skill', 'visual-forger', '1.1.0', process.env.VISUAL_FORGER_SKILL || '/Users/ruvebal/src/.cursor/skills/visual-forger/SKILL.md'),
  stackReceipt('skill', 'fractal-architect', '1.2.1', process.env.FRACTAL_ARCHITECT_SKILL || 'digital-creativity-pedagogy/.cursor/skills/fractal-architect/SKILL.md', process.env.FRACTAL_ARCHITECT_SKILL_SHA256),
  stackReceipt('agent', 'fractal-architect', '1.2.0', process.env.FRACTAL_ARCHITECT_AGENT || 'digital-creativity-pedagogy/.cursor/agents/fractal-architect.md', process.env.FRACTAL_ARCHITECT_AGENT_SHA256),
  stackReceipt('renderer', 'pass-track-backgrounds', GENERATOR_VERSION, fileURLToPath(import.meta.url)),
];

function buildSemanticIndex(manifest) {
  if (process.env.FRACTAL_OLLAMA_INDEX_DISABLED === 'yes') {
    return { provider: 'ollama', status: 'disabled-by-request', model: null, releases: [] };
  }

  const model = process.env.FRACTAL_OLLAMA_MODEL || 'nomic-embed-text:latest';
  const records = manifest.figures.map((figure) => {
    const searchText = [figure.title, figure.description, figure.formulae[0].display, figure.formulae[0].basic_explanation].join(' ');
    const embedding = spawnSync('ollama', ['run', model, searchText], { encoding: 'utf8' });
    if (embedding.status !== 0) throw new Error(`Ollama semantic index failed for ${figure.uuid}: ${embedding.stderr || embedding.stdout}`);
    let vector;
    try {
      vector = JSON.parse(embedding.stdout.trim());
    } catch {
      throw new Error(`Ollama semantic index returned a non-vector response for ${figure.uuid}`);
    }
    if (!Array.isArray(vector) || vector.length === 0 || !vector.every(Number.isFinite)) {
      throw new Error(`Ollama semantic index returned an invalid vector for ${figure.uuid}`);
    }
    return { figure_uuid: figure.uuid, text_sha256: sha256(searchText), dimensions: vector.length, vector };
  });

  return { provider: 'ollama', status: 'ready', model, release_id: manifest.release_id, records };
}

const semanticIndexPath = join(dirname(proofPath), 'fractal-art-semantic-index.private.json');
const priorSemanticIndex = existsSync(semanticIndexPath)
  ? JSON.parse(readFileSync(semanticIndexPath, 'utf8'))
  : { schema_version: '1.0.0', kind: 'fractal-architect.semantic-index', releases: [] };
const semanticRelease = buildSemanticIndex(figcaptionManifest);
if (semanticRelease.status === 'ready' && !priorSemanticIndex.releases.some((item) => item.release_id === releaseId)) {
  priorSemanticIndex.releases.push(semanticRelease);
}
priorSemanticIndex.current_release = releaseId;
priorSemanticIndex.updated_at = createdAt;
writeFileSync(semanticIndexPath, `${JSON.stringify(priorSemanticIndex, null, 2)}\n`);

const proof = {
  status: 'FORMULA_CONSUMED',
  source_export: basename(glossaryPath),
  source_export_sha256: createHash('sha256').update(glossaryBytes).digest('hex'),
  formula_contract: { latex: formula.latex, mathml: formula.mathml, fidelity_status: formula.fidelity_status, adapter: 'complex-quadratic-v1' },
  private_reference_anchor: privateAnchor,
  release_id: releaseId,
  studio_stack: privateStack,
  original_release_dir: originalReleaseDir,
  public_caption_manifest: join('caption-manifests', `${releaseId}.json`),
  semantic_index: {
    provider: semanticRelease.provider,
    status: semanticRelease.status,
    model: semanticRelease.model,
    path: semanticIndexPath,
  },
  public_asset_policy: 'No corpus or local-architecture metadata is embedded in SVG/PNG outputs.',
  outputs: outputs.map(({ svg, ...output }) => output),
};

const immutableProofPath = join(dirname(proofPath), `formula-consumption-proof-${releaseId}.private.json`);
writeImmutable(immutableProofPath, `${JSON.stringify(proof, null, 2)}\n`);
writeFileSync(proofPath, `${JSON.stringify(proof, null, 2)}\n`);
console.log(`Generated ${outputs.length} deterministic SVG backgrounds in ${outputDir}`);
console.log(`Release index: ${publicIndexPath} · current=${releaseId}`);
console.log(`Formula gate: ${formula.fidelity_status} · adapter: ${proof.formula_contract.adapter}`);
console.log(`Originals retained in ${originalReleaseDir}; immutable copies delivered to ${outputDir}.`);
