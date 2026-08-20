# Prompts to replicate — gap-fields, CD CV forge, and temario union

**FE → DC translation** of Web Atelier  
`frontend-pedagogy/grounding/gap-fields/PROMPTS-REPLICATE.md`  
**Do not execute this file as an agent task list until an operator pastes a section into a new session.**

Copy-paste §1–§3 into a Cursor agent on the **digital-creativity-uem** workspace (or a CD-only thread). Vaults stay in `~/ahmes-library` — never duplicate PDFs into the teaching repo.

| FE (source prompt) | DC (this file) |
| --- | --- |
| `profield-frontend-pedagogy` | `profield-digital-creativity` |
| `~/…/web-atelier-udit/frontend-pedagogy/grounding/` | `~/…/digital-creativity-uem/digital-creativity-pedagogy/grounding/` |
| `fe-*/20260815` | `dc-*/20260816` |
| FE II Units 2–4, 7, 10 | CD I/II units **I.2–I.9 · II.1–II.6** (see `../cv/UNIT-PLAN.md`) |
| Astro / PWA / WebSocket / performance | 2D craft · 3D volume · retouch · avatar · video · portfolio web · AR/hologram · motion/still · digital fashion experience |
| PLATFORM-NOTES-POLICY (vendor web) | Tool docs = HOW only; **VTON out of sprint**; Ladder A/B for FE sister coats |

---

## 1 · Prompt: create / refresh `gap-fields/` (CD)

```text
You are working in Creación Digital (UEM) pedagogy grounding.

Context:
- Profield gap runs live at ~/src/profield/runs/dc-*/20260816/
- Ten fields (plus omnibus digital-creativity): see GAP-PROSPECTION-INDEX.mdc
- Typical artefacts: pass1.gpt.deep-research.raw.md, pass1.edited.md, pass1.prompt.md,
  DOI-acquisition-seed.md, source-pdfs/, optional pass2.*.md / identifier-queue-report.json
- Ahmes batch-manifest.json under source-pdfs/.ahmes/ → ~/ahmes-library/scholar/documents/*/extract/extraction.db
- Teaching publication head (unpublished research home):
  ~/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem/digital-creativity-pedagogy/grounding/
- Unit IDs: ../cv/UNIT-PLAN.md (I.1–I.9, II.1–II.6). Official hours/eval from cv/guides/*.json + oficial-guia-framework.mdc
- Athanor project: --project-slug profield-digital-creativity --library scholar
- DevIAC discovery (optional): knowledge_scope=field_prospection · make ingest-profield-dc

Do this (create artefacts; do not forge student lessons in this pass):

1) Pass-2 discipline on every dc-* specialty field:
   - If pass2.claude.audit.raw.md (or batch ledger) exists: apply required amendments into pass1.edited.md
     (E1–E4 mechanical: strip ChatGPT chips / +N / UI chrome; ## headings; inline **[NEEDS CHECK]** / preprint flags).
   - If only pass1.edited.md exists: treat identifier-queue + DOI seed as the audit surface; do not invent Pass-2 prose.
   - Write/update pass2.claude.audit.ledger.md per field; rollup under dc-curriculum-gap-harvest.

2) Bibliographic coats (RIS/meta only — no re-extract):
   ~/src/ahmes/scripts/profield-meta-enrich.sh \
     ~/src/profield/runs/<dc-field>/20260816/source-pdfs --force-meta
   Expect residual host-heading BIBLIO-GAP on *pre-12G.4* coats until re-enrich; Ahmes **12G.4 is SHIPPED** (2026-08-16). `--force-meta` alone did not fix Abstract/Introduction titles before that fix — it is not a missing RIS pass. Do not invent AU/TI.

3) Athanor discoverability:
   - Dry-run then inject each source-pdfs/.ahmes/batch-manifest.json into
     --project-slug profield-digital-creativity --library scholar
   - Ahmes extract alone is not enough.

4) Promote into digital-creativity-pedagogy/grounding/gap-fields/:
   - Copy pass1.edited.md → dc-<field>.pass1.edited.md
   - COAT-INVENTORY.json (all extraction_db paths; dedupe shared coats)
   - INDEX.mdc — field → UNIT-PLAN ID (I.x / II.x) + forge wave + operator sequence
   - FORGE-AVANTGARDE-QUESTIONS.md — avant-garde questions for Wave 1–4 units still NONE / [BIBLIO-GAP]
     (priority: II.5 portfolio web UX; I.5/I.6 3D form/volume; then I.2–I.4, II.1–II.2, II.4, II.6, I.8/I.9, II.3 deepen)
     Method per question: Athanor search (discovery only) → read Ahmes node page →
     `ahmes query --cite db:node --style chicago-author-date`.
     Cite only evaluator_safe=yes; else ⟨coat⟩·nodo·p. + [BIBLIO-GAP] + reason.
   - PENDING-procurement.md — DOIs in seeds not coated; P0 forge-blocking first; no shadow libraries.
   - Update GAP-PROSPECTION-INDEX.mdc, README.md evidence matrix rows, PROFIELD-SYNC.json.

Hard rules:
- Never cite vector snippets or Athanor previews.
- Never invent bibliographic metadata when host title is Abstract/Introduction/Keywords (Ahmes **12G.4** SHIPPED — re-enrich coats; not a missing RIS pass).
- CLO / Photoshop / Premiere / Gravity Sketch docs = HOW only — never Chicago bibliography.
- VTON / virtual try-on = out of teaching sprint — say so; do not procure as pedagogy evidence.
- Pedagogy gaps stay declared gaps even when technique coats exist.
- Do not paste FE CER / Web Atelier unit claims into CD without Ladder A/B (atelier-synergy / grounding README).
- Student fashion work needs consent (consent/S-SET.md) before exhibition claims — drafts ≠ DPO approval.
```

---

## 2 · Prompt: replicate for the CD CV / unit forge (UEM)

Use in **digital-creativity-uem** (same machine; vaults in `~/ahmes-library`).

```text
You are forging Creación Digital I/II units (UEM) against digital-creativity-pedagogy grounding.

Read first:
- ~/projects/…/digital-creativity-uem/digital-creativity-pedagogy/grounding/README.md
- …/GAP-PROSPECTION-INDEX.mdc
- …/gap-fields/INDEX.mdc                    # after §1 has created it
- …/gap-fields/FORGE-AVANTGARDE-QUESTIONS.md
- …/gap-fields/PENDING-procurement.md
- …/cv/UNIT-PLAN.md
- …/cv/guides/{1-creacion-digital-i,3-creacion-digital-ii}.json  # after live PDF check
- …/oficial-guia-framework.mdc · …/dc-unit-forge.mdc · …/TEACHING-READINESS.mdc
- …/consent/README.md

For each unit ID you touch (I.x / II.x):

1) Look up the evidence-matrix row (grounding/README.md). If NONE / [BIBLIO-GAP] / pilot, the unit prose must declare it.
2) Prefer forge questions from FORGE-AVANTGARDE-QUESTIONS.md as studio/assessment stems —
   do not invent weaker “open CLO and export” checklists.
3) Provenance for every scholarly claim:
   ATHANOR=~/src/athanor/.venv/bin/athanor
   AHMES=~/src/ahmes/.venv/bin/ahmes
   set -a; source ~/src/athanor/.env; set +a
   $ATHANOR search "<claim theme>" --project-slug profield-digital-creativity --library scholar --top-k 20
   Then open extraction.db for the hit’s node_id; then:
   $AHMES query --cite <db>:<node_id> --style chicago-author-date
4) Insert citations only when evaluator_safe=yes.
   If BIBLIO-GAP: keep the pedagogical move, mark [BIBLIO-GAP], record coat·node·page, do not fake (Author Year).
5) Tool/vendor facts → dated platform notes, never bibliography.
6) If a needed DOI is in gap-fields/PENDING-procurement.md and not coated, stop and queue procurement —
   do not substitute a tutorial blog or FE coat without Ladder B.
7) Hours / evaluation weights / CONTENIDOS labels must match the guía JSON (150 h CD I · 150 h CD II) —
   never FE 10/30/14 substitution; do not invent a full sessions_list to fake allocation.

Deliverable: unit forge patches (per dc-unit-forge.mdc) + PROVENANCE appendix (coat·node·page or [BIBLIO-GAP] deferred).
Do not publish digital-creativity-pedagogy/ to GitHub Pages.
```

---

## 3 · Prompt: blend `gap-fields/` + `temario/` → one temario with no gaps (CD)

Destiny: one Contidos surface where every T/C strand and every UNIT-PLAN ID has either (a) cite-safe Ahmes evidence or (b) an explicit dated declared gap + procurement ticket — never a silent blank.

```text
You are unifying Creación Digital Contidos research into one gapless temario publication head.

Sources to merge (do not overwrite either blindly):
A) grounding/temario/     — T1–T3 + C1–C3 .pass1.resultant.mdc + PROVENANCE-LAYER.{md,json}
                            (omnibus digital-creativity / Contidos harvest)
B) grounding/gap-fields/  — Pass-2 audited dc-*.pass1.edited.md + FORGE questions + PENDING-procurement.md
                            (20260816 unit pedagogy fields: portfolio UX, 3D volume, 2D craft, retouch,
                             avatar, video, AR/hologram, motion/still, digital fashion experience, gap-harvest)

Create grounding/temario-unified/ (or evolve temario/ in place with a clear banner) containing:

1) INDEX.md — one row per Contidos resultant AND one row per UNIT-PLAN ID:
   | Strand / Unit | Map evidence | Coats (Ahmes) | Cite-safe? | Forge questions | Procurement | Status |
   Status ∈ {READY_CITE, READY_DECLARED_GAP, BLOCKED_PROCUREMENT, BLOCKED_BIBLIO_GAP_12G4}

2) Merge PENDING lists:
   - Deduplicate DOIs across any temario procurement notes and gap-fields/PENDING-procurement.md
   - Preserve P0: II.5 portfolio web UX studies; I.5/I.6 3D form/volume pedagogy coats
   - Keep ISBN / monograph campus procurement separate from DOI OA queue
   - Output PENDING-procurement.md (unified) + already-coated appendix → COAT-INVENTORY + omnibus coats

3) Content merges:
   - Map gap-fields forge questions onto UNIT-PLAN IDs (not only T1–T3 labels).
   - T1 (image/2D/volume) ← dc-2d-image-craft + dc-3d-form-volume
   - T2 (retouch/video/portfolio) ← dc-fashion-retouch + dc-fashion-video + dc-fashion-portfolio-web-ux
   - T3 (avatars/experiences/AR) ← dc-avatar-digital-fashion + dc-digital-fashion-experience + dc-ar-hologram-fashion
   - C1–C3 critical strands: keep critical Contidos; add gap-field coats only when they ground silence/gender/virtuality claims — never tool manuals.
   - Replace silent NONE with Tri-Anchors or DECLARED_GAP paragraphs from FORGE-AVANTGARDE-QUESTIONS.
   - Never promote [PLATFORM], VTON papers-as-curriculum, or NEEDS CHECK 2026 DOIs to ESTABLISHED.

4) Provenance pass:
   - Re-run Athanor search + Ahmes --cite for every ESTABLISHED/EMERGING claim you keep.
   - Refresh PROVENANCE-LAYER.md / .json (coat · nodo · p. · evaluator_safe).
   - BIBLIO-GAP from polluted host titles: re-enrich with post-12G.4 Ahmes (not another “RIS only” ticket); they do not block DECLARED_GAP teaching text.

5) Definition of done (“temario with no gaps”):
   - Every UNIT-PLAN ID and every T1–T3/C1–C3 row has Status ≠ empty.
   - Every READY_CITE row has ≥1 evaluator_safe Ahmes citation.
   - Every READY_DECLARED_GAP row states the gap in instructor-facing language and links procurement or research-line ticket.
   - Zero silent NONE cells for Wave 1–2 blockers (II.5, I.5, I.6) at minimum; ideally all I.* / II.*.

Hard rules unchanged: discover in Athanor/DevIAC, cite from Ahmes; no shadow libraries; no invented metadata;
VTON out of scope; Pages must not leak digital-creativity-pedagogy/.
```

---

## Quick operator cheatsheet (DC)

```bash
ATHANOR=~/src/athanor/.venv/bin/athanor
AHMES=~/src/ahmes/.venv/bin/ahmes
set -a; source ~/src/athanor/.env; set +a

# Discover
$ATHANOR search "…" --project-slug profield-digital-creativity --library scholar --top-k 20

# Cite
$AHMES query --cite ~/ahmes-library/scholar/documents/<coat>/extract/extraction.db:<node_id> \
  --style chicago-author-date

# Meta / RIS only (idempotent; no re-extract)
~/src/ahmes/scripts/profield-meta-enrich.sh \
  ~/src/profield/runs/dc-fashion-portfolio-web-ux/20260816/source-pdfs --force-meta

# Inventories (after §1)
open ~/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem/digital-creativity-pedagogy/grounding/gap-fields/COAT-INVENTORY.json
open …/gap-fields/PENDING-procurement.md
open …/temario/PROVENANCE-LAYER.md
```

## FE twin (do not confuse projects)

| | FE | DC |
| --- | --- | --- |
| Prompt source | `web-atelier-udit/.../gap-fields/PROMPTS-REPLICATE.md` | **this file** |
| Athanor slug | `profield-frontend-pedagogy` | `profield-digital-creativity` |
| Run date folder | `20260815` | `20260816` |
| Field prefix | `fe-` | `dc-` |
