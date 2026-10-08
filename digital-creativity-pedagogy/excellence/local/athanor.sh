#!/usr/bin/env bash
# Athanor CLI with .env exported (CLI reads os.environ only).
# Usage: local/athanor.sh search "<query>" --project-slug profield-digital-creativity -L scholar --top-k 5
set -euo pipefail
ATHANOR_HOME="${ATHANOR_HOME:-$HOME/src/athanor}"
set -a; . "$ATHANOR_HOME/.env"; set +a
exec "$ATHANOR_HOME/.venv/bin/athanor" "$@"
