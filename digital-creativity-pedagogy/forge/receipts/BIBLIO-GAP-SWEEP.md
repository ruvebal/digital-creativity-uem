# Biblio-gap sweep · Ahmes machinery run

**Date:** 2026-08-30  
**Tooling:** `ahmes enrich --meta --online`, `ahmes status`, `ahmes query --cite --require-evaluator-safe`  
**Script:** `forge/scripts/biblio-gap-sweep.sh` (reusable)

## Upgraded this session

| Unit | claim | Before | After | node |
| --- | --- | --- | --- | --- |
| **II.1** | Altered images → body satisfaction | `[BIBLIO-GAP]` / Ozimek matrix leak | **VERIFIED** | `cb1441df-9ff9-5563-b894-fff99b8d5fad`, coat `984f4f11` |

MacCallum & Widdows (2018) was already in `~/ahmes-library/scholar/`; `enrich --meta --online` confirmed `evaluator_safe=yes`. Lesson PROVENANCE_LINE updated in II.1 EN+ES.

## Target gap DOIs — no vault yet (procurement)

These remain `[BIBLIO-GAP]` in lessons until PDF ingest + cite resolver pass:

| DOI | Authors / use | Units | PENDING-procurement |
| --- | --- | --- | --- |
| `10.1080/17543266.2017.1299226` | Reddy-Best textbooks | I.1, I.2, I.7 | — |
| `10.1080/1362704X.2016.1173349` | Rocamora mediatization | I.1 | — |
| `10.1080/1362704X.2024.2389595` | Crepax affective trends | I.4 | — |
| `10.46328/ijtes.576` | Curcic studio drawing | I.2, I.4 | `no_oa` |
| `10.1177/0098858819849990` | McBride retouch ethics | I.4 | — |
| `10.1002/eat.22449` | McLean selfie editing | II.1 | `no_oa` |
| `10.3389/ejcmp.2025.14563` | Rodriguez Schon decolonial archives | II.1 | — |

**Workflow when PDF arrives:** `ahmes ingest <pdf> -o ~/ahmes-library --project scholar --save-db --treeshake --enrich-ner --enrich-semantic` → `ahmes enrich --meta --online <db>` → `ahmes query --cite <db>:<node> --require-evaluator-safe` → update lesson `PROVENANCE_LINE` from `[BIBLIO-GAP]` to `VERIFIED`.

RIS seeds: `~/src/profield/runs/dc-fashion-retouch-pedagogy/20260816/bibliography.ris` (McLean + skin-reflectance refs).

## Already VERIFIED in vault (no lesson upgrade needed this pass)

| coat | use |
| --- | --- |
| `1936070c` | Shinkle — I.1 |
| `31a9a359` | Campinho — I.7 |
| `6d1a7b81` | Coats — I.6 |
| `20e79483` | Papahristou — I.5 |
| `984f4f11` | MacCallum — II.1 |

## Full-library meta refresh

`biblio-gap-sweep.sh` runs `enrich --meta --online` over all `~/ahmes-library/scholar/documents/*/extract/extraction.db` — idempotent cache hits after first pass. Raw log: `forge/receipts/BIBLIO-GAP-SWEEP.log`.

## Lesson policy unchanged

`[BIBLIO-GAP]` does **not** remove public Chicago citations or References — it marks vault verification pending (`PROVENANCE-LAW.mdc`).
