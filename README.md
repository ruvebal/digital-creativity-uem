# Digital Creativity — Creación Digital (UEM)

_Avatars, digital fashion experiences, web portfolio, AR — Critical Coding for a Better Living._

Standalone teaching site for **Creación Digital I–II** (Grado en Comunicación y Gestión de Moda, Universidad Europea). Emancipated from the Web Atelier monorepo the same way [`hc-app-design`](https://github.com/ruvebal/hc-app-design) was: **own repo, own GitHub Pages, own research grounding**.

- **Live site (planned):** [https://ruvebal.github.io/digital-creativity-uem/](https://ruvebal.github.io/digital-creativity-uem/)
- **Student template:** [`student-project-template/`](student-project-template/)
- **Research / authorities (not published):** [`digital-creativity-pedagogy/`](digital-creativity-pedagogy/)
- **Sister craft site:** [Web Atelier — Web Foundations](https://ruvebal.github.io/web-atelier-udit/) (UDIT FE)
- **Sister HC site:** [Human-Centered Application Design](https://ruvebal.github.io/hc-app-design/)
- **Shared artefact:** [vShowroom synergy](https://github.com/ruvebal/web-atelier-udit/blob/main/frontend-pedagogy/atelier-synergy-vshowroom.mdc) (FE · CD · Diseño de Moda/CLO)

---

## Repository layout

| Path | Published on Pages? |
| ---- | ------------------- |
| `docs/` | Yes — Jekyll site |
| `student-project-template/` | No — fork on GitHub |
| `docs/_research/` | No — excluded in `_config.yml` |
| `digital-creativity-pedagogy/` | No — excluded; **authority home** |
| `private/` | No |

## Flagship courses

| Track | Degree placement | Status |
| ----- | ---------------- | ------ |
| **Creación Digital I** | Year 1 · S1 · 6 ECTS — 3D form foundations | scaffold |
| **Creación Digital II** | Year 1 · S2 · 6 ECTS — avatars, digital fashion experiences, web/portfolio, AR | scaffold |

## Local development

```bash
pnpm install
bundle install
npm run develop   # http://localhost:4002/digital-creativity-uem/
```

See [PUBLISHING.md](PUBLISHING.md).

## Authority & research

Canonical field map and authorities directory live under `digital-creativity-pedagogy/grounding/` (synced from the profield `digital-creativity` run). Structure inspired by Web Atelier’s `frontend-pedagogy/` — **without** importing that monorepo’s grown `.cursor` rules/skills.

Ahmes PDF extractions stay in the Ahmes library; this repo holds the **edited maps and directories**, not the binary corpus.

---

Rubén Vega Balbás, PhD — Creative Technologist & Developer · [ruvebal@crea-comm.net](mailto:ruvebal@crea-comm.net) · ORCID [0000-0001-6862-9081](https://orcid.org/0000-0001-6862-9081)  
Affiliation: Universidad Europea (teaching) · ECSIT / UDIT (research) · crea-comm.net  
Code MIT · Content CC BY-NC-SA 4.0
