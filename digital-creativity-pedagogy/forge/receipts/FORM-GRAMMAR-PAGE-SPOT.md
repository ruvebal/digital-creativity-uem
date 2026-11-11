# Form-grammar page-spot — Pacioli / Panofsky / Bertol (2026-11-11)

**Purpose:** gate body quotes before lesson inject. DevIAC vectors discover only.  
**Coats:** Pacioli `52954462` · Panofsky `8c4ae116` · Bertol `8a6631b8`.

## Verdict

| Work | `evaluator_safe` for body quote? | Notes |
| --- | --- | --- |
| **Panofsky 1991/1993** | **YES** (spot-checked) | AU/TI coats clean; cite below cleared |
| **Pacioli / Winterberg 1889** | **YES** (operator repair 2026-11-11) | RIS + metadata AU=`Pacioli, Luca`; editor=`Winterberg`; Eitelberger/Ilg cleared. Cite conf **0.95** `source=metadata` |
| **Bertol 2016** | **YES** (operator raise 2026-11-11) | AU/TI + DOI seeded; authors conf raised **0.70 → 0.95**. Table 1 / Schläfli nodes clear `--require-evaluator-safe` |

## Cleared Panofsky cite (usable in lessons after Chicago key)

```
ahmes query --cite <pan_db>:5c147654-5e0f-5dbf-bbef-60eae2a22a52 \
  --style chicago-author-date --require-evaluator-safe
→ (Panofsky 1991, 27)  confidence=0.95  evaluator_safe=yes  page_index=26
```

**Excerpt (for professor selection — trim to complete sentence before publish):**

> At this point we can almost predict where "modern" perspective will unfold: namely, where the northern Gothic feeling for space, strengthened in architecture and especially sculpture, seizes upon the architectural and landscape forms preserved in fragments in Byzantine painting…

Public Chicago key already in `references.yml`: `panofsky-1993`. Prefer Zone Books date note already present.

## Cleared Pacioli cites (AU repaired)

```
ahmes query --cite <pac_db>:c33230a5-f9d2-5028-a155-bcda6b95212d \
  --style chicago-author-date --require-evaluator-safe
→ (Pacioli 1889, 12)  confidence=0.95 source=metadata evaluator_safe=yes

ahmes query --cite <pac_db>:22a8e67f-e86b-5c77-a224-335fa2205e0f \
  --style chicago-author-date --require-evaluator-safe
→ (Pacioli 1889, 14)  confidence=0.95 source=metadata evaluator_safe=yes
```

| node_id | page_index | Why interesting |
| --- | --- | --- |
| `c33230a5-f9d2-5028-a155-bcda6b95212d` | 11 | Winterberg intro on theoretical/practical worth of golden section |
| `22a8e67f-e86b-5c77-a224-335fa2205e0f` | 13 | Continuous proportion vs golden section as special case |
| `e676a38a-357f-5c9f-b383-259d94c01995` | 15 | Geometric proportion + rhythm for the eye |
| Italian corpus nodes ~75–106 | pentagon / dodeca / icosa constructions | Leonardo-plate adjacency; OCR heavy |

Public Chicago key: `pacioli-1889` in `references.yml`. Cite surface now emits `(Pacioli 1889, …)` — no longer Eitelberger.

**Repair surface:** `extract/bibliographic.ris` (AU=Pacioli; A2=Winterberg) + metadata `authors`/`editors`/`biblio_repair_note`. Do **not** re-run `--force-meta --online` without re-checking — cascade re-selects the series heading.

## Cleared Bertol cites (conf raised)

```
ahmes query --cite <ber_db>:47abced0-d67d-565d-bc25-e91e4e2f538e \
  --style chicago-author-date --require-evaluator-safe
→ (Bertol 2016, 3)  confidence=0.95 source=metadata evaluator_safe=yes

ahmes query --cite <ber_db>:a061c0ed-90d5-5642-876d-1c08a82026c7 \
  --style chicago-author-date --require-evaluator-safe
→ (Bertol 2016, 3)  confidence=0.95 source=metadata evaluator_safe=yes
```

| node_id | page_index | Content |
| --- | --- | --- |
| `47abced0-d67d-565d-bc25-e91e4e2f538e` | 2 | Table 1 Schläfli / α / β |
| `a061c0ed-90d5-5642-876d-1c08a82026c7` | 2 | Schläfli definition |
| `80372fb2-3a9b-5eb9-9f07-56d91162348a` | 7 | circumsphere / `CR` size |

Public Chicago key: `bertol-2016`. Journal printed folios in PDF text begin near article p. 33 — Chicago page numbers above are `scheme=pdf_order` (pdf_order + 1); reconcile to printed SP/EP before claiming journal pagination in lessons.

## Munari Triangle procure

`munari_bruno/triangle.pdf` **SHA-256 equals** `Munari-Square Circle Triangle.pdf` (`d246eca6…`) — same 27-page sampler, not a full *Discovery of the Triangle*. Full Corraini Triangle remains **unprocured**.

## Alberti

No PDF/coat under studio bibliographies or `ahmes-library` (search 2026-11-11). Perspective teaching may use Panofsky (cleared) while Alberti stays Declared gap.

## DevIAC inject

`make ingest-ahmes-manifest MANIFEST=…/form-grammar-20261111/.ahmes/batch-manifest.json PROJECT_SLUG=profield-digital-creativity` → 4 vaults OK (Bertol 51 + Pacioli 973 + Munari 12 + Panofsky included). Discovery only.
