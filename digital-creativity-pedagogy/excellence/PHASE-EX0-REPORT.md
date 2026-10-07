# PHASE-EX0 REPORT — Live probe + weights + Sandra lock

**Status:** COLD_REVIEW PASS. Ready for `gitflow.sh land 0`. Implementer does not mark DONE.

**Branch:** `cascade/excellence-0`  
**Commit (verified):** `7f0d3b1`  
**Date:** 2026-10-07  

## What changed

| Area | Paths |
| --- | --- |
| Probe | `probe/excellence-probe.mjs` (Wave-1 metrics, leaks, decks, guía, Sandra PDF) |
| Evidence | `evidence/baseline-EX0.json`, `head-EX0.json` |
| Decision | `DECISION-EX0-GUIA.md` (55/15/20/10 + D2≡ACT3 + Wave-1) |
| Local | `local/{athanor,thessia,ollama-generate}.sh` |
| Gate | `PHASE-EX0.exit-gate.sh` strengthened |
| Log | `DECISIONS-LOG.md` |

## Commands

```text
node …/excellence-probe.mjs --write-baseline --write-head
bash PHASE-EX0.exit-gate.sh  → failures: 0
cascade-harness.sh verify → exit 0
```

## FINDINGS closed / deferred

| ID | Status |
| --- | --- |
| A1 | Decision locked; public page still lacks 55 → EX1 |
| A2 | D2≡ACT3 locked in DECISION + COORDINATION |
| A5 | Wave-1 scope recorded |
| E3 | gitflow init + start done |
| C1 | Measured (9/9 leak); fix EX2 |
| B1 | Measured (6 DCI decks); later phases |

## Cold review

`PHASE-EX0-COLD-REVIEW.md` — PASS (1 P2: lab counter null → EX3+)

## Rollback

`gitflow.sh rollback 0` after land.
