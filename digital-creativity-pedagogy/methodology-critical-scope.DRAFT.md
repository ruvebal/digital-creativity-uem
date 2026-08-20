# DRAFT — unapproved proposal for the DC methodology page

> **Status: DRAFT, NOT PUBLISHED, NOT APPROVED.** This file lives in
> `digital-creativity-pedagogy/` (the non-published pedagogy side of this
> repo) on purpose — per
> `~/src/profield/.cursor/skills/curriculum-publication-head/SKILL.md`
> rule 5, student-facing prose is never published automatically; it
> requires the content owner's (Rubén's) explicit approval. **Do not copy
> this text into `digital-creativity-uem/docs/methodology/en/index.md`
> without that approval.**
>
> **Target file:** `docs/methodology/en/index.md` (repo root
> `digital-creativity-uem`, i.e.
> `~/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem/docs/methodology/en/index.md`).
> **Proposed insertion point:** a new `## Critical scope` section, inserted
> after the existing `## Studio cycle` section and before `## Shared
> artefact` — the current page is short (four H2 sections, 38 lines total)
> and has no critical-pedagogy section at all yet; this proposal adds one
> rather than editing an existing section, since none currently touches
> this ground.

---

## Diff-style summary of what would change

- **No existing text is removed or altered.** The current
  `## Why a methodology of its own`, `## Studio cycle`, and `## Shared
  artefact` sections stand as published.
- **One new H2 section is added**, `## Critical scope`, inserted between
  `## Studio cycle` and `## Shared artefact`.
- **The page's `tags:` frontmatter already lists `critical-pedagogy`** —
  this draft is the first section that actually cashes that tag out into
  content; currently nothing on the page explains what "critical-pedagogy"
  means for this course.
- Net addition: ~300 words, 1 new H2 section, 7 new citations, 0 deletions.

---

## Proposed new section (verbatim text, pending approval)

## Critical scope

Digital Creativity's own field-prospection corpus names three critical
strands this course draws on directly: fashion and the digital world
(power, platform, authorship), fashion and virtuality (avatars, AR,
immersion), and — the strand most directly load-bearing for this section —
gender, minorities, and silences in fashion's digital representation. These
are not a separate "ethics week"; each strand's claims are grounded in the
specific technology a unit already requires the student to operate.

Two lineages of critical-technology scholarship apply across every unit
that teaches or requires a generative or algorithmic tool: a classical
strand concerned with who holds access to technical/creative authority in a
studio (Postman & Weingartner), and a contemporary strand treating
generative and recommendation systems as political, not neutral (Postman's
*Technopoly*). Concretely, in this course:

- **Avatar, AR, and generative-image units** are already standing on a
  representational question this course's own C3 strand documents
  directly: contemporary image-generation and classification systems "can
  reproduce intersectional gender and racialization inequalities," meaning
  the tools used to produce fashion imagery cannot be treated as neutral
  representational infrastructure (AlDahoul, Rahwan & Zaki 2025, DOI
  10.1038/s41598-025-99623-3) — a claim this course asks students to test
  against their own generated output, not take on faith.
- **Portfolio and platform-facing units** — any unit where a student's work
  becomes visible through a third-party platform's own infrastructure —
  are already standing on the same platform/publisher distinction the FE
  side of this studio grounds via Orrange: the moment a student's process
  or output depends on a platform's own distribution and ranking logic,
  authorship and infrastructure are no longer separable questions (Orrange
  2020, 42).
- **Any unit introducing a new generative tool** carries a design and
  cognitive cost worth naming alongside its creative one: interface
  affordances shape what a student believes the tool can do before any
  instruction is given (Norman 2013, 30), and tool-induced anxiety under
  deadline pressure narrows exactly the exploratory thinking studio work
  depends on (Norman 2004, 32).

**Where the evidence stands, stated plainly.** The cross-institution
sources above (Norman, Postman, Orrange) are grounded to the
`evaluator_safe` standard in this studio's shared didactics vault. The C3
strand's own domain claim above (AlDahoul, Rahwan & Zaki) carries a
checkable DOI and an `[ESTABLISHED]` confidence tag from this course's own
Pass-1 research map, but — unlike the cross-institution sources — has not
yet been run through this session's Ahmes coating/evaluator-safe gate the
way the FE side's parallel corpus has; treat it as citable-with-DOI, not
yet CV-bibliography-grade, until that pass is done.

**Sources:** AlDahoul, N., Rahwan, T., & Zaki, Y. (2025), "AI-generated
faces influence gender stereotypes and racial homogenization," *Scientific
Reports* 15, 14449, DOI 10.1038/s41598-025-99623-3 · Norman, D. A. (2013),
*The Design of Everyday Things* (Revised and Expanded Edition), Basic
Books · Norman, D. A. (2004), *Emotional Design: Why We Love (or Hate)
Everyday Things*, Basic Books · Postman, N. & Weingartner, C. (2009
reissue; orig. 1969), *Teaching as a Subversive Activity* · Postman, N.
(1992), *Technopoly: The Surrender of Culture to Technology* · Orrange,
R. M. (2020), *The Corporate State: Technopoly, Privatization and
Corporate Predation*, Routledge.

---

## Grounding ledger for this draft (Ahmes node + page + evaluator_safe)

| Claim | Coat | Node | Page | `evaluator_safe` |
| --- | --- | --- | --- | --- |
| Affordances definition | `norman_donald_a_the_design_of_everyday_things_..._f31e7737` | `7eed103c-d32d-59a3-bdc4-fb4160536332` | 30 | yes (method=human, confidence=1.0) |
| Anxiety narrows thought | `norman_donald_a_emotional_design_..._f70b91b4` | `3ca6136c-a219-5950-a676-61b2a5cddaac` | 31 (cited p.32) | yes (confidence=1.00) |
| Postman & Weingartner, schools passage | `teaching_as_a_subversive_activity_..._3f62f602` | `de5449a8-d7d1-579b-ab6a-34245a83629f` | 8 | yes (confidence 0.95) |
| Technopoly definition | `postman_neil_technopoly_..._01694c02` | `48ba02e5-d5a8-5111-9057-24976db87122` | 13 | yes (method=human, confidence=1.0) |
| Platform vs. publisher | `robert_m_orrange_the_corporate_state_..._14fcf2a0` | `c124e980-dbf9-5c5f-a8b8-65f62e32ac70` | 41 (cited p.42) | yes (confidence=1.00) |
| AI-generated faces / gender & racial bias | `digital-creativity-pedagogy/grounding/temario/C3-gender-minorities-silences.pass1.resultant.mdc` line 17–22 | — (not yet Ahmes-coated) | — | **no — DOI-checkable Pass-1 map claim only, not yet evaluator_safe** |

The five cross-institution rows are the same nodes cited in the parallel FE
draft (`frontend-pedagogy/methodology-critical-scope.DRAFT.md`) — this
studio's didactics vault (`profield-didactics`) is shared infrastructure,
not duplicated per institution, so both drafts cite the identical nodes
rather than re-deriving separate FE and DC versions of the same claim.

## What this draft does NOT do

- It does not claim DC's own critical-pedagogy corpus (C1–C3) has been
  through the same evaluator_safe audit pass the FE side's
  `03-temario-critica` run has — that audit was not run for DC in this
  task, and this draft says so explicitly rather than implying parity it
  cannot back.
- It does not assert a DC "capstone" or "defence" pairing parallel to FE's
  Units 11–12 — no forge-file text read for this task named one; see
  `curriculum-forger/references/curricular-form-lexicum.yaml`'s `capstone`
  and `defence / viva` entries, both flagged `[UNVERIFIED for this task's
  file set]` on the DC side.
- It does not publish itself. It is a proposal for Rubén to review, edit,
  reject, or approve before any copy moves into `docs/methodology/`.
