# Landing viewport + favicon touch

**Product claim:** Course landings (CT, DC, Web Atelier) fill the first viewport below the sticky header; touch on the screen disentangles the favicon facets the same way desktop pointer motion does.

**Engineering claim:** CT hub `min-block-size` was equal-specificity and later than `--landing`, shrinking the hero to ~14rem; fix with `:not(.hero-section--landing)` + explicit `block-size`. Mobile WebKit often skips window `pointermove` for touch — map `touchstart`/`touchmove` into the favicon camera (and geometry-live field).

| Artifact | Role |
| --- | --- |
| [`LANDING-VIEWPORT-TOUCH-ORCHESTRATOR.md`](LANDING-VIEWPORT-TOUCH-ORCHESTRATOR.md) | Programme · resume · gates |
| [`PHASE-L0.md`](PHASE-L0.md) | CT viewport − header + CSS cache bust |
| [`PHASE-L1.md`](PHASE-L1.md) | Favicon + geometry touch on CT/DC/atelier |

## Live snapshot (2026-11-15)

| Fact | Checked |
| --- | --- |
| CT hero computed `min-block-size` / height ≈ 224px | Browser CDP on `:4003` before fix (hub clamp won) |
| Actual header ≈ 84px vs `--site-header-height: 4.5rem` | CDP; sync from measured header on archive-hero boot |
| Favicon listeners were pointer-only on `window` | atelier/DC/CT `favicon-canvas.js` |

## Status

| Phase | Status |
| --- | --- |
| L0 · CT landing viewport | **DONE** (CSS + header sync + cache bust) |
| L1 · Touch facet displace | **DONE** (favicon ×3 + geometry-field ×2) |

## Amend 2026-11-15 evening
Mobile: `pointerout` with null relatedTarget was resetting the camera after every touch. Touch now uses capture listeners on `document`, ignores pointerout while `touchDriving`, immediate apply + depth floor, 900ms hold.
