#!/usr/bin/env bash
# PHASE-EX2.exit-gate.sh — publication firewall
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

jekyll_build_ok
publication_safety_ok

absent "no Forge date lesson-scribe in CD I EN public source" 'Forge date:.*lesson-scribe' docs/lessons/en/digital-creativity-i
absent "no Fecha de forja in CD I ES public source" 'Fecha de forja' docs/lessons/es/creacion-digital-i
absent "no MCP/RAG vault footer in CD I ES public source" 'vía MCP|contexto RAG del vault' docs/lessons/es/creacion-digital-i

# Probe counts only ungated markdown (publication switch stripped)
check "probe Wave-1 infra vocab is 0" bash -c '
  n=$(node digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs | python3 -c "import sys,json; print(json.load(sys.stdin)[\"wave1\"][\"lesson_infra_vocab_files\"])")
  test "$n" -eq 0
'

# Built HTML must not contain Ahmes/Athanor (EN + ES Wave-1)
absent "no Ahmes in built CD I EN HTML" '\bAhmes\b' _site/lessons/en/digital-creativity-i
absent "no Ahmes in built CD I ES HTML" '\bAhmes\b' _site/lessons/es/creacion-digital-i
absent "no Athanor in built CD I EN HTML" '\bAthanor\b' _site/lessons/en/digital-creativity-i
absent "no Fecha de forja in built CD I ES HTML" 'Fecha de forja' _site/lessons/es/creacion-digital-i

# EX2 patterns present in safety script (FINDINGS E1)
for p in lesson-scribe 'Profield' UDIT web-atelier ahmes-library Thessia 'Fecha de forja'; do
  present "safety script has pattern: $p" "$p" scripts/verify-publication-safety.mjs
done

# Fixture: a known leak term must fail the safety script
FIXTURE="_site/__excellence_ex2_leak_fixture.html"
printf '<p>Ahmes vault leak fixture</p>\n' > "$FIXTURE"
if node scripts/verify-publication-safety.mjs >/tmp/dc-excellence-ex2-fixture.log 2>&1; then
  fail "fixture with Ahmes should fail safety"
else
  pass "fixture with Ahmes fails safety"
fi
rm -f "$FIXTURE"
publication_safety_ok

finish
