#!/usr/bin/env bash
# Refresh Profield media collections — studio machine only.
# CI / machines without ~/src/profield must no-op (exit 0).
set -euo pipefail

PROFIELD_ROOT="${PROFIELD_ROOT:-${HOME}/src/profield}"
if [[ ! -d "${PROFIELD_ROOT}" ]]; then
  echo "media:refresh: skip — Profield not found at ${PROFIELD_ROOT} (CI/local without studio mount)."
  exit 0
fi

cd "${PROFIELD_ROOT}"
exec make media-refresh-collections MIN_RANK="${MIN_RANK:-1}"
