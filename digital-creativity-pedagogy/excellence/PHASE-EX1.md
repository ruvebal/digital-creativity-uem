# PHASE-EX1: Contract and factual hotfix

> **Track:** student contract
> **Status:** BLOCKED (EX0 DONE)
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Publish a coherent How-to-Pass / evaluation story: guía buckets, Sandra ACT↔D map, Workshop rhythm, transposition named once.

## Deliverables

1. Evaluation + How-to-Pass pages: 55/15/20/10 + ACT compatibility note (no fake guía rows)
2. Explicit D2 = ACT3 cartel brief pointer (full brief in EX10)
3. EN/ES critical factual fixes for Wave-1 (parity blockers only)
4. Session rhythm wording aligned with `SESSION-RHYTHM-AND-DELIVERABLES.mdc`

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX1 per runbook. Touch only contract surfaces + blocking Wave-1 factual errors. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Gate greps published weights 55/15/20/10 on evaluation/how-to-pass
- Gate finds Transposition/ACT3 coordination sentence
- No second competing transposition deliverable invented
- Build + publication safety still pass

- `PHASE-EX1.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
