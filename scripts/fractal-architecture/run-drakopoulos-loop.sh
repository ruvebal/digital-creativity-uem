#!/usr/bin/env bash
# Run Drakopoulos formula → fractal loop (steps 1–5).
# Author: ruvebal@crea-comm.net
set -euo pipefail

ROOT="${HOME}/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem"
BUNDLE="${HOME}/ahmes-library/scholar/documents/comparing_rendering_methods_for_julia_sets_a1e80611"
DB="${BUNDLE}/extract/extraction.db"
PDF="${HOME}/projects/ruvebal/scholar/bibliographies/design/Comparing_Rendering_Methods_for_Julia_Sets.pdf"
ORACLE="${ROOT}/digital-creativity-pedagogy/grounding/fractal-architecture/formula-audit/julia-rendering-oracle.json"
AUDIT_DIR="${BUNDLE}/extract/formula-audit"
AHEMES="${HOME}/src/ahmes"

echo "== Step 1: Promote the canonical oracle equation (visual audit gate) =="
mkdir -p "${AUDIT_DIR}/pages"
if [[ ! -f "${AUDIT_DIR}/pages/page-00.png" ]]; then
  magick -density 144 "${PDF}" "${AUDIT_DIR}/pages/page-%02d.png"
fi

cd "${AHEMES}" && . .venv/bin/activate
# Only eq-1 (the named iteration law) is CANONICAL and therefore promotable
# (AFEL §3.1/§4 derivation_role gate, ahmes/application/formula_glossary.py).
# eq-2..eq-5 are supporting/context equations — DERIVATION_STEP/WORKED_EXAMPLE —
# and are never promoted; build_render_brief reads their latex straight from
# this oracle file for the render brief's supporting_formulae list.
ahmes formula promote "${DB}" --eq eq-1 --oracle "${ORACLE}" --bundle "${BUNDLE}" \
  --derivation-role CANONICAL --fidelity EXACT
ahmes formula export "${DB}" -o "${AUDIT_DIR}/formula-glossary.private.json"
ahmes formula export "${DB}" -o "${AUDIT_DIR}/formula-glossary.public.json" --public

echo "== Step 2: Bibliographic meta (optional; requires Ollama for LLM path) =="
if ahmes enrich "${DB}" --meta --online 2>/dev/null; then
  CITE=$(ahmes query --cite "${DB}:$(sqlite3 "${DB}" "SELECT node_id FROM fission_node WHERE block_type='formula' LIMIT 1")" --style chicago-author-date 2>/dev/null || true)
else
  CITE="Drakopoulos, V. Comparing Rendering Methods for Julia Sets (oracle manual; enrich --meta pending)"
  echo "  meta enrich skipped or failed — using manual citation string"
fi

echo "== Step 3: Render brief (glossary → §11 JSON) =="
ahmes formula brief "${DB}" --oracle "${ORACLE}" \
  --private "${AUDIT_DIR}/render-brief.private.json" \
  --public "${AUDIT_DIR}/render-brief.public.json" \
  --eq eq-1 --seed 42 \
  ${CITE:+--citation "${CITE}"}

echo "== Step 4: Python escape-time Julia render + provenance sidecar =="
python3 "${ROOT}/scripts/fractal-architecture/render_julia_escape_time.py" \
  "${AUDIT_DIR}/render-brief.private.json" \
  -o "${AUDIT_DIR}/julia-eq1-escape-time.png" \
  --width 800 --height 800

echo "== Step 5: Controlled bibliography manifest (next references) =="
MANIFEST="${ROOT}/digital-creativity-pedagogy/grounding/fractal-architecture/formula-audit/design-bibliography-manifest.json"
echo "  Manifest: ${MANIFEST}"
python3 -c "import json; m=json.load(open('${MANIFEST}')); print('  entries:', len(m['entries']), 'complete:', sum(1 for e in m['entries'] if e.get('status')=='LOOP_COMPLETE'))"

echo "== Done =="
ls -la "${AUDIT_DIR}/julia-eq1-escape-time.png" "${AUDIT_DIR}/julia-eq1-escape-time.provenance.json" 2>/dev/null || true
