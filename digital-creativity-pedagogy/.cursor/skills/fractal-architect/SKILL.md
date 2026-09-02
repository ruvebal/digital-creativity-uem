---
name: fractal-architect
metadata:
  version: "1.2.1"
description: Design reproducible, formula-governed fractal and recursive visual systems for curriculum backgrounds and code art. Use when a visual-forger task needs verified mathematics, seeded variation, recursive geometry, or a formula-fidelity audit; do not use it to ingest a bibliography or to present decorative complexity as mathematical evidence.
---

# Fractal architect

Work as the mathematical studio inside `visual-forger`, not as a replacement
for it. The caller owns the curriculum claim, palette, typography, export, and
publication checks. This skill owns the recursive system and its evidence.

## Contract

1. Name the communicative job before choosing a fractal family.
2. Keep a verified symbolic layer separate from the visual layer. A formula
   may govern an artwork without appearing in it.
3. Record the seed, parameters, viewport, iteration budget, and stopping rule
   in inspectable source.
4. Use mathematics as structure, not as prestige decoration. A beautiful
   result is neither a proof nor evidence that extraction was correct.
5. Keep title-safe negative space and test at the actual crop and breakpoint.
6. In student output, expose no local corpus names, node identifiers,
   extraction paths, resolver states, or internal grounding labels.
7. Emit content-addressed SVG/PNG filenames, preserve prior releases, and
   publish a release index; never overwrite image bytes at an existing path.
8. Return a publication-safe semantic caption brief and a separate private
   provenance receipt containing skill/agent versions and hashes.
9. Ship `figcaption-data` as JSON for each delivery release. Each figure
   record must include UUID, SHA-256, title, description, authorship, ISO date,
   delivery SVG/PNG paths, and one record per governing formula. A formula
   record includes display text, LaTeX, basic explanation, and an
   evaluator-safe Chicago citation. Never put extraction/node/crop data in the
   public manifest.
10. Keep the native generated SVG/PNG in a content-addressed source release,
    then copy those exact bytes into the delivery directory. The source
    release, delivery copy, public release index, and private receipt must be
    independently traceable.
11. Local Ollama semantic indexing may index the public-safe caption record;
    it is retrieval metadata only and may never produce or validate a formula,
    citation, or caption claim.

## Choose a grammar

- **Self-similar construction:** substitution tilings, Sierpinski families,
  recursive polygons. Best for hierarchy and progression.
- **IFS / flame:** weighted affine or nonlinear transforms with density
  accumulation. Best for emergence, plurality, and atmospheric depth.
- **Escape-time / orbit trap:** Julia or Mandelbrot iteration with a geometric
  distance measure. Best for thresholds, boundaries, and feedback.
- **L-system:** rewriting plus turtle interpretation. Best for growth,
  branching, and curricular pathways.
- **Attractor / flow field:** deterministic trajectory rendered as density or
  line. Best for iteration, convergence, and productive instability.
- **Packing / recursive solids:** Apollonian circles, polyhedral projections,
  nested complete figures. Best for modular systems and spatial rhythm.
- **DLA / stochastic growth:** seeded accretion with explicit bounds. Best for
  networks and organic formation; never imply that randomness is unseeded.

Combine at most two primary grammars in one background. Glitch and noise are
surface operators, not substitutes for composition.

## Evidence route

For extraction or provenance work, read
[`references/formula-fidelity.md`](references/formula-fidelity.md). For
`how-to-pass-this-track` work, also read
[`references/slide-backgrounds.md`](references/slide-backgrounds.md).
For public caption data, source/delivery separation, or cold development work,
also read [`references/caption-manifests.md`](references/caption-manifests.md).
For a multi-phase skill or pipeline change, begin at
[`cascade/IGNITOR.md`](cascade/IGNITOR.md).

The attached reading-list brief is a hypothesis map. Verify books, papers,
formulae, and technique claims at source-page level before promoting them.
Vector search discovers candidates; only a checked page and citation resolver
can ground prose. A formula additionally requires visual transcription checks.

## Handoff to visual-forger

Return a compact render brief containing:

- subject and audience;
- selected grammar and why it carries the claim;
- verified formula or an explicit `geometry_only` status;
- palette tokens inherited from the host;
- seed and parameter envelope;
- title-safe region and crop behavior;
- motion/reduced-motion behavior when applicable;
- source, SVG, PNG, and HTML verification requirements.

Do not render or ingest merely because the skill was invoked. Respect the
caller's requested stage: plan, audit, prototype, or production.
