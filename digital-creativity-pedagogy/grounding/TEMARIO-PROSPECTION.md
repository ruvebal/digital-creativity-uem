# Temario bibliography prospection

Official CONTENIDOS need checkable references (**DOI and/or ISBN**) before CV / unit forge reading lists are honest.

## Canonical resultants (promoted)

| Location | Role |
| -------- | ---- |
| `profield/runs/digital-creativity/01/temario/*.pass1.resultant.mdc` | **Canonical** field grounding (6 files) |
| `digital-creativity-pedagogy/grounding/temario/` | Teaching-repo mirror (same 6; no PDFs) |

| Strand | Files |
| ------ | ----- |
| Technique | T1 · T2 · T3 |
| Critical | C1 · C2 · C3 |

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
