---
description: Whole-course sequential orchestrator for upgrading every CD I and CD II lesson, session prompt, and provenance record
globs: 'digital-creativity-pedagogy/forge/**'
alwaysApply: false
---

# DC CURRICULUM ORCHESTRATOR — CD I + CD II

**Status:** `READY_TO_TRIGGER` — Phase A + B placeholders; profield MP0+ in parallel.

**Audited:** 2026-08-30. This file prepares execution; its existence is not
authorization to edit the repository without an explicit operator go-ahead.

## What already exists (do not destroy)

| Artefact | State | Orchestrator stance |
| --- | --- | --- |
| Student lessons EN/ES (30 pages) | ✅ B1/B2/B3 scaffolds complete | **Upgrade only** — preserve verified prose; patch drift, provenance, boundaries |
| Session prompts (15 × 120 min) | ✅ first filled pass | **Reconcile** with lessons + `MASTER-IDEAS.md`; do not rewrite from scratch |
| `SESSION-PROMPTS-GROUNDING-RECEIPT.md` | ✅ discovery routing recorded | Use as baseline; re-run discovery only when a unit's claim changes |
| `docs/_data/tracks.yml` | ✅ 80/80 h closed both courses | **Verify** totals; do not reallocate |
| Track pages EN/ES | ✅ master-idea tables | Keep **Master idea & rationale** column in sync when unit claims change |
| EN CV (`uem-ruvebal-digital-creativity-*-cv.md`) | ✅ canonical | Spanish mirrors follow EN |
| `teaching-packs/i-*.md` | ◻ stubs only | **Out of scope** for this run unless operator explicitly expands scope |
| `PROVENANCE_LINE` in lessons/prompts | ✗ not yet migrated | **Primary forge gap** for this run |
| Media packs (video/still/graphic URLs) | ✗ prospector not built | **Blocked** — keep reviewed specifications; no invented embeds |
| AFEL formula corpus (12H.FC0–FC4) | ◻ planned | **Out of scope** — do not block lesson upgrade on formula ingestion |
| `FRACTAL-ARCHITECT-CASCADE.execute.md` | separate visual cascade | **Do not substitute** for this run |

`TEACHING-READINESS.mdc` §0 is authoritative on delivery sign-off: scaffold-complete
≠ institutionally released ≠ research-ready ≠ exhibition-ready.

## Operator trigger

Run with repository read/write tools in Cursor (preferred) or a local executor
with the pinned model. The model is an executor, not an authority: it must obey
repository contracts, preserve unrelated worktree changes, and stop at every
gate below.

**Pinned model (2026-08-30):**

```bash
export OLLAMA_MODEL='qwen3:8.28'
```

Use the **Ollama HTTP API** (`ollama.Client(...).chat(...)` with explicit
`timeout=`) for any scripted inference — never `ollama run` in unattended
agent loops. In Cursor, prefer the IDE agent with this execute file as the
controlling prompt and `qwen3:8.28` when the runtime exposes it.

## Agentic machinery — read completely before writing

Read in order:

1. `AGENTS.md` · `TEACHING-READINESS.mdc`
2. `digital-creativity-pedagogy/cv/guides/{1-creacion-digital-i,3-creacion-digital-ii}.json` + live PDF URLs
3. `digital-creativity-pedagogy/oficial-guia-framework.mdc`
4. `digital-creativity-pedagogy/dc-unit-forge.mdc`
5. `digital-creativity-pedagogy/forge/PROVENANCE-LAW.mdc`
6. `digital-creativity-pedagogy/forge/SESSION-PROMPT-FORGE.mdc`
7. `digital-creativity-pedagogy/forge/CRITICAL-FIELD-LAYER.md`
8. `digital-creativity-pedagogy/forge/PROFIELD-MEDIA-PROSPECTOR-REQUEST.md` (spec only — tool not shipped)
9. `digital-creativity-pedagogy/forge/MEDIA-PLACEHOLDER-CONTRACT.md`
10. `digital-creativity-pedagogy/forge/SESSION-PROMPTS-README.md`
11. `digital-creativity-pedagogy/forge/SESSION-PROMPTS-GROUNDING-RECEIPT.md`
12. `digital-creativity-pedagogy/grounding/README.md`
13. `digital-creativity-pedagogy/grounding/MASTER-IDEAS.md`
14. `digital-creativity-pedagogy/cv/UNIT-PLAN.md`
15. The unit's **existing** session prompt, EN lesson, ES lesson, and track-row summary

Apply relevant sections from:

- `~/src/.cursor/skills/curriculum-forger/SKILL.md`
- `~/src/.cursor/skills/user-guide-forger/SKILL.md`
- `~/src/.cursor/skills/visual-forger/SKILL.md`
- `~/src/.cursor/skills/ttod-bridge/SKILL.md` — epigraph proposals only; never hand-edit `ttod.yml`
- `~/src/.cursor/skills/media-embed-forger/SKILL.md` — **embedding stage only** after rights are evidenced

Repository agents: `digital-creativity-pedagogy/.cursor/agents/fractal-architect.md`
covers formula backgrounds only. If visual-forger routed references are
unavailable, emit a plain structured graph spec and stop with `BLOCKED` for
production artwork — do not fake a diagram.

`MASTER-IDEAS.md` is not decorative: for every unit carry master idea, emerging
direction, boundary, and “nail in the lesson” into the session prompt, both
lessons, and the track **Master idea & rationale** row. `UNIT-PLAN.md` and
Profield outputs are routing layers; only Ahmes-resolved evidence may become a
scholarly claim.

## Hard rules (forge failures)

- Do **not** use FE hour schemes (10/30/14), invent official contents or
  competencies, cite vector previews, expose internal grounding metadata in
  public HTML, or bring VTON into scope.
- **English is the canonical authoring language** for new/updated lesson prose,
  CV, and track tables; Spanish must keep outcome parity.
- Every Ahmes-backed claim needs one complete `PROVENANCE_LINE` per
  `PROVENANCE-LAW.mdc` inside the switch-gated `curriculum-internal` comment.
- Media without `MEDIA_RIGHTS_LINE` evidence stays a **reviewed specification**,
  not a live embed.
- **No UDIT mention anywhere in forge output** — lessons, session prompts,
  track pages, methodology edits, synergy copy, vShowroom briefs, receipts, or
  student-facing prose produced by this run. Do not name UDIT, Web Atelier,
  Front-End I/II, or cross-institutional showroom engineering. Refer only to
  **UEM**, **the shared digital showroom (L3)**, **fashion-design CLO workflow**,
  or **sibling web runtime** when a synergy must be named. If an existing file
  contains UDIT and this unit touches it, remove or neutralise that reference
  as part of the unit gate — do not add new ones.

## Ordered whole-course loop

Process sequentially to keep shared registries and provenance auditable:

```text
CD I:  I.1 → I.2 → I.3 → I.4 → I.5 → I.6 → I.7 → I.8 → I.9
CD II: II.1 → II.2 → II.3 → II.4 → II.5 → II.6
```

For each unit, complete every substep before moving on:

1. **Freeze the contract.** Copy official CONTENIDOS and competency codes
   verbatim from JSON; record the `tracks.yml` registry slice. Never fabricate
   a timetable or Campus Virtual procedure.
2. **Load the baseline.** Read the filled session prompt, both lessons, the
   `MASTER-IDEAS.md` row, and the track master-idea cell. List what is already
   verified vs what drifts.
3. **Discover narrowly (only if needed).** If no new claim is introduced, cite
   `SESSION-PROMPTS-GROUNDING-RECEIPT.md` and skip re-query. Otherwise run one
   unit-scoped discovery with `project_slug=profield-digital-creativity` and
   `knowledge_scope=field_prospection`; record exact query, locator, similarity,
   and bounded proposed use.
4. **Resolve evidence.** Resolve candidates in Ahmes; inspect the complete node
   and page; run `ahmes query --cite`; write a complete `PROVENANCE_LINE` beside
   every claim in **both lessons and the session prompt**. Preserve
   `[BIBLIO-GAP]` / `NONE` when evidence is absent or unsafe.
5. **Reconcile the session prompt.** Update the 120-minute guide only where the
   lesson, master idea, or provenance record changed. Keep B1/B2/B3 timing,
   three media cards (as specifications), accessibility fallbacks, and the
   critical field lens + open living prompt.
6. **Reconcile both languages.** Patch EN first, then ES with outcome parity
   (claims, boundaries, media semantics, citations, gated internal provenance).
   Do not regress complete student-facing sections.
7. **Install semantic media placeholders.** For each unit's three media roles
   (video, stills, graphic), write `media_slot_id`, `studio_semantics`,
   `why_this_is_here`, and `viewing_question` into lesson `<figure>` captions
   per `MEDIA-PLACEHOLDER-CONTRACT.md`. Generate placeholder graphics with
   `visual-forger` / `fractal-architect` (UEM palette) or ship video slots as
   poster-still + caption. Mark `placeholder: true` until MP5 accept. **Do not
   invent URLs or licences.** Optional: add `MEDIA_RIGHTS_LINE` only when
   operator supplies a reviewed asset.
8. **Sync the track row.** Update the EN and ES track **Master idea & rationale**
   cells if the unit claim changed. Do not revert to “evidence class” wording.
9. **Reconcile the registry.** Touch only the unit's pedagogical row if hours
   changed (they should not). Verify course totals remain
   10 / 20 / 8 / 14 / 20 / 8 contact-forgeable and 150 h overall.
10. **Run the unit gate.** Fail the unit if any claim lacks a full provenance
    line, any quote exceeds its source boundary, public HTML leaks metadata, a
    media right is misrepresented as resolved, the critical prompt is generic,
    EN/ES outcomes diverge, or **UDIT / Web Atelier** appears in touched
    student-facing copy.

## Phases and blockers

| Phase | Goal | Ready? |
| --- | --- | --- |
| **A — Provenance + reconcile** | `PROVENANCE_LINE` on all claims; session ↔ lesson ↔ track sync | ✅ **Run now** |
| **B — Semantic media placeholders** | `media_slot_id` + caption-first figures; fractal/SVG placeholders | ✅ **Run with Phase A** — see `MEDIA-PLACEHOLDER-CONTRACT.md` |
| **B′ — Licensed embed swap** | Replace placeholders from Profield manifests | ◻ After `~/src/profield` MP5 accept — **not a blocker** |
| **C — Teaching decks** | Optional slides | ◻ Out of scope unless operator opts in |
| **D — Formula backgrounds** | Fractal-architect cascade | ◻ Separate execute file; not a dependency for Phase A |

If Phase B′ (licensed swap) is not ready, Phase A+B still completes with
`COMPLETE_PHASE_AB` and a `media_slot_id` backlog keyed to profield MP5.

**Profield cascade (parallel track):**
`~/src/profield/docs/DEV_PLAN/MEDIA-PROSPECTOR/` — start MP0 (schema + acceptance
harness); does not gate this orchestrator.

## Course and final gates

After each course, verify all units, EN/ES parity, official contents,
competencies, contact totals, citation safety, provenance records, track master
ideas, and UDIT-absence on touched surfaces. Only then run:

```bash
npm run verify:publication
npm run verify:citations
npm run build
```

If unrelated dirty changes exist, do not reset, stash, or overwrite them. If a
gate blocks, leave prior verified units intact and stop with a resume list. Do
not claim completion.

## Pre-flight (operator, 5 minutes)

- [ ] `qwen3:8.28` available locally (`ollama list | rg 'qwen3:8.28'`)
- [ ] Ahmes + Athanor/DevIAC discovery reachable for spot-check cites
- [ ] `npm run build` green on current `main`/branch before the run starts
- [ ] Operator accepts **Phase A + B placeholders**; B′ swap is optional later
- [ ] Operator confirms **UDIT silence** for all forge output this run

## Completion receipt

On success, write
`digital-creativity-pedagogy/forge/DC-CURRICULUM-ORCHESTRATOR.execution.receipt.md`
with:

- model (`qwen3:8.28` or actual), timestamp, phase completed
- every unit: files changed, claim IDs, `PROVENANCE_LINE` status, media-rights status
- track rows touched, UDIT-absence check on edited surfaces
- commands run and final hour totals

Say `COMPLETE` only when all fifteen units pass Phase A+B gates (and B′ only
if explicitly in scope). Otherwise say `COMPLETE_PHASE_AB`, `PARTIAL`, or
`BLOCKED` with the exact gate and resume pointer (`I.4` = next unit, etc.).
