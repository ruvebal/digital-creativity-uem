# CD I Wave 2 execution receipt

**Executed:** 2026-08-20
**Contract:** `CD-I-WAVE-2.execute.md` (drafted this session, no prior version existed)
**Units:** I.5 — Fundamentos y representación de la forma tridimensional; I.6 — Volumen

## Correcting the trigger's own premise (found by direct inspection, not assumed)

The cascade trigger that led to this wave said `grounding/README.md` had "zero
mentions" of the field run `dc-3d-form-volume-pedagogy` and needed plugging
from scratch. On inspection at session start, the matrix already carried I.1–
II.6 rows from an earlier out-of-scope session, with I.5/I.6 already marked
**NONE** — an honest declared gap, just not yet upgraded with the field run's
findings. This session's actual Item-3 job was therefore narrower than the
trigger assumed: **upgrade** the existing NONE rows in place, not populate an
empty matrix.

## What the field run actually supported (the honesty check this receipt owes)

`~/src/profield/runs/dc-3d-form-volume-pedagogy/20260820/digest.md`: 205 rows,
59 confirmed (Pass-3-verified DOI/metadata resolution against Crossref), 1
disputed, 144 unverified, 54 pending OA. **Confirmed in Pass 3 means "the DOI
resolves to the claimed record," not "the claim is pedagogy evidence."** Read
the confirmed rows in full (`digital-creativity-pedagogy/grounding/README.md`
now documents which specific rows) before promoting anything — several
confirmed rows are art-historical, neuroscience, or general-CAD-education
findings adjacent to but not about fashion 3D-form/volume pedagogy, and those
were **not** promoted (e.g. the bas-relief-ambiguity vision-science paper, the
2D-drawing-error decomposition paper, generic CSG/mesh literature — all
real, all confirmed-DOI, none cited in the lessons below, per
`cv/UNIT-PLAN.md`'s own standing instruction not to silently transfer generic
CAD/mesh pedagogy to fashion).

Two rows *did* hold up as genuine fashion-education classroom pedagogy, not
industry practice or design history re-labelled — both describe an actually
taught sequence or module, not a vendor claim:

- Papahristou, E., & Zolota Tatsi, N. (2024) — a review reporting a real
  taught structure at two institutions (International Hellenic University;
  AMFI), 3D prototyping sequenced after 2D CAD, theory+lab split.
- Coats, M. (2026), "The Denim Project" — a published case study of one
  hybrid physical/digital CLO3D module, explicitly framed as constructivist
  experiential learning.

## Blocker found and resolved: the manual-PDF pipeline's metadata step had not run

All 10 PDFs the field run had manually harvested into
`~/src/profield/runs/dc-3d-form-volume-pedagogy/20260820/manual-pdfs/` were
already ingested into Ahmes (`ahmes ingest`, NER, semantic enrichment) but
**none** had run the bibliographic metadata cascade — `ahmes status` on every
one of the 10 extraction.db vaults showed `Metadata fields: 0` and
`Citation preview: [BIBLIO-GAP]` at session start. `ahmes query --cite
--require-evaluator-safe` therefore failed (`exit 2`, `[BIBLIO-GAP]`) on
every node tried, including the two now cited. This is a genuine, real
pipeline-lag blocker (`PENDING-RETRIEVE.md` in the same run directory names
it explicitly), not a fabrication risk — resolved by running
`ahmes enrich <db> --meta --online` live this session, which pulls real
Crossref metadata (author/year/DOI, no invented text) and is a documented,
legitimate step of Ahmes's own pipeline, not a new tool. After enrichment,
Papahristou's coat resolved at confidence 0.95 (Crossref match) and Coats's
coat likewise at 0.95. Both node citations were then **re-verified live**,
independently, not trusted from any prior claim:

```
ahmes query --cite "scholar/documents/cdatp_papachristou_20e79483/extract/extraction.db:88bcdad6-160b-5fab-a31e-848932abb7c3" --require-evaluator-safe
→ (Papahristou, 2024, p. 5)  confidence=0.95 source=metadata evaluator_safe=yes

ahmes query --cite "scholar/documents/the_denim_project_a_hybrid_approach_to_fashion_education_using_clo3d_6d1a7b81/extract/extraction.db:b3ded30f-381e-5425-80b1-cf125b52449f" --require-evaluator-safe
→ (Coats, 2026, p. 8)  confidence=0.95 source=metadata evaluator_safe=yes
```

Other candidate coats in the same 10-PDF batch (Widiyawati et al. 2024 /
`26216-86702-2-PB.pdf`) enriched to only `confidence=0.7, method=llm` with a
garbled author name (`Irwawidiyowati`) — tested, failed
`--require-evaluator-safe` (`exit 2`), **not used**. 28 of the field run's 43
cited DOIs remain genuinely un-retrieved (`PENDING-RETRIEVE.md`); no attempt
was made to force those into citations.

## Matrix upgrade — `digital-creativity-pedagogy/grounding/README.md`

I.5 and I.6 rows upgraded **in place** (existing table structure and every
other row preserved untouched):

| Unit | Before | After | Narrower gap still declared |
| --- | --- | --- | --- |
| I.5 | NONE | SAFE (course-structure pedagogy) — Papahristou & Zolota Tatsi 2024, two nodes, p.3 + p.5 | The same review states its surveyed studies report tool-adoption outcomes, not validated form/volume-understanding measures. Sequence exists; effectiveness unproven. |
| I.6 | NONE | SAFE (hybrid-studio pedagogy) — Coats 2026, node p.8; sustainability caveat node p.4 cited separately | Single case study, one cohort, one tool (CLO3D). Not evidence of a generalisable method. |

Also updated for consistency: the CV-bibliography allow-list line (added I.5
Papahristou, I.6 Coats) and the "2026-08-16 replication and grounding
addendum" paragraph, which previously stated flatly "I.5/I.6 remain a 3D/form
pedagogy gap" — now dated and qualified to say what changed and what
specific narrower gap survives the upgrade. `<!-- provenance: ... -->` was
not added to the matrix rows themselves (the matrix is prose, not a lesson
page) but the upgrade's inline text names the digest path and confirmed-row
IDs (`p1-c002`, `p1-c008`, `p1-c010`, `p1-c023`) so a future agent can
re-derive without re-running the field.

## CD I Wave 2 forge — I.5 and I.6

Drafted `CD-I-WAVE-2.execute.md` (this directory), same STEP A→D shape as
`CD-II-II.5.execute.md`, one `FORGE CD UNIT` block per unit. Executed both,
complete A→D, I.5 before I.6.

- Hours: I.5 = `clases_magistrales 1 · seminarios 2 · debates 1 ·
  talleres_labs 2 · investigaciones_proyectos 2 · resolucion_problemas 1`
  (9 h). I.6 = identical key shape, same 9 h. Running total after both:
  2/10 · 4/20 · 2/8 · 4/14 · 4/20 · 2/8 of CD I's 80 h contact bucket. The
  other 7 CD I units remain unallocated — no timetable invented for them.
- ARTEFACT ROLE: **none** for both units (dc-unit-forge.mdc's own deferred
  default) — no vShowroom naming, no S1/S2 templates attached; these are
  foundational spatial-literacy units, not portfolio-facing.
- `status: draft`; B1 conceptual (with declared gap), B2 studio brief
  (`investigaciones_proyectos`, CD I's own PDF name — not CD II's
  `proyectos`), B3 individual resolución de problemas, and provenance/
  evidence-gate section all present in all four lesson pages (EN+ES × 2
  units).

### TTOD epigraphs

- I.5: `wis-013` ("Practice in the dojo, perform in the arena.") — used
  analogically. Its own `teaches` field is about DEV/STG/PROD software
  environments; the fit here is the decontextualised-drill (B3) vs.
  contextualised-studio-piece (B2) distinction, flagged honestly in the
  lesson itself, same imperfect-fit disclosure discipline as FE Wave 2's
  `ops-001`. Confirmed unused elsewhere in this repo before selection (was
  already used once in FE II's testing-strategy unit — a different course,
  different repo track — not a same-track reuse).
- I.6: `qa-013` ("To bump wisely is to keep truth in two places: the
  manifest and the module.") — also analogical; its own `teaches` field is
  about software version sync. Fit: keeping a physical maquette and a
  digital pass in sync through iteration. Confirmed unused elsewhere in
  both this repo and FE II before selection — a genuinely fresh pick, not
  a forced reuse.
- Neither was located by hand-parsing `ttod.yml`; both were read via
  `ttod-bridge`'s `TTODCliAdapter.read_quote()` / `search_quotes()`
  (`~/src/.cursor/skills/ttod-bridge/scripts/`). No new aphorism was
  proposed to TTOD this session.

### Wiring

- `docs/_data/lessons.yml` — 2 new entries (`i-5-forma-tridimensional`,
  `i-6-volumen`), same schema as the II.5 entry added in this session's
  Item 2 (the file was `[]` for the whole repo at session start; this is
  its third and fourth entry).
- `docs/_data/tracks.yml` — under `slug: creacion-digital-i`, added both
  sessions to `sessions_list` (was `[]`); flipped that track's `status`
  from `scaffold` to `draft` in both the data file and the two track pages'
  front matter (`docs/tracks/{en,es}/{digital-creativity-i,creacion-digital-i}/index.md`),
  each page's Status section updated to link both new lessons and state
  explicitly that the other 7 CD I units are still pending. These two
  track-page files carried a **pre-existing, out-of-scope uncommitted
  diff** from an earlier session before this run touched them; that diff
  was left as found — only the `status:` field and the Status-section
  prose were edited, nothing else in the files was reverted or "cleaned
  up," per this cascade's explicit instruction to leave such pre-existing
  changes alone.

## Build

```bash
cd /Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem
JEKYLL_ENV=production npm run build 2>&1 | grep -i "liquid warning"
```

Result: **PASS (empty)**, run a second time after this wave's wiring (first
run in this session covered Item 2 only). `normalize-ids` processed 15 files
(up from 11 after Item 2 alone — the 4 new lesson pages plus track pages).
`mark-broken-links` reported no broken URLs. `_site/digital-creativity-pedagogy`
confirmed absent (no authority-tree leak). Spot-checked all four new built
pages (`_site/lessons/{en,es}/{digital-creativity-i,creacion-digital-i}/i-5-*/index.html`,
`i-6-*`) — each contains its provenance/evidence-gate section intact,
confirming no Liquid deletion inside fences. `docs/_data/tracks.yml` and
`lessons.yml` were not independently YAML-linted (`yaml-lint` binary is not
installed in this environment and `pyyaml` is not available either) — Jekyll
itself parses both data files to render every page above, and the build
succeeded, which is the practical validity check available here; flagged as
a lighter check than a dedicated linter, not silently claimed as one.

## Missing-evidence statements (one line each)

- **I.5:** 3D-form learning-outcome *validation* = NONE. Taught-sequence
  *structure* (2D→3D, theory+lab, two institutions) = SAFE, Papahristou &
  Zolota Tatsi 2024, `evaluator_safe=yes`.
- **I.6:** Volume-pedagogy *generalisability* beyond one CLO3D case study =
  NONE. Hybrid analogue/digital *teaching-module structure* = SAFE, Coats
  2026, `evaluator_safe=yes`.

## Remaining boundary

- 7 of 9 CD I units (I.1–I.4, I.7–I.9) remain unforged — Wave 4 per
  `dc-unit-forge.mdc` §4's own forge-order table.
- The CD I course is not teachable end-to-end; both track pages now say
  this explicitly rather than implying completeness via a status flip.
- 28 of the field run's 43 cited DOIs are still genuinely un-retrieved
  (`PENDING-RETRIEVE.md`) — several looked pedagogically promising on
  title alone (e.g. the haptic-sculpting VR paper, the metacognition-during-
  3D-modelling paper) but were **not** chased down or cited this session;
  they remain candidates for a future wave, not silently assumed.
- This wave upgraded exactly two matrix rows and forged exactly two units.
  It does not close CD I's hour totals, does not touch CD II beyond what
  Item 2 already wired, and does not authorize any public exhibition
  (ARTEFACT ROLE was deliberately `none` for both units — no consent
  templates were needed or added).
