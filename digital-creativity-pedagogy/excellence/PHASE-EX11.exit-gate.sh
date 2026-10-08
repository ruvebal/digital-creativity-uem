#!/usr/bin/env bash
# PHASE-EX11.exit-gate.sh — Closing audit + hardened probe + handoff seed
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

require_file "digital-creativity-pedagogy/excellence/PHASE-EX11.md"
require_file "digital-creativity-pedagogy/excellence/CLOSING-AUDIT.md"
require_file "digital-creativity-pedagogy/excellence/NEXT-CASCADE-CD-II.md"
require_file "digital-creativity-pedagogy/excellence/evidence/final-EX11.json"
require_file "digital-creativity-pedagogy/excellence/FINAL-REVIEW.md"

# Probe --targets must exit 0 (EX11 hardened Wave-1 targets)
if node digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs --targets >/tmp/ex11-probe-targets.json 2>&1; then
  pass "probe --targets"
else
  fail "probe --targets"
  cat /tmp/ex11-probe-targets.json >&2 || true
fi

# final-EX11.json must be current enough to include hardened keys
python3 - <<'PY' && pass "final-EX11 has Wave-1 media keys" || fail "final-EX11 has Wave-1 media keys"
import json
from pathlib import Path
d = json.loads(Path("digital-creativity-pedagogy/excellence/evidence/final-EX11.json").read_text())
w = d.get("wave1") or {}
need = ["wave1_media_deck_count", "wave1_media_ne_2_labs", "catalogue_present", "question_bank_present"]
missing = [k for k in need if k not in w]
assert not missing, missing
assert w.get("wave1_media_deck_count", 0) >= 6
assert w.get("wave1_media_ne_2_labs") == []
PY

python3 - "$CASCADE" <<'PY' && pass "closing audit covers every finding once" || fail "closing audit covers every finding once"
import pathlib, re, sys
c = pathlib.Path(sys.argv[1])
ids = sorted(set(re.findall(r"^\| ([A-E]\d+) \|", (c / "FINDINGS-2026-10-07.md").read_text(), re.M)))
audit = (c / "CLOSING-AUDIT.md").read_text()
bad = [i for i in ids if len(re.findall(rf"^\| {i} \|", audit, re.M)) != 1]
print("findings", len(ids), "missing or duplicated:", bad)
sys.exit(1 if bad else 0)
PY

present "NEXT-CASCADE names CD II" "Creación Digital II|CD II" \
  digital-creativity-pedagogy/excellence/NEXT-CASCADE-CD-II.md
present "NEXT-CASCADE names Nuevos Medios" "Nuevos Medios" \
  digital-creativity-pedagogy/excellence/NEXT-CASCADE-CD-II.md
present "FINAL-REVIEW §4 closing audit" "CLOSING-AUDIT" \
  digital-creativity-pedagogy/excellence/FINAL-REVIEW.md
present "FINAL-REVIEW §5 preview" "release-notes|How to preview" \
  digital-creativity-pedagogy/excellence/FINAL-REVIEW.md
present "FINAL-REVIEW §6 release" "Release or roll back|gitflow.sh release-notes" \
  digital-creativity-pedagogy/excellence/FINAL-REVIEW.md

present "forge mentions image_brief" "image_brief" \
  digital-creativity-pedagogy/forge/STUDENT-SLIDESHOW-FORGE.mdc
present "unit forge mentions references.yml" "references\.yml" \
  digital-creativity-pedagogy/dc-unit-forge.mdc
present "unit forge points to excellence" "excellence/" \
  digital-creativity-pedagogy/dc-unit-forge.mdc
present "AGENTS.md points to the cascade" "excellence/" AGENTS.md
present "AGENTS.md points to NEXT-CASCADE or EX11 handoff" "NEXT-CASCADE-CD-II|EX0–EX11|Excellence cascade" AGENTS.md

jekyll_build_ok
publication_safety_ok

# Validator still green on Wave-1
if node scripts/validate-decks.mjs --strict --rights=flag >/tmp/ex11-validate.log 2>&1; then
  pass "validate-decks --strict"
else
  fail "validate-decks --strict"
  tail -40 /tmp/ex11-validate.log >&2 || true
fi

finish
