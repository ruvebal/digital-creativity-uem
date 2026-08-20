# CD II Unit II.5 execution receipt

**Executed:** 2026-08-20
**Contract:** `CD-II-II.5.execute.md`
**Unit:** II.5 — Maquetación, edición y creación de web y portfolio digital

## Starting state (found, not authored fresh, this session)

The two lesson pages (`docs/lessons/en/digital-creativity-ii/ii-5-web-portfolio/index.md`,
`docs/lessons/es/creacion-digital-ii/ii-5-web-portfolio/index.md`) already existed,
timestamped 2026-08-20 14:42–14:43 — inside the same window as an earlier
out-of-scope session's `FE-II-WAVE-2` work, not authored by this run. Both were
untracked (`git status`: `docs/lessons/` listed as untracked). Read in full before
touching anything, per this cascade's own discipline for pre-existing uncommitted
work. Verdict: **substantively complete** B1/B2/B3 content matching the execute
file's spec (CONTENIDOS anchor, competencies, learning outcomes, evaluation-weight
mapping, TTOD epigraph `qa-010`, unsigned S1/S2 inside B2, declared
`[UNVERIFIED-GAP]` on portfolio web UX, provenance HTML comments) — not a stub.
**Not done:** `docs/_data/lessons.yml` registration (file was literally `[]`, no
lesson registered at all, CD-wide), the `tracks.yml` `sessions_list` session
(was `[]`), and the two track pages still said `status: scaffold` / "pending"
with no link to the unit. No receipt existed. This is what this session actually
executed.

## What this session did

1. **Re-verified both citations live**, independently of the file's own
   provenance comments (a claim of prior verification is not itself
   verification):
   - `ahmes query --cite "scholar/documents/anwar_raza_marzouk_generative_ai_in_studio_based_fashion_education_slr_ejbm_2025_0598ec0e/extract/extraction.db:c9a17328-72f7-56c8-95bf-b9860b1067b8" --require-evaluator-safe` → `(Anwar, 2025, p. 1)`, `confidence=0.95 source=metadata evaluator_safe=yes`.
   - `ahmes query --cite "scholar/documents/rizzi_bertola_exploring_the_generative_ai_potential_in_the_fashion_design_process_2025_167816a4/extract/extraction.db:908f5339-781d-51cc-a803-47dfbf9c0677" --require-evaluator-safe` → `(Rizzi, 2025, p. 10)`, `confidence=0.95 source=metadata evaluator_safe=yes`.
   - Both pass. No vendor doc was promoted to `(Author Year)` form; the file's
     declared `[UNVERIFIED-GAP]` on portfolio web-UX evidence is preserved
     as-is (not touched — it is still true; nothing in this session's Item 3
     work bears on II.5).
2. **Registered the lesson** in `docs/_data/lessons.yml` (previously empty
   `[]` for the whole repo, not just this unit) with `slug`, bilingual
   `title`/`path`/`file`, `status: draft` both languages, `type: lesson` —
   schema copied from FE's working `lessons.yml` (this repo had no prior
   entry to pattern-match against).
3. **Wired one `tracks.yml` session** under `slug: creacion-digital-ii` →
   `sessions_list` (previously `[]`), using the execute file's own suggested
   row verbatim: `clases_magistrales: 2, seminarios: 3, debates: 1,
   talleres_labs: 3, proyectos: 4, resolucion_problemas: 1` — sums to the
   contracted 14 h. No other unit's hours were allocated; course-level
   `formative_hours` unchanged (still closes at 150).
4. **Updated both track pages**
   (`docs/tracks/{en,es}/{digital-creativity-ii,creacion-digital-ii}/index.md`)
   and their `tracks.yml` status block from `scaffold` to `draft`, per
   `dc-unit-forge.mdc` §STEP C ("status leaves scaffold only when B1–B3
   exist") and the execute file's own boundary ("first unit present"; do not
   claim the course is teachable end-to-end). Each page now links to the
   II.5 lesson and states explicitly that the other five CD II units are
   still pending.

## Build

```bash
cd /Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem
JEKYLL_ENV=production npm run build 2>&1 | grep -i "liquid warning"
```

Result: **PASS (empty)**. Full build: Jekyll generated the site, `postcss:build`
succeeded, `normalize-ids` normalized 11 files, `mark-broken-links` reported no
broken URLs or error files. Verified `_site/digital-creativity-pedagogy` does
**not** exist (no leak of the authority/research tree onto the published site —
`PUBLISHING.md`'s own gate). Spot-checked both built pages
(`_site/lessons/en/digital-creativity-ii/ii-5-web-portfolio/index.html`,
`_site/lessons/es/creacion-digital-ii/ii-5-web-portfolio/index.html`) — both
contain their provenance/evidence-gate section and the B2 `.portfolio-piece`
template markup intact, confirming no Liquid deletion inside fences.

## Missing-evidence statement (one line)

**Fashion-portfolio web UX pedagogy = NONE / `[UNVERIFIED-GAP]`.** The unit
grounds *why* process and authorship must be visible (Anwar 2025; Rizzi &
Bertola 2025 — both `evaluator_safe=yes`); it does not, and does not claim to,
ground *which* layout/accessibility patterns get a portfolio seen or hired.
HTML/CSS guidance in B1 is labelled professional craft advice, not research
evidence.

## Remaining boundary

- Five of six CD II units (Retoque, Avatares, Experiencias, Vídeo,
  Hologramas/AR) remain unforged — Wave 3 per `dc-unit-forge.mdc` §4.
- The course is not teachable end-to-end; the track pages say this explicitly
  now rather than implying completeness via a status flip.
- No DPO approval, signed consent, or public vShowroom exhibition is implied
  by the unsigned S1/S2 templates embedded in B2 — they remain drafts.
- This receipt verifies the publication/build gate and the wiring this
  session added. It does not re-litigate the B1–B3 prose's own pedagogical
  judgment calls (e.g. the choice of "calidad profesional" as the quality
  bar) — those were authored by the earlier session and are represented
  here as found, not re-derived.
