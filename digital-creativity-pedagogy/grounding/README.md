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

The lesson-level trend synthesis is [`MASTER-IDEAS.md`](./MASTER-IDEAS.md): one durable master idea plus established/emerging field movements for every I.1–II.6 unit. It is an instructor-side forge aid; it does not replace the evidence matrix or promote trend signals into student-facing citations.

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
| **II.2** | Creación de avatares | Rodríguez-Borlado / Pérez-Curiel 2024 · `rodriguez_borlado_…_f711009d` · nodo `b6b4d953-b4af-596c-affe-0bc4a44aae9a` · p.4 · `evaluator_safe=no`; **Anwar, Raza & Marzouk 2025** · nodo `cd329fc8-be24-5335-ad0d-4fe91dd97693` · citation-resolver p.1 (extraction DB p.8) · `(Anwar 2025, 1)` · `evaluator_safe=yes` — authorship/copyright instruction only; **Gonzalez-Franco, Steed, Berger & Tajadura-Jiménez 2024** · `10_3389_frvir_2024_1436752_…_ef956306` · nodo `c17b40cf-11e0-57d4-86c2-eefca69448c0` · p.12 · `(Gonzalez-Franco et al. 2024, 12)` · `evaluator_safe=yes` — avatar-perspective/embodiment design finding | [BIBLIO-GAP] for avatar method · SAFE bounded design/ethics guardrails | Gonzalez-Franco et al. grounds a perspective-and-representation discussion, not a fashion-avatar teaching or assessment sequence. Anwar supports workshops on hybrid authorship and student voice. VTON out of scope. |
| **II.3** | Diseño de experiencias de moda digitales | Kim 2023 · `10_3389_fpsyg_2023_1276856_…_ddb20bc5` · nodo `b83ed780-006c-56e2-ab8b-8f68fa6f9499` · p.5 · `(Kim 2023, 6)` · `evaluator_safe=yes`; **Smith-Glaviana 2025** · `10_1177_0887302x231161641_…_7fd736b6` · nodo `19f2e4c6-34e6-599a-8b5c-87a01bc08900` · p.1 · `(Smith-Glaviana 2025, 1)` · `evaluator_safe=yes` | SAFE, bounded phenomenon/design criteria | Kim grounds 360° vs screened fashion-show stimuli; Smith-Glaviana grounds digital-tour experience criteria (observation/reflection, multiple views, close-ups). Neither proves a teaching sequence or AR method. C1/C2 metaverse coat remains `evaluator_safe=no` — lesson gap if used. |
| **II.4** | Recursos digitales de edición de vídeo | **Díaz Soloaga & García Guerrero 2016** · *Fashion films as a new communication format to build fashion brands* · DOI `10.15581/003.29.2.45-61` · `diazsoloagagarciacsfashionfilm_5647b386` · nodo `fe3206ba-60e3-5f3d-af86-84e0d5cca572` · p.5 · `(Díaz Soloaga & García Guerrero 2016, 5)` · `evaluator_safe=yes` — fashion-film form/communication | SAFE bounded genre/communication criterion · NONE for editing pedagogy | Use the source to frame purpose, audience, and fashion-film form. It does **not** validate the unit's storyboard-to-export teaching sequence or accessibility defaults; tool docs remain `[PLATFORM]`. |
| **II.5** | Maquetación, edición y creación de web y portfolio digital | **Anwar, Raza & Marzouk 2025** · `anwar_raza_marzouk_…_0598ec0e` · nodo `c9a17328-72f7-56c8-95bf-b9860b1067b8` · p.0 · `(Anwar 2025, 1)` · `evaluator_safe=yes` — GenAI in *studio-based fashion education*; pillars include Learner Identity & Authorship. **Rizzi & Bertola 2025** · `rizzi_bertola_…_167816a4` · nodo `908f5339-781d-51cc-a803-47dfbf9c0677` · p.9 · `(Rizzi 2025, 10)` · `evaluator_safe=yes` — human–AI co-creation as complement. **Garcia 2025** · *Self-Coded Digital Portfolios as an Authentic Project-Based Learning Assessment in Computing Education* · DOI `10.3390/educsci15091150` · `garcia_self_coded_digital_portfolios_…_8fef58f2` · nodos `e09e72ca-5a4b-51dc-823a-1d05ea71ee8f` p.2, `7cac84dd-3ac8-5022-bda7-027ef5f6651d` p.4, `evaluator_safe=yes` — coded portfolio as web-design PBL/assessment evidence | SAFE (authorship / studio AI / portfolio process) · **NONE** (fashion-portfolio UX outcomes) | **Wave 1.** Ground why process/authorship and the build-assessment link must be visible. Garcia is a technical-course analogue, not evidence that a particular layout, accessibility pattern, hiring outcome, or causal learning effect works. Tool docs for HTML/CSS. vShowroom = L3 ingest, not a substitute CONTENIDO. S1/S2 before any public piece. |
| **II.6** | Hologramas y R.A | Same Kim 2023 node as II.3 (VR/360 stimulus, not AR pedagogy). **Sarkis, Jabbour Al Maalouf, Saliba & Azizi 2026** · *The impact of augmented reality within the fashion industry on purchase decisions, customer engagement, and brand loyalty* · DOI `10.1080/17543266.2025.2470187` · `the_impact_of_augmented_reality_…_5c35833d` · nodos `c1e5a143-1e2e-5b7d-8600-002e4247b5a1` p.2, `4b9dbab8-21db-5d2e-b1cc-5c378303ce21` p.8 · `(Sarkis et al. 2026, 2, 8)` · `evaluator_safe=yes` — fashion-AR audience/consumer response. Harvest T3 Hafliger p.15 was **bibliography** — discarded. | SAFE bounded AR/experience phenomenon · NONE for AR pedagogy | Use Sarkis to make audience, interaction, and response part of the AR rationale; its 855-person Middle Eastern consumer sample does **not** validate AR/hologram teaching, a classroom sequence, or a general effect. Declare pilot. VTON stays out. |

**CV bibliography may use only `evaluator_safe=yes` rows** (I.1 Shinkle; I.5 Papahristou; I.6 Coats; II.2 Gonzalez-Franco as bounded avatar design; II.3 Kim as phenomenon; II.4 Díaz Soloaga & García Guerrero as bounded fashion-film form; II.5 Anwar + Rizzi + Garcia; II.6 Sarkis as bounded AR phenomenon). All `[BIBLIO-GAP]` / NONE portions stay honest in the lesson.

**Rule:** if a lesson cites a layer, that layer must be reconstructable from this repo’s maps + Ahmes vaults. Curriculum may not cite grounding the teaching repo does not carry (maps) or the library does not hold (vaults).

**Before forging NONE / `[BIBLIO-GAP]` / pilot units:** run the dedicated Profield fields in [`GAP-PROSPECTION-INDEX.mdc`](./GAP-PROSPECTION-INDEX.mdc) (gap harvest → portfolio web UX → volume/3D → 2D craft → retouch → avatar → video → AR → motion/still → experience pedagogy).

## 2026-08-16 replication and grounding addendum

The specialty-field Pass 1 edited artifacts are replicated under [`gap-fields/INDEX.mdc`](./gap-fields/INDEX.mdc), with coat coverage in [`gap-fields/COAT-INVENTORY.json`](./gap-fields/COAT-INVENTORY.json), procurement gaps in [`gap-fields/PENDING-procurement.md`](./gap-fields/PENDING-procurement.md), and forge discovery questions in [`gap-fields/FORGE-AVANTGARDE-QUESTIONS.md`](./gap-fields/FORGE-AVANTGARDE-QUESTIONS.md). The unified T1–T3/C1–C3 and I.1–II.6 map is [`temario-unified/INDEX.md`](./temario-unified/INDEX.md).

This replication does not silently upgrade evidence. **2026-08-20 update:** I.5/I.6 moved from NONE to SAFE course-structure/hybrid-studio pedagogy evidence (Papahristou & Zolota Tatsi 2024; Coats 2026), sourced from field run `dc-3d-form-volume-pedagogy`'s Pass-3-confirmed rows and resolved to `evaluator_safe=yes` Ahmes citations this session — see the matrix rows above for the exact narrower gap each still declares (learning-outcome validation for I.5; generalisability beyond one CLO3D case study for I.6). This is a genuine upgrade of *classroom pedagogy* evidence, not industry practice re-labelled: both cited passages describe an actually-taught sequence or module, not a vendor claim or a design-history account. II.3 remains safe only as a digital-experience phenomenon; II.2, II.4, II.5, and II.6 now also carry safe but bounded design/industry/process anchors while retaining their narrower pedagogy or UX gaps; II.1, I.8, and I.9 remain declared gaps or bibliography gaps as shown in the matrix. Athanor/DevIAC outputs are discovery aids only; publication citations require Ahmes page/node evidence and `evaluator_safe=yes`.

**2026-08-20 CD Wave 3 forge-time re-verification (II.1, II.2, II.3, II.4, II.6 — no matrix values changed at that checkpoint, only re-confirmed live):** forging these five units re-checked every citable claim against a live `ahmes status` / `ahmes query --cite --require-evaluator-safe`, not the matrix text alone. II.1's Ozimek-style coat and II.2's Rodríguez-Borlado & Pérez-Curiel coat both remained genuinely `[BIBLIO-GAP]` — each received one live `ahmes enrich --meta --online` attempt at that checkpoint (Ozimek: 0 nodes enriched, no online match; Rodríguez-Borlado: "Host registry mismatch — identifiers only," 0 nodes enriched) and neither resolved, confirming these were content gaps, not pipeline lag. II.3's Kim (2023) node re-resolved live at `evaluator_safe=yes`, unchanged from its existing SAFE-as-phenomenon status. At that checkpoint, II.4 was still NONE and II.6 reused the II.3 Kim node explicitly as a stimulus-type parallel, not independent AR evidence. The 2026-08-23 completion pass below adds later safe, bounded anchors without upgrading the narrower pedagogy gaps.

**2026-08-23 Athanor-assisted completion pass:** the scoped discovery seeds were run against `profield-digital-creativity` and `profield-frontend-pedagogy`. Vector results were treated as pointers only. Complete Ahmes nodes were read and passed the citation gate for Gonzalez-Franco et al. (2024), p.12 (avatar perspective/embodiment design); Díaz Soloaga & García Guerrero (2016), p.5 (fashion-film form); Sarkis et al. (2026), pp.2 and 8 (fashion-AR audience response); and Garcia (2025), pp.2 and 4 (self-coded portfolio process/PBL). The existing Anwar and Smith-Glaviana anchors remain safe at their narrower scopes. The AI-tools candidate with `host_title_mismatch=true`, the e-module/video-production candidate with `[BIBLIO-GAP]`, and the unverified avatar/video/AR teaching claims remain quarantined or declared gaps. No vector preview was promoted to lesson prose or citation.

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
