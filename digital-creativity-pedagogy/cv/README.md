# CV & official guides — Creación Digital

Institutional guías (PDF-patched clones) and CV drafts for Creación Digital I–II.

| Path | Role |
| ---- | ---- |
| [`guides/1-creacion-digital-i.json`](./guides/1-creacion-digital-i.json) | **Mandatory** official structure — CD I (**2026-27** PDF, patched 2026-08-14) |
| [`guides/3-creacion-digital-ii.json`](./guides/3-creacion-digital-ii.json) | **Mandatory** official structure — CD II (**2025-2026** PDF, confirmed 2026-08-14) |
| [`../oficial-guia-framework.mdc`](../oficial-guia-framework.mdc) | How every pedagogical action must respect those fields |
| [`../dc-cv-forge.mdc`](../dc-cv-forge.mdc) | Prompt to author `uem-ruvebal-creacion-digital-*-cv.md` |
| [`cv/uem-ruvebal-creacion-digital-*-cv.md`](./uem-ruvebal-creacion-digital-i-cv.md) | Instructor CV drafts (hours/eval close; SAFE bib seeded) |
| [`UNIT-PLAN.md`](./UNIT-PLAN.md) | Unit IDs I.1–I.9 / II.1–II.6 bound to CONTENIDOS |

## Provenance

- **Cloned:** 2026-08-11 from `/Users/ruvebal/src/unicrawler/output/guides/`
- **PDF-patched:** 2026-08-14 from the live UEM URLs (PyMuPDF text extract; not ingested into Ahmes)
- **CD I PDF:** https://universidadeuropea.es/myfiles/pr/9729001103.pdf · metadata CreationDate 2026-08-03 · academic year **2026-27** · formative p.3 · evaluation p.4
- **CD II PDF:** https://universidadeuropea.es/myfiles/pr/9729001108.pdf · academic year **2025-2026** · formative p.3 · evaluation p.4

```bash
# Re-sync when unicrawler re-scrapes *and* the scrape matches the live PDF
cp ~/src/unicrawler/output/guides/1-creacion-digital-i.json \
   digital-creativity-pedagogy/cv/guides/
cp ~/src/unicrawler/output/guides/3-creacion-digital-ii.json \
   digital-creativity-pedagogy/cv/guides/
# Then re-check hour/weight sums in oficial-guia-framework.mdc
# Do not overwrite the 2026-08-14 CD I patch with the 2025-26 unicrawler file.
```

## Known scrape defects (closed in the in-repo clone)

| Issue | Detail |
| ----- | ------ |
| **CD I presencial formative** | Unicrawler dropped `Clases magistrales` (10 h) → 140 h. PDF TOTAL **150**. JSON patched. |
| **CD I evaluation** | Unicrawler 55/20/10 = 85 %, missing Cuaderno 10, wrong Caso/Proyectos numbers. PDF **55 / 15 / 20 / 10** (pruebas / caso / investigaciones / cuaderno), presencial **and** online. JSON patched. |
| **CD I identity** | Live PDF is 2026-27, Facultad de Diseño y Tecnologías Creativas, castellano/inglés, rewritten presentación, RA bullets present. Clone updated. |
| **CD II formative** | Unicrawler hours already matched PDF (150, includes magistral). Project row name is **Proyectos**, not CD I’s Investigaciones y proyectos. |
| **CD II presencial evaluation** | JSON was already 55/15/20/10. The 2026-08-13 **CV draft** dropped Informes y escritos (15 %) and claimed 100 % for an 85 % table. CV restored 2026-08-14. |
| **CD II virtual evaluation** | PDF really has no Caso/problema (pruebas 55 · informes 15 · proyectos 20 · cuaderno 10). Leave it. |
| **CD II year** | Still 2025-2026 on the published PDF. Do not pretend it rolled with CD I. |
| CD II methodologies | Concatenated scrape string split to the five discrete PDF names. |

**Ahmes:** these institutional PDFs are **not** in `profield-digital-creativity`. Hour/weight claims cite the PDF URL + page, not a fission node. Do not duplicate the binaries into this repo.
