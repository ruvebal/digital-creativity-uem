# Autopilot mode — DC Excellence cascade

**Status:** READY (not started). The cascade runs EX0 → EX11 without
per-phase human sign-off. The professor reviews **once**, at the end, before
anything reaches `main` (the live student site). This file overrides the
"Human gate" lines in `TECHNICAL-DIRECTOR-CASCADE.md` and the phase files.

Departing point: CT Excellence AUTOPILOT (COMPLETE, 2026-10-07 release
`b79a022` on creativity-techniques-uem). Same loop, DC-specific decisions.

## 0 · Launch decisions (professor, 2026-10-07)

| Decision | Value |
| --- | --- |
| Official weights to publish | **55 / 15 / 20 / 10** from CD I/II guía JSON (2026–27); compatibility note for Sandra’s 4×11.2% continuous strip; P0 in final review |
| Transposition | **Lock D2 = Sandra ACT3** (cartel from another language) — see COORDINATION-SANDRA.md |
| Deck images | **Auto-pick** from accepted Profield + policy-compliant open collections; rights recorded; `flagged` not blocking; professor reviews every pick before release |
| Off-machine backup | **Push** `excellence/*` and `cascade/excellence-*` branches and `excellence/*` tags after each landing; **never push `main`** |
| Teaching languages | Student site EN + ES; coordination artefacts may be bilingual |
| Wave-1 scope | CD I (I.1–I.9) + fashion-image-analysis special; CD II / Nuevos Medios = firewall + EX11 handoff |

Execution profile: **local-first** — [LOCAL-EXECUTION.md](LOCAL-EXECUTION.md).

## 1 · What runs automatically, and what never does

| Automatic | Never automatic |
| --- | --- |
| Opening each phase worktree (`gitflow.sh start`) | Merging into `main` or pushing `main` |
| Implementation by `cascade-phase-executor` | Changing Sandra’s Campus Virtual plan |
| Exit gate via `cascade-harness.sh verify` | Starting measurement / collecting student data (EX10) |
| Cold review by `cascade-cold-reviewer` (fresh agent) | Claiming DPO / exhibition consent clearance |
| Landing on `excellence/integration` (`gitflow.sh land`) with regression | Hard-constraint exceptions |
| Pushing phase/integration branches and tags (`EXCELLENCE_PUSH=1`) | Pushing `main` |
| Rolling back integration on regression failure | Deleting tags/branches without professor |

## 2 · Pre-registered decisions (replace the human gates)

Every decision under this policy is appended to `DECISIONS-LOG.md`
(`date · phase · decision · rule · alternatives · undo`).

| Phase | Gate in the plan | Autopilot rule |
| --- | --- | --- |
| EX0 | Professor confirms weights + coordination | 55/15/20/10 from guía; D2=ACT3 lock; `confirmed_by: professor-launch-2026-10-07`; P0 final review |
| EX4 | Professor picks images | Best-fitting candidate per slide (brief ≥ 4/5, cold-reviewed); rights recorded; doubt → `flagged`; `approved_by: autopilot (final review pending)` |
| EX6 | Book procurement | Vault / open access only; else `gap`; PARTIAL allowed |
| EX8 | Professor signs off Labs | Target Labs in PHASE-EX8 (ACT1/ACT2-aligned); `approved_by: autopilot (final review pending)` |
| EX10 | Consent and bank approval | Drafts only; measurement never starts |
| Any | Ambiguity | More conservative option (less published, fewer claims); log; continue |
| Any | Sync conflict with `main` | Stop unless CT-style A8 protocol is followed and cold-reviewed |

## 3 · Orchestration loop

```text
bash tests/test-gitflow.sh                        # once, throwaway clone
gitflow.sh init                                   # once
for n in 0..11:
  gitflow.sh start
  Agent(cascade-phase-executor, worktree, PHASE-EXn.md + AUTOPILOT.md)
  cascade-harness.sh verify <integration>/…/excellence PHASE-EXn.md <worktree>
  commit PHASE-EXn-VERIFY-LOG.md
  Agent(cascade-cold-reviewer, fresh, …) → PHASE-EXn-COLD-REVIEW.md
  executor: PHASE-EXn-REPORT.md + DECISIONS-LOG.md
  gitflow.sh land n                               # --no-ff, regression, tag excellence/exn
  append FINAL-REVIEW.md section
```

Serialize heavy Ollama loads with any sibling cascade jobs (`ps` + wait).

## 4 · Stop rules

- Exit gate fails after 3 implementation attempts
- Cold review P0 survives 2 fix cycles
- Hard-constraint exception required
- Gate would need silent weakening (amendment + cold-review "gate amendment" only)
- Worktree / git / harness unexpected behaviour
- Sync conflict with genuine Wave-1 content from `main` (A8 protocol)

On stop: write reason at top of `FINAL-REVIEW.md`; do not start later phases
out of order.

## 5 · Final review packet (`FINAL-REVIEW.md`)

1. Run outcome (phases, PARTIALs, stop reason)
2. P0 decisions: weights, Sandra lock, every autopilot image, Lab sign-off, consent drafts, transposition brief
3. Per phase: diffstat, gate log, cold review, decisions, rollback
4. Closing audit (EX11): baseline vs final probe; every FINDINGS ID
5. Preview: `gitflow.sh release-notes`
6. Release / rollback commands

Suggested order (~2 h): §2 → preview I.1–I.4 decks/lessons + D2 brief → §4 → spot-check two diffs → release.

## 6 · Git flow

Identical to CT Excellence (see `gitflow.sh`):

- `excellence/base` tags `main` at init
- Land `--no-ff` on `excellence/integration`, tag `excellence/exN`
- Release: one `--no-ff` merge to `main` after professor review
- Rollback after release: `git revert -m 1 <merge>` (no force-push)
