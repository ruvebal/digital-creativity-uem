#!/usr/bin/env bash
# Plain Ollama generate (Qwen structure/code). Usage: local/ollama-generate.sh <prompt-file> [model]
set -euo pipefail
PROMPT_FILE="${1:?prompt file}"; MODEL="${2:-qwen2.5:32b-instruct}"
python3 - "$PROMPT_FILE" "$MODEL" <<'PY'
import json, sys, urllib.request
prompt = open(sys.argv[1]).read()
body = json.dumps({"model": sys.argv[2], "prompt": prompt, "stream": False,
                   "options": {"num_predict": 2048, "temperature": 0.2}}).encode()
req = urllib.request.Request("http://localhost:11434/api/generate", body, {"Content-Type": "application/json"})
d = json.load(urllib.request.urlopen(req, timeout=1800))
print(d["response"].strip())
PY
