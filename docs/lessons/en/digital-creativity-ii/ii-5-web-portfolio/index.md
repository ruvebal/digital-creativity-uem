---
layout: lesson
title: 'II.5 · Web Layout, Editing & Digital Portfolio Creation'
title_es: 'II.5 · Maquetación, edición y creación de web y portfolio digital'
slug: ii-5-web-portfolio
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/digital-creativity-ii/ii-5-web-portfolio/
description: 'Portfolio and web layout for fashion communication: making process and authorship visible, not just the finished look.'
status: scaffold
tags: [digital-creativity-ii, portfolio, web, authorship, genai-studio]
---

<!-- prettier-ignore-start -->

## 📋 Table of Contents
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"To understand the docs is to understand the code. To understand the code is to understand the mind that wrote it."_
> — Tao of Development, `qa-010`
{: .tao-development-quote }

> **AI Assistance Disclosure:** This unit is designed for a course where generative AI is a normal studio tool. Every piece placed on a portfolio carries an authorship trail, not just a finished image.

---

{% include lesson-semantic-graphic.html %}

## Where this sits — CONTENIDOS and competencies

**CONTENIDOS anchor (verbatim, official guía):** *Maquetación, edición y creación de web y portfolio digital.*

**Competencies served (`3-creacion-digital-ii.json`):** `CON1` (differentiate audiovisual representation techniques and their dissemination media), `HAB10` (design a fashion firm's brand image), `COMP8` (handle digital graphic/audiovisual representation tools in communicating fashion ideas or projects), `COMP9` (create new ideas from known concepts, reaching conclusions or solving problems originally).

**Learning outcomes this unit serves** (verbatim from the guía's `learning_outcomes`, not invented extras): *"Maquetar proyectos y trabajos de diseño con calidad profesional."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."* · *"Manejar formatos de archivo digitales propios y genéricos."*

**Evaluation weights this unit's evidence can feed** (CD II presencial, framework §6): **Investigaciones y proyectos 20%** is where this unit's portfolio deliverable is scored directly; its process trail (decisions, iterations, AI declaration) can also feed **Cuaderno de prácticas de laboratorio/taller 10%**. This unit does not touch Pruebas (55%) or Caso/problema (15%).

---

## 🎯 Learning Objectives

By the end of this unit, you will be able to:

- **Lay out a portfolio page** at a professional quality bar, not a placeholder grid.
- **Make process visible** — decisions, iterations, and tool use are part of what the page communicates, not an afterthought.
- **Declare AI use honestly** — name which pieces used a generator, for what, and what you changed.
- **Distinguish co-creation from authorship erasure** — where the line falls when a look was made *with* a generator.
- **Understand the exhibition boundary** — what it takes, formally, for a piece to leave your own folder and appear on a public showroom page.

---

## Why this unit exists — process and authorship must be visible

**Claim:** a portfolio page is assessable when its process and authorship are visible on the page, not merely when the images look finished. Polish without a trail is not the learning outcome this unit teaches.

A systematic review of generative AI in studio-based fashion education (28 academic sources, 2018–2025) identifies **Learner Identity & Authorship** as one of four core thematic pillars shaping how GenAI changes studio pedagogy — alongside Knowledge Construction, Teaching Practice, and Studio Culture & Ethics — and names the tension directly: GenAI brings “enhanced creative ideation and efficiency” alongside “concerns over originality, ethical responsibility, and equitable access” (Anwar, Raza, and Marzouk 2025, 1).

Rizzi and Bertola frame AI-assisted fashion design not as authorship replacement but as **complement**: AI is treated as a “supplement to natural human creativity,” with collaborative dynamics running through the *whole* process rather than one isolated phase (Rizzi and Bertola 2025, 10).

Garcia studied a web-design and development course in which 176 students completed weekly coding tasks culminating in a self-coded digital portfolio. The study treats the portfolio as evidence of technical competencies and as a learning artifact, not merely a container for pieces. It is a useful technical-course analogue for requiring a process trail; its one-group design and computing context **do not** prove which portfolio-UX, accessibility, or presentation pattern works best for fashion (Garcia 2025, 2, 4).

**What this supports, and what it does not.** Anwar et al. (2025), Rizzi and Bertola (2025), and Garcia (2025) support making authorship and process visible when GenAI is part of the studio, and integrating portfolio construction with technical tasks. **No reviewed source validates which fashion-portfolio web-UX patterns cause better communication, visibility, or hiring outcomes** — layout guidance below is professional craft, not research.

**Practice anchor (field lens):** semantic HTML structure, information architecture, responsive layout, alt text, credits, and a process trail as durable publishing operations — separate from any one static-site generator or hosting platform.

**Frontier signal (field lens):** AI portfolio generators and one-click site builders may produce polish faster than pedagogical validation; treat any generated page as input to judgement, not proof that authorship is honestly declared.

## Critical perspective

Decolonising fashion teaching is not the same as adding diverse examples to an intact canon: it requires examining how coloniality, teacher position, affect, and authority structure what the discipline recognises as fashion knowledge (Cheang and Suterwalla 2020).

A portfolio is self-presentation and evidence, while platforms and employers often reward visibility metrics over process trace. Who decides which proof counts — the finished render, the collaboration log, the tool declaration — is not neutral: platform authorship tension sits between what the page *shows* and what it can *prove* about the maker.

### The debate prompt

What counts as "the work" when a look was co-made with a generator? Anwar et al.'s authorship tension and Rizzi and Bertola's "supplement, not substitute" framing are two different answers — the studio should reach its own position, in writing, before the portfolio deliverable is due.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.video.portfolio-walkthrough" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for a portfolio process walkthrough; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> A short walkthrough tests whether navigation, case-study evidence, and maintenance assumptions are readable.</p>
<p><strong>Look for:</strong> Process trail versus image-only presentation — what each can and cannot prove.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.still.process-exemplar" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract placeholder for process-rich portfolio exemplar and image-only counterexample; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Paired pages test legibility of authorship, alt text, and inspectable process evidence.</p>
<p><strong>Look for:</strong> Craft purpose versus polish that hides collaboration.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.graphic.portfolio-ia" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Abstract diagram placeholder for home to case study to process to authorship declaration; no people or garments depicted." loading="lazy" />
<figcaption>
<p><strong>Why this is here:</strong> Maps home → selected work → case study → process → about/contact, plus an authorship declaration block.</p>
<p><strong>Look for:</strong> Where AI-use and credit lines must appear before the page reads as finished.</p>
<p class="media-note">Placeholder visual — licensed media pending review.</p>
</figcaption>
</figure>

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

Covered above: Anwar/Rizzi/Garcia framing, critical lens, debate, and placeholders.

### What "process visible" means on a page, concretely

A portfolio piece that only shows the final render answers "what did you make?" A portfolio piece with a process trail also answers "how did you make it, and what did you decide?" The minimum trail for this unit:

1. **The brief** — one sentence on what the piece was for.
2. **The process** — 2–4 process images or notes (sketch → 3D/AI pass → refinement → final), not just a before/after.
3. **The AI-use line** — which tool(s), for what step, and what you changed afterward. "None" is a valid, honest answer.
4. **The credit line** — your name (or chosen designer name, see S2 below), and any collaborators.

### Portfolio page structure — **Template**, adapt to your own content

```html
<!-- Template: replace all bracketed content -->
<article class="portfolio-piece">
	<h2>[Piece title]</h2>
	<p class="brief">[One-sentence brief: what was this piece for?]</p>

	<div class="process-trail">
		<h3>Process</h3>
		<img src="[sketch.jpg]" alt="[Initial sketch description]" />
		<img src="[iteration.jpg]" alt="[Mid-process iteration description]" />
		<img src="[final.jpg]" alt="[Final piece description]" />
	</div>

	<div class="ai-declaration">
		<h3>AI use</h3>
		<p>[Tool name] was used for [specific step]. [What you changed or verified afterward. Or: "No AI tools were used in this piece."]</p>
	</div>

	<p class="credit">[Your name or chosen designer name] · [date]</p>
</article>
```

### Minimal page shell — **Template**

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>[Your name] — Portfolio</title>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<header>
			<h1>[Your name or chosen designer name]</h1>
			<nav><!-- links to each piece --></nav>
		</header>
		<main>
			<!-- one <article class="portfolio-piece"> per piece -->
		</main>
	</body>
</html>
```

Quality bar is the guía's own phrase: *"calidad profesional"* — professional quality — not a Front-End meta-framework course. A static HTML/CSS page that loads correctly, reads clearly, and carries the process trail above meets the bar. You do not need Astro, React, or a build step to pass this unit.

---

## B2 · Studio — talleres 3 h + investigaciones y proyectos 4 h (workplace-like, contextualised)

**Deliverable:** one portfolio page (or small static site) that lays out your own Creación Digital work with a process trail and an AI-use declaration, per the structure above.

**Definition of done:**
- The page exists, locally or hosted, with at least one complete piece following the structure above.
- Each piece has a piece ID (a short slug you choose, e.g. `look-03-denim-hybrid`) and a process folder (sketches, intermediate renders, notes) — kept even if not all of it is published.
- An AI-use declaration is present for every piece, including pieces where no AI was used.
- **A public showroom URL is not required.** This deliverable can be complete and graded entirely inside your own folder.

**If you want a piece to be exhibited publicly** (vShowroom, a shared space this cohort's work may later populate as real users — see the track page), attach the **unsigned** consent checklist below to that piece's process folder now. Filling it in is not the same as signing it — these are drafts for you to understand what exhibition would require, not a live consent process. No DPO approval exists yet; nothing here authorizes actual publication.

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
**Evidence:** Investigaciones y proyectos 20% (portfolio deliverable); Cuaderno 10% (process trail + AI declaration). S1/S2 required before public vShowroom use only.
Tool docs referenced in this unit (any static-site generator, image editor, or hosting platform) are dated platform notes, not research citations — check versions before class.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, decontextualised

Not the portfolio deliverable. Short problems isolating one skill each:

1. **Diagnostic.** Given this broken HTML fragment, name what is wrong and fix it:

   ```html
   <!-- Excerpt — broken, for diagnosis only -->
   <img src="portrait.jpg" />
   <div>
     <h4>Look 02</h4>
     <p>Digital pattern draft, unedited</p>
   </div>
   ```

   (Hint: nothing here is semantically wrong syntax-wise — the problem is what's *missing* for an image that carries meaning on a portfolio page. Name it and add it.)

2. Given this piece description — *"A student used a generator to produce a full look image from a text prompt, made no further edits, and credited only themselves"* — identify what is missing from an honest AI-use declaration for this piece.

3. **No-AI, declared:** without AI assistance, write a two-sentence AI-use declaration for a piece where you sketched by hand, used an AI tool to generate three color variations, and manually selected and refined one.

Professor answer sketches are not published on this page — kept in the instructor's private notes.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "portfolio-lineage — process fragments converge into an inspectable page with visible authorship"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## References

- Anwar, S., A. Raza, and R. Marzouk. 2025. “Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.” *European Journal of Business and Management*. https://doi.org/10.65136/ejbm.v10i4.24.
- Cheang, Sarah, and Shehnaz Suterwalla. 2020. “Decolonizing the Curriculum? Transformation, Emotion, and Positionality in Teaching.” *Fashion Theory* 24 (6): 879–900. https://doi.org/10.1080/1362704X.2020.1800989.
- Garcia, M. B. 2025. “Self-Coded Digital Portfolios as an Authentic Project-Based Learning Assessment in Computing Education: Evidence from a Web Design and Development Course.” *Education Sciences* 15 (9): 1150. https://doi.org/10.3390/educsci15091150.
- Rizzi, G., and P. Bertola. 2025. “Exploring the Generative AI Potential in the Fashion Design Process.” *European Journal of Cultural Management and Policy*. https://doi.org/10.3389/ejcmp.2025.13875.

**Declared gap — stated plainly.** Anwar et al. (2025), Rizzi and Bertola (2025), and Garcia (2025) support authorship visibility and portfolio-as-evidence framing; they do **not** prove that this unit's HTML layout, accessibility choices, or portfolio structure cause better fashion communication, visibility, or hiring outcomes. No reviewed source validates fashion-portfolio web-UX outcomes for HE.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=II.5; temario=T2-retouch-video-portfolio.pass1.resultant.mdc § portfolio; subfield_runs=dc-fashion-portfolio-web-ux gap NONE
CRITICAL_ROUTING: unit=II.5; critica=C3 Cheang decolonizing curriculum L277; C1 platform authorship tension; session proof-beyond-polish prompt
PROVENANCE_LINE: claim=II.5.claim.genai-authorship-pillar; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="generative AI studio fashion education authorship Anwar"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Anwar; similarity=null; proposed_use="authorship anchor"}; source={document_coat=0598ec0e; extraction_db=ahmes-library/scholar/documents/generative_ai_in_studio_based_fashion_education_a_systematic_literature_review_0598ec0e/extract/extraction.db; node_id=c9a17328-72f7-56c8-95bf-b9860b1067b8; page_index=0; printed_page=1}; resolver="ahmes query --cite extraction.db:c9a17328-72f7-56c8-95bf-b9860b1067b8 --require-evaluator-safe evaluator_safe=yes"; quote="Learner Identity & Authorship"; public_citation="(Anwar, Raza, and Marzouk 2025, 1)"; supports="GenAI changes studio authorship; visibility is honest response"; does_not_support="which portfolio layout teaches best"
PROVENANCE_LINE: claim=II.5.claim.genai-complement; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="generative AI complement human creativity fashion design Rizzi"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Rizzi; similarity=null; proposed_use="complement anchor"}; source={document_coat=167816a4; extraction_db=ahmes-library/scholar/documents/exploring_the_generative_ai_potential_in_the_fashion_design_process_167816a4/extract/extraction.db; node_id=908f5339-781d-51cc-a803-47dfbf9c0677; page_index=9; printed_page=10}; resolver="ahmes query --cite extraction.db:908f5339-781d-51cc-a803-47dfbf9c0677 --require-evaluator-safe evaluator_safe=yes"; quote="supplement to natural human creativity"; public_citation="(Rizzi and Bertola 2025, 10)"; supports="AI as complement across whole process"; does_not_support="originality guarantee or hiring effect"
PROVENANCE_LINE: claim=II.5.claim.portfolio-pbl-analogue; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="self-coded digital portfolios web design Garcia"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Garcia; similarity=null; proposed_use="technical analogue"}; source={document_coat=educsci15091150; extraction_db=ahmes-library/scholar/documents/self_coded_digital_portfolios_as_an_authentic_project_based_learning_assessment_e09e72ca/extract/extraction.db; node_id=e09e72ca-5a4b-51dc-823a-1d05ea71ee8f; page_index=1; printed_page=2}; resolver="ahmes query --cite extraction.db:e09e72ca-5a4b-51dc-823a-1d05ea71ee8f --require-evaluator-safe evaluator_safe=yes"; quote="self-coded digital portfolio"; public_citation="(Garcia 2025, 2, 4)"; supports="portfolio as learning artifact and technical evidence"; does_not_support="fashion UX outcomes accessibility hiring causality"
PROVENANCE_LINE: claim=II.5.gap.fashion-portfolio-ux; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion portfolio web UX hiring outcomes"; source_locator=grounding/README.md row II.5; similarity=null; proposed_use="honest gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated fashion-portfolio layout or hiring effect"
PROVENANCE_LINE: claim=II.5.critical.decolonizing-curriculum; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="decolonizing curriculum fashion teaching Cheang Suterwalla"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc L277; similarity=null; proposed_use="critical theoretical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.1080/1362704X.2020.1800989 not in scholar vault; quote=none; public_citation="(Cheang and Suterwalla 2020)"; supports="decolonisation requires examining canon construction not additive diversity"; does_not_support="mandatory reading list assignment"
PROVENANCE_LINE: claim=II.5.critical.platform-authorship; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="portfolio proof beyond polish platform visibility"; source_locator=ii-5-web-portfolio.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming platform authorship tension"; does_not_support="employment outcome claim"
MEDIA_RIGHTS_LINE: slot=II.5.video.portfolio-walkthrough; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.5.still.process-exemplar; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.5.graphic.portfolio-ia; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}
