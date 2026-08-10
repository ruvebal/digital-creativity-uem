#!/usr/bin/env node
/**
 * Analyze lessons.yml to find missing translations
 */

import { readFileSync } from 'fs';
import yaml from 'js-yaml';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const lessonsYamlPath = join(__dirname, '../docs/_data/lessons.yml');
const data = yaml.load(readFileSync(lessonsYamlPath, 'utf8'));

console.log('\n📋 LESSONS MISSING FROM INDEX PAGES:\n');
console.log('═'.repeat(60));

// Lessons with only ES (missing from EN index)
const esOnly = data.filter(l => l.path?.es && !l.path?.en);
console.log('\n❌ Missing from EN index (ES only):\n');
esOnly.forEach(l => {
  console.log(`  - ${l.title?.es || l.slug} (slug: ${l.slug})`);
  console.log(`    Path: ${l.path.es}`);
});
console.log(`\n  Total: ${esOnly.length} lessons\n`);

// Lessons with only EN (missing from ES index)
const enOnly = data.filter(l => l.path?.en && !l.path?.es);
console.log('❌ Missing from ES index (EN only):\n');
enOnly.forEach(l => {
  console.log(`  - ${l.title?.en || l.slug} (slug: ${l.slug})`);
  console.log(`    Path: ${l.path.en}`);
});
console.log(`\n  Total: ${enOnly.length} lessons\n`);

console.log('═'.repeat(60));
console.log(`\n✅ Summary:\n`);
console.log(`  - Spanish index: Shows ${data.filter(l => l.path?.es).length} lessons`);
console.log(`  - English index: Shows ${data.filter(l => l.path?.en).length} lessons`);
console.log(`  - ES-only lessons: ${esOnly.length} (not showing on EN index)`);
console.log(`  - EN-only lessons: ${enOnly.length} (not showing on ES index)`);
console.log();
