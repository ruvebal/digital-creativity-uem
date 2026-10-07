# PHASE-EX3: Image/media pipeline rules + tests + deck validator

> **Track:** media engineering
> **Status:** BLOCKED (EX2 DONE)
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Port CT-grade media discipline: schema, validator modes, rights hooks, orphan checks — adapted to DC decks.

## Deliverables

1. `scripts/validate-decks.mjs` (or harden existing) with `--strict --rights=flag`
2. Tests under `scripts/tests/` for block/flag/orphan/reuse
3. Forge rule pointers in `STUDENT-SLIDESHOW-FORGE.mdc` / `dc-unit-forge.mdc`
4. Schema version note for Wave-1 decks

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX3. Prefer adapting CT patterns; do not delete cache files referenced by any deck. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Validator + tests green; gate runs them
- Rights report path exists (may be empty until EX4)
- Legacy decks outside Wave-1 warn, not hard-fail (A1)

- `PHASE-EX3.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
