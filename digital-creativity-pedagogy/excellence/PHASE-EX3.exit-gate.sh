#!/usr/bin/env bash
# PHASE-EX3.exit-gate.sh — media pipeline rules, tests, deck validator (no Jekyll)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

require_file "digital-creativity-pedagogy/excellence/PHASE-EX3.md"
require_file "scripts/lib/media-rules.mjs"
require_file "scripts/lib/deck-caption.mjs"
require_file "scripts/validate-decks.mjs"
require_file "scripts/tests/media-rules.test.mjs"
require_file "scripts/tests/validate-decks.test.mjs"
require_file "scripts/tests/validate-cli-modes.test.mjs"
require_file "digital-creativity-pedagogy/excellence/evidence/SCHEMA-VERSION-WAVE1.md"
require_file "digital-creativity-pedagogy/excellence/curation/autopilot-assets.json"

check "node --test green" node --test scripts/tests/
check "validator --strict --rights=flag green" node scripts/validate-decks.mjs --strict --rights=flag
check "rights report written" test -f "$CASCADE/curation/rights-report.json"

present "build or package exposes validate:decks" "validate:decks" package.json
present "forge names schema_version 2" "schema_version" digital-creativity-pedagogy/forge/STUDENT-SLIDESHOW-FORGE.mdc
present "unit forge points at validate-decks" "validate-decks" digital-creativity-pedagogy/dc-unit-forge.mdc

# Tests must cover block / flag / orphan / reuse by name.
for t in "rights=block" "orphan" "reuse" "dangling" "index.php" "rights_review_required" "asset_id"; do
  present "test corpus covers: $t" "$t" scripts/tests/media-rules.test.mjs scripts/tests/validate-decks.test.mjs scripts/tests/validate-cli-modes.test.mjs
done

# No .php in either cache; do not require empty orphans in profield-cache (warn-only).
CACHE_NEW=docs/assets/images/deck-media
CACHE_LEGACY=docs/assets/images/profield-cache
if [ -d "$CACHE_NEW" ]; then
  n_php="$(find "$CACHE_NEW" -type f -name '*.php' 2>/dev/null | wc -l | tr -d ' ')"
  [ "$n_php" = 0 ] && pass "no .php in deck-media" || fail "$n_php .php files in deck-media"
fi
if [ -d "$CACHE_LEGACY" ]; then
  n_php="$(find "$CACHE_LEGACY" -type f -name '*.php' 2>/dev/null | wc -l | tr -d ' ')"
  [ "$n_php" = 0 ] && pass "no .php in profield-cache" || fail "$n_php .php files in profield-cache"
fi

# Referenced media must exist (do not delete cache files).
python3 - <<'GATEPY' && pass "all deck-referenced media files exist" || fail "all deck-referenced media files exist"
import pathlib, re, sys
missing = []
for p in pathlib.Path("docs/tracks").rglob("data/content.json"):
    for ref in set(re.findall(r"assets/images/(?:profield-cache|deck-media)/[0-9A-Za-z._-]+", p.read_text())):
        if not (pathlib.Path("docs") / ref).exists():
            missing.append(f"{p.parent.parent.name}: {ref}")
print(missing[:20]); sys.exit(1 if missing else 0)
GATEPY

finish
