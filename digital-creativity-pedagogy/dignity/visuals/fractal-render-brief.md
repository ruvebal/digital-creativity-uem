# Dignity background studio — release 2026-10-20.1

## Commission and division of work

The visual-forger studio owns composition, curriculum fit and delivery. Its fractal-architect specialist owns the bounded recursive construction and its traceability. This production release supplies atmospheric backgrounds for the Dignity guide. The six photographic situations are a separate image-generation pipeline and carry the ethical teaching scenarios.

These backgrounds are **geometry_only**. They use original recursive subdivision, with no claim that a named mathematical formula has passed the source-page citation gate. The public formula arrays are deliberately empty. The geometry neither illustrates a scientific finding about dignity nor establishes an ethical proposition.

## Relational folds — algorithmic philosophy

The DC composition develops as a family of folded bands. Each division preserves a shared direction while giving the resulting band its own curve and interval. The suggestive connection to cloth remains quiet: no garment, body or identity is reduced to a geometric emblem. The artwork supports an attentive reading environment rather than becoming an argument about its readers.

The recursion stops before it becomes visual noise. Five subdivisions produce thirty-two ribbons, and three fine accent trajectories give the field a wider rhythm. The design can be regenerated from its controls; no local decorative edits exist outside the source. Density sits to the right so that the upper-left remains useful for a future lema.

The TC companion makes a different operation visible. Two triangular regions subdivide along alternating edges, producing sixty-four facets. The triangles form a composed textile-like surface, not a named fractal, a cultural motif or a representation of a vulnerable population. The same title-safe composition relates the two sites while their distinct grammars retain their identities.

Color follows each host. DC draws from its blue and olive; TC uses flame and coral. The dark counterparts preserve hue and saturation through the studio lightness-inversion tool. Both are static, with no animation, noise texture or motion dependency. The intended craft is restraint: enough material presence to frame the cinematic scenes, enough silence to leave their questions open.

## Exact generation controls

- Source: `scripts/dignity-visuals/generate-backgrounds.py`, version 1.0.0.
- Seed: 20261020; TC uses seed + 100. DC geometry is deterministic without random draws; TC uses the seeded stream only for facet opacity and accent choice.
- Viewport: 2390 × 1000, exact 2.39:1; no letterbox bars.
- Depth: 5. Stop condition: depth equals 5; no unbounded process.
- DC: 32 folded bands plus 3 accent curves.
- TC: 2 initial triangular regions, 32 leaf facets each.
- Quiet area: upper-left 40% of width and upper 50% of height contains no foreground geometry. The ground retains a soft gradient.
- Motion: none; reduced-motion behavior is identical.
- Recommended title colors: DC light `#00295e`; both dark `#fff7ec`; TC light `#1a0f08`.
- Integration: use `width:100%; height:auto` or `aspect-ratio:239/100; object-fit:contain`; do not center-crop to a square. A narrow viewport may show the full artwork; the lema should remain HTML outside the raster and must not be shrunk to unreadable size.
- Because these are backgrounds, never place meaningful instructional wording in image bytes. When displayed as an artwork, use a real figure and its structured caption. A pure decorative background may have an empty image alternative; do not use CSS to simulate its visible authorship caption.

## Delivery and review

The current public release is selected by `docs/assets/images/dignity/backgrounds/index.json`. Its immutable caption manifest records public titles, palettes, dimensions, authorship, roles, descriptions, delivery paths and hashes. Its native SVG and PNG copies remain under the corresponding private content-addressed release directories, with byte-identical delivery copies.

All four PNG exports were visually inspected by the specialist agent at their full composition: no text, people, identities, slogans or unintended symbols appear; recursive detail stays on the right. Human review is **not** claimed. The proof receipt records the machine render and false human-review flag. Base color contrast readings are 12.89:1 for DC navy on its light paper and 19.11:1 for warm white on TC dark paper; these are token checks, not a blanket contrast claim over the entire gradient or an integrated page.

The source version and skill versions/hashes are bound in `fractal-proof-20261020-v1.json`. Do not hand-edit a hashed delivery asset. Change the generator, create a new content-addressed release and append it to the index.
