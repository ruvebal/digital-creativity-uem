#!/usr/bin/env bash
# PHASE-EX0.exit-gate.sh — runnable Gate for DC Excellence EX0
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

pass "EX0 gate scaffolding present"
# Phase-specific checks land as the implementer fills Acceptance.
# Until then: require the phase file and this script exist (EX0 will replace
# with real probe/build checks).
require_file "digital-creativity-pedagogy/excellence/PHASE-EX0.md"

require_file "digital-creativity-pedagogy/excellence/FINDINGS-2026-10-07.md"
require_file "digital-creativity-pedagogy/excellence/COORDINATION-SANDRA.md"
# After implementer: probe + decision (gate will be strengthened in-phase)
if [[ -f digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs ]]; then
  node digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs --self-check || fail "probe self-check"
  pass "probe self-check"
fi
if [[ -f digital-creativity-pedagogy/excellence/DECISION-EX0-GUIA.md ]]; then
  grep -q '55' digital-creativity-pedagogy/excellence/DECISION-EX0-GUIA.md || fail "weights missing in DECISION"
  grep -qi 'ACT3\|Transposic' digital-creativity-pedagogy/excellence/DECISION-EX0-GUIA.md || fail "Sandra lock missing"
  pass "DECISION-EX0 present"
fi

finish
