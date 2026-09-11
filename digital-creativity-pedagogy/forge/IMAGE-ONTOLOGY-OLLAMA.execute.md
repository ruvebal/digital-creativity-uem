---
description: Local Ollama execution phase for the I.0 image-ontology lecture and student slideshow
globs: 'digital-creativity-pedagogy/forge/**'
alwaysApply: false
---

# I.0 OLLAMA EXECUTION — qwen3.8:27b

Run after loading the official CD I guide, the existing lesson/session
contracts, the grounding receipt, and the Media Prospector request.

```bash
OLLAMA_MODEL=qwen3.8:27b
```

Draft the professor lecture, an 8–12 slide student deck, ontology-card
exercises, and structured media slots. Each student slide must contain exactly:

```yaml
slide_id: stable-id
heading: one short heading
sentence: one sentence only
visual_focus: one image, accepted media group, or accessible diagram
observation_prompt: one question
media_slot_id: required unless course-generated graphic
```

Use accepted Profield media only. Until the MP5 pack exists, emit a reviewed
slot specification and accessible placeholder—not an invented image URL.
Backgrounds use one theme surface, with no stacked transparency, text collision,
or repeated graph.

The model must not resolve rights, fabricate bibliography, publish vector
previews, or expose Athanor/Ahmes/Profield internals. If the model is absent,
stop with `BLOCKED_MODEL_UNAVAILABLE`; do not substitute another model.

Accept the draft only after verifying official contents, 30/30/30/30 timing,
evaluator-safe citations or internal `[BIBLIO-GAP]`, accepted MP5 slots, and
publication/citation/media/readability gates.
