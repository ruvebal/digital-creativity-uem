import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { test } from 'node:test';
import yaml from 'js-yaml';

import { buildPages } from '../build-practice-quizzes.mjs';

const root = join(dirname(fileURLToPath(import.meta.url)), '../..');
const bank = yaml.load(readFileSync(join(root, 'digital-creativity-pedagogy/excellence/assessment/question-bank.yml'), 'utf8'));
const references = yaml.load(readFileSync(join(root, 'docs/_data/references.yml'), 'utf8'));
const pages = buildPages(bank, references);

test('practice index and quiz pages use distinct responsive layout wrappers in both locales', () => {
  assert.match(pages['docs/practice/en/index.html'], /practice-quiz--index/);
  assert.match(pages['docs/practice/en/i-6-volume/index.html'], /practice-quiz--page/);
  assert.match(pages['docs/practice/es/index.html'], /practice-quiz--index/);
  assert.match(pages['docs/practice/es/i-6-volumen/index.html'], /practice-quiz--page/);
});

test('Spanish I.6 practice route has five localized questions and lesson links', () => {
  const page = pages['docs/practice/es/i-6-volumen/index.html'];
  assert.equal((page.match(/class="practice-quiz__question"/g) || []).length, 5);
  assert.match(page, /lang: es/);
  assert.match(page, /Mostrar respuesta/);
  assert.match(page, /\/lessons\/es\/creacion-digital-i\/i-6-volumen\//);
  assert.match(page, /\/practice\/es\//);
});
