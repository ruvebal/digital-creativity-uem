# Formula readiness preflight

- status: DONE
- run_id: 20260830T-overnight-ingest-15
- mode: execute
- operator_approval: yes
- checked_at_utc: 2026-08-30T10:00:44Z
- ahmes_dev_plan: `/Users/ruvebal/src/ahmes/docs/DEV_PLAN`
- formula_audit_bundle: `/Users/ruvebal/ahmes-library/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611/extract/formula-audit`

## Required 12H reports and exports

| Artifact | Required path | State |
| --- | --- | --- |
| `PHASE-12H.F0-REPORT.md` | `/Users/ruvebal/src/ahmes/docs/DEV_PLAN/PHASE-12H.F0-REPORT.md` | present |
| `PHASE-12H.F1-REPORT.md` | `/Users/ruvebal/src/ahmes/docs/DEV_PLAN/PHASE-12H.F1-REPORT.md` | present |
| `PHASE-12H.F2-REPORT.md` | `/Users/ruvebal/src/ahmes/docs/DEV_PLAN/PHASE-12H.F2-REPORT.md` | present |
| `formula-glossary.private.json` | `/Users/ruvebal/ahmes-library/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611/extract/formula-audit/formula-glossary.private.json` | present |
| `formula-glossary.public.json` | `/Users/ruvebal/ahmes-library/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611/extract/formula-audit/formula-glossary.public.json` | present |

## Exportable math check

| Export | State |
| --- | --- |
| private glossary | exportable-math-present |
| public glossary | public-exportable-math-present |

## Policy

F0, F1, and F2 must exist before the broad design bibliography run is described as formula-ready. Formulae are exportable only from the glossary JSON files above. Athanor injection remains discovery-only and requires explicit `--inject`.
