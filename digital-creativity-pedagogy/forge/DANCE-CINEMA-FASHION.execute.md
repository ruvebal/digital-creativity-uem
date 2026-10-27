# EXECUTE — Dance–Cinema–Fashion masterclass series

**Run state:** prefilled instructor research scaffold; not release-ready. **Forge:** [DANCE-CINEMA-FASHION-FORGE.mdc](./DANCE-CINEMA-FASHION-FORGE.mdc). **Spine:** [dance-cinema-fashion-MAIN-IDEAS.yml](./session-prompts/dance-cinema-fashion-MAIN-IDEAS.yml). **Evidence:** [source and media ledger](./DANCE-CINEMA-FASHION-SOURCE-MEDIA-LEDGER.md).

## Operator brief

Build a critical field map for DC I: garments enable, extend, constrain, shape and stage movement; media, history and power shape its meaning. The provisional six moves are (1) moving dressed body and contested classical peplos revival, (2) Fuller, Duncan, central Schlemmer and Graham as choreographic costume systems, (3) Astaire and partners, screen framing/editing and stardom, (4) stage-to-fashion circulation and documented or contested transfer, including specific Ibero-American and non-Western evidence, (5) the limits of abjection through Delfín, Ana Locking and Matières Fécales as bounded case leads, and (6) butoh histories, affect and transnational reception. Reorder or narrow as evidence dictates. Do not present a single continuous genealogy or invent products.

Read the project's official guide PDF and JSON, unit plan, I.7/I.8 lessons and registry; then the named session, rhythm, slideshow, image-analysis and critical field forges. I.7 is the principal anchor; I.8 only for actual digital animation. Use the same analysis guide, two ordinary-unit Lab exercises, prescribed Workshop timing and existing assessment. Class count is unresolved pending real unit architecture; do not allocate hours or force two sessions.

Search `runs/dance-fashion-abject-butoh/20261027/pass1.raw.md` and `image-search-report.md` under the Profield research home as discovery only. Report: 26 candidates in ten nonempty searches; multiple false matches; none accepted or published. Triadic Ballet: three later Wilkins reconstruction photos marked CC0, one Stuttgart museum-display photo CC BY 2.0, and Feist's photograph CC BY-SA 4.0 (not the manifest's “public domain”); all need full rights review. Never identify any of these as a 1922 premiere photograph.

LIFE article: https://www.life.com/arts-entertainment/fred-astaire-the-dance-legend-is-about-to-be-discovered-all-over-again/ is a research pointer and possible instructor reading, not licensed visual material. No iframe, screenshot, thumbnail, downloaded image or derivative without current explicit permission; a separate link only if terms and project rules permit, otherwise direct navigation. Supply an accessible course-generated diagram or accepted asset instead.

## Exact outputs and boundaries

1. Focused reusable `.mdc` forge.
2. This ready-to-run `.execute.md` brief.
3. Instructor-only `MAIN-IDEAS.yml`: at most six, each with bounded source-backed claim, cases, visual need, critical tension, question.
4. Private source/media ledger: sources by claim, separate factual and interpretive status, open questions, all discovery/review and rights statuses, fallbacks and dates.

Do not produce a deck, lesson, assessment, media pack or publish anything in this run. A later production request must first repair unresolved PDF and Ahmes gates, review assets, obtain the owner release required by the publication workflow, and run build, publication and citation checks.

## Run receipt — 2026-10-27

Skills applied: `ground-with-athanor-ahmes` and project-local `curriculum-publication-head`. The latter's promotion and sync receipt gate is deferred because this is an explicitly unpublished research scaffold, not a promotion. Project forges are documents, not claimed studio skills. FieldSpecs and AI evidence harness read. Scoped Athanor search attempted for `profield-digital-creativity` / scholar, query `dance costume fashion movement choreography`; local database connection was denied, so no hits or nodes were verified. Web source records checked as research evidence only; all proposed classroom scholarly citations await complete Ahmes page and resolver checks. Live official PDF could not be accessed; JSON is a previously reconciled clone, so PDF comparison remains open. No shared database injection or source promotion.

**Validation:** `npm run build --ignore-scripts` passed on 2026-10-27, including Jekyll, publication, citation and NM campaign gates; prebuild generators were deliberately skipped to avoid changing unrelated curriculum. Deck validation reported 167 existing rights/cache warnings, no errors. Publication and citation gates also passed independently. Six-idea YAML structure and required fields passed; `git diff --check` passed. These site gates do not certify the new private research claims or media rights.

## Run 2 receipt — production, 2026-10-27 (class 2026-10-28, 08:30)

**Owner instruction overrides the run-1 "no teaching pages" boundary.** The professor asked in session to review and repair the grounding layer, then forge and run the cycle on branch `forge/dance-cinema-fashion`, with embedded video, images, course graphics and in-class phone-camera + Photoshop/Firefly prompts.

**Produced (on branch, not merged, not published):**
- `docs/lessons/en/master-lectures/dance-cinema-fashion/` (EN canonical) and `docs/lessons/es/master-lectures/danza-cine-moda/` (ES twin, class language). Registered in `lessons.yml` (ML-DCF) and the master-lectures index.
- 5 public-domain films self-hosted as silent H.264 MP4 (14 MB): Muybridge 1887 loop, Edison/Annabelle 1894, Lumière 1897, Pathé 1902 copy coloured by Segundo de Chomón, Chomón *Création de la serpentine* 1908 (uploader-added soundtrack stripped). 23 Commons images (PD or CC BY / BY-SA with credit). 5 course diagrams × EN/ES from `forge/scripts/dance_cinema_fashion_graphics.py`.
- Copyrighted works are **not** embedded: *Top Hat* (instructor plays a licensed copy), *Admiring La Argentina* (link to Numeridanse / Maison de la Danse record). No LIFE material used.
- Lab = exactly two exercises (C1–C5 capture menu; T1–T5 transform menu + mandatory AI audit) with consent guard and AI declaration. Two-exercise rule respected; prompts are menus inside them.

**Rule tension, flagged to owner:** CLAUDE.md hard rule 1 ("no cloud AI in teaching materials"). Materials contain no generated imagery; students use Adobe Firefly / Photoshop generative features under their own Creative Cloud licence at the professor's explicit request. Declared in the public Editorial note. Owner should confirm or amend rule 1.

**Session placement:** proposed 120′ (Analysis 15 → Masterclass 40 → Lab opener 5 → Ex1 25 → Ex2 25 → share 10). No Workshop block: if this falls in session ≥ 4, cut Ex2 to T1 + audit and give the last 20′ to D2/D3. Registry hours untouched.

**Grounding (see ledger §Grounding review):** Athanor reachable this run (run 1: DB denied). 19 scoped queries over `profield-digital-creativity`, `profield-nuevos-medios-moda-2026-27`, `scholar-ai-criticism`, `profield-dc-3d-form-volume-pedagogy`. 20 candidate nodes read in full; 12 used publicly with printed folios read from the PDFs; 4 kept as `[BIBLIO-GAP]`. S1–S15 still outside the vault.

**Validation:** `npm run build --ignore-scripts` → Jekyll OK, decks 0 errors / 167 existing warnings, publication safety passed, citation conformance passed, NM campaigns passed. `render-decks --check` 0 stale. Browser check (static `_site`): 22/22 images load, 5/5 films load and play, all `#ref-` anchors resolve, no horizontal scroll at 375 px. `verify_printed_folios.py`: 0 mismatches in edited lessons; 2 remaining (MacCallum and Widdows 2018; Anwar, Raza, and Marzouk 2025) queued, not auto-fixed.
