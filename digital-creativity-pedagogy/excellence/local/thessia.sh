#!/usr/bin/env bash
# Local Thessia over Ollama HTTP. Voice only on grounded drafts (LOCAL-EXECUTION.md).
# Usage: local/thessia.sh <prompt-file> [model] [num_predict]  > draft.md
set -euo pipefail
PROMPT_FILE="${1:?prompt file}"; MODEL="${2:-thessia-scholar-v3}"; NUM="${3:-1024}"
python3 - "$PROMPT_FILE" "$MODEL" "$NUM" <<'PY'
import json, sys, urllib.request
prompt = open(sys.argv[1]).read()
body = json.dumps({"model": sys.argv[2], "prompt": prompt, "stream": False,
                   "options": {"num_predict": int(sys.argv[3])}}).encode()
req = urllib.request.Request("http://localhost:11434/api/generate", body, {"Content-Type": "application/json"})
d = json.load(urllib.request.urlopen(req, timeout=1800))
print(d["response"].strip())
print(f"\n<!-- thessia: model={sys.argv[2]} tokens={d.get('eval_count')} -->", file=sys.stderr)
PY
