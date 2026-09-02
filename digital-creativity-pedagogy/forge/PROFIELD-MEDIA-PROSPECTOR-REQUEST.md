# Request to the Profield development team

**Target implementation:** `/Users/ruvebal/src/profield`
**Requesting repository:** `digital-creativity-uem`
**Consumer:** the instructor-facing session prompts in `digital-creativity-pedagogy/forge/session-prompts/`
**Priority:** teaching-pack infrastructure, read-only discovery first

## 1. Goal

Please implement a **Media Prospector** for Creación Digital I and II. Given a
course, unit, field, and subfield, it should discover legally reusable or
legally embeddable images, videos, diagrams, and graphics, then return a small
ranked media pack classified in two independent ways:

1. **Studio semantics:** what the asset is useful for in a 2-hour class
   (exemplar, counterexample, process demonstration, historical context,
   audience experience, object, interface graphic, or process trace).
2. **Licence conformance:** whether the repository may embed, download, crop,
   transform, remix, or publish the asset under the terms actually evidenced by
   the canonical source.

The tool must return evidence and uncertainty, not just a URL or a similarity
score. A search-result thumbnail, social preview, or inferred licence is never
enough for a conforming result.

## 2. Initial field/subfield vocabulary

Use this controlled vocabulary as the first taxonomy. It maps directly to the
official CONTENIDOS anchors; it does not replace them.

| Unit | Field | Subfield(s) |
| --- | --- | --- |
| I.1 | fashion image | image practices, circulation, editorial/commercial boundary |
| I.2 | digital drawing | 2D fashion sketching, vector/raster craft, line and path |
| I.3 | colour imaging | bitmap sampling, colour/display, contrast and accessibility |
| I.4 | image effects | compositing, masking, material and motion effects |
| I.5 | 3D form | 2D-to-3D representation, orthographic views, spatial visualization |
| I.6 | fashion volume | drape, fold, material, analogue/digital prototyping |
| I.7 | fashion design research | visual references, archives, composition, provenance |
| I.8 | animated image | keyframes, stop-motion, loops, fashion motion |
| I.9 | digital still life | fashion objects, light, material, scale, composition |
| II.1 | fashion retouching | non-destructive edit, appearance, material, disclosure |
| II.2 | avatar design | embodiment, identity fiction, pose, garment, authorship |
| II.3 | digital fashion experience | exhibition tour, object view, close-up, interaction |
| II.4 | fashion video | fashion film, branded content, storyboard, edit, export |
| II.5 | portfolio publishing | case study, responsive IA, accessibility, authorship |
| II.6 | fashion extended reality | AR layer, hologram-like display, trigger, audience response |

## 3. Studio-semantics classifier

Return one primary and up to two secondary labels from this enum:

```text
exemplar              a useful model to inspect against a stated criterion
counterexample        a visible failure or tension to diagnose, never ridicule
process_demonstration a sequence in which a decision or transformation is visible
historical_context    a dated artefact or practice used to establish context
audience_experience   an interaction/tour/display viewed from the audience side
object                 a garment, image, material, or artefact to observe closely
interface_graphic      IA, flow, layer stack, timeline, palette, or interaction map
process_trace          a student/professional record of revisions, credits, or export
```

Classification must include a short rationale tied to the requested subfield,
for example: `process_demonstration because the clip exposes the analogue →
digital handoff and the requested lesson is I.6 volume`. A visually attractive
asset with no teachable observation is not an exemplar by default.

## 4. Licence classifier

Do not use a language model to guess rights. Extract the rights statement from
the canonical provider page, preserve a quote or machine-readable field, and
record retrieval date. Return one of:

```text
conforming_public       public domain or CC0; repository use allowed as stated
conforming_attribution   CC BY / equivalent; credit line required
conforming_sharealike    CC BY-SA / equivalent; derivative terms must be preserved
embed_only               player/embed permitted, but download or local remix is not cleared
conditional               use needs a named action, permission, model release, or review
reject_unknown            missing, contradictory, or non-canonical rights evidence
reject_incompatible      terms conflict with repository/publication intent
```

Default repository preference is `conforming_public`, `conforming_attribution`,
or `conforming_sharealike`. `embed_only` may appear in an instructor brief but
must not be copied into local assets. `conditional`, `reject_unknown`, and
`reject_incompatible` are never emitted as ready-to-publish media.

The classifier must distinguish at least:

- asset licence versus platform terms;
- attribution requirement versus share-alike requirement;
- non-commercial or no-derivatives restrictions;
- model/property/privacy rights;
- permission to crop, subtitle, transcode, remix, or download;
- expiry, regional, or collection-specific restrictions.

## 5. Proposed result contract

Return a versioned JSON manifest; do not write directly into the teaching repo.
One record should resemble:

```json
{
  "asset_id": "stable-provider-id",
  "media_type": "video|image|graphic",
  "unit_id": "II.4",
  "field": "fashion video",
  "subfield": "fashion film, storyboard, edit, export",
  "studio_semantics": ["process_demonstration", "exemplar"],
  "semantic_rationale": "The clip exposes brief-to-edit decisions.",
  "canonical_source_url": "https://canonical.example/item",
  "asset_url": "https://canonical.example/file-or-player",
  "creator": "Verified creator or organization",
  "date": "2025 or null",
  "rights": {
    "class": "conforming_attribution",
    "spdx": "CC-BY-4.0",
    "source_statement": "Verbatim short rights statement",
    "retrieved_at": "2026-08-29",
    "actions": {"embed": true, "download": true, "crop": true, "remix": true},
    "credit_line": "Creator — title — source — licence"
  },
  "accessibility": {
    "captions": true,
    "transcript": true,
    "alt_text": "Required short description",
    "static_fallback": "Required for video/AR/animation"
  },
  "provenance": {"adapter": "provider-name", "source_hash": "optional"},
  "confidence": {"semantic": 0.0, "rights": 0.0},
  "review": {"status": "needs_human_review", "notes": []}
}
```

`source_hash` is an integrity aid, not an Ahmes or curriculum identifier. Do
not return local paths, private corpus IDs, or internal retrieval metadata to a
student-facing build.

## 6. Discovery and verification pipeline

1. Accept `course`, `unit_id`, `field`, `subfield`, `media_type`, desired
   semantics, language, duration, and licence actions.
2. Search only approved provider adapters and retain the provider’s canonical
   item page.
3. Canonicalize creator, title, date, asset URL, and rights statement.
4. Reject thumbnail-only and duplicate records before semantic ranking.
5. Classify studio semantics from the asset and its context; include rationale.
6. Resolve rights from the canonical rights page; never infer from filename,
   search rank, or “educational use” language.
7. Test accessibility fields and request a transcript/static fallback where
   missing.
8. Rank first by rights confidence and semantic fit, then by technical quality.
9. Mark every record `needs_human_review` until a teacher accepts the pack.
10. Export the manifest for review; only an explicit repo-side acceptance step
    may copy approved metadata into `docs/_data/` or a lesson.

## 7. Integration with these session prompts

Each guide requests one video, 2–3 still images, and one explanatory graphic.
The acceptance UI/CLI should let the instructor filter by:

```text
unit_id + studio_semantics + licence.class + media_type + duration + language
```

The selected pack must provide a credit block, transcript/alt text, static
fallback, and a “why this is here” sentence. The prompt author can then place
that block in the instructor guide or a gated lesson include.

Graphics generated by this course should be generated from the lesson’s
structured concept data and carry alt text; graphics sourced externally follow
the same rights classifier as images. No artwork may contain Ahmes, Athanor,
DevIAC, node IDs, extraction paths, or resolver states.

## 8. Safety and legal boundaries

- Crawl rate-limit and respect robots/provider terms; keep a provider audit log.
- Do not crawl behind authentication or bypass access controls.
- Do not retain faces, voices, student work, or personal data unless a separate
  approved workflow explicitly requires it.
- Do not treat “fair use,” “educational,” or “found online” as an automatic
  licence classification; escalate it to `conditional`.
- Preserve the original rights statement and retrieval date with every accepted
  record.
- No asset becomes a research stimulus or public exhibition object merely by
  being found; research and exhibition consent remain separate gates.

## 9. Acceptance tests

The implementation is ready for this repository when it can demonstrate:

1. a query for `II.4 / fashion video / process_demonstration` returning at least
   one legal candidate and one rejected/uncertain candidate with reasons;
2. a thumbnail-only result rejected before export;
3. a CC BY image returning a complete credit line and crop permission;
4. an embed-only video blocked from download/remix export;
5. contradictory rights metadata downgraded to `reject_unknown`;
6. an asset with no transcript/static fallback flagged for accessibility review;
7. the same asset deduplicated across two unit queries;
8. a manifest export containing no local paths, private corpus IDs, or student data;
9. a human acceptance step required before repo integration;
10. a reproducible provider audit record with retrieval date and adapter version.

Please return the proposed schema/API and a small fixture manifest before wiring
this into the public Jekyll build.
