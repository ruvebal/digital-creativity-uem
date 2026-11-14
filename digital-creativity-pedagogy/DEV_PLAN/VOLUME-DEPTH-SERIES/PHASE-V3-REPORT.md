# PHASE-V3-REPORT — Commons media-accept for ML-A

**Status:** DONE  
**Branch:** `forge/volume-depth-series-phase0`  
**Date:** 2026-11-14

## Gates

| Gate | Result |
| --- | --- |
| ≥4 human-accepted MP5 assets | **4** |
| ML-A deck binds accepted slots | **yes** — 4 bound after scoped rehydrate |
| No raw discovery URLs in student HTML | **yes** — `deck-media/*.webp` |
| Consumer pack | `docs/_data/media-packs/ml-vd-a-volume-depth.yml` (4 records) |
| `review-state.json` | `ml`/`ML-VD-A` for all four; `ml`/`ML-VD-B` for Dürer Commons IDs |

## Accepted assets (ML-A)

| Slot | asset_id | Run |
| --- | --- | --- |
| cover / volume-paint | `…Venetian School…jpg` | `I.5/20261113-foreshortening` |
| analysis / vanishing | `…Eye level and vanishing point…svg` | `I.5/20261113-perspective-vanishing` |
| masterclass-5 / depth-cues | `…Depth cues 1.png` | `I.5/20261113-texture-gradient` |
| masterclass-4 / cliff | `…NIH visual cliff experiment (cropped).png` | `I.6/20261114-visual-cliff` |

Accepted by: `ruvebal@crea-comm.net`.

## Dürer ML-B (orphan fix)

Replaced fake ids with real Commons files + `source_file_url`:

- `wikimedia:File:Dürer - Man Drawing a Lute.jpg`  
- `wikimedia:File:Duerer Underweysung der Messung 181.jpg`  

Scoped rehydrate: `DECK_ROOTS=docs/tracks/en/uem/2627-ml` → **2 bound**.

## Next

V4 verification + Qwen cold review.
