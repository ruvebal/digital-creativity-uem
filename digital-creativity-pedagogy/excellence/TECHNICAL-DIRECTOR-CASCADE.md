# Technical director — DC Excellence cascade (EX0–EX11)

**Status:** READY. Run phases **in order**. Each `PHASE-EXn.md` is a
self-contained paste prompt with a runnable `PHASE-EXn.exit-gate.sh`.

**Mode: AUTOPILOT** (professor decision, 2026-10-07). [AUTOPILOT.md](AUTOPILOT.md)
overrides every "Human gate" with a pre-registered policy;
[gitflow.sh](gitflow.sh) lands on `excellence/integration`, never on `main`.

**Sibling pattern:** Creativity Techniques Excellence (COMPLETE) — clone the
*discipline*, not the CONTENIDOS.

## Amendment A1 (launch, 2026-10-07) — Wave-1 scope

- **Owns:** Creación Digital I lessons/decks **I.1–I.9**, fashion-image-analysis
  special (master lecture), shared evaluation / How-to-Pass / session rhythm
  surfaces that name D1–D5, and forge rules those surfaces depend on.
- **Firewall-only** (EX2): CD II (`ii-*`), Nuevos Medios (`u-*` NM), any
  page that leaks internal terms — remove leaks only; no content redesign.
- **Out of scope for Labs/images/assessment depth:** full CD II and NM
  excellence pass — EX11 seeds `NEXT-CASCADE-CD-II.md`.
- **Coordination:** [COORDINATION-SANDRA.md](COORDINATION-SANDRA.md) is
  load-bearing; D2 Transposition ≡ ACT3 cartel.
- **Sync:** `gitflow.sh start` merges committed `main` into integration;
  conflict → stop (CT A8 protocol if professor later ratifies a sync path).

## Master paste (fresh session)

```text
You are the orchestrator for Digital Creativity Excellence (EX0–EX11).

Read first, in order:
1. digital-creativity-pedagogy/excellence/INDEX.md
2. AUTOPILOT.md
3. TECHNICAL-DIRECTOR-CASCADE.md (this file)
4. FINDINGS-2026-10-07.md
5. COORDINATION-SANDRA.md
6. PROFIELD-AND-INFRA.md
7. LOCAL-EXECUTION.md
8. The next READY PHASE-EXn.md

Hard constraints:
- No cloud LLMs for student text, citations, or rights adjudication.
  Facts: Ahmes nodes / Athanor discovery → cite Ahmes only.
  Local Ollama: Qwen structure/code; Thessia voice-only on grounded drafts;
  vision only for EX4 brief-fit with think:false when needed.
- Never push or merge to main; only excellence/integration + phase branches.
- Never start measurement / collect student data.
- Never invent media; never claim DPO/exhibition clearance.
- Do not name UDIT or sibling institutions on student-facing pages.
- Do not weaken an exit gate without a cold-review finding titled
  "gate amendment".
- Execute the next incomplete phase only, in order.

Out of scope: VTON; rewriting Sandra’s Campus Virtual plan; forging CD II/NM
to Wave-1 depth; hand-editing Profield acceptance DB.

When AUTOPILOT: follow AUTOPILOT.md §2–§4. Log decisions. Build FINAL-REVIEW.md
as you go. Prefer cascade-phase-executor / cascade-cold-reviewer subagents.
```

## Resume rule

Branch on the **first word** of the INDEX Gate cell and on
`PHASE-EXn-REPORT.md` status when present:

| Status | Action |
| --- | --- |
| `READY` | `gitflow.sh start` → implement |
| `BLOCKED` | Do nothing until prior DONE |
| `IN_PROGRESS` | Resume implementer in the open worktree; do not open a second |
| `VERIFYING` | Run / re-run harness verify; do not mark DONE |
| `COLD_REVIEW` | Launch fresh cold reviewer; triage findings |
| `DONE` | Skip; open next READY |
| `PARTIAL` | Allowed only where AUTOPILOT says so (EX6 gaps); treat as DONE for sequencing if Acceptance met |
| Job still running (Ollama) | Wait; do not kill; do not start another heavy model |

## Closing protocol

```text
BLOCKED → READY → IN_PROGRESS → VERIFYING → COLD_REVIEW → DONE
```

Implementer never self-certifies DONE. Cold reviewer files
`PHASE-EXn-COLD-REVIEW.md`. Amend cascade in the same commit as surprises.

## Programme (summary)

See INDEX.md table. Deliverable spine:

| EX | Spine |
| -- | ----- |
| 0 | Probe + baseline JSON + DECISION weights + Sandra lock recorded |
| 1 | Publish contract: guía buckets, ACT↔D map, How to Pass, EN/ES critical fixes |
| 2 | Site-wide firewall |
| 3 | Validator + media rules + tests |
| 4 | Curate Wave-1 deck images + rights report |
| 5 | Renderer + browser layout gate |
| 6 | `references.yml` + research-manifest from broadcast corpora |
| 7 | Fashion-craft method catalogue |
| 8 | Labs I.1–I.4 (ACT1/ACT2) + selected later I.* Labs |
| 9 | Lesson structure / exemplars / figures Wave-1 |
| 10 | Practice quizzes + transposition brief lock + consent drafts |
| 11 | Closing audit + CD II / NM seed |

## Human gates (overridden by AUTOPILOT)

| Phase | Human gate (if autopilot off) |
| --- | --- |
| EX0 | Confirm weights + Sandra lock |
| EX4 | Approve images |
| EX8 | Sign off Labs |
| EX10 | Approve bank + consent |
| Release | Merge to main |

## Hard constraints (repeat)

1. Local-only AI for generation touching student IP surfaces.
2. Publication firewall fail-closed.
3. Guia hours / weights / CONTENIDOS are contracts — no FE invention.
4. D2 ≡ ACT3.
5. Git: integration only until release.
