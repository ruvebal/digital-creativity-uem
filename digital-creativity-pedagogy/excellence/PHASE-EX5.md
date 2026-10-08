# PHASE-EX5: Deck renderer: pre-render, alt, captions, notes, layouts

> **Track:** renderer
> **Status:** VERIFYING (EX4 DONE)
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Student decks render captions/alt/notes/timers; browser layout check green on Wave-1.

## Deliverables

1. Renderer/lib updates as needed
2. `scripts/tests/browser/deck-layout.mjs` (or DC port) in EX5 gate
3. Speaker notes hygiene

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX5. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- `npm run test:browser` (or gate-equivalent) 0 failures on Wave-1 viewports + print card checks
- Captions/alt present for bound assets

- `PHASE-EX5.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
