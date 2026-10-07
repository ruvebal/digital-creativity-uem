#!/usr/bin/env bash
# PHASE-EX8.exit-gate.sh — Lab redesign Wave-1 + exercise cards (ACT1/ACT2)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

CAT="digital-creativity-pedagogy/catalogue/CANONICAL-METHODS.yml"
SIGN="$CASCADE/curation/LAB-SIGNOFF.md"
TOUCHED=(
  i-1-fashion-image
  i-2-2d-drawing
  i-3-color-bitmaps
  i-4-effects
  i-5-three-dimensional-form
)
# Lesson slug ≠ deck slug for I.1
declare -A LESSON_FOR=(
  [i-1-fashion-image]=i-1-digital-images
  [i-2-2d-drawing]=i-2-2d-drawing
  [i-3-color-bitmaps]=i-3-color-bitmaps
  [i-4-effects]=i-4-effects
  [i-5-three-dimensional-form]=i-5-three-dimensional-form
)

require_file "digital-creativity-pedagogy/excellence/PHASE-EX8.md"
require_file "$CAT"
check "lab sign-off file" test -f "$SIGN"
present "lab sign-off approved_by" "^approved_by: *autopilot" "$SIGN"
present "lab sign-off cites D1/D2" "findings: D1 · D2" "$SIGN"

# Exactly two lab_exercise slides; method_id in catalogue; practises → masterclass
ruby - "$CAT" "$DECKS" <<'RB' && pass "deck lab slides (exactly two + method_id + practises)" || fail "deck lab slides (exactly two + method_id + practises)"
require "yaml"
require "json"

cat = YAML.load_file(ARGV[0])
methods = cat.is_a?(Hash) && cat["methods"] ? cat["methods"] : (cat.is_a?(Array) ? cat : cat.values.flatten)
tech = methods.to_h { |t| [t["id"].to_s, t] }
bad = []
%w[
  i-1-fashion-image
  i-2-2d-drawing
  i-3-color-bitmaps
  i-4-effects
  i-5-three-dimensional-form
].each do |slug|
  path = File.join(ARGV[1], slug, "data/content.json")
  raw = File.read(path).sub(/\A---.*?---\s*/m, "")
  d = JSON.parse(raw)
  ids = d["slides"].select { |s| s["slide_role"] == "masterclass" }.map { |s| s["slide_id"] }
  labs = d["slides"].select { |s| s["slide_role"] == "lab_exercise" }
  bad << "#{slug}: #{labs.size} labs (need 2)" unless labs.size == 2
  labs.each do |s|
    mid = s["method_id"].to_s
    t = tech[mid]
    bad << "#{slug}: unknown method_id #{mid.inspect}" unless t
    pr = Array(s["practises"])
    bad << "#{slug}/#{s['slide_id']}: practises empty/invalid #{pr}" if pr.empty? || !(pr - ids).empty?
    bad << "#{slug}/#{s['slide_id']}: lab without notes" if s["notes"].to_s.strip.empty?
    bad << "#{slug}/#{s['slide_id']}: missing timer_seconds" if s["timer_seconds"].to_i <= 0
  end
end
# ACT anchors present on I.1–I.4 labs
want = {
  "i-1-fashion-image" => %w[figurin-digital],
  "i-2-2d-drawing" => %w[croquis-proportion-scaffold construction-vs-finish-lines],
  "i-3-color-bitmaps" => %w[key-visual-brief-lock gestalt-composition],
  "i-4-effects" => %w[photobash-integration],
}
want.each do |slug, ids|
  path = File.join(ARGV[1], slug, "data/content.json")
  raw = File.read(path).sub(/\A---.*?---\s*/m, "")
  d = JSON.parse(raw)
  have = d["slides"].select { |s| s["slide_role"] == "lab_exercise" }.map { |s| s["method_id"].to_s }
  ids.each { |id| bad << "#{slug}: missing ACT-aligned method #{id}" unless have.include?(id) }
end
warn_out = bad.first(40)
puts warn_out unless warn_out.empty?
exit(bad.empty? ? 0 : 1)
RB

# Lesson B2 cards: required labelled lines ×2
ruby - "$LESSONS" <<'RB' && pass "lesson B2 exercise cards" || fail "lesson B2 exercise cards"
require "json"
bad = []
map = {
  "i-1-digital-images" => "i-1-fashion-image",
  "i-2-2d-drawing" => "i-2-2d-drawing",
  "i-3-color-bitmaps" => "i-3-color-bitmaps",
  "i-4-effects" => "i-4-effects",
  "i-5-three-dimensional-form" => "i-5-three-dimensional-form",
}
labels = [
  "Time:",
  "Group:",
  "Materials:",
  "Steps:",
  "Portfolio trace:",
  "Judged by:",
  "Source:",
]
map.each_key do |lesson_slug|
  path = File.join(ARGV[0], lesson_slug, "index.md")
  lesson = File.read(path)
  # H2 Lab section only (`## ` + space so ### does not terminate early).
  b2 = lesson[/^## [^\n]*Lab[^\n]*\n[\s\S]*?(?=^## )/m].to_s
  bad << "#{lesson_slug}: B2 Lab section missing" if b2.empty?
  labels.each do |lab|
    n = b2.scan(/\*\*#{Regexp.escape(lab)}\*\*/).size
    bad << "#{lesson_slug}: '#{lab}' on #{n}/2 cards" if n < 2
  end
  # Exactly two exercise headings under B2
  ex = b2.scan(/^### Exercise \d+/).size
  bad << "#{lesson_slug}: #{ex} Exercise headings (need 2)" unless ex == 2
end
puts bad.first(40)
exit(bad.empty? ? 0 : 1)
RB

# No third lab slide left on I.2
absent "I.2 has no lab-3" '"slide_id": "lab-3"' "$DECKS/i-2-2d-drawing"

check "validator --strict green" node scripts/validate-decks.mjs --strict --rights=flag
check "render-decks runs" node scripts/render-decks.mjs
jekyll_build_ok

# Browser layout check (FINDINGS B4 / EX5 pattern). SKIP only when no Chrome.
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
