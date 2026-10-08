#!/usr/bin/env bash
# PHASE-EX0.exit-gate.sh — DC Excellence EX0
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"
REL="digital-creativity-pedagogy/excellence"

require_file "$REL/PHASE-EX0.md"
require_file "$REL/FINDINGS-2026-10-07.md"
require_file "$REL/COORDINATION-SANDRA.md"
require_file "$REL/DECISION-EX0-GUIA.md"
require_file "$REL/probe/excellence-probe.mjs"
require_file "$REL/evidence/baseline-EX0.json"
require_file "$REL/evidence/head-EX0.json"
require_file "digital-creativity-pedagogy/cv/sources/Plan_de_trabajo_2026-27_Creacion_Digital_I-Sandra_Jimenez.pdf"
require_file "$REL/local/athanor.sh"
require_file "$REL/local/thessia.sh"
require_file "$REL/local/ollama-generate.sh"

present "DECISION locks 55" 'weights_tests: *55' "$REL/DECISION-EX0-GUIA.md"
present "DECISION locks ACT3/D2" 'd2_equals_act3: *true' "$REL/DECISION-EX0-GUIA.md"
present "DECISION cites guía JSON" '1-creacion-digital-i\.json' "$REL/DECISION-EX0-GUIA.md"
present "DECISION cites Sandra PDF" 'Plan_de_trabajo_2026-27' "$REL/DECISION-EX0-GUIA.md"

check "probe self-check" node "$REL/probe/excellence-probe.mjs" --self-check
check "probe --targets (EX0 soft)" node "$REL/probe/excellence-probe.mjs" --targets

# Evidence JSONs must mention Wave-1 lesson count
present "baseline has lessons_en_cd_i" '"lessons_en_cd_i"' "$REL/evidence/baseline-EX0.json"
present "head has commit" '"commit"' "$REL/evidence/head-EX0.json"

finish
