# I.3 · Colour and Bitmap Images
## Lesson development prompt for instructors — 120 minutes

> **Central question:** When colour changes, has the design changed, the display changed, or both?

```yaml
course: CD I
unit_id: I.3
official_contents: "Color, imágenes con mapas de bits"
competencies: [CON1, HAB9, COMP8, COMP9]
session_length: 120 minutes
evidence_state: VERIFIED Roivainen platform styles + AlDahoul critical homogenization; [BIBLIO-GAP] Albers; NONE for colour-management pedagogy
registry_slice: "clases 1 · seminarios 2 · debates 1 · talleres 1 · proyectos 2 · problemas 1"
```

## Context & learning goals

Make students see a bitmap as sampled colour information that is interpreted by
devices and viewers. They will compare colour spaces at a conceptual level,
build a small palette with contrast checks, explain a visible mismatch, and
retain a colour decision in the process record.

## Session A: Sample, interpret, compare (2 hours)

| Time | Teacher move |
| --- | --- |
| 00–10 | Show one palette on two displays; ask whether the “same” colour is the same design. |
| 10–30 | Mini-lecture: pixels, resolution, bit depth, colour space/profile, display and export assumptions. |
| 30–45 | Screen a colour-management or bitmap-process video; students note each conversion and its risk. |
| 45–55 | Contrast audit of two fashion palettes: legibility, hierarchy, and mood. |
| 55–65 | Demonstrate sampling, naming, contrast checking, and a non-destructive adjustment layer. |
| 65–100 | Studio sprint: build a five-colour fashion palette with one accessible alternate and a bitmap crop. |
| 100–113 | Individual B3, no AI: diagnose a described colour mismatch and name the first check. |
| 113–120 | Exit ticket: name one colour decision and one uncertainty in the export chain. |

## Screening & analysis

- **Video:** a rights-cleared colour workflow or printing/display explanation;
  stop when the source/display assumption changes.
- **Stills:** a palette exemplar, a low-contrast counterexample, and a bitmap
  enlargement that reveals sampling.
- **Graphic:** `source colour → profile/space → display/export → viewer` with
  a contrast checkpoint and text-only table.

## Studio sprint

Deliver a palette sheet, a 1600px bitmap crop, an accessible alternate palette,
and a colour decision log. Include file format, profile assumption, creator/source
for any reference image, and a note that the class is not a colour-management
validation study.

## Individual problem

Follow the lesson page B3 items (authoritative for assessment):

1. **Diagnostic, no AI:** given two bitmap versions at different bit depths, identify each artifact and why.
2. Describe by hand the visual difference between limited and full palette for a described image.
3. Distinguish colour correction from colour change using B1 disclosure framing.

Students submit editable palette data, preview, export note, and one sentence
on what they would verify on a different monitor or printer.

## Media prospector request

`field=colour and bitmap imaging; subfield=fashion palette, sampling, display
and accessibility; semantics=technical demonstration|exemplar|counterexample;
licences=CC0|CC BY|CC BY-SA|public domain; require=contrast-safe thumbnail,
alt text, and source/creator metadata.`

## Enrichment handoff

Read `../unit-enrichment/I.3-colour-bitmaps/PROFESSOR.md` before drafting the
lecture or deck. Its critical question about the default viewer must remain in
the lesson and in the final debate; do not reduce the new palette routes to a
tool tutorial.

## Grounding note

- **VERIFIED:** Roivainen (2025, 8) — node `307e67e0-f3a3-5fa3-a623-ceebc74fd70c`, `evaluator_safe=yes`.
- **VERIFIED:** AlDahoul et al. (2025) — abstract node `b3fd5903-1b33-50b3-8abe-cd2e9241513a` (racial homogenization claim) for the critical deck slide; does not support classroom policy prescription.
- **[BIBLIO-GAP]:** Albers (2013) — not in scholar vault; use T1 verbatim + Chicago Reference.
- **NONE:** colour-management teaching sequence for fashion HE.
- **Critical:** C3 AlDahoul generative bias; session default-viewer prompt.
- **Refreshed discovery:** Nobile et al. (2021) palette computation and
  Balasubramanian (2026) HEX/Pantone activity are `[BIBLIO-GAP]` until Ahmes
  page resolution; they inform comparison, not efficacy claims.

## Canonical provenance record

The following complete records mirror the canonical English lesson and govern this instructor prompt. Unresolved records remain explicitly bounded; they are not promoted as validated pedagogy.

```text
PROVENANCE_LINE: claim=I.3.claim.relational-colour; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="Albers perceptual colour digital palettes"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Albers; similarity=null; proposed_use="perceptual anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Albers 2013 not in scholar vault; quote=none; public_citation="(Albers 2013)"; supports="relational perceptual colour teaching"; does_not_support="colour-management pedagogy sequence"
PROVENANCE_LINE: claim=I.3.claim.platform-editing-styles; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="skilled vision Instagram editing colour trends"; source_locator=MASTER-IDEAS I.3; similarity=null; proposed_use="frontier/platform colour conventions"}; source={document_coat=47ce5b17; extraction_db=ahmes-library/scholar/documents/how_i_edit_my_instagram_images_investigating_skilled_vision_in_the_work_of_youtube_s_lifestyle_content_creators_47ce5b17/extract/extraction.db; node_id=307e67e0-f3a3-5fa3-a623-ceebc74fd70c; page_index=7; printed_page=8}; resolver="ahmes query --cite extraction.db:307e67e0-f3a3-5fa3-a623-ceebc74fd70c --require-evaluator-safe evaluator_safe=yes"; quote="editing styles that are popular at a given moment"; public_citation="(Roivainen 2025, 8)"; supports="time-bound platform colour and tonal conventions"; does_not_support="fashion-specific colour syllabus or classroom efficacy"
PROVENANCE_LINE: claim=I.3.gap.colour-management-pedagogy; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion higher education colour management pedagogy validated"; source_locator=null; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated colour-management teaching method for fashion students"
PROVENANCE_LINE: claim=I.3.critical.generative-bias; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="AI generated faces gender racial bias fashion"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc § AlDahoul; similarity=null; proposed_use="critical technical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=AlDahoul 2025 not in scholar vault; quote=none; public_citation="(AlDahoul et al. 2025)"; supports="image tools are not representationally neutral"; does_not_support="classroom policy prescription"
PROVENANCE_LINE: claim=I.3.critical.default-viewer; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="colour accuracy default viewer accessibility"; source_locator=i-3-colour-bitmaps.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming default viewer and contrast assumptions"; does_not_support="empirical accessibility claim for cohort"
```
## Critical field lens & open living prompt

**Field tension:** technical “accuracy” is interpreted through devices, lighting,
cultural colour codes, and viewers with different perceptual access.

**Critical perspective:** Who is treated as the default viewer when a palette is
called accurate, beautiful, or accessible?

**Open living prompt:** Which colour decisions become visible only when another
viewer, display, or cultural code enters the room?

**Bring forward:** one contrast test, display mismatch, or excluded reading.
