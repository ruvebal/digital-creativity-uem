# CLOSING AUDIT — DC Excellence EX11

Probe at HEAD: `evidence/final-EX11.json`. Targets:

```bash
node digital-creativity-pedagogy/excellence/probe/excellence-probe.mjs --targets
```

Scope (TECHNICAL-DIRECTOR A1): CD I I.1–I.9 lessons + Wave-1 media decks
I.1–I.5 + fashion-image-analysis master lecture. CD II / Nuevos Medios are
firewall + handoff only — see `NEXT-CASCADE-CD-II.md`.

| FINDINGS ID | Closing phase | Evidence (probe key / test / file) | Status |
| --- | --- | --- | --- |
| A1 | EX0 · EX1 | `contract.weights_match_55_15_20_10`; `docs/evaluation/index.md` 55/15/20/10; DECISION-EX0-GUIA.md | closed |
| A2 | EX0 · EX1 · EX10 | COORDINATION-SANDRA.md; TRANSPOSITION-BRIEF.md EN+ES ≡ ACT3 cartel; DIVERGENCE-VS-PLAN-DE-TRABAJO.md | closed |
| A3 | EX1 · EX9 | `wave1.en_es_parity_delta` = 0 for CD I I.1–I.9; EX9 spine + ES B2 I.1–I.5 | closed |
| A4 | EX1 | How-to-Pass + evaluation name Workshop = Transposition + session rhythm | closed |
| A5 | EX0 · EX11 | Wave-1 owns CD I + FIA; CD II/NM = NEXT-CASCADE-CD-II.md (no Wave-1 redesign) | closed |
| B1 | EX5 · EX11 | Six Wave-1 media decks present (`wave1_media_deck_count`); I.6–I.9 / II.* / NM decks deferred | deferred |
| B2 | EX3 · EX4 | `php_cache_files` = 0; validate-decks orphan warn; rights-report.json | closed |
| B3 | EX3 · EX4 | media-rules + schema_version 2 + bindSlides; autopilot-assets.json | closed |
| B4 | EX5 · EX8 | `npm run test:browser` / deck-layout.mjs in EX5+EX8 gates | closed |
| B5 | EX5 · EX8 | Geometrical lab_opener / workshop_opener on Wave-1 decks | closed |
| C1 | EX2 | `lesson_infra_vocab_files` = 0; `special_infra_vocab` false (publicSource) | closed |
| C2 | EX6 | `references_yml_present`; research-manifest.yml; Wave-1 References resolve verified keys | closed |
| C3 | EX6 · EX7 | PARTIAL procurement in research-manifest; catalogue gaps honest | closed |
| C4 | EX7 | `catalogue_present` → CANONICAL-METHODS.yml (fashion-craft, not CT IDs) | closed |
| C5 | EX1 · EX10 | TRANSPOSITION-BRIEF critical layer; Steimberg/Werhane/Munari gapped until verified | closed |
| D1 | EX8 | LAB-SIGNOFF.md; lab_exercise method_id + practises → ACT1/ACT2 | closed |
| D2 | EX8 | `wave1_media_ne_2_labs` empty (exactly two Labs on I.1–I.5 + FIA) | closed |
| D3 | EX10 | `question_bank_present`; practice quizzes under `/practice/en/` | closed |
| D4 | EX10 · AUTOPILOT | APPROVAL.md drafts-only; measurement not started | closed |
| E1 | EX2 | verify-publication-safety.mjs DC-tuned; Ahmes fixture fail-closed | closed |
| E2 | all gates | jekyll_build_ok on every land regression | closed |
| E3 | EX0 · gitflow | excellence/integration + tags excellence/ex0…ex10; gitflow.sh | closed |
| E4 | all | CT patterns reused; no CT CONTENIDOS/technique IDs on student pages | closed |
| E5 | LOCAL-EXECUTION | Ollama local-only; Thessia voice-only (constraint retained) | closed |
| E6 | EX10 · EX11 | Consent drafts + APPROVAL; no DPO clearance claim | closed |
| E7 | gitflow sync | `gitflow.sh start` merges committed main; conflict = stop | closed |

## Out of scope — next cascade / professor

| Item | Why deferred | Decision / pointer |
| --- | --- | --- |
| I.6–I.9 DCI decks + Labs | No media decks yet (placeholders only) | NEXT-CASCADE-CD-II.md §2 (CD I remainder) |
| Full CD II / NM Wave-1 depth | A1 firewall-only | NEXT-CASCADE-CD-II.md |
| B1 full track 1:1 | II.* + NM + I.6–I.9 | Same |
| Measurement / student data | AUTOPILOT §2 | Never started |
| DPO / exhibition clearance | E6 | Consent drafts only |
| Professor ratification (weights, images, Labs, exemplars, consent) | Final review | FINAL-REVIEW.md §2 / §4–§6 |

## Probe targets (EX11 acceptance)

After `bundle exec jekyll build` (gates run this):

- `php_cache_files` = 0
- `lesson_infra_vocab_files` = 0; no special-lecture infra vocab
- CD I EN/ES parity delta = 0; fashion-image-analysis EN present
- ≥6 Wave-1 media decks; each exactly two `lab_exercise`; no Wave-1 dangling slots
- catalogue, references.yml, research-manifest, consent drafts, question-bank present
- guía weights 55/15/20/10; evaluation mentions 55; Sandra PDF + COORDINATION present
