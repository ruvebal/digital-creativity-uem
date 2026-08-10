#!/usr/bin/env node
/**
 * href-tester.mjs
 *
 * Usage:
 *   pnpm run href-tester -- [<rootDir> ...] [--exclude-dirs <glob> ...]
 * Example:
 *   pnpm run href-tester -- docs ../student-project-template --exclude-dirs _* templates
 *
 * Scans Markdown files for external links [text](url) and checks HTTP status (HEAD then GET fallback).
 * Writes two YAML files under docs/_data (always under web-foundations/docs/_data):
 *   - references.yml: consolidated database of scanned references
 *   - date-errors.yml: errors for the current run (non-200 or failures)
 */
import { load as cheerioLoad } from 'cheerio';
import { glob } from 'glob';
import matter from 'gray-matter';
import crypto from 'node:crypto';
import fssync from 'node:fs';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
let PRETTIER_NOTICE_DONE = false;

function parseArgs(argv) {
	/**
	 * Backwards-compatible CLI:
	 * - positional args are treated as one or more scan roots
	 * - if no root is provided, we scan:
	 *   - web-foundations/docs (includes tracks, lessons, etc.)
	 *   - ../student-project-template (repo-level template, outside web-foundations)
	 */
	const args = { roots: [], exclude: [] };
	const rest = argv.slice(2);
	for (let i = 0; i < rest.length; i++) {
		const token = rest[i];
		if (!token) continue;
		if (!token.startsWith('--')) {
			args.roots.push(token);
			continue;
		}
		if (token === '--exclude-dirs') {
			i++;
			while (i < rest.length && rest[i] && !rest[i].startsWith('--')) {
				args.exclude.push(rest[i]);
				i++;
			}
			i--; // step back one since for loop will increment
		}
	}
	return args;
}

function isExternalUrl(href) {
	return /^https?:\/\//i.test(href);
}

function uniqueKey({ url }) {
	return url.toLowerCase();
}

async function ensureDir(dir) {
	await fs.mkdir(dir, { recursive: true });
}

function nowIso() {
	return new Date().toISOString();
}

function extractLinksFromMarkdown(content) {
	// Matches [text](url) but ignores images ![alt](src) and inline code blocks
	const linkRegex = /(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
	const links = [];
	let match;
	while ((match = linkRegex.exec(content)) !== null) {
		links.push(match[1]);
	}
	return links;
}

async function headOrGet(url, controller) {
	const common = {
		headers: {
			Accept: 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
			'User-Agent': 'hc-app-design-href-tester/1.0',
		},
		signal: controller?.signal,
	};
	try {
		const res = await fetch(url, { method: 'HEAD', ...common });
		if (res.ok) return res;
	} catch (e) {
		// ignore, try GET
	}
	const res = await fetch(url, { method: 'GET', redirect: 'follow', ...common });
	return res;
}

function stripTags(html) {
	return html
		.replace(/<script[\s\S]*?<\/script>/gi, '')
		.replace(/<style[\s\S]*?<\/style>/gi, '')
		.replace(/<[^>]+>/g, ' ')
		.replace(/\s+/g, ' ')
		.trim();
}

function getAttr(tagHtml, attr) {
	const m = tagHtml.match(new RegExp(`${attr}=["']([^"']+)["']`, 'i'));
	return m ? m[1] : null;
}

function sha1(input) {
	return crypto.createHash('sha1').update(input).digest('hex');
}

function parseConceptDoc(htmlText, finalUrl) {
	const urlObj = new URL(finalUrl);
	const doc = {
		id: sha1(finalUrl),
		url: finalUrl,
		domain: urlObj.hostname,
		lang: null,
		page: {
			title: null,
			description: null,
			keywords: undefined,
			headings: { h1: [], h2: [], h3: [] },
			images: { og: null, icons: [] },
			canonical: null,
			alternates: [],
			feeds: [],
			dates: { published: null, modified: null },
			author: { name: null, url: null, org: null },
			license: null,
			robots: null,
		},
		social: {
			og: { title: null, type: null, siteName: null, url: null, image: null },
			twitter: { card: null, site: null, creator: null, image: null },
		},
		structuredData: { types: [], entities: [] },
		links: { inPage: [], out: [], rels: [], sitemap: null },
		tech: undefined,
		text: { readableTitle: null, readableText: null },
		tags: undefined,
		topics: undefined,
		entities: undefined,
		embeddings: undefined,
	};

	// html lang
	try {
		const $ = cheerioLoad(htmlText);
		const htmlLang = $('html').attr('lang');
		if (htmlLang) doc.lang = String(htmlLang).toLowerCase();

		// Title and basic metas
		doc.page.title = ($('title').first().text() || '').trim() || null;
		const metaName = (n) => $('meta[name="' + n + '"]').attr('content') || null;
		const metaProp = (p) => $('meta[property="' + p + '"]').attr('content') || null;
		doc.page.description = metaName('description');
		const kw = metaName('keywords');
		if (kw)
			doc.page.keywords = kw
				.split(',')
				.map((s) => s.trim())
				.filter(Boolean);
		doc.page.robots = metaName('robots');
		doc.page.license = metaName('license') || $('link[rel="license"]').attr('href') || null;

		// Headings
		$('h1').each((_, el) => doc.page.headings.h1.push($(el).text().trim()));
		$('h2').each((_, el) => doc.page.headings.h2.push($(el).text().trim()));
		$('h3').each((_, el) => doc.page.headings.h3.push($(el).text().trim()));
		doc.page.headings.h1 = doc.page.headings.h1.slice(0, 5);
		doc.page.headings.h2 = doc.page.headings.h2.slice(0, 20);
		doc.page.headings.h3 = doc.page.headings.h3.slice(0, 40);

		// Images
		doc.page.images.og = metaProp('og:image');
		$('link[rel*="icon"], link[rel="apple-touch-icon"]').each((_, el) => {
			const href = $(el).attr('href');
			if (href) doc.page.images.icons.push(new URL(href, finalUrl).href);
		});

		// Canonical, alternates, feeds
		const canonical = $('link[rel="canonical"]').attr('href');
		doc.page.canonical = canonical ? new URL(canonical, finalUrl).href : null;
		$('link[rel="alternate"]').each((_, el) => {
			const href = $(el).attr('href');
			const hreflang = $(el).attr('hreflang');
			const type = ($(el).attr('type') || '').toLowerCase();
			if (hreflang && href)
				doc.page.alternates.push({ hreflang: hreflang.toLowerCase(), url: new URL(href, finalUrl).href });
			if (href && (type.includes('rss') || type.includes('atom') || type.includes('json')))
				doc.page.feeds.push(new URL(href, finalUrl).href);
		});

		// Dates
		doc.page.dates.published = metaProp('article:published_time') || metaName('pubdate');
		doc.page.dates.modified = metaProp('article:modified_time') || metaName('lastmod');

		// Author
		doc.page.author.name = metaName('author') || metaProp('article:author');
		const authorLink = $('link[rel="author"]').attr('href');
		if (authorLink) doc.page.author.url = new URL(authorLink, finalUrl).href;
		const publisher = metaName('publisher') || metaProp('og:site_name');
		if (publisher) doc.page.author.org = publisher;

		// Social OG/Twitter
		doc.social.og.title = metaProp('og:title');
		doc.social.og.type = metaProp('og:type');
		doc.social.og.siteName = metaProp('og:site_name');
		doc.social.og.url = metaProp('og:url');
		doc.social.og.image = metaProp('og:image');
		doc.social.twitter.card = metaName('twitter:card');
		doc.social.twitter.site = metaName('twitter:site');
		doc.social.twitter.creator = metaName('twitter:creator');
		doc.social.twitter.image = metaName('twitter:image');

		// Structured data JSON-LD
		$('script[type="application/ld+json"]').each((_, el) => {
			try {
				const txt = $(el).text();
				if (!txt) return;
				const json = JSON.parse(txt);
				const items = Array.isArray(json) ? json : [json];
				for (const it of items) {
					const t = it['@type'];
					if (t) {
						if (Array.isArray(t)) doc.structuredData.types.push(...t.map(String));
						else doc.structuredData.types.push(String(t));
					}
					const entity = {
						id: it['@id'] || it.url || undefined,
						type: Array.isArray(t) ? t[0] : t || 'Thing',
						name: it.name || undefined,
						sameAs: it.sameAs || undefined,
						url: it.url || undefined,
					};
					if (entity.id || entity.name) doc.structuredData.entities.push(entity);
				}
			} catch {}
		});

		// Links in page
		const outSet = new Set();
		const inPageSet = new Set();
		$('a[href]').each((_, el) => {
			const href = $(el).attr('href');
			if (!href) return;
			if (href.startsWith('#')) inPageSet.add(href);
			else if (/^https?:\/\//i.test(href)) outSet.add(new URL(href, finalUrl).href);
		});
		doc.links.inPage = Array.from(inPageSet);
		doc.links.out = Array.from(outSet);

		// Link rels
		$('link[rel][href]').each((_, el) => {
			const rel = ($(el).attr('rel') || '').toString();
			const href = $(el).attr('href');
			if (!href) return;
			doc.links.rels.push({ rel, href: new URL(href, finalUrl).href });
		});

		// Text snapshot
		doc.text.readableTitle = doc.page.headings.h1[0] || doc.page.title;
		const paras = [];
		$('p').each((_, el) => {
			if (paras.length < 5) paras.push(($(el).text() || '').trim());
		});
		doc.text.readableText = paras.filter(Boolean).join('\n\n') || null;
	} catch {
		// Fallback regex path (existing implementation)
		const htmlLang = htmlText.match(/<html[^>]*lang=["']([^"']+)["'][^>]*>/i)?.[1];
		if (htmlLang) doc.lang = htmlLang.toLowerCase();
		doc.page.title = htmlText.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1]?.trim() || null;
		const metaByName = (n) =>
			htmlText.match(new RegExp(`<meta[^>]+name=["']${n}["'][^>]+content=["']([^"']+)["'][^>]*>`, 'i'))?.[1] || null;
		const metaByProp = (p) =>
			htmlText.match(new RegExp(`<meta[^>]+property=["']${p}["'][^>]+content=["']([^"']+)["'][^>]*>`, 'i'))?.[1] || null;
		doc.page.description = metaByName('description');
		const kw = metaByName('keywords');
		if (kw)
			doc.page.keywords = kw
				.split(',')
				.map((s) => s.trim())
				.filter(Boolean);
		doc.page.robots = metaByName('robots');
		doc.page.license =
			metaByName('license') ||
			htmlText.match(/<link[^>]+rel=["']license["'][^>]+href=["']([^"']+)["'][^>]*>/i)?.[1] ||
			null;
		const h1Re = /<h1[^>]*>([\s\S]*?)<\/h1>/gi;
		let m;
		while ((m = h1Re.exec(htmlText)) !== null) doc.page.headings.h1.push(stripTags(m[1]));
	}

	// Title and basic metas
	doc.page.title = htmlText.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1]?.trim() || null;
	const metaByName = (n) =>
		htmlText.match(new RegExp(`<meta[^>]+name=["']${n}["'][^>]+content=["']([^"']+)["'][^>]*>`, 'i'))?.[1] || null;
	const metaByProp = (p) =>
		htmlText.match(new RegExp(`<meta[^>]+property=["']${p}["'][^>]+content=["']([^"']+)["'][^>]*>`, 'i'))?.[1] || null;
	doc.page.description = metaByName('description');
	const kw = metaByName('keywords');
	if (kw)
		doc.page.keywords = kw
			.split(',')
			.map((s) => s.trim())
			.filter(Boolean);
	doc.page.robots = metaByName('robots');
	doc.page.license =
		metaByName('license') ||
		htmlText.match(/<link[^>]+rel=["']license["'][^>]+href=["']([^"']+)["'][^>]*>/i)?.[1] ||
		null;

	// Headings
	const h1Re = /<h1[^>]*>([\s\S]*?)<\/h1>/gi;
	const h2Re = /<h2[^>]*>([\s\S]*?)<\/h2>/gi;
	const h3Re = /<h3[^>]*>([\s\S]*?)<\/h3>/gi;
	let m;
	while ((m = h1Re.exec(htmlText)) !== null) doc.page.headings.h1.push(stripTags(m[1]));
	while ((m = h2Re.exec(htmlText)) !== null) doc.page.headings.h2.push(stripTags(m[1]));
	while ((m = h3Re.exec(htmlText)) !== null) doc.page.headings.h3.push(stripTags(m[1]));

	// Images
	doc.page.images.og = metaByProp('og:image');
	const iconRe = /<link[^>]+rel=["'][^"']*icon[^"']*["'][^>]*>/gi;
	let mi;
	while ((mi = iconRe.exec(htmlText)) !== null) {
		const href = getAttr(mi[0], 'href');
		if (href) doc.page.images.icons.push(href);
	}

	// Canonical, alternates, feeds
	doc.page.canonical = htmlText.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']+)["'][^>]*>/i)?.[1] || null;
	const altLinkRe = /<link[^>]+rel=["']alternate["'][^>]*>/gi;
	let la;
	while ((la = altLinkRe.exec(htmlText)) !== null) {
		const relTag = la[0];
		const hreflang = getAttr(relTag, 'hreflang');
		const href = getAttr(relTag, 'href');
		const type = getAttr(relTag, 'type')?.toLowerCase() || '';
		if (hreflang && href) doc.page.alternates.push({ hreflang: hreflang.toLowerCase(), url: href });
		if (href && (type.includes('rss') || type.includes('atom') || type.includes('json'))) doc.page.feeds.push(href);
	}

	// Dates
	doc.page.dates.published = metaByProp('article:published_time');
	doc.page.dates.modified = metaByProp('article:modified_time');

	// Author
	doc.page.author.name = metaByName('author');
	const authorLink = htmlText.match(/<link[^>]+rel=["']author["'][^>]+href=["']([^"']+)["'][^>]*>/i)?.[1] || null;
	if (authorLink) doc.page.author.url = authorLink;
	const publisher =
		htmlText.match(/<meta[^>]+property=["']article:publisher["'][^>]+content=["']([^"']+)["'][^>]*>/i)?.[1] || null;
	if (publisher) doc.page.author.org = publisher;

	// Social OG/Twitter
	doc.social.og.title = metaByProp('og:title');
	doc.social.og.type = metaByProp('og:type');
	doc.social.og.siteName = metaByProp('og:site_name');
	doc.social.og.url = metaByProp('og:url');
	doc.social.og.image = metaByProp('og:image');
	doc.social.twitter.card = metaByName('twitter:card');
	doc.social.twitter.site = metaByName('twitter:site');
	doc.social.twitter.creator = metaByName('twitter:creator');
	doc.social.twitter.image = metaByName('twitter:image');

	// Structured data JSON-LD
	const ldRe = /<script[^>]+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;
	let ld;
	while ((ld = ldRe.exec(htmlText)) !== null) {
		try {
			const json = JSON.parse(ld[1]);
			const items = Array.isArray(json) ? json : [json];
			for (const it of items) {
				const t = it['@type'];
				if (t) {
					if (Array.isArray(t)) doc.structuredData.types.push(...t.map(String));
					else doc.structuredData.types.push(String(t));
				}
				const entity = {
					id: it['@id'] || it.url || undefined,
					type: Array.isArray(t) ? t[0] : t || 'Thing',
					name: it.name || undefined,
					sameAs: it.sameAs || undefined,
					url: it.url || undefined,
				};
				if (entity.id || entity.name) doc.structuredData.entities.push(entity);
			}
		} catch {}
	}

	// Links in page
	const aRe = /<a\s+[^>]*href=["']([^"'#]+|#[^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi;
	let al;
	const outSet = new Set();
	const inPageSet = new Set();
	while ((al = aRe.exec(htmlText)) !== null) {
		const href = al[1];
		if (!href) continue;
		if (href.startsWith('#')) inPageSet.add(href);
		else if (/^https?:\/\//i.test(href)) outSet.add(href);
	}
	doc.links.inPage = Array.from(inPageSet);
	doc.links.out = Array.from(outSet);

	// Link rels
	const linkRe = /<link\s+[^>]*rel=["']([^"']+)["'][^>]*href=["']([^"']+)["'][^>]*>/gi;
	let lr;
	while ((lr = linkRe.exec(htmlText)) !== null) {
		doc.links.rels.push({ rel: lr[1], href: lr[2] });
	}

	// Text snapshot
	doc.text.readableTitle = doc.page.headings.h1[0] || doc.page.title;
	const pRe = /<p[^>]*>([\s\S]*?)<\/p>/gi;
	let p;
	const paras = [];
	while ((p = pRe.exec(htmlText)) !== null && paras.length < 5) paras.push(stripTags(p[1]));
	doc.text.readableText = paras.join('\n\n') || null;

	// Tags (from keywords)
	if (doc.page.keywords) doc.tags = doc.page.keywords.map((s) => s.toLowerCase());

	// Fallback lang if missing: from URL path
	if (!doc.lang) {
		const segs = urlObj.pathname.split('/').filter(Boolean);
		const hint = segs[0]?.toLowerCase();
		if (hint === 'en' || hint === 'es' || hint === 'fr' || hint === 'de') doc.lang = hint;
	}

	return doc;
}

function inferTopicsFromText(text) {
	if (!text) return [];
	const lc = text.toLowerCase();
	const topics = new Set();
	const addIf = (re, label) => {
		if (re.test(lc)) topics.add(label);
	};
	addIf(/accessibilit(y|ies)|wcag|aria|a11y/, 'accessibility');
	addIf(/seo|search(\s+)?engine|meta\s+description|sitemap/, 'seo');
	addIf(/performance|lighthouse|core\s+web\s+vitals|cls|lcp|fid|ttfb/, 'performance');
	addIf(/javascript|js\b|typescript|node\b/, 'javascript');
	addIf(/css\b|grid|flexbox|responsive|layout/, 'css');
	addIf(/design|typography|color|visual|ui\b|ux\b/, 'design');
	addIf(/privacy|gdpr|consent|cookies?/, 'privacy');
	addIf(/ethic(s|al)|bias|fairness|equity/, 'ethics');
	addIf(/sustainab(le|ility)|carbon|energy/, 'sustainability');
	return Array.from(topics);
}

function extractEntitiesFromText(text) {
	if (!text) return [];
	const entities = new Set();
	const re = /\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\b/g;
	let m;
	let count = 0;
	while ((m = re.exec(text)) !== null && count < 50) {
		const val = m[1].trim();
		if (val.length > 2) {
			entities.add(val);
			count++;
		}
	}
	return Array.from(entities);
}

function buildGraph(references) {
	const urlToId = new Map();
	for (const r of references) urlToId.set(r.url, r.doc?.id || r.url);

	const nodes = [];
	const edges = [];
	const nodeIds = new Set();
	const addNode = (id, label, type, extra = {}) => {
		if (nodeIds.has(id)) return;
		nodes.push({ data: { id, label, type, ...extra } });
		nodeIds.add(id);
	};
	const addEdge = (source, target, label) => {
		const id = `${source}->${target}:${label}`;
		edges.push({ data: { id, source, target, label } });
	};

	for (const r of references) {
		const doc = r.doc || {};
		const id = doc.id || r.url;
		const siteName = doc.social?.og?.siteName || doc.domain || '';
		const title = (doc.page?.title || '(no title)').trim();
		const statusTxt = r.status ? ` (${r.status})` : '';
		const label = `${title} | ${siteName}${statusTxt} • ${doc.domain || ''}`.trim();
		addNode(id, label, 'doc', { url: r.url, domain: doc.domain, lang: doc.lang, status: r.status, sources: r.sources });

		// Link edges to other known docs
		for (const outUrl of doc.links?.out || []) {
			const targetId = urlToId.get(outUrl);
			if (targetId) addEdge(id, targetId, 'links');
		}

		// Tags
		for (const tag of doc.tags || []) {
			const tagId = `tag:${tag}`;
			addNode(tagId, tag, 'tag');
			addEdge(id, tagId, 'hasTag');
		}

		// Entities (mentions)
		for (const ent of doc.entities || []) {
			const name = typeof ent === 'string' ? ent : ent.name || String(ent);
			const eid = `entity:${sha1(name)}`;
			addNode(eid, name, 'entity', { type: ent.type || 'Mention' });
			addEdge(id, eid, 'mentions');
		}
	}

	return { elements: { nodes, edges } };
}

function categorize(url, meta) {
	const u = new URL(meta?.url || url);
	const hostname = u.hostname;
	const path = u.pathname.toLowerCase();
	const categories = [];
	if (/\b(guide|docs|documentation|manual)\b/.test(path)) categories.push('documentation');
	if (/\b(blog|news|article|post)\b/.test(path)) categories.push('article');
	if (/\b(wiki)\b/.test(hostname + path)) categories.push('wiki');
	if (/\b(github|gitlab|bitbucket)\b/.test(hostname)) categories.push('code');
	if (/\b(w3c|whatwg|mdn|developer\.mozilla)\b/.test(hostname)) categories.push('standards');
	if (/\b(webby|awwwards|cssdesignawards|thefwa)\b/.test(hostname + path)) categories.push('awards');
	if (/\b(edu|ac\.\w+)$/i.test(hostname)) categories.push('academic');
	if (categories.length === 0) categories.push('other');
	return categories;
}

function normalizeLineTerminators(str) {
	if (typeof str !== 'string') return str;
	// Replace Line Separator (U+2028) and Paragraph Separator (U+2029) with newline
	// Also normalize CRLF to LF for consistency
	return str
		.replace(/\u2028|\u2029/g, '\n')
		.replace(/\r\n/g, '\n')
		.replace(/\r/g, '\n');
}

function toYaml(obj) {
	// Minimal YAML serializer for our simple structures
	const indent = (level) => '  '.repeat(level);
	const serialize = (val, level = 0) => {
		if (val === null || val === undefined) return 'null';
		if (typeof val === 'string') {
			// Normalize unusual line terminators before processing
			const normalized = normalizeLineTerminators(val);
			if (/[:\-?\[\]{}#,&*!|>'"%@`\n]/.test(normalized)) {
				// quote and escape as needed (basic)
				return JSON.stringify(normalized);
			}
			return normalized;
		}
		if (typeof val === 'number' || typeof val === 'boolean') return String(val);
		if (Array.isArray(val)) {
			if (val.length === 0) return '[]';
			return val
				.map((item) => {
					const isComplex = item !== null && typeof item === 'object';
					if (isComplex) {
						const body = serialize(item, level + 1);
						return `${indent(level)}-\n${body}`;
					}
					return `${indent(level)}- ${serialize(item, level + 1)}`;
				})
				.join('\n');
		}
		if (typeof val === 'object') {
			return Object.entries(val)
				.map(([k, v]) => {
					if (Array.isArray(v)) {
						if (v.length === 0) return `${indent(level)}${k}: []`;
						const arrLines = v
							.map((item) => {
								const isComplex = item !== null && typeof item === 'object';
								if (isComplex) {
									const body = serialize(item, level + 2);
									return `${indent(level + 1)}-\n${body}`;
								}
								return `${indent(level + 1)}- ${serialize(item, level + 2)}`;
							})
							.join('\n');
						return `${indent(level)}${k}:\n${arrLines}`;
					}
					if (v !== null && typeof v === 'object') {
						return `${indent(level)}${k}:\n${serialize(v, level + 1)}`;
					}
					return `${indent(level)}${k}: ${serialize(v, level + 1)}`;
				})
				.join('\n');
		}
		return String(val);
	};
	return serialize(obj, 0) + '\n';
}

async function formatWithPrettier(yamlText) {
	try {
		const prettier = await import('prettier');
		if (!PRETTIER_NOTICE_DONE) {
			console.log('[href-tester] Prettier detected; formatting YAML');
			PRETTIER_NOTICE_DONE = true;
		}
		return await prettier.format(yamlText, { parser: 'yaml' });
	} catch {
		if (!PRETTIER_NOTICE_DONE) {
			console.log('[href-tester] Prettier not available; writing YAML as-is');
			PRETTIER_NOTICE_DONE = true;
		}
		return yamlText; // Prettier not installed; skip formatting
	}
}

async function readYamlIfExists(filePath) {
	if (!fssync.existsSync(filePath)) return null;
	const text = await fs.readFile(filePath, 'utf8');
	// naive YAML parse via JSON since our writer is minimal – support arrays at root only
	try {
		// try JSON parse first (if manually edited)
		return JSON.parse(text);
	} catch {}
	// very naive YAML list parser (key: value pairs, two-level nesting)
	const lines = text.split(/\r?\n/);
	const items = [];
	let current = null;
	for (const line of lines) {
		if (/^\s*-\s*/.test(line)) {
			if (current) items.push(current);
			current = {};
			continue;
		}
		const m = line.match(/^\s*([A-Za-z0-9_]+):\s*(.*)$/);
		if (m && current) {
			const key = m[1];
			const value = m[2];
			current[key] = value === 'null' ? null : value.replace(/^"|"$/g, '');
		}
	}
	if (current) items.push(current);
	return items;
}

async function main() {
	const { roots, exclude } = parseArgs(process.argv);

	// web-foundations/ (project root for scripts)
	const wfRoot = path.resolve(__dirname, '..');
	// repo root (parent of web-foundations/)
	const repoRoot = path.resolve(wfRoot, '..');
	// site docs root (jekyll --source docs)
	const siteDocsRoot = path.join(wfRoot, 'docs');

	const effectiveRoots = roots.length > 0 ? roots : ['docs', 'student-project-template'];
	const rootAbsList = effectiveRoots
		.map((r) => (path.isAbsolute(r) ? r : path.resolve(wfRoot, r)))
		// normalize separators and remove trailing slashes
		.map((r) => r.replace(/[\\\/]+$/, ''))
		// dedupe
		.filter((r, idx, arr) => arr.indexOf(r) === idx)
		// remove roots that are contained within another root
		.filter((r, idx, arr) => !arr.some((other, j) => j !== idx && r.startsWith(other + path.sep)));

	// Always write outputs to web-foundations/docs/_data so Jekyll can consume them.
	const dataDir = path.join(siteDocsRoot, '_data');
	await ensureDir(dataDir);

	const ignoreGlobs = [...exclude.map((e) => `**/${e}/**`), '**/_site/**', '**/node_modules/**'];
	const sourceAbsBySourcePath = new Map();

	const allMdFiles = [];
	for (const rootAbs of rootAbsList) {
		const mdFiles = await glob('**/*.md', { cwd: rootAbs, ignore: ignoreGlobs, nodir: true });
		for (const relInRoot of mdFiles) {
			const abs = path.join(rootAbs, relInRoot);
			const isInSiteDocs = abs.startsWith(siteDocsRoot + path.sep);
			const sourcePath = isInSiteDocs
				? path.relative(siteDocsRoot, abs).split(path.sep).join('/')
				: path.relative(repoRoot, abs).split(path.sep).join('/');
			sourceAbsBySourcePath.set(sourcePath, abs);
			allMdFiles.push({ abs, sourcePath });
		}
	}

	console.log(`[href-tester] Scanning roots:\n- ${rootAbsList.join('\n- ')}`);
	console.log(`[href-tester] Excluding: ${exclude.length ? exclude.join(', ') : 'none'}`);
	console.log(`[href-tester] Found ${allMdFiles.length} Markdown files`);

	const seen = new Map();
	const errors = [];
	const datetime = nowIso();

	for (const { abs, sourcePath } of allMdFiles) {
		const src = await fs.readFile(abs, 'utf8');
		let content = src;
		let data = {};
		try {
			const parsed = matter(src);
			content = parsed.content;
			data = parsed.data || {};
		} catch (fmErr) {
			// Fallback: strip YAML front matter manually if present (--- ... ---)
			const fm = src.match(/^---[\s\S]*?\n---\s*\n([\s\S]*)$/);
			if (fm) content = fm[1];
		}
		const lang = data?.lang || (abs.includes('/en/') ? 'en' : abs.includes('/es/') ? 'es' : null);
		const links = extractLinksFromMarkdown(content);
		const externalLinks = links.filter(isExternalUrl);
		console.log(`[href-tester] File: ${sourcePath} — links: ${links.length}, external: ${externalLinks.length}`);
		for (const href of externalLinks) {
			const url = href;
			const key = uniqueKey({ url });
			if (seen.has(key)) {
				// still record source occurrence if new
				seen.get(key).sources.add(sourcePath);
				continue;
			}
			const controller = new AbortController();
			const timeout = setTimeout(() => controller.abort(), 20000);
			let res;
			let status = null;
			let ok = false;
			let error = null;
			try {
				res = await headOrGet(url, controller);
				status = res.status;
				ok = res.ok;
			} catch (e) {
				error = String(e?.message || e);
			} finally {
				clearTimeout(timeout);
			}

			let concept = null;
			try {
				if (res && ok) {
					// Prefer parsing HTML via GET to populate meta fields
					try {
						const htmlRes = await fetch(url, {
							method: 'GET',
							redirect: 'follow',
							headers: {
								Accept: 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8',
								'User-Agent': 'hc-app-design-href-tester/1.0',
							},
							signal: controller?.signal,
						});
						if (htmlRes.ok) {
							const finalUrl = htmlRes.url || url;
							const html = await htmlRes.text();
							concept = parseConceptDoc(html, finalUrl);
						}
					} catch {}
					// Fallback minimal concept if HTML fetch failed
					if (!concept) {
						const finalUrl = res.url || url;
						concept = {
							id: sha1(finalUrl),
							url: finalUrl,
							domain: new URL(finalUrl).hostname,
							lang: null,
							page: {
								title: null,
								description: null,
								keywords: undefined,
								headings: { h1: [], h2: [], h3: [] },
								images: { og: null, icons: [] },
								canonical: null,
								alternates: [],
								feeds: [],
								dates: { published: null, modified: null },
								author: { name: null, url: null, org: null },
								license: null,
								robots: null,
							},
							social: {
								og: { title: null, type: null, siteName: null, url: null, image: null },
								twitter: { card: null, site: null, creator: null, image: null },
							},
							structuredData: { types: [], entities: [] },
							links: { inPage: [], out: [], rels: [], sitemap: null },
							tech: undefined,
							text: { readableTitle: null, readableText: null },
							tags: undefined,
							topics: undefined,
							entities: undefined,
							embeddings: undefined,
						};
					}
				}
			} catch {}

			// Ensure concept object exists even on non-OK responses
			if (!concept) {
				const finalUrl = res?.url || url;
				concept = {
					id: sha1(finalUrl),
					url: finalUrl,
					domain: new URL(finalUrl).hostname,
					lang: null,
					page: {
						title: null,
						description: null,
						keywords: undefined,
						headings: { h1: [], h2: [], h3: [] },
						images: { og: null, icons: [] },
						canonical: null,
						alternates: [],
						feeds: [],
						dates: { published: null, modified: null },
						author: { name: null, url: null, org: null },
						license: null,
						robots: null,
					},
					social: {
						og: { title: null, type: null, siteName: null, url: null, image: null },
						twitter: { card: null, site: null, creator: null, image: null },
					},
					structuredData: { types: [], entities: [] },
					links: { inPage: [], out: [], rels: [], sitemap: null },
					tech: undefined,
					text: { readableTitle: null, readableText: null },
					tags: undefined,
					topics: undefined,
					entities: undefined,
					embeddings: undefined,
				};
			}

			// Enrich topics/entities (safe even if minimal concept)
			if (!concept.topics)
				concept.topics = inferTopicsFromText(concept.text?.readableText || concept.page?.description || '');
			if (!concept.entities) {
				const ents = extractEntitiesFromText(concept.text?.readableText || '');
				concept.entities = ents.map((name) => ({ name, type: 'Mention' }));
			}

			const item = {
				url,
				datetime,
				sources: new Set([sourcePath]),
				lang,
				status,
				ok,
				doc: concept,
			};
			seen.set(key, item);

			if (!ok) {
				errors.push({ url, status, error, source: sourcePath, datetime });
				console.error(
					`[href-tester] Error ${status ?? 'ERR'}: ${url} (source: ${sourcePath})${error ? ' - ' + error : ''}`
				);
			}
		}
	}

	// prepare references output as array
	let references = Array.from(seen.values())
		.filter((it) => it.ok && it.status && it.status < 400)
		.map((it) => ({
			url: it.url,
			datetime: it.datetime,
			sources: Array.from(it.sources).sort(),
			lang: it.lang,
			status: it.status,
			ok: it.ok,
			doc: it.doc,
		}))
		.sort((a, b) => a.url.localeCompare(b.url));

	// Enrich sources with titles and hrefs
	for (const ref of references) {
		const meta = [];
		for (const s of ref.sources || []) {
			try {
				const abs =
					sourceAbsBySourcePath.get(s) ||
					path.join(siteDocsRoot, s) ||
					path.join(repoRoot, s);
				const raw = await fs.readFile(abs, 'utf8');
				const fm = matter(raw).data || {};
				const title = fm.title || fm.title_alt || s;
				const isInSiteDocs = abs.startsWith(siteDocsRoot + path.sep);
				const docRel = isInSiteDocs
					? path.relative(siteDocsRoot, abs).split(path.sep).join('/')
					: null;
				const href = docRel ? ('/' + docRel).replace(/index\.md$/, '') : null;
				meta.push({ title, href, path: s });
			} catch {
				const abs = sourceAbsBySourcePath.get(s);
				const isInSiteDocs = abs ? abs.startsWith(siteDocsRoot + path.sep) : false;
				const docRel =
					abs && isInSiteDocs ? path.relative(siteDocsRoot, abs).split(path.sep).join('/') : null;
				const href = docRel ? ('/' + docRel).replace(/index\.md$/, '') : null;
				meta.push({ title: s, href, path: s });
			}
		}
		ref.sourcesMeta = meta;
	}

	const banner = `# DO NOT EDIT: generated by href-tester.mjs at ${datetime}\n# This file is overwritten on each run. Edit source Markdown instead.\n`;
	let referencesYaml = banner + toYaml({ references });
	let errorsYaml = banner + toYaml({ errors });

	// Prettify YAML if Prettier is available
	referencesYaml = await formatWithPrettier(referencesYaml);
	errorsYaml = await formatWithPrettier(errorsYaml);

	// Normalize line terminators in final output (ensure no LS/PS characters)
	referencesYaml = normalizeLineTerminators(referencesYaml);
	errorsYaml = normalizeLineTerminators(errorsYaml);

	const refPath = path.join(dataDir, 'references.yml');
	const errPath = path.join(dataDir, `${datetime.slice(0, 10)}-errors.yml`);
	await fs.writeFile(refPath, referencesYaml, 'utf8');
	await fs.writeFile(errPath, errorsYaml, 'utf8');
	console.log(`[href-tester] Wrote references: ${refPath}`);
	console.log(`[href-tester] Wrote errors: ${errPath}`);

	// Emit Cytoscape graph
	const graph = buildGraph(references);
	const graphPath = path.join(dataDir, 'graph.json');
	await fs.writeFile(graphPath, JSON.stringify(graph, null, 2), 'utf8');
	console.log(`[href-tester] Wrote graph: ${graphPath}`);

	// console output
	const errorCount = errors.length;
	if (errorCount > 0) {
		console.error(
			`[href-tester] Completed with ${errorCount} errors. See ${path.relative(siteDocsRoot, errPath)}`
		);
	} else {
		console.log('[href-tester] All external links returned 200 OK.');
	}
}

main().catch((e) => {
	console.error('[href-tester] Fatal error:', e);
	process.exit(1);
});
