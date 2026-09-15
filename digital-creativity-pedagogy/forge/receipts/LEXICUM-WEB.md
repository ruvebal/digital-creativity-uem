# Receipt — LEXICUM-WEB forge

**Status:** COMPLETE  
**Branch:** `forge/lexicum-web-route`  
**Date:** 2026-09-13  
**Cold review:** [Cold-review lexicum forge](a2d388d8-5b8f-4359-bb38-57b47b3118d9) — **PASS-WITH-FIXES** (fixes applied)

## Fixes applied before master forge

1. Sanitized discontinued-repo prefix in fashion `fit` scope note (upstream lexfield YAML) + sync sanitizer.
2. Re-synced snapshot; `MANIFEST.json` now carries matching `stats` (88 / 3).
3. Extended `scripts/verify-publication-safety.mjs` with `\bfashlex\b` forbid.
4. Master `docs/lexicum/index.md` forged with relation label resolution; `scope_note` / `uri_local` not rendered.
5. Kramdown escape fixed via `markdown="0"` on root wrapper (indented HTML was code-blocked).

## Counts

| Surface | Value |
| ------- | ----- |
| Concepts | 88 |
| Schemes | Design 29 · Business 31 · Communication 28 |
| Snapshot | `cv/data/lexicum/fashion.json` ≡ `docs/_data/lexicum.json` |
| Cloned at | 2026-09-13T15:03:10Z |

## Validation

- `bundle exec jekyll build` — OK
- `_site/lexicum/index.html` — 88 concept cards, unescaped HTML
- `node scripts/verify-publication-safety.mjs` — passed
- Firewall spot-check on `/lexicum/` — no Ahmes/Athanor/DevIAC/`/Users`/fashlex

## Follow-up — shared publication contract (2026-09-13)

- Schema renamed to **`lexfield-public/v1`** (fashion = prototype tenant; CT reuses same Field→Subfield→Concept).
- Header credit: author + ORCID + stack versions (lexfield 0.1.0, Jekyll 3.10.0, Liquid 4.0.4, SKOS 2009-08-18, CIDOC-CRM 7.1.3).
- Per-card footer: **semantic or omit** (CIDOC-CRM mapping and/or scope note only — no boilerplate “SKOS · CIDOC-CRM”).
- CT-UEM hydrate aligned to the same contract (`/lexicum/en/`).

## Public route

`/digital-creativity-uem/lexicum/` — Fashion Lexicum (search + scheme filters + deep anchors)
