#!/usr/bin/env node

import { readdirSync, readFileSync, statSync } from 'node:fs';
import { extname, join, relative, resolve } from 'node:path';

const root = process.cwd();
const citationMode = process.argv.includes('--citations');
const publicRoot = resolve(root, '_site');
const sourceRoots = [resolve(root, 'docs/lessons'), resolve(root, 'docs/tracks')];
const internalSwitch = 'site.publication.publish_internal_metadata';

// Student disclosure page may name the harness once (EX2 one-sentence footers link here).
function isDisclosurePath(relPath) {
	return /(?:^|\/)ai-declaration(?:\/|$)/i.test(relPath.replace(/\\/g, '/'));
}

const forbidden = [
	[/\bAhmes\b/i, 'internal corpus name'],
	[/\bAthanor\b/i, 'internal discovery service'],
	[/\bDevIAC\b/i, 'internal architecture'],
	[/\[BIBLIO-GAP\]/i, 'internal bibliography status'],
	[/\[UNVERIFIED-(?:GAP|NOISE)\]/i, 'internal verification status'],
	[/\bevaluator[_ -]?safe\b/i, 'internal evaluator status'],
	[/\bextraction\.db\b/i, 'local extraction database'],
	[/\bfission_node\b/i, 'local extraction schema'],
	[/\bproject_slug\b/i, 'internal project key'],
	[/\bknowledge_scope\b/i, 'internal search scope'],
	[/\b(?:course|research)\s+vault\b|\bcitation\s+library\b|\bresearch repository copy\b/i, 'local research architecture'],
	[/\b(?:evidence|grounding)\s+matrix\b/i, 'internal evidence architecture'],
	[/\bcitation[- ]resolver\b/i, 'internal resolver architecture'],
	[/\bvector (?:preview|snippet|search)\b/i, 'internal discovery trace'],
	[/\b(?:coat|node|nodo)\s+`?[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}`?/i, 'internal node identifier'],
	[/\bcoat\s+`?[0-9a-f]{8,}(?:_[0-9a-z]+)*`?/i, 'internal coat identifier'],
	[/\bfashlex\b/i, 'discontinued sibling vocabulary name'],
	[/\/Users\/ruvebal\/[^\s<'\"]+/i, 'local filesystem path'],
	[/~\/src\//i, 'local studio path'],
	[/\bdigital-creativity-pedagogy\//i, 'local curriculum-maintenance path'],
	[/\bfrontend-pedagogy\//i, 'local curriculum-maintenance path'],
	[/\bdocs\/_data\//i, 'local site-data path'],
	[/\btracks\.yml\b/i, 'local curriculum registry'],
	[/\b\.cursor\//i, 'local agent configuration'],
	[/\b(?:dc-)?unit-forge\.mdc\b/i, 'local forge rule'],
	[/\bCD-WAVE-4\.execute\.md\b/i, 'local execution plan'],
	// EX2 (FINDINGS C1/E1): authoring machinery + sibling surfaces (DC-tuned).
	// Asset dir `profield-cache/` is renamed in EX4; do not match path segments here.
	[/\blesson-scribe\b/i, 'internal authoring agent'],
	[/\bProfield\b/, 'internal media / campaign service'],
	[/profield\/runs\b/i, 'internal Profield run path'],
	[/\bThessia\b/, 'internal voice model'],
	[/\bForge date\b/i, 'internal authoring stamp'],
	[/\bFecha de forja\b/i, 'internal authoring stamp'],
	[/\bnm-unit-forge\b/i, 'internal unit forge'],
	[/(?<![A-Za-z0-9_-])UDIT(?![A-Za-z0-9_-])/, 'sibling institution (UDIT)'],
	[/\bweb-atelier\b/i, 'sibling course site'],
	[/\bcreativity-techniques-uem\b/i, 'sibling course site'],
	[/\bahmes-library\b/i, 'local vault path'],
];

const disclosureAllowed = new Set([
	'internal authoring agent',
	'internal authoring stamp',
	'sibling course site',
]);

function filesUnder(directory, extensions) {
	const result = [];
	for (const entry of readdirSync(directory)) {
		const path = join(directory, entry);
		if (statSync(path).isDirectory()) result.push(...filesUnder(path, extensions));
		else if (extensions.has(extname(path))) result.push(path);
	}
	return result;
}

function publicSource(markdown) {
	const output = [];
	let internalDepth = 0;
	for (const line of markdown.split(/\r?\n/)) {
		if (line.includes(`{% if ${internalSwitch} %}`)) {
			internalDepth += 1;
			continue;
		}
		if (internalDepth && line.includes('{% endif %}')) {
			internalDepth -= 1;
			continue;
		}
		if (!internalDepth) output.push(line);
	}
	return output.join('\n');
}

function isPublished(markdown) {
	const frontMatter = markdown.match(/^---\s*\n([\s\S]*?)\n---/);
	return !frontMatter || !/^published:\s*false\s*$/im.test(frontMatter[1]);
}

function leakAudit() {
	const failures = [];
	const extensions = new Set(['.html', '.xml', '.json', '.js', '.css', '.svg', '.md', '.txt', '.yml', '.yaml']);
	for (const file of filesUnder(publicRoot, extensions)) {
		const rel = relative(root, file);
		const disclosure = isDisclosurePath(rel);
		const content = readFileSync(file, 'utf8');
		for (const [pattern, label] of forbidden) {
			if (disclosure && disclosureAllowed.has(label)) continue;
			if (pattern.test(content)) failures.push(`${rel}: ${label}`);
		}
	}
	for (const sourceRoot of sourceRoots) {
		if (!statSync(sourceRoot, { throwIfNoEntry: false })?.isDirectory()) continue;
		for (const file of filesUnder(sourceRoot, new Set(['.md', '.html']))) {
			const raw = readFileSync(file, 'utf8');
			if (!isPublished(raw)) continue;
			const content = publicSource(raw);
			const rel = relative(root, file);
			for (const [pattern, label] of forbidden) {
				if (pattern.test(content)) failures.push(`${rel}: ungated ${label}`);
			}
		}
	}
	if (failures.length) {
		console.error(`Publication safety failed (${failures.length} finding(s)):\n${failures.join('\n')}`);
		process.exit(1);
	}
	console.log('Publication safety passed: no internal corpus or local-architecture metadata is publishable.');
}

function citationAudit() {
	const failures = [];
	const lessonRoot = resolve(root, 'docs/lessons');
	for (const file of filesUnder(lessonRoot, new Set(['.md']))) {
		const raw = readFileSync(file, 'utf8');
		if (!isPublished(raw)) continue;
		if (!raw.includes('lesson-semantic-graphic.html')) continue;
		const content = publicSource(raw);
		const body = content.replace(/^---[\s\S]*?---\s*/m, '');
		const inlineCitations = body.match(/\([A-ZÁÉÍÓÚÑ][^()\n]{0,90}\s(?:19|20)\d{2}(?:,\s*\d+(?:[–-]\d+)?)?\)/g) || [];
		const apaInline = body.match(/\([A-ZÁÉÍÓÚÑ][^()\n]{0,70},\s*(?:19|20)\d{2}\)/g) || [];
		const referenceHeadings = [...body.matchAll(/^##\s+(?:References|Referencias)\s*$/gim)];
		if (apaInline.length) failures.push(`${relative(root, file)}: APA-style comma in inline author-date citation (${apaInline[0]})`);
		if (inlineCitations.length && !referenceHeadings.length) {
			failures.push(`${relative(root, file)}: has author-date citations but no final References/Referencias section`);
		}
		if (referenceHeadings.length) {
			const finalReferences = referenceHeadings.at(-1);
			const afterReferences = body.slice(finalReferences.index + finalReferences[0].length);
			const trailingH2 = [...afterReferences.matchAll(/^##\s+(.+?)\s*$/gm)].map((m) => m[1].trim());
			const allowedTrailing = trailingH2.every((title) =>
				/^(?:Editorial note\b|Nota editorial\b|AI-assisted authorship\b|Autoría asistida)/i.test(title)
			);
			if (trailingH2.length && !allowedTrailing) {
				failures.push(`${relative(root, file)}: References/Referencias is not followed only by Editorial note / AI-assisted authorship`);
			}
			const beforeEditorial = afterReferences.split(/^##\s+(?:Editorial note\b|Nota editorial\b)/im)[0] || afterReferences;
			if (/\*\*(?:Declared gap|Missing evidence|Laguna declarada|Evidencia faltante)/i.test(beforeEditorial)) {
				failures.push(`${relative(root, file)}: Declared gap / Missing evidence must live under Editorial note, not under References`);
			}
			if (/\*\(bibliography present|page node still open/i.test(beforeEditorial)) {
				failures.push(`${relative(root, file)}: editor asides (page node / bibliography present) must move into Editorial note`);
			}
			const hasEditorial = trailingH2.some((title) => /^(?:Editorial note\b|Nota editorial\b)/i.test(title));
			const hasAi = trailingH2.some((title) => /^(?:AI-assisted authorship\b|Autoría asistida)/i.test(title));
			if (!hasEditorial) failures.push(`${relative(root, file)}: missing Editorial note / Nota editorial after References`);
			if (!hasAi) failures.push(`${relative(root, file)}: missing AI-assisted authorship / Autoría asistida footer`);
			if (hasEditorial && hasAi) {
				const edIdx = trailingH2.findIndex((title) => /^(?:Editorial note\b|Nota editorial\b)/i.test(title));
				const aiIdx = trailingH2.findIndex((title) => /^(?:AI-assisted authorship\b|Autoría asistida)/i.test(title));
				if (aiIdx < edIdx) failures.push(`${relative(root, file)}: AI-assisted authorship must follow Editorial note`);
			}
			if (!/\/ai-declaration\//.test(afterReferences) && !/\{\{\s*'\/ai-declaration\/'\s*\|\s*relative_url\s*\}\}/.test(afterReferences)) {
				failures.push(`${relative(root, file)}: AI-assisted authorship footer must link to /ai-declaration/`);
			}
			// EX2: public AI footer is one sentence + /ai-declaration/ link.
			// Forge date / lesson-scribe stay in gated curriculum-internal metadata.
		}
	}
	if (statSync(publicRoot, { throwIfNoEntry: false })) {
		for (const file of filesUnder(resolve(publicRoot, 'lessons'), new Set(['.html']))) {
			const body = readFileSync(file, 'utf8');
			const citationLinks = [...body.matchAll(/<a class="citation-link" href="#(ref-[^"]+)"[^>]*>\([^<]+\)<\/a>/g)];
			for (const match of citationLinks) {
				if (!body.includes(`id="${match[1]}"`)) failures.push(`${relative(root, file)}: citation link points to a missing reference anchor (${match[1]})`);
			}
			if (/\b(?:Shinkle|Anwar|Rizzi|Coats|Campinho|Kim|Smith-Glaviana)\b[^<\n]{0,55}\s(?:19|20)\d{2}/.test(body) && !citationLinks.length) {
				failures.push(`${relative(root, file)}: published author-date citations are not linked to reference anchors`);
			}
			const referencesBlock = body.match(/<h2 id="(?:references|referencias)">(?:References|Referencias)<\/h2>([\s\S]*?)(?=<h2\b|$)/i);
			if (referencesBlock) {
				const refs = referencesBlock[1];
				// Strip existing anchors so we only catch bare leftover URLs.
				const withoutAnchors = refs.replace(/<a\b[^>]*>[\s\S]*?<\/a>/gi, '');
				const bare = withoutAnchors.match(/https?:\/\/[^\s<>"']+/g) || [];
				for (const url of bare) {
					failures.push(`${relative(root, file)}: bare reference URL is not an anchor (${url})`);
				}
				const externalAnchors = [...refs.matchAll(/<a\b([^>]*)href=(["'])(https?:\/\/[^"']+)\2([^>]*)>/gi)];
				for (const match of externalAnchors) {
					const attrs = `${match[1]} ${match[4]}`;
					if (!/\btarget\s*=\s*(["'])_blank\1/i.test(attrs)) {
						failures.push(`${relative(root, file)}: external reference URL missing target="_blank" (${match[3]})`);
					}
				}
			}
		}
	}
	if (failures.length) {
		console.error(`Citation conformance failed (${failures.length} finding(s)):\n${failures.join('\n')}`);
		process.exit(1);
	}
	console.log('Citation conformance passed for canonical lessons.');
}

if (citationMode) citationAudit();
else leakAudit();
