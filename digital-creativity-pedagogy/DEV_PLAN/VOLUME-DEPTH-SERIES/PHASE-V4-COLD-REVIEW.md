# PHASE-V4-COLD-REVIEW — Volume–Depth Series (V0–V4)

**Reviewer:** local Ollama `qwen2.5:72b-instruct-q4_K_M` (not the implementing Cursor session)
**Date:** 2026-11-14
**Packet:** measured counts + hard constraints + gate notes (no full git dump)

### PHASE-V4-COLD-REVIEW.md

#### F1: I.6 Figure Count
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** I.6 EN figure count is 8, which meets the requirement of ≤9 figures.
- **Fix:** No action needed.

#### F2: Panofsky Kit Not in I.6 Body
- **Severity:** P1
- **Blocks_DONE:** Yes
- **Evidence:** The commit `fbe7462` parks Panofsky for ML-B, but the commit message does not explicitly confirm that Panofsky is not in the I.6 body. The cascade surface publication shows no findings on this, but the commit message is ambiguous.
- **Fix:** Verify that Panofsky content is not in the I.6 body and update the commit message to explicitly state this.

#### F3: Perspective-Kit Diagrams in ML-B
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** ML-B has 3 perspective-kit diagram sources, which meets the requirement.
- **Fix:** No action needed.

#### F4: ML-A Assets Bound
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** ML-A assets bound: 4 (Venetian, vanishing, cliff, depth-cues), which meets the requirement.
- **Fix:** No action needed.

#### F5: ML-B Assets Bound
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** ML-B assets bound: 2 (Dürer lute, Messung 181) with source_file_url, which meets the requirement.
- **Fix:** No action needed.

#### F6: Review-State Assignments
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** All six live IDs have the correct review-state assignments (project_id=ml unit_id=ML-VD-A|ML-VD-B).
- **Fix:** No action needed.

#### F7: Stale Review-State
- **Severity:** P1
- **Blocks_DONE:** Yes
- **Evidence:** The stale review-state lists `Durer_Perspective.jpg` and `Durer_Underweysung_der_Messung.jpg` as not bound in the deck, which contradicts the claim that ML-B assets are bound.
- **Fix:** Ensure that these assets are correctly bound in the ML-B deck and update the review-state.

#### F8: DECK_ROOTS Rehydrate
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** DECK_ROOTS used for rehydrate: `docs/tracks/en/uem/2627-ml`, which meets the requirement.
- **Fix:** No action needed.

#### F9: Cascade Decks Validate
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** Cascade decks validate, and publication is clean on VD/I.5/I.6.
- **Fix:** No action needed.

#### F10: Whole-Repo Publication
- **Severity:** P2
- **Blocks_DONE:** No
- **Evidence:** The full-repo publication/citation still fails on I.7 / neoplastic / platonic-favicon, but this is out of cascade scope.
- **Fix:** No action needed.

### VERDICT: PASS-WITH-AMENDMENTS

## Implementer triage (post-Qwen)

| Finding | Disposition |
| --- | --- |
| F2 | **Dismissed** — measured: `rg pv-p\|perspective-kit` on I.6 EN/ES lesson bodies → no matches. Commit-message ambiguity is not surface evidence. |
| F7 | **Amended** — fake ids `Durer_Perspective.jpg` / `Durer_Underweysung_der_Messung.jpg` set `status: rejected`, `assignments: []` in `profield/runs/media-prospector/review-state.json`. Live binds remain lute + Messung 181. |
| F1, F3–F6, F8–F10 | Accepted as non-blocking / informational. |

Programme report status remains **PARTIAL** solely because whole-repo gates stay red on out-of-scope I.7 / neoplastic / platonic dirt.
