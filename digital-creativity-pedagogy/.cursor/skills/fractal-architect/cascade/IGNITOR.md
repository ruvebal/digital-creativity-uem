# Fractal Architect Cold Cascade

This orchestrator is for changes that affect formula evidence, immutable
assets, caption data, client rendering, or semantic retrieval. Run every phase
in a fresh agent session. Each phase is allowed to inspect only the listed
inputs and produce only its listed output; a later phase cannot repair an
earlier failed gate.

1. [Phase 1: Contract](phase-1-contract.md)
2. [Phase 2: Source and provenance](phase-2-provenance.md)
3. [Phase 3: Delivery and client](phase-3-delivery.md)
4. [Phase 4: Release audit](phase-4-audit.md)

The orchestrator returns `DONE`, `PARTIAL`, or `BLOCKED` with phase evidence.
Local Ollama may contribute retrieval vectors only. It has no authority over
formula transcription, citation validity, or publication safety.
