# PHASE-EX6 Report

| Field | Value |
| --- | --- |
| **status** | VERIFYING (PARTIAL allowed under AUTOPILOT §2 EX6). Exit gate **failures: 0**. Do **not** mark DONE — harness verify + cold review next. |
| **started_at / finished_at** | 2026-10-07 / 2026-10-07 |
| **branch / worktree** | `cascade/excellence-6` · `digital-creativity-uem-integration-excellence-6` (`.cascade-lane` = `excellence`) |
| **mode** | AUTOPILOT. Vault / open access only; else `gap`. Critical layer Steimberg / Werhane / Munari recorded as **gap** (held or missing; no invented student cites). |

## Outcome

### Manifest stats

| Metric | Count |
| --- | --- |
| `research-manifest.yml` works | **46** |
| `verified` | **10** |
| `gap` | **36** |
| `docs/_data/references.yml` keys | **10** (1:1 with verified) |

Verified keys: `aldahoul-2025`, `campinho-2025`, `coats-2026`, `eckersall-2017`, `huppauf-wulf-2009`, `kandinsky-2012`, `papahristou-2024`, `roivainen-2025`, `rubin-2023`, `shinkle-2008`.

### Single bibliography

- New `docs/_data/references.yml` + `docs/_includes/references.html` (CT pattern).
- Wave-1 EN lessons I.1–I.9 + ML-FIA: front-matter `references: [...]`, hand-written `<span id="ref-…">` removed, `{% include references.html %}`.
- ES twin CD I lessons: same include + keys (bilingual References → Referencias).
- Gap works no longer in student References lists; `#ref-` links only to verified keys.

### Critical layer (D2 / FINDINGS C5)

| Key | Vault | Status |
| --- | --- | --- |
| `steimberg-2013` | coat `d639c32d` | **gap** (held; claim deferred to EX10 brief) |
| `steimberg-1993` | not held | **gap** |
| `werhane-2026` | coat `96302b7e` | **gap** (held; claim deferred to EX10) |
| `munari-design-method` | Circle / anthology only | **gap** (wrong works for method/manifest pin) |

### FINDINGS cited

- **C2:** single `references.yml` + `research-manifest.yml` landed (Wave-1).
- **C3:** gap/procurement table in manifest `procurement_priority` (PARTIAL).
- **C5:** Steimberg / Werhane / Munari present as gap entries (not invented).

## Gaps / procurement (summary)

See `research-manifest.yml` → `procurement_priority`.

1. **Held — place claim (EX9/EX10):** Steimberg 2013, Werhane 2026, Rizzi 2025 (`167816a4`), Anwar 2025 (`0598ec0e`), Norman 2013.
2. **OA candidates:** Curcic 2024, Moritz & Youn 2022, Balasubramanian 2026.
3. **Library / purchase:** Albers 2013, Abling, Entwistle 2015, Shaw 2015, Manovich 2013, Munari *Design as Art* (or authorised ES), Rocamora 2017, Reddy-Best 2018.

Units I.4 / I.8 / I.9 currently have **empty** student References (all body research pins still gap) — honest PARTIAL, not invented cites.

## What I ran (real)

- DevIAC MCP `search_knowledge` (`profield-digital-creativity`, `profield-creativity-techniques`) for discovery; Ahmes coats checked on disk; Kandinsky p.9 node `017a3864-6f07-5c36-8991-bd0350aef4fd` resolved from extraction.db.
- `bash digital-creativity-pedagogy/excellence/PHASE-EX6.exit-gate.sh` → **EXIT 0**, `failures: 0` (manifest/refs/citations; no hand `id="ref-`; jekyll build; publication safety; built `#ref-` anchors).

## Files changed

- `digital-creativity-pedagogy/excellence/research-manifest.yml` (new)
- `digital-creativity-pedagogy/excellence/PHASE-EX6.exit-gate.sh` (hardened)
- `docs/_data/references.yml` (new) · `docs/_includes/references.html` (new)
- `docs/lessons/en/digital-creativity-i/i-{1..9}-*/index.md`
- `docs/lessons/en/master-lectures/fashion-image-analysis/index.md`
- `docs/lessons/es/creacion-digital-i/i-*/index.md`
- This report · DECISIONS-LOG · PHASE-EX6 status · FINDINGS closure note · INDEX gate cell

## Uncertain / for cold reviewer

- Albers / Curcic / Entwistle still *named* in some EN body prose as open procurement without `#ref-` — intentional; confirm tone is not read as a verified Chicago pin.
- Kandinsky Dover page_index 9 treated as printed folio for this edition.
- ES lessons may still name gap authors in body without EN parity polish (EX9).
- I.4 / I.8 / I.9 empty References lists are PARTIAL by design until procurement.

## Resume point

1. `cascade-harness.sh verify` → `PHASE-EX6-VERIFY-LOG.md`
2. Fresh cold review (sample 5 verified cites: Shinkle 15, Roivainen 8, Coats 8, Papahristou 5, Kandinsky 9)
3. Do **not** open EX7 until EX6 triaged; PARTIAL may sequence under resume rule

Do not mark DONE.
