---
description: Whole-course cascade for Nuevos medios (RRSS · plataformas · moda) — skeleton → Thessia cold B1 → review → site index
globs: 'digital-creativity-pedagogy/forge/**,docs/lessons/**/nuevos-medios*/**,docs/tracks/**/nuevos-medios*/**'
alwaysApply: false
---

# NM CURRICULUM ORCHESTRATOR — Nuevos medios

**Status:** `RUNNING` — U1–U2 forged 2026-09-25; **U3 structure + Benetton** 2026-09-26 (`NM-COLD-REVIEW-U1-U3.md`); U3 Thessia/deck pending.  
**Authority:** PDF REF `4d3415b1` · `cv/guides/2-nuevos-medios-rrss.json` · CV
`uem-ruvebal-nuevos-medios-moda-cv.md` · unit plan `UNIT-PLAN-NUEVOS-MEDIOS.md`.  
**Prose:** `curriculum-forger` §5 STEP B prose → `lesson-scribe` → Ollama
`thessia-scholar-v3` via `thessia_generate.py` (never freehand cold B1).  
**Discovery:** `profield-nuevos-medios-moda-2026-27` · cite Ahmes only.  
**Campaigns:** `fashion-exemplary-social-campaigns/CANONICAL.md` → `20260925T200000Z`.  
**Harness:** `forge/nm_forge_u1_u2.py` · receipts `NM-THESSIA-U1-U2-REPORT.md` · `NM-COLD-REVIEW-U1-U3.md`.

**Primary Virtual Campus source layer:** `forge/NM-PDF-EXPORT-INGEST.execute.md` · `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/26-27/ONLINE/PDFs_export/` (23 teaching-content PDFs; separate from research bibliographies).

## Programme

| Phase | Gate | Output |
| --- | --- | --- |
| **N0** | CV + JSON + PDF reconciled; track indexed on `/tracks/{es,en}/` | done 2026-09-25 |
| **N1** | Lesson skeletons ES + EN; `lessons.yml`; track links | done (superseded by forge) |
| **N2** | Cold B1 + Reveal deck per unit; six-axis review; integrate | **U1–U3 decks done 2026-09-26**; U3 Thessia cold B1 optional; U4–U6 pending |
| **N3** | Publication gate; Thessia performance receipt | U1–U2 receipt |
| **N4** | Activity sheets 10 pt, exam bank, accepted Profield media on decks | deferred |

## Hard rules

- PDF CONTENIDOS beat Canvas titles; Canvas is delivery spine only.
- Teaching language ES; EN = S./E. twin.
- No FE/CD hour schemes forced; online 150 h / eval 50/10/20/20.
- Cold B1 → `lesson-scribe` only. Slideshow sentences never Thessia.
- Publication firewall: no Ahmes/Athanor/Thessia/Ollama names in student HTML.
- Stop and declare `[BIBLIO-GAP]` rather than fabricate cites.
- Keep Virtual Campus PDF exports in the dedicated teaching-content namespace; do not mix them into personal/research bibliography projects.

## Read before writing

1. `nm-cv-forge.mdc` · `nm-unit-forge.mdc` · `oficial-guia-framework.mdc` (NM row)
2. `~/src/.cursor/skills/curriculum-forger/SKILL.md` §5 STEP B prose
3. `~/src/.cursor/skills/lesson-scribe/SKILL.md`
4. Profield brief + `FORGE-SCHEDULE.md`
5. Existing CD lesson as shape reference (not content copy)

## Thessia call (pinned)

```bash
# Unload first — thessia_generate CI2 gate refuses if thessia-* already in `ollama ps`
ollama stop thessia-scholar-v3
PY=/Users/ruvebal/src/ahmes/.venv/bin/python   # ollama client (fine-tuning .venv may be absent)
$PY ~/src/deviac/fine-tuning/scripts/thessia_generate.py \
  --prompt "$(cat <record>/prompt.md)" \
  --out <record>/thessia-raw.md \
  --brief <record>/BRIEF.md \
  --model thessia-scholar-v3 \
  --num-predict 512 \
  --expected-sentences 4
```

Wave harness: `forge/nm_forge_u1_u2.py` (U1→amend→U2).  
Receipt: `forge/NM-THESSIA-U1-U2-REPORT.md`.

## Closing

Write `NM-CURRICULUM-ORCHESTRATOR.execution.receipt.md` with lesson paths,
`lessons.yml` slugs, Thessia pass/fail table, and remaining N4 backlog.
