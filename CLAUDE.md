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

| Subject | Relevant contents (from official guide) |
| ------- | --------------------------------------- |
| **CD I** | Fundamentos y representación de la forma tridimensional · Volumen |
| **CD II** | Creación de avatares · Diseño de experiencias de moda digitales · Maquetación, edición y creación de web y portfolio digital · Hologramas y R.A. |

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

Pattern inspired by Web Atelier `frontend-pedagogy/` (grounding README, research line, cohort proposal) — adapt, do not copy FE CER claims into fashion venues without Ladder A/B discipline.

---

## 4. Hard rules

1. **No cloud AI in teaching materials** — Ollama / local only for studio generation if used.
2. **Student fashion work is authorial property** — exhibition needs per-artefact consent (synergy S1–S5).
3. **VTON / try-on is out of teaching sprint scope** — open research problem; showroom exhibits, does not fit.
4. **Pages must not leak** `digital-creativity-pedagogy/`, `_research/`, or `private/`.
5. **Authorship** — credit `ruvebal@crea-comm.net`; UEM affiliation on teaching surfaces; UDIT where research co-badges.

---

## 5. Local commands

```bash
pnpm install && bundle install
npm run develop   # :4002 /digital-creativity-uem/
npm run build     # verify excludes
```

---

## 6. Related repos

| Repo | Relation |
| ---- | -------- |
| `web-atelier-udit` | FE I/II + vShowroom engineering + CER case |
| `hc-app-design` | Emancipation template (Jekyll + Pages) |
| `profield` | Upstream field-map runs |
| `ahmes` | Extraction engine for PDFs |

> _"Process, authorship, iteration and judgement need to be made visible."_ — digital-creativity field critique this course answers with portfolio + declaration practice.
