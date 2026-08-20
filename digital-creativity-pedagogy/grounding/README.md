# Grounding — digital creativity authorities

Synced edited maps and directories for Creación Digital. **Not published** on GitHub Pages.

See parent [`../README.mdc`](../README.mdc) for layout, re-sync commands, and Ladder A/B discipline.

| File | Role |
| ---- | ---- |
| `00-field-scope.md` | Field scope |
| `profield-digital-creativity.md` | Edited field map |
| `profield-authorities-directory.md` | Journals · FACTUM · awards · labs |
| `corpus-seed-list.md` / `corpus-seed-list-ibero.md` | Seed lists |
| `lexicum.yaml` | Controlled vocabulary |
| `FINAL.md` | Run wrap |
| [`TEMARIO-PROSPECTION.md`](./TEMARIO-PROSPECTION.md) | Technique + critical Contidos prompts & Ahmes path |
| [`temario/`](./temario/) | **Canonical** T1–T3 + C1–C3 `.pass1.resultant.mdc` (mirrored from profield `01/temario/`) |
| [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md) | **Worked demo** — how discovery bounced to Tri-Anchors for each resultant |
| [`temario/PROVENANCE-LAYER.json`](./temario/PROVENANCE-LAYER.json) | Machine harvest of that demo (queries, sims, cites, quotes) |

Upstream pipeline: `/Users/ruvebal/src/profield/runs/digital-creativity/`  
Ahmes PDFs / vaults: stay in Ahmes library + `profield/.../pdfs/` — **never duplicate binaries here**.

**Classical-didactics axis (new, 2026-08-16):** unit/CV design claims about *how
people learn* (backward design, inquiry flow, Bloom's taxonomy, cognitive
load, scaffolding) resolve against a separate field, `profield-didactics`
(`project_slug=profield-didactics`) — **never** blended with this repo's own
domain-evidence rows above. Skill: `curriculum-forger` (`~/src/.cursor/skills/curriculum-forger/SKILL.md`,
sibling to `user-guide-forger`), shared with FE.

---

## Retrieval vs citation — durable rule

Three layers; **only one may be cited** in guías or lessons:

| Layer | Role | Cite? |
| ----- | ---- | ----- |
| **Ahmes vault** — `extraction.db` node + page | Authoritative claim + quote | ✅ **Yes — only citable layer** |
| **DevIAC vectors** — `search_knowledge` / HTTP `/vectors/search`, `project_slug=profield-digital-creativity`, `knowledge_scope=field_prospection` | Fast semantic discovery (DERIVED) | ❌ Never cite a snippet |
| **Athanor inject + search** | Cite-grade **index** over injected fission nodes (`--vault` + `--project-slug`) | ❌ Not evidence itself — returns pointers **to** Ahmes nodes |

**Discover in vectors / Athanor, cite from Ahmes nodes.** A vector hit is a pointer: no stable page, may be mid-argument truncated, cannot show surrounding qualification. Citation form: `⟨coat⟩ · nodo ⟨id⟩ · p. ⟨n⟩`.

This README is the **policy**. The provenance layer is the **worked proof** that the policy runs end-to-end on the temario resultants. See § Process below.

### Cross-project vaults (2026-08-13) — first entry, pattern borrowed from FE

FE's twin file (`web-atelier-udit/frontend-pedagogy/grounding/README.mdc`) has run a
"cross-project vaults" table since 2026-08-11 — MSCA sources usable here with labelled scope
rules, never duplicated as PDFs. This repo didn't have one yet; starting it now with the first
real case rather than as an empty template.

| Vault | Class | Use for | Never use for |
| --- | --- | --- | --- |
| `MSCA/SVCM/research/computational-authorship` — Göbels et al. 2026, *Aligning AI with human values: Design principles for human-centered AI* (Procedia CIRP, CIRP Design 2026) | Peer-reviewed, general HCI/AI-design principles | Framing AI-assisted design tooling in the CD curriculum as *responsible*, not just *productive* — the same design-principles register `dc-unit-forge.mdc` already asks for when a unit touches AI-assisted authoring | Any fashion/CD-domain-specific claim — the paper is general, not fashion or 3D-specific |

Extraction lives once, in MSCA's `computational-authorship` workstream — cite the node from
here, never copy the PDF into this repo's `pdfs/`.

### Keep the corpus searchable

```bash
cd ~/src/deviac
make health                    # stack must be green
make ingest-profield-dc        # Ahmes vaults → vectors (after batch extract)

# Cite-grade field index (separate from DevIAC ingest)
cd ~/src/athanor && source .venv/bin/activate && set -a && source .env && set +a
athanor inject --from-manifest \
  ~/src/profield/runs/digital-creativity/01/pdfs/.ahmes/batch-manifest.json \
  --project-slug profield-digital-creativity --vault scholar
```

Smoke:

```bash
curl -s -X POST http://localhost:8100/vectors/search \
  -H "Content-Type: application/json" \
  -d '{"query":"generative AI fashion studio education","project_slug":"profield-digital-creativity","knowledge_scope":"field_prospection","n_results":5}'
```

Meta coats are **not** required for MCP/HTTP discovery; ingest reads `extract/index.md` from each vault. Re-run ingest **and** Athanor inject when the Ahmes batch gains vaults (DevIAC alone leaves Athanor stale — see provenance demo inject 43 → 62).

FE pedagogy twin: `project_slug=profield-frontend-pedagogy`. MSCA twin: `vault=svcm`, slug `svcm-*`, scope opaque (e.g. `work_package`) — same CLI, different namespace (`/Users/ruvebal/src/athanor/docs/DEV_PLAN/PHASE-P6-REPORT.md`).

---

## Process — how the provenance layer was built (2026-08-11)

Not a second policy: a **session recipe** that operationalises this README against `temario/INDEX.md`.

| Step | Action | Tool |
| ---- | ------ | ---- |
| 0 | Confirm corpus coated / ingestable | Ahmes batch + `make athanor-ready-dc` (profield) |
| 1 | Refresh **DERIVED** discovery | `make ingest-profield-dc` |
| 2 | Sync **cite-grade index** to vault growth | `athanor inject --from-manifest …` (idempotent; skipped 43, injected 19) |
| 3 | One query per resultant strand (T1–T3 · C1–C3) | Theme phrase from resultant focus — not DOI scraping |
| 4 | Rank candidates | `athanor search` (primary) + DevIAC (corroboration only) |
| 5 | Resolve coat | `source_hash[:8]` → `~/ahmes-library/scholar/documents/*_<hash8>/` |
| 6 | Cite + quote | `ahmes query --cite "$DB:<node_id>"` + fission `markdown_content` (prefer body text over thin headings) |
| 7 | Optional ledger | `ahmes ground` with **library-relative** `scholar/documents/…/extraction.db:<node_id>` |
| 8 | Persist | `PROVENANCE-LAYER.json` + human `PROVENANCE-LAYER.md`; link from `temario/INDEX.md` |

**Honesty gates observed:** `[BIBLIO-GAP]` stays visible (T2); incomplete meta titles are not papered over; vector snippets never become lesson prose.

Full operator recipe + per-resultant table: [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md).

---

## Bounce path — provenance → CV forge → unit forge → lessons

```text
temario/*.pass1.resultant.mdc     claims + DOI/ISBN (bibliography intent)
        │
        ▼
PROVENANCE-LAYER.{md,json}        live Tri-Anchors proving vault coverage
        │
        ├─► grounding/README evidence matrix   (unit row = coat·node·page)
        │
        ├─► dc-cv-forge.mdc Step A/B           bibliografía + scholarly notes
        │         only SAFE / evaluator-safe cites in published CV
        │
        └─► dc-unit-forge.mdc Step A           lesson WHY grounded in nodes
                  └─► docs/lessons/{en,es}/…   student-facing; Tri-Anchor in research note
                      B1 conceptual / B2 studio / B3 exercises
```

| Forge gate | Uses provenance layer how |
| ---------- | ------------------------- |
| **Evidence matrix** (below) | Promote demo Tri-Anchors into unit rows when forging; else **NONE** + declared gap |
| **`dc-cv-forge`** | Temario resultants supply reading-list structure; Ahmes cites supply checkable bibliography lines; PENDING ISBN/DOI stay honest |
| **`dc-unit-forge` Step A** | Query must hit the same project; lesson claims copy **Ahmes quote + Tri-Anchor**, not JSON `content_preview` from DevIAC/Athanor |
| **Published Pages** | Never ship `digital-creativity-pedagogy/` or provenance JSON; only forged lesson prose that already resolved cites |

Until a **row** exists, treat the unit as **NONE**. Rows now exist for I.1–I.9 and II.1–II.6; several are honest NONE / `[BIBLIO-GAP]`.

---

## Evidence matrix — read before forging (plugged 2026-08-14)

Unit IDs: [`../cv/UNIT-PLAN.md`](../cv/UNIT-PLAN.md). Harvest demo: [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md). **Cite Ahmes nodes, not the 2026-08-11 index-page T1 quote.**

Transfer boundary (all rows): a vault hit that describes industry practice, VR stimuli, or GenAI studio culture is **not** evidence that *this* teaching sequence works. Vendor/tool docs ground HOW.

| Unit | CONTENIDOS | Vault evidence | Gate | Authoring instruction |
| ---- | ---------- | -------------- | ---- | --------------------- |
| **I.1** | Introducción a las imágenes digitales | Shinkle 2008 · `eugenie_shinkle_…_1936070c` · nodo `cca1472b-b0c6-594c-8e13-ed87d6b73897` · p.14 · `(Shinkle 2008, 15)` · `evaluator_safe=yes` | SAFE | Fashion image as a field of practices, not a file format. Does **not** ground Photoshop pedagogy. |
| **I.2** | Tecnología digital 2D: Herramientas de dibujo | **NONE** for 2D-tool pedagogy | NONE | Declare gap. HOW = dated tool docs. |
| **I.3** | Color, imágenes con mapas de bits | **NONE** for colour-management pedagogy | NONE | Declare gap. |
| **I.4** | Efectos | **NONE** | NONE | Declare gap. |
| **I.5** | Forma tridimensional | **Papahristou, E., & Zolota Tatsi, N. 2024**, "A review of 3D design knowledge and its impact on creativity in fashion design education," *Communications in Development and Assembling of Textile Products* 5(2), 266–277, DOI [10.25367/cdatp.2024.5.p266-277](https://doi.org/10.25367/cdatp.2024.5.p266-277) · `cdatp_papachristou_20e79483` · nodo `88bcdad6-160b-5fab-a31e-848932abb7c3` · p.5 · `(Papahristou 2024, 5)` · `evaluator_safe=yes` — describes an actually-taught sequence: 3D virtual prototyping at International Hellenic University (3rd-year BA), sequenced after 2D CAD patternmaking, split theory/lab. Same coat, nodo `a196bf7e-da78-5714-86df-7e196221f633` · p.3 · `(Papahristou 2024, 3)` · `evaluator_safe=yes` — reports Siersema's (2015) account of AMFI integrating 3D prototyping across the multi-year curriculum, moving from final-phase to conceptual-phase use. Both resolved 2026-08-20 from field run `dc-3d-form-volume-pedagogy` (`~/src/profield/runs/dc-3d-form-volume-pedagogy/20260820/digest.md`, confirmed rows p1-c002/p1-c008); metadata cascade run live via `ahmes enrich --meta --online` this session (Crossref match, conf=0.95) — the coat existed in `manual-pdfs/` unenriched, not newly harvested. <!-- provenance: digest.md confirmed row p1-c002 (section 1) + p1-c008 (same section, gap statement); node text pulled via sqlite3 fission_node.markdown_content, not the digest's paraphrase --> | SAFE (course-structure pedagogy) | Wave 2. Grounds *that* 3D-form teaching sequences exist and how two institutions actually structured them. Narrower gap remains and must stay declared in the unit: the same review (p1-c008, same DOI, p.1) states its own reviewed studies report *tool-adoption* outcomes (efficiency, confidence, self-reported creativity) rather than validated measures of form/volume understanding — do not let the course-structure citation imply learning-outcome validation it does not carry. |
| **I.6** | Volumen | **Coats, M. 2026**, "The Denim project – a hybrid approach to fashion education using CLO3D," *International Journal of Fashion Design, Technology and Education*, DOI [10.1080/17543266.2026.2688308](https://doi.org/10.1080/17543266.2026.2688308) · `the_denim_project_a_hybrid_approach_to_fashion_education_using_clo3d_6d1a7b81` · nodo `b3ded30f-381e-5425-80b1-cf125b52449f` · p.8 · `(Coats 2026, 8)` · `evaluator_safe=yes` — a hybrid analogue/digital garment module explicitly framed as constructivist experiential learning (citing Biggs & Tang 2011; Kolb 1984), students iterating between physical muslin and CLO3D to build garment volume. Resolved 2026-08-20 from the same field run (confirmed rows p1-c010/p1-c023); metadata cascade run live this session (Crossref match, conf=0.95). <!-- provenance: digest.md confirmed row p1-c010 (section 2) + p1-c023 (section 4, same paper); node text pulled via sqlite3 fission_node.markdown_content --> | SAFE (hybrid-studio pedagogy) | Wave 2. Grounds one real teaching module for volume via combined physical+digital garment construction, explicitly theorised (not just described). Transfer boundary: single case study, one cohort, one module — not evidence of a generalisable method, and do not extend it past CLO3D-specific volume work. The same paper's sustainability critique (nodo `e4ea7122-7e03-5c1e-b82d-0416b553bc7b`, p.4 — CLO3D reduces sampling waste but risks reinforcing overproduction logic) is a caveat on the *tool*, not on the pedagogy; it grounds a classroom discussion prompt, not a pedagogy claim, and must not be cited as if it were one. |
| **I.7** | Fuentes y referencias compositivas en el diseño de moda | Campinho et al. 2025 · `campinho_et_al_…_31a9a359` · nodo `29e0b3cf-bd30-5373-bfbe-d208de8c3a3b` · p.1 · **`evaluator_safe=no`** (slug-derived) | [BIBLIO-GAP] | Quote fission text in the lesson with the gap visible. **Do not** put this coat in the published CV bibliography. |
| **I.8** | Creación de imágenes digitales animadas | **NONE** | NONE | Declare gap. |
| **I.9** | Bodegones digitales | **NONE** | NONE | Declare gap. S1 if any bodegón is exhibited. |
| **II.1** | Retoque fotográfico avanzado de imágenes moda | Ozimek-style coat `10_1186_s40359_023_01143_0_…_4abbe095` · nodo `19d22df6-075b-5405-b518-05d5e629c044` · p.1 · **`[BIBLIO-GAP]`** | [BIBLIO-GAP] | Quoteable on photo-editing / appearance comparison. Not SAFE for CV bib. Not a retouching-software curriculum. |
| **II.2** | Creación de avatares | Rodríguez-Borlado / Pérez-Curiel 2024 · `rodriguez_borlado_…_f711009d` · nodo `b6b4d953-b4af-596c-affe-0bc4a44aae9a` · p.4 · `evaluator_safe=no` | [BIBLIO-GAP] | Anthropomorphism / “avatar world” — identity frame, **not** a CLO/avatar modelling method. VTON out of scope. |
| **II.3** | Diseño de experiencias de moda digitales | Kim 2023 · `10_3389_fpsyg_2023_1276856_…_ddb20bc5` · nodo `b83ed780-006c-56e2-ab8b-8f68fa6f9499` · p.5 · `(Kim 2023, 6)` · `evaluator_safe=yes` | SAFE as *phenomenon* | 360° vs screened fashion-show stimuli. Transfer: how industry stages a digital experience. **Does not** prove a teaching sequence. C1/C2 metaverse coat remains `evaluator_safe=no` — lesson gap if used. |
| **II.4** | Recursos digitales de edición de vídeo | **NONE** | NONE | Declare gap. |
| **II.5** | Maquetación, edición y creación de web y portfolio digital | **Anwar, Raza & Marzouk 2025** · `anwar_raza_marzouk_…_0598ec0e` · nodo `c9a17328-72f7-56c8-95bf-b9860b1067b8` · p.0 · `(Anwar 2025, 1)` · `evaluator_safe=yes` — GenAI in *studio-based fashion education*; pillars include Learner Identity & Authorship. **Rizzi & Bertola 2025** · `rizzi_bertola_…_167816a4` · nodo `908f5339-781d-51cc-a803-47dfbf9c0677` · p.9 · `(Rizzi 2025, 10)` · `evaluator_safe=yes` — human–AI co-creation as complement. Field map still holds `[UNVERIFIED-GAP]` on fashion-portfolio *web UX* causal studies. | SAFE (authorship / studio AI) · **NONE** (portfolio web UX) | **Wave 1.** Ground *why process and authorship must be visible*. Declare gap on which layout/a11y patterns hire. Tool docs for HTML/CSS. vShowroom = L3 ingest, not a substitute CONTENIDO. S1/S2 before any public piece. |
| **II.6** | Hologramas y R.A | Same Kim 2023 node as II.3 (VR/360 stimulus, not AR pedagogy). Harvest T3 Hafliger p.15 was **bibliography** — discarded. | NONE for AR pedagogy | Declare pilot. VTON stays out. |

**CV bibliography may use only `evaluator_safe=yes` rows** (I.1 Shinkle; I.5 Papahristou; I.6 Coats; II.3 Kim as phenomenon; II.5 Anwar + Rizzi). All `[BIBLIO-GAP]` / NONE rows stay honest in the lesson.

**Rule:** if a lesson cites a layer, that layer must be reconstructable from this repo’s maps + Ahmes vaults. Curriculum may not cite grounding the teaching repo does not carry (maps) or the library does not hold (vaults).

**Before forging NONE / `[BIBLIO-GAP]` / pilot units:** run the dedicated Profield fields in [`GAP-PROSPECTION-INDEX.mdc`](./GAP-PROSPECTION-INDEX.mdc) (gap harvest → portfolio web UX → volume/3D → 2D craft → retouch → avatar → video → AR → motion/still → experience pedagogy).

## 2026-08-16 replication and grounding addendum

The specialty-field Pass 1 edited artifacts are replicated under [`gap-fields/INDEX.mdc`](./gap-fields/INDEX.mdc), with coat coverage in [`gap-fields/COAT-INVENTORY.json`](./gap-fields/COAT-INVENTORY.json), procurement gaps in [`gap-fields/PENDING-procurement.md`](./gap-fields/PENDING-procurement.md), and forge discovery questions in [`gap-fields/FORGE-AVANTGARDE-QUESTIONS.md`](./gap-fields/FORGE-AVANTGARDE-QUESTIONS.md). The unified T1–T3/C1–C3 and I.1–II.6 map is [`temario-unified/INDEX.md`](./temario-unified/INDEX.md).

This replication does not silently upgrade evidence. **2026-08-20 update:** I.5/I.6 moved from NONE to SAFE course-structure/hybrid-studio pedagogy evidence (Papahristou & Zolota Tatsi 2024; Coats 2026), sourced from field run `dc-3d-form-volume-pedagogy`'s Pass-3-confirmed rows and resolved to `evaluator_safe=yes` Ahmes citations this session — see the matrix rows above for the exact narrower gap each still declares (learning-outcome validation for I.5; generalisability beyond one CLO3D case study for I.6). This is a genuine upgrade of *classroom pedagogy* evidence, not industry practice re-labelled: both cited passages describe an actually-taught sequence or module, not a vendor claim or a design-history account. II.3 remains safe only as a digital-experience phenomenon; II.5 is safe for authorship/studio-AI framing but remains a gap for fashion-portfolio web UX outcomes; II.1, II.2, II.4, II.6, I.8, and I.9 remain declared gaps or bibliography gaps as shown in the matrix. Avatar and motion/still fields have no OA procurement result in this batch. Athanor/DevIAC outputs are discovery aids only; publication citations require Ahmes page/node evidence and `evaluator_safe=yes`.

**2026-08-20 CD Wave 3 forge-time re-verification (II.1, II.2, II.3, II.4, II.6 — no matrix values changed, only re-confirmed live):** forging these five units re-checked every citable claim against a live `ahmes status` / `ahmes query --cite --require-evaluator-safe`, not the matrix text alone. II.1's Ozimek-style coat and II.2's Rodríguez-Borlado & Pérez-Curiel coat both remain genuinely `[BIBLIO-GAP]` — each received one live `ahmes enrich --meta --online` attempt this session (Ozimek: 0 nodes enriched, no online match; Rodríguez-Borlado: "Host registry mismatch — identifiers only," 0 nodes enriched) and neither resolved, confirming these are content gaps, not pipeline lag. II.3's Kim (2023) node re-resolved live at `evaluator_safe=yes`, unchanged from its existing SAFE-as-phenomenon status. II.4 remains NONE — no coat exists to check. II.6 reuses the II.3 Kim node explicitly as a stimulus-type parallel, not independent AR evidence, same boundary this table already states.

---

## Improvements — skill / agent / MSCA twin

**Skill (generic):** `~/.cursor/skills/provenance-layer/` — field-agnostic harvest (`SKILL.md` + `profiles.md` + `scripts/harvest_provenance_layer.py`). Profiles: digital-creativity · frontend-pedagogy · msca-svcm.

| Gap | Improvement |
| --- | ----------- |
| Athanor lag after ingest | Makefile target: ingest → inject-if-stale → `harvest_provenance_layer.py` |
| Claim ↔ DOI mismatch | Second pass: for each resultant `doi:` / `isbn:`, search vault by identifier |
| Evidence matrix | Plugged 2026-08-14 with unit IDs + SAFE/`[BIBLIO-GAP]`/NONE; re-harvest when coats enrich |
| MSCA / SVCM | Use profile `msca-svcm` (`vault=svcm`); do not mix `scholar` coats into Part B without the SVCM ledger |

**Not recommended:** citing Athanor/DevIAC payloads; auto-filling CV bibliography from sim scores alone; collapsing MSCA `work_package` scope into `field_prospection`.
