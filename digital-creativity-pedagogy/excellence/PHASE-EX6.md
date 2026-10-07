# PHASE-EX6: Research grounding + single bibliography source

> **Track:** research
> **Status:** VERIFYING (PARTIAL — 10 verified / 36 gap; exit gate 0)
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.
> Implementer must not mark DONE — cold review + harness verify next.

## Goal

Broadcast Ahmes/Athanor/bibliographies into one research-manifest + references.yml; page-check pins.

## Deliverables

1. `research-manifest.yml` covering Wave-1 units from PROFIELD-AND-INFRA corpora
2. Single `references.yml` (or existing DC equivalent hardened)
3. Gap/procurement list; PARTIAL allowed
4. Critical-layer works for D2 (Steimberg, Werhane, Munari) verified or gapped

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX6. Discover in vectors; cite Ahmes only. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Probe/gate: uncited references scoped → 0 or documented
- Every Wave-1 lesson References resolve to manifest keys
- No vector snippets in student HTML

- `PHASE-EX6.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
