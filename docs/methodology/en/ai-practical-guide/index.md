---
layout: methodology
title: 'AI Practical Guide: The Book of the Woven Prompt'
title_es: 'Guía práctica de IA: El libro del prompt tejido'
slug: ai-practical-guide
date: 2026-08-31
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /methodology/en/ai-practical-guide/
description: 'A wisdom-book for fashion and digital creativity: use AI with intention, question its mirrors, and make authorship visible.'
tags: [ai, methodology, ethics, fashion, authorship, digital-creativity]
---

## 📜 Table of Contents
{: .no_toc }

- TOC
{:toc}

<div class="ai-guide">

<figure class="ai-guide__hero" markdown="0">
<img src="/digital-creativity-uem/assets/images/ai-guide/book-of-the-woven-prompt-cv-index-20260831-v2.png" width="1600" height="900" alt="A red thread crosses the geometric visual field of the Digital Creativity index, passing through a needle, a reflective circle, a fashion pattern, and a lantern-like machine." fetchpriority="high" />
<figcaption>The main course index becomes a poster field: the thread crosses intention, suggestion, reflection, and judgement.</figcaption>
</figure>

<p class="ai-guide__kicker">A small book for large questions · Digital Creativity · UEM</p>

<div class="ai-guide__orientation">
<p><strong>For:</strong> students making images, garments, avatars, moving images, digital experiences, or portfolios with AI nearby.</p>
<p><strong>Not for:</strong> legal advice, a promise that a model is neutral, or a substitute for learning the craft you submit.</p>
<p><strong>Purpose:</strong> use AI to extend a human intention, then leave enough of the thread visible that another person can understand, question, and trust the work.</p>
</div>

<blockquote class="ai-guide__ttod">
  <p>“The honest AI engineer does not lie to herself about her tools. She knows what they can and cannot do, and she designs her workflow to amplify their strengths.”</p>
  <cite>— The Tao of Development, <code>arch-037</code></cite>
</blockquote>

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROVENANCE_LINE: claim=guide.instructions.tested-comprehension; status=[BIBLIO-GAP]; discovery={service=studio-guide-forge; source=CPSC Manufacturer's Guide to Developing Consumer Product Instructions; proposed_use=audience-match-and-evaluate-the-instructions}; source={document_coat=studio-guides; extraction_db=ahmes-library/studio_guides/documents/manufacturers_guide_to_developing_consumer_product_instructions_cb1f154e/extract/extraction.db; node_id=82b3b541-0cf2-5f0a-adb9-7470db8f8a71; page_index=null}; resolver=surface-B-only; public_citation=OMITTED; supports=write-for-reader-and-test-comprehension; does_not_support=fashion-AI pedagogy
-->
{% endif %}

---

## Prologue · How to read this book

The proverbs are short because a tool can make a long answer before you have made a clear question. Read one, pause, and do the small act beneath it. The act is the lesson.

The studio default is local assistance through Ollama and the locally installed `qwen3.8:27b` model when the task genuinely benefits from AI. Models change; the covenant does not: keep the work local when required, declare the assistance, and question every result.

### The two turns

1. **The asking turn:** write your intention, constraints, references, and what you want the model to vary.
2. **The judging turn:** compare the result with your intention, reject defaults, remake what matters, and record what changed.

If the second turn is absent, the machine has not assisted your practice; it has replaced the part you were meant to learn.

---

## I · The hand before the prompt

<blockquote class="ai-guide__aphorism"><p>The hand that names the question remains the first author of the journey.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Before you ask for an image, say what the image must make someone feel, notice, or understand.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>A vague intention invites a beautiful stranger; a situated intention invites a useful collaborator.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the first stitch</strong></p>
<ol>
  <li>Write the brief in your own words.</li>
  <li>Name the audience, the material, and the decision that must remain yours.</li>
  <li>Only then write the prompt; keep the first version beside the result.</li>
</ol>
</div>

---

## II · The thread of intention

<blockquote class="ai-guide__aphorism"><p>A prompt is not a spell; it is a thread tied between intention and experiment.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Ask for alternatives, not permission to stop thinking.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>The first output is a proposition. The second look is where authorship begins.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the three variations</strong></p>
<ol>
  <li>Ask for three materially different directions, not three near-identical decorations.</li>
  <li>For each, write one sentence: <em>what does this reveal, and what does it hide?</em></li>
  <li>Keep the discarded path when it teaches you something about your own taste.</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>The student asked, “Which image is mine?”</p>
  <p>The teacher answered, “Show me the one you refused.”</p>
  <cite>Koan of the discarded image</cite>
</blockquote>

---

## III · The mirror that shows only some

<blockquote class="ai-guide__aphorism"><p>Every generated body is also a lesson about the bodies the system did not imagine.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>A smooth default is still a decision; ask who made it, who benefits, and who disappears.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Do not call an image inclusive because it contains difference; ask whether difference has agency.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the four questions</strong></p>
<ol>
  <li>Who is represented?</li>
  <li>Who is missing or made impossible?</li>
  <li>Which visual habits does the result repeat?</li>
  <li>What will you change, contextualise, or refuse?</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>A mirror showed the student a perfect model.</p>
  <p>“Perfect for whom?” asked the teacher.</p>
  <p>The mirror became a question.</p>
  <cite>Koan of the polished surface</cite>
</blockquote>

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROVENANCE_LINE: claim=guide.fashion-ai-ethics; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query=fashion AI human authorship identity cultural ethics; source_locator=grounding matrix II.5 and C1 fashion digital world; proposed_use=critical framing only}; source={document_coat=anwar_raza_marzouk_0598ec0e; extraction_db=ahmes-library/scholar/documents/anwar_raza_marzouk_generative_ai_in_studio_based_fashion_education_slr_ejbm_2025_0598ec0e/extract/extraction.db; node_id=c9a17328-72f7-56c8-95bf-b9860b1067b8; page_index=0}; resolver=ahmes query --cite extraction.db:c9a17328-72f7-56c8-95bf-b9860b1067b8 --style chicago-author-date; quote=knowledge construction, learner identity and authorship, teaching practice, studio culture and ethics; public_citation=(Anwar, Raza, and Marzouk 2025, 1); supports=ethical and authorship dimensions belong in studio AI instruction; does_not_support=universal image-bias measurement or a validated portfolio UX method
PROVENANCE_LINE: claim=guide.critical-mediated-world; status=[BIBLIO-GAP]; discovery={service=Athanor; project_slug=profield-stem-code-ai-epistemology-critique; knowledge_scope=field_prospection; query=digital mediated world ethics AI representation agency; proposed_use=question prompts only}; source={document_coat=multiple critical-AI candidates; node_id=none}; resolver=not promoted; public_citation=OMITTED; supports=critical questions about representation, expertise, and accountability; does_not_support=settled fashion-specific pedagogy
PROVENANCE_LINE: claim=guide.ethical-authorship; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query=fashion AI human authorship identity cultural ethics}; source={document_coat=anwar_raza_marzouk_0598ec0e; extraction_db=ahmes-library/scholar/documents/anwar_raza_marzouk_generative_ai_in_studio_based_fashion_education_slr_ejbm_2025_0598ec0e/extract/extraction.db; node_id=cd329fc8-be24-5335-ad0d-4fe91dd97693; page_index=8}; resolver=ahmes query --cite extraction.db:cd329fc8-be24-5335-ad0d-4fe91dd97693 --style chicago-author-date; public_citation=(Anwar, Raza, and Marzouk 2025, 9); supports=ethical authorship, copyright, ownership, hybrid authorship, and preserving student voice; does_not_support=legal advice or a universal rights determination
-->
{% endif %}

---

## IV · The ledger of authorship

<blockquote class="ai-guide__aphorism"><p>If the machine supplied a possibility, your ledger must still name the choice.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Ownership is not a feeling of familiarity; it is the ability to explain the decisive moves.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Hide the process and polish becomes a mask; show the process and critique can become a tool.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the visible ledger</strong></p>
<p>For every AI-assisted artefact, record:</p>
<ul>
  <li><strong>Tool:</strong> the local model or interface used.</li>
  <li><strong>Contribution:</strong> what it suggested, transformed, organised, or generated.</li>
  <li><strong>Human verification:</strong> what you checked, changed, rejected, and can defend.</li>
</ul>
</div>

<p>Fashion-education research places learner identity, authorship, and studio culture alongside knowledge construction and teaching practice; its proposed teaching direction includes explicit work on ethical authorship, copyright, ownership, and hybrid authorship (Anwar, Raza, and Marzouk 2025, 1, 9). This is why the declaration belongs beside the work, not in a hidden footnote.</p>

---

## V · The small local fire

<blockquote class="ai-guide__aphorism"><p>A local model is nearer to your studio, not nearer to truth.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Keep sensitive material outside the prompt; privacy is part of the composition.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>When the answer sounds certain, make your checking more patient.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the lantern</strong></p>
<ol>
  <li>Prepare a small, clean input; remove names, faces, secrets, and material you cannot share.</li>
  <li>Ask the model for a bounded task: variations, questions, a critique, or a transformation.</li>
  <li>Inspect the output against the brief and against the world it claims to depict.</li>
  <li>Save the prompt, the useful result, and the human edit that made it yours.</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>“The model has given me the answer,” said the student.</p>
  <p>“Good,” said the teacher. “Now ask it what would make the answer wrong.”</p>
  <cite>Koan of the second question</cite>
</blockquote>

<p class="ai-guide__note"><strong>Remember:</strong> AI assistance may accelerate a search or widen a sketch, but it cannot perform your observation, your ethical judgement, or your responsibility for the final image.</p>

<p>The studio literature describes both expanded ideation and efficiency and tensions around originality, ethical use, and equitable access; the wise workflow therefore keeps the tool bounded and the judgement visible (Anwar, Raza, and Marzouk 2025, 10).</p>

---

## VI · The portfolio as witness

<blockquote class="ai-guide__aphorism"><p>A portfolio is not a room where finished things pose; it is a path another person can walk.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Place the brief, the turn, the failure, and the decision beside the polished surface.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>The best case study does not say “look what the tool made”; it says “see why I chose this.”</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite of the four witnesses</strong></p>
<ol>
  <li><strong>Intent:</strong> what question or brief began the piece?</li>
  <li><strong>Trace:</strong> which references, prompts, files, and iterations shaped it?</li>
  <li><strong>Judgement:</strong> which alternatives were refused, and why?</li>
  <li><strong>Declaration:</strong> where did AI assist, and where did human authorship remain decisive?</li>
</ol>
</div>

<p>An experimental fashion-design laboratory describes human–AI work as a collaboration whose dynamics must be analysed through the design process, not inferred from the final output alone (Rizzi and Bertola 2025, 10). Your portfolio makes that process readable.</p>

---

## VII · The gate of care

<blockquote class="ai-guide__aphorism"><p>Do not borrow a face, a body, a garment, or a story merely because a machine made borrowing easy.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Ask consent before circulation; ask attribution before display.</p><cite>Proverb</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>An accessible image carries its meaning beyond the eye that first imagined it.</p><cite>Proverb</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rite before release</strong></p>
<ul>
  <li>Use self-authored, licensed, or clearly permitted material.</li>
  <li>Do not generate or publish an identifiable person’s likeness without permission.</li>
  <li>Give images purposeful alt text; label decorative images as decorative.</li>
  <li>Credit references, collaborators, and source materials.</li>
  <li>Keep a before/after or process trail when transformation changes meaning.</li>
  <li>Do not collect or exhibit someone else’s work without the required consent process.</li>
</ul>
</div>

---

## Epilogue · The declaration at the door

Write this beside the finished work, in plain language:

> **AI-use declaration**
>
> **Tool:** [local tool/model]
>
> **Contribution:** [what the tool suggested, generated, transformed, or organised]
>
> **Human decisions:** [what I selected, changed, rejected, verified, and take responsibility for]

<blockquote class="ai-guide__ttod">
  <p>“Use images to enhance the message, not to be the message. Words remain when images fail.”</p>
  <cite>— The Tao of Development, <code>img-053</code></cite>
</blockquote>

The same is true of AI: let it enhance the practice, not become the practice. If you can show the thread, name the choices, and defend the care taken, the work has a human centre.

<p class="ai-guide__signature"><em>Forged for the Digital Creativity studio · Edition 2026-08-31 · Human-authored, locally assisted, openly declared.</em></p>

## References

- Anwar, Rabia, Fahd Ali Raza, and Mostafa El-Sayed Marzouk. 2025. “Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.” <em>Electronic Journal of Business and Management</em> 10 (4): 17–28. <a href="https://doi.org/10.65136/ejbm.v10i4.24">https://doi.org/10.65136/ejbm.v10i4.24</a>.
- Rizzi, Greta, and Paola Bertola. 2025. “Exploring the Generative AI Potential in the Fashion Design Process: An Experimental Experience on the Collaboration between Fashion Design Practitioners and Generative AI Tools.” <em>European Journal of Cultural Management and Policy</em> 15: 13875. <a href="https://doi.org/10.3389/ejcmp.2025.13875">https://doi.org/10.3389/ejcmp.2025.13875</a>.

</div>

<style>
.ai-guide { --ink: #172033; --muted: #5d6674; --paper: #f8f4eb; --gold: #b88746; --red: #a83d2d; --night: #0b1622; max-width: 980px; margin: 0 auto; }
.ai-guide__hero { margin: 0 0 2rem; background: var(--night); border: 1px solid rgba(184, 135, 70, .45); box-shadow: 0 18px 50px rgba(11, 22, 34, .18); }
.ai-guide__hero img { display: block; width: 100%; height: auto; }
.ai-guide__hero figcaption { margin: 0; padding: .8rem 1rem 1rem; color: #e8dcc6; font: 500 .88rem/1.45 Georgia, serif; }
.ai-guide__kicker { color: var(--red); font: 700 .75rem/1.2 ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .14em; text-transform: uppercase; }
.ai-guide__orientation { padding: 1rem 1.2rem; border: 1px solid rgba(184, 135, 70, .55); background: linear-gradient(120deg, rgba(184, 135, 70, .1), rgba(168, 61, 45, .06)); }
.ai-guide__orientation p { margin: .35rem 0; }
.ai-guide__ttod, .ai-guide__koan { border-left: 4px solid var(--gold); padding: 1rem 1.2rem; background: rgba(184, 135, 70, .08); }
.ai-guide__ttod p, .ai-guide__koan p { margin: .2rem 0; }
.ai-guide__ttod cite, .ai-guide__koan cite { display: block; margin-top: .7rem; color: var(--muted); font-size: .82rem; }
.ai-guide__aphorism { margin: 1.7rem 0; padding: 1rem 1.2rem; border-left: 2px solid var(--red); background: rgba(168, 61, 45, .055); }
.ai-guide__aphorism p { margin: 0; color: var(--ink); font: 600 clamp(1.15rem, 2.2vw, 1.5rem)/1.35 Georgia, serif; }
.ai-guide__aphorism cite { display: block; margin-top: .45rem; color: var(--muted); font-size: .78rem; font-style: normal; text-transform: uppercase; letter-spacing: .08em; }
.ai-guide__rite { margin: 1.5rem 0 2rem; padding: 1rem 1.25rem; border: 1px solid rgba(23, 32, 51, .2); background: rgba(23, 32, 51, .04); }
.ai-guide__rite p:first-child { margin-top: 0; color: var(--red); }
.ai-guide__rite p:last-child, .ai-guide__rite ol:last-child, .ai-guide__rite ul:last-child { margin-bottom: 0; }
.ai-guide__note { padding: 1rem 1.2rem; background: #fff4d8; border: 1px solid #e5c27c; }
.ai-guide__signature { margin: 2rem 0 0; color: var(--muted); font-size: .9rem; }
@media (prefers-color-scheme: dark) {
  .ai-guide__orientation, .ai-guide__aphorism, .ai-guide__rite { color: #e7e1d7; }
  .ai-guide__aphorism p { color: #f4ead9; }
  .ai-guide__rite { border-color: rgba(232, 220, 198, .25); background: rgba(232, 220, 198, .06); }
  .ai-guide__note { color: #3b2d14; }
}
</style>
