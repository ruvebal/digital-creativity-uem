<!-- executable · CD I unit forge · Wave 2 · paste this file as the agent prompt -->

# EXECUTE — CD I Wave 2 (UNIT_ID I.5, I.6)

**Repo:** `digital-creativity-uem`
**Contract (do not rewrite):** [`../dc-unit-forge.mdc`](../dc-unit-forge.mdc)
**Hours/eval/CONTENIDOS:** [`../oficial-guia-framework.mdc`](../oficial-guia-framework.mdc)
**Guide JSON:** [`../cv/guides/1-creacion-digital-i.json`](../cv/guides/1-creacion-digital-i.json)
**PDF:** https://universidadeuropea.es/myfiles/pr/9729001103.pdf (2026-27)
**Unit IDs:** [`../cv/UNIT-PLAN.md`](../cv/UNIT-PLAN.md) — Wave 2 as planned there ("First forge: II.5 … then I.5/I.6 (volume)")
**Matrix (authoritative over harvest demo):** [`../grounding/README.md`](../grounding/README.md) — I.5/I.6 rows upgraded 2026-08-20 from NONE to SAFE (course-structure / hybrid-studio pedagogy), sourced from field run `dc-3d-form-volume-pedagogy` (`~/src/profield/runs/dc-3d-form-volume-pedagogy/20260820/digest.md`, Pass-3-confirmed rows), resolved to `evaluator_safe=yes` Ahmes citations same session.
**Precedent, same shape:** [`CD-II-II.5.execute.md`](./CD-II-II.5.execute.md) / [`CD-II-II.5.execution.receipt.md`](./CD-II-II.5.execution.receipt.md)

This file is the filled master prompt for both units in one wave (same
pattern FE used for `FE-II-WAVE-2.execute.md`: one `FORGE CD UNIT` block per
unit, executed in order, each complete A→D before the next). Do not use FE
10/30/14. Do not forge CD II in this run. Do not invent the remaining 62 h of
CD I's 80 h contact bucket — only I.5 and I.6 get session rows this wave.

**Transfer boundary named explicitly by `UNIT-PLAN.md`'s 2026-08-16 audited
promotion note:** "I.5/I.6: 3D-form and volume research supports a cautious
spatial-literacy strand; generic mesh/CSG pedagogy is not silently
transferred to fashion." Both citations below are fashion-education-specific
case studies — not general CAD/3D-printing pedagogy imported without
warrant — confirming this note rather than overriding it.

---

# FORGE CD UNIT — CD I Unit I.5: Forma tridimensional

## INPUT

- COURSE: CD I
- UNIT_ID: **I.5**
- GUIDE_JSON: `digital-creativity-pedagogy/cv/guides/1-creacion-digital-i.json`
- UNIT: 5 of 9 CONTENIDOS anchors
- CONTENIDOS anchor (verbatim): Fundamentos y representación de la forma tridimensional
- COMPETENCIES (subset of JSON): CON1 · HAB9 · COMP8 · COMP9
- Learning-outcome bullets this unit may serve (JSON `learning_outcomes`, do not invent extras):
  «Identificar los conceptos fundamentales de la forma tridimensional y su representación geométrica.» · «Reconocer las técnicas de representación tridimensional.»
- MODALITY: Modalidad presencial
- HOURS this unit (slice of the 80 h contact bucket; remaining 7 CD I units stay empty):

| key | h | running leftover after this unit |
| --- | -: | --- |
| `clases_magistrales` | 1 | 9 of 10 |
| `seminarios` | 2 | 18 of 20 |
| `debates` | 1 | 7 of 8 |
| `talleres_labs` | 2 | 12 of 14 |
| `investigaciones_proyectos` | 2 | 18 of 20 |
| `resolucion_problemas` | 1 | 7 of 8 |

Contact this unit: **9 h**. Use `investigaciones_proyectos` (CD I name), not `proyectos` (CD II name). Do not allocate `trabajo_autonomo` / `tutoria` / `pruebas` on the session.

- ARTEFACT ROLE: **none** — a 3D-form fundamentals exercise is not, by
  default, a portfolio or exhibition piece this wave. No S1/S2 attached; do
  not name vShowroom in this unit's content.
- COHORT: UEM Grado en Comunicación y Gestión de Moda · S1 · n ≈ (leave blank if unknown)
- Output paths (create; none exist yet):
  - `docs/lessons/en/digital-creativity-i/i-5-three-dimensional-form/index.md`
  - `docs/lessons/es/creacion-digital-i/i-5-forma-tridimensional/index.md`
- Register in `docs/_data/lessons.yml`
- Track pages: `docs/tracks/en/digital-creativity-i/index.md` · `docs/tracks/es/creacion-digital-i/index.md`

Frontmatter pattern (emancipation = hc-app-design): `layout: lesson`, `lang`, `permalink` `/lessons/en/digital-creativity-i/i-5-three-dimensional-form/` and `/lessons/es/creacion-digital-i/i-5-forma-tridimensional/`, bilingual `title` / `title_es` (or ES file `title_en`), `status: draft`, `author: Rubén Vega Balbás, PhD`. TOC fence as other lessons in that layout. Pages must not leak `digital-creativity-pedagogy/`.

## STEP A — GROUND BEFORE WRITING

1. Open GUIDE_JSON + framework. Confirm the anchor and competency codes exist. Hour/weight claims cite the **PDF URL + page**, not Ahmes.
2. Open matrix row **I.5**. Cite Ahmes nodes, not the digest's paraphrase or the 2026-08-11 harvest demo.
3. Re-open nodes. Cite `⟨coat⟩ · nodo ⟨id⟩ · p. ⟨n⟩`:
   - Papahristou, E., & Zolota Tatsi, N. 2024 · `cdatp_papachristou_20e79483` · nodo `88bcdad6-160b-5fab-a31e-848932abb7c3` · p.5 · `(Papahristou 2024, 5)` · `evaluator_safe=yes` — a real taught sequence (3D virtual prototyping at International Hellenic University, 3rd-year BA, sequenced after 2D CAD patternmaking, theory+lab split).
   - Same coat, nodo `a196bf7e-da78-5714-86df-7e196221f633` · p.3 · `(Papahristou 2024, 3)` · `evaluator_safe=yes` — Siersema's (2015) account of AMFI integrating 3D prototyping progressively across the curriculum.
4. **Declared gap (mandatory paragraph):** the same review (nodo p.1, DOI `10.25367/cdatp.2024.5.p266-277`) states its own reviewed studies report *tool-adoption* outcomes (efficiency, confidence, self-reported creativity), not validated measures of form/volume understanding. Ground *that a taught sequence exists and how one is structured*; do not imply the sequence is validated to produce spatial-form understanding.
5. vShowroom: **out of scope this unit** (ARTEFACT ROLE = none). Do not attach S1/S2.
6. VTON / try-on is out of scope.

## STEP B — EMIT THREE ARTEFACTS (EN + ES)

### B1 · Conceptual (magistral 1 + seminarios 2 + debates 1)
- One-sentence claim: 3D form is a spatial-reasoning skill that is taught in a sequence (2D → 3D prototyping), not a software feature students absorb by exposure.
- CONTENIDOS + competencies + eval weights quoted from framework §6 (presencial: pruebas 55 · caso/problema 15 · investigaciones y proyectos 20 · cuaderno taller 10).
- Papahristou as WHY a sequenced 2D→3D structure exists in practice; gap paragraph on validated learning-outcome measurement.
- TTOD epigraph: `wis-013` — "Practice in the dojo, perform in the arena." Used analogically (its own `teaches` field is DevOps-specific; the fit here is the practice/performance-context distinction between decontextualised B3 drills and the contextualised B2 studio piece) — flag the imperfect-fit honestly in the lesson or receipt, same discipline as FE Wave 2's `ops-001`.
- Debate prompt: is 3D virtual prototyping a *replacement* for physical model-making in learning to understand form, or a *different* representation that must be taught alongside it, not instead of it?
- Speaker outline ≤ 12 claims. No reveal.js in this run.

### B2 · Studio (talleres 2 + investigaciones_proyectos 2)
- Deliverable: a small sequence of 3D-form studies (sketch → primitive-volume study → simple digital 3D representation), mirroring the sequenced-teaching structure the citation describes — not a finished garment.
- Definition of done: piece ID, process folder (sketch + intermediate + final), one-paragraph reflection naming what changed between the 2D and 3D representation.
- Evidence maps to evaluation **Investigaciones y proyectos** (20%) and can feed **Cuaderno de prácticas de laboratorio/taller** (10%) — say so; do not invent a fifth weight.
- Tool docs dated; labelled Excerpt / Template.

### B3 · Resolución de problemas (1 h) — INDIVIDUAL
3–5 short problems isolating spatial-form reasoning from software operation: identify which of several 2D projections could/could not fold into a stated 3D volume; spot a form/volume error in a rendered mock-up; describe (without any tool) how a flat pattern piece becomes a rounded form. ≥1 diagnostic. ≥1 solvable without any digital tool, declared. Professor expected-answer sketch not on the student page.

## STEP C — WIRE IT

Add **one** session to `docs/_data/tracks.yml` under `slug: creacion-digital-i` → `sessions_list`. Every contact-forgeable key present:

```yaml
sessions_list:
  - title: 'I.5 Forma tridimensional'
    slug: 'i-5-forma-tridimensional'
    unit_id: I.5
    clases_magistrales: 1
    seminarios: 2
    debates: 1
    talleres_labs: 2
    investigaciones_proyectos: 2
    resolucion_problemas: 1
```

Course-level `formative_hours` stay 150. Evaluation sentences on the track must match framework §6.

## STEP D — VERIFY

```bash
npm run build
# no leak of digital-creativity-pedagogy/ into _site
```

Hour keys ⊆ CD I presencial set. CONTENIDOS + competencies ⊆ JSON. Nodes resolve. One-line missing-evidence statement: **3D-form learning-outcome validation = NONE; taught-sequence structure = SAFE.**

---

# FORGE CD UNIT — CD I Unit I.6: Volumen

## INPUT

- COURSE: CD I
- UNIT_ID: **I.6**
- GUIDE_JSON: `digital-creativity-pedagogy/cv/guides/1-creacion-digital-i.json`
- UNIT: 6 of 9 CONTENIDOS anchors
- CONTENIDOS anchor (verbatim): Volumen
- COMPETENCIES (subset of JSON): CON1 · HAB9 · COMP8 · COMP9
- Learning-outcome bullets this unit may serve: «Diferenciar los diferentes recursos técnicos para realizar modelos digitales tridimensionales.» · «Reconocer las técnicas de representación tridimensional.»
- MODALITY: Modalidad presencial
- HOURS this unit (slice of the 80 h contact bucket; running total after I.5+I.6):

| key | h (I.6) | running leftover after I.5+I.6 |
| --- | -: | --- |
| `clases_magistrales` | 1 | 8 of 10 |
| `seminarios` | 2 | 16 of 20 |
| `debates` | 1 | 6 of 8 |
| `talleres_labs` | 2 | 10 of 14 |
| `investigaciones_proyectos` | 2 | 16 of 20 |
| `resolucion_problemas` | 1 | 6 of 8 |

Contact this unit: **9 h**. Same key set as I.5. Do not allocate `trabajo_autonomo` / `tutoria` / `pruebas` on the session.

- ARTEFACT ROLE: **none** (same reasoning as I.5).
- COHORT: UEM Grado en Comunicación y Gestión de Moda · S1 · n ≈ (leave blank if unknown)
- Output paths (create; none exist yet):
  - `docs/lessons/en/digital-creativity-i/i-6-volume/index.md`
  - `docs/lessons/es/creacion-digital-i/i-6-volumen/index.md`
- Register in `docs/_data/lessons.yml`
- Track pages: same as I.5 (both units land on the same CD I track page)

## STEP A — GROUND BEFORE WRITING

1. Open GUIDE_JSON + framework. Confirm anchor + competencies. Hour/weight claims cite the PDF, not Ahmes.
2. Open matrix row **I.6**. Cite:
   - Coats, M. 2026, "The Denim project – a hybrid approach to fashion education using CLO3D," *IJFDTE*, DOI `10.1080/17543266.2026.2688308` · `the_denim_project_a_hybrid_approach_to_fashion_education_using_clo3d_6d1a7b81` · nodo `b3ded30f-381e-5425-80b1-cf125b52449f` · p.8 · `(Coats 2026, 8)` · `evaluator_safe=yes` — a hybrid analogue/digital garment module explicitly framed as constructivist experiential learning (Biggs & Tang 2011; Kolb 1984), students iterating between physical muslin and CLO3D to build garment volume.
3. **Declared gap (mandatory paragraph):** single case study, one cohort, one module — not evidence of a generalisable method, and CLO3D-specific (do not extend to other volume tools without new evidence). The same paper's sustainability critique (nodo `e4ea7122-7e03-5c1e-b82d-0416b553bc7b`, p.4) is a caveat on the *tool*, not on the pedagogy — usable as a discussion prompt, not as pedagogy evidence; do not blur the two.
4. vShowroom: **out of scope this unit** (ARTEFACT ROLE = none).
5. VTON / try-on is out of scope.

## STEP B — EMIT THREE ARTEFACTS (EN + ES)

### B1 · Conceptual (magistral 1 + seminarios 2 + debates 1)
- One-sentence claim: volume is built by iterating between physical and digital representations, not by picking one and discarding the other.
- CONTENIDOS + competencies + eval weights (same table as I.5).
- Coats 2026 as WHY a hybrid analogue/digital iteration model is a real, theorised teaching approach; gap paragraph on generalisability beyond one CLO3D case study.
- TTOD epigraph: `qa-013` — "To bump wisely is to keep truth in two places: the manifest and the module." Used analogically for keeping the physical maquette and the digital CLO3D pass in sync through iteration (its own `teaches` field is about software version sync across sources of truth — an imperfect fit, flagged honestly, same as `wis-013` above and FE Wave 2's `ops-001` precedent). Confirmed unused elsewhere in this repo and in FE II before selection.
- Debate prompt: Coats's own sustainability caveat — does reducing physical sampling waste via CLO3D risk normalising faster, more disposable design cycles? Reuse this directly, it is the paper's own critique of its own method.
- Speaker outline ≤ 12 claims.

### B2 · Studio (talleres 2 + investigaciones_proyectos 2)
- Deliverable: one small garment-adjacent volume study built by iterating between a physical maquette/muslin pass and a digital 3D representation — mirroring Coats's hybrid workflow structurally, at CD I's introductory scale (not a full garment).
- Definition of done: piece ID, process folder documenting at least one physical→digital→physical (or reverse) iteration, one-paragraph reflection on what each representation revealed that the other didn't.
- Evidence maps to **Investigaciones y proyectos** (20%), can feed **Cuaderno de prácticas** (10%).
- Tool docs dated; labelled Excerpt / Template.

### B3 · Resolución de problemas (1 h) — INDIVIDUAL
3–5 short problems: identify what a flat digital render cannot show about a volume that a physical (or rotating 3D) view can; given a described hybrid workflow, name which step is analogue and which is digital and why that choice was likely made; a no-tool sketch-reasoning problem about how draping changes with volume. ≥1 diagnostic. ≥1 solvable without any digital tool, declared.

## STEP C — WIRE IT

Add **one more** session to the same `sessions_list` (after I.5):

```yaml
  - title: 'I.6 Volumen'
    slug: 'i-6-volumen'
    unit_id: I.6
    clases_magistrales: 1
    seminarios: 2
    debates: 1
    talleres_labs: 2
    investigaciones_proyectos: 2
    resolucion_problemas: 1
```

Running total after both sessions: `clases_magistrales: 2/10 · seminarios: 4/20 · debates: 2/8 · talleres_labs: 4/14 · investigaciones_proyectos: 4/20 · resolucion_problemas: 2/8`. Remaining 7 CD I units stay unallocated — do not invent their timetable.

## STEP D — VERIFY

Same as I.5's STEP D. One-line missing-evidence statement: **volume-pedagogy generalisability beyond one CLO3D case study = NONE; hybrid analogue/digital teaching-module structure = SAFE.**

## OUTPUT CONTRACT

EN + ES lessons for I.5 and I.6 · `lessons.yml` (2 entries) · `tracks.yml` two sessions under `creacion-digital-i` · missing-evidence line per unit · no vShowroom naming · no VTON · no invented remaining-hour timetable for the other 7 CD I units.
