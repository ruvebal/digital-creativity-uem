# CLAUDE.md — Digital Creativity / Creación Digital (UEM)

> _"AI exists to AMPLIFY human intention, not to replace it."_

**Course:** Creación Digital I–II  
**Institution:** Universidad Europea — Grado en Comunicación y Gestión de Moda  
**Instructor:** Rubén Vega Balbás, PhD — `ruvebal@crea-comm.net` · ORCID [0000-0001-6862-9081](https://orcid.org/0000-0001-6862-9081)  
**Affiliation:** UEM (teaching) · ECSIT / UDIT (research) · crea-comm.net  
**License:** Code MIT · Content CC BY-NC-SA 4.0

---

## 1. What this repo is

A **sovereign teaching site** for digital fashion creation — emancipated from Web Atelier the same way `hc-app-design` was.

| Layer | Path | Role |
| ----- | ---- | ---- |
| **L1 · Teaching** | `docs/lessons/`, `docs/tracks/` | Student-facing lessons & itineraries (GitHub Pages) |
| **L2 · Research** | `digital-creativity-pedagogy/` | Field map, authorities, proposals — **not published** |
| **L3 · Product** | vShowroom (lives in Web Atelier FE II + this cohort as content authors) | Shared exhibition artefact |

**Do not** import Web Atelier’s `.cursor/rules` or `.cursor/skills` wholesale — that stack grew for FE lesson authoring (Liquid integrity, exam-forge, CodeSandbox). This repo stays lean: methodology + content. Add Cursor rules only when CD-specific authoring needs them.

---

## 2. Official curricular anchors (Creación Digital)

**Mandatory structure:** [`digital-creativity-pedagogy/cv/guides/*.json`](digital-creativity-pedagogy/cv/guides/) — cloned from unicrawler. Framework: [`oficial-guia-framework.mdc`](digital-creativity-pedagogy/oficial-guia-framework.mdc). CV forge: [`dc-cv-forge.mdc`](digital-creativity-pedagogy/dc-cv-forge.mdc). Unit forge: [`dc-unit-forge.mdc`](digital-creativity-pedagogy/dc-unit-forge.mdc).

| Subject | Semester | ECTS | CONTENIDOS (from guía JSON `contents`) |
| ------- | -------- | ---- | ---------------------------------------- |
| **CD I** | 1 | 6 | Imágenes digitales · 2D (dibujo, color, bitmaps, efectos) · **forma tridimensional · Volumen** · referencias moda · animación · bodegones |
| **CD II** | 2 | 6 | Retoque moda · **avatares** · **experiencias de moda digitales** · vídeo · **web y portfolio digital** · **Hologramas y R.A** |

Presencial formative totals: CD I **140 h** · CD II **150 h**. Evaluation weights and activity names must match the JSON (PDF-check CD I presencial eval sum 85%).

Sister content stream (same campus triangle): **UDIT Diseño de Moda** authors garments in **CLO 3D**; FE II builds the web runtime. See synergy brief in Web Atelier `frontend-pedagogy/atelier-synergy-vshowroom.mdc` (cross-repo).

---

## 3. Research grounding (authority home)

Canonical copies live under `digital-creativity-pedagogy/grounding/`:

| File | What |
| ---- | ---- |
| `00-field-scope.md` | Field scope for digital creativity in fashion |
| `profield-digital-creativity.md` | Edited field map (pass-1) |
| `profield-authorities-directory.md` | Journals, FACTUM, awards, labs |
| `corpus-seed-list*.md` | Seed corpus (global + ibero) |
| `lexicum.yaml` | Controlled vocabulary |
| `FINAL.md` | Run wrap notes |

**Source of truth for re-sync:** `/Users/ruvebal/src/profield/runs/digital-creativity/`.  
**Ahmes extractions / PDFs:** stay in Ahmes library + `profield/.../pdfs/` — do not duplicate binaries here.

Pattern inspired by Web Atelier `frontend-pedagogy/` (grounding README, research line, cohort proposal, unit forge) — adapt, do not copy FE CER claims into fashion venues without Ladder A/B discipline.

### Scholarly grounding pipeline (CV / lessons)

**Discover in vectors, cite from Ahmes nodes.** Guías and lessons stay grounded only if this chain is live:

| Step | Tool | Command / slug |
| ---- | ---- | -------------- |
| Extract | Ahmes | batch over `profield/runs/digital-creativity/01/pdfs` |
| Embed | DevIAC | `cd ~/src/deviac && make ingest-profield-dc` → `project_slug=profield-digital-creativity` |
| Discover | MCP `search_knowledge` or `POST :8100/vectors/search` | `knowledge_scope=field_prospection` |
| Cite | Ahmes `extraction.db` | `⟨coat⟩ · nodo ⟨id⟩ · p. ⟨n⟩` — **never cite vector snippets** |
| Inject (optional) | Athanor | collective search infra — not a citation source |

Authoring gate: [`dc-unit-forge.mdc`](digital-creativity-pedagogy/dc-unit-forge.mdc) · CV: [`dc-cv-forge.mdc`](digital-creativity-pedagogy/dc-cv-forge.mdc) · framework: [`oficial-guia-framework.mdc`](digital-creativity-pedagogy/oficial-guia-framework.mdc) · readiness: [`TEACHING-READINESS.mdc`](digital-creativity-pedagogy/TEACHING-READINESS.mdc) · citation: [`grounding/README.md`](digital-creativity-pedagogy/grounding/README.md).

---

## 4. Hard rules

1. **No cloud AI in teaching materials** — Ollama / local only for studio generation if used.
2. **Student fashion work is authorial property** — exhibition needs per-artefact consent (synergy S1–S5).
3. **VTON / try-on is out of teaching sprint scope** — open research problem; showroom exhibits, does not fit.
4. **Pages must not leak** `digital-creativity-pedagogy/`, `_research/`, or `private/`.
5. **Authorship** — credit `ruvebal@crea-comm.net`; UEM affiliation on teaching surfaces; UDIT where research co-badges.
6. **No citation without an Ahmes node** — DevIAC/Athanor find; vaults prove. Declared gaps when NONE.
7. **Official guía JSON is the pedagogical contract** — hours, evaluation %, competencies, and CONTENIDOS from `cv/guides/*.json` (see `oficial-guia-framework.mdc`). No FE 10/30/14 substitution.

---

## 5. Local commands

```bash
pnpm install && bundle install
npm run develop   # :4002 /digital-creativity-uem/
npm run build     # verify excludes

# Scholarly vectors (studio machine)
cd ~/src/deviac && make health && make ingest-profield-dc
```

---

## 6. Related repos

| Repo | Relation |
| ---- | -------- |
| `web-atelier-udit` | FE I/II + vShowroom engineering + CER case · `atelier-synergy-vshowroom.mdc` |
| `hc-app-design` | Emancipation template (Jekyll + Pages) |
| `profield` | Upstream field-map runs |
| `ahmes` | Extraction engine for PDFs |
| `deviac` | Postgres + pgvector ingest (`ingest-profield-dc`) |
| `athanor` | Optional inject / field search layer (not citation) |

> _"Process, authorship, iteration and judgement need to be made visible."_ — digital-creativity field critique this course answers with portfolio + declaration practice.
