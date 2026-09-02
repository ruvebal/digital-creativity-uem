import fs from 'node:fs';
import path from 'node:path';

const root = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();
const docsDir = path.join(root, 'docs');
const outDir = path.join(docsDir, 'assets/images/page-art');
const dataPath = path.join(docsDir, '_data/page_art.json');
const archiveDataPath = path.join(docsDir, '_data/archive_covers.json');

function loadArchiveUrls() {
	const urls = new Set();
	if (!fs.existsSync(archiveDataPath)) return urls;
	for (const url of Object.keys(JSON.parse(fs.readFileSync(archiveDataPath, 'utf8')))) urls.add(url);
	return urls;
}

const colors = [
	['#9373DD', '#0EA5A3', '#E2B127', '#C44536'],
	['#7F77DD', '#1D9E75', '#EF9F27', '#D4537E'],
	['#378ADD', '#F0997B', '#C9C932', '#AFA9EC'],
	['#534AB7', '#5DCAA5', '#FAC775', '#D85A30'],
	['#0C447C', '#97C459', '#ED93B1', '#E2B127'],
];

function walk(dir) {
	return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
		const full = path.join(dir, entry.name);
		if (entry.isDirectory()) {
			if (entry.name.startsWith('_') || ['assets', '.jekyll-cache', '.sass-cache'].includes(entry.name)) return [];
			return walk(full);
		}
		return entry.isFile() ? [full] : [];
	});
}

function frontmatter(text) {
	if (!text.startsWith('---\n')) return null;
	const end = text.indexOf('\n---', 4);
	if (end === -1) return null;
	const raw = text.slice(4, end);
	const data = {};
	for (const line of raw.split('\n')) {
		const match = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
		if (!match) continue;
		data[match[1]] = match[2].trim().replace(/^['"]|['"]$/g, '');
	}
	return data;
}

function pageUrl(file, fm) {
	if (fm?.permalink) return fm.permalink.startsWith('/') ? fm.permalink : `/${fm.permalink}`;
	const rel = path.relative(docsDir, file).replaceAll(path.sep, '/');
	if (rel === 'index.html' || rel === 'index.md') return '/';
	if (rel.endsWith('/index.md') || rel.endsWith('/index.html')) return `/${rel.replace(/\/index\.(md|html)$/, '/')}`;
	return `/${rel.replace(/\.(md|html)$/, '.html')}`;
}

function slugify(input) {
	return input
		.toLowerCase()
		.normalize('NFD')
		.replace(/[\u0300-\u036f]/g, '')
		.replace(/[^a-z0-9]+/g, '-')
		.replace(/^-+|-+$/g, '')
		.slice(0, 86) || 'index';
}

function hash(input) {
	let h = 2166136261;
	for (let i = 0; i < input.length; i += 1) {
		h ^= input.charCodeAt(i);
		h = Math.imul(h, 16777619);
	}
	return h >>> 0;
}

function rng(seed) {
	let state = seed || 1;
	return () => {
		state ^= state << 13;
		state ^= state >>> 17;
		state ^= state << 5;
		return ((state >>> 0) % 10000) / 10000;
	};
}

function poly(points) {
	return points.map(([x, y]) => `${x.toFixed(1)},${y.toFixed(1)}`).join(' ');
}

function solid(cx, cy, radius, sides, spin) {
	const outer = [];
	const inner = [];
	for (let i = 0; i < sides; i += 1) {
		const a = spin + (Math.PI * 2 * i) / sides;
		outer.push([cx + Math.cos(a) * radius, cy + Math.sin(a) * radius]);
		inner.push([cx + Math.cos(a + Math.PI / sides) * radius * 0.52, cy + Math.sin(a + Math.PI / sides) * radius * 0.52]);
	}
	const lines = [];
	for (let i = 0; i < sides; i += 1) {
		const next = (i + 1) % sides;
		lines.push(`<line x1="${outer[i][0].toFixed(1)}" y1="${outer[i][1].toFixed(1)}" x2="${inner[i][0].toFixed(1)}" y2="${inner[i][1].toFixed(1)}"/>`);
		lines.push(`<line x1="${inner[i][0].toFixed(1)}" y1="${inner[i][1].toFixed(1)}" x2="${outer[next][0].toFixed(1)}" y2="${outer[next][1].toFixed(1)}"/>`);
	}
	return `<polygon points="${poly(outer)}"/><polygon points="${poly(inner)}"/>${lines.join('')}`;
}

function fractalShard(cx, cy, radius, depth, spin, palette) {
	const points = Array.from({ length: 3 }, (_, i) => {
		const angle = spin + (Math.PI * 2 * i) / 3;
		return [cx + Math.cos(angle) * radius, cy + Math.sin(angle) * radius];
	});
	const color = palette[depth % palette.length];
	const shape = `<polygon points="${poly(points)}" fill="none" stroke="${color}" stroke-width="${(0.55 + depth * 0.22).toFixed(2)}" opacity="${(0.16 + depth * 0.07).toFixed(2)}"/>`;
	if (depth <= 0) return shape;
	const children = points.map(([x, y], i) => {
		const mx = (cx + x) / 2;
		const my = (cy + y) / 2;
		return fractalShard(mx, my, radius * 0.46, depth - 1, spin + Math.PI / 3 + i * 0.18, palette);
	});
	return `${shape}${children.join('')}`;
}

function art({ url, title, seed }) {
	const r = rng(seed);
	const palette = colors[seed % colors.length];
	const sides = [4, 6, 8, 12, 20][seed % 5];
	const cx = 1060 + r() * 260;
	const cy = 170 + r() * 48;
	const radius = 76 + r() * 58;
	const bars = Array.from({ length: 14 }, (_, i) => {
		const x = 80 + i * 104 + r() * 38;
		const y = 28 + r() * 288;
		const w = 22 + r() * 120;
		const h = 3 + r() * 12;
		return `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" fill="${palette[i % palette.length]}" opacity="${(0.1 + r() * 0.22).toFixed(2)}"/>`;
	}).join('');
	const fractals = Array.from({ length: 5 }, (_, i) => {
		const x = 170 + i * 270 + r() * 80;
		const y = 110 + r() * 160;
		const size = 46 + r() * 74;
		return fractalShard(x, y, size, 3, r() * Math.PI * 2, palette);
	}).join('');
	const curve = `M70 ${250 + r() * 55} C${330 + r() * 80} ${30 + r() * 70}, ${470 + r() * 120} ${342 - r() * 80}, ${730 + r() * 80} ${166 + r() * 80} S${1160 + r() * 80} ${86 + r() * 120}, ${1510} ${232 + r() * 56}`;
	const nodes = Array.from({ length: 10 }, (_, i) => {
		const x = 130 + i * 145 + Math.sin(seed + i) * 34;
		const y = 205 + Math.cos(seed * 0.3 + i) * 86;
		const n = 5 + (i % 3);
		const rr = 14 + r() * 17;
		return `<polygon points="${Array.from({ length: n }, (_, k) => {
			const a = (Math.PI * 2 * k) / n + r();
			return [x + Math.cos(a) * rr, y + Math.sin(a) * rr];
		}).map(([px, py]) => `${px.toFixed(1)},${py.toFixed(1)}`).join(' ')}" fill="${palette[(i + 1) % palette.length]}" opacity="${(0.15 + r() * 0.18).toFixed(2)}"/>`;
	}).join('');
	return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 360" role="img" aria-labelledby="title-${seed} desc-${seed}">
  <title id="title-${seed}">Generative page artwork</title>
  <desc id="desc-${seed}">Platonic-solid, fractal, opt-art, glitch, and organic dialogue geometry for ${escapeXml(title || url)}.</desc>
  <defs>
    <filter id="grain-${seed}" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="${(0.55 + r() * 0.45).toFixed(2)}" numOctaves="2" seed="${seed % 997}" result="noise"/>
      <feColorMatrix in="noise" type="saturate" values="0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 .16"/></feComponentTransfer>
    </filter>
  </defs>
  <rect width="1600" height="360" fill="#050816"/>
  <rect width="1600" height="360" fill="${palette[seed % palette.length]}" opacity=".10"/>
  <g fill="none" stroke="${palette[0]}" stroke-width="1.2" opacity=".58">${fractals}</g>
  <path d="${curve}" fill="none" stroke="${palette[1]}" stroke-width="7" stroke-linecap="round" opacity=".34"/>
  <path d="${curve}" fill="none" stroke="${palette[2]}" stroke-width="1.1" stroke-dasharray="11 16" stroke-linecap="round" opacity=".78"/>
  <g stroke="${palette[3]}" stroke-width="2.2" fill="none" opacity=".74" transform="rotate(${(r() * 18 - 9).toFixed(2)} ${cx.toFixed(1)} ${cy.toFixed(1)})">${solid(cx, cy, radius, sides, r() * Math.PI)}</g>
  <g>${nodes}</g>
  <g>${bars}</g>
  <rect width="1600" height="360" filter="url(#grain-${seed})" opacity=".85"/>
</svg>
`;
}

function escapeXml(value) {
	return String(value)
		.replaceAll('&', '&amp;')
		.replaceAll('<', '&lt;')
		.replaceAll('>', '&gt;')
		.replaceAll('"', '&quot;');
}

fs.mkdirSync(outDir, { recursive: true });
const files = walk(docsDir).filter((file) => {
	if (!/\.(md|html)$/.test(file)) return false;
	const text = fs.readFileSync(file, 'utf8');
	return frontmatter(text);
});

const archiveUrls = loadArchiveUrls();
const registry = {};
for (const file of files) {
	const text = fs.readFileSync(file, 'utf8');
	const fm = frontmatter(text);
	if (!fm || fm.published === 'false' || fm.sitemap === 'false') continue;
	const url = pageUrl(file, fm);
	if (archiveUrls.has(url)) continue;
	const seed = hash(url);
	const title = fm.title || url;
	const asset = `page-${slugify(url)}`;
	fs.writeFileSync(path.join(outDir, `${asset}.svg`), art({ url, title, seed }));
	registry[url] = {
		asset,
		title,
		grammar: ['platonic-solid', 'fractal-structure', 'opt-art', 'glitch', 'organic-dialogue'],
	};
}
fs.mkdirSync(path.dirname(dataPath), { recursive: true });
fs.writeFileSync(dataPath, `${JSON.stringify(registry, null, 2)}\n`);
console.log(`Generated ${Object.keys(registry).length} page artworks in ${path.relative(root, outDir)}`);
