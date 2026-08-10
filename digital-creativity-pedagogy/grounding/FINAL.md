<!--
AUTHORITY HOME — digital-creativity-uem
Canonical for Creación Digital teaching/research once emancipated.
Upstream profield path: /Users/ruvebal/src/profield/runs/digital-creativity/
Synced: 2026-08-10 · file: FINAL.md
Re-sync: copy from profield over this file and restore this banner.
PDFs / Ahmes extractions stay in the Ahmes library + profield/pdfs — not duplicated here.
-->

# Digital Creativity — final run result (01)

_Updated 2026-08-09 after Pass 1b → 2b → 3b (Ibero-American layer)._

## Canonical narrative map

**`pass1b.edited.md`** — authoritative field landscape (global + Ibero-America; Pass-3b tool upgrades).  
Prior global-only map: `pass1.edited.md` (kept for provenance).

## Machine digest

**`digest.md` / `digest.json`** (rebuilt after Pass-3b ingest)

| Metric | Value |
|--------|------:|
| Rows | 75 |
| Confirmed | 24 |
| Disputed | 7 |
| Unverified | 27 |
| Pending OA | 32 |

## Field in one paragraph

Digital creativity for fashion communication is a **durable media-literacy stack** under a **2024–2026 GenAI / VTON / XR frontier**. Ibero-America adds a strong **Spanish fashion-film / branded-AV** centre, **Brazil–Spain virtual-influencer** work (Lu do Magalu), Argentine *Cuadernos* **fashion–AI–law–ethics** (Pampuri, Albanese, Luna), and Spanish **GenAI assessment governance** (UPM), while remaining thin on fashion-studio GenAI pedagogy and student-portfolio research.

## Twin mandate

| Durable | Frontier |
|---------|----------|
| Colour, photographic literacy, animation principles, fashion film, brand identity, retouching ethics | Controllable diffusion, VTON, XR/metaverse, virtual influencers, GenAI assessment, algorithmic justice / dark patterns |

## Pass-3b headline corrections

1. **Pampuri 2026 restored** — Silvana Pampuri, *Cuadernos* 299, Dialnet `10654595` (Pass 2b false “unverifiable”).
2. Upgraded: Fontes & Lodi, Iszoro, Ramallal & Ruiz Mondaza, Ruiz Calleja, Delgado arXiv, Flavián (adjacent), Margalina, Albanese, Luna, Carrillo-Durán, Rodríguez-Borlado, Campinho, Carvalho (non-fashion scope).
3. **Dourado** relocated to Spain (`10.5783/revrrpp.v14i28.871`).
4. Soft: Jiménez Marín; Gouveia-as-fashion-doctorate; Borges/Fanpage-Karma.

## Operator files

| File | Role |
|------|------|
| `fields/digital-creativity.yaml` | FieldSpec |
| `pass1b.edited.md` | **Final map (reference)** |
| `pass3b.raw.md` | Tool verification ledger (Ibero) |
| `digest.md` | Provenance table |
| `corpus-seed-list-ibero.md` | Ibero OA seed list |
| `pdfs/` | Local OA corpus for Ahmes |
| `retrieval-manifest.json` | Unpaywall attempt log |

## Ahmes next

```bash
cd ~/src/ahmes && source .venv/bin/activate
ahmes batch /Users/ruvebal/src/profield/runs/digital-creativity/01/pdfs \
  -o ~/ahmes-library \
  --project scholar \
  --save-db --treeshake --enrich-ner --enrich-semantic --workers 2
```
