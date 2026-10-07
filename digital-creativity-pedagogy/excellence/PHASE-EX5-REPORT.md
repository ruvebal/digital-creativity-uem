# PHASE-EX5 Report — Deck renderer (pre-render, alt, captions, notes, layouts)

**Status:** VERIFYING  
**Branch:** `cascade/excellence-5`  
**Worktree:** `digital-creativity-uem-integration-excellence-5`  
**Date:** 2026-10-07

## Goal

Student decks render captions/alt/notes/timers offline; browser layout check green on Wave-1.

## What changed (files)

| Area | Paths |
| --- | --- |
| Renderer | `scripts/lib/deck-render.mjs` (new), `scripts/render-decks.mjs` (new), `scripts/lib/deck-caption.mjs` (re-export) |
| Tests | `scripts/tests/deck-render.test.mjs`, `scripts/tests/browser/deck-layout.mjs` |
| Runtime | `docs/assets/js/student-media-deck.js` (enhancement-only for pre-rendered; legacy path for non-v2) |
| CSS / forge | `docs/assets/css/pass-track-deck.css` (golden-rule clamps + EX5 layouts/timer/sr-only), `digital-creativity-pedagogy/forge/STUDENT-SLIDESHOW-FORGE.mdc` (golden rule 1 text for browser floors) |
| Diagram fallback | `docs/assets/images/fractal-triangles/current.json` + `uem-diagram-fallback-2fc3613c22a1.svg` |
| Wave-1 pages | `docs/tracks/en/uem/2627-dci/i-{1..5}-*/index.html`, `docs/tracks/en/uem/2627-ml/fashion-image-analysis/index.html` (`{% include decks/<slug>.html %}`, `data-base-url`) |
| Includes / figures | `docs/_includes/decks/*.html` (6), `docs/_data/lesson_figures.json` |
| Notes | Wave-1 `content.json` — notes on cover/opener/masterclass/lab/outro slides |
| Gate / package | `PHASE-EX5.exit-gate.sh`, `package.json` (`render:decks`, `test:browser`, prebuild/predevelop wiring) |
| Cascade | `DECISIONS-LOG.md`, `INDEX.md` / `PHASE-EX5.md` → VERIFYING |

## FINDINGS cited

| ID | Disposition |
| --- | --- |
| **B4** | Closed for Wave-1: browser layout + print type floors in EX5 gate (`deck-layout.mjs`, 375 views / 0 failures) |
| **B5** | Partial: geometrical openers use hashed henon SVGs with hash in caption; Lab/Workshop opener law verified by layout presence (full Lab redesign remains EX8) |
| **B1** | Unchanged (deck↔lesson 1:1) — deferred EX11 |

## Commands run (real)

```text
node scripts/render-decks.mjs                          # 6 decks rendered
node --test scripts/tests/deck-render.test.mjs         # 12/12 pass
node scripts/validate-decks.mjs --strict --rights=flag # 0 errors
bash digital-creativity-pedagogy/excellence/PHASE-EX5.exit-gate.sh
  → failures: 0
  → browser layout check: deck-layout: 375 slide view(s), 0 failure(s)
```

## Uncertain / residual

- Legacy decks (`how-to-pass-this-track`, `image-morphology`) keep the runtime path until migrated.
- CD II / NM firewall-only — not in browser hard-fail set (A1).
- Floating `.student-media-caption` CSS remains for legacy pages; Wave-1 uses in-section `.slide-caption`.
- Professor final review of autopilot image picks and notes still pending (AUTOPILOT).

## Resume point

Hand to harness `cascade-harness.sh verify` → cold reviewer → `PHASE-EX5-COLD-REVIEW.md`. Do **not** open EX6 until EX5 is DONE.
