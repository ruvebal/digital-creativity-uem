# COLD REVIEW — SU-FIA cycle 1 (Fashion Image Analysis)

**Reviewer role:** cascade-cold-reviewer (no implementer memory; fail-closed on stated criteria)  
**Date:** 2026-09-27  
**Unit:** SU-FIA · Especial · Análisis de imagen de moda (DC / NM)  
**Artefacts reviewed:** shared frame · forge `.mdc` · feedback report · MAIN-IDEAS · professor brief · student lesson · Reveal `content.json` · track wire  
**Decision owner:** product owner — this file does **not** mark the phase DONE.

---

## 1. Verdict

**PASS-WITH-AMENDS**

Pedagogy and slideshow spine are strong enough for a **pilot** special unit: eight steps live in the lesson, Lens A/B stay distinct, critical step is mandatory and visible, public Chicago is Shinkle-only from claimed `evaluator_safe=yes` nodes, and deck law (≤6 masterclass + `analysis_opener` + two labs + geometrical openers) holds.

**Do not forge the CT creative-process sibling from this cycle as a copy-paste template until the P0 publication-firewall amends below are applied** — otherwise CT will inherit the same student-visible studio jargon / hash leaks.

One SAFE public author (Shinkle 2008) is **acceptable for pilot** with honest Declared gap / Missing evidence. It is **not** enough to drop `status: pilot` or treat the unit as exam-grounded until a second SAFE spine (Steimberg and/or Shawcross, or Verón primary) clears.

---

## 2. Blocking finds (must fix before cycle-2 / CT sibling forge)

### F1 — P0 · Publication firewall leak in student lesson body

**Blocks DONE:** yes  
**Criterion:** no Ahmes / Athanor / DevIAC / `[BIBLIO-GAP]` / node IDs / resolver labels in student-visible HTML body.

**Evidence (paths + lines):**

| Location | Leak |
| -------- | ---- |
| `docs/lessons/es/nuevos-medios-moda/special-analisis-imagen-moda/index.md` ~L138 (studium §) | Student prose: “hasta que el **coat** bibliográfico sea **evaluator-safe**” — resolver + vault jargon |
| Same file ~L193–194 (Nota editorial) | “**evaluator-safe**”, “until **coats** clear”, “Verón primary **coats**”, run id `` `20260927-special-analysis` `` |
| Same file ~L199 (AI-assisted authorship) | Coat hash8 IDs `` `1936070c` ``, `` `03498f83` ``, `` `d639c32d` `` + “SAFE coat” / “coats gated” |

Gated `{% if site.publication.publish_internal_metadata %}` curriculum-internal (L27–52) is fine. Public closing sections are **not** a dump for vault IDs.

**Compare:** sibling lessons (e.g. `docs/lessons/es/creacion-digital-ii/ii-2-avatares/`) AI footers use vault **count** only — no hash8 coats.

**Fix:** Rewrite studium aside + Editorial note + AI footer to student language (Chicago authors named as gaps OK; no `coat` / `evaluator-safe` / hash8 / run paths). Match `dc-unit-forge` §3c / `AI-DECLARATION-LAW` ES twin headings where possible (`Autoría asistida por IA`).

---

### F2 — P0 · “Ahmes” string in published deck JSON

**Blocks DONE:** yes  
**Evidence:** `docs/tracks/es/uem/2627-nm/special-analisis-imagen-moda/data/content.json` L12:

```text
"description": "Special analysis unit: geometrical openers; Masterclass quotes from Ahmes-safe Shinkle 2008."
```

`index.html` loads this file via `data-content-url` (`student-media-deck.js`). Even if `media_selection.description` is not painted into slide DOM, the JSON is a **student-reachable published asset**. Forge law (`FASHION-IMAGE-ANALYSIS-FORGE.mdc` L126; `PROVENANCE-LAW.mdc`) forbids Ahmes names on student surfaces.

**Fix:** Strip studio infra from `description` (e.g. “geometrical openers; Masterclass quotes from Shinkle 2008”).

---

### F3 — P0 · Feedback self-check falsely claims firewall pass

**Blocks DONE:** yes (process / honesty gate)  
**Evidence:** `forge/receipts/SU-FIA-CYCLE1-FEEDBACK.md` L73–74:

| Gate | Status |
| ---- | ------ |
| No Ahmes/Athanor names in student HTML body | **pass** (gated only) |
| BIBLIO-GAP not exposed publicly | **pass** |

F1–F2 contradict both rows. Cold-review ask #4 (“Any publication-firewall leak?”) is answered: **yes**.

**Fix:** Amend feedback receipt after F1–F2; do not carry a green firewall row into CT forge planning.

---

### F4 — P1 · Numbers report inconsistency (BIBLIO-GAP count + tao inventeds)

**Blocks DONE:** yes for *receipt honesty* before CT sibling inherits the ledger; does not require re-forging pedagogy.

**Evidence:**

| Feedback claim | Artefact count |
| -------------- | -------------- |
| `Nodes held as [BIBLIO-GAP] … **5**` (FEEDBACK L20) | Only **3** BIBLIO-GAP `PROVENANCE_LINE`s in lesson curriculum-internal (studium Shawcross `7391ea20`; estilo-triad `e78340b1`; veron-via-steimberg `b93a7db9`). MAIN-IDEAS `gated_not_public` lists the same **3** nodes. |
| `Tao / course invented slide lines \| 3` (FEEDBACK L23) | Deck `quote_origin` tally: **`tao_invented`: 1**, **`page_verified`: 4**. No second/third `tao_invented` fields. |

**Consistent (spot-check):** masterclass **6**; labs **2**; public Chicago authors **1** (Shinkle); verbatim slide quotes **4**; `evaluator_safe` public nodes claimed **5** (four on slides + lesson-only p.15 `cca1472b` — matches professor brief table).

**Fix:** Correct FEEDBACK table to BIBLIO-GAP **3** (or document what the extra two were); set invented lines to **1** or define the counting rule and apply it to three explicit slides.

---

## 3. Non-blocking improvements

### F5 — P2 · Audience / quote length (~19yo, ES track)

English blockquotes on slides 3–4 are long for a first-year ES cohort (`content.json` L60–72; lesson L108–114). Pedagogy is sound; consider Spanish one-line paraphrase on the slide `sentence` (already present) and shorter quote cuts, or “read on lesson” for the longest sentence.

### F6 — P2 · Shared-frame idea 4 underweighted in deck

Shared frame spine idea 4 = “Making has conditions.” Deck idea 4 = genre/method plurality (Shinkle 17). Context-of-making lives in step 5 of the guide, not as a masterclass beat. Acceptable adaptation; optional: one prompt line on idea 4 or analysis_model naming briefs/labour.

### F7 — P2 · Verón naming policy (answers feedback ask #3)

Student lesson correctly keeps Verón **off** the public surface; Lens B is plain production → recepción → next production. **Keep professor-only until SAFE Chicago.** Do not add the name to student HTML as a “prestige cite” without a coat.

### F8 — P2 · Forge / execute path contract stale

`FASHION-IMAGE-ANALYSIS-FORGE.mdc` L119–120 and `FASHION-IMAGE-ANALYSIS.execute.md` L38–39 still suggest EN paths (`docs/lessons/en/digital-creativity/special-fashion-image-analysis/`). Shipped artefacts are NM ES:

- `docs/lessons/es/nuevos-medios-moda/special-analisis-imagen-moda/`
- `docs/tracks/es/uem/2627-nm/special-analisis-imagen-moda/`

Execute receipt table (execute.md L61–73) is still empty. Fill receipt + align suggested paths so CT sibling forge does not invent a second tree.

### F9 — P2 · Footer language form

Lesson is `lang: es` but closing uses hybrid EN (“Work in progress”, “AI-assisted authorship”, Declared gap in English). Prefer ES twins per `AI-DECLARATION-LAW.mdc`.

### F10 — P2 · Extra `analysis_model` slide

Deck inserts `analysis_model` (eight-step list) between `analysis_opener` and masterclass. Not a 7th idea; spine still legal. Optional: ensure STUDENT-SLIDESHOW-FORGE explicitly allows `analysis_model` for guide units so CT copies the same role cleanly.

---

## 4. Specific amend list

### A. Student lesson (`special-analisis-imagen-moda/index.md`)

1. **Studium § (~L136–138):** Remove “coat” / “evaluator-safe”. Example direction: “herramienta de clase; la cita textual de apoyo secundario queda en el brief del profesor hasta que la referencia pública esté disponible.”
2. **Nota editorial (~L191–195):** Keep author names + honest gap; drop resolver jargon, coat vocabulary, and run-folder ids. No vault architecture.
3. **AI-assisted (~L197–199):** Follow §3c template — vault **count** (e.g. “consultó **1** fuente pública del vault”) + forge date + harness line; **no** hash8 coats.
4. Prefer ES section titles for closing law.

### B. Deck (`…/data/content.json`)

1. Rewrite `media_selection.description` — delete “Ahmes-safe”.
2. (Optional) Shorten longest English quotes or strengthen ES `sentence` paraphrases for ideas 3–4.

### C. Forge `.mdc` / execute

1. Update output-contract paths to the **shipped NM ES** lesson/deck paths.
2. Add explicit firewall bullet: public Editorial / AI footers must not contain coat hash8, `evaluator_safe`, Ahmes/Athanor/DevIAC, or `[BIBLIO-GAP]` labels.
3. Fill execute receipt after amends.
4. State pilot policy: **one SAFE author OK for `status: pilot`**; second SAFE author required before exam / de-pilot.

### D. Feedback receipt

1. Flip firewall rows to fail → pass only after A+B.
2. Correct BIBLIO-GAP node count and tao-invented count (F4).

### E. CT sibling forge (when started)

1. Reuse eight steps + Lens A/B + slideshow law from **amended** forge, not from pre-amend artefacts.
2. Do not ship Verón/Steimberg Chicago until SAFE; copy the “course method / professor brief” pattern that already works here.

---

## 5. Numbers check

| Feedback metric | Claimed | Cold-check vs artefacts | Result |
| --------------- | ------: | ----------------------- | ------ |
| Athanor slugs queried | 2 | Named in curriculum-internal; cannot re-run search here | Unverified process claim (not contradicted) |
| Distinct queries | 5 | Same | Unverified |
| Raw hits | 42 | Same | Unverified |
| Unique coats | 3 (Shinkle, Shawcross, Steimberg) | Matches coat ledger + MAIN-IDEAS | **OK** |
| Ahmes nodes read | 12 | Not re-queried in vault this review | Unverified |
| `evaluator_safe` public | 5 | 5 PROVENANCE_LINE VERIFIED Shinkle nodes; 4 slide cites + 1 lesson-only (p.15) | **OK** |
| BIBLIO-GAP nodes | 5 | **3** documented gap nodes / lines | **INCONSISTENT** |
| Public Chicago authors | 1 | Referencias = Shinkle only | **OK** |
| Verbatim slide quotes | 4 | 4× `page_verified` + citation.href → lesson `#referencias` | **OK** |
| Tao / invented | 3 | 1× `tao_invented` | **INCONSISTENT** |
| Masterclass ideas | 6 | 6× `slide_role: masterclass` | **OK** |
| Lab exercises | 2 | 2× `lab_exercise`, both `portfolio_bound` | **OK** |

**Slideshow law checklist (this review):**

- [x] ≤ 6 masterclass ideas  
- [x] `unit_cover` → `analysis_opener` (geometrical) → … → `lab_opener` (geometrical) → 2 labs → `outro` (geometrical)  
- [x] Critical mandatory (lesson L102; deck `analysis_model` prompt + idea 6 prompt)  
- [x] Lenses distinct (lesson B1 table; deck analysis_opener)  
- [x] Verbatim quotes link to `#referencias`  
- [ ] Publication firewall clean — **fail until F1–F2 amended**

---

## 6. Answers to feedback “Cold-review asks”

1. **One SAFE author (Shinkle) for pilot?** Yes — keep `status: pilot`. Require second SAFE spine before exam use / de-pilot (lesson L195 already anticipates this).  
2. **Four verbatim quotes for ~19yo?** Pedagogically right themes; two are long in English — trim or lean on ES sentences (F5).  
3. **Name Verón on student surface without Chicago?** No — keep professor-only until coated (F7).  
4. **Firewall leak?** Yes — F1 (lesson body/footer) + F2 (deck JSON). Feedback self-check was wrong (F3).

---

## 7. Findings index

| ID | Severity | Blocks DONE | Summary |
| -- | -------- | ----------- | ------- |
| F1 | P0 | yes | Lesson body/footer: coat / evaluator-safe / hash8 |
| F2 | P0 | yes | `content.json` description names Ahmes |
| F3 | P0 | yes | Feedback firewall “pass” false |
| F4 | P1 | yes* | BIBLIO-GAP=5 and tao=3 do not match artefacts |
| F5 | P2 | no | Long EN quotes for ES ~19yo |
| F6 | P2 | no | Shared-frame “making conditions” soft in deck |
| F7 | P2 | no | Affirm Verón stays professor-only |
| F8 | P2 | no | Forge/execute path + empty receipt |
| F9 | P2 | no | ES footer heading form |
| F10 | P2 | no | Document `analysis_model` role |

\*F4 blocks *ledger trust* for CT kickoff, not the teaching method itself.

---

*Cold review complete. No lesson/deck rewrite performed in this pass — amends belong to implementer / next forge cycle.*
