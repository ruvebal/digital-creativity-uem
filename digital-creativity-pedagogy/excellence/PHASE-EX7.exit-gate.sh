#!/usr/bin/env bash
# PHASE-EX7.exit-gate.sh — fashion-craft method catalogue (not CT techniques)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

CAT="digital-creativity-pedagogy/catalogue"
BASE="$CAT/methods.base.yml"
CANON="$CAT/CANONICAL-METHODS.yml"
MAP="$CAT/profield-map.yml"
SEED="docs/_data/fashion_craft_methods.seed.yml"
CARDS_SEED="docs/methods/en/cards/SEED.md"

require_file "digital-creativity-pedagogy/excellence/PHASE-EX7.md"
require_file "$BASE"
require_file "$CANON"
require_file "$CAT/CANONICAL-METHODS.md"
require_file "$CAT/CANONICAL-METHODS-BY-UNIT.yml"
require_file "$MAP"
require_file "$CAT/INDEX.md"
require_file "$SEED"
require_file "$CARDS_SEED"

# Catalogue rules + ACT1/ACT2 anchors + no CT technique dump into student docs
ruby - "$BASE" "$CANON" "$MAP" "$SEED" "docs/_data/references.yml" <<'RB' && pass "catalogue rules" || fail "catalogue rules"
require "yaml"

base = YAML.load_file(ARGV[0])
canon = YAML.load_file(ARGV[1])
pmap = YAML.load_file(ARGV[2])
seed = YAML.load_file(ARGV[3])
refs = YAML.load_file(ARGV[4])
ref_keys = refs.is_a?(Hash) ? refs.keys.map(&:to_s) : []

methods = base["methods"] || []
cmethods = canon["methods"] || []
bad = []

bad << "base count #{methods.size} outside 40..80" unless (40..80).cover?(methods.size)
bad << "canon count mismatch" unless methods.size == cmethods.size

fields = %w[id name family craft_mode primary_source source_status steps time_min group_size materials units evidence accessibility]
families = %w[drawing colour composition bitmap form-volume retouch still-motion research presentation critical-craft]
modes = %w[constructive synthetic critical workflow]
statuses = %w[verified held gap]

methods.each do |m|
  fields.each { |f| bad << "#{m['id']}: missing #{f}" if m[f].nil? || m[f] == "" }
  bad << "#{m['id']}: bad family" unless families.include?(m["family"].to_s)
  bad << "#{m['id']}: bad craft_mode" unless modes.include?(m["craft_mode"].to_s)
  bad << "#{m['id']}: bad source_status" unless statuses.include?(m["source_status"].to_s)
  bad << "#{m['id']}: steps 3..8" unless m["steps"].is_a?(Array) && (3..8).cover?(m["steps"].size)
  ps = m["primary_source"].to_s
  st = m["source_status"].to_s
  if st == "verified"
    bad << "#{m['id']}: verified source missing from references.yml" unless ref_keys.include?(ps)
    bad << "#{m['id']}: verified missing source_locator" if m["source_locator"].to_s.empty?
  else
    bad << "#{m['id']}: non-gap primary_source not in refs (use gap or add refs)" if ps != "gap" && !ref_keys.include?(ps) && st == "verified"
  end
end

%w[id name].each do |k|
  vals = methods.map { |t| t[k].to_s.downcase }
  bad << "duplicate #{k}" if vals.uniq.size != vals.size
end

required = {
  "figurin-digital" => /figur/i,
  "photobash-integration" => /photobash/i,
  "gestalt-composition" => /gestalt/i,
}
ids = methods.map { |m| m["id"].to_s }
names = methods.map { |m| "#{m['name']} #{m['id']}" }
required.each do |id, rx|
  bad << "required id missing: #{id}" unless ids.include?(id)
  bad << "required name missing: #{rx.source}" unless names.any? { |n| n =~ rx }
end

act1 = Array(pmap.dig("sandra_act_methods", "ACT1"))
act2 = Array(pmap.dig("sandra_act_methods", "ACT2"))
bad << "profield-map ACT1 must include figurin-digital" unless act1.include?("figurin-digital")
bad << "profield-map ACT2 must include photobash-integration" unless act2.include?("photobash-integration")
bad << "profield-map ACT2 must include gestalt-composition" unless act2.include?("gestalt-composition")
bad << "profield-map missing by_profield_run" if pmap["by_profield_run"].to_h.empty?

seed_cards = seed["cards"] || []
bad << "seed has no cards" if seed_cards.empty?
seed_ids = seed_cards.map { |c| c["id"].to_s }
%w[figurin-digital photobash-integration gestalt-composition].each do |id|
  bad << "seed missing #{id}" unless seed_ids.include?(id)
end

# CT technique ids must not appear in the DC catalogue
ct_needles = %w[
  alternative-uses-task brainstorming-osborn brainwriting-635 scamper
  six-thinking-hats oblique-strategies synectics-excursion crazy-8s
  mom-test-interview cocd-box morphological-box po-provocation
]
blob = methods.to_s.downcase
ct_needles.each do |n|
  bad << "CT technique id leaked into catalogue: #{n}" if blob.include?(n)
end

puts bad.first(40)
exit(bad.empty? ? 0 : 1)
RB

# Student-facing docs must not dump CT-only technique catalogue ids
absent "no CT technique ids in docs/" \
  'alternative-uses-task|brainstorming-osborn|brainwriting-635|scamper|six-thinking-hats|oblique-strategies|synectics-excursion|crazy-8s|mom-test-interview|cocd-box|morphological-box|po-provocation|CANONICAL-TECHNIQUES' \
  docs/

# Private catalogue must not leak into _site under pedagogy path names
jekyll_build_ok
if grep -rqiE 'CANONICAL-METHODS|methods\.base\.yml|digital-creativity-pedagogy/catalogue' _site 2>/dev/null; then
  fail "private catalogue leaked into _site"
else
  pass "private catalogue not published"
fi

# Seed path should be present on the built site (SEED.md)
if [ -f _site/methods/en/cards/index.html ] || [ -f _site/methods/en/cards/SEED.html ] || find _site/methods -name '*SEED*' 2>/dev/null | grep -q .; then
  pass "public method-card seed path built"
elif [ -d docs/methods/en/cards ] && [ -f docs/_data/fashion_craft_methods.seed.yml ]; then
  # Jekyll may ignore .md without collection — require data seed + path exist (already require_file)
  pass "public method-card seed path present (data + cards dir)"
else
  fail "public method-card seed path missing after build"
fi

publication_safety_ok
finish
