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
status: draft
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

> **AI Assistance Disclosure:** This unit is designed for a course where generative AI is a normal studio tool. Every piece placed on a portfolio carries an authorship trail, not just a finished image.

---

## Code conventions in this unit

- **CodeSandbox-ready** — complete file, copy-paste, runs as-is.
- **Excerpt** — partial pattern, illustrative. Does **not** run as-is.
- **Template** — copy and replace placeholder values before use.

This unit's HTML/CSS blocks are labelled individually; most are **Template** — a starting structure to adapt to your own portfolio content, not a finished site.

---

## Where this sits — CONTENIDOS and competencies

**CONTENIDOS anchor (verbatim, official guía):** *Maquetación, edición y creación de web y portfolio digital.*

**Competencies served (`3-creacion-digital-ii.json`):** `CON1` (differentiate audiovisual representation techniques and their dissemination media), `HAB10` (design a fashion firm's brand image), `COMP8` (handle digital graphic/audiovisual representation tools in communicating fashion ideas or projects), `COMP9` (create new ideas from known concepts, reaching conclusions or solving problems originally).

**Learning outcomes this unit serves** (verbatim from the guía's `learning_outcomes`, not invented extras): *"Maquetar proyectos y trabajos de diseño con calidad profesional."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."* · *"Manejar formatos de archivo digitales propios y genéricos."*

**Evaluation weights this unit's evidence can feed** (CD II presencial, framework §6): **Proyectos 10%** is where this unit's portfolio deliverable is scored directly; its process trail (decisions, iterations, AI declaration) can also feed **Informes y escritos 15%**. This unit does not touch Pruebas (55%) or Caso/problema (20%).

---

## 🎯 Learning Objectives

By the end of this unit, you will be able to:

- **Lay out a portfolio page** at a professional quality bar, not a placeholder grid.
- **Make process visible** — decisions, iterations, and tool use are part of what the page communicates, not an afterthought.
- **Declare AI use honestly** — name which pieces used a generator, for what, and what you changed.
- **Distinguish co-creation from authorship erasure** — where the line falls when a look was made *with* a generator.
- **Understand the exhibition boundary** — what it takes, formally, for a piece to leave your own folder and appear on a public showroom page.

---

## Why this unit exists: process and authorship must be visible

**Claim:** a portfolio page is assessable when its process and authorship are visible on the page, not merely when the images look finished. Polish without a trail is not the learning outcome this unit teaches.

This is not a stylistic preference. A systematic review of generative AI in studio-based fashion education (28 academic sources, 2018–2025) identifies **Learner Identity & Authorship** as one of four core thematic pillars shaping how GenAI changes studio pedagogy — alongside Knowledge Construction, Teaching Practice, and Studio Culture & Ethics — and names the tension directly: GenAI brings "enhanced creative ideation and efficiency" alongside "concerns over originality, ethical responsibility, and equitable access" (Anwar, Raza & Marzouk 2025, 1 — Ahmes coat `0598ec0e`, node `c9a17328-72f7-56c8-95bf-b9860b1067b8`).

A separate laboratory study of AI-assisted fashion design ("Artificial A(i)rchive") frames the relationship not as authorship replacement but as **complement**: AI is treated as a "supplement to natural human creativity," examined through six capabilities — Perceive, Think, Express, Collaborate, Build, Test — with the finding that collaborative dynamics run through the *whole* process rather than one isolated phase (Rizzi & Bertola 2025, 10 — Ahmes coat `167816a4`, node `908f5339-781d-51cc-a803-47dfbf9c0677`).

Read together: the field agrees GenAI changes studio authorship, and it agrees the honest response is visibility — showing the collaboration, not hiding it or pretending it didn't happen.

### Declared gap — read this before assuming the portfolio format itself is validated

**What is grounded above:** *why* authorship and process must be visible when GenAI is part of the studio. **What is NOT grounded:** which specific portfolio web-UX patterns, layouts, or accessibility choices actually help a fashion portfolio get hired, get seen, or communicate well. That question sits outside the current vault — it is a declared `[UNVERIFIED-GAP]` in the field map, not a solved problem being taught as settled research. HTML/CSS/tool documentation in this unit grounds **how** to build the page; it does not ground **why this layout teaches or hires better than another one**. Do not read the layout advice below as research-backed UX science — it is professional craft guidance, labelled as such.

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

### The debate prompt

Put this to the group before building anything: **what counts as "the work" when a look was co-made with a generator?** Anwar et al.'s authorship tension and Rizzi & Bertola's "supplement, not substitute" framing are two different answers — the studio should reach its own position, in writing, before the portfolio deliverable is due.

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

## B2 · Studio — talleres 3 h + proyectos 4 h (workplace-like, contextualised)

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

**Evidence this deliverable maps to:** Evaluación → **Proyectos (10%)** directly; the process trail and AI declaration can also support **Informes y escritos (15%)** if the instructor asks for a written reflection alongside the piece. This unit does not invent a fourth evaluation weight — only these two are claimed.

Tool docs referenced in this unit (any static-site generator, image editor, or hosting platform) are dated platform notes, not research citations — check versions before class.

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

---

## Provenance and evidence gate

- Anwar, S., Raza, A. &amp; Marzouk, R. (2025). *Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.* European Journal of Business and Management, `10.65136/ejbm.v10i4.24`. Ahmes coat `0598ec0e`, node `c9a17328-72f7-56c8-95bf-b9860b1067b8`, p.1. `(Anwar 2025, 1)`. Resolved via `ahmes query --cite`, `evaluator_safe=yes`.
  <!-- provenance: node/citation named in digital-creativity-pedagogy/grounding/README.md matrix row II.5 and re-confirmed live this session via `ahmes query --cite <db>:<node_id> --require-evaluator-safe --style chicago-author-date`; node text read directly from fission_node.markdown_content, not from a vector/Athanor preview -->
- Rizzi, G. &amp; Bertola, P. (2025). *Exploring the generative AI potential in the fashion design process.* European Journal of Cultural Management and Policy, `10.3389/ejcmp.2025.13875`. Ahmes coat `167816a4`, node `908f5339-781d-51cc-a803-47dfbf9c0677`, p.9(→10). `(Rizzi 2025, 10)`. Resolved via `ahmes query --cite`, `evaluator_safe=yes`.
  <!-- provenance: node/citation named in digital-creativity-pedagogy/grounding/README.md matrix row II.5 and re-confirmed live this session via `ahmes query --cite <db>:<node_id> --require-evaluator-safe --style chicago-author-date`; node text read directly from fission_node.markdown_content -->
- **Missing evidence — declared, not papered over:** the field map holds an `[UNVERIFIED-GAP]` on **fashion-portfolio web UX** — no vault source establishes which layout, accessibility, or presentation patterns cause a portfolio to communicate better, get seen, or get hired. Everything in this unit's B1 template/layout guidance is professional craft advice, not research evidence. Do not cite it as if it were.
