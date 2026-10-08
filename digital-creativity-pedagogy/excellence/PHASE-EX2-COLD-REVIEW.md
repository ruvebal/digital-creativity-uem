# PHASE-EX2 cold review — Publication firewall (round 2)

| field | value |
| --- | --- |
| **phase** | PHASE-EX2 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-2` |
| **fix commit** | `d61156ba871a9b5285a1dcb8ecd3cf16a4a63ee6` |
| **verify log commit** | `1c724194cef60b65f66d28f076a0a2c19fdcfa06` (log only; gate ran on fix commit) |
| **verify log** | `PHASE-EX2-VERIFY-LOG.md` — Exit code **0** |
| **reviewed** | 2026-10-07 (round 2 after P0 fix) |
| **verdict** | PASS |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

Prior FAIL (`F1`/`F2`): ES Wave-1 footers + EN-only gate. Re-checked after `d61156b`.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Safety script exit 0 on built `_site` | Re-ran `node scripts/verify-publication-safety.mjs` → passed; `Fecha de forja` present in forbidden list | Met |
| FINDINGS C1/E1 Wave-1; CD II/NM firewall-only | EN+ES CD I one-sentence footers; ES CD II same; PROVENANCE gated; FINDINGS says “pending cold-review PASS” | Met (NM residual → P1) |
| Gate proves leak fixture fails | VERIFY-LOG + re-run Ahmes fixture; also confirmed `Fecha de forja` fixture fails safety | Met |
| `PHASE-EX2.exit-gate.sh` exits 0 | VERIFY-LOG exit 0; ES asserts present in gate script | Met |
| Cold review PASS before land | This document (round 2) | Met |

---

## Round-2 spot checks

### ES i-1 public AI section

`docs/lessons/es/creacion-digital-i/i-1-imagenes-digitales/index.md` after Liquid strip:

- Public footer: one-sentence form + `/ai-declaration/` link.
- Public: no `Fecha de forja`, no `vía MCP`, no `contexto RAG`, no `Ahmes`, no `lesson-scribe`.
- Stamp moved into gated comment as `forge_date: 2026-09-22 · …` (not the Spanish phrase; still non-publishable with switch false).

All nine ES CD I + six ES CD II publicSources: `bad=0` for Fecha/MCP/RAG/Ahmes/lesson-scribe.

### Exit-gate ES checks (re-run absent helpers)

```text
PASS: no Fecha de forja in CD I ES public source
PASS: no MCP/RAG vault footer in CD I ES public source
PASS: no Fecha de forja in built CD I ES HTML
PASS: no Ahmes in built CD I ES HTML
```

Built `_site/lessons/es/creacion-digital-i`: no `Fecha de forja` / `vía MCP` / `Ahmes` hits.

### Safety / probe

- `scripts/verify-publication-safety.mjs` forbids `\bFecha de forja\b`.
- Probe `wave1.lesson_infra_vocab_files = 0`.
- EN i-1: PROVENANCE only in raw gated blocks; public clean.

### Prior P0 disposition

| Prior | Status |
| --- | --- |
| F1 ES Wave-1 footers / Fecha | **Closed** — rewritten + gated stamp |
| F2 EN-only exit gate | **Closed** — ES source + built HTML asserts + Fecha pattern |
| F5 FINDINGS “closed” | **Closed** — wording is “pending cold-review PASS” |

---

## Remaining findings

### F3 — NM ES u2 AI footer still exposes ledger path tokens

- **Severity:** P1  
- **Blocks DONE:** no  
- **Evidence:** Editorial note line scrubbed (`20260925T200000Z` → “ledger docente del curso”), but AI-assisted authorship paragraph still public-contains `` `fashion-exemplary-social-campaigns` · `20260925T200000Z` `` and “unit forge”.  
- **Fix:** Same one-sentence / redact treatment as CD lessons (firewall-only). Optional follow-up before EX11 audit.

### F4 — Nested duplicate Liquid `if` on NM ES scaffolds

- **Severity:** P2  
- **Blocks DONE:** no  
- **Evidence:** `u4` / `u5` / `u6` still `max_depth=2`. Stripper still correct.  
- **Fix:** Single `if`/`endif` pair.

---

## What holds

- DC-tuned safety patterns + ai-declaration allowlist + Ahmes fail-closed fixture.  
- Bilingual Wave-1 (+ ES CD II firewall) one-sentence AI footers; EN provenance gated.  
- Exit gate bilingual; `absent` under `set -e` intact.  
- Probe infra vocab 0; built EN/ES CD I HTML free of Ahmes / Fecha de forja.

---

## Verdict summary

| **verdict** | PASS |
| --- | --- |

No open P0. Residual **P1:** NM ES u2 ledger path tokens in AI footer (F3). **P2:** nested Liquid if (F4).

## Round-3 note (orchestrator)

P1 closed: NM ES u1/u2/u3 long English AI footers replaced with one-sentence ES form; path tokens removed. Re-verified at HEAD after scrub.
