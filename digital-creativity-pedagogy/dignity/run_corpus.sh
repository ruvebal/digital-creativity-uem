#!/usr/bin/env bash
# Explicitly authorized Dignity extraction and isolated research index injection.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
CORPUS=/Users/ruvebal/projects/ruvebal/scholar/dignity
AHMES=/Users/ruvebal/src/ahmes/.venv/bin/ahmes
ATHANOR=/Users/ruvebal/src/athanor/.venv/bin/athanor
set -a
source /Users/ruvebal/src/athanor/.env
set +a
"$AHMES" batch "$CORPUS" --output /Users/ruvebal/ahmes-library \
  --library scholar --save-db --treeshake --enrich-ner --enrich-semantic \
  --online --workers 2 > "$ROOT/corpus-pipeline.log" 2>&1
/Users/ruvebal/src/ahmes/scripts/profield-cite-ready.sh "$CORPUS" --json \
  > "$ROOT/bibliography-audit.log" 2>&1
"$ATHANOR" project list --library scholar > "$ROOT/athanor-projects-before.json"
if ! python3 - "$ROOT/athanor-projects-before.json" <<'PY'
import json, sys
projects=json.load(open(sys.argv[1]))
sys.exit(0 if any(p['slug']=='scholar-dignity' for p in projects) else 1)
PY
then
  "$ATHANOR" project create 'Dignity — supplied educational corpus' \
    --slug scholar-dignity --library scholar --application studio \
    --scope field_prospection > "$ROOT/athanor-project-created.json"
fi
"$ATHANOR" inject --from-manifest "$CORPUS/.ahmes/batch-manifest.json" \
  --project-slug scholar-dignity --library scholar --dry-run \
  > "$ROOT/athanor-dry-run.json"
"$ATHANOR" inject --from-manifest "$CORPUS/.ahmes/batch-manifest.json" \
  --project-slug scholar-dignity --library scholar > "$ROOT/athanor-injection.json"
"$ATHANOR" search 'dignidad valor inherente respeto diferencias escucha privacidad' \
  --project-slug scholar-dignity --library scholar --top-k 8 \
  > "$ROOT/athanor-smoke-query.json"
printf 'Corpus extraction, bibliography audit and Athanor injection completed.\n'
