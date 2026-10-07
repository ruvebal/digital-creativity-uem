# PHASE-EX4: Slide-bound image curation with rights checks

> **Track:** curation
> **Status:** VERIFYING
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Bind Wave-1 deck slides to brief-fitting assets; record rights; flag doubts.

## Deliverables

1. `curation/*-SHORTLIST.md` + `curation/autopilot-assets.json` + `rights-report.json`
2. Rebound Wave-1 `content.json` slides (≥60% core image slides bound or explicit diagram fallback)
3. Vision brief-fit log under `evidence/EX4/` (local model)

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX4 under AUTOPILOT image policy. Profield runs per PROFIELD-AND-INFRA. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Gate: rights report fresh vs decks; curator_flagged counted
- Autopilot assets recorded; no silent `ok` on EU-term doubt
- Browser not required yet (EX5)

- `PHASE-EX4.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
