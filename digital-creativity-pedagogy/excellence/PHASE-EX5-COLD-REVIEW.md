# PHASE-EX5 cold review — Deck renderer + browser layout (Wave-1)

| field | value |
| --- | --- |
| **phase** | PHASE-EX5 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-5` |
| **implementation commit** | `f0947d33a4cacaa6a57d60fea5300c7c0160854f` |
| **verify log** | `PHASE-EX5-VERIFY-LOG.md` (harness transcript truncated — see F1); cold re-run Exit code **0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| `npm run test:browser` (or gate-equivalent) 0 failures on Wave-1 viewports + print | Cold re-run: `PASS: browser layout check: deck-layout: 375 slide view(s), 0 failure(s)` (3× screen + 2× print over 6 Wave-1 decks = 375) | Met |
| Captions/alt present for bound assets | All Wave-1 curated sections in `docs/_includes/decks/*.html` carry `.sr-only` + `.slide-caption`; gate Python check PASS | Met |
| `PHASE-EX5.exit-gate.sh` exits 0 | Cold re-run → `failures: 0` / `EXIT:0` | Met |
| Cold review PASS before land | This document | Met |
| Deliverable: renderer + browser test in gate | `scripts/lib/deck-render.mjs`, `scripts/render-decks.mjs`, `scripts/tests/browser/deck-layout.mjs`; gate requires file + runs browser check (fails on SKIP) | Met |
| Speaker notes hygiene | Required roles (`masterclass` / `lab_exercise` / `workshop_work`) all have notes in content + built includes; no empty `aside.notes` | Met |

---

## Spot checks (cold session)

### Exit gate (re-run)

```text
$ bash digital-creativity-pedagogy/excellence/PHASE-EX5.exit-gate.sh
PASS: render-decks runs
PASS: validator --strict green
PASS: jekyll build
PASS: no hard-coded base path in deck JS
PASS: no timestamped runtime fetch
PASS: render step wired into prebuild
PASS: browser test script wired
PASS: geometric SVGs carry a hash (6/6)
PASS: file docs/assets/images/fractal-triangles/current.json
PASS: file scripts/tests/browser/deck-layout.mjs
PASS: pre-rendered sections, alt text, notes (Wave-1)
PASS: browser layout check: deck-layout: 375 slide view(s), 0 failure(s)
----
failures: 0
EXIT:0
```

### Full existing Node suite

```text
$ node --test scripts/tests/*.test.mjs
# tests 45  # pass 45  # fail 0
```

### Module load

```text
$ node -e "import('./scripts/lib/deck-render.mjs').then(…)"
# exports load; exit 0
$ node scripts/render-decks.mjs
# render-decks: 6 deck(s), 0 written.  (includes already match renderer)
```

### FINDINGS B4 / B5

| ID | Disposition (cold) |
| --- | --- |
| **B4** | Closed for Wave-1: `deck-layout.mjs` in EX5 gate; 375 views / 0 failures (screen floors + print). |
| **B5** | Closed for EX5 scope: every Wave-1 `analysis_opener` / `lab_opener` / `workshop_opener` is `geometrical` with hashed henon caption (`slide-caption__hash`). Lab/Workshop *content* redesign remains EX8 (report “Partial” is accurate for that remainder). |
| **B1** | Still deferred (EX11) — out of EX5 Acceptance. |

### Pre-rendered include sample

`docs/_includes/decks/i-1-fashion-image.html`: sections with `data-layout`, curated `sr-only` + `slide-caption`, geometrical openers with `#…` hash captions, `lab_exercise` with `data-timer="180"`, `aside.notes` present. Pages wire `{% include decks/<slug>.html %}`. No CD II / NM path touches in `bdeb361..HEAD`.

### New tests would fail pre-fix

`scripts/tests/deck-render.test.mjs` (12 cases) and browser layout script did not exist before EX5; `committed deck includes match the renderer` fails if includes drift from `renderDeck`.

---

## Findings

### F1 — Harness VERIFY-LOG truncated before browser check

- **Severity:** P2  
- **Blocks DONE:** no  
- **Evidence:** `PHASE-EX5-VERIFY-LOG.md` ends after `PASS: pre-rendered sections…` with no browser line and no `failures: 0` / Exit footer (unlike EX3 VERIFY-LOG). Cold re-run of the same exit-gate at `f0947d3` produced the missing browser PASS and `EXIT:0`.  
- **Fix:** Re-capture harness verify log on next land, or amend harness log capture so long-running browser steps are not clipped.

### F2 — Filename-like `alt` / `sr-only` text (EX4 F2 carry-forward)

- **Severity:** P2  
- **Blocks DONE:** no (Acceptance requires presence, not prose quality)  
- **Evidence:** 25 Wave-1 curated alts still mirror Commons filenames (e.g. `Astronaut Riding a Horse (SD3.5).webp`, `Dirty and damaged fashion doll.jpg`).  
- **Fix:** Optional alt prose pass before release; not EX5-blocking.

### F3 — Gate run mutates `rights-report.json` timestamp only

- **Severity:** P2  
- **Blocks DONE:** no  
- **Evidence:** Uncommitted diff is solely `generated_at` (`14:35:09` → `14:54:51`).  
- **Fix:** Discard or avoid committing timestamp-only churn after verify.

No open P0. No open P1.

---

## Verdict

| **verdict** | PASS |

Eligible for product-owner promotion to DONE / land on the excellence integration branch after triage of P2 F1–F3 (non-blocking). Do not open EX6 until DONE.
