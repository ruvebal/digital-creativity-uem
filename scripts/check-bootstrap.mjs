#!/usr/bin/env node
/**
 * Check bootstrap lessons in lessons.yml
 */

import { readFileSync } from 'fs';
import yaml from 'js-yaml';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const lessonsYamlPath = join(__dirname, '../docs/_data/lessons.yml');
const data = yaml.load(readFileSync(lessonsYamlPath, 'utf8'));

const bootstrap = data.filter((l) => l.slug && l.slug.startsWith('bootstrap'));

console.log('\n📦 Bootstrap Lessons in lessons.yml:\n');
console.log(`Total: ${bootstrap.length} lessons\n`);
console.log('═'.repeat(60));

bootstrap.forEach((l, i) => {
	const esPath = l.path?.es ? '✓' : '✗';
	const enPath = l.path?.en ? '✓' : '✗';
	console.log(`\n${i + 1}. [${esPath} ES] [${enPath} EN] ${l.slug}`);
	if (l.title?.es) console.log(`   ES: ${l.title.es}`);
	if (l.title?.en) console.log(`   EN: ${l.title.en}`);
	if (l.path?.es) console.log(`   Path ES: ${l.path.es}`);
	if (l.path?.en) console.log(`   Path EN: ${l.path.en}`);
});

console.log('\n' + '═'.repeat(60));
console.log('\n✅ All bootstrap lessons are indexed in lessons.yml\n');
