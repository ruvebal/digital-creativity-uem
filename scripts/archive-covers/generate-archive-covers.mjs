#!/usr/bin/env node
/**
 * Archive hub hex heroes — Hexaform field + nebula shader (theme palette).
 * Source: docs/_data/archive_covers.manifest.json (URLs excluded from page-art).
 */
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { createHash } from 'node:crypto';

const root = resolve(process.argv[2] || process.cwd());
const brand = process.argv[3] || 'udit';
const docsDir = join(root, 'docs');
const manifestPath = join(docsDir, '_data/archive_covers.manifest.json');
const outDir = join(docsDir, 'assets/images/archive-covers');
const dataPath = join(docsDir, '_data/archive_covers.json');

const palettes = {
	'fe-i': { paper: '#101827', ink: '#F7F2E8', accent: '#FF7A59', accent2: '#54D6BE', accent3: '#F3C969' },
	'fe-ii': { paper: '#191128', ink: '#FBF5ED', accent: '#FF6B3D', accent2: '#A6F4D4', accent3: '#B6A1FF' },
	'dc-i': { paper: '#18141D', ink: '#FFF7EC', accent: '#E8C56C', accent2: '#F07C63', accent3: '#9BE2D1' },
	'dc-ii': { paper: '#121A2E', ink: '#F8F6ED', accent: '#E7FF79', accent2: '#AF89FF', accent3: '#FF82A7' },
};

function hash32(text) {
	let value = 2166136261;
	for (const character of String(text)) {
		value ^= character.charCodeAt(0);
		value = Math.imul(value, 16777619);
	}
	return value >>> 0;
}

function randomFactory(seed) {
	let state = seed >>> 0;
	return () => {
		state += 0x6d2b79f5;
		let value = state;
		value = Math.imul(value ^ (value >>> 15), value | 1);
		value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
		return ((value ^ (value >>> 14)) >>> 0) / 4294967296;
	};
}

function hex(cx, cy, size, attrs) {
	const points = Array.from({ length: 6 }, (_, index) => {
		const angle = (Math.PI / 3) * index - Math.PI / 6;
		return `${(cx + Math.cos(angle) * size).toFixed(2)},${(cy + Math.sin(angle) * size).toFixed(2)}`;
	}).join(' ');
	const attrText = Object.entries(attrs)
		.map(([key, value]) => `${key}="${value}"`)
		.join(' ');
	return `<polygon points="${points}" ${attrText}/>`;
}

function escapeXml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;');
}

function nebulaDefs(id, palette, seed) {
	return `
    <radialGradient id="${id}-neb-a" cx="22%" cy="38%" r="58%">
      <stop offset="0" stop-color="${palette.accent}" stop-opacity="0.42"/>
      <stop offset="1" stop-color="${palette.paper}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="${id}-neb-b" cx="78%" cy="62%" r="52%">
      <stop offset="0" stop-color="${palette.accent2}" stop-opacity="0.38"/>
      <stop offset="1" stop-color="${palette.paper}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="${id}-neb-c" cx="52%" cy="18%" r="44%">
      <stop offset="0" stop-color="${palette.accent3}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="${palette.paper}" stop-opacity="0"/>
    </radialGradient>
    <filter id="${id}-nebula" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.007 0.011" numOctaves="4" seed="${seed % 997}" result="noise"/>
      <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0.12  0 0 0 0 0.08  0 0 0 0 0.22  0 0 0 0.85 0" result="cloud"/>
      <feGaussianBlur in="cloud" stdDeviation="10" result="blur"/>
      <feBlend in="SourceGraphic" in2="blur" mode="screen"/>
    </filter>`;
}

function renderArchiveCover(entry) {
	const palette = palettes[entry.family];
	if (!palette) throw new Error(`Unknown family ${entry.family} for ${entry.url}`);
	const id = entry.asset;
	const seed = hash32(`${entry.url}-${entry.seed || entry.asset}`);
	const random = randomFactory(seed);
	const width = 1600;
	const height = 900;
	const radius = 42;
	const horizontal = Math.sqrt(3) * radius;
	const vertical = radius * 1.5;
	const centreX = 940 + (random() - 0.5) * 120;
	const centreY = 440 + (random() - 0.5) * 70;
	const energy = 0.62;
	const density = 16;
	const scene = [];

	const halos = [520, 390, 285, 195]
		.map((size, index) =>
			hex(centreX, centreY, size, {
				fill: index % 2 ? palette.accent : palette.accent2,
				'fill-opacity': (0.02 + (4 - index) * 0.014).toFixed(3),
				stroke: index % 2 ? palette.accent : palette.accent2,
				'stroke-opacity': (0.03 + (4 - index) * 0.014).toFixed(3),
				'stroke-width': '1.2',
			}),
		)
		.join('');

	for (let row = -1; row < 15; row += 1) {
		for (let column = -1; column < 25; column += 1) {
			const x = column * horizontal + (row % 2 ? horizontal / 2 : 0);
			const y = row * vertical;
			const distance = Math.hypot((x - centreX) / width, (y - centreY) / height);
			const wave = (Math.sin(column * 0.52 + row * 2.75 + seed * 0.013) + 1) / 2;
			const focus = Math.max(0, 1 - distance * 2.1);
			const activation = wave * 0.48 + focus * 0.74 + random() * 0.18;
			if (activation <= 0.34 - energy * 0.08) continue;
			const selected = activation > 0.78 ? 'accent2' : activation > 0.6 ? 'accent' : 'accent3';
			const opacity = (0.035 + activation * 0.17).toFixed(3);
			const scale = (0.16 + activation * 0.42 + energy * 0.09) * radius;
			scene.push(
				hex(x, y, scale, {
					fill: palette[selected],
					'fill-opacity': opacity,
					stroke: palette[selected],
					'stroke-opacity': (Number(opacity) * 1.8).toFixed(3),
					'stroke-width': '1.1',
				}),
			);
		}
	}

	for (let index = 0; index < density; index += 1) {
		const angle = index * 2.399963229728653 + seed * 0.0019;
		const radial = 34 + Math.sqrt(index + 1) * (28 + energy * 55);
		const x = centreX + Math.cos(angle) * radial * 1.14;
		const y = centreY + Math.sin(angle) * radial * 0.67;
		const size = 15 + ((density - index) / density) * (40 + energy * 32) + random() * 9;
		const colour = index % 5 === 0 ? palette.accent3 : index % 2 === 0 ? palette.accent2 : palette.accent;
		scene.push(
			hex(x, y, size, {
				fill: colour,
				'fill-opacity': (0.2 + (density - index) / density * 0.48).toFixed(3),
				stroke: palette.ink,
				'stroke-opacity': '0.12',
				'stroke-width': '1.2',
			}),
		);
	}

	return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title-${id} desc-${id}">
  <title id="title-${id}">${escapeXml(entry.title)}</title>
  <desc id="desc-${id}">${escapeXml(entry.alt || 'Archive hub hex field with nebula shader — no people or brands depicted.')}</desc>
  <defs>
    <linearGradient id="ground-${id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="${palette.paper}"/>
      <stop offset="1" stop-color="#070A11"/>
    </linearGradient>
    <linearGradient id="mark-${id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="${palette.accent}"/>
      <stop offset="0.55" stop-color="${palette.accent2}"/>
      <stop offset="1" stop-color="${palette.accent3}"/>
    </linearGradient>
    ${nebulaDefs(id, palette, seed)}
  </defs>
  <rect width="${width}" height="${height}" fill="url(#ground-${id})"/>
  <rect width="${width}" height="${height}" fill="url(#${id}-neb-a)"/>
  <rect width="${width}" height="${height}" fill="url(#${id}-neb-b)"/>
  <rect width="${width}" height="${height}" fill="url(#${id}-neb-c)"/>
  <rect width="${width}" height="${height}" filter="url(#${id}-nebula)" opacity="0.62"/>
  <g aria-hidden="true">${halos}</g>
  <g aria-hidden="true">${scene.join('')}</g>
  <g aria-hidden="true" transform="translate(98 110)">
    ${hex(0, 0, 15, { fill: `url(#mark-${id})` })}
    ${hex(42, -3, 8, { fill: palette.ink, 'fill-opacity': '0.78' })}
    ${hex(68, -5, 5, { fill: palette.accent3, 'fill-opacity': '0.9' })}
  </g>
</svg>`;
}

const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
const hubs = manifest[brand];
if (!hubs) throw new Error(`No archive hub manifest for brand "${brand}"`);

mkdirSync(outDir, { recursive: true });
const registry = {};

for (const entry of hubs) {
	const asset = entry.asset || `archive-${createHash('sha256').update(entry.url).digest('hex').slice(0, 10)}`;
	const record = { ...entry, asset };
	writeFileSync(join(outDir, `${asset}.svg`), renderArchiveCover(record));
	registry[entry.url] = {
		asset,
		title: entry.title,
		family: entry.family,
		mode: 'archive',
	};
}

writeFileSync(dataPath, `${JSON.stringify(registry, null, '\t')}\n`);
console.log(`Generated ${Object.keys(registry).length} archive covers (${brand}) → ${outDir}`);
