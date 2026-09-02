# I.1 forge receipt · cycle 1

**Date:** 2026-08-30  
**Unit:** I.1 · Introduction to Digital Images  
**Verdict:** cycle 2 applied reviewer patches — **FORGE_FROZEN** (ready for I.2)

## Cycle 2 fixes (reviewer TUNE_FORGER)

- Neutral `media-note` figcaptions (no Profield leak)
- ES switch-gates for learning_outcomes + S1/S2
- Shinkle public prose paraphrased; verified phrase only in quotes
- Session prompt: competencies aligned; B3 #3 matches lesson
- Full `extraction_db` path; `MEDIA_RIGHTS_LINE: PENDING` per slot

## Build

- [x] `npm run build` — publication + citation gates pass

| Artefact | Change |
| --- | --- |
| EN lesson | Field lens (Established/Emerging), 3 media placeholders, PROVENANCE_LINE block, removed FE II reference |
| ES lesson | Parity with EN |
| `lesson_covers.json` | `field_lens` / `field_lens_es` tied to MASTER-IDEAS |
| Session prompt | PROFIELD_ROUTING + condensed PROVENANCE_LINE |
| `PROVENANCE-LAW.mdc` | § Three layers (Profield vs PROVENANCE_LINE vs public) |
| `PROFIELD-UNIT-MAP.md` | Unit ↔ profield run table |
| `FORGE-UNIT-ITERATION.md` | 2–3 cycle workflow |

## Profield routing (layer 1)

| Signal | Source | Disposition |
| --- | --- | --- |
| `[ESTABLISHED]` field-of-practices | T1 + Shinkle | → VERIFIED public claim |
| `[ESTABLISHED]` bitmap/vector exercises | T1 line 17 | → I.2–I.4 adjacent; **not** cited in I.1 |
| `[ESTABLISHED]` Curcic studio drawing | `dc-2d-image-craft-pedagogy` | → **I.2 only** |
| `[ESTABLISHED]` Perthuis fashion photograph | T1 line 187 | → debate support; not VERIFIED in vault |
| `[EMERGING]` motion graphics | T1 line 222 | → forward to I.8/I.9 |
| Emerging transmedia | MASTER-IDEAS I.1 | → `[BIBLIO-GAP]` frontier signal in lesson |

## PROVENANCE_LINE summary (layer 2)

| claim-id | status | public_citation |
| --- | --- | --- |
| `I.1.claim.field-of-practices` | VERIFIED | `(Shinkle 2008, 15)` |
| `I.1.gap.tool-pedagogy` | NONE | OMITTED |
| `I.1.emerging.transmedia` | [BIBLIO-GAP] | OMITTED |

## Build

- [ ] `npm run build` (run after cycle 1 edits)

## Cycle 2 reviewer

- [ ] Cold subagent verdict: PASS | TUNE_FORGER | BLOCKED
