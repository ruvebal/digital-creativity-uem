# Formula fidelity gate

Mathematical extraction has a higher burden than prose extraction. Preserve
three distinct representations:

1. **Page image:** visual source of truth for glyphs, layout, indices, radicals,
   limits, and equation numbering.
2. **Symbolic transcription:** human-checked LaTeX or MathML used by the
   renderer and tests.
3. **Search text:** normalized prose/tokens used for discovery only.

Never reconstruct representation 2 from representation 3 without comparing
it with representation 1.

## Audit protocol

For each selected equation:

- record source page, equation number if present, and a crop or page render;
- compare Ahmes `markdown_content` and `original_content` with the page;
- record upstream label and Ahmes `block_type` when available;
- check operators, relation signs, superscripts, subscripts, accents, set
  delimiters, limits, products/sums, roots, and line breaks independently;
- transcribe a canonical LaTeX form and have a second pass compare it against
  the rendered page;
- classify `EXACT`, `USABLE_WITH_REPAIR`, `DISCOVERY_ONLY`, or `MISSING`;
- never allow `DISCOVERY_ONLY` or `MISSING` formulae to drive production art.

## Current evidence and experiment

The existing Bosch *Opt Art* coat retains page-addressable prose but visibly
damages mathematical notation: membership signs, inequalities, subscripts,
exponents, and objective functions are flattened or corrupted. Ahmes's own
2026-08-16 structural-fidelity report records that Docling exposes a `formula`
label while the current adapter maps unhandled labels to `text`.

V. Drakopoulos, "Comparing Rendering Methods for Julia Sets" was the first
controlled specimen (seven pages, Type-3 fonts — the page render is clean
while ordinary PDF text extraction is largely glyph codes, a strong test of
layout/OCR recovery rather than an easy born-digital success). Four more
formulae have since cleared the full gate; see the table below for the
current state, not just the historical starting point.

Run the audit with the oracle and script in:

- `digital-creativity-pedagogy/grounding/fractal-architecture/formula-audit/`
- `scripts/fractal-architecture/audit-formula-fidelity.py`

The audit may recommend an Ahmes engineering request. It must not silently
patch extracted mathematics or inject a failed specimen into Athanor.

## Confirmed formulas (2026-09-02)

Every row cleared the full AFEL gate: `fidelity_status=EXACT`,
`derivation_role=CANONICAL`, and `graphic_status=HUMAN_CONFIRMED` — a human
read the source page, and a human separately confirmed the render matched
it, before the render-brief and pass-track release existed. This is 5 of
the 7 "Choose a grammar" families above; **packing/recursive solids** and
**DLA/stochastic growth** have no confirmed formula yet (a corpus scan for
Apollonian/circle-packing and DLA/percolation/Brownian content across the
11 unpromoted documents in
`digital-creativity-pedagogy/grounding/fractal-architecture/runs/20260830T-afel-fc1-candidates/`
found packing-*dimension* theory, not a packing *construction*, and no
closed-form DLA equation at all — DLA is fundamentally a stochastic
algorithm, which is a structural mismatch with AFEL's page-verified-LaTeX
evidence model, not yet a solved problem).

| Grammar family | Formula | Source | Generator |
|---|---|---|---|
| Escape-time / orbit trap | `p_c(z)=z²+c` | Drakopoulos 2002, p.1 | `generate-pass-track-backgrounds.mjs` |
| IFS / flame | `P = w₁(P) ∪ w₂(P) ∪ ⋯ ∪ wN(P)` (chaos game, right-triangle instance) | Barnsley et al. 1988, p.225 | `generate-pass-track-backgrounds-ifs.mjs` |
| L-system | `A(s) → F(s)[+A(s/R)][-A(s/R)]F(s)A(s/R)` | Prusinkiewicz & Lindenmayer 2004, p.187 | `generate-pass-track-backgrounds-lsystem.mjs` |
| Self-similar construction | `φ₁,φ₂,φ₃` (direct prefractal subdivision, equilateral instance) | Graduate Studies in Math. vol. 247, p.134 (Eq. 4.15) | `generate-pass-track-backgrounds-sierpinski-gasket.mjs` |
| Attractor / flow field | `H(x,y)=(y+1-ax²,bx)`, a=1.4, b=0.3 | Peitgen, Jürgens & Saupe 2004, p.610 (Eq. 12.1) | `generate-pass-track-backgrounds-henon.mjs` |

Each generator's own `LOOP_NOTE`/citation-gate machinery (or, for the first
three, the equivalent inline checks) refuses to run against a glossary
entry that isn't `EXACT`, and refuses to publish an entry that isn't
`derivation_role=CANONICAL` — see `render-brief.schema.json` in the Ahmes
repo for the formal contract these generators consume
(`schemas/render-brief.schema.json`, `ConsumerBriefPort`, AFEL §2).
`PHASE-12H.FC-FORMULA-EVIDENCE-LIFECYCLE.md` in that repo is the
authoritative source for what these statuses mean and how they're gated;
this table is a snapshot of what has cleared them, not a redefinition.

The IFS-family instance above (Barnsley, chaos game) and the self-similar
construction instance (the equilateral gasket) both converge to a
Sierpinski-triangle attractor but are deliberately rendered with different
techniques — chaos-game point-density vs. direct recursive polygon
subdivision — because the grammar taxonomy above is about rendering
technique, not the attractor's topology alone.

