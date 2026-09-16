#!/usr/bin/env node
/**
 * Hydrate DC field directory:
 *   directory/*.yml  → ONE route /directory/en/  (#section hashes)
 *
 * Mimics creativity-techniques-uem `hydrate-field-site.mjs` directory lane only.
 * Lexicum stays on its existing forge/sync path (`/lexicum/`).
 */

import {
	mkdirSync,
	readFileSync,
	readdirSync,
	rmSync,
	writeFileSync,
	existsSync,
} from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const docs = join(root, 'docs');
const dataOut = join(docs, '_data');
const dirSrc = join(root, 'directory');

const CATEGORIES = [
	'prizes',
	'awards',
	'studios',
	'journals',
	'organizations',
	'contests',
	'figures',
];

const PROVENANCE = {
	author: {
		name: 'Rubén Vega Balbás, PhD',
		role: 'Creative Technologist & Developer',
		orcid: 'https://orcid.org/0000-0001-6862-9081',
		email: 'ruvebal@crea-comm.net',
	},
	vocabulary_engine: {
		name: 'lexfield',
		version: '0.1.0',
	},
	publication_stack: {
		static_site: 'Jekyll 3.10.0',
		templates: 'Liquid 4.0.4',
		hydrate: 'Node.js (js-yaml)',
	},
	ontology: {
		skos: {
			url: 'https://www.w3.org/TR/skos-reference/',
		},
		cidoc_crm: {
			version: '7.1.3 (2024-02-13)',
			url: 'https://gitlab.isl.ics.forth.gr/cidoc-crm/cidoc_crm_rdf',
		},
	},
};

const CREDIT_METHOD =
	'Curriculum-local field directory (YAML-as-code); entries seeded from the digital-creativity field panorama — prizes, awards, studios, journals, organizations, contests, and figures.';

function loadYaml(path) {
	return yaml.load(readFileSync(path, 'utf8'));
}

function write(path, text) {
	mkdirSync(dirname(path), { recursive: true });
	writeFileSync(path, text, 'utf8');
}

function fm(fields) {
	const lines = Object.entries(fields).map(([k, v]) => {
		if (typeof v === 'boolean') return `${k}: ${v}`;
		return `${k}: ${JSON.stringify(v)}`;
	});
	return `---\n${lines.join('\n')}\n---\n`;
}

function publicEntry(row) {
	const {
		id,
		name,
		kind,
		status,
		summary,
		url = null,
		doi = null,
		location = null,
		years = null,
		references = [],
		units = [],
	} = row;
	return { id, name, kind, status, summary, url, doi, location, years, references, units };
}

function wipeChildrenExceptIndex(dir) {
	if (!existsSync(dir)) return;
	for (const name of readdirSync(dir)) {
		if (name === 'index.md') continue;
		rmSync(join(dir, name), { recursive: true, force: true });
	}
}

function tocNav(items) {
	const lis = items
		.map(
			(item) =>
				`<li><a href="#${item.id}">${item.label} <span class="field-index__count">${item.count}</span></a></li>`,
		)
		.join('\n');
	return `<nav class="field-index__toc" aria-label="On this page">
<p class="field-index__toc-label">On this page</p>
<ul>
${lis}
</ul>
</nav>`;
}

function renderCredit() {
	const prov = PROVENANCE;
	const stack = prov.publication_stack;
	return `<div class="field-index__credit">
<p class="field-index__credit-by">By <a href="${prov.author.orcid}">${prov.author.name}</a> — ${prov.author.role} · ORCID <a href="${prov.author.orcid}">0000-0001-6862-9081</a></p>
<p class="field-index__credit-stack">Built with <strong>${prov.vocabulary_engine.name} ${prov.vocabulary_engine.version}</strong> (YAML → SKOS ConceptSchemes); published via <strong>${stack.static_site}</strong> + ${stack.templates} + ${stack.hydrate}; ontology layer <a href="${prov.ontology.skos.url}">SKOS (2009-08-18)</a> with optional <a href="${prov.ontology.cidoc_crm.url}">CIDOC-CRM ${prov.ontology.cidoc_crm.version}</a> class maps.</p>
<p class="field-index__credit-method">${CREDIT_METHOD}</p>
</div>`;
}

function hydrateDirectory() {
	const index = loadYaml(join(dirSrc, 'index.yml'));
	const categories = {};
	for (const cat of CATEGORIES) {
		const path = join(dirSrc, `${cat}.yml`);
		const rows = existsSync(path) ? loadYaml(path) || [] : [];
		categories[cat] = rows.map(publicEntry);
	}

	const payload = { ...index, categories };
	delete payload.source;
	payload.source_note =
		'Seeded from the digital-creativity field panorama; edit directory/*.yml to update.';
	write(join(dataOut, 'field_directory.yml'), yaml.dump(payload, { lineWidth: 100 }));

	const base = join(docs, 'directory/en');
	mkdirSync(base, { recursive: true });
	wipeChildrenExceptIndex(base);

	const toc = tocNav(
		CATEGORIES.map((id) => ({
			id,
			label: index.categories.find((c) => c.id === id)?.title || id,
			count: categories[id].length,
		})),
	);

	const entryTotal = CATEGORIES.reduce((n, c) => n + categories[c].length, 0);
	const sections = CATEGORIES.map((cat) => {
		const title = index.categories.find((c) => c.id === cat)?.title || cat;
		const entries = categories[cat];
		const cards = entries
			.map((e) => {
				const meta = [
					e.status ? `<span class="field-card__status">${e.status}</span>` : '',
					e.location ? `<span class="field-card__meta">${e.location}</span>` : '',
					e.years ? `<span class="field-card__meta">${e.years}</span>` : '',
				]
					.filter(Boolean)
					.join('');
				const link = e.url
					? `<p class="field-card__link"><a href="${e.url}" rel="noopener noreferrer">${e.url.replace(/^https?:\/\//, '')}</a></p>`
					: '';
				const doi = e.doi ? `<p class="field-card__doi">DOI <code>${e.doi}</code></p>` : '';
				const refs = (e.references || []).length
					? `<ul class="field-card__refs">${(e.references || []).map((r) => `<li>${r}</li>`).join('')}</ul>`
					: '';
				return `<article class="field-card" id="${cat}--${e.id}">
<h3 class="field-card__title">${e.name}</h3>
<p class="field-card__summary">${e.summary}</p>
<p class="field-card__badges">${meta}</p>
${link}${doi}${refs}
</article>`;
			})
			.join('\n');
		return `<section class="field-index__section" id="${cat}">
<h2>${title}</h2>
<div class="field-card-grid">
${cards || '<p class="field-index__empty">No entries yet.</p>'}
</div>
</section>`;
	}).join('\n\n');

	write(
		join(base, 'index.md'),
		fm({
			layout: 'default',
			title: 'Field directory',
			lang: 'en',
			permalink: '/directory/en/',
			description:
				'Prizes, awards, studios, journals, organizations, contests, and figures — one page, section hashes.',
			field_index: true,
		}) +
			`<div class="field-index not-prose" data-field-index="directory">
<header class="field-index__hero">
<p class="field-index__eyebrow">Field map</p>
<h1 class="field-index__title">Directory</h1>
<p class="field-index__lede">Authorities and reference points for Digital Creativity in fashion. Stay on this page — jump by section.</p>
<ul class="field-index__stats" aria-label="Directory statistics">
<li><strong>${entryTotal}</strong> entries</li>
<li><strong>${CATEGORIES.length}</strong> sections</li>
</ul>
${renderCredit()}
</header>
${toc}
${sections}
<footer class="field-index__related">
<p>Also see <a href="{{ '/lexicum/' | relative_url }}">Lexicum</a> · <a href="{{ '/tao/' | relative_url }}">Tao</a></p>
</footer>
</div>
`,
	);

	return entryTotal;
}

const n = hydrateDirectory();
console.log(`hydrate-directory: ${n} entries → /directory/en/`);
