# PHASE-V3-REPORT — Commons media-accept for ML-A

**Status:** PARTIAL  
**Branch:** `forge/volume-depth-series-phase0`  
**Date:** 2026-11-14

## Gates

| Gate | Result |
| --- | --- |
| ≥4 human-accepted MP5 assets | **PARTIAL — 3** classroom stills accepted (gate asked 4; Wikipedia cliff/Alberti not in 20261113 manifests) |
| ML-A deck binds accepted slots | **yes** — cover · analysis · masterclass-5 bound; rehydrate cached 3× `.webp` |
| No raw discovery URLs in student HTML | **yes** — deck uses `/assets/images/deck-media/*.webp` after rehydrate |
| Consumer pack | `docs/_data/media-packs/ml-vd-a-volume-depth.yml` |
| `review-state.json` assignments | `ml` / `ML-VD-A` for the three asset_ids (profield run tree) |

## Accepted assets

| Slot | asset_id | Run |
| --- | --- | --- |
| `ML-VD-A.cue.depth-cues` | `wikimedia:File:Depth cues 1.png` | `I.5/20261113-texture-gradient` |
| `ML-VD-A.cue.vanishing` | `wikimedia:File:Eye level and vanishing point diagram japanese.svg` | `I.5/20261113-perspective-vanishing` |
| `ML-VD-A.cue.volume-paint` | `wikimedia:File:The Venetian School of Painting (1912) (14597540617).jpg` | `I.5/20261113-foreshortening` |

Accepted by: `ruvebal@crea-comm.net` via `.venv/bin/profield media-accept` + `review-state.json` assignment (rehydrate reads review-state, not run manifests alone).

## Remaining for DONE

1. Fresh `media-prospect` (or manual Commons pull) for visual-cliff + Alberti self-portrait Wikipedia leads → accept #4–5.  
2. Optional: register Dürer ML-B stills with downloadable `source_file_url` so `media:rehydrate` does not orphan `3fcc495e…` / `c9f5e339…` (kit SVGs already carry ML-B).  
3. Do **not** run unscoped `npm run media:rehydrate` without `DECK_ROOTS` awareness — it strips unaccepted curated binds.

## Amend-on-surprise

`profield media-accept --consumer-pack` overwrites the pack per run; merged pack hand-assembled. Rehydrate requires `review-state.json` assignments keyed `project_id/unit_id` matching `media_selection` (`ml` / `ML-VD-A`).

## Next

V4 verification gates, or finish V3 fourth accept then V4.
