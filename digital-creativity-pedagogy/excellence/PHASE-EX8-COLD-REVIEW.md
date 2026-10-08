# PHASE-EX8 cold review — Lab redesign Wave-1 + exercise cards

| field | value |
| --- | --- |
| **phase** | PHASE-EX8 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-8` |
| **implementation commit** | `a49365795655dd3b88c94a710951352cdea3ff34` |
| **verify log** | `PHASE-EX8-VERIFY-LOG.md` — harness **Exit 1** / `failures: 1` (browser Reveal flake); cold re-run **Exit 0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |
| **PARTIAL** | Content acceptance (labs · cards · ACT adaptations · LAB-SIGNOFF · no invented graded work) met; gate evidence not green in harness log |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Exactly two `lab_exercise` slides on touched decks | Cold Ruby scan of I.1–I.5 `content.json`: each deck `lab_count=2`; I.2 has no `lab-3`; each lab has `method_id` ∈ catalogue, non-empty `practises` → masterclass ids, `timer_seconds` > 0, notes, `portfolio_trace` | Met |
| Cards expose Time/Group/Materials/Steps/Portfolio/Judged by/Source | B2 Lab sections on five EN lessons: each label appears **2/2**; exactly two `### Exercise` headings; Judged-by links resolve to portfolio `#rubric` | Met |
| FINDINGS D1/D2 addressed for touched units | `FINDINGS-2026-10-07.md` D1/D2 closure note; Labs practise Masterclass / feed ACT1–ACT2 craft; forge law two Labs; `LAB-SIGNOFF.md` cites `findings: D1 · D2` | Met (pending green verify) |
| ACT1/ACT2 as adaptations (EX7 F2) | `figurin-digital` / croquis held; `photobash-integration` / `gestalt-composition` / key-visual gap; card **Source:** lines say Classroom adaptation; no invented Abling/Arnheim pages | Met |
| `curation/LAB-SIGNOFF.md` autopilot | File present; `approved_by: autopilot (final review pending)`; ACT table + I.5 selected / I.6–I.9 deferred | Met |
| No invented graded work | Lesson intros + deck notes explicitly refuse second Campus Virtual / off-book graded channel; portfolio traces only; How to Pass stakes unchanged | Met |
| `PHASE-EX8.exit-gate.sh` exits 0 | **Harness verify log Exit 1** (`FAIL: browser layout check`, `Reveal is not defined`). Cold session re-run: `failures: 0` / `EXIT:0`. Standalone `deck-layout.mjs`: `370 slide view(s), 0 failure(s)` | **Unmet in harness log** (see F1) |
| Cold review PASS before land | This document → **FAIL** | Unmet |

---

## Spot checks (cold session)

### Exit gate

**Harness** (`PHASE-EX8-VERIFY-LOG.md`, commit `a493657`):

```text
PASS: … (files, LAB-SIGNOFF, decks, B2 cards, I.2 no lab-3, validator, render, jekyll)
FAIL: browser layout check
… Error: … ReferenceError: Reveal is not defined …
failures: 1
Exit code: 1
Verdict: exit-gate FAILED. Do not promote.
```

**Cold re-run** (same worktree, after harness fail):

```text
$ bash digital-creativity-pedagogy/excellence/PHASE-EX8.exit-gate.sh
PASS: file … PHASE-EX8.md
PASS: file … CANONICAL-METHODS.yml
PASS: lab sign-off file
PASS: lab sign-off approved_by
PASS: lab sign-off cites D1/D2
PASS: deck lab slides (exactly two + method_id + practises)
PASS: lesson B2 exercise cards
PASS: I.2 has no lab-3
PASS: validator --strict green
PASS: render-decks runs
PASS: jekyll build
PASS: browser layout check: deck-layout: 370 slide view(s), 0 failure(s)
----
failures: 0
EXIT:0
```

Implementer `PHASE-EX8-REPORT.md` claims `GATE_EXIT:0` / browser PASS — that claim does **not** match the harness verify transcript (F2).

### Deck labs (exactly two + ACT anchors)

| Deck | lab-1 method | lab-2 method | ACT |
| --- | --- | --- | --- |
| I.1 | fashion-photograph-reading | figurin-digital | ACT1 prep / ACT1 |
| I.2 | croquis-proportion-scaffold | construction-vs-finish-lines | ACT1 |
| I.3 | key-visual-brief-lock | gestalt-composition | ACT2 |
| I.4 | photobash-integration | compositing-before-after-strip | ACT2 |
| I.5 | 2d-to-3d-sequence-sketch | silhouette-from-volume | selected I.5–I.9 |

`practises` targets all resolve to masterclass `slide_id`s on the same deck.

### Source honesty (held/gap)

ACT anchors on cards are **Classroom adaptation** (held/gap). Verified field cites used only where catalogue/`references.yml` already support them (Shinkle on I.1 Lab 1 claim; Hüppauf/Wulf critical frame on I.2 Lab 2; Papahristou on I.5 Lab 1) with steps still labelled classroom adaptation. No Abling/Arnheim page invention.

### No invented graded work

Sample (I.1 Lab 2 notes): “ACT1 craft practice, not a graded Campus Virtual submit.” Lesson B2 lead-ins state Labs feed ACT craft / portfolio index, not a second graded channel. “Not this week” lists refuse invented off-book graded work.

---

## Findings

### F1 — Harness verify log Exit 1 (browser Reveal flake)

| | |
| --- | --- |
| **severity** | P0 |
| **blocks DONE** | yes |
| **evidence** | `PHASE-EX8-VERIFY-LOG.md`: `FAIL: browser layout check` → `ReferenceError: Reveal is not defined` mid `deck-layout.mjs` → `failures: 1` / **Exit code: 1**. Cold re-run of the same gate and a standalone `node scripts/tests/browser/deck-layout.mjs` both exit **0** (`370 slide view(s), 0 failure(s)`). Acceptance requires exit-gate **0** in the harness transcript before land. |
| **fix** | Re-run `cascade-harness.sh verify` for EX8 until `PHASE-EX8-VERIFY-LOG.md` records Exit **0**. No Lab content rewrite required for this flake unless a second fail reproduces on a green Chrome path. Then request cold-review round-2. |

### F2 — Implementer report claims green while harness log is red

| | |
| --- | --- |
| **severity** | P1 |
| **blocks DONE** | no (subsumed by F1) |
| **evidence** | `PHASE-EX8-REPORT.md` lines claim `failures: 0 (GATE_EXIT:0)` and browser PASS; harness verify log for the same commit records Exit **1**. |
| **fix** | After F1 re-verify, align REPORT status with the verify log (or delete the stale green claim). Do not land on report prose alone. |

### F3 — `fashion-photograph-reading` catalogue locator still lacks page pin

| | |
| --- | --- |
| **severity** | P1 |
| **blocks DONE** | no |
| **evidence** | Catalogue: `source_status: verified`, locator = field claim text without `p. 15`. Student card + LAB-SIGNOFF cite `(Shinkle 2008, 15)`. Lesson `PROVENANCE_LINE` already pins Ahmes `printed_page=15` — not an invented page in EX8, but catalogue/EX7 F1 sync remains open. |
| **fix** | Before EX10 hydration: set catalogue `source_locator` to include `p. 15` (from existing Ahmes pin) or demote to held if the pin is disputed. Do not invent a different page. |

### F4 — I.4 browser reports 3 timers (workshop + 2 labs)

| | |
| --- | --- |
| **severity** | P2 |
| **blocks DONE** | no |
| **evidence** | `deck-layout` logs `i-4-effects: … 3 timer(s)`; include has `lab-1`/`lab-2` timers plus `workshop-1` `data-timer="180"`. Still exactly two `lab_exercise` slides. |
| **fix** | None for EX8 acceptance. Optional later: document that workshop timers are expected on I.4. |

---

## Agentic-change failure modes

| Check | Result |
| --- | --- |
| Load modules touched | Deck JSON + catalogue YAML parse under gate Ruby; `validate-decks --strict` PASS on cold re-run |
| Full gate / suite for phase | Harness Exit **1**; cold re-run Exit **0** (browser flake) |
| New checks would fail pre-fix | Pre-EX8 scaffolding gate / missing LAB-SIGNOFF / I.2 third lab would fail new requires + Ruby rules |
| Return shapes / field modes | `lab_exercise` vs masterclass discriminated; held/gap vs verified Sources separated on cards |
| Doc commands as claims | Gate runs `validate-decks`, `render-decks`, jekyll, browser — cold re-run executed them |

Content path closes FINDINGS **D1** / **D2** for I.1–I.5. **F1** blocks PASS/land until harness verify log is green.

Downstream: no cascade amend required for EX9 assumptions (I.6–I.9 Labs deferred is already logged). Do not treat EX8 as DONE while F1 stands.

---

## Verdict

| **verdict** | FAIL |

**P0:** F1 (harness exit-gate Exit 1).  
**P1:** F2 (report vs verify mismatch), F3 (catalogue Shinkle locator sync).  
**P2:** F4 (I.4 workshop timer count).

Eligible for land only after harness re-verify Exit **0** + cold-review round-2 PASS. Reviewer does not mark DONE and does not land.

## Round-2 (orchestrator)

Harness re-verify after Reveal wait harden: **Exit code 0** (370 views / 0 failures).
P1 F3 locator now cites Shinkle p. 15 (held adaptation). F1 flake addressed.
