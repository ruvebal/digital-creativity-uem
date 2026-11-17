# NM U5 + U6 forge receipt (2026-11-17)

**Skill:** master-lecture-forger 1.1.0 + `nm-unit-forge.mdc` · **Status:** forged · cold B1 integrated (see §5)

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

## 5 · Cold B1 (lesson-scribe / Thessia) — DONE 2026-11-17

Run 3 (after restarting a wedged Ollama server; 30-min timeout, ≤3 attempts) produced a gate-passing draft for all 11 ideas. Every draft was then reviewed on the six axes and amended by hand; `integrated.md`, `amendments.diff` and `evaluation.md` sit in each record, and each lesson paragraph carries a hidden `tuning_record` pointer.

| Idea | Record | Main amendments |
| --- | --- | --- |
| U5·1 | 7887cf42 | Apollo framing corrected; grammar |
| U5·2 | e8d03eed | **fabricated page "p. 39"** removed; RefScale assurance overclaim fixed |
| U5·3 | 164a68c6 | Couldry & Mejias page completed (2); invented Google/Amazon detail removed |
| U5·4 | e77d42ac | *lista suja* claim corrected (could enter, not appeared) |
| U5·5 | f346647f | invented "Nike" example removed; misattached UNEP 88 cite removed |
| U6·1 | d35b221f | placeholder "([author_year])" → Sarkis et al. 2026, 229 |
| U6·2 | 01cb3a7c | date (2024), campaign vs collection, Bendel re-anchored to training data |
| U6·3 | 68dadd29 | **fabricated Flavián quotation** removed |
| U6·4 | 6466b050 | Lamerichs re-anchored (337); TikTok example removed |
| U6·5 | c3b1435d | game title used as citation; Lamerichs 345 re-anchored; ownership claim removed |
| U6·6 | ffc9c674 | **fabricated DOI link** for Boden removed; Lovelace mis-framing fixed |

### Harness findings (report to the Thessia/lesson-scribe owner)

1. **CI3 citation fidelity reported 0 checked on every pass** — it let a wrong page ("p. 39"), page-less cites and a placeholder through. The regex accepts these forms, so the registry built from BRIEF.md is probably empty.
2. **v2.1 quote verification false-passes** when an invented quotation *contains* a registered fragment ("dark side"). It should require the whole quoted span to match.
3. Under GPU contention the default HTTP timeout fails passes silently (no raw output); the forge now uses `--timeout 1800`.
4. Thessia regularly ignores `[S1]…[S4]`, overruns length and invents examples; the six-axis human pass remains necessary.

## 6 · Not done

Human final review of the new media records · Athanor inject.
