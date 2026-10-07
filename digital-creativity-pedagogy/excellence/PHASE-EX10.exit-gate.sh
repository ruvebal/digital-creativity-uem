#!/usr/bin/env bash
# PHASE-EX10.exit-gate.sh — Assessment layer + D2≡ACT3 lock + consent drafts
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

A="$CASCADE/assessment"

require_file "$A/question-bank.yml"
require_file "$A/TRANSPOSITION-BRIEF.md"
require_file "$A/DIVERGENCE-VS-PLAN-DE-TRABAJO.md"
require_file "$A/APPROVAL.md"
require_file "digital-creativity-pedagogy/consent/CONSENT-FORM-EN.md"
require_file "digital-creativity-pedagogy/consent/CONSENT-FORM-ES.md"

present "approval drafts-only" "approved_by: *autopilot \(drafts" "$A/APPROVAL.md"
present "approval status DRAFT" "^status: *DRAFT" "$A/APPROVAL.md"
absent "no DPO clearance claim in APPROVAL" "DPO (approved|clearance|granted)|dpo_approved" "$A/APPROVAL.md"
absent "measurement not started (APPROVAL)" "measurement (started|in progress|collecting)" "$A/APPROVAL.md"
present "measurement never starts (APPROVAL)" "Not started" "$A/APPROVAL.md"
present "measurement never starts (consent EN)" "never starts|No data are collected under the current draft" \
  digital-creativity-pedagogy/consent/CONSENT-FORM-EN.md

# Transposition brief: cartel + other-language (EN + ES)
present "brief EN cartel" "cartel" "$A/TRANSPOSITION-BRIEF.md"
present "brief EN other language" "another language" "$A/TRANSPOSITION-BRIEF.md"
present "brief ES cartel" "cartel" "$A/TRANSPOSITION-BRIEF.md"
present "brief ES otro lenguaje" "otro lenguaje" "$A/TRANSPOSITION-BRIEF.md"
present "divergence table exists" "Divergence" "$A/DIVERGENCE-VS-PLAN-DE-TRABAJO.md"

# Question bank rules (Ruby — matches CT EX10 shape)
ruby - "$A/question-bank.yml" docs/_data/references.yml <<'RB' && pass "question bank rules" || fail "question bank rules"
require "yaml"
bank = YAML.load_file(ARGV[0])
qs = bank.is_a?(Hash) ? bank["questions"] : bank
refs = YAML.load_file(ARGV[1])
keys = refs.is_a?(Hash) ? refs.keys.map(&:to_s) : refs.map { |r| r["key"].to_s }
units = bank["units"] || {}
bad = []
qs.each_with_index do |q, i|
  %w[unit ra type stem answer ref bloom].each { |f| bad << "q#{i}/#{q['id']}: missing #{f}" if q[f].to_s.empty? }
  bad << "#{q['id']}: ref #{q['ref']} unknown" unless keys.include?(q["ref"].to_s)
  bad << "#{q['id']}: mcq without distractors" if q["type"] == "mcq" && Array(q["distractors"]).size < 2
  info = units[q["unit"]]
  if info
    lesson = info["lesson"].to_s.sub(%r{\A/}, "").sub(%r{/\z}, "")
    md = File.read("docs/#{lesson}/index.md")
    m = md.match(/^references:\s*\[(.*?)\]/m)
    lesson_refs = m ? m[1].split(",").map { |s| s.strip }.reject(&:empty?) : []
    bad << "#{q['id']}: ref #{q['ref']} not in lesson front matter" unless lesson_refs.include?(q["ref"].to_s)
  else
    bad << "#{q['id']}: unknown unit #{q['unit']}"
  end
end
high = qs.count { |q| %w[apply analyse analyze evaluate create].include?(q["bloom"].to_s.downcase) }
share = qs.empty? ? 0.0 : high.to_f / qs.size
puts "higher-order share: #{high}/#{qs.size} (#{(share * 100).round(1)}%)"
bad << "higher-order share #{high}/#{qs.size} < 30%" if share < 0.3
puts bad.first(30)
exit(bad.empty? ? 0 : 1)
RB

# Optional retrieval slides: exactly one per bank unit that names a deck path
BANK_YML="$A/question-bank.yml" node <<'NODE' && pass "retrieval slides (optional, consistent)" || fail "retrieval slides"
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const bank = yaml.load(fs.readFileSync(process.env.BANK_YML, 'utf8'));
const bad = [];
for (const [unit, info] of Object.entries(bank.units || {})) {
  const deck = info.deck;
  if (!deck) continue;
  const p = path.join(deck, 'data', 'content.json');
  if (!fs.existsSync(p)) { bad.push(`missing deck ${p}`); continue; }
  const text = fs.readFileSync(p, 'utf8').replace(/^---[\s\S]*?---\s*/, '');
  const d = JSON.parse(text);
  const slides = d.slides || [];
  const idxs = slides.map((s, i) => (s.slide_role === 'retrieval' ? i : -1)).filter((i) => i >= 0);
  if (idxs.length !== 1) { bad.push(`${p}: ${idxs.length} retrieval slides (need 1)`); continue; }
  const i = idxs[0];
  if (!slides[i + 1] || slides[i + 1].slide_role !== 'lab_opener') {
    bad.push(`${p}: retrieval not immediately before lab_opener`);
  }
  const qs = slides[i].questions || [];
  if (qs.length !== 5) bad.push(`${p}: ${qs.length} retrieval questions`);
  if (!/answer/i.test(slides[i].notes || '')) bad.push(`${p}: retrieval notes missing answers`);
  if (slides[i].background_kind !== 'geometrical') bad.push(`${p}: retrieval background_kind`);
}
if (bad.length) console.error(bad.join('\n'));
process.exit(bad.length ? 1 : 0);
NODE

jekyll_build_ok
publication_safety_ok

# Practice quizzes: ≥5 data-question each for banked public units
for slug in i-1-digital-images i-2-2d-drawing i-3-color-bitmaps i-5-three-dimensional-form i-6-volume i-7-fashion-references fashion-image-analysis; do
  f="_site/practice/en/${slug}/index.html"
  if [ -f "$f" ] && [ "$(grep -o 'data-question' "$f" | wc -l | tr -d ' ')" -ge 5 ]; then
    pass "practice quiz $slug"
  else
    fail "practice quiz $slug (need 5 data-question in $f)"
  fi
done

# Private assessment / consent must not leak into _site
if grep -rqiE "question-bank\.yml|DIVERGENCE-VS-PLAN|CONSENT-FORM-EN|approved_by: autopilot \(drafts" _site 2>/dev/null; then
  fail "private assessment/consent artefacts leaked into _site"
else
  pass "assessment + consent stay private"
fi

# Consent must remain drafts-only language
present "consent EN draft banner" "DRAFT — not for use" digital-creativity-pedagogy/consent/CONSENT-FORM-EN.md
present "consent ES draft banner" "BORRADOR — no usar" digital-creativity-pedagogy/consent/CONSENT-FORM-ES.md
absent "consent EN no DPO claimed" "DPO (has )?(approved|clearance)|aprobación del DPO concedida" \
  digital-creativity-pedagogy/consent/CONSENT-FORM-EN.md digital-creativity-pedagogy/consent/CONSENT-FORM-ES.md

finish
