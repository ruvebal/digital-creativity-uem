# Curriculum-local Fashion Lexicum snapshot

Cloned from the studio **lexfield** fashion field for the Creación Digital public
route `/lexicum/`. Re-sync:

```bash
python digital-creativity-pedagogy/forge/scripts/sync-fashion-lexicum.py
```

| Path | Role |
| ---- | ---- |
| `fashion/` | YAML source snapshot (field + three schemes) |
| `fashion.json` | Compiled public payload |
| `exports/` | SKOS review exports (ttl / jsonld / md) |
| `MANIFEST.json` | Clone provenance (pedagogy-only) |

Do not live-mount the engine repo into Pages. Student HTML must not expose
absolute local paths or corpus-tool names.
