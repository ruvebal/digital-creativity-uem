#!/usr/bin/env node

import { readdirSync, readFileSync, statSync } from 'node:fs';
import { extname, join, relative, resolve } from 'node:path';

const root = process.cwd();
const citationMode = process.argv.includes('--citations');
const publicRoot = resolve(root, '_site');
const sourceRoot = resolve(root, 'docs/lessons');
const internalSwitch = 'site.publication.publish_internal_metadata';

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
];

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
		const content = readFileSync(file, 'utf8');
		for (const [pattern, label] of forbidden) {
			if (pattern.test(content)) failures.push(`${relative(root, file)}: ${label}`);
		}
	}
	for (const file of filesUnder(sourceRoot, new Set(['.md', '.html']))) {
		const raw = readFileSync(file, 'utf8');
		if (!isPublished(raw)) continue;
		const content = publicSource(raw);
		for (const [pattern, label] of forbidden) {
			if (pattern.test(content)) failures.push(`${relative(root, file)}: ungated ${label}`);
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
	for (const file of filesUnder(sourceRoot, new Set(['.md']))) {
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
		if (inlineCitations.length && referenceHeadings.length) {
			const finalReferences = referenceHeadings.at(-1);
			const afterReferences = body.slice(finalReferences.index + finalReferences[0].length);
			const trailingH2 = [...afterReferences.matchAll(/^##\s+(.+?)\s*$/gm)].map((m) => m[1].trim());
			const allowedTrailing = trailingH2.every((title) =>
				/^(?:Editorial note\b|Nota editorial\b|AI-assisted authorship\b|Autoría asistida)/i.test(title)
			);
			if (trailingH2.length && !allowedTrailing) {
				failures.push(`${relative(root, file)}: References/Referencias is not the final visible level-two section`);
			}
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
