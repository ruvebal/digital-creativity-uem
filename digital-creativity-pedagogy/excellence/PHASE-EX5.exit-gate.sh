#!/usr/bin/env bash
# EX5 exit gate — deck renderer (pre-render, alt, captions, notes, browser layout).
# shellcheck source=/dev/null
source "$(git rev-parse --show-toplevel)/digital-creativity-pedagogy/excellence/gates/common.sh"

check "render-decks runs" node scripts/render-decks.mjs
check "validator --strict green" node scripts/validate-decks.mjs --strict --rights=flag
build_site
absent "no hard-coded base path in deck JS" "/digital-creativity-uem" docs/assets/js/student-media-deck.js
absent "no timestamped runtime fetch" "Date\.now\(\)" docs/assets/js/student-media-deck.js
present "render step wired into prebuild" "render-decks" package.json
present "browser test script wired" "test:browser" package.json

n_geo="$(ls docs/assets/images/fractal-pass-track/uem-henon-pass-*.svg 2>/dev/null | wc -l | tr -d ' ')"
n_hash="$(ls docs/assets/images/fractal-pass-track/uem-henon-pass-*.svg 2>/dev/null | grep -cE -- '-[0-9a-f]{8,}\.svg$' || true)"
[ "$n_geo" -gt 0 ] && [ "$n_geo" = "$n_hash" ] && pass "geometric SVGs carry a hash ($n_hash/$n_geo)" || fail "geometric SVGs carry a hash ($n_hash/$n_geo)"

require_file "docs/assets/images/fractal-triangles/current.json"
require_file "scripts/tests/browser/deck-layout.mjs"

python3 - <<'PY' && pass "pre-rendered sections, alt text, notes (Wave-1)" || fail "pre-rendered sections, alt text, notes (Wave-1)"
import json, pathlib, re, sys
bad = []
roots = [
    pathlib.Path("docs/tracks/en/uem/2627-dci"),
    pathlib.Path("docs/tracks/en/uem/2627-ml"),
]
# Wave-1 hard-fail set (A1): I.1–I.5 + fashion-image-analysis
wave1 = {
    "i-1-fashion-image", "i-2-2d-drawing", "i-3-color-bitmaps",
    "i-4-effects", "i-5-three-dimensional-form", "fashion-image-analysis",
}
for root in roots:
    for p in sorted(root.glob("*/data/content.json")):
        slug = p.parent.parent.name
        if slug not in wave1:
            continue
        raw = re.sub(r"^---[\s\S]*?---\s*", "", p.read_text())
        d = json.loads(raw)
        if d.get("schema_version") != 2:
            bad.append(f"{slug}: expected schema_version 2"); continue
        html = pathlib.Path("_site/tracks/dci") / slug / "index.html"
        if slug == "fashion-image-analysis":
            html = pathlib.Path("_site/master-lectures/fashion-image-analysis/index.html")
        if not html.exists():
            cands = [c for c in pathlib.Path("_site").rglob(f"{slug}/index.html") if "<section" in c.read_text()]
            html = cands[0] if cands else html
        if not html.exists():
            bad.append(f"{slug}: built deck not found"); continue
        t = html.read_text()
        n = len(re.findall(r"<section\b", t))
        if n != len(d["slides"]):
            bad.append(f"{slug}: {n} sections vs {len(d['slides'])} slides")
        for s in d["slides"]:
            sid = s.get("slide_id")
            role = s.get("slide_role")
            if role in ("masterclass", "lab_exercise", "workshop_work") and not s.get("notes"):
                bad.append(f"{slug}: {sid} missing notes")
        if 'class="notes"' not in t:
            bad.append(f"{slug}: no notes asides in built HTML")
        curated = sum(1 for s in d["slides"] if s.get("background_kind") == "curated")
        alt_hits = t.count("data-alt") + t.count('class="sr-only"') + t.count('class="visually-hidden"')
        if curated and alt_hits < curated:
            bad.append(f"{slug}: alt text elements ({alt_hits}) fewer than curated slides ({curated})")
        if curated and t.count("slide-caption") < curated:
            bad.append(f"{slug}: captions fewer than curated slides")
print("\n".join(bad))
sys.exit(1 if bad else 0)
PY

# Browser layout check (FINDINGS B4). SKIP only when no Chrome; on Tanit Chrome is present.
DL_LOG="$(mktemp -t excellence-deck-layout)"
if node scripts/tests/browser/deck-layout.mjs > "$DL_LOG" 2>&1; then
  if grep -q "SKIP" "$DL_LOG"; then
    fail "browser layout check skipped (no Chrome)"
  else
    pass "browser layout check: $(tail -1 "$DL_LOG")"
  fi
else
  fail "browser layout check"
  tail -20 "$DL_LOG"
fi

finish
