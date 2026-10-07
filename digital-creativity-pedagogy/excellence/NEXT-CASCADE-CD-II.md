# NEXT CASCADE — Creación Digital II + Nuevos Medios (seed)

> Seed for the follow-on autopilot cascade. This Excellence run (EX0–EX11)
> finishes the **Wave-1 platform** on CD I I.1–I.9 + fashion-image-analysis.
> It does **not** forge CD II or Nuevos Medios to Wave-1 depth.
>
> Authority: TECHNICAL-DIRECTOR-CASCADE Amendment A1; official guías
> `cv/guides/3-creacion-digital-ii.json` (+ NM guía when in scope);
> session rhythm: `forge/SESSION-RHYTHM-AND-DELIVERABLES.mdc`.

## 1 · Target shape

| Subject | Units / hubs | Notes |
| --- | --- | --- |
| **CD I remainder** | I.6–I.9 media decks + Labs | Placeholders exist; need 2627-dci decks, EX4–EX8 depth, bank refs |
| **CD II** | II.* lessons/decks per guía CONTENIDOS | Avatars, digital fashion experiences, video, web/portfolio, holograms/AR — **no VTON** |
| **Nuevos Medios** | `u-*` NM track | Firewall already scrubbed (EX2); content redesign = this cascade |
| **Special** | Keep fashion-image-analysis; add CD II specials only if guía demands | Do not invent CONTENIDOS |

Official CONTENIDOS and evaluation weights stay locked to the guía JSON after
PDF check (`oficial-guia-framework.mdc`). Sandra Plan de trabajo coordination
for CD I (ACT1–4) stays; CD II coordination needs a separate Plan if Sandra
publishes one — do not invent ACT IDs.

## 2 · CD I remainder (finish Wave-1 media)

1. Author `docs/tracks/en/uem/2627-dci/i-6-*` … `i-9-*` content.json (`schema_version: 2`).
2. Run EX4-style curation + rights report; EX5 render + browser gate.
3. Two `lab_exercise` slides + B2 lesson cards; EX8 LAB-SIGNOFF amendment.
4. Extend `assessment/question-bank.yml` only with lesson `references:` keys
   already in `docs/_data/references.yml` (no invented cites).

## 3 · CD II forge order (suggested)

| Slice | Focus | Reuse |
| --- | --- | --- |
| II contract | Publish guía buckets on evaluation / How-to-Pass for CD II track | EX1 pattern |
| Firewall | Re-run publication safety on every new lesson | EX2 |
| Media | schema v2 + bindSlides + rights | EX3–EX5 |
| Research | Extend research-manifest + references.yml from Ahmes only | EX6 |
| Methods | Fashion-craft catalogue candidates for retouch / avatar / AR craft | EX7 (no CT IDs) |
| Labs | Exactly two Labs; portfolio feed without inventing graded work | EX8 |
| Assessment | Bank + practice quizzes; consent stays drafts until DPO | EX10 |

## 4 · Nuevos Medios note

- EX2 already removed leak vocabulary from NM public pages — **preserve**.
- Do not treat NM as CD I Wave-1; open a dedicated INDEX cascade or a
  clearly named phase pack under `excellence/` only after professor scope.
- No UDIT / sibling-institution names on student-facing NM surfaces.

## 5 · Platform contracts to reuse (do not re-open)

- Probe: `excellence/probe/excellence-probe.mjs --targets` (extend scopes carefully)
- Validator: `scripts/validate-decks.mjs --strict --rights=flag`
- Safety: `scripts/verify-publication-safety.mjs`
- Browser: `npm run test:browser` / `scripts/tests/browser/deck-layout.mjs`
- Gitflow: land on `excellence/integration`; never push `main` until release
- Autopilot: measurement never starts; no cloud LLMs for student text/cites

## 6 · Open decisions for the follow-on cascade

- Whether CD II shares Sandra’s 4×11.2% continuous strip or a different plan
- Whether NM gets its own FINDINGS live audit before forging
- Exhibition / DPO path for student fashion work (S1/S2) — still blocked here
- I.4 / I.8 / I.9 bank gaps from EX10 — fill only after lesson refs exist
