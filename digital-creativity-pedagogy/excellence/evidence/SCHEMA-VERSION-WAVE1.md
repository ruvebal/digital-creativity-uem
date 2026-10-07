# Schema version note — Wave-1 decks (PHASE-EX3)

**Decision:** Wave-1 decks adopt `"schema_version": 2` (same contract as CT Excellence).
Until a deck is migrated, the validator treats it as **legacy** (warnings only under
`--strict`). Outside Wave-1 (CD II / Nuevos Medios / other) always warns, never hard-fails
(Amendment A1 / FINDINGS A5).

## Wave-1 surfaces

| Deck path | Current `schema_version` | Notes |
| --- | --- | --- |
| `docs/tracks/en/uem/2627-dci/i-1-fashion-image/data/content.json` | missing (legacy) | Migrate in EX4 with rights + image briefs |
| `docs/tracks/en/uem/2627-dci/i-2-2d-drawing/data/content.json` | missing (legacy) | same |
| `docs/tracks/en/uem/2627-dci/i-3-color-bitmaps/data/content.json` | missing (legacy) | same |
| `docs/tracks/en/uem/2627-dci/i-4-effects/data/content.json` | missing (legacy) | same |
| `docs/tracks/en/uem/2627-dci/i-5-three-dimensional-form/data/content.json` | missing (legacy) | same |
| `docs/tracks/en/uem/2627-ml/fashion-image-analysis/data/content.json` | missing (legacy) | Wave-1 special |
| `docs/tracks/en/uem/2627-dci/how-to-pass-this-track/data/content.json` | n/a | Not a media deck (`slide_role` absent) — skipped |

I.6–I.9 decks, when forged, must ship as `schema_version: 2` from the first commit.

## v2 contract (summary)

See `forge/STUDENT-SLIDESHOW-FORGE.mdc` §"Deck schema version 2".

- `background_kind`: `curated` \| `diagram` \| `geometrical` \| `none` (`profield` retired)
- Slide binding: `asset_id` only — no rank dealing / wrap-around reuse
- Renditions: `docs/assets/images/deck-media/` (≤ 600 KB; no raw SVG)
- Legacy files may remain in `profield-cache/` while referenced; orphans there **warn**, not delete (EX3 policy)
- Gate: `node scripts/validate-decks.mjs --strict --rights=flag`

## FINDINGS

Closes discipline for **B2** (orphan/rights/reuse hooks) and **B3** (CT-grade validator port) at the tooling layer; slide-bound curation itself is **EX4**.
