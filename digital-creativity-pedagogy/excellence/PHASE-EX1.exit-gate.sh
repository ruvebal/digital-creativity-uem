#!/usr/bin/env bash
# PHASE-EX1.exit-gate.sh — contract hotfix
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

jekyll_build_ok
publication_safety_ok

present "evaluation shows 55" '\*\*55%\*\*|Knowledge tests.*55' docs/evaluation/index.md
present "evaluation shows 15" '\*\*15%\*\*' docs/evaluation/index.md
present "evaluation shows 20" '\*\*20%\*\*' docs/evaluation/index.md
present "evaluation shows 10" '\*\*10%\*\*' docs/evaluation/index.md
present "evaluation ACT3 / Transposition lock" 'ACT3|Transposición cartel|cartel.*another language' docs/evaluation/index.md
present "DCI how-to-pass 55" '55%' docs/tracks/en/uem/2627-dci/how-to-pass-this-track/data/content.json
present "DCI how-to-pass ACT3/cartel" 'ACT3|cartel from another language' docs/tracks/en/uem/2627-dci/how-to-pass-this-track/data/content.json
present "DCII how-to-pass 55" '55%' docs/tracks/en/uem/2627-dcii/how-to-pass-this-track/data/content.json
present "Workshop from session 4" 'from session 4' docs/evaluation/index.md

# Probe should now see 55 on evaluation page
check "probe notes evaluation 55" bash -c 'node digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs | grep -q "evaluation_page_mentions_55\": true"'

finish
