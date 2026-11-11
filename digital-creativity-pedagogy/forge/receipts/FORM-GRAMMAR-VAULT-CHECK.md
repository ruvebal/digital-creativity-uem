# Form-grammar vault check — 2026-11-11

**Scope:** CD I form grammar across matching lessons — **not I.6 alone.**  
**Supersedes:** `I6-FORM-GRAMMAR-VAULT-CHECK-20261111.md` (filename was too narrow).  
**Status:** unpublished operational receipt · forge seed lives beside this file as `../FORM-GRAMMAR.execute.md`.  
**Skill bridge:** studio [`platonic-solids`](/Users/ruvebal/src/.cursor/skills/platonic-solids/SKILL.md) (default mode `FAVICON-RIVE-3D`; forge prop `props/forge-index.json`).

## Lesson map (who consumes which primitive)

| Primitive / solid | Teaching voice (resolved) | Primary CD I homes | Vault ready? |
| --- | --- | --- | --- |
| Point · line · plane | **Kandinsky**, *Point and Line to Plane* | I.2 drawing → I.5 3D form → I.6 volume (plane before wear) | **Yes** — `ruslib_kandinsky_…_5c285f15` · already `kandinsky-2012` in `references.yml` (cite by **section**, EPUB) |
| Square | **Munari**, *Discovery of the Square* (1960) + **Mondrian** neo-plastic planar equilibrium | I.1–I.3 composition · neoplastic decks · I.5 planar structure | **Partial** — Mondrian coats yes; PAP omnibus sampler coated `munari_square_circle_triangle_d246eca6` (**27 pp** — not full Square book); prior *Circle*-only echo remains |
| Circle | **Munari**, *Discovery of the Circle* (1964/2009 Corraini) | I.2–I.3 modules · I.5 revolution solids · I.8 motion as rotation metaphor | **Yes** — `bruno_munari_the_circle_…_84c0fd33` + omnibus sampler `d246eca6` |
| Triangle | **Munari**, *Discovery of the Triangle* (1976) — equilateral as modular connective form | I.2 structure · I.5 nets/modules · I.6 structural volume cues | **Partial** — omnibus sampler coat `d246eca6` (118 blocks); full Corraini *Triangle* still preferred if sampler proves thin |
| Pentagon | **Pacioli**, *Divina proportione* (Winterberg 1889 critical edition) — pentagon ↔ golden section ↔ **dodecahedron** | I.5 Platonic solids · I.6 structured volume · optional I.2 construction | **Yes** — coat `…_52954462` · AU repaired · `pacioli-1889` · evaluator_safe cites clear (conf 0.95) |
| Platonic solids as volumes | **Bertol 2016** (parametric `{p,q}`, `α`, `β`, `CR`) + **Pacioli/Leonardo** plates + **Fuller** Synergetics | **I.5** primary · **I.6** behaviour-on-solid · graphics skill `platonic-solids` | **Yes coats** — Bertol `…_8a6631b8` · Pacioli `…_52954462` · Fuller already `d86aca34` / `318a6518` |
| Linear perspective | **Panofsky**, *Perspective as Symbolic Form* (1993 Zone) — Alberti still gap | I.2 multi-view · I.5–I.6 front/side/¾ | **Partial** — Panofsky coat **yes** `…_8c4ae116` (551 blocks); Alberti / *perspectiva pingendi* still absent |

False friends already filtered: coats matching “perspective” as *ethical / instructor / teatro perspectiva* are **not** form-grammar sources.

## Triangle — resolved authority

**Who:** Bruno Munari, *La scoperta del triangolo* / *The Discovery of the Triangle* (1976; Corraini / PAP trilogy with Square + Circle).

**Why him (not a fourth unrelated author):** same pedagogical instrument as circle/square — alphabetical visual encyclopedia of the equilateral triangle as **modular connective** form (nature → architecture → design). Field sources: Corraini product page; Princeton Architectural Press *Square Circle Triangle* (2015 omnibus); Hyperallergic overview of the trilogy.

**Ahmes/Athanor now:** *Circle* coat still primary (`84c0fd33`). PAP omnibus sampler queued+extracted 2026-11-11: `munari_square_circle_triangle_d246eca6` (27-page Preview PDF from `bibliographies/munari_bruno/Munari-Square Circle Triangle.pdf`). Treat as **bridge coat**, not proof the full trilogy is in vault — expand if page-spot shows missing Square/Triangle chapters.

## Pentagon — coated + cite-safe (AU repaired 2026-11-11)

**Who (primary):** Luca Pacioli, *Divina proportione* — studio text: Constantin Winterberg, ed., *Die Lehre vom Goldenen Schnitt* (Vienna: Carl Graeser, 1889), Quellenschriften series.

**Coat:** `quellenschriften_fur_kunstgeschichte_und_kunsttechnik_fra_luca_pacioli_constantin_winterberg_divina_proportione_die_lehre_vom_goldenen_schnitt_1889_carl_graeser_52954462`.  
**Cite gate:** operator RIS/metadata repair — AU=`Pacioli, Luca`; editor=`Winterberg`; Eitelberger/Ilg cleared · conf **0.95** · `evaluator_safe=yes` · key `pacioli-1889`.

**Who (volume bridge already in vault):** R. Buckminster Fuller, *Synergetics* (1975) and *Synergetics 2* (1983) — tetrahedron / icosahedron as thinking-and-structure volumes; coats `d86aca34` / `318a6518`.

**Parametric bridge:** Daniela Bertol, “The parametric making of geometry: the Platonic solids,” *Int. J. Rapid Manufacturing* 6 (1), 2016 — Table 1 + `CR` envelope in `platonic-solids/references/BERTOL-MATHS.md`. Coat `…_8a6631b8` · authors conf raised **0.95** · `bertol-2016` · `evaluator_safe=yes`.

## Perspective — Panofsky cite-safe; Alberti still open

**Panofsky coat:** `perspective_as_symbolic_form_erwin_panofsky_1993_zone_books_8c4ae116`.  
Spot-checked body quote cleared (`evaluator_safe=yes`); key `panofsky-1993`. Alberti / *perspectiva pingendi* manuals remain absent.

## Batch receipt (2026-11-11)

Stage dir: `bibliographies/art/.ahmes-form-grammar-20261111/`  
Ahmes library: `scholar` · `--save-db --treeshake` (NER/semantic deferred — background enrich was SIGKILL-prone).

| Symlink | Coat suffix | Blocks (Docling) |
| --- | --- | ---: |
| `bertol-2016-parametric-platonic-solids.pdf` | `8a6631b8` | 283–284 |
| `pacioli-divina-proportione-winterberg-1889.pdf` | `52954462` | 2175 |
| `panofsky-1993-perspective-as-symbolic-form.pdf` | `8c4ae116` | 551 |
| `munari-square-circle-triangle.pdf` | `d246eca6` | 118 (27-page sampler) |

## Vector / neural pass (2026-11-11)

- `profield-dc-3d-form-volume-pedagogy`: Coats / Papahristou — garment volume methods (already I.6), not shape grammar.
- `profield-digital-creativity` + `mondrian-project`: Kandinsky / Mondrian / Munari *Circle* / Fuller adjacency as above.
- Graph entity resolve for “Alberti”: empty in sampled SVCM vault.

## Page-spot + inject (2026-11-11 follow-up)

Full receipt: [`FORM-GRAMMAR-PAGE-SPOT.md`](FORM-GRAMMAR-PAGE-SPOT.md).

- **DevIAC:** form-grammar manifest → `profield-digital-creativity` / `field_prospection` (4 vaults OK).
- **Panofsky:** body quote **evaluator_safe=yes** (node `5c147654-…`, p. 27).
- **Pacioli:** AU repaired → **evaluator_safe=yes** (conf 0.95; no longer Eitelberger).
- **Bertol:** authors conf **0.95** → **evaluator_safe=yes** (Table 1 / Schläfli nodes).
- **Perspective kit P2–P6:** static SVGs + local `.riv` published under `docs/assets/.../perspective-kit/` (watermarked CLI builds; not yet lesson-embedded).
- **Munari Triangle:** `triangle.pdf` ≡ sampler hash — full Triangle still missing.
- **Alberti:** absent in bibliographies / library.
- **Course favicon:** lab shipped at `/labs/platonic-favicon/` — brand `favicon.svg` **not** replaced.

## Recommendation

1. **Student cites:** Kandinsky; Panofsky; Pacioli; Bertol — all spot-checked nodes above clear `evaluator_safe` (Chicago keys in `references.yml`).
2. **Still procure:** full Corraini *Discovery of the Triangle* · Alberti treatise.
3. **Already usable:** Kandinsky; Fuller; Munari *Circle*; Bertol maths via `platonic-solids`; Panofsky/Pacioli/Bertol cleared excerpts; perspective-kit SVG twins.
4. **Forge:** `FORM-GRAMMAR.execute.md` + `platonic-solids` lab · kit index [`PERSPECTIVE-VOLUME-IMAGE-KIT.md`](PERSPECTIVE-VOLUME-IMAGE-KIT.md) — embed P2–P6 `.riv` only after watermark plan or accept splash.

## Tie to I.7 media-sources addendum

Provenance Graph A class 3 (CGI) and Graph B hybrid remixes are where students may *depict* Platonic or Munari forms digitally — still ledger upstream class; form grammar does not grant image rights.
