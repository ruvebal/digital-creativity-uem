# PHASE-EX3 cold review — Image/media pipeline (validator + tests)

| field | value |
| --- | --- |
| **phase** | PHASE-EX3 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-3` |
| **implementation commit** | `86f7ecfc935dba2a4632a321824b4a7353dbcfdf` |
| **verify log commit** | `9a9933ff0b51af5e348410772ecac8e18c29ca66` |
| **verify log** | `PHASE-EX3-VERIFY-LOG.md` — Exit code **0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Validator + tests green; gate runs them | Re-ran `node --test scripts/tests/*.test.mjs` → **33 pass / 0 fail**; `node --test scripts/tests/` (gate path) → **33 pass**; gate `check "node --test green"` present | Met |
| `--strict --rights=flag` | Re-ran `node scripts/validate-decks.mjs --strict --rights=flag` → `13 deck file(s), 0 error(s), 389 warning(s)` **exit 0** | Met |
| Rights report path exists | `digital-creativity-pedagogy/excellence/curation/rights-report.json` present; summary `assets=123`, `flagged=123`, `mode=flag` | Met |
| Legacy / outside Wave-1 warn, not hard-fail (A1) | Live Wave-1 decks all `schema_version` missing → warnings only; 5 outside-Wave-1 decks emit `outside Wave-1 … warns only`; `--rights=block` on live tree also exit 0 (all legacy). Fixture test `legacy outside Wave-1` exit 0. Forced `schema_version: 2` on i-1 → **165 errors** (legacy path is load-bearing) | Met |
| Orphans not deleted | `profield-cache`: **79** files remain; **20** orphan WARNs (`kept until EX4`); no `unlink`/`rm` of cache in `validate-decks.mjs` (only writes rights-report) | Met |
| Forge pointers + schema note | `STUDENT-SLIDESHOW-FORGE.mdc` names `schema_version` 2 + `validate:decks`; `dc-unit-forge.mdc` points at validator; `SCHEMA-VERSION-WAVE1.md` present | Met |
| `PHASE-EX3.exit-gate.sh` exits 0 | VERIFY-LOG exit 0; cold re-run → `failures: 0` | Met |
| Cold review PASS before land | This document | Met |

---

## Spot checks (cold session)

### Tests (anti-vacuous)

```text
$ node --test scripts/tests/*.test.mjs
# tests 33  # pass 33  # fail 0  EXIT:0

$ MEDIA_RULES_IMPL=legacy node --test scripts/tests/media-rules.test.mjs
# tests 16  # pass 1  # fail 15  EXIT:1
```

Legacy mode fails 15/16 — the suite would not have been green against pre-EX3 rank-dealing / strip-tag “rights”.

### Validator + orphans

```text
$ node scripts/validate-decks.mjs --strict --rights=flag
validate-decks: 13 deck file(s), 0 error(s), 389 warning(s) [strict; rights=flag]
EXIT:0
# ERROR lines: 0
# orphan profield-cache WARNs: 20
# orphan deck-media ERRORs: 0
# outside Wave-1 WARNs: 5
```

### Modules load

`scripts/lib/media-rules.mjs` and `scripts/lib/deck-caption.mjs` import cleanly. `validate-decks.mjs` is a CLI entrypoint (top-level run on import — expected).

### FINDINGS B2 / B3

Tooling layer closed as claimed: orphan/rights/reuse/block/flag covered in tests; CT-grade validator + rights-report path present; caches not deleted. Slide-bound curation remains **EX4** (report + SCHEMA note + DECISIONS-LOG agree). **B1** correctly left open for EX5/EX11.

---

## Findings

### F1 — `captionHtml` (A12/F8) has no unit test

- **Severity:** P2  
- **Blocks DONE:** no  
- **Evidence:** `scripts/lib/deck-caption.mjs` implements Public-domain → “Rights under review” for `rights_status === 'flagged'`; no `scripts/tests/*` asserts that path (validator wires it, fixtures do not exercise flagged PD captions).  
- **Fix:** Optional one-liner test in EX4/EX5 when the full caption renderer lands; not required for EX3 acceptance.

### F2 — Downstream: `rehydrate-student-media.mjs` still rank-deals

- **Severity:** P1 (downstream, not EX3 gate)  
- **Blocks DONE:** no  
- **Evidence:** Implementer report + DECISIONS-LOG: EX3 deliberately did not migrate decks or switch rehydrate to `bindSlides`. Live decks remain legacy (`schema_version` missing).  
- **Fix:** EX4 must migrate Wave-1 to `schema_version: 2`, populate `autopilot-assets.json`, and retire `rankCursor` dealing — otherwise the first v2 migration will hard-fail under `--strict` (cold session: forced v2 on i-1 → 165 errors). Amend EX4 runbook if it still assumes rehydrate already binds by `asset_id`.

No P0 findings. Zero issues that invalidate EX3 Acceptance.

---

## Verdict

| **verdict** | PASS |

Eligible for product-owner promotion to DONE / land on the excellence integration branch after triage of F2 as an EX4 prerequisite (not an EX3 rework).
