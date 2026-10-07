# PHASE-EX2: Publication firewall

> **Track:** safety
> **Status:** BLOCKED (EX1 DONE)
> **Autopilot:** human gates replaced by AUTOPILOT.md §2; log in DECISIONS-LOG.md.

## Goal

Remove internal infra vocabulary from student HTML; fail-closed safety script tuned for DC.

## Deliverables

1. Expanded `verify-publication-safety` patterns (Ahmes, Athanor, profield, lesson-scribe, vault paths, UDIT, sibling course brand leakage)
2. Rewrite offending Wave-1 (+ firewall-only CD II/NM) student sentences
3. One-sentence AI declaration footers + `/ai-declaration/` link
4. Gate that fails on pre-fix fixtures

## Scope

**In:** Wave-1 (A1) surfaces named in the Goal/Deliverables.  
**Out:** VTON; Sandra Campus Virtual edits; full CD II/NM redesign (firewall-only in EX2); measurement start.

## Prompt (Implementation Agent)

```text
Implement PHASE-EX2. Site-wide firewall outranks Wave-1 scope for leak removal only. Do NOT mark DONE.

Read: INDEX.md, AUTOPILOT.md, TECHNICAL-DIRECTOR-CASCADE.md, FINDINGS-2026-10-07.md,
COORDINATION-SANDRA.md, PROFIELD-AND-INFRA.md, LOCAL-EXECUTION.md, this file.
Cite FINDINGS IDs you close. Prefer cascade-phase-executor. Do not commit unless the orchestrator policy says to (AUTOPILOT commits on the phase branch).
```

## Acceptance

- Safety script exit 0 on built `_site`
- FINDINGS C1/E1 addressed for Wave-1; CD II/NM firewall-only
- Gate proves at least one known leak term would fail a fixture

- `PHASE-EX2.exit-gate.sh` exits 0
- Cold review PASS before land

## Risks

- Scope creep into CD II/NM content redesign
- Model-invented citations (forbid)
- Weakening gates to pass regression (forbid without gate amendment)
