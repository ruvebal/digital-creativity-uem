#!/usr/bin/env bash
# PHASE-EX4.exit-gate.sh — slide-bound curation + rights (Wave-1)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

check "validator --strict --rights=flag green" node scripts/validate-decks.mjs --strict --rights=flag

python3 - "$DECKS" "$ML_DECKS" <<'PY' && pass "curation rules (≥60% core curated, briefs, rights, no reuse)" || fail "curation rules"
import json, pathlib, re, sys
bad = []
CORE = {"unit_cover", "analysis_model", "masterclass", "lab_exercise", "workshop_work"}
WAVE = []
for root in sys.argv[1:]:
    for p in pathlib.Path(root).glob("*/data/content.json"):
        s = str(p)
        if "how-to-pass" in s:
            continue
        if "/2627-dci/i-" not in s and "/fashion-image-analysis/" not in s:
            continue
        WAVE.append(p)
for p in WAVE:
    d = json.loads(re.sub(r"^---[\s\S]*?---\s*", "", p.read_text()))
    if d.get("schema_version") != 2:
        bad.append(f"{p}: schema_version != 2")
        continue
    assets = {a.get("asset_id"): a for a in d.get("assets", [])}
    used = []
    for s in d["slides"]:
        if s.get("background_kind") != "curated":
            continue
        a = assets.get(s.get("asset_id"))
        if not s.get("image_brief") or "TODO" in s.get("image_brief", ""):
            bad.append(f"{p}: {s.get('slide_id')} brief missing")
        if not a:
            bad.append(f"{p}: {s.get('slide_id')} asset missing")
            continue
        for k in ("licence", "author", "canonical_source_url", "alt_text"):
            if not a.get(k):
                bad.append(f"{p}: {s.get('slide_id')} asset lacks {k}")
        if a.get("rights_status") not in ("ok", "flagged"):
            bad.append(f"{p}: {s.get('slide_id')} rights_status missing")
        used.append(s.get("asset_id"))
    if len(used) != len(set(used)):
        bad.append(f"{p}: asset reused within deck")
    core = [s for s in d["slides"] if s.get("slide_role") in CORE]
    imaged = [s for s in core if s.get("background_kind") == "curated"]
    if core and len(imaged) / len(core) < 0.6:
        bad.append(f"{p}: only {len(imaged)}/{len(core)} core slides curated")
print("\n".join(bad[:40]))
sys.exit(1 if bad else 0)
PY

SIGN="$CASCADE/curation/CURATION-SIGNOFF.md"
check "sign-off file" test -f "$SIGN"
present "sign-off approved_by" "^approved_by: *[^ ]" "$SIGN"
present "sign-off approved_on" "^approved_on: *[0-9]{4}-" "$SIGN"
check "autopilot-assets.json" test -f "$CASCADE/curation/autopilot-assets.json"
check "rights-report.json" test -f "$CASCADE/curation/rights-report.json"

python3 - "$CASCADE/curation/autopilot-assets.json" <<'PY' && pass "registry has assets with raw_title" || fail "registry empty/missing raw_title"
import json, sys
reg = json.load(open(sys.argv[1]))
assets = reg.get("assets") or []
bad = [a.get("asset_id") for a in assets if not str(a.get("raw_title") or "").strip()]
print("assets", len(assets), "missing raw_title", bad[:5])
sys.exit(0 if assets and not bad else 1)
PY

python3 - "$DECKS" "$ML_DECKS" "$CASCADE/curation/autopilot-assets.json" <<'PY' && pass "bound assets registered with raw_title (A6/F3)" || fail "bound assets registered with raw_title (A6/F3)"
import json, pathlib, re, sys
reg = {a["asset_id"]: a for a in json.load(open(sys.argv[3])).get("assets", [])}
bad = []
for root in sys.argv[1:3]:
    for p in pathlib.Path(root).glob("*/data/content.json"):
        s = str(p)
        if "how-to-pass" in s:
            continue
        if "/2627-dci/i-" not in s and "/fashion-image-analysis/" not in s:
            continue
        d = json.loads(re.sub(r"^---[\s\S]*?---\s*", "", p.read_text()))
        if d.get("schema_version") != 2:
            continue
        for slide in d["slides"]:
            if slide.get("background_kind") == "curated":
                a = reg.get(slide.get("asset_id"))
                if not a or not a.get("raw_title"):
                    bad.append(f"{p.parent.parent.name}:{slide.get('slide_id')}")
print(bad[:20])
sys.exit(1 if bad else 0)
PY

# Amendment A6/F1: death-year contradiction always fails rightsVerdict.
node --input-type=module -e "
import { rightsVerdict } from './scripts/lib/media-rules.mjs';
const v = rightsVerdict({ licence: 'PD-old-70', author: 'Marcel Duchamp', author_death_year: 1968,
  eu_term_reason: 'public domain in the US', canonical_source_url: 'https://commons.wikimedia.org/x', title: 'x' });
process.exit(v && v.ok === false ? 0 : 1);
" && pass "rightsVerdict rejects contradicting death year (A6/F1)" || fail "rightsVerdict rejects contradicting death year (A6/F1)"

if find docs/assets/images/deck-media -name '*.svg' 2>/dev/null | grep -q .; then
  fail "raw SVG in deck-media (A6/F6)"
else
  pass "no raw SVG in deck-media (A6/F6)"
fi

check "EX4 vision evidence" test -f "$CASCADE/evidence/EX4/vision_raw.json"
check "EX4 shortlists present" test -f "$CASCADE/curation/I.1-SHORTLIST.md"

# EX3 F2: rehydrate must not rank-deal
if grep -n "rankCursor" scripts/rehydrate-student-media.mjs >/dev/null; then
  fail "rehydrate still uses rankCursor (EX3 F2)"
else
  pass "rehydrate uses bindSlides (no rankCursor)"
fi
if grep -n "bindSlides" scripts/rehydrate-student-media.mjs >/dev/null; then
  pass "rehydrate imports bindSlides"
else
  fail "rehydrate missing bindSlides"
fi

check "node tests green" node --test scripts/tests/*.test.mjs

finish
