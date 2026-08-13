# CV & official guides — Creación Digital

Institutional guías (scraped) and CV drafts for Creación Digital I–II.

| Path | Role |
| ---- | ---- |
| [`guides/1-creacion-digital-i.json`](./guides/1-creacion-digital-i.json) | **Mandatory** official structure — CD I (unicrawler clone) |
| [`guides/3-creacion-digital-ii.json`](./guides/3-creacion-digital-ii.json) | **Mandatory** official structure — CD II (unicrawler clone) |
| [`../oficial-guia-framework.mdc`](../oficial-guia-framework.mdc) | How every pedagogical action must respect those JSON fields |
| [`../dc-cv-forge.mdc`](../dc-cv-forge.mdc) | Prompt to author `uem-ruvebal-creacion-digital-*-cv.md` |
| `uem-ruvebal-creacion-digital-*-cv.md` | **forged 2026-08-13** — instructor CV / guía curricular drafts |

## Provenance

- **Cloned:** 2026-08-11 from `/Users/ruvebal/src/unicrawler/output/guides/`  
- **CD I PDF:** https://universidadeuropea.es/myfiles/pr/9729001103.pdf  
- **CD II PDF:** https://universidadeuropea.es/myfiles/pr/9729001108.pdf  

```bash
# Re-sync when unicrawler re-scrapes
cp ~/src/unicrawler/output/guides/1-creacion-digital-i.json \
   digital-creativity-pedagogy/cv/guides/
cp ~/src/unicrawler/output/guides/3-creacion-digital-ii.json \
   digital-creativity-pedagogy/cv/guides/
# Then re-check hour/weight sums in oficial-guia-framework.mdc
```

## Known scrape defects (do not paper over)

| Issue | Detail |
| ----- | ------ |
| **CD I presencial evaluation — RESOLVED 2026-08-13** | JSON weights sum 85% (`Caso/problema` mis-scraped as 20 instead of 15; `Investigaciones y proyectos` as 10 instead of 20; missing `Cuaderno de prácticas de laboratorio/taller` 10% row entirely). **PDF re-extracted via Ahmes this session** (`9729001103.pdf` → docling, 98 blocks) and confirms 100% across 4 rows: 55/15/20/10. Correct table is now in `uem-ruvebal-creacion-digital-i-cv.md` §8, not the JSON. **JSON itself not yet re-synced — this is a clone bug, not a footnote.** |
| **CD I presencial formative — RESOLVED 2026-08-13** | Was previously read as "140h, deliberately different from CD II's 150h" — **that reading was wrong.** The PDF's own TOTAL row says 150, matching CD II exactly; the JSON clone is simply missing the `Clases magistrales` (10h) row. Not a real difference between the two courses — a dropped row. Correct table in `uem-ruvebal-creacion-digital-i-cv.md` §7. |
| CD II methodologies | One concatenated string in `methodologies.General[1]` — prefer discrete method names when writing CVs. Not re-checked against PDF this session (CD II's JSON sums were internally consistent, 150h/100%, so no trigger to reconcile — see `oficial-guia-framework.mdc`'s own rule: check PDF *when sums disagree*, which CD II's didn't) |

**Action still open:** re-sync `guides/1-creacion-digital-i.json` from unicrawler with the
corrected rows, so the next forge run doesn't have to re-discover this. The CV draft is correct
today; the JSON clone underneath it is not.
