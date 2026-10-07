# Shared helpers for PHASE-EXn.exit-gate.sh scripts. Source, do not execute.
# Each gate counts failures and exits non-zero if any check failed, so the
# verify log shows every failing check, not only the first one.
set -uo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT" || exit 2
CASCADE="digital-creativity-pedagogy/excellence"
# Wave-1 decks (A1): Creación Digital I track + master-lecture decks
DECKS="docs/tracks/en/uem/2627-dci"
ML_DECKS="docs/tracks/en/uem/2627-ml"
LESSONS="docs/lessons/en/digital-creativity-i"
FAILS=0

# Scope: CD I lessons + fashion-image-analysis special (not CD II / NM).
SCOPED_LESSONS=()
for d in "$LESSONS"/* docs/lessons/en/master-lectures/fashion-image-analysis; do
  [ -e "$d" ] && SCOPED_LESSONS+=("$d")
done
SCOPED_DECKS=()
for d in "$DECKS"/* "$ML_DECKS"/*; do
  [ -d "$d" ] && SCOPED_DECKS+=("$d")
done

# Built-site HTML in Wave-1 scope (drop CD II / NM paths).
scoped_site_html() {
  find _site -name '*.html' 2>/dev/null \
    | grep -vE '/digital-creativity-ii/|/creacion-digital-ii/|/nuevos-medios' \
    || true
}

pass() { echo "PASS: $*"; }
fail() { echo "FAIL: $*"; FAILS=$((FAILS + 1)); }

require_file() {
  local f="$1"
  if [ -f "$f" ]; then pass "file $f"; else fail "missing file $f"; fi
}

check() {
  local label="$1"; shift
  if "$@" >/dev/null 2>&1; then pass "$label"; else fail "$label"; fi
}

absent() {
  local label="$1" regex="$2"; shift 2
  local hits
  hits="$(grep -rniE -- "$regex" "$@" 2>/dev/null | head -5)"
  if [ -z "$hits" ]; then pass "$label"; else fail "$label"; echo "$hits"; fi
}

present() {
  local label="$1" regex="$2"; shift 2
  if grep -rqiE -- "$regex" "$@" 2>/dev/null; then pass "$label"; else fail "$label"; fi
}

build_site() {
  rm -rf _site
  if bundle exec jekyll build --source docs --destination _site --config _config.yml >/tmp/dc-excellence-build.log 2>&1; then
    pass "jekyll build"
  else
    fail "jekyll build (see /tmp/dc-excellence-build.log)"; tail -20 /tmp/dc-excellence-build.log
  fi
}

jekyll_build_ok() { build_site; }

publication_safety_ok() {
  if [ ! -f scripts/verify-publication-safety.mjs ]; then
    fail "verify-publication-safety.mjs missing"
    return
  fi
  if [ ! -d _site ]; then build_site; fi
  if node scripts/verify-publication-safety.mjs >/tmp/dc-excellence-safety.log 2>&1; then
    pass "publication safety"
  else
    fail "publication safety (see /tmp/dc-excellence-safety.log)"
    tail -30 /tmp/dc-excellence-safety.log
  fi
}

finish() {
  echo "----"
  echo "failures: $FAILS"
  [ "$FAILS" -eq 0 ]
}
