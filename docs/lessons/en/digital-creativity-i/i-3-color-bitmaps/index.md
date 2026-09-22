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

## 🎯 Learning Objectives

- **Describe a bitmap image as a fixed grid of colour values** — and explain what a given colour decision (mode, depth, gamut) forecloses for later.
- **Explain colour as relational and perceptual** — digital palettes taught through interaction, contrast, and context, not isolated RGB sliders [(Albers 2013)](#ref-albers-2013).
- **Name how creator technologies produce time-bound colour and tonal conventions** on platforms [(Roivainen 2025, 8)](#ref-roivainen-2025).
- **Produce a colour comparison** (not a single “final” palette): what changed, what stayed legible, which platform or cultural code you invoked.
- **Distinguish "colour correction" from "colour change"** — a disclosure question, not a technical one.

---

## Why this unit exists — colour as relation, not a one-time palette

**Claim:** colour is relational and perceptual, so digital palettes must be taught through interaction, contrast, and context — not as fixed swatches or isolated RGB values [(Albers 2013)](#ref-albers-2013).

A bitmap image is a fixed grid of colour values; every decision about mode, bit depth, or gamut is also a decision about what the image cannot later become without loss. Skilled digital image work produces visualities that reflect editing styles popular at a given moment — lighting, colour trends, and tones that make images look "professional" or "unique" [(Roivainen 2025, 8)](#ref-roivainen-2025).

**What this supports, and what it does not.** Albers (2013) supports perceptual colour teaching beyond tool menus. Roivainen (2025) supports naming platform-native, time-bound editing conventions — adjacent to fashion, not a validated fashion-colour syllabus. Neither validates a **colour-management teaching sequence** for fashion HE; tool docs ground operations only — label `[PLATFORM]`, never research.

**Practice anchor (field lens):** relational colour and bitmap literacy [(Albers 2013)](#ref-albers-2013); T1 technical colour operations.

**Frontier signal (field lens):** platform-native editing styles circulate quickly; treat trending tones as historical signals to compare, not defaults to copy.

## Critical perspective

Computational fashion research can extract palettes and forecast colour, while
fashion-design teaching can ask students to specify palettes in HEX or Pantone
terms [(Nobile et al. 2021)](#ref-nobile-2021); [(Balasubramanian 2026)](#ref-balasubramanian-2026). That precedent is useful for
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

## B1 · Conceptual — magistral 1 h + seminarios 2 h + debates 1 h

Covered above: relational colour claim, Roivainen platform styles, critical lens, debate, and placeholders.

---

## B2 · Studio — talleres 1 h + investigaciones y proyectos 2 h

**Deliverable:** a **colour comparison** — two palettes or colour-mode versions of the same fashion image — with a process note naming what changed, what remained legible, and which platform or cultural code you invoked.

**Definition of done:** piece ID; process folder; the trade-off note present and specific.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidence:** Investigaciones y proyectos 20% (piece); Cuaderno 10% (note). No S1/S2 — ARTEFACT ROLE none.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, decontextualised

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

## References

- Balasubramanian, Mahendran. 2026. “Implementing Generative AI in Fashion Design Curriculum.” *Frontiers in Education*. <a href="https://doi.org/10.3389/feduc.2026.1824003" target="_blank" rel="noopener noreferrer">https://doi.org/10.3389/feduc.2026.1824003</a>.
- Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education* 14. <a href="https://doi.org/10.1080/17543266.2021.1931476" target="_blank" rel="noopener noreferrer">https://doi.org/10.1080/17543266.2021.1931476</a>.

- Albers, Josef. 2013. *Interaction of Color: 50th Anniversary Edition*. New Haven: Yale University Press. ISBN 9780300179354.
- AlDahoul, Nouar, Talal Rahwan, and Yasir Zaki. 2025. "AI-Generated Faces Influence Gender Stereotypes and Racial Homogenization." *Scientific Reports* 15: 14449. <a href="https://doi.org/10.1038/s41598-025-99623-3" target="_blank" rel="noopener noreferrer">https://doi.org/10.1038/s41598-025-99623-3</a>.
- Roivainen, Ida. 2025. "'How I Edit My Instagram Images': Investigating Skilled Vision in the Work of YouTube's Lifestyle-Content Creators." *Visual Studies* 40 (3): 569–585. <a href="https://doi.org/10.1080/1472586X.2024.2353689" target="_blank" rel="noopener noreferrer">https://doi.org/10.1080/1472586X.2024.2353689</a>.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.3; temario=T1-image-2d-volume.pass1.resultant.mdc § "Color; mapas de bits"; subfield_runs=dc-2d-image-craft-pedagogy/pass1.edited.md § colour management
CRITICAL_ROUTING: unit=I.3; critica=C1 algorithmic colour trends; C3 AlDahoul image-generation bias; session default-viewer prompt
PROVENANCE_LINE: claim=I.3.claim.relational-colour; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="Albers perceptual colour digital palettes"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Albers; similarity=null; proposed_use="perceptual anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Albers 2013 not in scholar vault; quote=none; public_citation="(Albers 2013)"; supports="relational perceptual colour teaching"; does_not_support="colour-management pedagogy sequence"
PROVENANCE_LINE: claim=I.3.claim.platform-editing-styles; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="skilled vision Instagram editing colour trends"; source_locator=MASTER-IDEAS I.3; similarity=null; proposed_use="frontier/platform colour conventions"}; source={document_coat=47ce5b17; extraction_db=ahmes-library/scholar/documents/how_i_edit_my_instagram_images_investigating_skilled_vision_in_the_work_of_youtube_s_lifestyle_content_creators_47ce5b17/extract/extraction.db; node_id=307e67e0-f3a3-5fa3-a623-ceebc74fd70c; page_index=7; printed_page=8}; resolver="ahmes query --cite extraction.db:307e67e0-f3a3-5fa3-a623-ceebc74fd70c --require-evaluator-safe evaluator_safe=yes"; quote="editing styles that are popular at a given moment"; public_citation="(Roivainen 2025, 8)"; supports="time-bound platform colour and tonal conventions"; does_not_support="fashion-specific colour syllabus or classroom efficacy"
PROVENANCE_LINE: claim=I.3.gap.colour-management-pedagogy; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion higher education colour management pedagogy validated"; source_locator=null; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated colour-management teaching method for fashion students"
PROVENANCE_LINE: claim=I.3.critical.generative-bias; status=VERIFIED; discovery={service=Ahmes; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="AI generated faces gender racial homogenization"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc § AlDahoul; similarity=null; proposed_use="critical technical + deck critical slide"}; source={document_coat=fe54fc54; extraction_db=ahmes-library/scholar/documents/10_1038_s41598_025_99623_3_ai_generated_faces_influence_gender_stereotypes_and_racial_h_fe54fc54/extract/extraction.db; node_id=b3fd5903-1b33-50b3-8abe-cd2e9241513a; page_index=0; printed_page=1}; resolver="sqlite fission_node + anchor_spatial; abstract racial homogenization claim"; quote="This analysis reveals significant racial homogenization, e.g., depicting nearly all Middle Eastern men as bearded, brown-skinned, and wearing traditional attire."; public_citation="(AlDahoul et al. 2025)"; supports="image tools are not representationally neutral; racial homogenization in generative faces"; does_not_support="classroom policy prescription or colour-management pedagogy"
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

Rubén Vega Balbás, PhD (`ruvebal@crea-comm.net`) wrote this lesson in the
crea-comm.net studio environment — a local agentic harness with MCP-backed
retrieval, RAG context from the curriculum vault, and a scholar-voice model
fine-tuned on his own writing. Forging consulted **5** vault sources; every
public `(Author, Year)` was checked against that vault before acceptance.
Prompts, model drafts, and human amendments are archived for later evaluation.
Editorial judgment and responsibility for the final text remain with the author.

Student and teaching AI declaration: [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).

*Forge date: 2026-09-22 · Studio: crea-comm.net · harness: `lesson-scribe` v0.1 · prompt-v2.1*


{% if site.publication.publish_internal_metadata %}
<!-- lesson_uuid: 7eded8ac-9620-463a-a84f-d85fb34f93b6
     vault_refs_consulted: 5
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
