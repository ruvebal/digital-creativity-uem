# PHASE-EX9 cold review — Lesson structure, exemplars, figures

| field | value |
| --- | --- |
| **phase** | PHASE-EX9 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-9` |
| **implementation commit** | `d2c56bae603bd752fbaa5497f0a5e03674331352` |
| **verify log** | `PHASE-EX9-VERIFY-LOG.md` — harness `failures: 0` / Exit **0**; cold re-run Exit **0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |
| **PARTIAL** | I.6–I.9 Labs remain deck-less placeholders; ES I.1–I.5 traces still largely English (structural parity, not voice translation) |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Wave-1 spine headings (I.1–I.9 EN/ES + special) | Cold Python scan: all 9 EN + 9 ES lessons have required H2s in order (LO → Analysis → Masterclass → Lab → Workshop → Conclusion → Tao → References). Fashion master lecture: LO → Analysis → Masterclass → Lab → Conclusion → References (no Workshop/Tao). Workshop first lines name session; `{#tao-of-the-image}` / `id` present on Wave-1 DCI lessons. Editorial + AI after References on all I.1–I.9 | Met |
| Exemplars labelled not student work | `rg` over `docs/lessons/**/i-*/index.md`: every `**Example trace:**` carries `*(Illustrative · not student work.)*` or `*(Ilustrativo · no es trabajo de estudiante.)*`. **UNLABELLED TRACES: 0**. ≥2 traces per Lab (EN+ES I.1–I.9) | Met |
| Provenance / citation counts not regress | Baseline `evidence/EX9/provenance-baseline.json` (19 keys). Cold compare: **0 regressions** on `PROVENANCE_LINE` / `cite_links` / `public_citation`; LAB_LINE only rises (I.6–I.9 placeholders + ES B2). Gate PASS | Met |
| hreflang sane | Built `_site/lessons/en/master-lectures/fashion-image-analysis/index.html`: `hreflang=en` + `x-default` present; **no** `hreflang=es`. Paired I.1 EN emits real ES alternate that resolves under `_site`. `head-hreflang.html` gates ES emit on built page ≠ self | Met |
| Exemplars flagged for professor in FINAL-REVIEW | `FINAL-REVIEW.md` § EX9: **P0 for professor — exemplars** (approve/rewrite/replace; priority I.1–I.2 then I.3–I.5 then I.6–I.9) | Met |
| `PHASE-EX9.exit-gate.sh` exits 0 | Harness log Exit 0; cold re-run Exit 0 (`failures: 0`) | Met |
| Cold review PASS before land | This document → **PASS** | Met |
| Out of scope held | Diff `dca557b..d2c56ba`: Wave-1 lessons + includes/CSS/gate/evidence only; **no** CD II / Nuevos Medios paths | Met |

---

## Spot checks (cold session)

### Exit gate (re-run)

```text
$ bash digital-creativity-pedagogy/excellence/PHASE-EX9.exit-gate.sh
PASS: file digital-creativity-pedagogy/excellence/PHASE-EX9.md
PASS: file docs/_includes/lesson-figure.html
PASS: file docs/_data/lesson_figures.json
PASS: file digital-creativity-pedagogy/excellence/evidence/EX9/provenance-baseline.json

PASS: EN I.1–I.9 section spine

PASS: ES I.1–I.9 section spine

PASS: fashion-image-analysis spine

PASS: B2 exercise cards I.1–I.5 EN+ES

PASS: provenance/citation non-regression
PASS: jekyll build
PASS: publication safety

PASS: hreflang sane (fashion EN-only)
----
failures: 0
EXIT:0
```

Matches harness `PHASE-EX9-VERIFY-LOG.md` (commit `d2c56ba`, failures 0).

### Spine (sample)

| Surface | Order check |
| --- | --- |
| EN I.1–I.9 | Required H2 positions strictly increasing |
| ES I.1–I.9 | Same under ES titles |
| Fashion | Required subset ordered; interstitial “Why this guide” / “Quick card” allowed (relative-order gate) |

I.1 Workshop: `No Workshop in sessions 1–2…`. I.2–I.9: `From session 4: Workshop is protected studio time…`.

### Exemplars

- I.1–I.5 EN: two Lab traces each, labelled illustrative.
- I.1–I.5 ES: B2 card labels present (Time/Group/…/Source ×2); traces present and labelled (see F1 for language).
- I.6–I.9: structural Lab placeholders + two labelled traces each (see F2).

### Figures

- `lesson-figure.html` + `lesson_figures.json` required by gate.
- Cold counts: I.1–I.5 EN/ES + fashion each have 5–6 `lesson-figure.html` includes; I.6–I.9 have **0** (deck-less — consistent with report / FINAL-REVIEW).

### Provenance

```text
REGRESSIONS: 0
RISES: LAB_LINE 0→2 on I.6–I.9 EN/ES (+ some ES cite_links 0→1) — allowed rises only
```

### FINAL-REVIEW exemplar flag

```text
### EX9 — lesson structure / exemplars / figures
- **P0 for professor — exemplars:** every `**Example trace:**` …
```

---

## Findings

### F1 — ES I.1–I.5 example traces still English (P1 · does not block DONE)

**Evidence:** Cold tally on `docs/lessons/es/creacion-digital-i/**`: `Illustrative · not student work` = **10**; `Ilustrativo · no es trabajo de estudiante` = **8** (I.6–I.9 only). I.1–I.5 ES Lab traces reuse EN wording.

**Why not P0:** Acceptance requires labelling + structure, not full ES voice pass. Report already discloses “structural parity only.”

**Fix:** Translate I.1–I.5 ES Lab traces (label + body) in a follow-on pass or EX11 cleanup; keep labels as *Ilustrativo · no es trabajo de estudiante.*

### F2 — I.6–I.9 placeholder traces are thematically identical (P1 · does not block DONE)

**Evidence:** EN/ES I.6–I.9 Lab traces reuse the same volume/CLO “hybrid iteration” / “maquette crease” copy even on animation and bodegones lessons.

**Why not P0:** Explicit structural placeholders pending DCI decks; FINAL-REVIEW already flags professor review + deck gap.

**Fix:** When decks land, replace with unit-specific illustrative traces (still labelled not student work).

### F3 — Gate does not assert the “not student work” string (P2 · does not block DONE)

**Evidence:** Exit gate counts `**Example trace:**` ≥ 2 only. Cold session verified 0 unlabelled traces.

**Fix (optional gate amendment):** Assert label regex on each Example-trace line. Not required to land EX9; would harden EX11 regression.

---

## Hard constraints / out of scope

| Constraint | Check |
| --- | --- |
| No CD II/NM Wave-1 redesign | Diff paths clean |
| No invent media / DPO claims | Figures via EX4/EX5 `lesson_figures.json` captions; flagged rights remain via deck pipeline |
| No main push / land by reviewer | Not performed |
| No gate weakening | Gate filled with real checks; cold re-run green without amendment |
| VTON / Sandra Campus Virtual | Untouched |

---

## Verdict

| **verdict** | PASS |

**P0:** none.  
**P1:** F1 (ES I.1–I.5 English traces), F2 (I.6–I.9 identical placeholders).  
**P2:** F3 (gate label assertion optional).

Eligible for orchestrator land after normal gitflow regression. Reviewer does not mark DONE or land.
