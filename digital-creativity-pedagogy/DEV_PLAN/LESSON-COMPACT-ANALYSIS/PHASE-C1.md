# PHASE-C1 — Strip Analysis-opener prose (Digital Creativity)

**Depends on:** C0 DONE  
**Out of scope:** CT (C2) · new illustrations

## Do

1. In `docs/lessons/**` remove “Analysis opens the class” / session-block Analysis ritual paragraphs; keep compact method axes and all `<figure>` / cover assets.  
2. In `docs/_includes/decks/**` and `docs/tracks/**/data/content.json` remove “Now the analysis” / matching ritual copy from `analysis_opener` / early slides; keep geometrical backgrounds and slide structure.  
3. Re-render decks if the course pipeline requires it (`render:decks` / site build).  
4. `PHASE-C1-REPORT.md` with before/after `rg` counts.

## Gate

- `rg -i 'Analysis opens the class|Now the analysis|Session block 1 · Analysis'` under DC `docs/` → **0** (or only intentional archive notes outside student surfaces)  
- Figure / cover / SVG paths untouched  
- Report status ∈ {DONE, PARTIAL, BLOCKED}
