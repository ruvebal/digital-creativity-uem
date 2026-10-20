# Dignity cascade — review packet

Completed for local review: 2026-10-20. Branch: `codex/dignity-cascade`.
Public-site implementation is prepared and previewed locally; it has not
been committed, pushed or deployed. TC implementation is a later stage.

## Delivered

- English guide: `docs/dignity/index.md`, route `/dignity/`.
- Spanish companion: `docs/dignity/es/index.md`, route `/dignity/es/`.
- Six source-grounded concepts, five distinct supplemental cases, two
  portfolio labs and eight shorter classroom activities.
- Integration links in eight relevant image/media lesson pages and the
  shared master-lecture index; locale-aware main navigation link.
- Thirteen bibliography entries in the shared references registry, complete
  source-gated provenance and an explicit limitations/AI declaration footer.
- Five guide-owned cases reserved in the campaign index. Existing U1–U3
  allocations preserved. The validator now protects guide reservations and
  treats English/Spanish mirrors as one teaching owner.
- Publication/citation checks extended to the new guide route and to an
  explicit isolated build destination.

## Cascade completion

| Phase | Result |
| --- | --- |
| D0 | Five original PDFs inventoried and hashed; 64 pages; documentary instructions distinguished from the user's request |
| D1 | Five successful Ahmes extractions; 772 nodes; 275 semantic annotations across 314 eligible text nodes; NER and bibliography passes completed |
| D2 | Dry run followed by authorized native Athanor injection: 5/5 originals, no failures. Nine supplementary/scoped source snapshots also ingested; isolated project contains 14 documents |
| D3a | Ideas Profield run: 12 claims, 9 confirmed, 2 disputed, 1 unverifiable; no unmatched verdicts |
| D3b | Images Profield run: 10 claims, 7 confirmed, 3 disputed; no unmatched verdicts. Twenty-one broad provider candidates unaccepted; primary case documentation used instead |
| D4 | Eleven planned neural/scoped searches succeeded; additional post-ingestion native and cross-project queries completed; source pages and citations checked separately |
| D5 | Thirteen retained public source works; four undated original documents retain explicit bibliography gaps; rejected/noisy records documented |
| D6 | English/Spanish guide, two labs, eight optional activities, source matrix, research synthesis and teacher activity packet prepared |
| D7 | Jekyll build, publication safety, citation conformance, campaign uniqueness and whitespace checks pass; both guide pages have 13 references, one H1 and no missing internal targets/anchors |
| D8 | TC transfer questions and entry gates prepared in `TC-HANDOFF.md`; no TC curriculum files changed |

The original corpus is also in the shared derived semantic store: 5 vaults,
5 successful ingest operations, no failures. This makes it discoverable
alongside existing vaults. The native project's final query returns the GD16
textile exercise with the corrected document title and a source-node pointer.

## Bibliographic integrity

The automatic coat initially produced no safe author-year citations for the
five supplied documents. The 2026 date printed on the practice-bank cover and
the repeated corporate footer support a verified correction for that source.
The other four lack a verified publication year; PDF creation timestamps,
event dates and historical dates were not substituted. They remain readable
and searchable, but do not receive fabricated ordinary author-date citations.

`CORPUS-BIBLIOGRAPHY.md` and `dignity-corpus.ris` preserve those outcomes.
`bibliographic-corrections.json` retains old values and verification bases.

The recovered Freire record had the publisher as author and a cover slogan
as title. Its own title/copyright pages support the corrected Paulo Freire /
2000 anniversary-edition attribution. The hooks record and an anthology
chapter attribution were not promoted. No library-wide repair is claimed.

Native injection is idempotent and skips completed documents, even after
metadata corrections. Consequently, this cascade used the existing document
upsert adapter to refresh **only** its isolated project's metadata. Before
states are in `index-metadata-refresh.json`; no nodes/embeddings were removed
or rewritten. The final native query confirms the corrected bank title.

## Research integrity and remaining limits

- The two Profield strands were launched before synthesis, using public
  keywords. Their native digests, manifests, pass artefacts and vocabulary
  outputs are retained. Mapping and adversarial checking were done by the
  same agent: no independent second model or human review is claimed.
- Profield's digest status and its native OA queue are not the Ahmes citation
  gate. Some documentary URLs remain in the engine's OA queue even though
  the source has been read and its snapshot acquired separately; the actual
  acquisition and citation status are recorded explicitly in this packet.
- Four local draft attempts were rejected. Six accepted paragraph drafts
  were extensively edited; raw output, checks, revisions and six-axis notes
  remain in the native tuning-memory records. Automatic marker/citation
  checks did not establish factual fidelity or readable sentence structure.
- Final direct citation checks passed for five English source sentences.
  The English GD16 paraphrase triggered low overlap against its Spanish
  source; its reviewed Spanish sentence passed. The original diagnostic flag
  and direct bilingual source review are both preserved. No threshold was
  lowered to manufacture a pass.
- No classroom-effectiveness evaluation, affected-participant consultation,
  systematic-review completeness or media rights clearance is claimed.
- The official GUCCI video is related media, not an authenticated copy of
  the adjudicated end-frame. No viewing timecodes or unavailable original
  campaign URLs were invented.
- The 2026-27 live PDFs for CD I, CD II and NM were read alongside their guía
  JSONs. This is a supplementary method guide: no official hours, evaluation
  weights or competencies were changed.

## Build and visual review

The isolated Jekyll output is `/private/tmp/dignity-course-site`. The existing
post-build hook targets `_site` directly, so its two citation/reference
processors were also run against the isolated output before the gates.
That avoids claiming a raw alternative-destination build is fully processed.

Concurrent edits elsewhere in the shared checkout were preserved. An interim
scan caught volume-lesson metadata while that work was in progress; those
sources were already corrected when inspected, and a fresh build passed the
full privacy scan. This cascade did not overwrite the volume lessons.

The browser preview confirmed readable whole-word table cards at the default
narrow viewport. A duplicate body title was removed; each locale now has one
H1. Structure and internal-link checks are in
`guide-structure-validation.json`; gate results are in `validation.json`.

Local preview: `http://127.0.0.1:4178/digital-creativity-uem/dignity/`.
The preview server is local-only and remains running for review.

## Read these first

1. `RESEARCH-SYNTHESIS.md` — arguments, tensions and transfer boundaries.
2. `ACTIVITY-PROPOSALS.md` — full teacher instructions and feedback questions.
3. `EVIDENCE-MATRIX.md` — retained sources, exclusions, gaps and vault coverage.
4. `CORPUS-BIBLIOGRAPHY.md` — all five originals and the unknown-date outcomes.
5. `TC-HANDOFF.md` — next curriculum stage, without premature implementation.
6. `MASTER-CASCADE.md` — plan registered before the pipeline.

Detailed machine receipts: `inventory.json`, `corpus-final-audit.json`,
`evidence-nodes.json`, `primary-sources.json`, `SCRIBE-PERFORMANCE.json`,
`final-citation-fidelity.json`, `gd16-bilingual-fidelity.json`,
`vault-search/receipts.json`, and the two `profield/` run trees.
