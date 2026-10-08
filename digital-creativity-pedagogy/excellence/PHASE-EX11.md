# PHASE-EX11: Closing audit against EX0 baseline + handoff

> **Track:** measurement + handoff
> **Status:** VERIFYING
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Prove FINDINGS closed/deferred; harden probe; seed CD II / NM next cascade; forge handoff.

## Deliverables

1. `evidence/final-EX11.json` + probe `--targets` exit 0
2. `CLOSING-AUDIT.md` every FINDINGS ID once
3. `NEXT-CASCADE-CD-II.md` (+ NM note)
4. Forge/AGENTS pointers updated
5. FINAL-REVIEW §4–§6 complete

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX11. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Probe targets met on Wave-1 scope
- CLOSING-AUDIT complete
- Gate regression EX0–EX11 green on land
- Handoff seed exists

- `PHASE-EX11.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
