<!--
DC EXCELLENCE — gated cascade that lifts Creación Digital I–II (UEM) to the
same excellence bar as Creativity Techniques EX0–EX11, coordinated with the
Spanish cohort Plan de trabajo (Sandra Jiménez Duarte, 2026–27).
Author: Rubén Vega Balbás, PhD · 2026-10-07
Departing point: creativity-techniques-uem/…/excellence (COMPLETE).
-->

# Digital Creativity — Excellence cascade (EX0–EX11)

**Status:** READY (pack authored; not started). Same git strategy as CT
Excellence: land on `excellence/integration`, never on `main` until
professor release.
**Author:** Rubén Vega Balbás, PhD · 2026-10-07
**Readers:** the professor (one final review); implementing and
cold-review agents (orchestrator, then one phase file at a time).

## Product claim

Ship a student-facing Digital Creativity site whose contract, publication
firewall, media rights, research grounding, Labs, and assessment layer meet
the CT Excellence bar — while **locking D2 Transposition to the same
substance as Sandra’s ACT3 Transposición** (cartel from another language)
so the bilingual cohort stays coordinated.

## Engineering claim

Phased, harness-gated, cold-reviewed autopilot cascade (`gitflow.sh` +
`cascade-harness.sh` + local Ollama / Ahmes / Athanor / DevIAC), with a live
FINDINGS baseline and a closing probe that proves every FINDINGS ID closed
or deferred with a decision record.

## How to read this pack

| Face | File | Question it answers |
| ---- | ---- | ------------------- |
| Evidence | [FINDINGS-2026-10-07.md](FINDINGS-2026-10-07.md) | What was checked live, with IDs (A1…E7) every phase cites |
| Coordination | [COORDINATION-SANDRA.md](COORDINATION-SANDRA.md) | Plan de trabajo ACT1–4 ↔ D1–D5 / CONTENIDOS map |
| Profield + infra | [PROFIELD-AND-INFRA.md](PROFIELD-AND-INFRA.md) | Which runs, vaults, bibliographies, MCP scopes to use |
| Technical director | [TECHNICAL-DIRECTOR-CASCADE.md](TECHNICAL-DIRECTOR-CASCADE.md) | Order, master paste, hard constraints, resume, closing |
| Autopilot policy | [AUTOPILOT.md](AUTOPILOT.md) | Pre-registered decisions, loop, stop rules, final packet |
| Local execution | [LOCAL-EXECUTION.md](LOCAL-EXECUTION.md) + `local/` | Verified local stack, model roles, workload map |
| Git flow | [gitflow.sh](gitflow.sh) | Integration branch, landing, tags, rollback, release |
| Final review | `FINAL-REVIEW.md` (built during the run) | What the professor reads once at the end |
| Shared gate helpers | [gates/common.sh](gates/common.sh) | Build + pass/fail helpers sourced by every exit gate |
| Operator subagents | `~/src/.cursor/agents/cascade-phase-executor.md`, `cascade-cold-reviewer.md` | Implement one phase → VERIFYING; cold-review it |

Closing: each phase → VERIFYING (`cascade-harness.sh verify`) →
`PHASE-EXn-COLD-REVIEW.md` → amend if needed → `PHASE-EXn-REPORT.md` → DONE.

## Programme

Only the **first word** of the Gate cell is parsed by `cascade-harness.sh`.

| Step | File | Deliverable | Gate |
| ---- | ---- | ----------- | ---- |
| 0 | [PHASE-EX0.md](PHASE-EX0.md) | Live probe + baseline + guía weights + Sandra coordination lock | DONE |
| 1 | [PHASE-EX1.md](PHASE-EX1.md) | Contract and factual hotfix (weights, How to Pass, EN/ES, ACT↔D map) | READY (EX0 DONE) |
| 2 | [PHASE-EX2.md](PHASE-EX2.md) | Publication firewall (leak terms, AI footers, no sibling-institution names) | BLOCKED (EX1 DONE) |
| 3 | [PHASE-EX3.md](PHASE-EX3.md) | Image/media pipeline rules + tests + deck validator | BLOCKED (EX2 DONE) |
| 4 | [PHASE-EX4.md](PHASE-EX4.md) | Slide-bound image curation with rights checks (Wave-1 decks) | BLOCKED (EX3 DONE) |
| 5 | [PHASE-EX5.md](PHASE-EX5.md) | Deck renderer: pre-render, alt, captions, notes, layouts, browser check | BLOCKED (EX4 DONE) |
| 6 | [PHASE-EX6.md](PHASE-EX6.md) | Research grounding + single bibliography (broadcast Ahmes / Athanor) | BLOCKED (EX5 DONE) |
| 7 | [PHASE-EX7.md](PHASE-EX7.md) | Canonical fashion-craft method catalogue (studio methods, not CT techniques) | BLOCKED (EX6 DONE) |
| 8 | [PHASE-EX8.md](PHASE-EX8.md) | Lab redesign Wave-1 units + exercise cards aligned to ACT1–2 | BLOCKED (EX7 DONE) |
| 9 | [PHASE-EX9.md](PHASE-EX9.md) | Lesson structure, exemplars, lesson images (Wave-1) | BLOCKED (EX8 DONE) |
| 10 | [PHASE-EX10.md](PHASE-EX10.md) | Assessment: practice quizzes, D2=ACT3 lock, consent drafts | BLOCKED (EX9 DONE) |
| 11 | [PHASE-EX11.md](PHASE-EX11.md) | Closing audit vs EX0 baseline + CD II / NM handoff seed | BLOCKED (EX10 DONE) |

## Live snapshot (2026-10-07)

| Fact | Value | Where checked |
| ---- | ----- | -------------- |
| Official CD I/II weights | 55 / 15 / 20 / 10 | `cv/guides/1-creacion-digital-i.json`, `3-creacion-digital-ii.json` |
| Sandra Plan de trabajo ACT weights | 4 × 11.2% continuous (ACT1–4) | `cv/sources/Plan_de_trabajo_2026-27_Creacion_Digital_I-Sandra_Jimenez.pdf` |
| Teaching languages | ES (Sandra) · EN/ES (this site) | operator, 2026-10-07 |
| Student lessons EN / ES | 26 / 24 `index.md` | `docs/lessons/{en,es}` |
| Deck `content.json` (all tracks) | 13 | `docs/tracks/**/content.json` |
| Wave-1 DCI decks | 6 | `docs/tracks/en/uem/2627-dci/**/content.json` (probe) |
| `profield-cache` files / `.php` | 79 / **0** | `docs/assets/images/profield-cache/` |
| CD I EN lessons with infra vocab | **9 / 9** | `evidence/baseline-EX0.json` (Ahmes/Athanor/profield/…) |
| Ollama (Tanit) | 11 models incl. Thessia + Qwen + vision | `curl localhost:11434/api/tags` |
| CT Excellence | COMPLETE on `main` (`b79a022`) | sibling repo — pattern source |
| Cascade pack | this directory | authored 2026-10-07 |
