# Per-unit forge iteration (2–3 cycles)

Use this loop **per unit** before advancing in `DC-CURRICULUM-ORCHESTRATOR.execute.md`.

## Cycle 1 — Forge

1. Load `PROFIELD-UNIT-MAP.md` + `PROFIELD-CRITICAL-MAP.md` + `MASTER-IDEAS.md` + session prompt + both lessons.
2. Map Profield `[ESTABLISHED]` / `[EMERGING]` + critica C1–C3; reject cross-unit leakage.
3. For each claim reaching students: run **BIBLIO-GAP workflow** (`PROVENANCE-LAW.mdc`); write `PROVENANCE_LINE` + `CRITICAL_ROUTING` where applicable.
4. Promote pass-audited profield sentences **verbatim** into public prose; add **Chicago References** for every `public_citation`.
5. Add `## Critical perspective` block; media placeholders; sync session prompt.
6. `npm run build` + verify gates.

## Cycle 2 — Cold reviewer (subagent)

Prompt a **fresh** reviewer with no forge context except:

- `PROVENANCE-LAW.mdc`, `PROFIELD-UNIT-MAP.md`, `PROFIELD-CRITICAL-MAP.md`, unit session prompt, EN+ES lesson diff
- Verdict: `PASS` | `TUNE_FORGER` | `BLOCKED`

**ES parity gate (mandatory):** copy full EN `PROVENANCE_LINE` / `MEDIA_RIGHTS_LINE` block into ES; gate every B2 internal note (`S1/S2`, platform note, learning-outcomes gap) behind `publish_internal_metadata`.

**Session prompt gate:** B3 individual problems must match the lesson page (lesson is authoritative). Studio sprint must match lesson B2 deliverable.

**Teaching language:** forge **EN first** (`docs/lessons/en/…`) as the instructor-facing canonical page; ES is a faithful mirror for guía compliance, not a substitute for EN delivery.

**B2 evidence gate (ES):** never leave `**Evidencia:**` or platform notes outside `publish_internal_metadata` — copy EN pattern (gated block only).

**Critica verbatim gate:** critical opening sentence must match pass-audited profield critica text — C1 for I.4 (Crepax L119); C3 where mapped (e.g. Reddy-Best L265 for I.2). Translate faithfully for ES; do not paraphrase.

## Cycle 3 — Tune (only if `TUNE_FORGER`)

Apply reviewer patches; re-run build. Max **3 cycles** per unit — then mark unit `FORGE_FROZEN` in receipt and move to next unit.

## Wave retrospective (optional — after CD I I.9 or before term start)

Early units (I.1–I.4) forged before later gates hardened may need a **light retrofit pass**, not a full re-forge:

| Check | I.1 likely needs? |
| --- | --- |
| Consolidated single `PROVENANCE_LINE` block (not scattered comments) | Maybe |
| ES full provenance parity | Verify |
| Critica verbatim opening (C1/C3 per map) | Verify Reddy-Best L265 |
| Session B3 = lesson B3 | Done |
| Media placeholders (3 slots) | Already present |
| B2 ES evidence gate | Verify |

Schedule retrospective as **one cold-review sweep** across I.1–I.4 after the wave completes; patch only what fails gates — do not block forward forging.

Receipt path: `digital-creativity-pedagogy/forge/receipts/{unit-id}.md`
