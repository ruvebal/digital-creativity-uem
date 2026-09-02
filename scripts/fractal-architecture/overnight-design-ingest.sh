#!/usr/bin/env bash
# Deferred design-library pipeline. Dry-run by default; never launched by this file alone.
set -euo pipefail

STUDIO_USER_ROOT="${STUDIO_USER_ROOT:-/Users/ruvebal}"
DESIGN_DIR="${DESIGN_DIR:-${STUDIO_USER_ROOT}/projects/ruvebal/scholar/bibliographies/design}"
AHMES_BIN="${AHMES_BIN:-${STUDIO_USER_ROOT}/src/ahmes/.venv/bin/ahmes}"
ATHANOR_BIN="${ATHANOR_BIN:-${STUDIO_USER_ROOT}/src/athanor/.venv/bin/athanor}"
ATHANOR_ENV="${ATHANOR_ENV:-${STUDIO_USER_ROOT}/src/athanor/.env}"
AHMES_LIBRARY="${AHMES_LIBRARY:-${STUDIO_USER_ROOT}/ahmes-library}"
PROJECT_SLUG="${PROJECT_SLUG:-profield-formula-driven-visual-systems}"
RUN_ROOT="${RUN_ROOT:-${STUDIO_USER_ROOT}/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem/digital-creativity-pedagogy/grounding/fractal-architecture/runs}"
AHMES_DEV_PLAN="${AHMES_DEV_PLAN:-${STUDIO_USER_ROOT}/src/ahmes/docs/DEV_PLAN}"
FORMULA_AUDIT_BUNDLE="${FORMULA_AUDIT_BUNDLE:-${AHMES_LIBRARY}/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611/extract/formula-audit}"
WORKERS="${WORKERS:-2}"
MODE="dry-run"
INJECT="no"
OPERATOR_APPROVED="no"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"

# Athanor needs exported connection settings for the injection stage. Never
# print this file; its values may contain database credentials.
if [[ -f "$ATHANOR_ENV" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ATHANOR_ENV"
  set +a
fi

while (($#)); do
  case "$1" in
    --execute) MODE="execute" ;;
    --inject) INJECT="yes" ;;
    --operator-approve) OPERATOR_APPROVED="yes" ;;
    --workers) shift; WORKERS="$1" ;;
    --run-id) shift; RUN_ID="$1" ;;
    *) printf 'Unknown argument: %s\n' "$1" >&2; exit 2 ;;
  esac
  shift
done

if [[ "$INJECT" == "yes" && "$MODE" != "execute" ]]; then
  printf '%s\n' '--inject requires --execute' >&2
  exit 2
fi

RUN_DIR="${RUN_ROOT}/${RUN_ID}"
MANIFEST="${RUN_DIR}/batch-manifest.json"
REPORT="${RUN_DIR}/batch-report.json"
FORMULA_READINESS_REPORT="${RUN_DIR}/formula-readiness-report.md"
F0_REPORT="${AHMES_DEV_PLAN}/PHASE-12H.F0-REPORT.md"
F1_REPORT="${AHMES_DEV_PLAN}/PHASE-12H.F1-REPORT.md"
F2_REPORT="${AHMES_DEV_PLAN}/PHASE-12H.F2-REPORT.md"
AFEL_PLAN="${AHMES_DEV_PLAN}/PHASE-12H.FC-FORMULA-EVIDENCE-LIFECYCLE.md"
AFEL_READINESS="${AFEL_READINESS:-${AHMES_DEV_PLAN}/PHASE-12H.FC-READINESS.json}"
FORMULA_GLOSSARY_PRIVATE="${FORMULA_AUDIT_BUNDLE}/formula-glossary.private.json"
FORMULA_GLOSSARY_PUBLIC="${FORMULA_AUDIT_BUNDLE}/formula-glossary.public.json"
mkdir -p "$RUN_DIR"

write_formula_readiness_report() {
  local status="DONE"
  local private_export_state="unchecked"
  local public_export_state="unchecked"
  local required_files=(
    "$F0_REPORT"
    "$F1_REPORT"
    "$F2_REPORT"
    "$FORMULA_GLOSSARY_PRIVATE"
    "$FORMULA_GLOSSARY_PUBLIC"
  )

  for file in "${required_files[@]}"; do
    if [[ ! -f "$file" ]]; then
      status="BLOCKED"
    fi
  done

  if ! command -v jq >/dev/null 2>&1; then
    status="BLOCKED"
    private_export_state="jq-missing"
    public_export_state="jq-missing"
  elif [[ -f "$FORMULA_GLOSSARY_PRIVATE" ]]; then
    if jq -e '(.entries | type) == "array" and ([.entries[] | select(((.fidelity_status == "EXACT") or (.fidelity_status == "USABLE_WITH_REPAIR")) and ((.latex | type) == "string") and ((.latex | length) > 0) and ((.mathml | type) == "string") and ((.mathml | length) > 0))] | length > 0)' "$FORMULA_GLOSSARY_PRIVATE" >/dev/null; then
      private_export_state="exportable-math-present"
    else
      status="BLOCKED"
      private_export_state="missing-exportable-math"
    fi
  else
    private_export_state="missing"
  fi

  if command -v jq >/dev/null 2>&1 && [[ -f "$FORMULA_GLOSSARY_PUBLIC" ]]; then
    if jq -e '.public_safe == true and ((.entries | type) == "array") and ([.entries[] | select(((.fidelity_status == "EXACT") or (.fidelity_status == "USABLE_WITH_REPAIR")) and ((.latex | type) == "string") and ((.latex | length) > 0) and ((.mathml | type) == "string") and ((.mathml | length) > 0))] | length > 0)' "$FORMULA_GLOSSARY_PUBLIC" >/dev/null; then
      public_export_state="public-exportable-math-present"
    else
      status="BLOCKED"
      public_export_state="missing-public-exportable-math"
    fi
  elif [[ "$public_export_state" != "jq-missing" ]]; then
    public_export_state="missing"
  fi

  {
    printf '# Formula readiness preflight\n\n'
    printf -- '- status: %s\n' "$status"
    printf -- '- run_id: %s\n' "$RUN_ID"
    printf -- '- mode: %s\n' "$MODE"
    printf -- '- operator_approval: %s\n' "$OPERATOR_APPROVED"
    printf -- '- checked_at_utc: %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    printf -- '- ahmes_dev_plan: `%s`\n' "$AHMES_DEV_PLAN"
    printf -- '- formula_audit_bundle: `%s`\n\n' "$FORMULA_AUDIT_BUNDLE"
    printf '## Required 12H reports and exports\n\n'
    printf '| Artifact | Required path | State |\n'
    printf '| --- | --- | --- |\n'
    for file in "${required_files[@]}"; do
      if [[ -f "$file" ]]; then
        printf '| `%s` | `%s` | present |\n' "$(basename "$file")" "$file"
      else
        printf '| `%s` | `%s` | missing |\n' "$(basename "$file")" "$file"
      fi
    done
    printf '\n'
    printf '## Exportable math check\n\n'
    printf '| Export | State |\n'
    printf '| --- | --- |\n'
    printf '| private glossary | %s |\n' "$private_export_state"
    printf '| public glossary | %s |\n\n' "$public_export_state"
    printf '## Policy\n\n'
    printf 'F0, F1, and F2 must exist before the broad design bibliography run is described as formula-ready. Formulae are exportable only from the glossary JSON files above. Athanor injection remains discovery-only and requires explicit `--inject`.\n'
  } > "$FORMULA_READINESS_REPORT"

  printf '%s' "$status"
}

FORMULA_STATUS="$(write_formula_readiness_report)"
printf 'formula_status=%s report=%s\n' "$FORMULA_STATUS" "$FORMULA_READINESS_REPORT"
if [[ "$MODE" == "execute" && "$FORMULA_STATUS" != "DONE" ]]; then
  printf '%s\n' 'Formula readiness is blocked. Complete PHASE-12H.F0/F1/F2 reports and glossary exports before broad bibliography ingestion.'
  exit 4
fi

validate_afel_readiness() {
  [[ -f "$AFEL_PLAN" ]] || return 1
  [[ -f "$AFEL_READINESS" ]] || return 1
  jq -e '
    .schema_version == "1.0.0" and
    .workflow == "AFEL" and
    .status == "CORPUS_READY" and
    ((.completed_phases | sort) == (["12H.FC0", "12H.FC1", "12H.FC2", "12H.FC3", "12H.FC4"] | sort)) and
    (.canary_report_sha256 | type == "string" and test("^[0-9a-f]{64}$")) and
    .public_firewall == "PASS" and
    .promotion_idempotence == "PASS" and
    .resume_test == "PASS" and
    (.approved_by | type == "string" and length > 0) and
    (.approved_at_utc | type == "string" and test("^[0-9]{4}-[0-9]{2}-[0-9]{2}T"))
  ' "$AFEL_READINESS" >/dev/null
}

if [[ "$MODE" == "execute" && "$OPERATOR_APPROVED" != "yes" ]] && ! validate_afel_readiness; then
  printf '%s\n' 'AFEL corpus gate is BLOCKED. Complete 12H.FC0-FC4 and provide a valid operator-approved PHASE-12H.FC-READINESS.json.' >&2
  printf 'plan=%s\nreadiness=%s\n' "$AFEL_PLAN" "$AFEL_READINESS" >&2
  exit 5
fi

if [[ "$MODE" == "execute" && "$OPERATOR_APPROVED" == "yes" ]]; then
  printf '%s\n' 'AFEL corpus gate overridden by explicit operator approval; promotion remains receipt-driven and Athanor injection remains separately controlled.'
fi

printf 'mode=%s\nsource=%s\nrun=%s\n' "$MODE" "$DESIGN_DIR" "$RUN_DIR"
"$AHMES_BIN" batch "$DESIGN_DIR" \
  --output "$AHMES_LIBRARY" \
  --library scholar \
  --workers "$WORKERS" \
  --manifest-path "$MANIFEST" \
  --report-path "$REPORT" \
  --dry-run

if [[ "$MODE" == "dry-run" ]]; then
  printf 'Dry-run complete. No bibliography was ingested or injected. formula_readiness_report=%s afel_readiness=%s\n' "$FORMULA_READINESS_REPORT" "$AFEL_READINESS"
  exit 0
fi

"$AHMES_BIN" batch "$DESIGN_DIR" \
  --output "$AHMES_LIBRARY" \
  --library scholar \
  --save-db \
  --treeshake \
  --enrich-ner \
  --enrich-semantic \
  --workers "$WORKERS" \
  --manifest-path "$MANIFEST" \
  --report-path "$REPORT"

DATABASE_LIST="${RUN_DIR}/database-paths.txt"
jq -r '.. | objects | select(.status? == "PROCESSED_OK") | .outputs.extraction_db? // empty' "$MANIFEST" | sort -u > "$DATABASE_LIST"
while IFS= read -r database; do
  [[ -f "$database" ]] || { printf 'Missing database from manifest: %s\n' "$database" >&2; exit 3; }
  "$AHMES_BIN" enrich "$database" --meta --online
done < "$DATABASE_LIST"

"$ATHANOR_BIN" inject \
  --from-manifest "$MANIFEST" \
  --project-slug "$PROJECT_SLUG" \
  --library scholar \
  --dry-run

if [[ "$INJECT" == "yes" ]]; then
  "$ATHANOR_BIN" inject \
    --from-manifest "$MANIFEST" \
    --project-slug "$PROJECT_SLUG" \
    --library scholar
fi

printf 'DONE manifest=%s report=%s formula_readiness_report=%s injected=%s\n' "$MANIFEST" "$REPORT" "$FORMULA_READINESS_REPORT" "$INJECT"
