#!/usr/bin/env node
/**
 * Classroom board rule: DOI / http(s) reference URLs must be clickable and open
 * in a new tab so professors do not lose the lesson on the projected screen.
 *
 * Runs after Jekyll write. Idempotent.
 * 1) Wrap bare http(s) URLs in text nodes as <a target="_blank" …>
 * 2) Ensure existing external <a href="http(s):…"> carry target="_blank" rel="noopener noreferrer"
 */
import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const siteRoot = resolve(process.cwd(), '_site');
const EXTERNAL_ATTRS = 'target="_blank" rel="noopener noreferrer"';
const LINK_CLASS = 'external-ref-link';
const URL_RE = /https?:\/\/[^\s<>"']+/g;
const TRAILING_PUNCT_RE = /[.,;:!?)\]]+$/;

function filesUnder(directory) {
	if (!statSync(directory, { throwIfNoEntry: false })) return [];
	return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
		const path = join(directory, entry.name);
		return entry.isDirectory() ? filesUnder(path) : path.endsWith('.html') ? [path] : [];
	});
}

function splitTrailingPunctuation(url) {
	const match = url.match(TRAILING_PUNCT_RE);
	if (!match) return { href: url, trailing: '' };
	return { href: url.slice(0, -match[0].length), trailing: match[0] };
}

/**
 * Link bare http(s) URLs in text nodes only. Protects element interiors
 * (script/style/code/pre/a/…) and every remaining tag so href attributes
 * are never re-wrapped.
 */
function linkBareUrls(html) {
	const placeholders = [];
	const stash = (chunk) => {
		placeholders.push(chunk);
		return `\u0000${placeholders.length - 1}\u0000`;
	};
	let protectedHtml = html.replace(
		/<(script|style|code|pre|textarea|svg|math|a)\b[^>]*>[\s\S]*?<\/\1>/gi,
		stash,
	);
	protectedHtml = protectedHtml.replace(/<[^>]+>/g, stash);
	protectedHtml = protectedHtml.replace(URL_RE, (raw) => {
		const { href, trailing } = splitTrailingPunctuation(raw);
		if (!href) return raw;
		return `<a class="${LINK_CLASS}" href="${href}" ${EXTERNAL_ATTRS}>${href}</a>${trailing}`;
	});
	return protectedHtml.replace(/\u0000(\d+)\u0000/g, (_, index) => placeholders[Number(index)]);
}

function ensureExternalAnchorTargets(html) {
	return html.replace(/<a\b([^>]*)>/gi, (full, attrs) => {
		const hrefMatch = attrs.match(/\bhref\s*=\s*(["'])(.*?)\1/i);
		if (!hrefMatch) return full;
		const href = hrefMatch[2].trim();
		if (!/^https?:\/\//i.test(href)) return full;
		if (/\bclass\s*=\s*(["'])[^"']*\bcitation-link\b/i.test(attrs)) return full;
		let next = attrs;
		if (!/\btarget\s*=/i.test(next)) {
			next = `${next} target="_blank"`;
		} else {
			next = next.replace(/\btarget\s*=\s*(["'])[^"']*\1/i, 'target="_blank"');
		}
		if (!/\brel\s*=/i.test(next)) {
			next = `${next} rel="noopener noreferrer"`;
		} else if (!/noopener/i.test(next)) {
			next = next.replace(/\brel\s*=\s*(["'])([^"']*)\1/i, (_m, q, rel) => `rel=${q}${rel} noopener noreferrer${q}`);
		}
		if (!/\bclass\s*=/i.test(next)) {
			next = `${next} class="${LINK_CLASS}"`;
		} else if (!new RegExp(`\\b${LINK_CLASS}\\b`).test(next)) {
			next = next.replace(/\bclass\s*=\s*(["'])([^"']*)\1/i, (_m, q, cls) => `class=${q}${cls} ${LINK_CLASS}${q}`);
		}
		return `<a${next}>`;
	});
}

function processFile(path) {
	const before = readFileSync(path, 'utf8');
	let after = linkBareUrls(before);
	after = ensureExternalAnchorTargets(after);
	if (after === before) return false;
	writeFileSync(path, after, 'utf8');
	return true;
}

const targets = [
	join(siteRoot, 'lessons'),
	join(siteRoot, 'tao'),
	join(siteRoot, 'bibliography'),
	join(siteRoot, 'directory'),
	join(siteRoot, 'methodology'),
];

let changed = 0;
let scanned = 0;
for (const root of targets) {
	for (const file of filesUnder(root)) {
		scanned += 1;
		if (processFile(file)) changed += 1;
	}
}
console.log(`Linked external reference URLs in ${changed}/${scanned} HTML file(s).`);
