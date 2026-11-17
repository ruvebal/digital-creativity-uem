# NM U5 + U6 forge receipt (2026-11-17)

**Skill:** master-lecture-forger 1.1.0 + `nm-unit-forge.mdc` · **Status:** forged, cold B1 pending (see §5)

## 1 · Surfaces

| Surface | U5 · Herramientas y datos | U6 · Futuro de la comunicación |
| --- | --- | --- |
| ES lesson | session clock, frame, objectives, analysis, 5 ideas, B2 ×2, B3, recall, case table, credits | same; 6 ideas; B2 Ex 1 = Canvas 10 ptos |
| EN twin | structure + teaching-language notice | same |
| Deck (`2627-nm`) | 15 slides · 9 curated · 2 diagrams · pre-rendered shell | 16 slides · 10 curated · 2 diagrams |
| Diagrams | `nm-u5-evidence-ladder`, `nm-u5-kpi-audit` | `nm-u6-disclosure-ladder`, `nm-u6-promise-proof-risk` |

## 2 · Campaign allocation (index updated)

U5: `reformation-refscale` (rank 17) · `zara-brasil-lista-suja` (rank 14) · `norrona-higg-msi-nca` (supplemental, regulator).
U6 (ranked bank has no AI/AR case): `dior-snapchat-b27-2020` · `mango-teen-ai-2024` · `guess-vogue-ai-2025` · `balenciaga-afterworld-2020` — all supplemental, scoped to their linked sources; vendor metrics taught as vendor claims. `verify:nm-campaigns` passes (29 cases).

## 3 · Grounding

- New vault: Lamerichs 2025 (`10_1515_9783839474624_013_2ebbda3a`), ingested at operator request; printed = PDF + 334; DevIAC vectors `profield-nuevos-medios-moda-2026-27` (51 chunks). Athanor inject **not run** (stack down; its Postgres binds :5432 used by DevIAC).
- Cites (all evaluator_safe, printed page read on page): UNEP 2023, 33 · 88; Couldry & Mejias 2018 (OnlineFirst), 2; Sarkis et al. 2026, 229; Bendel 2025, 440; Lamerichs 2025, 337 · 345; Flavián et al. 2024, 9; An & Park 2026, 15; Boden 2004, 320.

## 4 · Corrections to already-published units

- **UNEP page basis, U1–U3 (+ decks):** printed = PDF − 5 (footer folio). 20 public cites corrected (15→10, 26→21, 27→22, 55→50, 56→51, 79→74, 80→75). Raw resolver strings in hidden provenance left untouched. Dignity guide cites year-only — unaffected.
- **U4 Shinkle:** node `cca1472b` is printed p. 2 (was cited as 15, pdf_order) — lesson + deck fixed.
- **Rights:** Cottingley (author d. 1988) and Poirier window (d. 1968) failed the EU-term check → replaced before publication.
- **Deck JS:** back link localised by `<html lang>` (all ES decks showed English labels).
- **Anchors:** kramdown transliterates accents in heading ids; deck card links fixed.

## 5 · Cold B1 (lesson-scribe / Thessia) — PENDING

Run `forge/nm_forge_u5_u6.py` (quotes locked, verbatim registry `registries/nm-u5-u6-verbatims.json`). On 2026-11-17 another client held `qwen3.8:27b` on the GPU; attempts timed out (`httpx.ReadTimeout`) or were rejected by the v2.1 gates (fabricated quotations, missing `[S3]`). Run stopped after U5 ideas 1–3; records kept in `thessia-tuning-memory` as training signal. Lessons carry invisible slots `<!--B1:U5:n-->` / `<!--B1:U6:n-->` and an editorial-note line saying the paragraphs are in review.

**Resume:** free the GPU, then `THESSIA_PY=<python with ollama+pyyaml> python3 forge/nm_forge_u5_u6.py` (consider `--timeout 900` in the script's call), evaluate on the six axes, integrate with `amendments.diff`, remove the editorial "En revisión" line.

## 6 · Not done

Human final review of 17 new media records · Athanor inject · Thessia B1 (above).
