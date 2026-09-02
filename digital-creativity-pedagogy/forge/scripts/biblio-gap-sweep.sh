#!/usr/bin/env bash
# Biblio-gap sweep — Ahmes enrich --meta [--online] over scholar vaults + gap DOI audit.
# Usage: ./biblio-gap-sweep.sh [--online] [--log path]
set -euo pipefail

AHMES="${AHMES_BIN:-$HOME/src/ahmes/.venv/bin/ahmes}"
LIBRARY="${AHMES_LIBRARY:-$HOME/ahmes-library}"
LOG="${1:-$(dirname "$0")/../receipts/BIBLIO-GAP-SWEEP.log}"
ONLINE="${ONLINE:-1}"

: >"$LOG"
echo "# Ahmes biblio-gap sweep $(date -u +%Y-%m-%dT%H:%M:%SZ)" >>"$LOG"

# CD I/II high-priority gap DOIs (from lesson PROVENANCE_LINE ahmes_attempt fields)
GAP_DOIS=(
  10.1080/17543266.2017.1299226
  10.1080/1362704X.2016.1173349
  10.1080/1362704X.2024.2389595
  10.46328/ijtes.576
  10.1177/0098858819849990
  10.1002/eat.22449
  10.3389/ejcmp.2025.14563
)

for doi in "${GAP_DOIS[@]}"; do
  slug=$(ls "$LIBRARY/scholar/documents/" 2>/dev/null | rg -i "${doi//\./_}" | head -1 || true)
  if [[ -n "$slug" ]]; then
    db="$LIBRARY/scholar/documents/$slug/extract/extraction.db"
    echo "## DOI $doi — vault $slug" >>"$LOG"
    if [[ "$ONLINE" == "1" ]]; then
      "$AHMES" enrich --meta --online "$db" >>"$LOG" 2>&1 || true
    else
      "$AHMES" enrich --meta "$db" >>"$LOG" 2>&1 || true
    fi
    "$AHMES" status "$db" 2>&1 | rg -i 'evaluator_safe|Citation preview|title:|doi:' >>"$LOG" || true
  else
    echo "## DOI $doi — no vault (procurement required; see grounding/gap-fields/PENDING-procurement.md)" >>"$LOG"
  fi
  echo "" >>"$LOG"
done

vault_count=0
while IFS= read -r db; do
  if [[ "$ONLINE" == "1" ]]; then
    "$AHMES" enrich --meta --online "$db" >/dev/null 2>&1 || true
  else
    "$AHMES" enrich --meta "$db" >/dev/null 2>&1 || true
  fi
  vault_count=$((vault_count + 1))
done < <(find "$LIBRARY/scholar/documents" -name extraction.db 2>/dev/null)

echo "## Full library meta refresh: $vault_count vaults" >>"$LOG"
echo "Log: $LOG"
