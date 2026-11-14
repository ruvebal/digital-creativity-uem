# PHASE-V3 — Commons media-accept for ML-A

**Depends on:** PHASE-V2 DONE  
**Out of scope:** inventing rights clearance · raw discovery URLs in student HTML · cloud LLM

## Do

1. Human `media-review` of Profield 20261113 leads + Wikipedia Commons candidates from the research spine.  
2. Explicit `profield media-accept` for 4–6 ML-A cue plates (occlusion / size / perspective / texture / aerial / visual cliff).  
3. Drop accepted MP5 pack into `docs/_data/media-packs/` (or site convention) and bind `media_slot_id` on ML-A deck.  
4. Re-render ML-A deck; confirm student HTML has **no** raw discovery URLs.  
5. `PHASE-V3-REPORT.md`.

## Candidate shortlist (from research spine — not accepted)

| Cue | Commons File (P2 OK 2026-11-13) | Slot intent |
| --- | --- | --- |
| Visual cliff | `NIH_visual_cliff_experiment_(cropped).png` | ML-A.cue.cliff |
| Alberti (optional ML-B) | `Leon_Battista_Alberti,_Self-Portrait,_c._1435,_NGA_43845.jpg` | ML-B already has Dürer |
| Volume in painting | `Madonna_del_parto_piero_della_Francesca.jpg` | ML-A.cue.volume-paint |
| Aerial treatise PDF | `A_treatise_on_painting_(IA_davincionpainting00leon).pdf` | crop/still only after accept |

Profield run dirs: `~/src/profield/runs/media-prospector/20261113-*` (perspective, aerial, alberti, texture, foreshortening, visual-cliff=0, occlusion=0).

## Gate

- ≥4 accepted assets with `accepted_by` human  
- ML-A deck binds accepted slots only  
- Report status ∈ {DONE, PARTIAL, BLOCKED}
