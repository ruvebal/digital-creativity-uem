#!/usr/bin/env node
/**
 * Comprehensive check of lessons indexing
 */

import { readFileSync } from 'fs';
import { glob } from 'glob';
import yaml from 'js-yaml';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Load lessons.yml
const lessonsYamlPath = join(__dirname, '../docs/_data/lessons.yml');
const lessonsData = yaml.load(readFileSync(lessonsYamlPath, 'utf8'));

// Find all actual lesson index.md files (excluding demo/README.md)
const esFiles = await glob('docs/lessons/es/**/index.md', { 
  cwd: join(__dirname, '..'),
  ignore: ['**/demo/**', '**/README.md']
});
const enFiles = await glob('docs/lessons/en/**/index.md', {
  cwd: join(__dirname, '..'),
  ignore: ['**/demo/**', '**/README.md']
});

// Convert file paths to URL paths
function filePathToUrlPath(filePath) {
  // Remove docs/ prefix and /index.md suffix
  const relative = filePath.replace(/^docs\//, '');
  return '/' + relative.replace(/\/index\.md$/, '/');
}

// Build maps
const indexedByPath = new Map();
lessonsData.forEach(lesson => {
  if (lesson.path?.es) indexedByPath.set(lesson.path.es, { ...lesson, lang: 'es' });
  if (lesson.path?.en) indexedByPath.set(lesson.path.en, { ...lesson, lang: 'en' });
});

const existingByPath = new Map();
esFiles.forEach(file => {
  const urlPath = filePathToUrlPath(file);
  existingByPath.set(urlPath, { file, lang: 'es' });
});
enFiles.forEach(file => {
  const urlPath = filePathToUrlPath(file);
  if (existingByPath.has(urlPath)) {
    existingByPath.get(urlPath).lang = 'both';
  } else {
    existingByPath.set(urlPath, { file, lang: 'en' });
  }
});

// Find missing entries
const missingFromYaml = [];
existingByPath.forEach(({ file, lang }, path) => {
  if (!indexedByPath.has(path)) {
    missingFromYaml.push({ path, file, lang });
  }
});

// Find entries in YAML but missing files
const missingFiles = [];
indexedByPath.forEach((lesson, path) => {
  if (!existingByPath.has(path)) {
    missingFiles.push({ path, slug: lesson.slug, lang: lesson.lang });
  }
});

// Print comprehensive report
console.log('\n📚 COMPREHENSIVE LESSON INDEXING REPORT\n');
console.log('═'.repeat(60));
console.log(`Total indexed in YAML: ${indexedByPath.size} paths`);
console.log(`Total existing files: ${existingByPath.size} paths`);
console.log('═'.repeat(60));

if (missingFromYaml.length > 0) {
  console.log(`\n❌ MISSING FROM lessons.yml (${missingFromYaml.length} files):\n`);
  missingFromYaml.forEach(({ path, file, lang }) => {
    console.log(`  [${lang.toUpperCase()}] ${path}`);
    console.log(`      File: ${file}`);
    
    // Try to suggest slug and title
    const slug = path.split('/').filter(Boolean).slice(-1)[0] || 'unknown';
    console.log(`      Suggested slug: ${slug}`);
    console.log();
  });
} else {
  console.log('\n✅ All existing lesson files are indexed in lessons.yml');
}

if (missingFiles.length > 0) {
  console.log(`\n⚠️  IN YAML BUT FILE NOT FOUND (${missingFiles.length} entries):\n`);
  missingFiles.forEach(({ path, slug, lang }) => {
    console.log(`  [${lang.toUpperCase()}] ${path}`);
    console.log(`      Slug: ${slug}`);
    console.log();
  });
}

// Summary by language
console.log('\n📊 SUMMARY BY LANGUAGE:\n');
const esIndexed = Array.from(indexedByPath.values()).filter(l => l.lang === 'es').length;
const enIndexed = Array.from(indexedByPath.values()).filter(l => l.lang === 'en').length;
const esFilesCount = esFiles.length;
const enFilesCount = enFiles.length;

console.log(`Spanish (ES):`);
console.log(`  - Indexed in YAML: ${esIndexed}`);
console.log(`  - Existing files: ${esFilesCount}`);
console.log(`  - Missing from YAML: ${missingFromYaml.filter(m => m.lang === 'es').length}`);
console.log(`\nEnglish (EN):`);
console.log(`  - Indexed in YAML: ${enIndexed}`);
console.log(`  - Existing files: ${enFilesCount}`);
console.log(`  - Missing from YAML: ${missingFromYaml.filter(m => m.lang === 'en').length}`);

console.log('\n' + '═'.repeat(60));
console.log('✅ Report complete!\n');
