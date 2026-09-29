# EXECUTE — Nuevos medios UEM · Virtual Campus PDF export layer

**Status:** scheduled source-grounding pass

## Primary course-grounding layer

Use `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/26-27/ONLINE/PDFs_export/` as the primary Virtual Campus teaching-content source for `profield-nuevos-medios-moda-2026-27`. The export currently contains 23 PDFs: three Temario PDFs per U1–U6, five activity/assessment PDFs, and the U1 glossary resource.

Filename mapping:

```text
9729001302_U{1..6}_T{01..03}.pdf  →  unit theme 1–3
9729001302_U{1..6}_AA1.pdf        →  unit activity/assessment brief
9729001302_U1_RC_GLOSARIO.pdf     →  U1 complementary glossary
```

## Preservation metadata

For every source, preserve: original filename and hash, unit, theme/activity code, Canvas location, course language, export date, author/source as printed, and publication status. Do not overwrite the PDFs or collapse them into the research bibliography namespace.

## Corpus separation

Extract into a dedicated UEM teaching-content namespace/project, separate from personal/research bibliography projects. Suggested project slug: `profield-nuevos-medios-moda-2026-27-teaching-content`. Inject only after a manifest dry-run and explicit operator confirmation.

## Cross-concept pass

Cross-reference the exported teaching content against:

- the official UEM guide and JSON contract;
- related research-vault findings;
- profield critical runs, including non-Western and critical materials;
- current lessons, three-theme unit maps, activities, dates, and assessment weights.

Every forged insertion must label its boundary: official source content, critical pedagogical interpretation, authored teaching voice, or unresolved evidence. Internal corpus IDs, vault paths, extraction databases, and resolver states remain behind the publication switch.

## Execution sequence

```text
inventory + hashes → local Ahmes extraction → semantic enrichment → metadata/citation gate
→ Athanor dry-run in teaching-content project → injection
→ concept crosswalk → lesson/deck forge → publication and citation gates
```

Do not use the ordinary guide PDF as a substitute for these Canvas exports: the guide controls authority and assessment, while the exports preserve actual sequencing, examples, scaffolding, and teaching voice.
