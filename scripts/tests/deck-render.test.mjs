/**
 * Deck pre-renderer (PHASE-EX5, FINDINGS B4 / B5).
 *   node --test scripts/tests/
 */
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

import {
  captionHtml,
  diagramCaptionHtml,
  escapeHtml,
  geometricCaptionHtml,
  layoutFor,
  licenceLabel,
  notesHtml,
  parseHashedSvgName,
  questionsHtml,
  renderDeck,
  timerFor,
  withBase,
} from '../lib/deck-render.mjs';

const root = join(dirname(fileURLToPath(import.meta.url)), '../..');
const geometricDir = join(root, 'docs/assets/images/fractal-pass-track');

const CC_ASSET = {
  media_slot_id: 'I.1.masterclass-1',
  asset_id: 'wikimedia:File:Example.jpg',
  asset_url: '/digital-creativity-uem/assets/images/deck-media/abc.webp',
  title: 'File:Example work [modern_rights_review_required]',
  alt_text: 'A drawing of a chair.',
  author: 'Ada Example',
  licence: 'CC-BY-SA-4.0',
  licence_url: 'https://creativecommons.org/licenses/by-sa/4.0/',
  canonical_source_url: 'https://commons.wikimedia.org/wiki/File:Example.jpg',
};

const CTX = {
  base: '/digital-creativity-uem',
  geometric: [
    'uem-henon-pass-01-structure-2fc3613c22a1.svg',
    'uem-henon-pass-02-threshold-c378606cc29b.svg',
  ],
  koch: 'uem-diagram-fallback-2fc3613c22a1.svg',
};

const deck = (slides, assets = []) => ({ schema_version: 2, unit_label: 'Unit', slides, assets });

test('caption shows title · author · licence linked · source link', () => {
  const html = captionHtml(CC_ASSET);
  assert.match(html, /Example work/);
  assert.doesNotMatch(html, /review_required/);
  assert.match(html, /Ada Example/);
  assert.match(html, /CC BY-SA 4\.0/);
  assert.match(html, />Source</);
});

test('licence labels', () => {
  assert.equal(licenceLabel('PD-old-70'), 'Public domain');
  assert.equal(licenceLabel('CC0'), 'CC0 1.0');
  assert.equal(licenceLabel('CC-BY-4.0'), 'CC BY 4.0');
});

test('escapeHtml escapes markup and Liquid braces', () => {
  assert.equal(escapeHtml('<a href="x">{{ y }}</a>'), '&lt;a href=&quot;x&quot;&gt;&#123;&#123; y &#125;&#125;&lt;/a&gt;');
});

test('uem-henon geometric captions carry the content hash', () => {
  const name = 'uem-henon-pass-01-structure-2fc3613c22a1.svg';
  assert.deepEqual(parseHashedSvgName(name), {
    stem: 'uem-henon-pass-01-structure',
    name: 'structure',
    hash: '2fc3613c22a1',
  });
  assert.equal(parseHashedSvgName('uem-henon-pass-01-structure.svg'), null);
  assert.match(geometricCaptionHtml(name), /#2fc3613c22a1/);
  assert.match(diagramCaptionHtml('uem-diagram-fallback-2fc3613c22a1.svg'), /#2fc3613c22a1/);
});

test('layouts and Lab timer', () => {
  assert.equal(layoutFor({ slide_role: 'masterclass' }), 'image_argument');
  assert.equal(layoutFor({ slide_role: 'lab_exercise' }), 'exercise');
  assert.equal(layoutFor({ slide_role: 'lab_opener' }), 'split');
  assert.equal(timerFor({ slide_role: 'lab_exercise' }), 180);
  assert.equal(timerFor({ slide_role: 'masterclass' }), null);
});

test('notes and questions helpers', () => {
  assert.equal(notesHtml('Say this.\n- one\n- <two>'), '<p>Say this.</p><ul><li>one</li><li>&lt;two&gt;</li></ul>');
  assert.equal(questionsHtml(['A?', 'B?']), '<ol class="student-media-slide__questions"><li>A?</li><li>B?</li></ol>');
});

test('renderDeck emits sections with background, alt, caption, notes, timer', () => {
  const html = renderDeck(deck([
    { slide_id: 'cover', slide_role: 'unit_cover', background_kind: 'curated', media_slot_id: 'I.1.masterclass-1', heading: 'H', sentence: 'S', notes: 'Talk.' },
    { slide_id: 'analysis-opener', slide_role: 'analysis_opener', background_kind: 'geometrical', heading: 'A' },
    { slide_id: 'lab-1', slide_role: 'lab_exercise', background_kind: 'diagram', heading: 'L', portfolio_trace: 'Save it.', notes: 'Lab talk.' },
  ], [CC_ASSET]), CTX);
  assert.equal((html.match(/<section\b/g) || []).length, 3);
  assert.match(html, /class="sr-only">Image: A drawing of a chair\./);
  assert.match(html, /<aside class="notes"><p>Talk\.<\/p><\/aside>/);
  assert.match(html, /uem-henon-pass-01-structure-2fc3613c22a1\.svg/);
  assert.match(html, /fractal-triangles\/uem-diagram-fallback-2fc3613c22a1\.svg/);
  assert.match(html, /data-slide-id="lab-1"[^>]*data-timer="180"/);
});

test('withBase prefixes root-relative citation hrefs once', () => {
  assert.equal(withBase('/lessons/en/x/', '/digital-creativity-uem'), '/digital-creativity-uem/lessons/en/x/');
  assert.equal(withBase('/digital-creativity-uem/lessons/en/x/', '/digital-creativity-uem'), '/digital-creativity-uem/lessons/en/x/');
  assert.equal(withBase('https://example.org/a', '/digital-creativity-uem'), 'https://example.org/a');
});

test('every henon geometric SVG name carries its true SHA-256 prefix', () => {
  const files = readdirSync(geometricDir).filter((n) => /^uem-henon-pass-.*\.svg$/.test(n));
  assert.ok(files.length > 0);
  for (const name of files) {
    const parsed = parseHashedSvgName(name);
    assert.ok(parsed, `${name} has no hash`);
    const hash = createHash('sha256').update(readFileSync(join(geometricDir, name))).digest('hex').slice(0, parsed.hash.length);
    assert.equal(parsed.hash, hash, `${name}: content hash is ${hash}`);
  }
});

test('deck JS: no hard-coded base path, no timestamped fetch', () => {
  const js = readFileSync(join(root, 'docs/assets/js/student-media-deck.js'), 'utf8');
  assert.doesNotMatch(js, /\/digital-creativity-uem/);
  assert.doesNotMatch(js, /Date\.now\(\)/);
  assert.match(js, /dataset\.baseUrl/);
});

test('committed deck includes match the renderer', () => {
  execFileSync(process.execPath, [join(root, 'scripts/render-decks.mjs'), '--check'], { cwd: root, stdio: 'pipe' });
});

test('diagram fallback exists', () => {
  const meta = JSON.parse(readFileSync(join(root, 'docs/assets/images/fractal-triangles/current.json'), 'utf8'));
  assert.ok(existsSync(join(root, 'docs/assets/images/fractal-triangles', `${meta.asset}.svg`)));
});
