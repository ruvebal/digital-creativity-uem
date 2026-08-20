# CD Wave 4 execution receipt

**Executed:** 2026-08-20
**Contract:** `CD-WAVE-4.execute.md`
**Units:** I.1 — Introducción a las imágenes digitales; I.2 — Tecnología digital 2D: Herramientas de dibujo; I.3 — Color, imágenes con mapas de bits; I.4 — Efectos; I.7 — Fuentes y referencias compositivas en el diseño de moda; I.8 — Creación de imágenes digitales animadas; I.9 — Bodegones digitales

This wave completes CD I's nine-CONTENIDOS-anchor set — I.5/I.6 (three-dimensional form/volume) were forged in an earlier session (Wave 2); this wave forges the remaining seven, in the trigger's specified order: I.1 → I.2 → I.3 → I.4 → I.7 → I.8 → I.9.

## `[BIBLIO-GAP]` and citation rows — what was genuinely re-verified this session

Every citable claim was checked live via `ahmes status` and/or `ahmes query --cite --require-evaluator-safe` this session, not trusted from the matrix's existing text:

| Unit | Coat | `ahmes status` before | Live re-check this session | Disposition |
| --- | --- | --- | --- | --- |
| I.1 | Shinkle 2008, `1936070c` | `evaluator_safe: yes` (matrix already SAFE) | `ahmes query --cite --require-evaluator-safe` on node `cca1472b-b0c6-594c-8e13-ed87d6b73897` re-confirmed `(Shinkle 2008, 15)`, evaluator_safe=yes, confidence 0.95 | **Re-confirmed live, unchanged.** SAFE for the field-of-practices frame only; does not ground tool pedagogy. |
| I.7 | Campinho et al. 2025, `31a9a359` | Matrix's prior text: `evaluator_safe=no` (slug-derived) | `ahmes status` this session shows `evaluator_safe: yes`, confidence 0.95, `source: metadata`, `method: manual-verified-crossref`. `ahmes query --cite --require-evaluator-safe` on node `29e0b3cf-bd30-5373-bfbe-d208de8c3a3b` confirmed `(Campinho 2025, 2)`, evaluator_safe=yes | **Genuinely resolved — the one `[BIBLIO-GAP]` this trigger explicitly asked to attempt, and it resolved on its own before this session's check (the metadata cascade had already run and been manually verified).** No `ahmes enrich --meta --online` attempt was needed or run — the coat was already `evaluator_safe=yes` at the first live check, so forcing an enrich would have been redundant, not a missed step. Per the trigger's own instruction ("if it resolves, cite it"), I.7 is forged as **SAFE, narrow** rather than a declared-gap unit — but the *topical* boundary is preserved and stated explicitly in the lesson: the paper studies representation of fat/obese bodies in Google-Images search results (a body-representation-ethics study), not compositional-reference-sourcing pedagogy. The metadata fix changed whether the citation is *usable*, not what topic it *studies* — both units' lessons say this in as many words. |
| I.2, I.3, I.4, I.8, I.9 | — (matrix rows are NONE) | n/a — no coat named | Not applicable | **No citation to force.** Five full declared-gap units; no enrich attempt was possible because there is no candidate source. |

**No `[BIBLIO-GAP]` row was forced this wave.** I.7 resolved genuinely (not by an enrich attempt run this session — the resolution had already landed via an earlier manual-verified-crossref pass, and this session's job was to re-check it live rather than trust the matrix's stale text, which it did). `digital-creativity-pedagogy/grounding/README.md` was **not** edited this session — I.7's matrix row text still shows the old `evaluator_safe=no` state as historical record; the live disposition is documented in `CD-WAVE-4.execute.md`'s header instead, following the same pattern CD Wave 3 used for its own live re-verification addendum. A future matrix-maintenance pass should fold this into `grounding/README.md` directly; flagged, not done here (out of this wave's per-lesson scope).

## What each unit teaches, and its honest evidence class

- **I.1 (imágenes digitales):** SAFE, narrow. Shinkle (2008)'s field-of-practices frame — fashion photography as simultaneously artistic and commercial, boundary "shifting and highly permeable" — grounds the unit's opening claim. Does not ground any tool sequence. No guía `learning_outcomes` bullet names this anchor directly; stated honestly rather than stretched.
- **I.2 (dibujo 2D):** declared gap, full. Vector-drawing-as-relationship taught as craft discipline. The one guía LO bullet naming vector drawing tools directly (*"Seleccionar las herramientas de dibujo vectorial…"*) is used verbatim.
- **I.3 (color, bitmaps):** declared gap, full. Bitmap-as-fixed-grid taught as craft discipline; the colour-correction/colour-change disclosure question deliberately echoes CD II's retouching unit (II.1) at the level of colour rather than body.
- **I.4 (efectos):** declared gap, full. Effect-as-transformation-with-a-before taught as craft discipline; same disclosure-ethics register as I.3 and CD II's II.1.
- **I.7 (referencias de moda):** SAFE, narrow — the wave's one real citation upgrade. Campinho et al. (2025) grounds the representation-ethics of what a compositional-reference search surfaces (a real, unflattering finding about Google-Images results for "fat body"/"obese body" searches), explicitly **not** a sourcing-pedagogy method. `COMP9` (original problem-solving) is the load-bearing competency.
- **I.8 (animación):** declared gap, full, **with a disclosed hour-allocation exception.** This unit carries 0 h debates and 0 h resolución de problemas in the wave's own allocation table — the only departure from `dc-unit-forge.mdc`'s "B2 ≠ B3" rule in this wave, justified only by that 0 h resolución allocation and stated explicitly on the unit page, not silently absorbed.
- **I.9 (bodegones):** declared gap, full, and explicitly framed as a **synthesis exercise** across I.1–I.4 rather than new grounded technique. Matrix's own conditional ("S1 if any bodegón is exhibited") is honoured: no exhibition claim is made, so no S1/S2 in this unit — stated explicitly rather than silently dropped.

## ARTEFACT ROLE

**`none` for all seven units.** CD I's CONTENIDOS anchors are not on `oficial-guia-framework.mdc` §2's vShowroom-eligible list (that list is CD II anchors 2·3·5·6 only) — this is a structural fact about CD I, not a per-unit judgement call, and no S1/S2 consent template appears in any of the seven lessons.

## TTOD epigraphs

Selected via `TTODCliAdapter.search_quotes()`, never by hand-parsing `ttod.yml`. All seven confirmed unused elsewhere in this repo (`grep` across `docs/lessons/**/index.md`) before selection, alongside the eight IDs already in use (`arch-017`, `img-001`, `img-024`, `img-046`, `img-058`, `qa-010`, `qa-013`, `wis-013`):

- **I.1:** `qa-008` — *"The path to mastery begins with reading…"* — direct-ish fit (an introductory unit is the "begins with reading" moment).
- **I.2:** `img-004` — *"The SVG scales infinitely, yet remains exactly what it is…"* — direct fit (vector drawing's own scale-without-losing-identity property).
- **I.3:** `img-016` — *"The raster image fears the zoom…"* — direct fit (this unit's own anchor is bitmap/raster imagery).
- **I.4:** `arch-018` — *"Offset is not mathematics—it is empathy. You must remember what came before."* — analogical (its own `teaches` field is UI offset/positioning; disclosed fit: an effect is a transformation that should remember, not erase, its "before").
- **I.7:** `qa-011` — *"Free as in freedom… only proper attribution."* — analogical (its own `teaches` field is open-source licensing; disclosed fit: sourcing a reference asks the same attribution question).
- **I.8:** `img-002` — *"A GIF that loops forever teaches us: motion without movement is still life."* — direct fit (animation's own motion/stillness paradox).
- **I.9:** `img-070` — *"The way of the image is the way of balance…"* — direct fit (a bodegón is precisely a composition-of-balance exercise), despite the quote's own literal register being web-page image density.

## Hours — CD I's 80 h contact bucket now closes to 80/80

I.5/I.6 (forged in an earlier session) used 18 h of the 80 h contact-forgeable bucket (`clases_magistrales` 2 · `seminarios` 4 · `debates` 2 · `talleres_labs` 4 · `investigaciones_proyectos` 4 · `resolucion_problemas` 2 — verified live from `tracks.yml` before allocating, not assumed). This wave allocates the remaining 62 h across the seven units it forges:

| Unit | clases_magistrales | seminarios | debates | talleres_labs | investigaciones_proyectos | resolucion_problemas | total |
| --- | -: | -: | -: | -: | -: | -: | -: |
| I.1 | 2 | 3 | 1 | 2 | 3 | 1 | 12 |
| I.2 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.3 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.4 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.7 | 1 | 2 | 1 | 2 | 2 | 1 | 9 |
| I.8 | 1 | 2 | 0 | 1 | 2 | 0 | 6 |
| I.9 | 1 | 3 | 1 | 2 | 3 | 1 | 11 |
| **wave sum** | **8** | **16** | **6** | **10** | **16** | **6** | **62** |

Combined with I.5/I.6, CD I's `sessions_list` in `docs/_data/tracks.yml` now sums to **10 · 20 · 8 · 14 · 20 · 8 = 80 h** (`clases_magistrales` · `seminarios` · `debates` · `talleres_labs` · `investigaciones_proyectos` · `resolucion_problemas`), matching `oficial-guia-framework.mdc` §5's official activity table exactly — verified by direct arithmetic over the file, not assumed. **This closes the hour bucket; it does not close the pedagogical gap.** Seven of nine units still declare `NONE`, and I.1/I.7 are SAFE-but-narrow, not validated teaching methods — both track pages state this explicitly.

## Wiring

- `docs/_data/lessons.yml`: seven new entries (`i-1-imagenes-digitales`, `i-2-dibujo-2d`, `i-3-color-bitmaps`, `i-4-efectos`, `i-7-referencias-moda`, `i-8-animacion`, `i-9-bodegones`), same schema as the existing `i-5-forma-tridimensional`/`i-6-volumen` entries, appended after `i-6-volumen`.
- `docs/_data/tracks.yml`: seven new rows appended to `creacion-digital-i`'s `sessions_list` (was two rows, I.5/I.6, from the earlier wave); every contact-forgeable key present on each row, including the explicit `0` values on I.8's `debates`/`resolucion_problemas` — no key omitted, no zero silently dropped.
- Both `docs/tracks/{en,es}/{digital-creativity-i,creacion-digital-i}/index.md` Status sections rewritten to list all nine units with their evidence class in one line each, and to state the 80/80 hour closure alongside the pedagogical-completeness caveat. The "Official contents" and "Arc" sections are untouched from the prior session.

## Build

```bash
cd /Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem
JEKYLL_ENV=production npm run build 2>&1 | grep -i "liquid warning"
```

Result: **PASS (empty)**. Full build succeeded (39 HTML files normalized by `normalize-ids`; `mark-broken-links` reported no broken URLs). No `digital-creativity-pedagogy/` leak in `_site` (`find _site -iname "*digital-creativity-pedagogy*"` returns nothing). All fourteen new pages confirmed present at their built paths (`_site/lessons/{en,es}/{digital-creativity-i,creacion-digital-i}/{i-1…i-9}/index.html`). Spot-checked content survival: I.7's Campinho citation and `evaluator_safe` language intact (6 matches), I.9's `img-070`/synthesis framing intact (14 matches), I.8's `img-002`/"0 h" disclosure intact (15 matches), both track pages' "80/80" hour-closure statement present.

## Missing-evidence statements (one line each)

- **I.1:** digital-image *tool* pedagogy = NONE; Shinkle (2008) grounds the field-of-practices frame only, re-confirmed evaluator_safe=yes live.
- **I.2:** 2D-vector-drawing-tool pedagogy = NONE, full stop.
- **I.3:** colour/bitmap-editing pedagogy = NONE, full stop.
- **I.4:** digital-effects pedagogy = NONE, full stop.
- **I.7:** compositional-reference-*sourcing pedagogy* = `[UNVERIFIED-GAP]`; Campinho et al. (2025) is now genuinely evaluator_safe=yes (resolved from `[BIBLIO-GAP]`, not forced) but grounds image-sourcing representation-ethics only, never a sourcing method.
- **I.8:** digital-animation pedagogy = NONE; 0 h debates/resolución allocation is real and disclosed, not an oversight.
- **I.9:** bodegón-composition pedagogy = NONE; declared synthesis exercise across I.1–I.4, not new grounded technique.

## Milestone — and its limit

**After this wave, CD I's full nine-unit set has first-pass lesson content for the first time in this cascade, and CD I's 80 h contact bucket closes to 80/80 for the first time.** This is a real, verified milestone (checked, not assumed, by direct arithmetic over `tracks.yml`). It is **not** the same claim as CD I being pedagogically complete or teachable end-to-end: seven of nine units declare a genuine evidence gap, I.1 and I.7 are SAFE only for a narrow, disclosed claim each (a field-of-practices frame; an image-sourcing-ethics finding), no deck exists for any CD I unit (CD's forge contract does not require decks — Wave 5 in `fe-unit-forge.mdc`'s sense has no CD analogue), and no S1/S2 consent instrument applies to any CD I unit (ARTEFACT ROLE none throughout, a structural fact about CD I's CONTENIDOS anchors, not a per-unit choice).

## Remaining boundary

- `digital-creativity-pedagogy/grounding/README.md`'s I.7 matrix row still shows the historical `evaluator_safe=no` text — this session's live resolution is documented in `CD-WAVE-4.execute.md`'s header, not yet folded back into the matrix file itself. Flagged for a future matrix-maintenance pass, out of this wave's per-lesson scope.
- No research-consent administration, DPO approval, or research-data collection is implied by anything in this wave — no unit carries an S1/S2 template (ARTEFACT ROLE none throughout).
- No institution name was attached to any shared synergy in this wave — not applicable, since CD I carries no vShowroom-eligible anchors.
- This receipt does not claim any of the seven units' underlying pedagogical gaps are closed — 2D drawing, colour/bitmap editing, effects, animation, and bodegón-composition pedagogy all remain declared `NONE` by design; I.1's and I.7's SAFE citations are narrow and stated as such, per `dc-unit-forge.mdc`'s own non-negotiable that "a unit with no evidence says so."
- **Both CD I and CD II now have their full official-unit sets forged for the first time** (CD II closed in Wave 3, CD I closes in this wave) — a genuine two-course milestone for this cascade, stated here without inflating it into a claim about either course's classroom readiness.
