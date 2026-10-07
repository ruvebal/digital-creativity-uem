# PHASE-EX2 cold review — Publication firewall

| field | value |
| --- | --- |
| **phase** | PHASE-EX2 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-2` |
| **commit** | `400ce62426055f5f70a41503ccc28d0402b01f88` |
| **verify log** | `PHASE-EX2-VERIFY-LOG.md` — Exit code **0** (harness) |
| **reviewed** | 2026-10-07 |
| **verdict** | FAIL |

Reviewer did not implement this phase. Status was not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Safety script exit 0 on built `_site` | Re-ran `node scripts/verify-publication-safety.mjs` → `Publication safety passed`; exit 0 | Met (EN-centric patterns) |
| FINDINGS C1/E1 for Wave-1; CD II/NM firewall-only | EN CD I: PROVENANCE / Ahmes / lesson-scribe gated; one-sentence AI footers. ES CD I: only renamed `lesson-scribe` → `local drafting tools`; long MCP/RAG/vault footers + `Fecha de forja` still public. NM/CD II: EN scrubbed; ES incomplete | **Not met (bilingual)** |
| Gate proves known leak fails fixture | Exit gate + re-run: fixture `_site/__excellence_ex2_leak_fixture.html` with `Ahmes` → safety fails; removed → passes | Met |
| `PHASE-EX2.exit-gate.sh` exits 0 | VERIFY-LOG exit 0; checks are EN CD I + script-pattern presence | Met as written; **blind to ES** |
| Cold review PASS before land | This document | **FAIL** |

---

## Spot checks (commands + output)

### Wave-1 EN — PROVENANCE only behind Liquid gate

`docs/lessons/en/digital-creativity-i/{i-1,i-5,i-9}/index.md`: all `PROVENANCE_LINE` / `Ahmes` / `ahmes-library` / `lesson-scribe` hits sit inside `{% if site.publication.publish_internal_metadata %}…{% endif %}`. Public AI footer is one sentence + `/ai-declaration/`.

`_config.yml`: `publish_internal_metadata: false`.

### Built `_site` — CD I EN clean

```text
rg '\bAhmes\b|\bAthanor\b|\blesson-scribe\b|\bThessia\b|\bProfield\b|\bahmes-library\b' \
  _site/lessons/en/digital-creativity-i
# → no hits

rg '\bAhmes\b' _site --glob '!**/ai-declaration/**'
# → no hits
```

### Probe

```text
lesson_infra_vocab_files= 0
```

(`excellence-probe.mjs` strips the same Liquid switch before counting.)

### Pre-fix would have failed new EN patterns

On `HEAD~1` `i-1-digital-images` publicSource: `Forge date=True`, `lesson-scribe=True`. After EX2: both absent from public EN source. New patterns are not vacuous for EN.

### ES Wave-1 still student-visible (P0)

```text
rg 'Fecha de forja' _site/lessons/es/creacion-digital-i
# hits on all 9 units, e.g.
# _site/.../i-1-imagenes-digitales/index.html:578:
#   <em>Fecha de forja: 2026-09-22 · … harness: local drafting tools v0.1 …</em>
```

Public ES footers still name MCP / RAG / vault curricular (same register EN removed).

`Forge date` regex in `verify-publication-safety.mjs` does **not** match `Fecha de forja`. Exit gate `absent … docs/lessons/en/digital-creativity-i` never looks at ES.

### Safety / fixture re-check

```text
Publication safety passed: …
OK: fixture failed as expected
… __excellence_ex2_leak_fixture.html: internal corpus name
OK: clean after fixture
```

### `absent` under `set -e`

`gates/common.sh`: `hits="$(grep … | head -5 || true)"` — smoke `absent` with no match → `PASS` without aborting.

---

## Findings

### F1 — Wave-1 ES publication surface incomplete (blocks DONE)

- **Severity:** P0  
- **Blocks DONE:** yes  
- **Evidence:** All nine `docs/lessons/es/creacion-digital-i/*/index.md` still publish `*Fecha de forja: …*` and multi-paragraph AI footers (MCP, RAG, vault curricular). Diff only swapped `` `lesson-scribe` `` → `local drafting tools`. EN Wave-1 + EN CD II got the one-sentence footer. Built `_site` mirrors ES sources.  
- **Why it matters:** Phase goal / deliverable 3 require removing infra vocabulary and one-sentence AI footers on Wave-1. CD I is bilingual (probe: `lessons_en_cd_i` / `lessons_es_cd_i`). C1/E1 are not closed for the Spanish student surface.  
- **Fix:** Apply the same one-sentence AI footer + move forge/harness stamps into `{% if site.publication.publish_internal_metadata %}` for all ES CD I (and preferably ES CD II firewall scrub). Add `Fecha de forja` (and ideally MCP/RAG authoring-prose) to `forbidden` in `verify-publication-safety.mjs`. Extend exit-gate `absent` / probe coverage to `docs/lessons/es/creacion-digital-i` and `_site/lessons/es/creacion-digital-i`.

### F2 — Exit gate / safety EN-biased (blocks DONE with F1)

- **Severity:** P0  
- **Blocks DONE:** yes (same root cause as F1)  
- **Evidence:** Gate checks `Forge date:.*lesson-scribe` and Ahmes only under EN paths; safety `Forge date` misses Spanish stamp; harness VERIFY-LOG can be green while ES HTML still leaks authoring stamps.  
- **Fix:** Same as F1 — bilingual patterns + bilingual gate assertions. Do not treat EN-only green as Wave-1 closed.

### F3 — NM ES firewall scrub incomplete

- **Severity:** P1  
- **Blocks DONE:** no (if F1/F2 fixed; still required before claiming full NM firewall)  
- **Evidence:** `docs/lessons/es/nuevos-medios-moda/u2-estrategias-comunicacion-digital/index.md` public AI footer still cites `` `fashion-exemplary-social-campaigns` · `20260925T200000Z` `` and “unit forge”; line 248 still exposes ledger token `20260925T200000Z`.  
- **Fix:** Redact path/run tokens to student-facing wording (as EN NM / `tracks.yml` campaign_ledger redaction already did).

### F4 — Nested duplicate Liquid `if` on NM ES scaffolds

- **Severity:** P2  
- **Blocks DONE:** no  
- **Evidence:** `u4` / `u5` / `u6` open `publish_internal_metadata` twice then close twice (e.g. `u6` lines 17–25). Depth stripper still hides content; Jekyll with flag false is OK.  
- **Fix:** Collapse to a single `if`/`endif` pair.

### F5 — FINDINGS “EX2 closed” before cold review

- **Severity:** P1 (process)  
- **Blocks DONE:** no  
- **Evidence:** `FINDINGS-2026-10-07.md` Closure notes claim C1/E1 “EX2 closed 2026-10-07” while phase must await cold-review PASS.  
- **Fix:** Soften to “implemented; pending cold review” until land, or amend after PASS.

---

## What did work (recorded)

- DC-tuned forbidden list (lesson-scribe, Profield prose, UDIT, web-atelier, Thessia, ahmes-library) + ai-declaration allowlist.  
- EN Wave-1 provenance gated; probe infra count 0; built EN CD I HTML free of Ahmes/Athanor.  
- Ahmes fixture fail-closed; second `publication_safety_ok` after cleanup.  
- `absent` helper fixed for `set -e` / pipefail.  
- UDIT stripped from `archive_covers.manifest.json`; CSS/JS/track ledger Profield/UDIT scrub consistent with firewall-only scope.  
- Incidental media description scrub in deck `content.json` is firewall-aligned, not redesign.

---

## Downstream

If F1/F2 stand, do **not** treat C1/E1 as closed in EX11 closing audit until ES Wave-1 matches EN. No other phase file needs assumption amendments beyond FINDINGS closure wording (F5).

---

## Verdict summary

| **verdict** | FAIL |
| --- | --- |

**P0:** F1, F2 — ES Wave-1 still publishes forge stamps + infra AI prose; EN-only gate/safety blind spot.  
**P1:** F3 (NM ES tokens), F5 (premature FINDINGS closed).  
**P2:** F4 (nested Liquid if).
