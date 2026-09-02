#!/usr/bin/env node
/**
 * Hexaform cover generator
 *
 * Source of truth: docs/_data/lesson_covers.json
 * Output: docs/assets/images/lesson-covers/<cover-id>.{svg,png}
 *
 * The generator intentionally makes no bodies, faces, garments, brands, or
 * student artefacts. A record's master idea becomes a deterministic field of
 * hexagons through its mode, density, energy, and seed.
 */

import { copyFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';

const projectRoot = process.cwd();
const dataPath = resolve(projectRoot, process.argv[2] || 'docs/_data/lesson_covers.json');
const outputDir = resolve(projectRoot, process.argv[3] || 'docs/assets/images/lesson-covers');
const covers = JSON.parse(readFileSync(dataPath, 'utf8'));
const archiveStamp = new Date().toISOString().replaceAll(':', '').replaceAll('.', '-');
const archiveRoot = resolve(projectRoot, process.env.LESSON_COVER_ARCHIVE_DIR || process.argv[4] || 'digital-creativity-pedagogy/archives/lesson-covers');
const archiveDir = resolve(archiveRoot, archiveStamp);
const archivedPaths = new Set();

const palettes = {
	'fe-i': {
		paper: '#101827',
		ink: '#F7F2E8',
		accent: '#FF7A59',
		accent2: '#54D6BE',
		accent3: '#F3C969',
	},
	'fe-ii': {
		paper: '#191128',
		ink: '#FBF5ED',
		accent: '#FF6B3D',
		accent2: '#A6F4D4',
		accent3: '#B6A1FF',
	},
	'dc-i': {
		paper: '#18141D',
		ink: '#FFF7EC',
		accent: '#E8C56C',
		accent2: '#F07C63',
		accent3: '#9BE2D1',
	},
	'dc-ii': {
		paper: '#121A2E',
		ink: '#F8F6ED',
		accent: '#E7FF79',
		accent2: '#AF89FF',
		accent3: '#FF82A7',
	},
};

const modeProfile = {
	lattice: [1.4, 0.25, 0.12],
	constellation: [1.62, 0.62, 0.36],
	archive: [0.72, 0.55, 0.34],
	contract: [1.18, 0.32, 0.22],
	spectrum: [0.88, 0.7, 0.48],
	field: [1.55, 0.42, 0.38],
	state: [1.02, 0.82, 0.25],
	signal: [1.8, 0.45, 0.52],
	boundary: [0.95, 0.68, 0.17],
	motion: [1.7, 0.72, 0.5],
	transform: [1.3, 0.9, 0.44],
	space: [0.78, 0.35, 0.6],
	material: [0.66, 0.48, 0.64],
	identity: [1.08, 0.75, 0.35],
	path: [1.5, 0.67, 0.42],
	sequence: [1.86, 0.58, 0.31],
	portal: [0.78, 0.92, 0.56],
	risk: [1.16, 0.86, 0.29],
	review: [1.03, 0.58, 0.18],
	scene: [1.35, 0.52, 0.73],
	shader: [1.92, 0.94, 0.68],
	membrane: [1.2, 0.88, 0.39],
	evidence: [0.92, 0.6, 0.27],
	defence: [1.06, 0.72, 0.45],
	judgment: [1.24, 0.44, 0.2],
	budget: [0.96, 0.5, 0.3],
};

const fieldLensByMode = {
	lattice: 'System grid',
	constellation: 'Relations map',
	archive: 'Provenance field',
	contract: 'Learning contract',
	spectrum: 'Perceptual code',
	field: 'Practice field',
	state: 'State model',
	signal: 'Signal flow',
	boundary: 'Boundary condition',
	motion: 'Temporal rhythm',
	transform: 'Semantic transformation',
	space: 'Spatial literacy',
	material: 'Material behaviour',
	identity: 'Representation system',
	path: 'Audience journey',
	sequence: 'Narrative sequence',
	portal: 'Access threshold',
	risk: 'Risk surface',
	review: 'Accountability loop',
	scene: 'Experience staging',
	shader: 'Per-frame aesthetics',
	membrane: 'Interface membrane',
	evidence: 'Inspectable evidence',
	defence: 'Defensible decision',
	judgment: 'Critical judgment',
	budget: 'Cost budget',
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
	let state = (seed >>> 0) || 1;
	return () => {
		state += 0x6d2b79f5;
		let result = state;
		result = Math.imul(result ^ (result >>> 15), result | 1);
		result ^= result + Math.imul(result ^ (result >>> 7), result | 61);
		return ((result ^ (result >>> 14)) >>> 0) / 4294967296;
	};
}

function escapeXml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;')
		.replaceAll("'", '&apos;');
}

function hexPoints(cx, cy, radius, rotation = 0) {
	return Array.from({ length: 6 }, (_, index) => {
		const angle = rotation + Math.PI / 3 * index;
		return `${(cx + Math.cos(angle) * radius).toFixed(2)},${(cy + Math.sin(angle) * radius).toFixed(2)}`;
	}).join(' ');
}

function hex(cx, cy, radius, attributes = {}) {
	const attrs = Object.entries(attributes)
		.map(([key, value]) => `${key}="${value}"`)
		.join(' ');
	return `<polygon points="${hexPoints(cx, cy, radius, Math.PI / 6)}" ${attrs}/>`;
}

function svgAttributes(attributes = {}) {
	return Object.entries(attributes)
		.map(([key, value]) => `${key}="${value}"`)
		.join(' ');
}

function rect(x, y, width, height, attributes = {}) {
	return `<rect x="${x}" y="${y}" width="${width}" height="${height}" ${svgAttributes(attributes)}/>`;
}

function circle(cx, cy, radius, attributes = {}) {
	return `<circle cx="${cx}" cy="${cy}" r="${radius}" ${svgAttributes(attributes)}/>`;
}

function line(x1, y1, x2, y2, attributes = {}) {
	return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" ${svgAttributes(attributes)}/>`;
}

function path(d, attributes = {}) {
	return `<path d="${d}" ${svgAttributes(attributes)}/>`;
}

function polyline(points, attributes = {}) {
	return `<polyline points="${points}" ${svgAttributes(attributes)}/>`;
}

function semanticAsset(cover) {
	return cover.semantic_asset || `${cover.asset}-semantic`;
}

function outcomeAsset(cover) {
	return cover.outcome?.asset || `${cover.asset}-outcome`;
}

function wrapWords(value, maxLineLength) {
	const words = String(value).split(/\s+/).filter(Boolean);
	const lines = [];
	let line = '';
	for (const word of words) {
		const next = line ? `${line} ${word}` : word;
		if (next.length > maxLineLength && line) {
			lines.push(line);
			line = word;
		} else {
			line = next;
		}
	}
	if (line) lines.push(line);
	return lines.slice(0, 3);
}

function multilineText(lines, x, y, attributes = {}) {
	const attrs = Object.entries(attributes)
		.map(([key, value]) => `${key}="${value}"`)
		.join(' ');
	const startY = y - (lines.length - 1) * 18;
	const tspans = lines
		.map((line, index) => `<tspan x="${x}" y="${startY + index * 36}">${escapeXml(line)}</tspan>`)
		.join('');
	return `<text ${attrs}>${tspans}</text>`;
}

function estimateTextWidth(text, fontSize) {
	return String(text).length * fontSize * 0.56;
}

function textFitsInsideHex(lines, radius, fontSize) {
	const maxWidth = radius * 1.46;
	const maxHeight = radius * 0.74;
	const textHeight = lines.length * fontSize * 1.18;
	const longestLine = lines.reduce((longest, line) => Math.max(longest, estimateTextWidth(line, fontSize)), 0);
	return lines.length <= 2 && textHeight <= maxHeight && longestLine <= maxWidth;
}

function semanticValueText(label, lines, fontSize, labelFill, palette) {
	if (textFitsInsideHex(lines, label.size, fontSize)) {
		return multilineText(lines, 0, 26, {
			'text-anchor': 'middle',
			fill: labelFill,
			'font-family': 'Inter, ui-sans-serif, system-ui, sans-serif',
			'font-size': fontSize,
			'font-weight': '400',
		});
	}

	const placement = label.size <= 80 ? 'above' : label.y < 220 ? 'below' : 'above';
	const y = placement === 'below' ? label.size + 64 : -(label.size + 46);
	const boxWidth = Math.min(430, Math.max(260, lines.reduce((longest, line) => Math.max(longest, estimateTextWidth(line, fontSize)), 0) + 56));
	const boxHeight = lines.length * 34 + 32;
	const boxY = y - boxHeight / 2 - 5;
	const textY = y - (lines.length - 1) * 17;
	const panelFill = label.key === 'EVIDENCE' ? palette.ink : palette.paper;
	const panelText = label.key === 'EVIDENCE' ? palette.paper : palette.ink;

	return `<g class="semantic-callout semantic-callout--${placement}">
    <rect x="${(-boxWidth / 2).toFixed(2)}" y="${boxY.toFixed(2)}" width="${boxWidth.toFixed(2)}" height="${boxHeight.toFixed(2)}" rx="18" fill="${panelFill}" fill-opacity="0.88" stroke="${label.colour}" stroke-opacity="0.78" stroke-width="1.4"/>
    ${multilineText(lines, 0, textY, { 'text-anchor': 'middle', fill: panelText, 'font-family': 'Inter, ui-sans-serif, system-ui, sans-serif', 'font-size': fontSize, 'font-weight': '400' })}
  </g>`;
}

function renderCover(id, cover) {
	const palette = palettes[cover.family];
	if (!palette) throw new Error(`Unknown cover family "${cover.family}" for ${id}`);

	const [frequency, drift, pulse] = modeProfile[cover.mode] || modeProfile.lattice;
	const random = randomFactory(hash32(`${cover.seed}-${id}-${cover.mode}`));
	const width = 1600;
	const height = 900;
	const radius = 42;
	const horizontal = Math.sqrt(3) * radius;
	const vertical = radius * 1.5;
	const centreX = 940 + (random() - 0.5) * 120;
	const centreY = 440 + (random() - 0.5) * 70;
	const energy = Math.max(0.1, Math.min(1, Number(cover.energy ?? 0.5)));
	const density = Math.max(5, Math.min(28, Number(cover.density ?? 14)));
	const scene = [];
	const halos = [520, 390, 285, 195]
		.map((size, index) =>
			hex(centreX, centreY, size, {
				fill: index % 2 ? palette.accent : palette.accent2,
				'fill-opacity': (0.015 + (4 - index) * 0.012).toFixed(3),
				stroke: index % 2 ? palette.accent : palette.accent2,
				'stroke-opacity': (0.025 + (4 - index) * 0.012).toFixed(3),
				'stroke-width': '1.2',
			}),
		)
		.join('');

	for (let row = -1; row < 15; row += 1) {
		for (let column = -1; column < 25; column += 1) {
			const x = column * horizontal + (row % 2 ? horizontal / 2 : 0);
			const y = row * vertical;
			const distance = Math.hypot((x - centreX) / width, (y - centreY) / height);
			const wave = (Math.sin(column * frequency * 0.72 + row * drift * 5 + cover.seed * 0.013) + 1) / 2;
			const focus = Math.max(0, 1 - distance * 2.1);
			const activation = wave * 0.48 + focus * 0.74 + random() * 0.18;
			const visible = activation > 0.37 - energy * 0.08;
			if (!visible) continue;
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
		const angle = index * 2.399963229728653 + cover.seed * 0.0019;
		const radial = 34 + Math.sqrt(index + 1) * (28 + energy * 55);
		const x = centreX + Math.cos(angle) * radial * (1 + drift * 0.36);
		const y = centreY + Math.sin(angle) * radial * (0.67 + pulse * 0.47);
		const size = 15 + (density - index) / density * (40 + energy * 32) + random() * 9;
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

	const alt = cover.alt_en || cover.master_idea;
	return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title-${id} desc-${id}">
  <title id="title-${id}">${escapeXml(cover.course)} · ${escapeXml(cover.index)}</title>
  <desc id="desc-${id}">${escapeXml(alt)}</desc>
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
  </defs>
  <rect width="${width}" height="${height}" fill="url(#ground-${id})"/>
  <g aria-hidden="true">${halos}</g>
  <g aria-hidden="true">${scene.join('')}</g>
  <g aria-hidden="true" transform="translate(98 110)">
    ${hex(0, 0, 15, { fill: 'url(#mark-' + id + ')' })}
    ${hex(42, 0, 9, { fill: palette.ink, 'fill-opacity': '0.78' })}
    ${hex(68, 0, 5, { fill: palette.accent3, 'fill-opacity': '0.9' })}
  </g>
</svg>`;
}

function renderSemanticGraphic(id, cover) {
	const palette = palettes[cover.family];
	if (!palette) throw new Error(`Unknown cover family "${cover.family}" for ${id}`);

	const [frequency, drift, pulse] = modeProfile[cover.mode] || modeProfile.lattice;
	const random = randomFactory(hash32(`semantic-${cover.seed}-${id}-${cover.mode}`));
	const width = 1600;
	const height = 560;
	const centreY = height / 2;
	const lens = cover.field_lens || fieldLensByMode[cover.mode] || 'Field lens';
	const idea = cover.master_idea || 'Master idea';
	const alt = cover.semantic_alt_en || `Semantic hexagonal diagram linking the master idea "${idea}" with the field lens "${lens}".`;
	const nodes = [];
	const connectors = [];
	const labels = [
		{ key: 'MASTER IDEA', value: idea, x: 420, y: centreY, size: 118, colour: palette.accent },
		{ key: 'FIELD LENS', value: lens, x: 1180, y: centreY, size: 118, colour: palette.accent2 },
		{ key: cover.mode.toUpperCase(), value: 'studio decision', x: 800, y: 160, size: 72, colour: palette.accent3 },
		{ key: 'EVIDENCE', value: 'process trace', x: 800, y: 400, size: 72, colour: palette.ink },
	];

	for (let index = 0; index < 18; index += 1) {
		const t = index / 17;
		const x = 430 + t * 740 + Math.sin(index * frequency) * 32;
		const y = centreY + Math.sin(index * drift * 3.8 + cover.seed * 0.01) * (82 + pulse * 32);
		const opacity = (0.1 + t * (1 - t) * 0.32).toFixed(3);
		const colour = index % 3 === 0 ? palette.accent3 : index % 2 === 0 ? palette.accent2 : palette.accent;
		connectors.push(`<line x1="${x.toFixed(2)}" y1="${y.toFixed(2)}" x2="${(x + 38).toFixed(2)}" y2="${(centreY + (random() - 0.5) * 160).toFixed(2)}" stroke="${colour}" stroke-opacity="${opacity}" stroke-width="2"/>`);
		nodes.push(
			hex(x, y, 10 + random() * 16, {
				fill: colour,
				'fill-opacity': (0.18 + random() * 0.32).toFixed(3),
				stroke: colour,
				'stroke-opacity': '0.55',
				'stroke-width': '1.1',
			}),
		);
	}

	const labelGroups = labels.map((label) => {
		const labelFill = label.key === 'EVIDENCE' ? palette.paper : palette.ink;
		const valueSize = label.value.length > 46 ? 22 : label.value.length > 32 ? 25 : 30;
		const lines = wrapWords(label.value, label.key === 'MASTER IDEA' ? 24 : 20);
		const valueText = semanticValueText(label, lines, valueSize, labelFill, palette);
		return `<g transform="translate(${label.x} ${label.y})">
    ${hex(0, 0, label.size, { fill: label.colour, 'fill-opacity': label.key === 'EVIDENCE' ? '0.88' : '0.24', stroke: label.colour, 'stroke-opacity': '0.9', 'stroke-width': '2.4' })}
    <text x="0" y="-20" text-anchor="middle" fill="${labelFill}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="18" font-weight="500" letter-spacing="2" opacity="0.88">${escapeXml(label.key)}</text>
    ${valueText}
  </g>`;
	});

	return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title-${id}-semantic desc-${id}-semantic">
  <title id="title-${id}-semantic">${escapeXml(cover.course)} · semantic graphic</title>
  <desc id="desc-${id}-semantic">${escapeXml(alt)}</desc>
  <defs>
    <linearGradient id="semantic-ground-${id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="${palette.paper}"/>
      <stop offset="1" stop-color="#070A11"/>
    </linearGradient>
  </defs>
  <rect width="${width}" height="${height}" fill="url(#semantic-ground-${id})"/>
  <g aria-hidden="true">${connectors.join('')}</g>
  <g aria-hidden="true">${nodes.join('')}</g>
  ${labelGroups.join('\n  ')}
</svg>`;
}

function outcomeTexture(id, cover, palette) {
	const random = randomFactory(hash32('outcome-texture-' + id + '-' + cover.seed));
	const marks = [];
	for (let index = 0; index < 38; index += 1) {
		const x = 70 + random() * 1460;
		const y = 60 + random() * 600;
		const size = 5 + random() * 15;
		const colour = index % 3 === 0 ? palette.accent3 : index % 2 === 0 ? palette.accent2 : palette.accent;
		marks.push(hex(x, y, size, {
			fill: colour,
			'fill-opacity': (0.025 + random() * 0.055).toFixed(3),
			stroke: colour,
			'stroke-opacity': (0.08 + random() * 0.12).toFixed(3),
			'stroke-width': '1',
		}));
	}
	return marks.join('');
}

function renderOutcomeGrammar(grammar, cover, palette) {
	const inkLine = { fill: 'none', stroke: palette.ink, 'stroke-opacity': '0.48', 'stroke-width': '3' };
	const fineLine = { fill: 'none', stroke: palette.ink, 'stroke-opacity': '0.25', 'stroke-width': '1.5' };
	const accentLine = { fill: 'none', stroke: palette.accent, 'stroke-opacity': '0.92', 'stroke-width': '7', 'stroke-linecap': 'round' };
	const secondLine = { fill: 'none', stroke: palette.accent2, 'stroke-opacity': '0.84', 'stroke-width': '5', 'stroke-linecap': 'round' };
	const thirdLine = { fill: 'none', stroke: palette.accent3, 'stroke-opacity': '0.78', 'stroke-width': '4', 'stroke-linecap': 'round' };
	const art = [];

	switch (grammar) {
		case 'practice-boundary': {
			const fields = [
				[250, 190, 78, palette.accent], [380, 390, 105, palette.accent2],
				[225, 540, 62, palette.accent3], [600, 175, 48, palette.accent2],
				[1010, 180, 66, palette.accent3], [1250, 360, 112, palette.accent],
				[1060, 545, 82, palette.accent2], [1390, 550, 46, palette.accent3],
			];
			for (const [x, y, size, colour] of fields) {
				art.push(hex(x, y, size, { fill: colour, 'fill-opacity': '0.2', stroke: colour, 'stroke-opacity': '0.75', 'stroke-width': '3' }));
			}
			art.push(path('M800 65 C725 165 875 255 798 360 C720 466 870 555 800 655', { fill: 'none', stroke: palette.ink, 'stroke-opacity': '0.64', 'stroke-width': '5', 'stroke-dasharray': '18 14' }));
			art.push(hex(800, 360, 142, { fill: palette.accent, 'fill-opacity': '0.32', stroke: palette.accent3, 'stroke-opacity': '0.95', 'stroke-width': '6' }));
			art.push(circle(800, 360, 28, { fill: palette.ink, 'fill-opacity': '0.9' }));
			break;
		}
		case 'curve-diagnosis': {
			art.push(path('M150 500 C330 70 530 640 730 245', { ...inkLine, 'stroke-dasharray': '15 12' }));
			art.push(line(150, 500, 330, 70, fineLine));
			art.push(line(530, 640, 730, 245, fineLine));
			for (const [x, y] of [[150, 500], [330, 70], [530, 640], [730, 245]]) {
				art.push(circle(x, y, 13, { fill: palette.paper, stroke: palette.ink, 'stroke-opacity': '0.7', 'stroke-width': '3' }));
			}
			art.push(path('M870 500 C1040 390 1150 105 1450 245', accentLine));
			art.push(line(870, 500, 1040, 390, { ...fineLine, stroke: palette.accent2, 'stroke-opacity': '0.65' }));
			art.push(line(1150, 105, 1450, 245, { ...fineLine, stroke: palette.accent2, 'stroke-opacity': '0.65' }));
			for (const [x, y, colour] of [[870, 500, palette.accent], [1040, 390, palette.accent2], [1150, 105, palette.accent2], [1450, 245, palette.accent]]) {
				art.push(circle(x, y, 16, { fill: colour, 'fill-opacity': '0.9', stroke: palette.ink, 'stroke-opacity': '0.5', 'stroke-width': '2' }));
			}
			art.push(hex(800, 360, 54, { fill: palette.accent3, 'fill-opacity': '0.28', stroke: palette.accent3, 'stroke-opacity': '0.9', 'stroke-width': '3' }));
			break;
		}
		case 'palette-depth': {
			const cell = 48;
			for (let row = 0; row < 8; row += 1) {
				for (let column = 0; column < 10; column += 1) {
					const limited = (row + column) % 3 === 0 ? palette.accent : palette.accent2;
					const nuanced = [palette.accent, palette.accent2, palette.accent3][(row * 2 + column) % 3];
					art.push(rect(125 + column * cell, 160 + row * cell, cell - 5, cell - 5, { rx: '4', fill: limited, 'fill-opacity': ((row + column) % 2 ? '0.34' : '0.72') }));
					art.push(rect(995 + column * cell, 160 + row * cell, cell - 5, cell - 5, { rx: '4', fill: nuanced, 'fill-opacity': (0.16 + (((row * 10 + column) % 7) / 8)).toFixed(2) }));
				}
			}
			art.push(path('M710 120 L890 120 L845 600 L755 600 Z', { fill: palette.ink, 'fill-opacity': '0.08', stroke: palette.ink, 'stroke-opacity': '0.34', 'stroke-width': '2' }));
			for (let index = 0; index < 7; index += 1) {
				art.push(line(742 + index * 19, 145, 775 + index * 8, 575, { fill: 'none', stroke: index % 2 ? palette.accent2 : palette.accent3, 'stroke-opacity': '0.5', 'stroke-width': '3' }));
			}
			break;
		}
		case 'traceable-transform': {
			const stages = [[250, 360, 92, palette.accent3], [520, 320, 105, palette.accent2], [800, 390, 118, palette.accent], [1080, 300, 105, palette.accent2], [1350, 360, 92, palette.accent3]];
			art.push(path('M250 360 C470 150 610 530 800 390 C1010 215 1160 470 1350 360', accentLine));
			for (let index = 0; index < stages.length; index += 1) {
				const [x, y, size, colour] = stages[index];
				art.push(hex(x, y, size, { fill: colour, 'fill-opacity': String(0.12 + index * 0.055), stroke: colour, 'stroke-opacity': '0.88', 'stroke-width': '4' }));
				art.push(hex(x, y, 28 + index * 5, { fill: colour, 'fill-opacity': '0.78' }));
				art.push(circle(x, 585, 12, { fill: colour, 'fill-opacity': '0.9' }));
				if (index > 0) art.push(line(stages[index - 1][0], 585, x, 585, thirdLine));
			}
			art.push(path('M250 585 C555 650 1045 650 1350 585', { ...fineLine, stroke: palette.accent3, 'stroke-opacity': '0.65' }));
			break;
		}
		case 'projection-fold': {
			art.push(rect(160, 150, 250, 175, { rx: '8', fill: palette.accent, 'fill-opacity': '0.16', stroke: palette.accent, 'stroke-opacity': '0.75', 'stroke-width': '3' }));
			art.push(rect(160, 405, 250, 175, { rx: '8', fill: palette.accent2, 'fill-opacity': '0.16', stroke: palette.accent2, 'stroke-opacity': '0.75', 'stroke-width': '3' }));
			art.push(polyline('520,185 690,135 760,300 590,350 520,185', { fill: palette.accent3, 'fill-opacity': '0.14', stroke: palette.accent3, 'stroke-opacity': '0.76', 'stroke-width': '3' }));
			for (const [x1, y1, x2, y2, colour] of [[410, 235, 990, 285, palette.accent], [410, 490, 990, 435, palette.accent2], [690, 245, 1050, 170, palette.accent3]]) {
				art.push(path('M' + x1 + ' ' + y1 + ' Q780 360 ' + x2 + ' ' + y2, { fill: 'none', stroke: colour, 'stroke-opacity': '0.58', 'stroke-width': '4', 'stroke-dasharray': '12 10' }));
			}
			art.push(polyline('1040,210 1280,145 1435,265 1190,335 1040,210', { fill: palette.accent, 'fill-opacity': '0.17', stroke: palette.accent, 'stroke-opacity': '0.9', 'stroke-width': '4' }));
			art.push(polyline('1040,210 1040,455 1190,575 1190,335 1040,210', { fill: palette.accent2, 'fill-opacity': '0.13', stroke: palette.accent2, 'stroke-opacity': '0.82', 'stroke-width': '4' }));
			art.push(polyline('1190,335 1435,265 1435,505 1190,575 1190,335', { fill: palette.accent3, 'fill-opacity': '0.13', stroke: palette.accent3, 'stroke-opacity': '0.82', 'stroke-width': '4' }));
			art.push(line(505, 450, 730, 585, { ...secondLine, 'stroke-dasharray': '10 10' }));
			art.push(line(505, 585, 730, 450, secondLine));
			break;
		}
		case 'hybrid-volume': {
			for (let index = 0; index < 9; index += 1) {
				art.push(path('M120 ' + (160 + index * 48) + ' C300 ' + (70 + index * 58) + ' 470 ' + (250 + index * 28) + ' 740 ' + (150 + index * 48), { fill: 'none', stroke: index % 2 ? palette.accent2 : palette.accent, 'stroke-opacity': '0.55', 'stroke-width': index % 3 === 0 ? '8' : '4' }));
			}
			for (let index = 0; index < 7; index += 1) {
				art.push(path('M' + (850 + index * 80) + ' 115 C' + (730 + index * 110) + ' 280 ' + (760 + index * 95) + ' 510 ' + (850 + index * 80) + ' 610', thirdLine));
			}
			for (let index = 0; index < 6; index += 1) {
				art.push(path('M830 ' + (150 + index * 82) + ' C1040 ' + (95 + index * 90) + ' 1300 ' + (210 + index * 65) + ' 1490 ' + (150 + index * 82), fineLine));
			}
			art.push(hex(800, 360, 104, { fill: palette.accent3, 'fill-opacity': '0.34', stroke: palette.ink, 'stroke-opacity': '0.78', 'stroke-width': '4' }));
			art.push(circle(800, 360, 34, { fill: palette.ink, 'fill-opacity': '0.9' }));
			break;
		}
		case 'reference-lineage': {
			const sources = [[160, 125], [160, 405], [475, 125], [475, 405]];
			for (let index = 0; index < sources.length; index += 1) {
				const [x, y] = sources[index];
				const colour = [palette.accent, palette.accent2, palette.accent3, palette.ink][index];
				art.push(rect(x, y, 230, 170, { rx: '10', fill: colour, 'fill-opacity': index === 3 ? '0.09' : '0.18', stroke: colour, 'stroke-opacity': '0.72', 'stroke-width': '3' }));
				art.push(hex(x + 72, y + 82, 38 + index * 5, { fill: colour, 'fill-opacity': '0.5' }));
				art.push(line(x + 130, y + 55, x + 195, y + 55, { ...fineLine, stroke: colour, 'stroke-opacity': '0.72' }));
				art.push(line(x + 130, y + 95, x + 182, y + 95, { ...fineLine, stroke: colour, 'stroke-opacity': '0.5' }));
			}
			for (const [x, y, colour] of [[390, 210, palette.accent], [390, 490, palette.accent2], [705, 210, palette.accent3], [705, 490, palette.ink]]) {
				art.push(path('M' + x + ' ' + y + ' C850 ' + y + ' 880 360 1050 360', { fill: 'none', stroke: colour, 'stroke-opacity': '0.65', 'stroke-width': '4' }));
			}
			art.push(hex(1235, 360, 245, { fill: palette.accent2, 'fill-opacity': '0.13', stroke: palette.accent2, 'stroke-opacity': '0.86', 'stroke-width': '5' }));
			art.push(hex(1180, 315, 95, { fill: palette.accent, 'fill-opacity': '0.42' }));
			art.push(hex(1305, 410, 78, { fill: palette.accent3, 'fill-opacity': '0.5' }));
			art.push(hex(1325, 270, 42, { fill: palette.ink, 'fill-opacity': '0.76' }));
			break;
		}
		case 'temporal-loop': {
			const frames = [];
			for (let index = 0; index < 7; index += 1) {
				const x = 180 + index * 205;
				const y = 310 + Math.sin(index * 0.9) * 85;
				const size = 46 + Math.sin(index * 0.65) * 24;
				frames.push([x, y]);
				art.push(hex(x, y, 92, { fill: palette.ink, 'fill-opacity': '0.04', stroke: palette.ink, 'stroke-opacity': '0.28', 'stroke-width': '2' }));
				art.push(hex(x, y, size, { fill: index % 2 ? palette.accent2 : palette.accent, 'fill-opacity': '0.58', stroke: palette.accent3, 'stroke-opacity': '0.72', 'stroke-width': '2' }));
				art.push(circle(x, 585, 10 + (index % 3) * 4, { fill: palette.accent3, 'fill-opacity': '0.85' }));
				if (index > 0) art.push(line(frames[index - 1][0] + 92, frames[index - 1][1], x - 92, y, secondLine));
			}
			art.push(path('M1410 310 C1510 80 80 70 180 310', { fill: 'none', stroke: palette.accent3, 'stroke-opacity': '0.58', 'stroke-width': '5', 'stroke-dasharray': '16 12' }));
			art.push(line(180, 585, 1410, 585, { ...fineLine, stroke: palette.accent3, 'stroke-opacity': '0.7' }));
			break;
		}
		case 'compositional-balance': {
			art.push(path('M210 500 Q800 535 1390 500', { ...inkLine, 'stroke-width': '5' }));
			art.push(polyline('720,560 800,405 880,560 720,560', { fill: palette.accent3, 'fill-opacity': '0.22', stroke: palette.accent3, 'stroke-opacity': '0.72', 'stroke-width': '3' }));
			art.push(circle(390, 395, 112, { fill: palette.accent, 'fill-opacity': '0.42', stroke: palette.accent, 'stroke-opacity': '0.86', 'stroke-width': '4' }));
			art.push(circle(1040, 430, 66, { fill: palette.accent2, 'fill-opacity': '0.5' }));
			art.push(hex(1200, 405, 72, { fill: palette.accent3, 'fill-opacity': '0.46' }));
			art.push(hex(965, 340, 38, { fill: palette.accent, 'fill-opacity': '0.62' }));
			for (let index = 0; index < 7; index += 1) {
				art.push(line(155 + index * 205, 105, 260 + index * 170, 300 + (index % 2) * 45, { fill: 'none', stroke: index % 2 ? palette.accent2 : palette.accent3, 'stroke-opacity': '0.25', 'stroke-width': '13' }));
			}
			art.push(hex(800, 405, 34, { fill: palette.ink, 'fill-opacity': '0.9' }));
			break;
		}
		case 'accountable-retouch': {
			for (const [x, colour] of [[170, palette.accent2], [930, palette.accent]]) {
				art.push(rect(x, 120, 500, 420, { rx: '12', fill: colour, 'fill-opacity': '0.1', stroke: colour, 'stroke-opacity': '0.76', 'stroke-width': '4' }));
				art.push(path('M' + (x + 80) + ' 445 C' + (x + 160) + ' 250 ' + (x + 300) + ' 220 ' + (x + 420) + ' 390', { fill: 'none', stroke: colour, 'stroke-opacity': '0.72', 'stroke-width': '18', 'stroke-linecap': 'round' }));
				art.push(circle(x + 180, 240, 54, { fill: palette.accent3, 'fill-opacity': '0.38' }));
			}
			art.push(path('M670 330 C755 250 845 250 930 330', accentLine));
			for (let index = 0; index < 5; index += 1) {
				art.push(circle(720 + index * 40, 292 - Math.sin(index * 0.8) * 28, 10, { fill: palette.ink, 'fill-opacity': '0.86' }));
			}
			art.push(path('M800 350 C800 470 760 535 690 610', { fill: 'none', stroke: palette.accent3, 'stroke-opacity': '0.45', 'stroke-width': '4', 'stroke-dasharray': '12 10' }));
			art.push(line(635, 610, 745, 610, { ...thirdLine, 'stroke-width': '8' }));
			art.push(line(680, 565, 700, 650, { ...thirdLine, 'stroke-width': '8' }));
			break;
		}
		case 'identity-parameters': {
			art.push(hex(260, 360, 118, { fill: palette.accent, 'fill-opacity': '0.28', stroke: palette.accent, 'stroke-opacity': '0.86', 'stroke-width': '4' }));
			for (let index = 0; index < 6; index += 1) {
				const x = 800 + (index % 3) * 280;
				const y = 180 + Math.floor(index / 3) * 360;
				const colour = [palette.accent2, palette.accent3, palette.accent][index % 3];
				art.push(path('M378 360 C560 360 570 ' + y + ' ' + (x - 88) + ' ' + y, { fill: 'none', stroke: colour, 'stroke-opacity': '0.55', 'stroke-width': '4' }));
				art.push(hex(x, y, 86, { fill: colour, 'fill-opacity': '0.22', stroke: colour, 'stroke-opacity': '0.82', 'stroke-width': '3' }));
				art.push(circle(x + (index % 2 ? 22 : -22), y - 8, 24 + (index % 3) * 7, { fill: palette.ink, 'fill-opacity': '0.58' }));
				for (let slider = 0; slider < 3; slider += 1) {
					art.push(line(x - 55, y + 25 + slider * 18, x + 55, y + 25 + slider * 18, { ...fineLine, stroke: colour, 'stroke-opacity': '0.6' }));
					art.push(circle(x - 35 + ((index + slider) % 5) * 18, y + 25 + slider * 18, 5, { fill: colour, 'fill-opacity': '0.95' }));
				}
			}
			break;
		}
		case 'staged-response': {
			art.push(path('M120 225 C380 110 470 285 720 225 C930 175 1020 180 1210 225', { ...secondLine, 'stroke-width': '9' }));
			art.push(path('M120 500 C360 575 510 390 720 500 C930 605 1020 430 1210 500', { ...thirdLine, 'stroke-width': '7' }));
			for (const [x, y, colour] of [[420, 205, palette.accent2], [760, 235, palette.accent2], [420, 515, palette.accent3], [760, 485, palette.accent3]]) {
				art.push(hex(x, y, 72, { fill: colour, 'fill-opacity': '0.2', stroke: colour, 'stroke-opacity': '0.72', 'stroke-width': '3' }));
			}
			for (let index = 0; index < 5; index += 1) {
				art.push(path('M1210 ' + (225 - index * 18) + ' C1320 ' + (150 - index * 8) + ' 1410 ' + (300 + index * 8) + ' 1510 ' + (225 + index * 18), { fill: 'none', stroke: palette.accent, 'stroke-opacity': String(0.76 - index * 0.1), 'stroke-width': String(7 - index) }));
				art.push(path('M1210 ' + (500 - index * 12) + ' C1320 ' + (445 - index * 4) + ' 1410 ' + (550 + index * 4) + ' 1510 ' + (500 + index * 12), { fill: 'none', stroke: palette.accent3, 'stroke-opacity': String(0.58 - index * 0.08), 'stroke-width': String(5 - index * 0.6) }));
			}
			art.push(rect(1170, 95, 370, 540, { rx: '18', fill: palette.ink, 'fill-opacity': '0.025', stroke: palette.ink, 'stroke-opacity': '0.22', 'stroke-width': '2', 'stroke-dasharray': '14 12' }));
			break;
		}
		case 'consent-sequence': {
			for (let index = 0; index < 3; index += 1) {
				const x = 150 + index * 500;
				const colour = [palette.accent, palette.accent2, palette.accent3][index];
				art.push(rect(x, 105, 390, 270, { rx: '10', fill: colour, 'fill-opacity': '0.12', stroke: colour, 'stroke-opacity': '0.78', 'stroke-width': '4' }));
				art.push(hex(x + 195, 235, 68 + index * 12, { fill: colour, 'fill-opacity': '0.46' }));
				if (index > 0) art.push(line(x - 105, 240, x - 10, 240, accentLine));
			}
			for (let track = 0; track < 3; track += 1) {
				const y = 465 + track * 65;
				const colour = [palette.accent, palette.accent2, palette.accent3][track];
				art.push(line(150, y, 1450, y, { fill: 'none', stroke: colour, 'stroke-opacity': '0.42', 'stroke-width': '8' }));
				for (let index = 0; index < 3; index += 1) {
					art.push(rect(180 + index * 500 + track * 24, y - 12, 270 - track * 28, 24, { rx: '5', fill: colour, 'fill-opacity': '0.72' }));
				}
			}
			art.push(hex(1450, 530, 46, { fill: palette.ink, 'fill-opacity': '0.9', stroke: palette.accent3, 'stroke-opacity': '0.9', 'stroke-width': '3' }));
			break;
		}
		case 'portfolio-lineage': {
			const tiles = [[130, 115], [130, 310], [420, 115], [420, 310]];
			for (let index = 0; index < tiles.length; index += 1) {
				const [x, y] = tiles[index];
				const colour = [palette.accent, palette.accent2, palette.accent3, palette.accent][index];
				art.push(rect(x, y, 220, 145, { rx: '8', fill: colour, 'fill-opacity': '0.13', stroke: colour, 'stroke-opacity': '0.72', 'stroke-width': '3' }));
				art.push(path('M' + (x + 35) + ' ' + (y + 100) + ' Q' + (x + 105) + ' ' + (y + 25 + index * 8) + ' ' + (x + 185) + ' ' + (y + 85), { fill: 'none', stroke: colour, 'stroke-opacity': '0.78', 'stroke-width': '5' }));
				art.push(circle(x + 40 + index * 35, y + 35, 10, { fill: colour, 'fill-opacity': '0.88' }));
			}
			art.push(path('M350 185 C680 185 650 360 900 360 M350 380 C680 380 650 360 900 360 M640 185 C760 185 770 300 900 360 M640 380 C760 380 770 380 900 360', { fill: 'none', stroke: palette.ink, 'stroke-opacity': '0.36', 'stroke-width': '4' }));
			art.push(rect(920, 70, 530, 580, { rx: '12', fill: palette.ink, 'fill-opacity': '0.045', stroke: palette.ink, 'stroke-opacity': '0.38', 'stroke-width': '3' }));
			art.push(rect(975, 130, 420, 250, { rx: '7', fill: palette.accent2, 'fill-opacity': '0.18', stroke: palette.accent2, 'stroke-opacity': '0.68', 'stroke-width': '3' }));
			for (let index = 0; index < 4; index += 1) {
				art.push(rect(975, 425 + index * 40, 250 + index * 35, 12, { rx: '4', fill: index % 2 ? palette.accent3 : palette.accent, 'fill-opacity': '0.62' }));
			}
			art.push(hex(900, 360, 48, { fill: palette.ink, 'fill-opacity': '0.9' }));
			break;
		}
		case 'medium-threshold': {
			art.push(path('M990 70 L1080 70 L1160 180 L1080 650 L990 650 L910 540 Z', { fill: palette.accent2, 'fill-opacity': '0.12', stroke: palette.accent2, 'stroke-opacity': '0.82', 'stroke-width': '5' }));
			const routes = [{ y: 175, colour: palette.accent, pass: false }, { y: 360, colour: palette.accent2, pass: true }, { y: 545, colour: palette.accent3, pass: false }];
			for (const route of routes) {
				art.push(hex(190, route.y, 72, { fill: route.colour, 'fill-opacity': '0.28', stroke: route.colour, 'stroke-opacity': '0.78', 'stroke-width': '3' }));
				art.push(path('M265 ' + route.y + ' C500 ' + (route.y - 70) + ' 700 ' + (route.y + 70) + ' ' + (route.pass ? 1040 : 850) + ' ' + route.y, { fill: 'none', stroke: route.colour, 'stroke-opacity': route.pass ? '0.92' : '0.48', 'stroke-width': route.pass ? '9' : '5', 'stroke-dasharray': route.pass ? '0' : '15 12' }));
				if (!route.pass) art.push(circle(860, route.y, 18, { fill: route.colour, 'fill-opacity': '0.78' }));
			}
			for (const [x, y, size] of [[1220, 235, 78], [1390, 360, 112], [1215, 520, 58]]) {
				art.push(hex(x, y, size, { fill: palette.accent2, 'fill-opacity': '0.22', stroke: palette.accent3, 'stroke-opacity': '0.74', 'stroke-width': '3' }));
			}
			art.push(path('M1080 360 C1190 360 1250 290 1390 360', secondLine));
			break;
		}
		default:
			throw new Error('Unknown outcome grammar \"' + grammar + '\"');
	}
	return art.join('');
}

function renderOutcomeGraphic(id, cover) {
	const palette = palettes[cover.family];
	const outcome = cover.outcome;
	if (!palette) throw new Error('Unknown cover family \"' + cover.family + '\" for ' + id);
	if (!outcome?.grammar) throw new Error('Cover ' + id + ' needs outcome.grammar');
	const width = 1600;
	const height = 720;
	const alt = outcome.alt_en || cover.alt_en || cover.master_idea;
	const grammar = renderOutcomeGrammar(outcome.grammar, cover, palette);
	return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n' +
		'<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 ' + width + ' ' + height + '\" role=\"img\" aria-labelledby=\"title-' + id + '-outcome desc-' + id + '-outcome\">\n' +
		'  <title id=\"title-' + id + '-outcome\">' + escapeXml(cover.course) + ' · outcome illustration</title>\n' +
		'  <desc id=\"desc-' + id + '-outcome\">' + escapeXml(alt) + '</desc>\n' +
		'  <rect width=\"' + width + '\" height=\"' + height + '\" fill=\"' + palette.paper + '\"/>\n' +
		'  <g aria-hidden=\"true\">' + outcomeTexture(id, cover, palette) + '</g>\n' +
		'  <g aria-hidden=\"true\">' + grammar + '</g>\n' +
		'  <path d=\"M46 82 L92 46 H1508 L1554 82 V638 L1508 674 H92 L46 638 Z\" fill=\"none\" stroke=\"' + palette.ink + '\" stroke-opacity=\"0.16\" stroke-width=\"2\"/>\n' +
		'</svg>';
}

function assertSemanticTextWeights(svg, asset) {
	const invalid = [...svg.matchAll(/font-weight=\"(\d+)\"/g)]
		.map((match) => Number(match[1]))
		.filter((weight) => weight !== 400 && weight !== 500);
	if (invalid.length) throw new Error('Semantic graphic ' + asset + ' uses invalid text weights: ' + invalid.join(', '));
}

function archiveExisting(filePath) {
	if (!existsSync(filePath) || archivedPaths.has(filePath)) return;
	mkdirSync(archiveDir, { recursive: true });
	copyFileSync(filePath, resolve(archiveDir, basename(filePath)));
	archivedPaths.add(filePath);
}

mkdirSync(outputDir, { recursive: true });
const manifest = [];

for (const [id, cover] of Object.entries(covers)) {
	if (id.startsWith('_')) continue;
	if (!cover.asset) throw new Error(`Cover ${id} needs an asset name`);
	const svgPath = resolve(outputDir, `${cover.asset}.svg`);
	const pngPath = resolve(outputDir, `${cover.asset}.png`);
	const semanticSvgPath = resolve(outputDir, `${semanticAsset(cover)}.svg`);
	const semanticPngPath = resolve(outputDir, `${semanticAsset(cover)}.png`);
	const outcomeSvgPath = resolve(outputDir, `${outcomeAsset(cover)}.svg`);
	const outcomePngPath = resolve(outputDir, `${outcomeAsset(cover)}.png`);
	const semanticSvg = renderSemanticGraphic(id, cover);
	for (const targetPath of [svgPath, pngPath, semanticSvgPath, semanticPngPath, outcomeSvgPath, outcomePngPath]) {
		archiveExisting(targetPath);
	}
	writeFileSync(svgPath, renderCover(id, cover));
	assertSemanticTextWeights(semanticSvg, semanticAsset(cover));
	writeFileSync(semanticSvgPath, semanticSvg);
	writeFileSync(outcomeSvgPath, renderOutcomeGraphic(id, cover));
	const converted = spawnSync('rsvg-convert', ['--width', '1600', '--height', '900', '--output', pngPath, svgPath], {
		encoding: 'utf8',
	});
	if (converted.status !== 0) {
		throw new Error(`PNG export failed for ${cover.asset}: ${converted.stderr || converted.error || 'unknown error'}`);
	}
	const semanticConverted = spawnSync('rsvg-convert', ['--width', '1600', '--height', '560', '--output', semanticPngPath, semanticSvgPath], {
		encoding: 'utf8',
	});
	if (semanticConverted.status !== 0) {
		throw new Error(`Semantic PNG export failed for ${cover.asset}: ${semanticConverted.stderr || semanticConverted.error || 'unknown error'}`);
	}
	const outcomeConverted = spawnSync('rsvg-convert', ['--width', '1600', '--height', '720', '--output', outcomePngPath, outcomeSvgPath], {
		encoding: 'utf8',
	});
	if (outcomeConverted.status !== 0) {
		throw new Error(`Outcome PNG export failed for ${cover.asset}: ${outcomeConverted.stderr || outcomeConverted.error || 'unknown error'}`);
	}
	manifest.push({
		id,
		asset: cover.asset,
		svg: `${cover.asset}.svg`,
		png: `${cover.asset}.png`,
		semantic_asset: semanticAsset(cover),
		semantic_svg: `${semanticAsset(cover)}.svg`,
		semantic_png: `${semanticAsset(cover)}.png`,
		outcome_asset: outcomeAsset(cover),
		outcome_svg: `${outcomeAsset(cover)}.svg`,
		outcome_png: `${outcomeAsset(cover)}.png`,
	});
}

const manifestPath = resolve(outputDir, 'manifest.json');
archiveExisting(manifestPath);
writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
const archiveNote = archivedPaths.size ? ` Archived ${archivedPaths.size} previous files in ${archiveDir}.` : ' No previous generated files were present to archive.';
console.log(`Generated ${manifest.length} Hexaform cover, semantic graphic, and outcome illustration sets in ${outputDir}.${archiveNote}`);
