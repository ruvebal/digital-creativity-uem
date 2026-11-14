# PHASE-V2 — Register ML-A/B/C student surfaces

**Depends on:** PHASE-V1 DONE  
**Out of scope:** media-accept Commons pack (V3) · full publication gates (V4) · new CONTENIDOS

## Do

1. Author EN master-lecture pages + decks for:
   - **ML-A** Seeing volume (perception) — ≤6 main ideas; geometrical / existing course diagrams until V3 media
   - **ML-B** Constructing space — mount perspective-kit P1–P5 as full graphic slides; Panofsky SAFE cites; bridge to I.6
   - **ML-C** Digital & AI depth — projection honesty · 2.5D vs true 3D · bridge to I.6 behaviour
2. Register in `docs/_data/lessons.yml` + `tracks.yml` `master_lectures` + master-lectures index.
3. Tracks under `docs/tracks/en/uem/2627-ml/volume-depth-{perception,construction,digital}/`.
4. Update `forge/volume-depth/ML-B-construction-DRAFT.md` → registered.
5. `PHASE-V2-REPORT.md` + `npm run render:decks` for the three new decks.

## Gate

- Each deck has ≤6 `slide_role: masterclass` cards  
- ML-B binds at least P1 + P5 kit SVGs (no raw discovery URLs)  
- Lessons registered (`type: master-lecture`)  
- Report status ∈ {DONE, PARTIAL, BLOCKED}
