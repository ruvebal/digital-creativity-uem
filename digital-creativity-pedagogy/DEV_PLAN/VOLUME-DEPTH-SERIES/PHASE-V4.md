# PHASE-V4 — Verification gates

**Depends on:** PHASE-V3 DONE (or PARTIAL with ≥4 accepts)  
**Out of scope:** new CONTENIDOS · media-prospect expansion beyond gate

## Do

1. `DECK_ROOTS=docs/tracks/en/uem/2627-ml npm run media:rehydrate -- --rights=flag`  
2. `npm run render:decks`  
3. `npm run validate:decks`  
4. `npm run verify:publication` · `npm run verify:citations`  
5. Spot-check: I.6 EN lesson has no `pv-p*` / Panofsky wall; ML-B has kit diagrams.  
6. Cold review via Ollama Qwen → `PHASE-V4-COLD-REVIEW.md` (and cascade-wide notes if needed).  
7. `PHASE-V4-REPORT.md`.

## Gate

- All commands exit 0  
- I.6 figure count ≤ 9; no perspective-kit in I.6 body  
- ML-A ≥ 4 accepted bound images; ML-B Dürer has `source_file_url`  
- Report status ∈ {DONE, PARTIAL, BLOCKED}
