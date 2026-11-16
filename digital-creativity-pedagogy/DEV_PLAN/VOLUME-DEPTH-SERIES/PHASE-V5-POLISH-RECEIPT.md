# PHASE-V5 — Polish receipt · ML-VD-A/B/C (2026-11-16)

**Trigger:** professor in-session instruction — polish and complete the three master lectures and decks with semantic image backgrounds; raise the creativity-studies and human–machine collaboration level.

## What changed

| Surface | Before | After |
| --- | --- | --- |
| Lessons A/B/C | ~70 lines each, 1–2 figures, 0–1 cites | ~230–300 lines each: session clock, objectives, analysis, 5–6 masterclass ideas, 2 Lab exercises, recall, references |
| Decks | runtime shells (old CSS `v=20261006a`, no pre-rendered include), numbered headings, 4–6 geometric content slides | reference pattern (DCF): pre-rendered include, typography law, 16–17 slides, **every content slide on a semantic image**; geometric only on opener/retrieval/lab-opener/outro |
| Course diagrams | reused I.5 figures | 8 new `vd-*` SVGs in `lesson-figures/visual-forger/` (inverse problem, three frames, cue ledger, visual pyramid, Boden moves, projection x/z, engine honesty, human–machine loop) |
| Media | ML-VD-A 4 · ML-VD-B 3 · ML-VD-C 0 bound | 10 bound per deck; +21 Commons assets in `autopilot-assets.json` (`approved_by: professor in-session instruction 2026-11-16 (final review pending)`) |
| References | `panofsky-1993` only | + `boden-2004`, `vince-2017`, `an-park-2026`, `bendel-2025` |

## Grounding corrections (important)

- **Panofsky page basis was wrong.** The Zone Books PDF is a two-up scan (99 sheets). `ahmes query --cite` reports `scheme=pdf_order`, not printed pages. Printed page = 2 × pdf_seq (left half, x0 < 320) or 2 × pdf_seq + 1 (right half). Validated against Wood's introduction citing the symbolic-form passage as pp. 40–41. The old public cites "(Panofsky 1991, 14–15)" → now 28, 29, 31, 40, 67, 71.
- `FORM-GRAMMAR-PAGE-SPOT.md` records "(Panofsky 1991, 27)" for page_index 26 — by the same rule that node sits on printed 54/55. Not used on any public page today; fix before reuse.
- Boden printed = pdf_seq − 15; Vince printed = pdf_seq − 13; Bendel printed = pdf_seq + 436; An and Park = article page.
- `panofsky-1993.edition_note` rendered "coat ready — spot-check…" publicly — replaced with a student-safe note.

## Held for next pass (BIBLIO-GAP, not cited)

Jang 2026 *From designer to curator* (Fashion and Textiles 13:12) · Kim 2024 (IEEE Access) · Fu et al. 2024 (arXiv) · Van Hulle 2019 (IJDH, evaluator_safe=no). Repair RIS metadata to promote Jang into Lecture C §5.

## Gates

| Gate | Result |
| --- | --- |
| `node --test scripts/tests/` | 50/50 pass |
| `validate-decks --strict --rights=flag` | 0 errors (rights warnings = pre-existing flagged statuses) |
| `verify:citations` | pass |
| `verify:publication` | 1 pre-existing finding (`_site/_data/forged_assets.json`), unrelated |
| Browser (dev :4002) | 3 decks render pre-rendered; all lesson images 200; all `#ref-` and lab card anchors resolve |

## Not done

Spanish twins (no ES volume-depth lessons exist yet) · human final review of the 21 new media rights · Rive overlays.
