# PHASE-EX4 Report — Slide-bound image curation (Wave-1)

| Field | Value |
| --- | --- |
| **status** | VERIFYING |
| **started_at** | 2026-10-07 |
| **finished_at** | 2026-10-07 (implementation done; awaiting harness verify + cold review) |
| **branch / worktree** | `cascade/excellence-4` · `digital-creativity-uem-integration-excellence-4` (`.cascade-lane` = `excellence`) |
| **mode** | AUTOPILOT (§0 deck images; §2 EX4 row) |
| **exit gate (local)** | `PHASE-EX4.exit-gate.sh` → **failures: 0** (logged in `PHASE-EX4-VERIFY-LOG.md`) |

## Outcome

| Deck | Core curated | Core total | Bind % | Notes |
| --- | --- | --- | --- | --- |
| I.1 fashion-image | 10 | 10 | 100% | |
| I.2 2d-drawing | 11 | 11 | 100% | |
| I.3 color-bitmaps | 10 | 10 | 100% | |
| I.4 effects | 8 | 8 | 100% | |
| I.5 three-dimensional-form | 7 | 7 | 100% | |
| ML-FIA fashion-image-analysis | 9 | 10 | 90% | `lab-2` explicit diagram fallback |
| **Wave-1 total** | **55** | **56** | **98%** | ≥60% gate met |

- Registry: **40** assets in `curation/autopilot-assets.json` (`raw_title` on all)
- Rights: **31** curator `flagged`, **9** `ok` (no silent `ok` on EU-term doubt)
- Vision: `evidence/EX4/vision_raw.json` + `vision.json` via local **qwen3.8:27b (think:false)** only
- `profield-cache`: **79** files retained (orphans warn only; not deleted)
- `deck-media`: **41** WebP renditions (≤ 600 KB; no raw SVG)

## What changed (files)

| Path | Change |
| --- | --- |
| `scripts/rehydrate-student-media.mjs` | EX3 F2: `bindSlides` only; no `rankCursor`; profield-cache never deleted |
| `scripts/lib/rendition.mjs` | Added (WebP ≤1920 / ≤600 KB; SVG rasterise) |
| `package.json` | `sharp` devDependency; `media:rehydrate --rights=flag` |
| Wave-1 `docs/tracks/.../content.json` (6 decks) | `schema_version: 2`, `slide_id`, `image_brief`, `asset_id` bindings |
| `docs/assets/images/deck-media/` | 41 renditions |
| `excellence/curation/*-SHORTLIST.md`, `autopilot-assets.json`, `rights-report.json`, `CURATION-SIGNOFF.md` | Autopilot curation packet |
| `excellence/evidence/EX4/` | plan, curate script, vision logs, bindings |
| `PHASE-EX4.exit-gate.sh` | Real acceptance checks |

## FINDINGS closed (cite)

- **B2** — rights / orphan / reuse discipline live on Wave-1 v2 decks; orphans in `profield-cache` warn, not delete
- **B3** — slide-bound curation + rights report pattern ported (CT Excellence EX4 discipline)
- **EX3 cold-review F2** — rehydrate no longer rank-deals; Wave-1 on `schema_version: 2`

## Uncertain / resume

- Cold review must spot-check ≥5 bindings for brief fit
- Commons HTTP 429 during rehydrate; several assets recovered from local `profield-cache` (TIFF Shanghai rasterised via sharp)
- `image-morphology` left legacy (not Wave-1 per SCHEMA / INDEX)
- Do **not** mark DONE; do not land; harness verify + cold reviewer next

## Resume point

`cascade-harness.sh verify` → cold reviewer → `PHASE-EX4-COLD-REVIEW.md` → only then DONE / land.

## Cold-review fix (P0 F1) — 2026-10-07

I.3 `analysis-model` had Kawakubo Stierch 01 bound while `evidence/EX4/vision.json` recorded fit **2** (bindings/shortlist falsely claimed 4). Unbound; rebound to `wikimedia:File:Grafik nach Josef Albers1.jpg` after local vision (**fit 5**, CC0). Kawakubo fit-2 left in vision log as evidence. Exit gate re-run after fix.

