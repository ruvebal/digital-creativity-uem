# PHASE-EX0: Live probe + baseline + guía weights + Sandra coordination lock

> **Track:** measurement + decision
> **Status:** READY
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Instrument the live site, freeze a baseline JSON, record official 55/15/20/10 weights and the D2≡ACT3 lock so later phases have a falsifiable target.

## Deliverables

1. `probe/excellence-probe.mjs` (Node) measuring Wave-1 lessons/decks: leak terms, lab count, dangling slots, rights freshness hooks, EN/ES parity counts
2. `evidence/baseline-EX0.json` + `evidence/head-EX0.json`
3. `DECISION-EX0-GUIA.md` — weights from `cv/guides/1-creacion-digital-i.json` / CD II twin; Sandra continuous strip compatibility note
4. `local/` shell helpers stubs (athanor/thessia/ollama) if missing
5. Confirm `COORDINATION-SANDRA.md` + PDF under `cv/sources/`

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX0. Build a DC-tuned probe (do not blindly copy CT CONTENIDOS selectors — use I.1–I.9 / fashion-image-analysis). Write baseline at current HEAD. Write DECISION-EX0-GUIA.md locking 55/15/20/10 and D2=ACT3. Hand off for cold review — do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Exit gate 0; probe runs and writes JSON
- DECISION file cites guía JSON paths and Plan de trabajo PDF path
- FINDINGS A1/A2/A5 reflected in decision + INDEX live snapshot still accurate or amended
- `gitflow.sh init` documented in REPORT (or already done by orchestrator)

- `PHASE-EX0.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
