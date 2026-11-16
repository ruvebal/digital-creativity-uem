---
layout: lesson
title: 'Master Lecture · Seeing volume'
title_es: 'Master Lecture · Ver el volumen'
slug: volume-depth-perception
date: 2026-11-16
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/master-lectures/volume-depth-perception/
description: 'Lecture A of three. Volume on a flat image is built by the viewer: the inverse problem, three ways to explain depth perception, seven pictorial cues and what none of them can prove about a garment.'
status: pilot
tags: [master-lecture, volume-depth, perception, creativity, series-vd]
deck_url: /master-lectures/volume-depth-perception/
series: volume-depth
series_part: 1
master_idea: 'Volume on a flat picture is built by the viewer: a cue is evidence about the picture, never proof about the body.'
practice_anchor: 'Cue audit on one garment photo + one fold lit from above and from below'
frontier_signal: 'Machines solve the same inverse problem in depth estimation — Lecture C asks what they know and what they only imitate'
references: [boden-2004]
---

<!-- prettier-ignore-start -->

## Table of contents
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
unit_id: ML-VD-A
series: Volume perception and depth (ML-VD-A · B · C); enrichment after slim I.5, never a CONTENIDOS row; official volume behaviour stays in I.6
forge: digital-creativity-pedagogy/forge/VOLUME-DEPTH-SERIES-PLAN.md · DEV_PLAN/VOLUME-DEPTH-SERIES/
spine: digital-creativity-pedagogy/grounding/lesson-corpus/I.5-I.6-depth-perception-perspective-research.md (unpublished)
forged: 2026-11-16 polish pass (creativity studies + human–machine thread)
page_basis: printed page read from the source PDF; resolver scheme=pdf_order is not the printed page (Boden printed = pdf_seq − 15)
PROVENANCE_LINE: claim=ML-VD-A.perception-grounds-perspective; status=VERIFIED; page_basis=printed; source={coat=c2f1c705; node=1587e9f9-13b8-54f7-917a-27f838af872b; pdf_seq=38; printed=23; continues node 07ec8bba-5130-53ac-a228-ec2114b3cffd printed=22}; public="(Boden 2004, 22–23)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-A.creativity-definition; status=VERIFIED; page_basis=printed; source={coat=c2f1c705; node=4e5cd4a2-388b-5b2a-af71-bd0dfeeed477; pdf_seq=16; printed=1}; public="(Boden 2004, 1)"; evaluator_safe=yes
PROVENANCE_LINE: claim=ML-VD-A.p-creativity; status=VERIFIED; page_basis=printed; source={coat=c2f1c705; node=658073bf-cc4d-52af-9088-8e698c942f3a; pdf_seq=17; printed=2}; public="(Boden 2004, 2)"; evaluator_safe=yes
ORIENTATION (named, not cited — no course-library node yet): Helmholtz, Handbuch der physiologischen Optik (1856–67); Gibson and Walk, "The visual cliff" (1960); Gibson, The Ecological Approach to Visual Perception (1979); Marr, Vision (1982); Ames room (1946); Arnheim via temario T1-B.
MEDIA: all backgrounds bound in docs/tracks/en/uem/2627-ml/volume-depth-perception/data/content.json; rights in excellence/curation/autopilot-assets.json (final review pending).
-->
{% endif %}

{% include lesson-semantic-graphic.html %}

<div class="lesson-opener" markdown="1">

> **There is no volume on a flat picture. There is a viewer who builds it — and a garment the picture can never fully prove.**

**In-class slideshow:** [open deck]({{ '/master-lectures/volume-depth-perception/' | relative_url }})

**Series · Volume perception and depth:** **A · Seeing volume** → [B · Constructing space]({{ '/lessons/en/master-lectures/volume-depth-construction/' | relative_url }}) → [C · Digital and AI depth]({{ '/lessons/en/master-lectures/volume-depth-digital/' | relative_url }})

This is a **Master Lecture**: an enrichment session after [I.5 Three-dimensional form]({{ '/lessons/en/digital-creativity-i/i-5-three-dimensional-form/' | relative_url }}). It gives you the vocabulary of depth perception. It does **not** replace [I.6 Volume]({{ '/lessons/en/digital-creativity-i/i-6-volume/' | relative_url }}), where you test how a real garment behaves.

</div>

## Session at a glance (120′)

| Time | Block | What you do |
| --- | --- | --- |
| 0–15′ | Analysis | Read one 1877 painting for depth, then ask what it cannot say about fit |
| 15–55′ | Masterclass | Five ideas: paradox · inverse problem · three frames · cue ledger · creativity |
| 55–105′ | Lab (portfolio) | Exercise 1 cue audit · Exercise 2 flip the light |
| 105–120′ | Share | Two students show one cue that lied |

## Learning objectives

By the end of this lecture you can:

1. Explain why **one flat image fits many three-dimensional scenes** (the inverse problem).
2. Compare **three ways of explaining depth perception** — inference, pick-up, computation — and turn each into a studio test.
3. Name **seven pictorial depth cues** and say, for each, what it **cannot prove** about a garment.
4. Describe an image as **creative** when it changes what a viewer infers, using Margaret Boden's definition.

---

## Analysis · one painting (15′)

<figure class="lesson-figure" id="figure-caillebotte" markdown="0">
<img src="{{ '/assets/images/deck-media/2c784043003df3d0.webp' | relative_url }}" alt="Caillebotte’s 1877 painting of a Paris street in the rain: fashionable walkers under umbrellas, paving stones shrinking toward the distance." loading="lazy" decoding="async">
<figcaption>Gustave Caillebotte, <em>Paris Street; Rainy Day</em>, 1877. Art Institute of Chicago. Public domain · <a href="https://commons.wikimedia.org/wiki/File:Gustave_Caillebotte_-_Paris_Street;_Rainy_Day_-_Google_Art_Project.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

Work in pairs with the first three steps of the [fashion image analysis card]({{ '/lessons/en/master-lectures/fashion-image-analysis/' | relative_url }}):

- **Describe.** Umbrellas, top hats, a long coat, wet paving stones. Say what is near and what is far.
- **Cues.** Which clues tell you? Look at the shrinking stones, the overlapping bodies, the size of the distant walkers.
- **Critical.** The couple's clothes look solid and heavy. What does the painting **not** tell you about how those clothes fit?

Keep your answers. They return in the cue ledger.

---

## Masterclass · five ideas (40′)

### 1 · The paradox: one outline, many volumes

The retina — the light-sensitive layer at the back of the eye — receives a flat projection of light. Yet we experience a world of solid things at different distances. Every image-making tradition, from fresco to the 3-D render, works inside that gap.

<figure class="lesson-figure" id="figure-kawakubo" markdown="0">
<img src="{{ '/assets/images/deck-media/a7fe225309618a85.webp' | relative_url }}" alt="Black Comme des Garçons pieces on stands in a white gallery: silhouettes that hide where the body ends and padding begins." loading="lazy" decoding="async">
<figcaption>Rei Kawakubo / Comme des Garçons, in <em>Art of the In-Between</em>, The Metropolitan Museum of Art, 2017. Photograph: Sarah Stierch · CC BY 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Dresses_by_Rei_Kawakubo_-_Sarah_Stierch_01.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

Fashion makes the paradox visible. Rei Kawakubo builds garments that do not follow the outline of the body. From one view the eye cannot tell padding from body: the silhouette alone does not decide the volume. **A second view, or movement, is the cheapest way to settle it.**

### 2 · Seeing solves an inverse problem

Vision scientists call this an **inverse problem**: many different scenes can send the same image to the eye, so the picture underdetermines the world. Seeing depth means choosing one scene among many — and the choice can be wrong.

<figure class="lesson-figure" id="figure-inverse" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-a-inverse-problem-81f96c33dbac.svg' | relative_url }}" width="1600" height="900" alt="Course diagram: an eye looks through a flat picture plane; a small near card, a tilted plank and a large far card all fill the same two rays and cast the same red image, so the picture alone cannot say which world is there." loading="lazy" decoding="async">
<figcaption><strong>One picture, many worlds.</strong> Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-ames" markdown="0">
<img src="{{ '/assets/images/deck-media/fcc3b86fe739b009.webp' | relative_url }}" alt="Diagram of an Ames room: a trapezoidal room seen through a peephole looks rectangular, so two people at different distances appear giant and tiny." loading="lazy" decoding="async">
<figcaption>The Ames room, first built by Adelbert Ames Jr. in 1946: the eye prefers “square room” to “equal people”. Diagram: Alex Valavanis · public domain · <a href="https://commons.wikimedia.org/wiki/File:Ames_room.svg">Wikimedia Commons</a>.</figcaption>
</figure>

**Studio consequence.** A single fashion photograph is one answer to an inverse problem. Before you claim anything about volume, ask which other garments could have produced the same picture.

### 3 · Three frames: inference, pick-up, computation

Three classic explanations give three different studio tests. Treat them as frames for making, not as exam dogma.

| Frame | Claim in one line | Studio test |
| --- | --- | --- |
| **Inference** — Hermann von Helmholtz, 1860s | The brain makes a fast, unconscious best guess from experience | Move the light: does a fold flip from hollow to bump? |
| **Pick-up** — James J. Gibson, 1979 | A moving viewer finds depth already in the light: texture, flow, horizon | Walk around the garment: what changes, what stays? |
| **Computation** — David Marr, 1982 | Seeing builds stages: image → sketch → “2½-D sketch” → 3-D model | Name the stage your software is really working at |

<figure class="lesson-figure" id="figure-crater" markdown="0">
<img src="{{ '/assets/images/deck-media/bdef7ce13fec1e61.webp' | relative_url }}" alt="Two lunar orbiter photographs of the same crater; rotated 180 degrees, the hollow crater reads as a raised dome." loading="lazy" decoding="async">
<figcaption>The crater illusion: the same crater, rotated. The eye bets that light comes from above. NASA / GSFC / Arizona State University · public domain · <a href="https://commons.wikimedia.org/wiki/File:Crater_illusion.jpg">Wikimedia Commons</a>.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-cliff" markdown="0">
<img src="{{ '/assets/images/deck-media/b9f4e3d6aa856453.webp' | relative_url }}" alt="Infant on a glass visual cliff apparatus used in Gibson and Walk depth-perception research." loading="lazy" decoding="async">
<figcaption>The visual cliff, tested by Eleanor Gibson and Richard Walk in 1960: most babies would not crawl over the apparent drop. NIH / Nature Publishing Group · CC BY 4.0 · cropped · <a href="https://commons.wikimedia.org/wiki/File:NIH_visual_cliff_experiment_(cropped).png">Wikimedia Commons</a>.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-frames" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-a-three-frames-d0881c358931.svg' | relative_url }}" width="1600" height="900" alt="Course diagram in three columns: Helmholtz 1867, inference, test by moving the light; Gibson 1979, pick-up, test by walking around the garment; Marr 1982, computation from image to sketch to 2½-D sketch to 3-D model, test by naming the stage your software works at." loading="lazy" decoding="async">
<figcaption><strong>Three ways to explain seeing depth.</strong> Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

Marr's middle stage, the **2½-D sketch** — depth for each visible point, seen from one place — returns in [Lecture C]({{ '/lessons/en/master-lectures/volume-depth-digital/' | relative_url }}): it is close to what a depth sensor or a depth-estimation network produces.

### 4 · The cue ledger

A flat image cannot use the cues that need two eyes (binocular disparity) or a moving head. It can use **pictorial** cues:

<figure class="lesson-figure" id="figure-depth-cues" markdown="0">
<img src="{{ '/assets/images/deck-media/60a50b4472b6540e.webp' | relative_url }}" alt="Diagram plate of pictorial depth cues including occlusion, relative size and perspective." loading="lazy" decoding="async">
<figcaption>Pictorial depth cues. Diagram: Brazzit · CC BY-SA 3.0 · <a href="https://commons.wikimedia.org/wiki/File:Depth_cues_1.png">Wikimedia Commons</a>.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-cue-ledger" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/vd-a-cue-ledger-0c9502289438.svg' | relative_url }}" width="1600" height="900" alt="Course diagram: a table of seven depth cues, each with what it can show and, in red, what it cannot prove about a garment." loading="lazy" decoding="async">
<figcaption><strong>What a cue proves — and what it cannot.</strong> Course diagram · Rubén Vega Balbás · CC BY-NC-SA 4.0. The same table, as text:</figcaption>
</figure>

| Cue | It can show… | It cannot prove… |
| --- | --- | --- |
| Occlusion | which layer is in front | how much ease lies underneath |
| Relative size | nearer or farther, if sizes are known | the wearer's real measurements |
| Linear perspective | where the camera stood | whether a seam hangs straight on the body |
| Texture gradient | how a surface tilts away | whether the fabric will stretch |
| Aerial perspective | that something is far away | anything indoors, under studio light |
| Shading and shadow | which way a fold curves | the fold's weight or drape |
| Motion parallax | depth order as the camera moves | how the garment itself moves |

**Rule of the ledger:** a cue is evidence about the **picture**. Fit, drape and stretch need another test — the one you run in I.6.

### 5 · Creativity begins in perception

Why does this matter for creative work and not only for vision science? The cognitive scientist Margaret Boden defines creativity as the ability to come up with ideas or artefacts that are “new, surprising and valuable” [(Boden 2004, 1)](#ref-boden-2004). She separates **P-creativity**, an idea new to the person who has it, from **H-creativity**, an idea new to history [(Boden 2004, 2)](#ref-boden-2004). Most studio learning is P-creative — and that is exactly what this course assesses.

Boden then makes a claim that joins this lecture to art history. Renaissance perspective and the “deformations” of Cubism, she argues, are both grounded in

> the set of psychological processes that make it possible for the mind to interpret two-dimensional images as depicting three-dimensional scenes

<p class="quote-ref" markdown="1">— [(Boden 2004, 23)](#ref-boden-2004)</p>

<figure class="lesson-figure" id="figure-venetian" markdown="0">
<img src="{{ '/assets/images/deck-media/52de9862187535a4.webp' | relative_url }}" alt="Black-and-white 1912 book plate of a crowded Venetian Adoration of the Magi: figures in rich garments stacked up the picture rather than receding to one vanishing point." loading="lazy" decoding="async">
<figcaption>A Venetian <em>Adoration of the Magi</em>, reproduced in <em>The Venetian School of Painting</em> (1912): depth by stacking, before one measured box. Internet Archive Book Images · public domain · <a href="https://commons.wikimedia.org/wiki/File:The_Venetian_School_of_Painting_(1912)_(14597540617).jpg">Wikimedia Commons</a>.</figcaption>
</figure>

**So an image is creative in depth when it changes what a viewer infers** — not when it adds more detail. A pictorial revolution works on the viewer's inference machinery. Your fashion image can do the same on a small scale: a crop that hides the second view, a light that inverts a fold, a pose that makes a silhouette ambiguous on purpose.

**Human–machine note.** Software faces the same inverse problem. A depth sensor *measures* distance; a depth-estimation network *guesses* it from one photo, the way Helmholtz's viewer does — from experience, in its case training images. Lecture C asks what such machines know and what they only imitate.

---

## Lab (portfolio) · 50′

Two exercises with your phone and one garment. Everything you make goes to your portfolio index on Canvas with a short note.

> **Consent and care.** Photograph a classmate only if they say yes, and show them the result. A garment on a hanger or a chair is enough. Never upload a classmate's image to any AI tool. Student work is authorial property: nothing is exhibited without a separate permission.

### Exercise 1 · Cue audit (25′)

1. Photograph one garment **from the front**, plain background, side light.
2. On the photo (any markup app), mark **three depth cues** from the ledger.
3. Next to each mark, write one line: *cue · what it shows · what it cannot prove about fit.*
4. Add the **second view** that would answer one of your “cannot prove” lines — and shoot it.

**Example line:** *Shading · the front pleat curves inward · not whether the pleat will open when the wearer walks.*

### Exercise 2 · Flip the light (25′)

1. Dark corner. Pleated, quilted or gathered fabric works best.
2. Light the folds with a phone torch **from above** at about 45°. Shoot.
3. Light the same folds **from below**. Shoot.
4. Rotate the second photo 180° on screen. Find the frame where a **hollow reads as a bump**.

This is Helmholtz's “unconscious inference” caught in the act: your eye bets that light comes from above.

**Portfolio entry:** the marked photo + second view (Ex 1) and the two light frames (Ex 2), with one sentence: *which bet did my eye make, and which view would correct it?* Today needs no AI; if you used any tool that generates content, declare it following the [course AI declaration]({{ '/ai-declaration/' | relative_url }}).

---

## Recall check

1. Why can one flat image fit many three-dimensional scenes?
2. What did Helmholtz call seeing?
3. What did babies do at the visual cliff?
4. Name three pictorial depth cues.
5. Which depth cue can prove how a garment fits? *(Careful.)*

## Conclusion

Volume in a picture is **built by the viewer**, using cues that are evidence about the picture and never proof about the body. [Lecture B]({{ '/lessons/en/master-lectures/volume-depth-construction/' | relative_url }}) asks who wrote the rules of that picture — and whose eye perspective assumes. Bring your cue audit to [I.6 Volume]({{ '/lessons/en/digital-creativity-i/i-6-volume/' | relative_url }}): it tells you which test to run on the real garment.

## Media credits

Every image caption names the creator, licence and source page. Backgrounds and figures are public domain or openly licensed (CC BY 4.0, CC BY-SA 3.0). Diagrams are course-made (CC BY-NC-SA 4.0).

## References

{% include references.html %}

## Editorial note · Work in progress · Teaching Innovation Practice
{: .lesson-editorial-note }

Boden's definitions and her perspective–Cubism claim are page-verified against the printed second edition. Helmholtz, Gibson and Walk, Gibson and Marr are named with their dates as **orientation**: their own texts are not yet in the course library, so they are not quoted. There is still no published study on teaching light-on-form as volume evidence in fashion higher education; the cue ledger is a studio literacy tool, not an evidence-based claim.

## AI-assisted authorship

Drafted with AI assistance under the author's editorial control. [Full disclosure]({{ '/ai-declaration/' | relative_url }}).
