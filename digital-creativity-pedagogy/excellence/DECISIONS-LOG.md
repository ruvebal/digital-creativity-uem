# Decisions log — DC Excellence

Append-only. Format:

`YYYY-MM-DD · EXn · decision · rule applied · alternatives · how to undo`

---

2026-10-07 · launch · Clone CT Excellence pack structure for DC; Wave-1 = CD I + fashion-image-analysis; D2≡Sandra ACT3; weights 55/15/20/10 from guía · AUTOPILOT §0 · n/a · amend AUTOPILOT + INDEX

2026-10-07 · EX0 · Lock 55/15/20/10 from guía JSON + D2≡ACT3 + Wave-1 scope · AUTOPILOT §0/§2 · alt: wait for Campus Virtual reconfirm · undo: amend DECISION-EX0-GUIA.md + re-verify
2026-10-07 · EX0 · gitflow init already done (excellence/base @ 98ef567); start opened cascade/excellence-0 · AUTOPILOT §3 · n/a · gitflow.sh rollback 0 after land if needed

2026-10-07 · EX1 · Publish 55/15/20/10 + D2≡ACT3 cartel lock on evaluation + How-to-Pass decks; Workshop from s4 · AUTOPILOT §2 EX1 / DECISION-EX0 · alt: keep vague "see guía" · undo: revert evaluation + how-to-pass JSON

2026-10-07 · EX2 · Rewrite AI footers to one-sentence form; gate PROVENANCE/VOICE into publish_internal comments; firewall CD II lessons · AUTOPILOT §2 · alt: leave footers · undo: revert lesson index.md batch
2026-10-07 · EX2 · Expand safety patterns (lesson-scribe, Profield prose, UDIT, web-atelier, Thessia, vault); strip UDIT archive_covers; redact tracks campaign_ledger; gate PROVENANCE; one-sentence AI footers; Ahmes fixture proves fail-closed · AUTOPILOT §2 / FINDINGS C1 E1 · alt: leave NM redesign · undo: revert safety script + lesson/track scrub

2026-10-07 · EX3 · Port CT media-rules + validate-decks; Wave-1 schema_version 2 contract documented but decks stay legacy until EX4; profield-cache orphans warn-only (do not delete); deck-media orphans error; outside Wave-1 always warn · AUTOPILOT §0/§2 · FINDINGS B2 B3 · alt: delete orphans / migrate all decks now · undo: revert scripts/ + forge pointers + curation/
2026-10-07 · EX3 · EX3 exit gate focused on validator+tests (no Jekyll) so harness stays light; `npm run build` still runs validate:decks · AUTOPILOT §2 · alt: keep jekyll in EX3 gate · undo: amend PHASE-EX3.exit-gate.sh


2026-10-07 · EX4 · Auto-pick best-fitting Commons/NYPL/Profield candidates per Wave-1 slide (brief ≥ 4/5 via local qwen3.8:27b think:false); doubt → rights_status flagged; approved_by autopilot (final review pending) · AUTOPILOT §2 EX4 · alt: leave legacy rank-deal · undo: revert Wave-1 content.json + curation/ + rehydrate
2026-10-07 · EX4 · Migrate rehydrate off rankCursor → bindSlides; schema_version 2 on I.1–I.5 + ML-FIA; keep profield-cache orphans (warn only) · EX3 cold-review F2 / FINDINGS B2 B3 · alt: keep rank dealing · undo: restore legacy rehydrate
2026-10-07 · EX4 · ML-FIA lab-2 stays diagram (no cleared student-owned image); I.3 analysis-model rebound to Kawakubo 01 after vision floor miss · AUTOPILOT conservative · alt: invent student photo · undo: re-bind from bindings.json
2026-10-07 · EX4 · P0 F1 fix: I.3 analysis-model unbound Kawakubo (vision fit 2) → Albers CC0 nested squares (vision fit 5); shortlist/bindings/registry aligned to vision.json · AUTOPILOT §2 brief≥4/5 · alt: diagram fallback · undo: restore Kawakubo binding from prior commit

2026-10-07 · EX5 · Port CT deck pre-renderer for Wave-1 (render-decks + deck-render.mjs); henon SVGs keep 12-hex content hashes; diagram fallback = fractal-triangles/uem-diagram-fallback-* · AUTOPILOT §2 / FINDINGS B4 B5 · alt: keep runtime fetch · undo: revert scripts/lib/deck-render.mjs + scripts/render-decks.mjs + includes
2026-10-07 · EX5 · Speaker notes drafted for every Wave-1 masterclass/lab/opener/cover slide; enhancement-only student-media-deck.js (data-base-url, no Date.now, no hard-coded base) · FINDINGS B4 · alt: notes only on masterclass · undo: strip notes fields from content.json
2026-10-07 · EX5 · Align CSS + forge golden rule 1 clamps (22px/2.6vw/38px · h1 2.15rem/6.6vw/3.15rem); layout recovery (no 62vh min-height, section overflow visible, lab skips duplicate prompt when portfolio_trace set); browser deck-layout.mjs in EX5 gate (Wave-1 only) · FINDINGS B4 · AUTOPILOT §2 · alt: weaken type floors · undo: revert pass-track-deck.css + forge golden-rule paragraph + deck-layout.mjs

2026-10-07 · EX6 · Single bibliography: only Ahmes page-verified works in `references.yml`; gaps stay in `research-manifest.yml`; PARTIAL OK · AUTOPILOT §2 EX6 / FINDINGS C2 C3 C5 · alt: invent cites or leave hand-written spans · undo: revert references.yml + include + Wave-1 lesson front matter
2026-10-07 · EX6 · Critical layer Steimberg 2013 / Werhane 2026 / Munari method = gap (held or wrong edition); no student cite until EX10 brief · AUTOPILOT conservative · alt: force unverified pin · undo: amend manifest + place claim
2026-10-07 · EX6 · Kandinsky 2012 p.9 verified from Dover coat 5c285f15 page_index 9 · AUTOPILOT vault rule · alt: leave ML-FIA cite as gap · undo: demote key + remove from references.yml

2026-10-07 · EX6 · Fix cold P1 F1 Rubin page 42→123 in I.1; F2 Coats sustainability public_citation 8→4 to match printed_page · AUTOPILOT conservative · alt: leave PARTIAL mismatches · undo: revert those two lines

2026-10-07 · EX7 · Fashion-craft catalogue (60 methods) under pedagogy/catalogue; public seed at methods/en/cards + fashion_craft_methods.seed.yml; ACT1/ACT2 anchors required; no CT technique IDs · AUTOPILOT §2 / FINDINGS C4 · alt: copy CT techniques (forbidden) · undo: revert catalogue/ + docs/methods + seed data + EX7 gate
2026-10-07 · EX7 · Verified sources only when already in references.yml (11); held/gap honest for Gestalt/photobash/figurín pedagogy blanks · AUTOPILOT conservative · alt: invent Arnheim/Abling pages · undo: demote verified keys in emit_catalogue.py
2026-10-07 · EX7 · Include `methods` in _config.yml so seed path builds; SEED.md avoids local path strings for publication safety · AUTOPILOT · alt: leave seed private-only · undo: revert _config include + SEED.md
2026-10-07 · EX8 · Target Labs I.1–I.4 ACT1/ACT2 + selected I.5; approved_by autopilot (final review pending); held/gap ACT anchors as classroom adaptations · AUTOPILOT §2 EX8 / EX7 F2 / FINDINGS D1 D2 · alt: invent Abling/Arnheim pages (forbidden) · undo: revert Wave-1 lab slides + B2 cards + LAB-SIGNOFF
2026-10-07 · EX8 · I.1 Directory Lab → optional outside-class; I.2 drops lab-3 (forge: exactly two lab_exercise) · AUTOPILOT conservative / D2 · alt: keep three Labs · undo: restore lab-3 + Directory as Lab 2
2026-10-07 · EX8 · I.6–I.9 Labs deferred to EX9 (no DCI decks yet) · AUTOPILOT scope · alt: forge decks early · undo: amend LAB-SIGNOFF selection note
2026-10-07 · EX8 · I.2 lab-3 curated asset rebound to lab-2; orphan deck-media 152b234… removed · validator orphan rule · alt: keep third Lab · undo: restore lab-3 slide + asset

2026-10-07 · EX9 · Wave-1 lesson spine = Learning objectives → Analysis → Masterclass → Lab → Workshop → Conclusion → Tao of the Image → References (B1/B2/B3 labels dropped); Workshop first line states session timing · AUTOPILOT §2 / forge SESSION-RHYTHM + dc-unit-forge · FINDINGS A3 · alt: keep B-labels · undo: revert lesson H2 renames
2026-10-07 · EX9 · I.6–I.9 Labs = structural placeholders (no 2627-dci decks); I.1–I.5 ES B2 cards ported from EN with EX8 English field labels · EX8 deferral / AUTOPILOT conservative · alt: forge I.6–I.9 decks now (out of EX9) · undo: restore prior ES Lab bodies
2026-10-07 · EX9 · Example traces are illustrative professor-made drafts (not student work); flagged for FINAL-REVIEW P0 · AUTOPILOT §2 EX8-style · alt: leave Labs without traces · undo: strip **Example trace:** blocks
2026-10-07 · EX9 · Lesson figures reuse EX4/EX5 deck assets via lesson_figures.json + lesson-figure.html; hreflang emits es only when built page exists and differs · CT EX9 A5 pattern · alt: keep always-on es alternate · undo: revert head-hreflang.html

2026-10-07 · EX10 · Consent + bank + transposition brief = drafts only; measurement never starts · AUTOPILOT §2 EX10 / FINDINGS D3 D4 E6 A2 C5 · alt: invent DPO clearance (forbidden) · undo: revert assessment/ + consent forms + practice pages
2026-10-07 · EX10 · Bank covers I1–I3, I5–I7, FIA only; I4/I8/I9 empty lesson refs → gap (no invented cites) · AUTOPILOT conservative · alt: invent refs for empty lessons · undo: amend question-bank.yml gaps
2026-10-07 · EX10 · Lock TRANSPOSITION-BRIEF EN+ES ≡ ACT3 cartel from another language; divergence table filed · COORDINATION-SANDRA §3 / A2 · alt: English-only competing brief (forbidden) · undo: revert assessment/TRANSPOSITION-BRIEF.md
