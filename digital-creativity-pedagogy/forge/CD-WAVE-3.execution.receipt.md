# CD Wave 3 execution receipt

**Executed:** 2026-08-20
**Contract:** `CD-WAVE-3.execute.md` (drafted this session, no prior version existed)
**Units:** II.1 — Retoque fotográfico avanzado de imágenes moda; II.2 — Creación de avatares; II.3 — Diseño de experiencias de moda digitales; II.4 — Recursos digitales de edición de vídeo; II.6 — Hologramas y R.A.

This wave completes CD II's six CONTENIDOS anchors — II.5 (portfolio/web) was already forged in an earlier session (Wave 1); this wave forges the remaining five, in the order the trigger specified: II.1 → II.2 → II.3 → II.4 → II.6.

## `[BIBLIO-GAP]` rows — what was genuinely re-verified, and what happened to each

Every citable claim in this wave was checked live via `ahmes status` and/or `ahmes query --cite --require-evaluator-safe` this session, not trusted from the matrix's existing text. Two rows the trigger flagged for a possible pipeline-lag fix were tested with a real `ahmes enrich --meta --online` attempt each — neither resolved:

| Unit | Coat | `ahmes status` before | Enrich attempted | Result | Disposition |
| --- | --- | --- | --- | --- | --- |
| II.1 | Ozimek-style, `10_1186_s40359_023_01143_0_…_4abbe095` | `Citation preview: [BIBLIO-GAP]`, reason "missing year" | Yes, live | 0 nodes enriched, no online registry match | **Genuine content gap, confirmed — stays `[BIBLIO-GAP]`.** Quoted in the lesson with the gap visible (appearance/social-comparison psychology, not a retouching curriculum); not entered into the CV bibliography. |
| II.2 | Rodríguez-Borlado & Pérez-Curiel 2024, `rodriguez_borlado_…_f711009d` | `evaluator_safe: no`, confidence 0.60 (source=slug) | Yes, live | "Host registry mismatch — identifiers only," 0 nodes enriched | **Genuine content gap, confirmed — stays `[BIBLIO-GAP]`.** Quoted with the gap visible (anthropomorphism mechanism, not a CLO/avatar-modelling method); not CV-bibliography-eligible. |
| II.3 / II.6 | Kim 2023, `10_3389_fpsyg_2023_1276856_…_ddb20bc5` | (already SAFE per matrix) | Not needed | `(Kim 2023, 6)`, evaluator_safe=yes, confidence 0.95 | **Re-confirmed live, unchanged.** SAFE as phenomenon evidence only; II.6 reuses the same node explicitly as a stimulus-type parallel, not independent AR evidence — that boundary is stated in both units' evidence gates and in the matrix. |
| II.4 | — (matrix row is NONE) | n/a — no coat named | Not applicable | n/a | **No citation to force.** Full declared-gap unit; no enrich attempt was possible because there is no candidate source. |

**No `[BIBLIO-GAP]` row was resolved this wave.** Both candidates the trigger named as possibly fixable turned out, after a real attempt each, to be genuine content gaps — Ahmes's own host-registry-mismatch refusal (II.2) and its "no online match" outcome (II.1) are the same honesty mechanism CD I Wave 2 relied on when it rejected the Widiyawati coat; nothing here was forced. `digital-creativity-pedagogy/grounding/README.md` was updated with a short 2026-08-20 addendum recording this live re-verification (no matrix *values* changed — every disposition above matches what the matrix already said before this session).

## What each unit teaches, and its honest evidence class

- **II.1 (retoque):** declared gap. Ozimek-adjacent finding quoted with the gap visible for *why disclosure matters*, never as retouching pedagogy. B2 deliverable requires a kept before/after pair plus a disclosure line.
- **II.2 (avatares):** declared gap. Rodríguez-Borlado & Pérez-Curiel's anthropomorphism mechanism quoted with the gap visible for *why identity intent matters*, never as an avatar-modelling method. VTON explicitly out of scope, stated in both B1 and a dedicated B3 exercise.
- **II.3 (experiencias):** SAFE as phenomenon only. Kim (2023)'s stimulus-type comparison (screened vs. 360°) is real, live-verified evidence that staging changes audience response — explicitly bounded as *not* proof of a validated teaching sequence. The C1/C2 metaverse coat stays `evaluator_safe=no` and is named as excluded, not silently dropped.
- **II.4 (vídeo):** full declared gap, by design. No coat exists in the vault for this CONTENIDOS anchor at all — every B1 claim is stated as craft guidance, never dressed as `(Author Year)` research. TTOD `img-058` ("autoplay video is not engagement — it is assault") anchors a consent-aware editing discipline as the unit's actual content.
- **II.6 (hologramas/R.A.):** declared pilot, NONE for AR pedagogy. Reuses II.3's Kim node explicitly and only as a stimulus-type parallel — both the lesson text and a dedicated B3 exercise require students to articulate why that citation is *not* independent AR evidence, so the shared-node reuse cannot be silently misread as double-counted support. The previously-discarded Hafliger bibliography-only candidate is named and confirmed not cited.

## ARTEFACT ROLE and VTON boundary

Per `oficial-guia-framework.mdc` §2's own vShowroom-eligible-anchor list (2·3·5·6), ARTEFACT ROLE was set to **`portfolio`** for II.2, II.3, and II.6 (unsigned S1/S2 attached in B2, same templates as II.5) and **`none`** for II.1 and II.4 (no S1/S2 — retouching and video are not on that list). This follows `dc-unit-forge.mdc`'s own deferred-default rule: `vShowroom` was never named in any unit's output, only `portfolio`. VTON/try-on is stated as explicitly out of scope in II.2 and II.6, per the trigger and per this repo's Hard Rule 3.

## TTOD epigraphs

Selected via `ttod_cli_adapter.TTODCliAdapter.search_quotes()`, never by hand-parsing `ttod.yml`: `img-001` (II.1, direct fit — a retouching unit is literally about what an edited image communicates), `arch-017` (II.2, analogical — avatar-as-identity), `img-024` (II.3, analogical — staged experience as a mirror/reflection), `img-058` (II.4, direct fit — video-editing unit teaching consent-aware craft), `img-046` (II.6, analogical — medium choice, know the nature of each). All five confirmed unused elsewhere in this repo (`grep` across `docs/lessons/**/index.md`) before selection, alongside the three already in use (`qa-010`, `qa-013`, `wis-013`). No new aphorism was proposed to TTOD this session.

## Hours — CD II's 80 h contact bucket now closes to 80/80

II.5 (forged in an earlier session) used 14 h of the 80 h contact-forgeable bucket. This wave allocates the remaining 66 h across the five units it forges, closing the course total exactly:

| Unit | magistral | seminarios | debates | talleres | proyectos | resolución | total |
| --- | -: | -: | -: | -: | -: | -: | -: |
| II.1 | 2 | 4 | 2 | 3 | 4 | 2 | 17 |
| II.2 | 2 | 3 | 1 | 2 | 3 | 1 | 12 |
| II.3 | 1 | 3 | 1 | 2 | 3 | 1 | 11 |
| II.4 | 2 | 4 | 2 | 3 | 3 | 2 | 16 |
| II.6 | 1 | 3 | 1 | 1 | 3 | 1 | 10 |
| **wave sum** | **8** | **17** | **7** | **11** | **16** | **7** | **66** |

Combined with II.5, CD II's `sessions_list` in `docs/_data/tracks.yml` now sums to **10 · 20 · 8 · 14 · 20 · 8 = 80 h**, matching `oficial-guia-framework.mdc` §5's official activity table exactly. This is not an invented timetable — it is the natural closure of allocating real, now-forged units, stated explicitly on both track pages alongside an equally explicit statement that closing the hour bucket is **not** the same as the course being pedagogically complete (five of six units still declare a gap or partial-phenomenon-only evidence).

## Wiring

- `docs/_data/lessons.yml`: five new entries (`ii-1-retoque-moda`, `ii-2-avatares`, `ii-3-experiencias-digitales`, `ii-4-video`, `ii-6-hologramas-ra`), same schema as the existing `ii-5-web-portfolio`/`i-5-forma-tridimensional`/`i-6-volumen` entries, inserted before the I.6 entry.
- `docs/_data/tracks.yml`: five new rows appended to `creacion-digital-ii`'s `sessions_list` (was one row, II.5, from the earlier wave), every contact-forgeable key present on each row per `dc-unit-forge.mdc` §1's own defect warning — no key omitted, no zero silently dropped.
- Both `docs/tracks/{en,es}/{digital-creativity-ii,creacion-digital-ii}/index.md` Status sections rewritten to list all six units with their evidence class in one line each, and to state the 80/80 hour closure alongside the pedagogical-completeness caveat. No other content in these two files was touched — the "Official contents" and "vShowroom role" sections are untouched from the prior session.
- `digital-creativity-pedagogy/grounding/README.md` received one addendum paragraph (after the existing 2026-08-16 addendum) recording this session's live re-verification; no existing matrix row text was altered.

## Build

```bash
cd /Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem
JEKYLL_ENV=production npm run build 2>&1 | grep -i "liquid warning"
```

Result: **PASS (empty)**. Full build succeeded (25 HTML files normalized by `normalize-ids`, up from the prior session's count; `mark-broken-links` reported no broken URLs). No `digital-creativity-pedagogy/` leak in `_site` (`find _site -iname "*digital-creativity-pedagogy*"` returns nothing). All ten new pages confirmed present at their built paths (`_site/lessons/{en,es}/{digital-creativity-ii,creacion-digital-ii}/{ii-1-retoque-moda,ii-2-avatares,ii-3-experiencias-digitales,ii-4-video,ii-6-hologramas-ra}/index.html`). Spot-checked provenance/evidence-gate sections survived the build intact on both a `[BIBLIO-GAP]`-only page (II.1 EN) and a citation-reuse page (II.6 ES). The II.6 → II.3 cross-link (`{{ '...' | relative_url }}`) resolved correctly to `/digital-creativity-uem/lessons/{en,es}/.../ii-3-experiencias-digitales/` in the built HTML, confirming the Liquid filter rendered rather than leaking literal syntax.

## Missing-evidence statements (one line each)

- **II.1:** retouching-curriculum pedagogy = NONE (`[BIBLIO-GAP]` re-confirmed genuine); appearance/social-comparison finding grounds *why disclosure matters*, not a teaching sequence.
- **II.2:** avatar-modelling-method pedagogy = NONE (`[BIBLIO-GAP]` re-confirmed genuine); anthropomorphism finding grounds the identity-perception mechanism, not a method. VTON out of scope.
- **II.3:** experience-design *teaching sequence* = NONE; Kim (2023) is SAFE as phenomenon evidence only (re-confirmed live), not a validated method.
- **II.4:** fashion-video-editing pedagogy = NONE, in full — no coat in the vault addresses this anchor at any confidence.
- **II.6:** AR/hologram pedagogy = NONE, declared pilot; the II.3 Kim node is reused strictly as a stimulus-type parallel, never independent AR evidence. VTON out of scope.

## Remaining boundary

- CD I remains untouched by this wave (7 of 9 CD I units still unforged, per CD I Wave 2's own standing note).
- CD II is now fully hour-allocated (80/80) and fully lesson-drafted (six of six CONTENIDOS anchors), but **not** pedagogically complete or teachable end-to-end as a validated curriculum — both track pages state this explicitly rather than letting the hour closure imply it.
- No research-consent administration, DPO approval, or research-data collection is implied by any unsigned S1/S2 template attached in II.2/II.3/II.6's B2 sections.
- No institution name was attached to the shared vShowroom synergy in any unit's student-facing text — `portfolio` was used throughout, `vShowroom` only in the track pages' own pre-existing "vShowroom role" section, unchanged from before this session.
- This receipt does not claim any of the five units' underlying pedagogical gaps are closed — retouching, avatar-modelling, experience-design-as-method, video-editing, and AR/hologram pedagogy all remain declared gaps or pilot status by design, per `dc-unit-forge.mdc`'s own non-negotiable that "a unit with no evidence says so."
