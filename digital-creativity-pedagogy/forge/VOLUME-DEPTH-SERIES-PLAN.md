# Plan — Volume / depth teaching series

**Date:** 2026-11-13  
**Trigger:** Live I.6 audit (`/lessons/en/digital-creativity-i/i-6-volume/`) + research corpus `grounding/lesson-corpus/I.5-I.6-depth-perception-perspective-research.md`  
**Constraint:** slides specific, brief, semantic markup; graphics as full slides (SLIDE-TYPOGRAPHY-LAW §4); discovery ≠ Ahmes citation.

---

## 1 · Audit verdict (live I.6)

**Diagnosis:** one official CONTENIDO (*Volumen*) is carrying **three courses at once**.

| Layer jammed into I.6 | What it is | Why it feels “far away” |
| --- | --- | --- |
| A · Fashion volume behaviour | Galada fit signs · Coats hybrid discrepancy · variables · lab fold | Correct I.6 nail — but buried |
| B · Perspective as symbolic form | Panofsky P1–P6 kit + six SVGs + Rive motion | Art-history / construction curriculum — belongs with I.5 spatial literacy, not as I.6 masterclass filler |
| C · Critical / cultural volume | Cheang · default body · kente/weaving stills · relocated costs | Necessary, but overload when stacked with A+B in one 120′ session |

**Counts (current):**

- Lesson page ≈ **20** `<figure>` blocks · **~297** lines EN · masterclass packs Panofsky kit *inside* “volume variables”
- Deck `content.json` ≈ **12** card headings (cover → analysis → hybrid iterates → 2× motion/perspective overlays → lab ×2 → recall → carry) — already at the upper edge for one session; **not** “5–6 main-idea cards”
- Deck opener reads abstract (“a fold becomes volume…”) with sparse geometric foldouts — weak vs the image density of the lesson body

**Master idea still right for official I.6:** *volume is behaviour* (MASTER-IDEAS). The problem is **scope creep**, not the nail.

---

## 2 · Is temario relevant?

**Yes — for the I.5/I.6 pair, not as a dump into one slide deck.**

`grounding/temario/T1-image-2d-volume.pass1.resultant.mdc` § *Fundamentos y representación de la forma tridimensional; volumen* already splits three loads:

| Temario strand | Maps to |
| --- | --- |
| **A · Technical** — Hughes et al. CGPPP (geometry, transform, light, viewpoint) | I.5 + digital projection lesson (series L4) |
| **B · Canonical** — Arnheim (perception of shape, depth, volume) | Perception series L1–L2 (research report spine) |
| **C · Academic** — McQuillan / 3D fashion + sustainability | Keep light in I.6 living prompt; do not rebuild I.6 around it |

So: temario **validates splitting** “perception of volume” from “fashion volume behaviour” from “render geometry.” It does **not** justify stuffing Arnheim + Panofsky + Coats into one I.6 session.

### Bidirectional bridge · SVG / Canvas 2.5D (web-atelier) ↔ this split

Sister lesson: [SVG Animation Master Session](https://ruvebal.github.io/web-atelier-udit/lessons/en/web-animations/svg-master-session/) Round 4 + skill `canvas-25d-content-hero` (painter-order projection, clamped scale, occlusion by sort — **no** Z-buffer).

| Temario / series layer | What 2.5D / SVG technique can do | What it must not claim |
| --- | --- | --- |
| **Perception** (Arnheim / cues) | Illustrate occlusion, relative size, motion parallax, texture compression with edge-clean course SVGs; float camera as *cue demo* | That Canvas 2.5D *is* stereopsis or Helmholtz inference |
| **Fashion volume behaviour** (I.6) | Optional ambient diagram only; keep Galada/Coats nails | Replacing fit diagnosis with a pretty projected fold |
| **Render geometry** (Hughes / ML-C) | Exact place for 2.5D vs CSS planes vs Rive-3D / WebGL honesty — same taxonomy as the master session | Calling painter-order “true 3D” or a depth buffer |

**Both ways:** perception vocabulary makes FE/SVG students name *why* a projected fold reads as volume; SVG/Canvas craft gives CD I **Awwwards-grade full graphic slides** (perspective-kit already; future cue diagrams) without bloating I.6 prose. True depth-tested claims → `rive-animascript-3d` / WebGL, not 2.5D.

Cascade home: `digital-creativity-pedagogy/DEV_PLAN/VOLUME-DEPTH-SERIES/`.

---

## 3 · Gap-fields: what can be covered (honestly)

From `gap-fields/dc-3d-form-volume-pedagogy.pass1.edited.md`:

| Gap | Cover in series? | How (without fake evidence) |
| --- | --- | --- |
| Light-on-form / shading as volume cue | **Yes (pedagogical)** | Pictorial cues lesson + Commons diagrams; declare **no fashion-HE RCT** |
| Still-life → fashion-volume pipeline | **Partial** | Studio exercise only; keep `[UNVERIFIED]` in editorial note |
| Orthographic vs perspective → CLO competence | **Adjacent only** | Multi-view as *questions about volume*; never claim CLO outcome validation |
| Process-evidence rubric (not software commands) | **Yes** | Already I.6 nail — keep assessable; don’t grade polish |
| Mesh/topology as fashion foundation | **No** | Out of CONTENIDOS / transfer boundary |
| Accessible 3D instruction | **Declare** | Living prompt / alt routes; not a full unit yet |

Fashion-HE SAFE anchors stay where they are: **I.5** Papahristou course-structure · **I.6** Coats hybrid + Galada fit signs.

---

## 4 · How many lessons? How many slides?

### Recommended product shape

Do **not** expand official CD I to 5–6 new guía units. Official map stays **I.5 + I.6**.

Build a **compact series** as:

1. **Slim I.5** — form / multi-view / spatial literacy (keep official)  
2. **Slim I.6** — volume-as-behaviour + hybrid lab (keep official)  
3. **Optional master-lecture / enrichment track** (3 short decks) — the research title *Human Construction of Volume Perception…* — for when you want perception → Alberti → cues → AI without breaking the guía

### Slide budget (state of the art for *this* forge)

Per deck (SLIDE-TYPOGRAPHY-LAW + STUDENT-SLIDESHOW-FORGE):

| Slot | Count | Rule |
| --- | --- | --- |
| Main-idea reading cards | **5–6** | one claim ≤ ~35 words; `**key**` / one `==tension==` |
| Full graphic slides | **4–6** | immediately after the claim they prove; never inset in the card |
| Lab / recall | **2–3** | exercises + exit ticket |
| **Total deck** | **≈ 12–15** max | cut text before adding slides |

**Answer to “how many 5–6 slides main-ideas lessons?”**

| Surface | Main-idea cards | Role |
| --- | --- | --- |
| **I.5** (official) | **5** | form ↔ views ↔ spatial viz |
| **I.6** (official) | **5** | behaviour · variables · discrepancy · body default · one revision |
| **ML-A Perception** (enrichment) | **6** | retina paradox · Helmholtz/Gibson · cues inventory |
| **ML-B Construction** (enrichment) | **6** | Alberti window · Panofsky P1/P5 · multi-view ≠ fit |
| **ML-C Digital / AI** (enrichment) | **5** | projection as Alberti-in-algebra · plausibility vs perspective |

That is **2 official lessons + 3 optional master decks**, not six official CONTENIDOS. Classroom week: teach **I.5 then I.6**; run ML-A/B/C only as master lecture / make-up / advanced seminar.

---

## 5 · Reorganization plan (execution order)

### Phase 0 — Split the jammed I.6 (1 session of forge work)

1. **Strip from I.6 masterclass:** Kandinsky digression; Panofsky P1–P6 figure block; perspective-kit Rive as *core* argument.  
2. **Keep in I.6:** Galada · Coats · variables · critical body · relocated-costs prompt · Lab 1–2 · practice quiz.  
3. **Cap lesson figures at ~8** (behaviour + discrepancy + one multi-view nail). Move excess to ML-B or media ledger.  
4. **Rewrite I.6 deck** to **5 main-idea cards** aligned to MASTER-IDEAS nail; drop motion-perspective cards from this unit’s *required* path (or move to ML-B).

### Phase 1 — Slim I.5 (official)

**Five main ideas:**

1. Flat evidence vs volumetric claim  
2. Orthographic / front–side–¾ = different questions  
3. Spatial visualization ≠ software fluency (Moritz / Papahristou bounded)  
4. Light and silhouette as form evidence (adjacent; gap-honest)  
5. Hand-off: I.6 will test *behaviour*, not prettier mesh  

Deck: 5 cards + 4–5 full graphics (existing form SVGs / one Commons depth cue). Semantic HTML: `<figure>` + Chicago only.

### Phase 2 — Enrichment series title

**Series name (student-facing):** *Volume Perception & Depth Representation*  
**Spine source:** `lesson-corpus/I.5-I.6-depth-perception-perspective-research.md`  
**Do not** publish the research MD as a lesson.

| Deck ID | Main ideas (≤6) | Image / graphic plan | Evidence stance |
| --- | --- | --- | --- |
| **ML-A · Seeing volume** | Paradox · inverse problem · Helmholtz · Gibson · cue table · studio ask | Depth cues 1 · visual cliff · optical flow · railroad VP · texture/aerial Commons (after `media-accept`) | Orientation + cleared media; Arnheim via temario T1-B when Ahmes-safe |
| **ML-B · Constructing space** | Alberti window · visual pyramid · Leonardo aerial · Panofsky symbolic form · P1 vs P5 · multi-view ≠ fit | Perspective-kit P1–P5 as **full graphic slides**; Alberti self-portrait if cleared | Panofsky SAFE nodes already in I.6 provenance — relocate cites here |
| **ML-C · Digital & AI depth** | Projection \(x/z\) · virtual camera = Alberti · Z-buffer/stereo · AI plausibility question · bridge back to I.6 behaviour | Comparison_of_graphical_projections · Scratchapixel as *link card* not PDF dump · one NeRF/plausibility still only if rights-clear | No Midjourney scrape; question-led |

### Phase 3 — Media pipeline (non-negotiable)

```text
Profield 20261113 manifests
  → human review / media-accept
  → docs/_data/media-packs/
  → deck media_slot_id
```

Never paste raw Commons URLs into student HTML without accept. Prefer **course perspective-kit SVGs** (already authored) for ML-B; use Wikipedia-lead Commons for ML-A after clearance.

### Phase 4 — Semantic / compactness law (every surface)

- Lesson: `figure` + `figcaption` + short masterclass (§) · no encyclopedia paragraphs  
- Deck: heading ≤ 8 words · sentence ≤ ~35 words · graphics `placement: "full"`  
- One assessable nail per official unit; enrichment decks end with a **bridge card** to I.5/I.6, not a second nail  
- Editorial note keeps Declared gaps (still-life pipeline, light-on-form fashion RCT, Alberti if still unvaulted)

### Phase 5 — Verification

- `npm run render:decks` · publication + citation gates  
- Browser: I.6 no longer shows P1–P6 wall; ML-B does  
- Slide mark counts per SLIDE-TYPOGRAPHY-LAW §5  
- Temario T1 rows referenced in forge receipt only; student text stays Chicago

---

## 6 · What not to do

- Do **not** replace I.6’s fashion behaviour nail with the optics monograph.  
- Do **not** invent a sixth official CONTENIDO.  
- Do **not** claim gap-fields UNVERIFIED blanks are “covered” by teaching them — teach as **studio literacy**, declare evidence blank.  
- Do **not** keep 20 figures on the I.6 lesson page “because the research is rich.”

---

## 7 · Success criteria

| Check | Pass |
| --- | --- |
| I.6 session | Student can name behaviour variables + one discrepancy without hearing Panofsky |
| I.5 session | Student can explain multi-view without CLO menus |
| ML series | 3 decks × ≤6 main-idea cards; image-led; semantic markup |
| Temario | T1 A/B/C visibly mapped in forge receipt, not copied into slides |
| Gaps | Light-on-form + still-life blanks named in editorial notes |

---

## 8 · Suggested next forge move

1. Phase 0 strip of I.6 (highest classroom value).  
2. Relocate Panofsky kit → ML-B draft `content.json`.  
3. Accept 4–6 ML-A Commons leads from the 20261113 image research.  
4. Only then expand ML-C.

Source spine: `grounding/lesson-corpus/I.5-I.6-depth-perception-perspective-research.md` · gap map: `gap-fields/dc-3d-form-volume-pedagogy.pass1.edited.md` · temario: `temario/T1-image-2d-volume.pass1.resultant.mdc`.
