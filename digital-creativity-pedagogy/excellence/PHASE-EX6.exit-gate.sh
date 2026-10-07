#!/usr/bin/env bash
# PHASE-EX6.exit-gate.sh — research grounding + single bibliography (Wave-1)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

MAN="$CASCADE/research-manifest.yml"
REFS="docs/_data/references.yml"
INC="docs/_includes/references.html"

require_file "$MAN"
require_file "$REFS"
require_file "$INC"
require_file "digital-creativity-pedagogy/excellence/PHASE-EX6.md"

absent "no hand-written reference spans in Wave-1" 'id="ref-' "${SCOPED_LESSONS[@]}"

# Front matter + include present; #ref- keys resolve to references.yml; verified
# manifest keys appear in references.yml; gap keys are not linked in student body.
ruby - "$MAN" "$REFS" "${SCOPED_LESSONS[@]}" <<'RB' && pass "manifest, refs and citations agree" || fail "manifest, refs and citations agree"
require "yaml"
man = YAML.load_file(ARGV[0])
refs = YAML.load_file(ARGV[1])
man_works = man.is_a?(Hash) && man["works"] ? man["works"] : man
ref_keys = refs.is_a?(Hash) ? refs.keys.map(&:to_s) : []
bad = []

# Critical-layer D2 works must be present (verified or gap)
d2_keys = ["steimberg-2013", "werhane-2026", "munari-design-method"]
d2_keys.each do |k|
  bad << "manifest lacks D2 critical key #{k}" unless man_works.any? { |w| w["key"].to_s == k }
end

man_works.each do |w|
  key = w["key"].to_s
  st = w["status"].to_s
  bad << "#{key}: bad status #{st.inspect}" unless %w[verified gap].include?(st)
  if st == "verified"
    bad << "#{key}: verified but missing from references.yml" unless ref_keys.include?(key)
    bad << "#{key}: verified missing page_basis" unless %w[printed section].include?(w["page_basis"].to_s)
  end
end

# Every references.yml key must be a verified manifest entry
ref_keys.each do |k|
  w = man_works.find { |x| x["key"].to_s == k }
  bad << "references.yml #{k} not in manifest" unless w
  bad << "references.yml #{k} not status=verified" if w && w["status"].to_s != "verified"
end

gap_keys = man_works.select { |w| w["status"].to_s == "gap" }.map { |w| w["key"].to_s }

ARGV[2..].each do |path|
  # SCOPED_LESSONS may be dirs or the ML path
  files = File.directory?(path) ? Dir.glob(File.join(path, "index.md")) : [path]
  files = files.select { |f| File.file?(f) }
  files.each do |f|
    t = File.read(f)
    bad << "#{f}: missing references.html include" unless t.include?("{% include references.html %}")
    bad << "#{f}: missing front-matter references:" unless t =~ /^references:\s*\[/m
    fm = t[/\A---\n(.*?)\n---/m, 1].to_s
    listed = fm[/^references:\s*\[([^\]]*)\]/, 1].to_s.split(",").map { |s| s.strip }.reject(&:empty?)
    listed.each do |k|
      bad << "#{f}: front-matter key #{k} missing from references.yml" unless ref_keys.include?(k)
    end
    cited = t.scan(/#ref-([\w-]+)/).flatten.uniq
    cited.each do |c|
      bad << "#{f}: cites unknown #ref-#{c}" unless ref_keys.include?(c)
      bad << "#{f}: gap key #{c} linked in student text" if gap_keys.include?(c)
    end
    listed.each do |k|
      bad << "#{f}: listed #{k} never cited via #ref-" unless cited.include?(k)
    end
    # VERIFIED provenance lines declare page_basis
    t.each_line do |line|
      next unless line.include?("PROVENANCE_LINE") && line.include?("status=VERIFIED")
      unless line =~ /page_basis=(printed|section)/
        bad << "#{f}: VERIFIED line missing page_basis: #{line.strip[0, 90]}"
      end
    end
  end
end

puts bad.first(40)
exit(bad.empty? ? 0 : 1)
RB

jekyll_build_ok
publication_safety_ok

# Built Wave-1 HTML: every #ref- has matching id
python3 - <<'PY' && pass "built #ref- anchors resolve" || fail "built #ref- anchors resolve"
import pathlib, re, sys
root = pathlib.Path("_site")
if not root.exists():
    print("no _site"); sys.exit(1)
bad = []
# Wave-1 lesson HTML paths
patterns = [
    "**/digital-creativity-i/**/*.html",
    "**/creacion-digital-i/**/*.html",
    "**/fashion-image-analysis/**/*.html",
    "**/analisis-imagen-moda/**/*.html",
]
files = []
for p in patterns:
    files.extend(root.glob(p))
for f in files:
    t = f.read_text(errors="ignore")
    hrefs = set(re.findall(r'href="#(ref-[\w-]+)"', t))
    ids = set(re.findall(r'id="(ref-[\w-]+)"', t))
    missing = sorted(hrefs - ids)
    if missing:
        bad.append(f"{f.relative_to(root)}: missing ids {missing}")
print("\n".join(bad[:20]))
sys.exit(1 if bad else 0)
PY

finish
