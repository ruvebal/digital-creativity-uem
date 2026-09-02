#!/usr/bin/env bash
set -euo pipefail

STUDIO_USER_ROOT="${STUDIO_USER_ROOT:-/Users/ruvebal}"
FORMULA_BUNDLE="${FORMULA_BUNDLE:-${STUDIO_USER_ROOT}/ahmes-library/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611/extract/formula-audit}"

node scripts/fractal-architecture/generate-pass-track-backgrounds.mjs \
  "${FORMULA_BUNDLE}/formula-glossary.public.json" \
  docs/assets/images/fractal-pass-track \
  "${FORMULA_BUNDLE}/formula-glossary.private.json" \
  digital-creativity-pedagogy/grounding/fractal-architecture/formula-consumption-proof.private.json \
  digital-creativity-pedagogy/archives/fractal-pass-track \
  digital-creativity-pedagogy/fractal-architecture/originals/pass-track \
  uem
