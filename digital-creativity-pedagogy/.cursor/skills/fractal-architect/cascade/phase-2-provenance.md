# Phase 2: Source And Provenance

Cold-session prompt:

> Implement or assess the generation core. It accepts verified formula and
> citation records through ports, writes native content-addressed SVG/PNG
> originals, copies byte-identical delivery assets, and appends a release index.
> The private receipt must bind the public formula UUID to page-level source
> evidence, formula fidelity, tool/skill hashes, and original/delivery paths.
> Fail closed on missing EXACT fidelity or evaluator-safe citation.

Dependencies: Phase 1.

Gate: rerunning one release does not mutate its immutable files or timestamp.
