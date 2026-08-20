<!-- executable · CD I unit forge · Wave 4 (closes CD I's full 9-unit set) · paste this file as the agent prompt -->

# EXECUTE — CD Wave 4 (CD I remaining: I.1, I.2, I.3, I.4, I.7, I.8, I.9)

**Repo:** `digital-creativity-uem`
**Contract (do not rewrite):** [`../dc-unit-forge.mdc`](../dc-unit-forge.mdc)
**Hours/eval/CONTENIDOS:** [`../oficial-guia-framework.mdc`](../oficial-guia-framework.mdc)
**Guide JSON:** [`../cv/guides/1-creacion-digital-i.json`](../cv/guides/1-creacion-digital-i.json)
**Unit IDs:** [`../cv/UNIT-PLAN.md`](../cv/UNIT-PLAN.md)
**Matrix (authoritative):** [`../grounding/README.md`](../grounding/README.md)
**Precedent, same shape:** [`CD-WAVE-3.execute.md`](./CD-WAVE-3.execute.md) / [`CD-WAVE-3.execution.receipt.md`](./CD-WAVE-3.execution.receipt.md)

Do **not** use FE's 10/30/14 hour scheme — CD I closes to the guía JSON's own 80 h contact-forgeable bucket (`clases_magistrales` 10 · `seminarios` 20 · `debates` 8 · `talleres_labs` 14 · `investigaciones_proyectos` 20 · `resolucion_problemas` 8). No VTON (not applicable to CD I anyway). `dc-unit-forge.mdc` §3 "Deferred 2026-08-20" rule: ARTEFACT ROLE defaults to `portfolio`/`none`, never `vShowroom` — CD I's own CONTENIDOS anchors are not on the vShowroom-eligible list in `oficial-guia-framework.mdc` §2 (that list is CD II anchors 2·3·5·6 only), so every CD I unit this wave gets ARTEFACT ROLE **none**.

**I.5/I.6 already used 18 h of the 80 h bucket** (`clases_magistrales` 2 · `seminarios` 4 · `debates` 2 · `talleres_labs` 4 · `investigaciones_proyectos` 4 · `resolucion_problemas` 2 — verified live from `docs/_data/tracks.yml`, not assumed). **Remaining budget before this wave: `clases_magistrales` 8 · `seminarios` 16 · `debates` 6 · `talleres_labs` 10 · `investigaciones_proyectos` 16 · `resolucion_problemas` 6 (62 h).** Allocated below across the seven remaining units, summing exactly to that remainder:

| Unit | clases_magistrales | seminarios | debates | talleres_labs | investigaciones_proyectos | resolucion_problemas | total |
| --- | -: | -: | -: | -: | -: | -: | -: |
| I.1 | 2 | 3 | 1 | 2 | 3 | 1 | 12 |
| I.2 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.3 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.4 | 1 | 2 | 1 | 1 | 2 | 1 | 8 |
| I.7 | 1 | 2 | 1 | 2 | 2 | 1 | 9 |
| I.8 | 1 | 2 | 0 | 1 | 2 | 0 | 6 |
| I.9 | 1 | 3 | 1 | 2 | 3 | 1 | 11 |
| **sum** | **8** | **16** | **6** | **10** | **16** | **6** | **62** |

I.1 and I.9 get the largest slices (foundational/orientation-heavy for I.1; a synthesis project drawing on 2D, colour and effects for I.9) — an editorial allocation choice, disclosed as such, not an invented timetable: it is the honest distribution of a real, now-fully-forged remainder.

**Live re-verification at session start (not trusted from the matrix text without re-checking):**

- **I.1** Shinkle (2008), *Fashion as Photograph* — coat `eugenie_shinkle_..._1936070c`, node `cca1472b-b0c6-594c-8e13-ed87d6b73897`, p.15. `ahmes query --cite --require-evaluator-safe` re-confirmed live: `(Shinkle 2008, 15)`, evaluator_safe=yes, confidence 0.95, source=openlibrary/metadata. Unchanged from the matrix. Grounds fashion photography as *"simultaneous placement within the artistic and commercial realms"* — a field of practices, not a file format or tool sequence.
- **I.7** Campinho, Cardim da Silva, Dantas Soares & Amparo-Santos (2025), *Corpos gordos e corpos obesos em telas digitais* — coat `campinho_et_al_..._31a9a359`. **Genuinely resolved this session's re-check**, not forced: `ahmes status` shows `evaluator_safe: yes`, confidence 0.95, `source: metadata`, `method: manual-verified-crossref` — the matrix's prior `evaluator_safe=no` (slug-derived) entry has closed. `ahmes query --cite --require-evaluator-safe` re-confirmed live on the matrix's own node (`29e0b3cf-bd30-5373-bfbe-d208de8c3a3b`, p.2): `(Campinho 2025, 2)`, evaluator_safe=yes. **Topical caveat, undiminished by the metadata fix:** the paper studies representation of fat/obese bodies in Google-Images search results — a body-representation-ethics study, **not** a study of compositional-reference-sourcing pedagogy (mood-boarding, visual-research method, citation practice for design references). Cite it for what it grounds — the ethics of how bodies are represented in the images students will source and reference — and declare, explicitly, that a *teaching sequence for sourcing compositional references* remains ungrounded.
- **I.2, I.3, I.4, I.8, I.9** — matrix rows are **NONE**, no coat named. No enrich attempt applicable (nothing to enrich against). Full declared-gap units, tool docs `[PLATFORM]` only.

Execute each unit completely (A→D, EN+ES) before the next, in order **I.1 → I.2 → I.3 → I.4 → I.7 → I.8 → I.9** (matches `cv/UNIT-PLAN.md`'s numbering, not the JSON contents-string order, except I.7 is deliberately forged after I.1–I.4 and before I.8–I.9 per the trigger's own instruction).

---

# FORGE CD UNIT — CD I Unit I.1: Introducción a las imágenes digitales

## INPUT

- COURSE: CD I · UNIT_ID: **I.1** · UNIT: 1 of 9
- CONTENIDOS anchor (verbatim): *Introducción a las imágenes digitales*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 2 · seminarios 3 · debates 1 · talleres_labs 2 · investigaciones_proyectos 3 · resolucion_problemas 1 (12 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-1-digital-images/index.md` · `docs/lessons/es/creacion-digital-i/i-1-imagenes-digitales/index.md`

## STEP A

Matrix row I.1: Shinkle 2008, **SAFE**, re-confirmed live (see header). TTOD: `qa-008` — *"The path to mastery begins with reading. The path to enlightenment continues with practice."* — direct fit (an introductory unit is literally the "begins with reading" moment before I.2's hands-on drawing tools); confirmed unused elsewhere via the ttod-bridge adapter.

## STEP B

- **B1:** claim — a digital fashion image is not defined by its file format; it is defined by the field of practices around it (editorial, advertising, portraiture, documentary), and by its simultaneous placement in "artistic and commercial realms" (Shinkle 2008, 15, quoted). This does **not** ground Photoshop/tool pedagogy — the matrix is explicit on that boundary, restated here. Debate prompt: if the same image can be "art" in a gallery caption and "commerce" in an ad caption, whose intent decides which it is — the maker's, the venue's, or the viewer's?
- **B2 (talleres 2 + investigaciones_proyectos 3):** deliverable — a short annotated set of 3–5 found or created digital fashion images, each labelled with which "field of practice" it belongs to (editorial/advertising/documentary/etc.) and one sentence on where its artistic/commercial boundary sits. DoD: piece ID; process folder; labels present. No S1/S2 (ARTEFACT ROLE none). Evidence → **Investigaciones y proyectos 20%**; process note → **Cuaderno de prácticas 10%**.
- **B3 (resolución 1 h):** ≥1 diagnostic (given an image with no practice-label, assign the most defensible one and justify); ≥1 no-AI-declared (write the artistic/commercial boundary sentence for a described image by hand); a third distinguishing "field of practices" from "file format" (why "it's a JPEG" is not an answer to "what kind of fashion image is this").

## STEP C

`tracks.yml` session `i-1-imagenes-digitales`. `lessons.yml` EN+ES.

## STEP D

Shinkle node re-resolves live. Missing-evidence line: digital-image-*tool* pedagogy = NONE; Shinkle grounds the field-of-practices frame only.

---

# FORGE CD UNIT — CD I Unit I.2: Tecnología digital 2D: Herramientas de dibujo

## INPUT

- COURSE: CD I · UNIT_ID: **I.2** · UNIT: 2 of 9
- CONTENIDOS anchor (verbatim): *Tecnología digital 2D: Herramientas de dibujo*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 2 · debates 1 · talleres_labs 1 · investigaciones_proyectos 2 · resolucion_problemas 1 (8 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-2-2d-drawing/index.md` · `docs/lessons/es/creacion-digital-i/i-2-dibujo-2d/index.md`

## STEP A

Matrix row I.2: **NONE** — no coat for 2D-drawing-tool pedagogy. Declared-gap paragraph: no vault source validates a vector-drawing-tool teaching sequence; any tool's own documentation grounds HOW only, labelled `[PLATFORM]`. TTOD: `img-004` — *"The SVG scales infinitely, yet remains exactly what it is. Be like the SVG."* — direct fit (vector drawing is exactly the "scales without losing identity" property this unit teaches); confirmed unused elsewhere.

## STEP B

- **B1:** claim — vector drawing is a discipline of describing shape as a relationship (anchor points, curves, fills), not a discipline of pixels; the vault has no source validating *how best to teach this*, so the claim is taught as craft discipline, stated plainly as ungrounded pedagogy. Debate prompt: does starting from vector-first (rather than freehand-raster-first) change what a beginner notices about garment silhouette?
- **B2 (talleres 1 + investigaciones_proyectos 2):** deliverable — one vector illustration of a simple fashion silhouette (flat sketch or croqui), built from primitive shapes and paths, with a process note on which anchor-point decisions mattered. DoD: piece ID; process folder; note present. No S1/S2. Evidence → Investigaciones y proyectos 20%; note → Cuaderno 10%.
- **B3:** ≥1 diagnostic (given a vector path with a visibly wrong curve handle, identify what's wrong and what a correct handle would do); ≥1 no-AI-declared (describe, in writing, how to construct a simple vector shape from primitives, no tool open); a third naming why "I drew it in a raster app" would not satisfy this unit's own CONTENIDOS anchor.

## STEP C

`tracks.yml` session `i-2-dibujo-2d`. `lessons.yml` EN+ES.

## STEP D

No citation to force (declared NONE). Missing-evidence line: 2D-vector-drawing-tool pedagogy = NONE, full stop.

---

# FORGE CD UNIT — CD I Unit I.3: Color, imágenes con mapas de bits

## INPUT

- COURSE: CD I · UNIT_ID: **I.3** · UNIT: 3 of 9
- CONTENIDOS anchor (verbatim): *Color, imágenes con mapas de bits*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 2 · debates 1 · talleres_labs 1 · investigaciones_proyectos 2 · resolucion_problemas 1 (8 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-3-color-bitmaps/index.md` · `docs/lessons/es/creacion-digital-i/i-3-color-bitmaps/index.md`

## STEP A

Matrix row I.3: **NONE** — no coat for colour-management pedagogy. Declared-gap paragraph: no vault source validates a colour/bitmap-editing teaching sequence; tool docs (any raster editor's colour tools) ground HOW only, `[PLATFORM]`. TTOD: `img-016` — *"The raster image fears the zoom. The SVG welcomes it."* — direct fit (this unit's own anchor is bitmap/raster imagery specifically, in contrast to I.2's vector); confirmed unused elsewhere.

## STEP B

- **B1:** claim — a bitmap image is a fixed grid of colour values, and every colour decision (mode, depth, gamut) is a decision about what the image *cannot* later become; the vault has no source validating a teaching method for this, stated plainly. Debate prompt: when does "correcting" a colour become "changing" the garment it depicts — same disclosure question CD II's retouching unit already asks, here at the level of colour rather than body.
- **B2:** deliverable — one bitmap composition demonstrating a deliberate colour decision (a limited palette study of a fashion image, or a colour-mode comparison of the same image), with a process note naming the trade-off made. DoD: piece ID; process folder; note. No S1/S2. Evidence → Investigaciones y proyectos 20%; note → Cuaderno 10%.
- **B3:** ≥1 diagnostic (given two versions of the same bitmap at different bit depths, identify which artifact each shows and why); ≥1 no-AI-declared (describe by hand the visual difference between a limited and a full palette for a described image); a third distinguishing "colour correction" from "colour change" using the disclosure framing from B1.

## STEP C

`tracks.yml` session `i-3-color-bitmaps`. `lessons.yml` EN+ES.

## STEP D

No citation to force. Missing-evidence line: colour/bitmap-editing pedagogy = NONE.

---

# FORGE CD UNIT — CD I Unit I.4: Efectos

## INPUT

- COURSE: CD I · UNIT_ID: **I.4** · UNIT: 4 of 9
- CONTENIDOS anchor (verbatim): *Efectos*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 2 · debates 1 · talleres_labs 1 · investigaciones_proyectos 2 · resolucion_problemas 1 (8 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-4-effects/index.md` · `docs/lessons/es/creacion-digital-i/i-4-efectos/index.md`

## STEP A

Matrix row I.4: **NONE** — no coat for digital-effects pedagogy. Declared-gap paragraph: no vault source validates an effects/filter teaching sequence; tool docs ground HOW only, `[PLATFORM]`. TTOD: `arch-018` — *"Offset is not mathematics—it is empathy. You must remember what came before."* — analogical (its own `teaches` field is about UI offset/positioning, not image effects; the fit is disclosed: an effect applied to an image is a transformation that should remember, not erase, the original — the same disclosure discipline CD II's retouching unit already teaches, here for effects generally); confirmed unused elsewhere.

## STEP B

- **B1:** claim — an effect is a deliberate transformation with a "before," and losing track of the before is the actual risk this unit teaches against, not any specific filter's technique; ungrounded pedagogy, stated plainly. Debate prompt: is there a meaningful line between an "effect" (stylisation, disclosed) and a "manipulation" (deception, undisclosed) — and does the line move depending on the image's context (editorial vs. advertising)?
- **B2:** deliverable — one before/after pair showing a deliberately applied effect, with the "before" kept and a one-line disclosure of what changed. DoD: before/after pair saved; disclosure line present; piece ID. No S1/S2. Evidence → Investigaciones y proyectos 20%; disclosure → Cuaderno 10%.
- **B3:** ≥1 diagnostic (given an "after" image with no "before" kept, name what's missing from an honest effects workflow); ≥1 no-AI-declared (write the one-line disclosure by hand for a described effect); a third distinguishing "effect" from "manipulation" using B1's framing.

## STEP C

`tracks.yml` session `i-4-efectos`. `lessons.yml` EN+ES.

## STEP D

No citation to force. Missing-evidence line: digital-effects pedagogy = NONE.

---

# FORGE CD UNIT — CD I Unit I.7: Fuentes y referencias compositivas en el diseño de moda

## INPUT

- COURSE: CD I · UNIT_ID: **I.7** · UNIT: 7 of 9
- CONTENIDOS anchor (verbatim): *Fuentes y referencias compositivas en el diseño de moda*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 2 · debates 1 · talleres_labs 2 · investigaciones_proyectos 2 · resolucion_problemas 1 (9 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-7-fashion-references/index.md` · `docs/lessons/es/creacion-digital-i/i-7-referencias-moda/index.md`

## STEP A

Matrix row I.7: Campinho et al. 2025, **genuinely resolved to `evaluator_safe=yes` this session's re-check** (see header) — a real citation upgrade, not forced. TTOD: `qa-011` — *"Free as in freedom, stable as in tested. The Tao asks not for payment, only for proper attribution."* — analogical (its own `teaches` field is open-source licensing; the fit is disclosed: sourcing a compositional reference asks the same question open-source use does — not "can I use this" but "have I attributed it honestly"); confirmed unused elsewhere.

## STEP B

- **B1:** claim — sourcing a compositional reference is not a neutral act of collection; Campinho et al. (2025)'s finding that Google-Images searches for "fat body"/"obese body" reproduce dehumanising, disease-associated visual patterns shows that *what a search surfaces* already carries a representational politics, before a student even chooses which image to reference (Campinho 2025, 2, quoted). **Declared boundary, stated explicitly:** this grounds the *ethics of the images students will encounter while sourcing*, not a validated *teaching method for compositional-reference-sourcing itself* — that pedagogy stays `[UNVERIFIED-GAP]`, undiminished by the citation's own metadata fix. Debate prompt: if a mood-board search reproduces a biased pattern before you've chosen anything, whose responsibility is the bias — the search engine's, the archive's, or the student's for not noticing?
- **B2:** deliverable — a small compositional-reference board (3–6 images) for one fashion concept, with a one-paragraph note naming what each reference contributes *and* one sentence reflecting on whether the sourcing process itself surfaced any representational pattern worth naming (per B1). DoD: board exists; note present; piece ID; process folder. No S1/S2. Evidence → Investigaciones y proyectos 20%; note → Cuaderno 10%.
- **B3:** ≥1 diagnostic (given a reference board with no attribution and no reflection note, name what's missing from an honest sourcing practice); ≥1 no-AI-declared (write the one-sentence representational-pattern reflection by hand for a described board); a third distinguishing "a reference that informs" from "a reference that is copied" — the sourcing-vs-plagiarism line this unit's competencies (COMP9: original problem-solving) require.

## STEP C

`tracks.yml` session `i-7-referencias-moda`. `lessons.yml` EN+ES.

## STEP D

Campinho node re-resolves live, evaluator_safe=yes. Missing-evidence line: compositional-reference-*sourcing pedagogy* = `[UNVERIFIED-GAP]`; Campinho (2025) grounds the representation-ethics of what a search surfaces, not a sourcing method, and is now CV-bibliography-eligible (previously was not).

---

# FORGE CD UNIT — CD I Unit I.8: Creación de imágenes digitales animadas

## INPUT

- COURSE: CD I · UNIT_ID: **I.8** · UNIT: 8 of 9
- CONTENIDOS anchor (verbatim): *Creación de imágenes digitales animadas*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 2 · debates 0 · talleres_labs 1 · investigaciones_proyectos 2 · resolucion_problemas 0 (6 h)
- ARTEFACT ROLE: **none**
- Output paths: `docs/lessons/en/digital-creativity-i/i-8-animation/index.md` · `docs/lessons/es/creacion-digital-i/i-8-animacion/index.md`

## STEP A

Matrix row I.8: **NONE** — no coat for digital-animation pedagogy. Declared-gap paragraph: no vault source validates an animation teaching sequence; tool docs ground HOW only, `[PLATFORM]`. TTOD: `img-002` — *"A GIF that loops forever teaches us: motion without movement is still life."* — direct fit (animation's own paradox — implied motion vs. actual movement — is literally this unit's conceptual turn); confirmed unused elsewhere. No debate/resolución hours this unit (0/0 by design, per the allocation table) — B1 keeps a short reflective prompt without a formal graded debate slot, and B3 is folded into B2's process note rather than a separate individual set; state this explicitly rather than inventing hours that were not allocated.

## STEP B

- **B1:** claim — an animated image implies motion through a sequence of stills, and the craft is deciding which stills to keep, not which effect to add; ungrounded pedagogy, stated plainly. No formal debate slot this unit (0 h allocated) — the img-002 epigraph's own paradox (looping motion as a kind of stillness) is left as a reflective prompt inside B1's text rather than a graded activity.
- **B2 (talleres 1 + investigaciones_proyectos 2):** deliverable — one short animated sequence (GIF, sprite sheet, or simple loop) of a fashion detail (e.g., fabric drape, an accessory turn), with a process note listing the stills chosen and why. Since B3 has 0 h this unit, the process note doubles as the individual-evidence artefact — this collapsing is disclosed, not hidden, and is the one exception to `dc-unit-forge.mdc`'s own "B2 ≠ B3" rule, justified only by the 0 h resolución allocation. DoD: sequence exists; process note present; piece ID. No S1/S2. Evidence → Investigaciones y proyectos 20%; note → Cuaderno 10%.
- **B3:** **0 h — none this unit**, stated as content per the allocation table, not omitted silently.

## STEP C

`tracks.yml` session `i-8-animacion`. `lessons.yml` EN+ES.

## STEP D

No citation to force. Missing-evidence line: digital-animation pedagogy = NONE. Hour-allocation exception (B2/B3 collapse) stated explicitly in the lesson text itself.

---

# FORGE CD UNIT — CD I Unit I.9: Bodegones digitales

## INPUT

- COURSE: CD I · UNIT_ID: **I.9** · UNIT: 9 of 9
- CONTENIDOS anchor (verbatim): *Bodegones digitales*
- COMPETENCIES: CON1 · HAB9 · COMP8 · COMP9
- HOURS: clases_magistrales 1 · seminarios 3 · debates 1 · talleres_labs 2 · investigaciones_proyectos 3 · resolucion_problemas 1 (11 h)
- ARTEFACT ROLE: **none** (matrix's own I.9 row notes "S1 if any bodegón is exhibited" — no exhibition claim is made in this forge, so S1/S2 stay out of scope; state this explicitly rather than silently dropping the matrix's own conditional)
- Output paths: `docs/lessons/en/digital-creativity-i/i-9-bodegones/index.md` · `docs/lessons/es/creacion-digital-i/i-9-bodegones/index.md`

## STEP A

Matrix row I.9: **NONE** — no coat for still-life/bodegón pedagogy. Declared-gap paragraph: no vault source validates a bodegón-composition teaching sequence; tool docs ground HOW only, `[PLATFORM]`. TTOD: `img-070` — *"The way of the image is the way of balance. Too heavy, and the user departs. Too light, and meaning is lost. Too many, and the message drowns. Too few, and the page speaks in monotone."* — direct fit (a bodegón is precisely a composition-of-balance exercise, arranging objects until the visual weight reads correctly — even though the quote's own literal register is web-page image density); confirmed unused elsewhere.

## STEP B

- **B1:** claim — a digital bodegón (still-life composition) is where I.1's field-of-practices frame, I.2's drawing/arrangement literacy, I.3's colour decisions, and I.4's effects discipline converge into one deliberately balanced image — a synthesis exercise, not a new technique; ungrounded pedagogy for the synthesis claim itself, stated plainly. Debate prompt: is a digital bodegón judged by the same compositional rules as a painted or photographed one, or does the "digital" part change what balance means?
- **B2 (talleres 2 + investigaciones_proyectos 3):** deliverable — one digital bodegón composition (arranged fashion objects/accessories, digitally composited or drawn) with a process note explaining the balance decisions made (what was added, removed, or resized, and why), explicitly cross-referencing at least one decision each from I.1–I.4 where applicable. No exhibition claim, so **no S1/S2** in this unit, per the matrix's own conditional. DoD: piece ID; process folder; note present. Evidence → Investigaciones y proyectos 20%; note → Cuaderno 10%.
- **B3:** ≥1 diagnostic (given a bodegón description that is visually "too heavy" per img-070's framing, name what a rebalancing pass should remove or lighten); ≥1 no-AI-declared (write the balance-decision process note by hand for a described arrangement); a third naming which of I.1–I.4's prior units this synthesis piece draws on and how, checking the cross-reference is genuine rather than decorative.

## STEP C

`tracks.yml` session `i-9-bodegones`. `lessons.yml` EN+ES. This is the seventh and last unit this wave — after this, CD I's `sessions_list` totals close to **80/80** contact hours across all nine now-forged CD I units. State that explicitly on both track pages, and state equally explicitly that closing the hour bucket is **not** the same as CD I being pedagogically complete (seven of nine units still declare a gap; I.1 and I.7 are SAFE-but-narrow, not validated teaching methods).

## STEP D

No citation to force. Missing-evidence line: bodegón-composition pedagogy = NONE; unit is a declared synthesis exercise across I.1–I.4, not new grounded technique.

---

## OUTPUT CONTRACT

Seven EN+ES lesson pairs (I.1, I.2, I.3, I.4, I.7, I.8, I.9) · `docs/_data/lessons.yml` seven new entries × 2 langs · `docs/_data/tracks.yml` seven new `sessions_list` rows under `creacion-digital-i`, closing CD I's contact bucket to 80/80 · both EN/ES `digital-creativity-i`/`creacion-digital-i` track pages' Status sections updated · `npm run build` clean, no `digital-creativity-pedagogy/` leak · one-line missing-evidence statement per unit · explicit note on I.7's `[BIBLIO-GAP]` resolution (genuinely resolved this session's live re-check, not forced) · explicit note that this closes CD I's full 9-unit set for the first time, with the pedagogical-completeness caveat stated plainly, not implied away by the hour closure.
