# PHASE-EX9 report — Lesson structure, exemplars, lesson images

**Status:** VERIFYING. Deliverables 1–4 done; gate pre-check failures 0. Next: `cascade-harness.sh verify`, then cold review. Do **not** mark DONE here.

| Field | Value |
| --- | --- |
| **branch / worktree** | `cascade/excellence-9` · `digital-creativity-uem-integration-excellence-9` (`.cascade-lane` = `excellence`) |
| **mode** | AUTOPILOT; judgment calls in `DECISIONS-LOG.md` |
| **cascade_amended** | Exit gate filled (was scaffolding); INDEX/PHASE status → VERIFYING only after harness — this report stays VERIFYING |

## Files changed

- Lessons EN: `docs/lessons/en/digital-creativity-i/i-{1..9}-*/index.md`, `docs/lessons/en/master-lectures/fashion-image-analysis/index.md`
- Lessons ES: `docs/lessons/es/creacion-digital-i/i-{1..9}-*/index.md`
- Includes: `docs/_includes/lesson-figure.html`, `docs/_includes/head-hreflang.html`
- CSS: `docs/assets/css/site.css` (`.lesson-figure`)
- Gate: `PHASE-EX9.exit-gate.sh` (real Acceptance checks)
- Evidence: `evidence/EX9/provenance-baseline.json`, `restructure_wave1.py`, `es_b2_parity.py`, `inject_lesson_figures.py`
- Records: `DECISIONS-LOG.md`, `FINAL-REVIEW.md` (exemplars P0), `FINDINGS-2026-10-07.md` closure note

## Structure (after)

EN/ES I.1–I.9 spine (in order): Learning objectives / Objetivos · Analysis / Análisis · Masterclass · Lab (Portfolio) · Workshop · Conclusion / Conclusión · Tao of the Image / Tao de la imagen `{#tao-of-the-image}` · References / Referencias · Editorial · AI.

Fashion-image-analysis: Learning objectives · Analysis · Masterclass · Lab · Conclusion · References (no Workshop/Tao — master lecture).

Workshop first line names session timing (I.1: no Workshop in sessions 1–2; others: from session 4).

## Exemplars

- I.1–I.5 EN: `**Example trace:**` ×2 per Lab (labelled *Illustrative · not student work*).
- I.1–I.5 ES: B2 card parity from EN Labs (same EX8 field labels) + traces.
- I.6–I.9 EN/ES: structural Lab placeholders (no DCI decks) + two illustrative traces each.
- **Professor flag:** all Example traces + design examples need approval/replace — see FINAL-REVIEW.

## Figures

- `lesson-figure.html` + deck assets from `lesson_figures.json` (EX4/EX5 bindings).
- Injected into Masterclass for I.1–I.5 EN/ES + fashion-image-analysis (3–6 figures each, rights-safe captions; flagged assets keep “Rights under review” via deck caption pipeline).

## EX8 deferrals closed

- I.6–I.9 Labs: structural placeholders (decks absent under `2627-dci`).
- ES B2 card parity: I.1–I.5 done.

## Citation / provenance

Baseline: `evidence/EX9/provenance-baseline.json`. Gate checks PROVENANCE_LINE / cite_links / public_citation never fall; LAB_LINE may rise for I.6–I.9 placeholders. Pre-check: no regressions.

## Verification (implementer)

```text
bash digital-creativity-pedagogy/excellence/PHASE-EX9.exit-gate.sh
→ failures: 0
```

Includes jekyll build + publication safety + hreflang check (fashion EN-only does not emit bogus `hreflang=es`).

## Uncertain / open

- I.6–I.9 still lack DCI decks — Lab placeholders only (EX11 / next deck wave).
- ES Masterclass bodies for I.2–I.5 remain thinner than EN (structural parity only; not a full voice translation pass).
- Example traces are autopilot drafts — professor P0 in FINAL-REVIEW.

**Resume point:** `cascade-harness.sh verify … PHASE-EX9.md <worktree>`, then cold review. Do not land until cold review PASS.
