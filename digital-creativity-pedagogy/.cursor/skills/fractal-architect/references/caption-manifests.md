# Caption manifests and release delivery

## Public contract

Deliver one immutable `figcaption-data` JSON document per release and a
current pointer. Each figure must carry a stable UUID, `fractal_hash256`,
title, description, authorship email, ISO creation date, SVG/PNG delivery
paths, and a formula array. Formula records contain display text, canonical
LaTex, a short plain-language explanation, and an evaluator-safe Chicago
author-date citation. Public documents must never expose local source-system
names, node IDs, crop hashes, resolver diagnostics, or local paths.

## Private contract

The private receipt binds each public formula UUID to the source-page evidence,
formula fidelity result, source and delivery filesystem paths, generator and
skill hashes, plus the local semantic-index receipt. Private paths are never
copied into a client manifest.

## Delivery rule

Generate the native SVG and its PNG derivative into a content-addressed source
release first. Copy those bytes into the client delivery directory. Existing
content-addressed filenames are immutable; indexes append releases and merely
move their current pointer.

## Cold cascade

Use a fresh planning session for each phase: contract; provenance and render;
client and semantic index. Each phase prompt must name its allowed artefacts,
inputs, invariants, and blocking gates. An Ollama embedding can make release
records discoverable, but only page-checked source evidence can approve a
formula or citation.
