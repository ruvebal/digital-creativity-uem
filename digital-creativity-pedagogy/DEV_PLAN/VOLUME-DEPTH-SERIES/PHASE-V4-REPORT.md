# PHASE-V4-REPORT — Verification gates

**Status:** PARTIAL  
**Branch:** `forge/volume-depth-series-phase0`  
**Date:** 2026-11-14  
**Cold review:** [`PHASE-V4-COLD-REVIEW.md`](PHASE-V4-COLD-REVIEW.md) — VERDICT `PASS-WITH-AMENDMENTS` (F7 amended)

## Gates

| Gate | Result |
| --- | --- |
| `DECK_ROOTS=docs/tracks/en/uem/2627-ml npm run media:rehydrate -- --rights=flag` | **ok** — 8 deck files, changed 0, orphans removed 0 |
| `npm run render:decks` | **ok** — 17 decks, 0 written (already current) |
| `npm run validate:decks` | **PARTIAL** — cascade decks (i-5 / i-6 / volume-depth-*) **0 ERROR**; full tree 19 ERROR (all I.7 rights/rendition — out of scope) |
| `npm run verify:publication` | **PARTIAL** — exit 1; **0 findings** on Volume–Depth / I.5 / I.6; 12 findings on I.7 / neoplastic / platonic-favicon |
| `npm run verify:citations` | **PARTIAL** — exit 1; **0 findings** on cascade surface; 2 findings on I.7 EN/ES |
| Spot-check I.6 | EN figures **8** (≤9); **no** `pv-p*` / `perspective-kit` in lesson body |
| Spot-check ML-B | perspective-kit `diagram_src` present; Dürer lute + Messung 181 have `source_file_url` |
| ML-A binds | **4** accepted Commons (Venetian, vanishing, cliff, depth-cues) |
| `review-state.json` | live six ids: `project_id=ml` + `unit_id=ML-VD-A\|B`; fake Dürer filenames **rejected** + assignments cleared (F7) |

## Cascade surface verdict

Volume–Depth programme gates hold. Whole-repo `verify:*` / `validate:decks` remain red on pre-existing I.7 / neoplastic / platonic dirt — not introduced by this cascade and not fixed here.

## Remaining (keeps PARTIAL)

1. Whole-repo publication/citation/validate exit 0 blocked by I.7 + neoplastic SOURCE.txt + platonic-favicon (separate work).  
2. Optional: Alberti / further Commons for ML-B beyond the two Dürer stills.  
3. ML-C (`volume-depth-digital`) still enrichment-only — no Commons bind required by V4.

## Next

Cascade programme closed at PARTIAL. Resume only if a follow-on phase is opened for I.7 dirt or further ML media.
