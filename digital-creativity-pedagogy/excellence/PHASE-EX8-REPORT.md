# PHASE-EX8 report — Lab redesign Wave-1 + exercise cards

**Status:** VERIFYING (implementer stop — cold review owns PASS/DONE)

**Worktree:** `digital-creativity-uem-integration-excellence-8` · branch `cascade/excellence-8` · lane `excellence`

**FINDINGS cited:** **D1**, **D2** (ACT1/ACT2 Labs practise Masterclass; exactly two `lab_exercise` per touched deck). EX7 cold-review **F2** (held/gap ACT anchors = classroom adaptations).

## What changed (files)

### Decks (`docs/tracks/en/uem/2627-dci/*/data/content.json`)

| Deck | Labs | method_ids |
| --- | --- | --- |
| `i-1-fashion-image` | 2 | `fashion-photograph-reading`, `figurin-digital` |
| `i-2-2d-drawing` | 2 (was 3) | `croquis-proportion-scaffold`, `construction-vs-finish-lines` |
| `i-3-color-bitmaps` | 2 | `key-visual-brief-lock`, `gestalt-composition` |
| `i-4-effects` | 2 | `photobash-integration`, `compositing-before-after-strip` |
| `i-5-three-dimensional-form` | 2 | `2d-to-3d-sequence-sketch`, `silhouette-from-volume` |

Each `lab_exercise` now carries `method_id`, `practises` → existing masterclass `slide_id`s, `timer_seconds`, facilitation `notes`, `portfolio_trace`.

I.2: removed `lab-3`; rebound curated `Work in Progress.JPG` from `I.2.lab-3` → `I.2.lab-2`; deleted orphan `deck-media/152b234ba400335e.webp`.

### Lessons (B2 exercise cards)

- `docs/lessons/en/digital-creativity-i/i-1-digital-images/index.md`
- `…/i-2-2d-drawing/index.md`
- `…/i-3-color-bitmaps/index.md`
- `…/i-4-effects/index.md`
- `…/i-5-three-dimensional-form/index.md`

Each B2 has exactly two Exercise cards with **Time / Group / Materials / Steps / Portfolio trace / Judged by / Source**.

### Curation / gates / log

- `curation/LAB-SIGNOFF.md` — `approved_by: autopilot (final review pending)`
- `PHASE-EX8.exit-gate.sh` — real checks (decks, cards, validator, jekyll, browser)
- `FINDINGS-2026-10-07.md` — D1/D2 closure note (pending cold-review PASS)
- `DECISIONS-LOG.md` — EX8 autopilot rows
- `docs/assignments/en/digital-creativity-portfolio/index.md` — `{#rubric}` anchor for Judged-by links
- `curation/rights-report.json`, `autopilot-assets.json`, `I.2-SHORTLIST.md` — lab-3 rebound notes
- Re-rendered includes via `npm run render:decks` (I.2 include + `lesson_figures.json`)

## What was run

```text
bash digital-creativity-pedagogy/excellence/PHASE-EX8.exit-gate.sh
→ failures: 0  (GATE_EXIT:0)
  PASS deck labs · B2 cards · no I.2 lab-3 · validate-decks --strict
  PASS render-decks · jekyll build
  PASS browser: deck-layout: 370 slide view(s), 0 failure(s)
```

## Selection / scope

- **In:** I.1–I.4 ACT1/ACT2 Labs + **selected I.5** (only I.* deck beyond I.4 with Wave-1 DCI deck).
- **Deferred:** I.6–I.9 Labs (no `2627-dci` decks yet) → EX9.
- **Not invented:** off-book graded Campus Virtual work; Abling/Arnheim page cites for held/gap anchors.

## Uncertain / resume

- Cold reviewer should spot-check card Steps vs catalogue methods and Source honesty (classroom adaptation vs verified).
- ES lesson parity for B2 cards not in this phase (Wave-1 EN decks/lessons only; A3 remains EX9).
- Resume point for harness: verify log → cold review → land (implementer does **not** mark DONE / land).
