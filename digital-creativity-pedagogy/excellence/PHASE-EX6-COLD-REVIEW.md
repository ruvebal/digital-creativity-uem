# PHASE-EX6 cold review — Research grounding + bibliography (Wave-1)

| field | value |
| --- | --- |
| **phase** | PHASE-EX6 |
| **worktree** | `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-6` |
| **implementation commit** | `d8728ae518a3f1208bb00f1d8f3097b17a415607` (verify log commit `c5704ca`) |
| **verify log** | `PHASE-EX6-VERIFY-LOG.md` — harness `failures: 0` / Exit **0**; cold re-run Exit **0** |
| **reviewed** | 2026-10-07 |
| **verdict** | PASS |
| **PARTIAL** | Allowed (AUTOPILOT §2 EX6): **10 verified / 36 gap** |

Reviewer did not implement this phase. Status not flipped to DONE. No land / push.

---

## Acceptance vs evidence

| Acceptance item | Evidence | Result |
| --- | --- | --- |
| Probe/gate: uncited references scoped → 0 or documented | Gate `absent "no hand-written reference spans"` + Ruby: every EN front-matter key is `#ref-` cited; gap keys never `#ref-` linked (0 hits) | Met |
| Every Wave-1 lesson References resolve to manifest keys | EN I.1–I.9 + ML-FIA + ES CD I: `{% include references.html %}`; FM keys ⊆ `references.yml` ⊆ verified manifest | Met |
| No vector snippets in student HTML | Cold scan of 22 Wave-1 `_site` HTML files for Ahmes/Athanor/DevIAC/`extraction.db`/`PROVENANCE_LINE`/coat/node patterns → **0 hits**; `node scripts/verify-publication-safety.mjs` → passed | Met |
| `PHASE-EX6.exit-gate.sh` exits 0 | Cold re-run → `failures: 0` / `EXIT:0` | Met |
| Cold review PASS before land | This document | Met |
| Deliverables: manifest + single bibliography + honest gaps + D2 critical works | `research-manifest.yml` (46 works); `docs/_data/references.yml` (10); Steimberg/Werhane/Munari present as **gap** | Met (PARTIAL) |

---

## Spot checks (cold session)

### Exit gate (re-run)

```text
$ bash digital-creativity-pedagogy/excellence/PHASE-EX6.exit-gate.sh
PASS: file digital-creativity-pedagogy/excellence/research-manifest.yml
PASS: file docs/_data/references.yml
PASS: file docs/_includes/references.html
PASS: file digital-creativity-pedagogy/excellence/PHASE-EX6.md
PASS: no hand-written reference spans in Wave-1
PASS: manifest, refs and citations agree
PASS: jekyll build
PASS: publication safety
PASS: built #ref- anchors resolve
----
failures: 0
EXIT:0
```

### Manifest / bibliography integrity

```text
works=46 verified=10 gap=36 refs=10
verified==refs? true
D2 steimberg-2013: status=gap vault=coat d639c32d
D2 werhane-2026: status=gap vault=coat 96302b7e
D2 munari-design-method: status=gap (partial coats 84c0fd33, 65912961 — wrong works)
gap #ref hits in Wave-1 EN: 0
```

I.4 / I.8 / I.9 EN (and ES twins) have empty `references: []` — honest PARTIAL, not invented cites.

### Sample pins (Shinkle 15, Roivainen 8, Coats 8, Papahristou 5, Kandinsky 9)

| Pin | Coat | Ahmes check | Student cite |
| --- | --- | --- | --- |
| Shinkle 15 | `1936070c` node `cca1472b…` | `page_index=14`; text has “wide array of practices” + “shifting and highly permeable” → printed **15** | Matches I.1 / ML-FIA |
| Roivainen 8 | `47ce5b17` node `307e67e0…` | `page_index=7`; “editing styles that are popular at a given moment” → printed **8** | Matches I.3 |
| Coats 8 | `6d1a7b81` node `b3ded30f…` | `page_index=7`; hybrid iteration + student sustainability scepticism on **same node** → printed **8** | Matches I.6 body (see F2 on provenance sibling) |
| Papahristou 5 | `20e79483` node `88bcdad6…` | `page_index=4`; IHU 2D→3D / theory–lab split → printed **5**; AMFI case `a196bf7e…` printed **3** | Matches I.5 |
| Kandinsky 9 | `5c285f15` node `017a3864…` | `page_index=9` exists (“star of straight lines…”); POINT chapter is `page_index=8` | Pedagogical “looking order” gloss is broader than that node — see F3 |

D2 coats on disk: Steimberg `d639c32d`, Werhane `96302b7e` held; Munari method text not held (Circle / anthology only) — gap reasons match vault.

### Publication firewall

```text
Publication safety passed: no internal corpus or local-architecture metadata is publishable.
Wave-1 HTML leak scan: 0 hits
```

---

## Findings

### F1 — I.1 closing paragraph cites Rubin page 42; verified pin is page 123

- **Severity:** P1  
- **Blocks DONE:** no (Acceptance + exit gate met; one locator drift, not an invented work or gap `#ref-`)  
- **Evidence:** Ahmes coat `574691eb` node `b9d0c0a0…` = taste/editing at `page_index=122` (printed 123). Same lesson correctly cites `(Rubin 2023, 123)` at L75 and in PROVENANCE; closing L171 uses `(Rubin 2023, 42)` while page 41–42 is the Listening chapter, not the taste pin.  
- **Fix:** Change L171 public cite to `(Rubin 2023, 123)` (or split taste vs listening with both pages). Do before release polish / EX9 if not sooner.

### F2 — I.6 sustainability-caveat PROVENANCE_LINE points at wrong node/page

- **Severity:** P1  
- **Blocks DONE:** no (student-facing `(Coats 2026, 8)` is supported by `b3ded30f` on printed 8)  
- **Evidence:** `I.6.claim.sustainability-caveat` sources `e4ea7122…` at `page_index=3` / `printed_page=4` (systemic overproduction framing) while `public_citation` is page **8**. Student scepticism text lives on `b3ded30f` (printed 8) with the hybrid claim.  
- **Fix:** Retarget provenance `source=` to `b3ded30f` (or cite both pages honestly). Manifest claim text that collapses both ideas onto “p. 8” can stay if both remain on that folio via the correct node.

### F3 — Kandinsky “looking order” gloss exceeds sampled node on p.9

- **Severity:** P2  
- **Blocks DONE:** no (DECISIONS-LOG accepts Dover p.9; POINT/LINE pages 8–9 hold the vocabulary; not a fabricated work)  
- **Evidence:** Node `017a3864…` on page_index 9 is only the “star of straight lines…” sentence; ML-FIA body teaches point→line→plane as a looking order.  
- **Fix:** Optional EX9: pin POINT (`page_index=8`) and/or soften public locator, or add a second node that supports plane vocabulary.

### F4 — ES Wave-1 lists References but has no in-text `#ref-` hrefs

- **Severity:** P2  
- **Blocks DONE:** no (gate scopes EN `SCOPED_LESSONS`; bibliography IDs render; implementer flagged EX9 parity)  
- **Evidence:** e.g. `_site/.../creacion-digital-i/i-1-.../index.html` has `id="ref-shinkle-2008"` etc. and `hrefs []`.  
- **Fix:** EX9 bilingual cite parity when body pins are translated.

No open P0.

---

## Downstream

PARTIAL procurement (Albers, Curcic, Entwistle, Munari method, Steimberg/Werhane page pins) remains EX9/EX10 — do **not** amend later phase files to pretend those are verified. FINDINGS C2/C3 addressed for Wave-1 bibliography; C5 remains gapped until EX10 D2 brief (honest).

---

## Verdict

| **verdict** | PASS |

Eligible for product-owner promotion to DONE / land on `excellence/integration` after triage of P1 F1–F2 (locator/provenance hygiene; non-blocking for exit gate). PARTIAL standing is intentional under AUTOPILOT §2. Do not mark DONE in this review; do not land from the cold-reviewer session.

## Round-2 note

P1 F1/F2 fixed on phase branch (Rubin 123; Coats sustainability public_citation p.4). Re-verified.
