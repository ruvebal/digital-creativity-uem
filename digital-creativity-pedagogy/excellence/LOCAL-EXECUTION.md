# Local-first execution — DC Excellence

**Goal:** maximise Ollama / Ahmes / Athanor / DevIAC; keep cloud tokens to
orchestration and cold review only.

## Verified live on 2026-10-07 (Tanit)

| Component | State | How checked |
| --- | --- | --- |
| Ollama native Metal | up · 11 models | `curl localhost:11434/api/tags` |
| `qwen2.5-coder:32b`, `qwen2.5:32b-instruct`, `qwen3.8:27b`, `qwen2.5:72b-instruct-q4_K_M` | installed | tags list |
| `thessia-scholar-v3`, `thessia-coder-v3`, `thessia-sentinel-v3` | installed | tags list |
| `llama3.2-vision` | listed (may fail load — CT found `mllama` issues; prefer `qwen3.8:27b` think:false for EX4) | tags + CT A7 lesson |
| DevIAC / Postgres / MCP | assume studio health before EX6 | `cd ~/src/deviac && make health` |
| Ahmes CLI | `~/src/ahmes` | `--help` |
| Profield DC runs | present on disk | `PROFIELD-AND-INFRA.md` §1 |

**Fact rule (from CT):** Thessia fabricates. Voice only on grounded drafts.

## Rules

1. Facts from Athanor discovery → **Ahmes cite**, never model memory.
2. Thessia rewrites grounded drafts; discard any new name/number/quote.
3. Qwen for structure/code; `qwen3.8:27b` only with `think:false` + plain delimiters (no JSON mode trap).
4. One heavy model at a time; check `ps` before load.
5. Gates are mechanical — never trust model self-report.

## Workload map

| Phase | Local (Ollama · Ahmes · Athanor · DevIAC) | Cloud (Claude / Cursor) |
| --- | --- | --- |
| EX0 | Probe script; Qwen-coder drafts probe | Orchestration; cold review |
| EX1 | Qwen drafts contract diffs from guía + Sandra PDF text | Orchestration; cold review |
| EX2 | Qwen rewrites leak sentences; safety script local | Cold review |
| EX3–EX5 | Coder for validator/renderer/tests; browser check local | Cold review |
| EX4 | Vision brief-fit local; rights recording scripts | Cold review |
| EX6 | Athanor search + Ahmes query; Qwen classifies gaps | Cold review |
| EX7 | Qwen catalogue classification from retrieved sources | Cold review |
| EX8–EX9 | Qwen Lab cards / exemplars from retrieved + Sandra rubrics | Cold review |
| EX10 | Qwen question drafts from lesson refs only | Cold review |
| EX11 | Probe + audit tables | Cold review |

## `local/` helpers (EX0 creates)

Mirror CT Excellence:

- `local/athanor.sh` — search with `.env` exported
- `local/thessia.sh` — HTTP generate, scholar voice
- `local/ollama-generate.sh` — plain generate wrapper

Do not commit secrets. Do not call cloud embeddings.
