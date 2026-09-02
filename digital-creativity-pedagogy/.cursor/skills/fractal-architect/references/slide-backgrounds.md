# How-to-pass slide backgrounds

The background should make the track feel navigable, demanding, and alive. It
must not compete with assessment information.

## Shared system

- Inherit each curriculum's existing palette; do not introduce a second brand.
- Generate from source with a stable seed and a per-slide parameter delta.
- Reserve a title-safe region with measurable contrast at desktop and mobile.
- Prefer complete recursive structures at the focal edge. Cropping may happen
  responsively, but no crop may create an accidental pseudo-symbol behind text.
- Use regular/medium typography only. Backgrounds contain no lesson titles,
  institutional rules, formula labels, or provenance metadata.
- Supply a static SVG/PNG fallback. If motion is later added, stop it under
  `prefers-reduced-motion` and keep comprehension independent of animation.

## First experimental suite

Use one family per section so the deck reads as a journey:

1. recursive polyhedral lattice — track structure;
2. orbit-trapped Julia boundary — thresholds and pass conditions;
3. L-system branching — routes, recovery, and iteration;
4. IFS density field — accumulated practice;
5. attractor or flow field — feedback and revision;
6. Apollonian/packing closure — portfolio coherence.

The DC decks use the UEM palette and logo only. The FE decks use the UDIT
palette and logo only. Preserve the existing dark-only site decision.

## Acceptance

- text contrast passes WCAG AA in the real slide markup;
- no body copy intersects the high-density focal region at tested breakpoints;
- the deck has a working back-to-track control;
- source, SVG, and PNG regenerate deterministically;
- generated HTML contains real media elements, never escaped figure markup;
- publication gates find no internal research-system metadata.

