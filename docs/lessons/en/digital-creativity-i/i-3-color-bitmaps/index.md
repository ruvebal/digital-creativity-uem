---
layout: lesson
title: 'I.3 · Colour, Bitmap Images'
title_es: 'I.3 · Color, imágenes con mapas de bits'
slug: i-3-color-bitmaps
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/digital-creativity-i/i-3-color-bitmaps/
description: 'Colour is relational and time-sensitive — perceptual colour theory plus platform editing styles, with an honest gap on colour-management pedagogy.'
status: pilot
tags: [digital-creativity-i, color, bitmap, raster-imaging]
deck_url: /tracks/dci/i-3-color-bitmaps/
master_idea: 'Colour is a relation — sampled, displayed, named, and interpreted — not a fixed swatch'
practice_anchor: 'Bitmap literacy: mode, depth, gamut, contrast check, and an accessible alternate palette kept visible in the process record'
frontier_signal: 'Platform editing styles circulate quickly; colour-management teaching sequences for fashion HE remain unvalidated'
references: [roivainen-2025, aldahoul-2025]
---

<!-- prettier-ignore-start -->

## 📋 Table of Contents
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

<div class="lesson-opener" markdown="1">

> _"The raster image fears the zoom. The SVG welcomes it."_
<!-- TTDO fit: direct fit — this unit's own anchor is bitmap/raster imagery specifically, in contrast to I.2's vector. -->
> — Tao of Development, `img-016`
{: .tao-development-quote }

{% include lesson-semantic-graphic.html %}

</div>

{% comment %}
cover-agentic:
  unit: I.3
  contenidos: "Color, imágenes con mapas de bits."
  competencies: [CON1, HAB9, COMP8, COMP9]
  one_line: "Colour is relational — bitmaps sample it under display and cultural assumptions."
  class_rhythm: "Analysis → Masterclass → Lab (Portfolio) — no Workshop in early sessions"
  evaluation_feed: "Investigaciones y proyectos 20%; Cuaderno 10%"
  how_to_pass: "/tracks/dci/how-to-pass-this-track/"
{% endcomment %}

## Where this sits — CONTENIDOS and competencies

**CONTENIDOS anchor (verbatim, official guía):** *Color, imágenes con mapas de bits.*

**Competencies served:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Learning outcomes:** *"Asociar los diferentes programas de efectos y recursos de edición de imagen digital"* is the closest guía bullet, shared with I.4 — colour tools are one of the "recursos de edición" it names; no bullet is exclusive to colour/bitmaps alone.

**Evaluation weights:** Investigaciones y proyectos 20% (studio piece); Cuaderno 10% (process note).

---

## Learning objectives

- **Describe a bitmap image as a fixed grid of colour values** — and explain what a given colour decision (mode, depth, gamut) forecloses for later.
- **Explain colour as relational and perceptual** — digital palettes taught through interaction, contrast, and context, not isolated RGB sliders (Albers 2013).
- **Name how creator technologies produce time-bound colour and tonal conventions** on platforms [(Roivainen 2025, 8)](#ref-roivainen-2025).
- **Produce a colour comparison** (not a single “final” palette): what changed, what stayed legible, which platform or cultural code you invoked.
- **Distinguish "colour correction" from "colour change"** — a disclosure question, not a technical one.

---

## Analysis
### Critical perspective

Computational fashion research can extract palettes and forecast colour, while
fashion-design teaching can ask students to specify palettes in HEX or Pantone
terms (Nobile et al. 2021); (Balasubramanian 2026). That precedent is useful for
comparison, not evidence that one coding system or classroom sequence is
universally correct. The critical question remains: who is the default viewer
when a colour is called accurate or accessible?

Contemporary image-generation and classification systems can reproduce intersectional gender and racial bias — tools used to produce fashion images should not be treated as representationally neutral infrastructure [(AlDahoul et al. 2025)](#ref-aldahoul-2025).

Who is treated as the default viewer when a palette is called accurate, beautiful, or accessible? Name one contrast test, display mismatch, or excluded skin/garment context your export chain assumes.

### The debate prompt

**When does "correcting" a colour become "changing" the garment it depicts?** This is the same disclosure question CD II's retouching unit (II.1) asks about bodies — asked here at the level of colour. The group decides together and states the decision.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.video.colour-workflow" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for a colour workflow demonstration; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> A short clip pauses whenever a profile, space, or export assumption changes.</p>
<p><strong>Look for:</strong> Conversion points and what each step forecloses.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.still.palette-contrast" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for palette contrast exemplar and counterexample; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Side-by-side palettes test legibility, hierarchy, and mood.</p>
<p><strong>Look for:</strong> Pairs that fail contrast on one display but pass on another.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.graphic.colour-chain" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract diagram placeholder for source-colour to display-export chain; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Maps source colour → profile/space → display/export → viewer.</p>
<p><strong>Look for:</strong> Where the chain breaks if one device changes.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

---



Covered above: relational colour claim, Roivainen platform styles, critical lens, debate, and placeholders.

---

## Masterclass

<figure class="lesson-figure" id="figure-masterclass-1" markdown="0">
<img src="{{ '/assets/images/deck-media/750f32a08550dcff.webp' | relative_url }}" alt="This is a digital graphic or print design, not a photograph, painting, or document. It features a 2x2 grid of solid color blocks—cyan (top-left), magenta (top-right), yellow (bottom-left), and black (bottom-right)—each containing a large, bold, white or black capital letter: “C”" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-1" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-2" markdown="0">
<img src="{{ '/assets/images/deck-media/7a2791f63dcc1d31.webp' | relative_url }}" alt="Nokia 8-display pixel pattern PNr°0495.jpg" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-2" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-3" markdown="0">
<img src="{{ '/assets/images/deck-media/67e8367fb0719e25.webp' | relative_url }}" alt="Fashion illustration" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-3" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-4" markdown="0">
<img src="{{ '/assets/images/deck-media/c425a4f37ec39601.webp' | relative_url }}" alt="Fashion illustration" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-4" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-5" markdown="0">
<img src="{{ '/assets/images/deck-media/37ef9f5bda8f9a93.webp' | relative_url }}" alt="An exhibition poster composition" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-5" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-6" markdown="0">
<img src="{{ '/assets/images/deck-media/9399010fa60a83d5.webp' | relative_url }}" alt="Test - image size comparison (Jpeg vs Png vs Jpeg XL vs Heic).png" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-6" %}</figcaption>
</figure>


**Claim:** colour is relational and perceptual, so digital palettes must be taught through interaction, contrast, and context — not as fixed swatches or isolated RGB values (Albers 2013).

A bitmap image is a fixed grid of colour values; every decision about mode, bit depth, or gamut is also a decision about what the image cannot later become without loss. Skilled digital image work produces visualities that reflect editing styles popular at a given moment — lighting, colour trends, and tones that make images look "professional" or "unique" [(Roivainen 2025, 8)](#ref-roivainen-2025).

**What this supports, and what it does not.** Albers (2013) supports perceptual colour teaching beyond tool menus. Roivainen (2025) supports naming platform-native, time-bound editing conventions — adjacent to fashion, not a validated fashion-colour syllabus. Neither validates a **colour-management teaching sequence** for fashion HE; tool docs ground operations only — label `[PLATFORM]`, never research.

**Practice anchor (field lens):** relational colour and bitmap literacy (Albers 2013); T1 technical colour operations.

**Frontier signal (field lens):** platform-native editing styles circulate quickly; treat trending tones as historical signals to compare, not defaults to copy.

## Lab (Portfolio)

*A geometrical slide announces the Lab: **two** exercises follow. Traces go into the **portfolio index**. Labs practise Masterclass and feed **ACT2 Key visual** craft — they do not invent a second graded Campus Virtual channel.*

### Exercise 1 — Lock the key-visual brief, then sample a palette {#lab-exercise-1}

Practises Masterclass ideas **1** (colour is a relation) and **6** (correcting vs changing).

**Time:** 20 minutes.

**Group:** alone for craft; pairs OK for a 2-minute brief critique.

**Materials:** laptop; one rights-clear garment/fabric photo; timer; notes app.

**Steps:**

1. Write **audience**, **channel**, and a **single claim** before opening the canvas.
2. Sample five colours from the garment photo; build a palette strip (no moodboard tiles yet).
3. Build one accessible alternate (contrast-aware) without inventing a second claim.
4. Reject any swatch that does not serve the claim.
5. Note one hierarchy decision the clash forced.

**Portfolio trace:** brief text + five-colour strip + accessible alternate + hierarchy note.

**Judged by:** [Portfolio rubric — process evidence and craft]({{ '/assignments/en/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (key-visual / palette craft gap — no Wave-1 verified pedagogy sequence).

**Example trace:** *(Illustrative · not student work.)* Brief: audience = campus drop, channel = Instagram square, claim = “denim reads cooler under tungsten.” Five-swatch strip + one high-contrast alternate; hierarchy note: “Claim forced the mid-blue to lose saturation.”


### Exercise 2 — One Gestalt pass on a key-visual crop {#lab-exercise-2}

Practises Masterclass ideas **2** (a bitmap has limits) and **4** (the display participates).

**Time:** 20 minutes.

**Group:** alone for the two crops; pairs for the peer vote.

**Materials:** a key-visual or fashion crop; bitmap editor; timer.

**Steps:**

1. Name one Gestalt relation to test (proximity, similarity, closure, continuity, or figure–ground).
2. Apply the relation once to the crop.
3. Invert or break the relation in a second version; keep both.
4. Peer names which version groups more clearly and why (one sentence).
5. Record the chosen relation in the process note.

**Portfolio trace:** two crops + peer sentence + process note naming the relation.

**Judged by:** [Portfolio rubric — composition judgement]({{ '/assignments/en/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (Gestalt pedagogy gap — Arnheim not in Wave-1 references).

**Example trace:** *(Illustrative · not student work.)* Relation = proximity. Crop A clusters buttons; crop B spreads them. Peer: “A groups as a placket; B reads as scatter.”


**Definition of done (studio slice):** piece ID; process folder; colour/Gestalt pair present and specific — the Lab traces are the cuaderno evidence.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidence:** Investigaciones y proyectos 20% (piece); Cuaderno 10% (note). No S1/S2 — ARTEFACT ROLE none.
LAB_LINE: exercise=1; method_id=key-visual-brief-lock; practises=masterclass-1,masterclass-6; source=gap/classroom adaptation; ACT=ACT2
LAB_LINE: exercise=2; method_id=gestalt-composition; practises=masterclass-2,masterclass-4; source=gap/classroom adaptation; ACT=ACT2
-->
{% endif %}

---

## Workshop

From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.


1. **Diagnostic.** Given two versions of the same bitmap at different bit depths, identify which artifact each shows and why.
2. Describe by hand, no tool open, the visual difference between a limited and a full palette for a described image. **No AI — declared as such.**
3. Distinguish "colour correction" from "colour change" for a described edit, using B1's disclosure framing.

Professor answer sketches are not published on this page.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "palette-depth — restricted and nuanced pixel fields divided by a correction threshold"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Conclusion

This unit leaves named gaps on purpose: what the vault can page-verify stays in References; what remains open stays in the Editorial note. Keep Lab traces honest in the portfolio index. Do not invent a graded deliverable that How to Pass does not ask for. The next stake is the session rhythm already named — Analysis defence (D1) from session 3, Workshop from session 4 for Transposition and the final event.

---

## Tao of the Image {#tao-of-the-image}

Unit epigraph (studio Tao register — not a scholarly quotation):

> _"The raster image fears the zoom. The SVG welcomes it."_

Deck and lesson links that target `#tao-of-the-image` resolve here.

---

## References

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.3; temario=T1-image-2d-volume.pass1.resultant.mdc § "Color; mapas de bits"; subfield_runs=dc-2d-image-craft-pedagogy/pass1.edited.md § colour management
CRITICAL_ROUTING: unit=I.3; critica=C1 algorithmic colour trends; C3 AlDahoul image-generation bias; session default-viewer prompt
PROVENANCE_LINE: claim=I.3.claim.relational-colour; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="Albers perceptual colour digital palettes"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Albers; similarity=null; proposed_use="perceptual anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Albers 2013 not in scholar vault; quote=none; public_citation="(Albers 2013)"; supports="relational perceptual colour teaching"; does_not_support="colour-management pedagogy sequence"
PROVENANCE_LINE: claim=I.3.claim.platform-editing-styles; status=VERIFIED; page_basis=printed; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="skilled vision Instagram editing colour trends"; source_locator=MASTER-IDEAS I.3; similarity=null; proposed_use="frontier/platform colour conventions"}; source={document_coat=47ce5b17; extraction_db=ahmes-library/scholar/documents/how_i_edit_my_instagram_images_investigating_skilled_vision_in_the_work_of_youtube_s_lifestyle_content_creators_47ce5b17/extract/extraction.db; node_id=307e67e0-f3a3-5fa3-a623-ceebc74fd70c; page_index=7; printed_page=8}; resolver="ahmes query --cite extraction.db:307e67e0-f3a3-5fa3-a623-ceebc74fd70c --require-evaluator-safe evaluator_safe=yes"; quote="editing styles that are popular at a given moment"; public_citation="[(Roivainen 2025, 8)](#ref-roivainen-2025)"; supports="time-bound platform colour and tonal conventions"; does_not_support="fashion-specific colour syllabus or classroom efficacy"
PROVENANCE_LINE: claim=I.3.gap.colour-management-pedagogy; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion higher education colour management pedagogy validated"; source_locator=null; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated colour-management teaching method for fashion students"
PROVENANCE_LINE: claim=I.3.critical.generative-bias; status=VERIFIED; page_basis=printed; discovery={service=Ahmes; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="AI generated faces gender racial homogenization"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc § AlDahoul; similarity=null; proposed_use="critical technical + deck critical slide"}; source={document_coat=fe54fc54; extraction_db=ahmes-library/scholar/documents/10_1038_s41598_025_99623_3_ai_generated_faces_influence_gender_stereotypes_and_racial_h_fe54fc54/extract/extraction.db; node_id=b3fd5903-1b33-50b3-8abe-cd2e9241513a; page_index=0; printed_page=1}; resolver="sqlite fission_node + anchor_spatial; abstract racial homogenization claim"; quote="This analysis reveals significant racial homogenization, e.g., depicting nearly all Middle Eastern men as bearded, brown-skinned, and wearing traditional attire."; public_citation="[(AlDahoul et al. 2025)](#ref-aldahoul-2025)"; supports="image tools are not representationally neutral; racial homogenization in generative faces"; does_not_support="classroom policy prescription or colour-management pedagogy"
PROVENANCE_LINE: claim=I.3.critical.default-viewer; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="colour accuracy default viewer accessibility"; source_locator=i-3-colour-bitmaps.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming default viewer and contrast assumptions"; does_not_support="empirical accessibility claim for cohort"
MEDIA_RIGHTS_LINE: slot=I.3.video.colour-workflow; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.3.still.palette-contrast; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.3.graphic.colour-chain; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}

---

## Editorial note. Work in progress. Teaching Innovation Practice
{: .lesson-editorial-note }

**Declared gap — stated plainly.** No reviewed source validates a fashion-HE **colour-management teaching sequence**. Albers and Roivainen support perceptual and platform-colour literacy; they do not prove this classroom workflow teaches better than an alternative.

This note is part of an ongoing *Práctica de Innovación docente* — epistemic limits stay here, not between Masterclass paragraphs.

---

## AI-assisted authorship

This lesson was written with local AI-assisted drafting under the author's editorial control. Student and teaching AI declaration: [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).


{% if site.publication.publish_internal_metadata %}
<!-- lesson_uuid: 7eded8ac-9620-463a-a84f-d85fb34f93b6
     vault_refs_consulted: 5
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
