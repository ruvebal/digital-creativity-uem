---
layout: lesson
title: 'II.2 · Avatar Creation'
title_es: 'II.2 · Creación de avatares'
slug: ii-2-avatares
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/digital-creativity-ii/ii-2-avatares/
description: 'An avatar is an identity claim, not a neutral mannequin — deciding what it represents is the graded skill, not the modelling tool.'
status: scaffold
tags: [digital-creativity-ii, avatars, identity, representation, genai-studio]
---

<!-- prettier-ignore-start -->

## 📋 Table of Contents
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"In a forest, every tree must be itself. Reuse is wisdom, but identity is sacred."_
> — Tao of Development, `arch-017`
{: .tao-development-quote }

> **AI Assistance Disclosure:** avatars may be hand-modelled, AI-generated, or a hybrid. Every avatar piece carries an identity-intent note and, where a generator was used, an AI-use declaration — same discipline as II.5's portfolio pieces.

---

{% include lesson-semantic-graphic.html %}

## Where this sits — CONTENIDOS and competencies

**CONTENIDOS anchor (verbatim, official guía):** *Creación de avatares.*

**Competencies served (`3-creacion-digital-ii.json`):** `CON1` (differentiate audiovisual representation techniques and their dissemination media), `HAB1` (graphically represent fashion ideas), `COMP8` (handle digital graphic/audiovisual representation tools in fashion communication), `COMP9` (create new ideas from known concepts, solving problems originally).

**Learning outcomes this unit serves** (verbatim from `learning_outcomes`): *"Aplicar herramientas informáticas avanzadas en la creación y la representación digital de creaciones de moda."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."*

**Evaluation weights this unit's evidence can feed** (CD II presencial, framework §6): **Investigaciones y proyectos 20%** scores the avatar piece; the identity-intent note can feed **Cuaderno de prácticas de laboratorio/taller 10%**.

---

## 🎯 Learning Objectives

By the end of this unit, you will be able to:

- **Build one avatar piece** — hand-modelled, AI-assisted, or hybrid — to a professional craft standard.
- **Write an identity-intent note** — what body type, skin tone, and styling choices were made, and why.
- **Declare AI use honestly** where a generator was part of the pipeline.
- **Distinguish avatar creation from VTON** — this unit's avatar represents an identity, not a virtual try-on fit-check.
- **Connect avatar choices to adjacent research on authorship and embodiment** — hybrid-authorship instruction can strengthen student voice when authorship limits are explicit (Anwar 2025, 1); first- versus third-person avatar customization can change embodiment experience (Gonzalez-Franco et al. 2024, 12).

---

## Why this unit exists — an avatar is an identity claim first

**Claim:** an avatar is an identity claim, not a neutral mannequin. Every default the student does *not* deliberately choose — body type, skin tone, proportions — is still a choice, made by the tool's defaults instead of the student.

A scoped finding from Anwar, Raza, and Marzouk's systematic review is useful as an **adjacent guardrail**, not as avatar-method evidence: the authors recommend that instruction make authorship, copyright, and ownership limits explicit through hybrid-authorship workshops and critique. The studio translation here is concrete: every avatar keeps an identity-intent note, a tool/material declaration, and one human-judgement checkpoint. The review does **not** establish which avatar workflow or assessment sequence works best (Anwar 2025, 1).

A virtual-reality experiment offers a second, deliberately narrow anchor: first-person avatar customization was compared with third-person configuration. In that study, the third-person condition reduced embodiment of the larger avatar, while the first-person condition did not show that reduction. For this studio, that makes editing perspective and body representation decisions worth justifying; it **does not** show that one sequence teaches avatar modelling better, nor does it justify generalising from a small sample (Gonzalez-Franco et al. 2024, 12).

**What this supports, and what it does not.** Anwar (2025) supports making authorship, copyright, and ownership limits explicit in studio instruction. Gonzalez-Franco et al. (2024) supports treating editing perspective and body representation as decisions to justify. **No reviewed source validates an avatar-modelling teaching sequence** for HE; tool docs ground operations only — label `[PLATFORM]`, never research.

**VTON/try-on is explicitly out of scope.** This unit's avatar exists to represent a body/identity; it does not simulate a garment fit-check on that body.

**Practice anchor (field lens):** mesh or parametric body, skin/material assignment, pose, camera, and garment attachment as durable operation classes — separate from any one avatar application's UI or preset library.

**Frontier signal (field lens):** generative avatar pipelines and AI-assisted character tools may accelerate output faster than pedagogical validation; treat any generated body as input to identity judgement, not proof that an identity-intent note is honest or complete.

## Critical perspective

Avatar libraries are not neutral representations of the body: the categories, skin tones, and available features condition which identities can be recognised and studied in virtual environments.

Contemporary visual generation and classification systems can reproduce intersectional gender and racial inequalities, so the tools used to produce fashion imagery should not be treated as representationally neutral infrastructure (AlDahoul, Rahwan, and Zaki 2025).

### The debate prompt

Should a student avatar disclose that it is not a photograph of the student? Does that answer change if the avatar is AI-generated versus hand-modelled?

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.video.avatar-breakdown" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for an avatar design breakdown demonstration; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> A short breakdown pauses before each identity decision so students label body, pose, garment, and viewpoint choices.</p>
<p><strong>Look for:</strong> Default preset, deliberate override, representational effect, and what each step forecloses.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.still.identity-exemplar" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for respectful avatar exemplar and stereotype counterexample; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Paired stills test legibility, restraint, and what remains readable after identity configuration.</p>
<p><strong>Look for:</strong> Authored identity choice versus unexamined default.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.graphic.component-map" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract diagram placeholder for identity-body-pose-garment-camera-provenance chain; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Maps identity fiction → body → pose → garment → camera → authorship declaration.</p>
<p><strong>Look for:</strong> Where a default could be replaced with a deliberate identity decision.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

Covered above: Anwar/Gonzalez-Franco framing, critical lens, debate, and placeholders. Cover avatar-creation technique (whichever tool the studio uses) as craft, then pair each technique with the identity question it raises: *if I accept this default, what identity am I claiming that I did not choose?* Run the debate prompt above before any hands-on work. Make explicit: the grade is on the *identity decision*, not on which tool produced the mesh.

---

## B2 · Taller — talleres 2 h + investigaciones y proyectos 3 h (workplace-like, contextualised)

**Deliverable:** one avatar piece with a written **identity-intent note** (body type, skin tone, styling choices — what and why) and an AI-use declaration if a generator was used ("none" is valid).

**Definition of done:**
- Piece exists; identity-intent note present and specific (not a generic "made in [tool]").
- Piece ID assigned; process folder kept even if not published.

**If you want this piece exhibited publicly** (vShowroom), attach the **unsigned** consent checklist below to the process folder now. Filling it in is not signing it — no DPO approval exists yet.

### S1 — Exhibit this piece in vShowroom (unsigned draft — do not sign)

**Pieza / piece ID:** _________________
**Tipo:** still / avatar / look / video / other: _______

- [ ] I licence Universidad Europea / the vShowroom operators to **display** this piece on the showroom (web). I keep copyright.
- [ ] The licence is **revocable**. After withdrawal the public page comes down within a DPO/ops-defined delay (suggested 14 days). Cached copies may linger briefly.
- [ ] This is **not** a sale, a VTON/try-on right, or a right to train models on my work.

Nombre · Fecha · Firma — *(unsigned template; not a live consent instrument)*

### S2 — Attribution vs. anonymity (unsigned draft — do not sign)

Default: **attributed** (name as the student writes it).

- [ ] Show my name / chosen designer name: _________________
- [ ] Exhibit **without** my civil name (piece ID only)

S2 without S1 does nothing. S1 without S2 defaults to attributed.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidence:** Investigaciones y proyectos 20% (avatar piece); Cuaderno 10% (identity-intent note). S1/S2 optional for vShowroom exhibition — attach unsigned drafts only; no live consent instrument.
Tool docs referenced (any 3D/avatar-creation software) are dated platform notes, not research citations — check versions before class.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, decontextualised

1. **Diagnostic.** Given an avatar-generation brief where every customizable trait defaults to one narrow body type, name the representational problem and how you would correct it.
2. Write the identity-intent note (body type, skin tone, styling, and why) for a described avatar concept — without using any generator.
3. **No-AI, declared:** in two sentences, explain why this unit's avatar is not a VTON/try-on simulation.

Professor answer sketches are not published on this page — kept in the instructor's private notes.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "identity-parameters — one narrow default branches into equally weighted identity configurations"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## References

- AlDahoul, Nouar, Talal Rahwan, and Yasir Zaki. 2025. "AI-generated faces influence gender stereotypes and racial homogenization." *Scientific Reports* 15: 14449. https://doi.org/10.1038/s41598-025-99623-3.
- Anwar, S., A. Raza, and R. Marzouk. 2025. "Generative AI in Studio-Based Fashion Education: A Systematic Literature Review." *European Journal of Business and Management*. https://doi.org/10.65136/ejbm.v10i4.24.
- Gonzalez-Franco, M., A. Steed, C. C. Berger, and A. Tajadura-Jiménez. 2024. "The Impact of First-Person Avatar Customization on Embodiment in Immersive Virtual Reality." *Frontiers in Virtual Reality* 5: 1436752. https://doi.org/10.3389/frvir.2024.1436752.

**Declared gap — stated plainly.** Anwar (2025) and Gonzalez-Franco et al. (2024) support authorship guardrails and embodiment perspective respectively; they do **not** prove that this classroom's avatar sequence, identity-intent rubric, or deliverable teaches avatar creation better than an alternative. No reviewed source validates an avatar-modelling method for fashion education. Research on anthropomorphism in fashion-AI contexts may inform why identity claims matter, but that literature remains outside this unit's verified bibliography. VTON/try-on is out of scope for this unit and remains unaddressed by design.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=II.2; temario=T2-avatars-experiences.pass1.resultant.mdc § avatars; subfield_runs=digital-creativity/03-temario-critica/C2-fashion-virtuality.pass1.resultant.mdc
CRITICAL_ROUTING: unit=II.2; critica=C2 avatar libraries L17; C3 gender/race generation L17; session identity-agency prompt
PROVENANCE_LINE: claim=II.2.claim.hybrid-authorship-guardrail; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="hybrid authorship workshops critique GenAI fashion education Anwar"; source_locator=T2-avatars-experiences.pass1.resultant.mdc § Anwar; similarity=null; proposed_use="adjacent guardrail"}; source={document_coat=ejbm_v10i4_24; extraction_db=ahmes-library/scholar/documents/generative_ai_in_studio_based_fashion_education_a_systematic_literature_review_ejbm_v10i4_24/extract/extraction.db; node_id=cd329fc8-be24-5335-ad0d-4fe91dd97693; page_index=0; printed_page=1}; resolver="ahmes query --cite extraction.db:cd329fc8-be24-5335-ad0d-4fe91dd97693 --require-evaluator-safe evaluator_safe=yes"; quote="authorship, copyright, and ownership limits explicit through hybrid-authorship workshops and critique"; public_citation="(Anwar 2025, 1)"; supports="explicit authorship/copyright/ownership instruction in studio"; does_not_support="avatar modelling method or assessment sequence"
PROVENANCE_LINE: claim=II.2.claim.embodiment-perspective; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="first-person third-person avatar customization embodiment Gonzalez-Franco"; source_locator=T2-avatars-experiences.pass1.resultant.mdc § Gonzalez-Franco; similarity=null; proposed_use="perspective ethics anchor"}; source={document_coat=10_3389_frvir_2024_1436752; extraction_db=ahmes-library/scholar/documents/the_impact_of_first_person_avatar_customization_on_embodiment_in_immersive_virtual_reality_10_3389_frvir_2024_1436752/extract/extraction.db; node_id=c17b40cf-11e0-57d4-86c2-eefca69448c0; page_index=11; printed_page=12}; resolver="ahmes query --cite extraction.db:c17b40cf-11e0-57d4-86c2-eefca69448c0 --require-evaluator-safe evaluator_safe=yes"; quote="third-person condition reduced embodiment of the larger avatar"; public_citation="(Gonzalez-Franco et al. 2024, 12)"; supports="editing perspective affects embodiment experience"; does_not_support="avatar modelling teaching sequence or fashion-education assessment"
PROVENANCE_LINE: claim=II.2.gap.avatar-modelling-sequence; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="validated avatar modelling teaching sequence fashion HE"; source_locator=T2-avatars-experiences.pass1.resultant.mdc; similarity=null; proposed_use="honest gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated avatar-modelling method for fashion students"
PROVENANCE_LINE: claim=II.2.critical.avatar-libraries; status=NONE; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="bibliotecas avatares no representaciones neutrales cuerpo"; source_locator=C2-fashion-virtuality.pass1.resultant.mdc L17; similarity=null; proposed_use="critical established"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote="Las bibliotecas de avatares no son representaciones neutrales del cuerpo"; public_citation=OMITTED; supports="avatar libraries condition recognisable identities"; does_not_support="mandatory VALID library assignment"
PROVENANCE_LINE: claim=II.2.critical.generation-bias; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="generacion clasificacion visual desigualdades genero racializacion Stable Diffusion"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc L17; similarity=null; proposed_use="critical technical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.1038/s41598-025-99623-3 not in scholar vault; quote=none; public_citation="(AlDahoul, Rahwan, and Zaki 2025)"; supports="generation systems reproduce gender and racial inequalities"; does_not_support="which avatar tool students must use"
PROVENANCE_LINE: claim=II.2.critical.anthropomorphism; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="antropomorfismo IA moda Rodriguez-Borlado"; source_locator=grounding matrix II.2; similarity=null; proposed_use="adjacent mechanism naming"}; source={document_coat=rodriguez_borlado_perez_curiel_universitas_ia_moda_2024_f711009d; extraction_db=ahmes-library/scholar/documents/rodriguez_borlado_perez_curiel_universitas_ia_moda_2024_f711009d/extract/extraction.db; node_id=b6b4d953-b4af-596c-affe-0bc4a44aae9a; page_index=3; printed_page=4}; resolver=OMITTED; ahmes_attempt=evaluator_safe=no host registry mismatch; quote=none; public_citation=OMITTED; supports="anthropomorphism mechanism worth naming to students"; does_not_support="avatar modelling method or CV bibliography entry"
PROVENANCE_LINE: claim=II.2.critical.identity-agency-prompt; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="avatar agency identity defaults"; source_locator=ii-2-avatars.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming identity agency as studio question"; does_not_support="empirical claim about cohort norms"
MEDIA_RIGHTS_LINE: slot=II.2.video.avatar-breakdown; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.2.still.identity-exemplar; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.2.graphic.component-map; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}
