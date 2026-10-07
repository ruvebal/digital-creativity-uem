# PHASE-EX3 report — Media pipeline rules + deck validator

**Status:** ready to land (gate exit 0 · cold review PASS)

## Delivered
- `scripts/validate-decks.mjs` + `scripts/lib/media-rules.mjs` (`--strict --rights=flag`)
- 33 tests: block/flag/orphan/reuse + CLI modes
- Forge pointers in STUDENT-SLIDESHOW-FORGE / dc-unit-forge
- SCHEMA-VERSION-WAVE1 note; rights-report path; Wave-1 legacy warn-only until EX4

## FINDINGS
- B2 / B3 addressed at tooling layer

## Residual (EX4)
- bindSlides / schema_version 2 migration; rehydrate off rankCursor
