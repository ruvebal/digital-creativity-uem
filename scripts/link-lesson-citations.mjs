#!/usr/bin/env node
/**
 * Link published Chicago author-date citations to their local reference-list
 * entries. Source lessons remain readable instructor material; anchors are
 * applied to generated HTML after Jekyll has rendered Markdown.
 */
import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const siteRoot = resolve(process.cwd(), '_site', 'lessons');

function filesUnder(directory) {
  if (!statSync(directory, { throwIfNoEntry: false })) return [];
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    return entry.isDirectory() ? filesUnder(path) : (path.endsWith('.html') ? [path] : []);
  });
}

function slug(value) {
  return value.normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

function referenceKey(reference) {
  const text = reference.replace(/<[^>]+>/g, ' ').replace(/&[^;]+;/g, ' ');
  if (/^\s*(?:Missing evidence|Evidencia faltante|Bibliography|Bibliografía)/i.test(text)) return null;
  const year = text.match(/\b(19|20)\d{2}\b/);
  if (!year) return null;
  const author = text.match(/^\s*([A-ZÁÉÍÓÚÑ][\p{L}'’.-]+),/u);
  return author ? `${slug(author[1])}-${year[0]}` : null;
}

function processFile(path) {
  const before = readFileSync(path, 'utf8');
  const heading = before.match(/<h2 id="(?:references|referencias)">(?:References|Referencias)<\/h2>\s*<ul>([\s\S]*?)<\/ul>/i);
  if (!heading) return false;
  const keys = new Set();
  const list = heading[1].replace(/<li(?![^>]*\bid=)([^>]*)>([\s\S]*?)<\/li>/gi, (match, attrs, entry) => {
    const key = referenceKey(entry);
    if (!key || keys.has(key)) return match;
    keys.add(key);
    return `<li${attrs} id="ref-${key}">${entry}</li>`;
  });
  let after = before.replace(heading[0], heading[0].replace(heading[1], list));
  const [body, references] = after.split(heading[0].replace(heading[1], list));
  if (references === undefined) return false;
  const linkedBody = body.replace(/\(([^()\n]{1,80}?)\s+((?:19|20)\d{2})(,\s*\d+(?:[–-]\d+)?)?\)/g, (match, authors, year, pages = '') => {
    if (authors.includes('<') || authors.includes('>')) return match;
    const firstAuthor = authors.trim().split(/[\s,;&]/)[0];
    const key = `${slug(firstAuthor)}-${year}`;
    return keys.has(key) ? `<a class="citation-link" href="#ref-${key}" aria-label="Jump to ${authors} ${year} in the reference list">${match}</a>` : match;
  });
  after = `${linkedBody}${heading[0].replace(heading[1], list)}${references}`;
  if (after === before) return false;
  writeFileSync(path, after, 'utf8');
  return true;
}

let changed = 0;
for (const file of filesUnder(siteRoot)) if (processFile(file)) changed += 1;
console.log(`Linked citations in ${changed} lesson HTML file(s).`);
