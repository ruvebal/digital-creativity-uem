#!/usr/bin/env bash
# PHASE-EX2.exit-gate.sh — runnable Gate for DC Excellence EX2
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

pass "EX2 gate scaffolding present"
# Phase-specific checks land as the implementer fills Acceptance.
# Until then: require the phase file and this script exist (EX0 will replace
# with real probe/build checks).
require_file "digital-creativity-pedagogy/excellence/PHASE-EX2.md"
jekyll_build_ok
publication_safety_ok

finish
