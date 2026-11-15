# PHASE-L1 — Mobile touch disentangles favicon

## Do

1. In atelier / DC / CT `favicon-motion/favicon-canvas.js`: map `touchstart`/`touchmove`/`touchend` through `clientPoint` into `move()`.  
2. In DC/CT `geometry-field.js`: same for `pointerRoot`.  
3. Bust favicon + archive-hero module queries.

## Gate

Device-mode touch drag on landing moves favicon facets (and CT geometry field).
