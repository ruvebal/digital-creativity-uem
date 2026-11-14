# PHASE-V4-REPORT — Verification gates

**Status:** DONE  
**Branch:** `forge/volume-depth-series-phase0`  
**Date:** 2026-11-14  
**Cold review:** [`PHASE-V4-COLD-REVIEW.md`](PHASE-V4-COLD-REVIEW.md) — VERDICT `PASS-WITH-AMENDMENTS` (F7 amended)

## Gates

| Gate | Result |
| --- | --- |
| `npm run media:rehydrate -- --rights=flag` (full / unscoped) | **ok** — ML-B **3** bound (Dürer lute + Messung + Alberti); orphans removed **0** |
| `npm run render:decks` | **ok** |
| `npm run validate:decks` | **PARTIAL** — cascade decks (i-5 / i-6 / volume-depth-*) clean of ERROR; I.7 fashion-references deck still has pre-existing slot/retrieval/rendition ERRORs (not Volume–Depth) |
| `npm run verify:publication` | **ok** — exit 0 (I.7 addendum AI footer scrubbed; neoplastic SOURCE.txt + platonic Ahmes leak fixed) |
| `npm run verify:citations` | **ok** — exit 0 (I.7 addendum EN/ES citation links) |
| Spot-check I.6 | EN figures **8** (≤9); **no** `pv-p*` / `perspective-kit` in lesson body |
| Spot-check ML-B | perspective-kit `diagram_src` present; Dürer + Alberti have `source_file_url` |
| ML-A binds | **4** accepted Commons |
| ML-B Alberti | `wikimedia:File:Della Pittura Alberti perspective vanishing point.jpg` · `ml`/`ML-VD-B` |
| Orphan root-fix | rehydrate prefers committed https `source_file_url`; review-state assignments required — **DECK_ROOTS scoping no longer required** |

## Cascade surface verdict

Volume–Depth programme + publication/citation gates hold. I.7 *deck* validate ERRORs remain a separate deck-hygiene task (not publication dirt).

## Remaining (non-blocking for V4 DONE)

1. `validate:decks` I.7 fashion-references slot/retrieval/missing webp hygiene.  
2. ML-C enrichment media (optional).
