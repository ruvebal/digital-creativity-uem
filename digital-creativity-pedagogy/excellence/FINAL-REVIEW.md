# Final review — DC Excellence cascade

Built during the autopilot run (AUTOPILOT.md §5). Professor reads this **once**
before merging `excellence/integration` → `main`.

## 1 · Run outcome

| Phase | Status | Tag | Notes |
| --- | --- | --- | --- |
| EX0 | DONE | excellence/ex0 | Probe + 55/15/20/10 + D2≡ACT3 lock |
| EX1 | DONE | excellence/ex1 | Contract / How to Pass / ACT↔D |
| EX2 | DONE | excellence/ex2 | Publication firewall |
| EX3 | DONE | excellence/ex3 | Media rules + validate-decks |
| EX4 | DONE | excellence/ex4 | Slide-bound curation + rights |
| EX5 | DONE | excellence/ex5 | Deck renderer + browser layout |
| EX6 | DONE | excellence/ex6 | references.yml + research-manifest (PARTIAL OK) |
| EX7 | DONE | excellence/ex7 | Fashion-craft catalogue |
| EX8 | DONE | excellence/ex8 | Wave-1 Labs I.1–I.5 + FIA |
| EX9 | DONE | excellence/ex9 | Lesson spine / exemplars / figures |
| EX10 | DONE | excellence/ex10 | Assessment bank + consent drafts |
| EX11 | DONE | excellence/ex11 | Closing audit + CD II/NM seed |

## 2 · P0 decisions for you

- **Weights 55/15/20/10** (guía) + Sandra 4×11.2% continuous strip compatibility.
- **D2 Transposition ≡ ACT3 cartel** — see COORDINATION-SANDRA.md + TRANSPOSITION-BRIEF.md.
- **Images (EX4):** autopilot `approved_by` pending your ratification; rights-report flagged rows.
- **Labs (EX8):** classroom adaptations where catalogue sources are held/gap — approve or rewrite.
- **Exemplars (EX9):** every `**Example trace:**` is an illustrative draft, *not student work*.
- **Consent (EX10):** drafts only — **no DPO clearance**; measurement never started.
- **B1 deferred:** I.6–I.9 / CD II / NM decks → NEXT-CASCADE-CD-II.md.

## 3 · Per phase

_(Land notes from earlier phases retained below; EX11 closes the pack.)_

### EX1 — contract

- Published 55/15/20/10 and D2≡ACT3 on evaluation + How-to-Pass.
- Cold review PASS.

### EX9 — lesson structure / exemplars / figures

- Spine pass: I.1–I.9 EN/ES + fashion-image-analysis; Workshop/Tao/Conclusion order per forge laws.
- Gate: `PHASE-EX9.exit-gate.sh` failures 0.
- **P0 for professor — exemplars:** approve, rewrite, or replace Example traces before release.
- I.6–I.9 still await DCI decks (Lab placeholders only).
- Rollback after land: `gitflow.sh rollback 9`.

### EX10 — assessment + consent

- Private question bank (72; higher-order ≥30%); practice quizzes; TRANSPOSITION-BRIEF ≡ ACT3.
- Consent EN/ES + APPROVAL drafts-only; measurement not started.
- Rollback: `gitflow.sh rollback 10`.

### EX11 — closing audit

- Probe `--targets` hardened; `evidence/final-EX11.json` filed.
- `CLOSING-AUDIT.md` lists every FINDINGS ID once (closed or deferred).
- `NEXT-CASCADE-CD-II.md` seeds CD I remainder + CD II + Nuevos Medios.
- Rollback: `gitflow.sh rollback 11`.

## 4 · Closing audit (EX11)

See **[CLOSING-AUDIT.md](CLOSING-AUDIT.md)**. Probe evidence:
`evidence/final-EX11.json`. Handoff seed:
**[NEXT-CASCADE-CD-II.md](NEXT-CASCADE-CD-II.md)**.

## 5 · How to preview

```bash
bash digital-creativity-pedagogy/excellence/gitflow.sh release-notes
# From the integration worktree:
cd "$(dirname "$(git rev-parse --show-toplevel)")/digital-creativity-uem-integration"
bundle exec jekyll serve --source docs --config _config.yml --port 4013
```

Walk Wave-1: evaluation → How to Pass → I.1–I.5 decks → fashion-image-analysis
→ practice quizzes → confirm no infra vocabulary in student HTML.

## 6 · Release or roll back

See `gitflow.sh release-notes` after the full run. Summary:

**Release (professor only, on main):**

```bash
cd /path/to/digital-creativity-uem
git tag -a excellence/pre-release -m "main before Excellence release" main
git merge --no-ff excellence/integration -m "Release DC Excellence cascade"
git push origin main --follow-tags
```

**Roll back after release (no force-push):**

```bash
git revert -m 1 <release-merge-sha> && git push origin main
```

**Roll back one phase on integration (before release):**

```bash
bash digital-creativity-pedagogy/excellence/gitflow.sh rollback <n>
```

Autopilot never pushes `main`.
