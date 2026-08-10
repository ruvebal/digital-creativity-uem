#!/usr/bin/env node
/**
 * Normalize Spanish/European accents in Kramdown-generated heading IDs
 * Post-processes Jekyll HTML output to convert accented IDs to ASCII
 */

import { readFileSync, writeFileSync } from 'fs';
import { glob } from 'glob';
import { join } from 'path';

const ACCENT_MAP = {
  'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
  'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
  'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
  'ã': 'a', 'õ': 'o',
  'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
  'ç': 'c',
  'ñ': 'n',
  'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
  'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
  'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
  'Ã': 'A', 'Õ': 'O',
  'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
  'Ç': 'C',
  'Ñ': 'N'
};

function normalize(text) {
  let result = text;
  // Remove leading hyphens from IDs (Kramdown generates these for non-word characters)
  result = result.replace(/^-+/, '');
  for (const [accent, normal] of Object.entries(ACCENT_MAP)) {
    result = result.replace(new RegExp(accent, 'g'), normal);
  }
  return result;
}

function processFile(filePath) {
  const content = readFileSync(filePath, 'utf8');
  let modified = false;
  
  // Normalize all heading IDs
  let newContent = content.replace(/id="([^"]*)"/g, (match, id) => {
    const normalized = normalize(id);
    if (normalized !== id) {
      modified = true;
      return `id="${normalized}"`;
    }
    return match;
  });
  
  // Normalize all href links to headings
  newContent = newContent.replace(/href="#([^"]*)"/g, (match, anchor) => {
    const normalized = normalize(anchor);
    if (normalized !== anchor) {
      modified = true;
      return `href="#${normalized}"`;
    }
    return match;
  });
  
  // Remove plaintext class from inline code blocks
  newContent = newContent.replace(/<code class="language-plaintext highlighter-rouge">/g, (match) => {
    modified = true;
    return '<code>';
  });
  
  // Only write if modified
  if (modified) {
    writeFileSync(filePath, newContent, 'utf8');
    return true;
  }
  return false;
}

// Main
async function main() {
  const siteDir = join(process.cwd(), '_site');
  const htmlFiles = await glob('**/*.html', { cwd: siteDir, absolute: true });
  
  let count = 0;
  for (const file of htmlFiles) {
    if (processFile(file)) {
      count++;
    }
  }
  
  console.log(`✅ Normalized accents in ${count} HTML files`);
}

main().catch(console.error);

