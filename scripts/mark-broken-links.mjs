#!/usr/bin/env node
/**
 * Mark broken links in generated HTML
 * Post-processes Jekyll HTML output to add visual indicators for broken links

 * Usage:
 *   pnpm run mark-broken-links
 * 
 * Or directly:
 *   node scripts/mark-broken-links.mjs
 * 
 * This script scans generated HTML in docs/ for <a> tags with hrefs that match
 * known broken links from the most recent *_errors.yml file,
 * and adds a CSS class or inline style to visually indicate them as broken.
 * 
 */

import { readFileSync, writeFileSync } from 'fs';
import { glob } from 'glob';
import yaml from 'js-yaml';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load error data from most recent date-errors.yml file
function loadErrorData() {
	const dataDir = join(__dirname, '../docs/_data');
	const errorFiles = glob.sync('*-errors.yml', { cwd: dataDir });

	if (errorFiles.length === 0) {
		console.log('[mark-broken-links] No error files found');
		return new Map();
	}

	// Get most recent file
	const latestFile = errorFiles.sort().reverse()[0];
	const errorPath = join(dataDir, latestFile);

	console.log(`[mark-broken-links] Loading errors from: ${latestFile}`);

	try {
		const content = readFileSync(errorPath, 'utf8');
		const data = yaml.load(content);

		// Build map of broken URLs
		const brokenUrls = new Map();
		for (const error of data.errors || []) {
			const url = error.url?.toLowerCase();
			if (url) {
				brokenUrls.set(url, error.status || 'ERROR');
			}
		}

		console.log(`[mark-broken-links] Found ${brokenUrls.size} broken URLs`);
		return brokenUrls;
	} catch (err) {
		console.error('[mark-broken-links] Error loading error file:', err.message);
		return new Map();
	}
}

// Process HTML file to mark broken links
function processFile(filePath, brokenUrls) {
	const content = readFileSync(filePath, 'utf8');
	let modified = false;
	const foundLinks = [];

	// Match <a href="...">...</a> tags
	const linkRegex = /<a\s+([^>]*href=["']([^"']+)["'][^>]*)>([\s\S]*?)<\/a>/gi;

	const newContent = content.replace(linkRegex, (match, attrs, href, linkText) => {
		// Skip if already marked or internal link
		if (match.includes('class="broken-link"') || !href.startsWith('http')) {
			return match;
		}

		const normalizedUrl = href.toLowerCase();
		if (brokenUrls.has(normalizedUrl)) {
			const status = brokenUrls.get(normalizedUrl);
			modified = true;
			foundLinks.push(href);
			// Wrap in <s> tag and add title attribute with status
			const newLink = `<a ${attrs} class="broken-link" title="Broken link (HTTP ${status})"><s>${linkText}</s></a>`;
			return newLink;
		}

		return match;
	});

	if (modified) {
		writeFileSync(filePath, newContent, 'utf8');
		const relativePath = filePath.replace(process.cwd() + '/_site/', '');
		console.log(`  ✓ ${relativePath} (${foundLinks.length} broken link${foundLinks.length > 1 ? 's' : ''})`);
		return true;
	}
	return false;
}

// Main execution
async function main() {
	const siteDir = join(process.cwd(), '_site');
	const brokenUrls = loadErrorData();

	if (brokenUrls.size === 0) {
		console.log('[mark-broken-links] No broken URLs to mark');
		return;
	}

	const htmlFiles = await glob('**/*.html', { cwd: siteDir, absolute: true });

	let count = 0;
	for (const file of htmlFiles) {
		if (processFile(file, brokenUrls)) {
			count++;
		}
	}

	console.log(`✅ Marked broken links in ${count} HTML files`);
}

main().catch(console.error);
