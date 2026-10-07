# PHASE-EX10 cold review — Assessment layer + D2≡ACT3 lock + consent drafts

| field | value |
| --- | --- |
| **phase** | PHASE-EX10 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-10` |
| **implementation commit** | `e7f6d25900b42685434b8471443a9bdb691fd0ae` |
| **verify log** | `PHASE-EX10-VERIFY-LOG.md` — harness `failures: 0` / Exit **0** (commit `e7f6d25`); cold re-run Exit **0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |
| **P0** | none |
| **P1** | none |
| **PARTIAL / residual** | I4/I8/I9 bank gaps (honest); practice quizzes EN-only; FINAL-REVIEW EX10 P0 block still for professor packet |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Bank refs ⊆ lesson front-matter references; higher-order share honest | Exit-gate Ruby: `higher-order share: 30/72 (41.7%)`; `PASS: question bank rules`; cold re-run identical. Gaps I4/I8/I9 listed in `question-bank.yml` (no invented items) | Met |
| TRANSPOSITION-BRIEF EN+ES; cartel + other-language | File present; gate greps `cartel`, `another language`, `otro lenguaje` — all PASS. Substance matches `COORDINATION-SANDRA.md` §3 (D2 ≡ ACT3 cartel from another language). Divergence table filed | Met |
| No consent claiming DPO approval; measurement not started | `APPROVAL.md`: `status: DRAFT`, `approved_by: autopilot (drafts…)`, **Not started.** Consent EN/ES: DRAFT/BORRADOR banners; “DPO approval is not claimed” / “No se reivindica aprobación del DPO”; “never starts” / “No se recogen datos…”. Gate absents + presents PASS | Met |
| Private bank / consent not in `_site` | Gate `PASS: assessment + consent stay private`; cold `rg` for `question-bank.yml\|CONSENT-FORM\|DIVERGENCE-VS-PLAN\|approved_by: autopilot` under `_site` → **0 hits**. Pedagogy excluded in `_config.yml` | Met |
| `PHASE-EX10.exit-gate.sh` exits 0 | Harness log Exit 0; cold re-run Exit 0 (`failures: 0`) | Met |
| Cold review PASS before land | This document → **PASS** | Met |
| Out of scope held | Diff `61cd5d2..e7f6d25`: assessment/consent/practice/retrieval/forge — **no** CD II redesign / Nuevos Medios / VTON / Sandra Campus Virtual edits | Met |

Hard constraints (orchestrator / AUTOPILOT §2 EX10): measurement never starts ✓ · consent drafts-only ✓ · D2≡ACT3 bilingual ✓ · private bank not leaked ✓ · exit gate 0 ✓.

---

## Spot checks (cold session)

### Exit gate (re-run)

```text
$ bash digital-creativity-pedagogy/excellence/PHASE-EX10.exit-gate.sh
… (all PASS lines as in VERIFY-LOG) …
higher-order share: 30/72 (41.7%)
PASS: question bank rules
PASS: retrieval slides (optional, consistent)
PASS: jekyll build
PASS: publication safety
PASS: practice quiz i-1-digital-images … fashion-image-analysis
PASS: assessment + consent stay private
----
failures: 0
EXIT:0
```

Matches harness `PHASE-EX10-VERIFY-LOG.md` (implementation commit `e7f6d25`, failures 0).

### Full suite (pre-existing)

```text
$ node scripts/validate-decks.mjs --strict --rights=flag
validate-decks: 13 deck file(s), 0 error(s), 170 warning(s) [strict; rights=flag]
EXIT:0

$ npm test
# tests 45
# pass 45
# fail 0
TEST_EXIT:0
```

### Bank vs lesson text (14 items)

| ID | Lesson support | Notes |
| --- | --- | --- |
| I1-01 | I.1 Masterclass field-of-practices list (Shinkle 2008, 15) | Match |
| I1-02 | Same paragraph: shared goals and contexts | Match |
| I1-10 | Lab Exercise 1: practice · agents · venues · interests | Match |
| I2-01 | Vector path = set of relations (points/handles/fills) | Match |
| I2-05 | Hüppauf/Wulf three-way check carried in I.2 | Match |
| I3-01 | LO + Masterclass: fixed grid; mode/depth/gamut foreclose | Match |
| I5-01 | Papahristou 2024, 5: third year + 2D CAD after traditional | Match |
| I5-04 | Form-understanding evidence trail (2D read · sketch→volume→digital · divergence sentence) | Match |
| I6-01 | Coats 2026 Denim Project constructivist/experiential | Match |
| I6-04 | Sustainability scepticism as discussion prompt, not pedagogy proof | Match |
| I7-01 | Campinho Google Images “fat body” / “obese body” | Match |
| I7-02 | Empowerment vs medicalised fragmentation | Match (see F1 paraphrase) |
| FIA-01 | Kandinsky looking order (2012, 9) | Match |
| FIA-02 | Morphological chain dot→…→space/perspective | Match |

### D2 ≡ ACT3

- EN brief: cartel + another language + one bilingual deliverable (no English-only competitor).
- ES brief: cartel + otro lenguaje + same substance.
- `DIVERGENCE-VS-PLAN-DE-TRABAJO.md`: object/axes **None** on substance; critical lenses **Logged** held (C5/EX6).
- Public Evaluation page still names the same cartel task (pre-existing EX1 lock + EX10 brief).

### Retrieval slides

Units with `deck:` (I1–I3, I5, FIA): exactly one `retrieval` immediately before `lab_opener`; 5 questions; geometrical; notes contain Answers. I6/I7 correctly have `deck: nil` (optional). Notes state practice-only / nothing collected.

### Practice quizzes

Seven public pages under `_site/practice/en/*/`; each ≥5 `data-question`; index states not graded / nothing recorded. Sample I1-01 answer (A) matches bank and lesson.

---

## Findings

### F1 — I7-02 answer wording vs lesson sentence · **P2** · does not block DONE

**Evidence:** Lesson: “contrasting patterns of empowerment and medicalised fragmentation”. Bank answer: “Empowerment expressions versus medicalised fragmentation…”. Provenance quote uses “expression of empowerment”; stem is still lesson-true.

**Fix (optional):** Align bank answer to the published lesson sentence before professor bank approval.

### F2 — Unit `ref` is ⊆ lesson refs, not always the supporting cite for the stem · **P2** · does not block DONE

**Evidence:** Gate enforces `ref ∈ lesson front matter` (Acceptance). Some stems (e.g. I2 vector-path literacy) are classroom pedagogy while `ref` may be one of the unit’s few verified keys. Not an invented citation key; attribution can read looser than the Masterclass pin.

**Fix (optional):** Prefer `ref` pins that appear in the same Masterclass paragraph as the tested claim, or add an explicit `claim_source: classroom` field in a later bank schema (would need gate amendment + cold review).

### F3 — Practice quizzes EN-only · **P2** · does not block DONE

**Evidence:** `docs/practice/en/**` only; Acceptance does not require ES. AUTOPILOT teaching languages are EN+ES.

**Fix (residual):** ES mirrors under `docs/practice/es/` if professor wants parity before release (not required to land EX10).

### F4 — FINAL-REVIEW lacks EX10 P0 checklist section · **P2** · does not block DONE

**Evidence:** `DECISIONS-LOG.md` has EX10 draft/measurement/ACT3 entries; `FINAL-REVIEW.md` still only previews EX10 under autopilot. AUTOPILOT §5 wants consent/brief in the final packet — land/EX11 territory, not EX10 Acceptance.

**Fix:** Append EX10 P0 block (bank, brief, divergence, consent) when assembling FINAL-REVIEW.

### F5 — Exit gate measurement language asymmetric EN vs ES consent · **P2** · does not block DONE

**Evidence:** Gate asserts EN “never starts|No data are collected…”. ES correctly contains “no empieza” / “No se recogen datos…” but is not `present`-asserted. Draft banners and DPO absent checks cover both files.

**Fix (optional):** Add ES present checks in a gate amendment (cold-reviewed) — not a silent weaken.

---

## Downstream / amend-on-surprise

No cascade world-model break. I4/I8/I9 gaps remain as logged; do not invent refs in EX11. Steimberg/Werhane/Munari stay **held** in the brief (C5/EX6) — professor wording review before release.

---

## Verdict

| **verdict** | PASS |
| **P0** | none |
| **P1** | none |

Eligible for land after orchestrator policy (`gitflow.sh land`); reviewer does not land.
