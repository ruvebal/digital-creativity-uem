---
layout: lesson
title: 'Master Lecture · Digital and AI depth'
title_es: 'Master Lecture · Profundidad digital e IA'
slug: volume-depth-digital
date: 2026-11-16
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/master-lectures/volume-depth-digital/
description: 'Lecture C of three. Alberti’s window as a formula, painted order versus tested depth, AI images as learned plausibility, and a declared human–machine studio loop — then back to I.6 behaviour.'
status: pilot
tags: [master-lecture, volume-depth, projection, 2.5d, ai, human-machine, creativity, series-vd]
deck_url: /master-lectures/volume-depth-digital/
series: volume-depth
series_part: 3
master_idea: 'Volume on a screen is a claim made by an engine: name the engine, keep the judgement human, test the real garment.'
practice_anchor: 'Classify three images by engine + one declared human–machine collaboration with a local tool'
frontier_signal: 'Image generators imitate depth without a scene; fashion instructors find them useful for ideas, not for construction'
references: [vince-2017, boden-2004, an-park-2026, bendel-2025]
---

<!-- prettier-ignore-start -->

## Table of contents
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
unit_id: ML-VD-C
series: Volume perception and depth (ML-VD-A · B · C); sister craft = FE SVG / Canvas 2.5D master session (painter-order projection, no Z-buffer)
forged: 2026-11-16 polish pass (human–machine collaboration thread)
hard rule: no cloud AI in teaching materials — Lab 2 is local/offline only, or no tool
page_basis: printed pages. Vince printed = pdf_seq − 13; Bendel printed = pdf_seq + 436 (AI & Society 40:437–446); An and Park = article page (Page n of 22) = pdf_seq; Boden printed = pdf_seq − 15
PROVENANCE_LINE: claim=ML-VD-C.perspective-projection; status=VERIFIED; page_basis=printed; source={coat=9f6b4c20; node=0874eb09-97c7-5cdd-9841-77b7b2c5a5cc; pdf_seq=217; printed=204; divide-by-w node 55241666-725f-5e10-91c1-7e3e5125ea5b printed=205}; public="(Vince 2017, 204)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-C.ai-images-not-construction; status=VERIFIED; page_basis=article page; source={coat=c4236068; node=2b8cb50e-4765-5808-badf-dfc55ef6b8d9; pdf_seq=15; printed=15}; speaker=instructor P9; public="(An and Park 2026, 15)"; evaluator_safe=yes; resolver prints "(An 2026, …)" — second author restored
PROVENANCE_LINE: claim=ML-VD-C.process-assessment; status=VERIFIED; page_basis=article page; source={coat=c4236068; node=bc55c433-cf8c-52b8-86f2-e38b69f951a8; printed=14}; public="(An and Park 2026, 14)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-C.dependence-warning; status=VERIFIED; page_basis=article page; source={coat=c4236068; node=eac9c52d-9d13-5f23-9f0d-ac6330ebf811; printed=14}; public="(An and Park 2026, 14)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-C.watermarks; status=VERIFIED; page_basis=printed; source={coat=71d6c25f; node=8120b38b-979f-5799-9d3c-00a468e3cd3c; pdf_seq=4; printed=440}; public="(Bendel 2025, 440)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-C.evaluation-bottleneck; status=VERIFIED; page_basis=printed; source={coat=c2f1c705; node=0c034f5e-4d9d-5969-8451-c43df0cf5029; pdf_seq=335; printed=320}; public="(Boden 2004, 320)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-C.lovelace-questions; status=VERIFIED; page_basis=printed; source={coat=c2f1c705; node=ebfc2222-7261-5c58-910c-950f7e1380c6; pdf_seq=31; printed=16}; public="(Boden 2004, 16)"; evaluator_safe=yes
[BIBLIO-GAP] Jang 2026, "From designer to curator" (Fashion and Textiles 13:12) nodes f0420073, 8b002239, 51a28f46 — metadata gap, not cited publicly; strong fashion-HE fit (designer → curator shift). Repair RIS to promote.
[BIBLIO-GAP] Kim 2024 (IEEE Access, collaborative ideation with fashion students) and Fu et al. 2024 (arXiv 2411.00168) — not cited publicly.
[BIBLIO-GAP] Van Hulle 2019 (IJDH, "Artificial imagination, imagine") — evaluator_safe=no (0.70); DH frame "artificial imagination as imitatio" kept for a later pass.
-->
{% endif %}

{% include lesson-semantic-graphic.html %}

<div class="lesson-opener" markdown="1">

> **Every camera projects. Only some machines know the scene. And none of them decides what counts as a good volume — you do.**

**In-class slideshow:** [open deck]({{ '/master-lectures/volume-depth-digital/' | relative_url }})

**Series · Volume perception and depth:** [A · Seeing volume]({{ '/lessons/en/master-lectures/volume-depth-perception/' | relative_url }}) → [B · Constructing space]({{ '/lessons/en/master-lectures/volume-depth-construction/' | relative_url }}) → **C · Digital and AI depth**

Lecture A: the viewer builds volume. Lecture B: someone wrote the rule. Lecture C: the rule becomes software — and some software imitates the rule without having it. The lecture ends with a **human–machine studio loop** you can declare in your portfolio. Fit and drape still belong to [I.6 Volume]({{ '/lessons/en/digital-creativity-i/i-6-volume/' | relative_url }}).

</div>

## Session at a glance (120′)

| Time | Block | What you do |
| --- | --- | --- |
| 0–15′ | Analysis | Read a perfect 3-D render: every cue, and no cloth |
| 15–55′ | Masterclass | Six ideas: ratio · tested depth · plausibility · images not patterns · human judgement · whose data |
| 55–105′ | Lab (portfolio) | Exercise 1 name the engine · Exercise 2 a declared collaboration |
| 105–120′ | Share | Two students show one machine proposal they rejected, and why |

## Learning objectives

By the end of this lecture you can:

1. Explain perspective projection as **division by depth** and link it to Alberti's window.
2. Distinguish **2.5-D painter's order**, **depth-tested 3-D** and **AI learned plausibility** — and say what each one guarantees.
3. Use Boden's idea of the **evaluation bottleneck** to place judgement on the human side of a collaboration.
4. Run and **declare** a human–machine loop with a local tool, keeping prompt, settings, rejects and reasons.
5. Name one ethical question about the **images that trained** a generator.

---

## Analysis · one render (15′)

<figure class="lesson-figure" id="figure-cube" markdown="0">
<img src="{{ '/assets/images/deck-media/c9c84626ccfb914a.webp' | relative_url }}" alt="A computer-rendered hollow white cube standing on a blue and green checkered floor, with soft shading and cast shadows." loading="lazy" decoding="async">
<figcaption>A computer-rendered test scene. Render: Dominicos · CC BY-SA 3.0 · <a href="https://commons.wikimedia.org/wiki/File:Cubic_Structure.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

- **Describe.** List the cues from Lecture A: cast shadow, shading, the shrinking squares, occlusion.
- **Engine.** Photograph, 3-D render or AI image? What in the picture decides — and what would not?
- **Critical.** It is a 3-D render. Perfect cues prove the software works. What would they prove about a garment made of real cloth?

---

## Masterclass · six ideas (40′)

### 1 · Alberti's window becomes a ratio

<figure class="lesson-figure" id="figure-kircher" markdown="0">
<img src="{{ '/assets/images/deck-media/615df243ed4970ea.webp' | relative_url }}" alt="Kircher’s 1646 engraving of a portable camera obscura: a person inside a box traces the inverted image projected through small openings." loading="lazy" decoding="async">
<figcaption>Athanasius Kircher, portable camera obscura, in <em>Ars Magna Lucis et Umbrae</em>, 1646. Public domain · <a href="https://commons.wikimedia.org/wiki/File:1646_Athanasius_Kircher_-_Camera_obscura.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

The camera obscura, the photographic camera and the virtual camera of a 3-D program all do what Alberti's window does: they cut the rays from a scene with a plane. In software, the cut is a formula. The computer-graphics textbook by John Vince opens its section plainly:

> Of all the projections employed in computer graphics, the perspective projection is one most widely used.

<p class="quote-ref" markdown="1">— [(Vince 2017, 204)](#ref-vince-2017)</p>

<figure class="lesson-figure" id="figure-projection" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-c-projection-xz-32f6c73dbf40.svg' | relative_url }}" width="1600" height="900" alt="Course diagram: a camera, a picture plane at distance d, and the same garment at depth z and 2z; the farther image is half as tall. Formula: x prime equals d times x divided by z." loading="lazy" decoding="async">
<figcaption><strong>Alberti's window, written as a ratio:</strong> x′ = d · x / z. Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

Divide by depth, and farther things shrink: twice as far, half as big. Vince's construction converts world coordinates to the camera's frame and then projects them onto the screen [(Vince 2017, 204)](#ref-vince-2017). **Orthographic** views — the flat front, side and back views of a pattern or a CLO window — do **not** divide by depth. That is why they measure well and look less “real”.

<figure class="lesson-figure" id="figure-projections" markdown="0">
<img src="{{ '/assets/images/deck-media/187d0facfadeb354.webp' | relative_url }}" alt="Chart comparing graphical projections of the same house: multiview, axonometric, oblique and perspective." loading="lazy" decoding="async">
<figcaption>One object, many projection rules. Chart: Cmglee · CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Comparison_of_graphical_projections.svg">Wikimedia Commons</a>.</figcaption>
</figure>

### 2 · Painted order or tested depth?

On screen, “in front of” can be decided in two very different ways:

- **2.5-D (painter's order).** Flat layers are sorted back to front and drawn once — the parallax hero of many portfolio sites. If two shapes cross each other, one of them must lie.
- **Depth-tested 3-D (Z-buffer).** The engine keeps a depth value for every pixel and tests each new surface against it, every frame. Crossing shapes stay honest — as honest as the model and its light.

<figure class="lesson-figure" id="figure-zbuffer" markdown="0">
<img src="{{ '/assets/images/deck-media/10ea743f3ea99e0f.webp' | relative_url }}" alt="Diagram of a Z-buffer: a simple 3D scene and its depth image, where nearer surfaces are brighter." loading="lazy" decoding="async">
<figcaption>A scene and its Z-buffer (depth image). Diagram: -Zeus- · CC BY-SA 3.0 · <a href="https://commons.wikimedia.org/wiki/File:Z_buffer.svg">Wikimedia Commons</a>.</figcaption>
</figure>

A depth image is close to Marr's **2½-D sketch** from Lecture A: depth for each visible point, seen from one place. **Photogrammetry** and 3-D scanning go one step further and *measure* a surface by matching many photographs — but shiny, black or sheer fabrics often scan badly, because the machine needs visible texture to match points.

<figure class="lesson-figure" id="figure-engine" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-c-engine-honesty-3e067f094649.svg' | relative_url }}" width="1600" height="900" alt="Course diagram in three columns: 2.5-D layers in painter’s order; 3-D depth-tested with a Z-buffer; AI image of learned plausibility — each with what it guarantees and how it can lie." loading="lazy" decoding="async">
<figcaption><strong>Before you praise the depth, name the engine.</strong> Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

### 3 · Plausible is not the same as possible

<figure class="lesson-figure" id="figure-piranesi" markdown="0">
<img src="{{ '/assets/images/deck-media/c1af268770cfe9e9.webp' | relative_url }}" alt="Piranesi’s etching The Drawbridge from the Imaginary Prisons: vast stairways and bridges that look convincing but cannot all connect." loading="lazy" decoding="async">
<figcaption>Giovanni Battista Piranesi, <em>The Drawbridge</em>, from <em>Carceri d'invenzione</em>, first edition, about 1750. Public domain · <a href="https://commons.wikimedia.org/wiki/File:Giovanni_Battista_Piranesi_-_Le_Carceri_d%27Invenzione_-_First_Edition_-_1750_-_07_-_The_Drawbridge.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

Piranesi's imaginary prisons look convincing, yet their stairs and bridges cannot all connect. Image generators produce depth in a comparable way: there is no scene and no camera, only patterns of cues **learned from training images**. The research question for this decade:

> **Has the machine learned perspective — or only what perspective looks like?**

**Plausibility check for any AI garment image:** Do shadows agree on one light? Does a seam continue across a fold? What holds the volume up — a body, a structure, or nothing?

### 4 · AI gives images, not patterns

A 2026 interview study with ten fashion design instructors found AI tools useful for brainstorming and concept visualisation, but not for making. One instructor put it this way:

> they just give you images; they don't actually support garment construction

<p class="quote-ref" markdown="1">— [(An and Park 2026, 15)](#ref-an-park-2026)</p>

<figure class="lesson-figure" id="figure-delphos" markdown="0">
<img src="{{ '/assets/images/deck-media/d3a43bbac02a702a.webp' | relative_url }}" alt="A pink Fortuny Delphos dress from the 1920s, finely pleated silk falling in a column." loading="lazy" decoding="async">
<figcaption>Mariano Fortuny, <em>Delphos</em> dress, 1920s. Photograph: Mabalu · CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Pink_Delphos_dress_by_Fortuny,_1920s.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

The same instructors warned that excessive dependence on AI may weaken independent reasoning, and asked for **process-oriented** assessment that looks at how AI tools are used to expand and refine ideas rather than counting outputs [(An and Park 2026, 14)](#ref-an-park-2026). That is how this course assesses Lab 2.

### 5 · The tool explores; you judge

Margaret Boden asked four **Lovelace questions** — after Ada Lovelace's remark that the Analytical Engine could not originate anything. The first is “whether computational ideas can help us understand how human creativity is possible” [(Boden 2004, 16)](#ref-boden-2004); the others ask whether computers could appear creative, appear to recognise creativity, or really be creative.

Her answer for design today: a program can **explore** a well-defined space very well. Changing the rules is harder, because a new rule breaks the very criteria that would tell the program its result is good:

> This example illustrates the evaluation bottleneck that lies in the way of automated transformational creativity.

<p class="quote-ref" markdown="1">— [(Boden 2004, 320)](#ref-boden-2004)</p>

<figure class="lesson-figure" id="figure-kawakubo-2" markdown="0">
<img src="{{ '/assets/images/deck-media/8243faeb5945da08.webp' | relative_url }}" alt="Comme des Garçons pieces displayed in the 2017 exhibition at the Metropolitan Museum of Art: sculptural volumes that break the rules of silhouette." loading="lazy" decoding="async">
<figcaption>Rei Kawakubo / Comme des Garçons, in <em>Art of the In-Between</em>, The Metropolitan Museum of Art, 2017. Photograph: Sarah Stierch · CC BY 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Dresses_by_Rei_Kawakubo_-_Sarah_Stierch_02.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

So in a human–machine collaboration the decisive moves stay human: **intention, constraints, judgement and signature**. The machine proposes inside its learned space; you decide what counts as a good volume — and you say so.

<figure class="lesson-figure" id="figure-loop" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-c-human-machine-loop-5dc1c097cea8.svg' | relative_url }}" width="1600" height="900" alt="Course diagram: a loop of intention, constraints, machine proposal, human judgement, revision and declaration; human decisions in red, the machine move in blue; centre note, trace kept: prompt, seed, rejects, reasons." loading="lazy" decoding="async">
<figcaption><strong>Who decides what counts as volume?</strong> The Lab 2 protocol. Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

**Why a loop and not a button.** In digital humanities and creativity studies alike, the interesting object is not the output but the **process** that produced it — the drafts, the rejects, the reasons. Keeping that trace makes your authorship visible and assessable.

### 6 · Whose pictures taught the machine?

Image generators learn from millions of pictures made by people who were rarely asked. In his ethical review of DALL-E 2, Stable Diffusion and Midjourney, Oliver Bendel notes that “it was repeatedly noticed that images bore watermarks and fonts” — traces of protected image platforms inside the outputs [(Bendel 2025, 440)](#ref-bendel-2025).

<figure class="lesson-figure" id="figure-catalogue" markdown="0">
<img src="{{ '/assets/images/deck-media/99969ed97ba1044d.webp' | relative_url }}" alt="An 1890 department-store fashion catalogue page of engraved garments by an anonymous commercial illustrator." loading="lazy" decoding="async">
<figcaption><em>Illustrated fashion catalogue, summer 1890</em> (Bloomingdale Bros.). Internet Archive Book Images · public domain · <a href="https://commons.wikimedia.org/wiki/File:Illustrated_fashion_catalogue_-_summer,_1890_(1890)_(14781648884).jpg">Wikimedia Commons</a>.</figcaption>
</figure>

This catalogue illustrator is anonymous and public domain today. **Who is credited, and who is paid, when a living illustrator's style is learned?** The course answer for your own work: local tools only in class, no classmate's image in any generator, and a full [AI declaration]({{ '/ai-declaration/' | relative_url }}).

---

## Lab (portfolio) · 50′

> **Rules for this Lab.** Local, offline tools only — a 3-D program (CLO, Blender) or an offline generator installed for the course — or no tool at all. Never put a classmate's image, or anyone's work without permission, into a generator. Credit every image you did not make.

### Exercise 1 · Name the engine (25′)

Choose three garment images: a **photograph**, a **3-D render** and an **AI image** (from your own work or credited sources). For each:

1. Label the engine: *projection (photo)* · *depth-tested (3-D)* · *learned plausibility (AI)*.
2. Name one depth cue that could be **lying**, using the [cue ledger]({{ '/lessons/en/master-lectures/volume-depth-perception/' | relative_url }}#4--the-cue-ledger).
3. Run the plausibility check on the AI image: one light? continuous seams? what holds the volume up?

### Exercise 2 · A declared collaboration (25′)

Follow the loop:

1. **Intention.** One sentence: what must this garment's volume do?
2. **Constraints.** Write your prompt or set your parameters; choose one reference photo of a real garment.
3. **Proposal.** Generate or render up to four views with the local tool.
4. **Judgement.** Reject at least one and say why, comparing with the real garment.
5. **Revision and declaration.** Change one thing, and write the declaration.

**Keep the trace:** prompt or settings · seed or file · rejects · reasons. Doing it by hand with no tool is valid — say why you chose that.

**Portfolio entry:** the three labelled images (Ex 1) and the pair real garment / machine proposal with your loop trace (Ex 2), plus an [AI declaration]({{ '/ai-declaration/' | relative_url }}): *what did the machine propose, and what did I decide?*

---

## Recall check

1. What does a virtual camera divide each point by?
2. How does 2.5-D decide what is in front?
3. What does a Z-buffer store for each pixel?
4. Why is an AI image plausible but not proven?
5. What did fashion instructors say AI tools cannot support?

## Conclusion

Volume on a screen is a **claim** made by an engine: projection, tested depth or learned plausibility. The series closes on one rule: name the engine, keep the judgement human, and **test the real garment** — in [I.6 Volume]({{ '/lessons/en/digital-creativity-i/i-6-volume/' | relative_url }}), behaviour, not appearance, decides fit.

## Media credits

Every image caption names the creator, licence and source page: public domain works and openly licensed files (CC BY 4.0, CC BY-SA 3.0 and 4.0). Diagrams are course-made (CC BY-NC-SA 4.0).

## References

{% include references.html %}

## Editorial note · Work in progress · Teaching Innovation Practice
{: .lesson-editorial-note }

Vince, An and Park, Bendel and Boden are page-verified. Two fashion-education studies on generative AI — one describing a shift “from designer to curator”, one on collaborative ideation with fashion students — and a digital-humanities essay on “artificial imagination” are held for the next pass and not yet cited. Marr's 2½-D sketch is named as orientation. The sister front-end lesson on SVG and Canvas 2.5-D gives the code side of painter's order.

## AI-assisted authorship

Drafted with AI assistance under the author's editorial control. [Full disclosure]({{ '/ai-declaration/' | relative_url }}).
