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
