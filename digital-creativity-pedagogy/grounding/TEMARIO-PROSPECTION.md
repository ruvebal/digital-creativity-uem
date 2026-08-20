# Temario bibliography prospection

Official CONTENIDOS need checkable references (**DOI and/or ISBN**) before CV / unit forge reading lists are honest.

## Promoted resultants

| Location | Role |
| -------- | ---- |
| `digital-creativity-pedagogy/grounding/temario/` | **Publication head** for the six promoted temario resultants |
| `profield/runs/digital-creativity/01/temario/*.pass1.resultant.mdc` | Profield provenance/source-run copy |

| Strand | Files |
| ------ | ----- |
| Technique | T1 · T2 · T3 |
| Critical | C1 · C2 · C3 |

Most former bibliography-data gaps have been repaired by later DOI/ISBN lookup,
retrieval, metadata coats, and procurement notes. Treat remaining `BIBLIO-GAP` or
`READY_DECLARED_GAP` labels as precise gates: page-level citation still needed,
evaluator-safe coat not yet available, no OA/full text procured, or a real
pedagogical research gap still being declared.

## PDF corpus + Ahmes path

Shared with the field run (sibling pattern):

`/Users/ruvebal/src/profield/runs/digital-creativity/01/pdfs/`

After promoting resultants: extract DOI/ISBN → Unpaywall retrieve → **Ahmes batch** → two-pass coats → `make ingest-profield-dc` / Athanor inject.

```bash
cd ~/src/profield
make retrieve-temario-dc      # OA PDFs
make pending-dc               # PENDING-procurement.md (DOI no-OA · fail · ISBN)
make athanor-ready-dc-batch   # batch + meta×2 + require-coats
# or if batch already done:
make athanor-ready-dc

cd ~/src/deviac && make ingest-profield-dc
```

Artifacts: `01/corpus-seed-list-temario.md` · `01/REFERENCES-temario-for-refcheck.md` · `01/PENDING-procurement.md` · `01/temario/retrieve-report.json`  
Scripts index: `~/src/ahmes/scripts/INDEX.md` · Guide: `profield/docs/PROFIELD-CORPUS-USAGE-GUIDE.mdc`

## Prompt sources (still editable)

- Technique prompts: `profield/.../02-temario-contenidos/`
- Critical prompts: `profield/.../03-temario-critica/`
