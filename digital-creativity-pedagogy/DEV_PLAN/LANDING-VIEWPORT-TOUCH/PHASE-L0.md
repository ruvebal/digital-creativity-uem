# PHASE-L0 — CT landing viewport − header

## Do

1. `.hero-section--hub:not(.hero-section--landing)` for hub clamp.  
2. `.hero-section--landing` gets explicit `block-size` + `min-block-size` = `100dvh − var(--site-header-height)`.  
3. Measure sticky header into `--site-header-height` on archive-hero boot.  
4. Bust `site.css` query.

## Gate

Hero height ≈ viewport − header on `:4003`.
