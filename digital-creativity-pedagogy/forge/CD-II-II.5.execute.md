<!-- executable · CD II unit forge · Wave 1 · paste this file as the agent prompt -->

# EXECUTE — CD II Wave 1 (UNIT_ID II.5)

**Repo:** `digital-creativity-uem`  
**Contract (do not rewrite):** [`../dc-unit-forge.mdc`](../dc-unit-forge.mdc)  
**Hours/eval/CONTENIDOS:** [`../oficial-guia-framework.mdc`](../oficial-guia-framework.mdc)  
**Guide JSON:** [`../cv/guides/3-creacion-digital-ii.json`](../cv/guides/3-creacion-digital-ii.json)  
**PDF:** https://universidadeuropea.es/myfiles/pr/9729001108.pdf (2025-2026)  
**Unit IDs:** [`../cv/UNIT-PLAN.md`](../cv/UNIT-PLAN.md)  
**Matrix (authoritative over harvest demo):** [`../grounding/README.md`](../grounding/README.md)  
**Consent (unsigned templates only):** [`../consent/S-SET.md`](../consent/S-SET.md) · [`../consent/README.md`](../consent/README.md)

This file is the filled master prompt. The `.mdc` is the procedure. Do not use FE 10/30/14. Do not forge CD I in this run. Do not invent the remaining 66 h timetable.

---

# FORGE CD UNIT — CD II Unit II.5: Web y portfolio

## INPUT

- COURSE: CD II
- UNIT_ID: **II.5**
- GUIDE_JSON: `digital-creativity-pedagogy/cv/guides/3-creacion-digital-ii.json`
- UNIT: 5 of 6 CONTENIDOS anchors
- CONTENIDOS anchor (verbatim): Maquetación, edición y creación de web y portfolio digital
- COMPETENCIES (subset of JSON): CON1 · HAB10 · COMP8 · COMP9
- Learning-outcome bullets this unit may serve (JSON `learning_outcomes`, do not invent extras):  
  «Maquetar proyectos y trabajos de diseño con calidad profesional.» · «Diseñar estrategias creativas de comunicación digital en empresas de moda.» · «Manejar formatos de archivo digitales propios y genéricos.»
- MODALITY: Modalidad presencial
- HOURS this unit (slice of the 80 h contact bucket; remaining sessions stay empty):

| key | h | running leftover after this unit |
| --- | -: | --- |
| `clases_magistrales` | 2 | 8 of 10 |
| `seminarios` | 3 | 17 of 20 |
| `debates` | 1 | 7 of 8 |
| `talleres_labs` | 3 | 11 of 14 |
| `proyectos` | 4 | 16 of 20 |
| `resolucion_problemas` | 1 | 7 of 8 |

Contact this unit: **14 h**. Do not emit `investigaciones_proyectos` (CD I name). Do not allocate `trabajo_autonomo` / `tutoria` / `pruebas` on the session.

- ARTEFACT ROLE: **portfolio** — a public-ready page *may* later ingest to vShowroom (L3). L3 does not rewrite the CONTENIDO. Exhibition is **not** live in this run.
- COHORT: UEM Grado en Comunicación y Gestión de Moda · S2 · n ≈ (leave blank if unknown)
- Output paths (create; none exist yet):
  - `docs/lessons/en/digital-creativity-ii/ii-5-web-portfolio/index.md`
  - `docs/lessons/es/creacion-digital-ii/ii-5-web-portfolio/index.md`
- Register in `docs/_data/lessons.yml`
- Track pages: `docs/tracks/en/digital-creativity-ii/index.md` · `docs/tracks/es/creacion-digital-ii/index.md`

Frontmatter pattern (emancipation = hc-app-design): `layout: lesson`, `lang`, `permalink` `/lessons/en/digital-creativity-ii/ii-5-web-portfolio/` and `/lessons/es/creacion-digital-ii/ii-5-web-portfolio/`, bilingual `title` / `title_es` (or ES file `title_en`), `status: draft`, `author: Rubén Vega Balbás, PhD`. TOC fence as other lessons in that layout. Pages must not leak `digital-creativity-pedagogy/`.

## STEP A — GROUND BEFORE WRITING

1. Open GUIDE_JSON + framework. Confirm the anchor and competency codes exist. Hour/weight claims cite the **PDF URL + page**, not Ahmes.
2. Open matrix row **II.5**. That row beats the 2026-08-11 harvest demo. Do not paste the T1 index-page quote.
3. Re-open nodes. Cite `⟨coat⟩ · nodo ⟨id⟩ · p. ⟨n⟩`. Matrix names (verify):
   - Anwar, Raza & Marzouk 2025 · `anwar_raza_marzouk_…_0598ec0e` · nodo `c9a17328-72f7-56c8-95bf-b9860b1067b8` · p.0 · `(Anwar 2025, 1)` · `evaluator_safe=yes` — **authorship / studio GenAI**, not web UX.
   - Rizzi & Bertola 2025 · `rizzi_bertola_…_167816a4` · nodo `908f5339-781d-51cc-a803-47dfbf9c0677` · p.9 · `(Rizzi 2025, 10)` · `evaluator_safe=yes` — human–AI co-creation as complement.
4. **Declared gap (mandatory paragraph):** fashion-portfolio *web UX* / which layout-a11y patterns hire = NONE / `[UNVERIFIED-GAP]` on the field map. HTML/CSS/tool docs ground HOW only.
5. vShowroom: Web Atelier `frontend-pedagogy/atelier-synergy-vshowroom.mdc`. Attach **unsigned** S1/S2 checklists inside B2 (copy the boxes, do not publish the consent folder, do not claim DPO approval). C-set is **off** — teacher does not collect research data.
6. VTON / try-on is out of scope.

## STEP B — EMIT THREE ARTEFACTS (EN + ES)

### B1 · Conceptual (magistral 2 + seminarios 3 + debates 1)
- One-sentence claim: process and authorship must be visible on the portfolio page; polish without a trail is not the learning outcome.
- CONTENIDOS + competencies + eval weights quoted from framework §6 (presencial: pruebas 55 · informes 15 · caso 20 · proyectos 10).
- Anwar + Rizzi as WHY visibility; gap paragraph on UX-as-research.
- Debate prompt: what counts as “the work” when a look was co-made with a generator.
- Speaker outline ≤ 12 claims. No reveal.js in this run.

### B2 · Studio (talleres 3 + proyectos 4)
- Deliverable: one portfolio page (or small static site) that maquetas the student’s own CD work with process trail + AI-use declaration. Quality bar = JSON «calidad profesional», not a FE meta-framework course.
- Definition of done: page exists locally; piece ID; process folder; unsigned S1/S2 attached *if* they want exhibition later. Public showroom URL is **not** required.
- Evidence maps to evaluation **Proyectos** (10%) and can feed **Informes y escritos** (15%) — say so; do not invent a fourth weight.
- Tool docs dated; labelled Excerpt / Template (no CodeSandbox-ready unless a complete static file really runs).

### B3 · Resolución de problemas (1 h) — INDIVIDUAL
3–5 short problems **not** the portfolio: broken semantic HTML, missing alt/attribution, a generator prompt that erases authorship. ≥1 diagnostic. ≥1 solvable without AI, declared. Professor expected-answer sketch not on the student page.

## STEP C — WIRE IT

Add **one** session to `docs/_data/tracks.yml` under `slug: creacion-digital-ii` → `sessions_list` (today it is `[]`). Every contact-forgeable key present, including zeros if unused — **do not omit keys**. Suggested row:

```yaml
sessions_list:
  - title: 'II.5 Web y portfolio'
    slug: 'ii-5-web-portfolio'
    unit_id: II.5
    clases_magistrales: 2
    seminarios: 3
    debates: 1
    talleres_labs: 3
    proyectos: 4
    resolucion_problemas: 1
```

Course-level `formative_hours` stay 150. Leave all other units unallocated. Track `status` may move off `scaffold` only for “first unit present”; do not claim the course is teachable end-to-end. Evaluation sentences on the track must match framework §6.

## STEP D — VERIFY

```bash
npm run build
# no leak of digital-creativity-pedagogy/ into _site
```

Hour keys ⊆ CD II presencial set. CONTENIDOS + competencies ⊆ JSON. Nodes resolve. One-line missing-evidence statement: **portfolio web UX pedagogy = NONE**.

## OUTPUT CONTRACT

EN lesson · ES lesson · `lessons.yml` · one `tracks.yml` session · unsigned S1/S2 inside B2 · missing-evidence line. No DPO pack on Pages. No CD I files. No remaining-hour fiction.
