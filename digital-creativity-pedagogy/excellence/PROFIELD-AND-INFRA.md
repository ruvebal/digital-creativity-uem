# Profield runs + DevIAC / Ahmes / Athanor / bibliographies

Authority for discovery; **citations still require Ahmes nodes** (publication
firewall). This file is the cascade’s retrieval map — phases name it; they
do not invent alternate corpora.

## 1 · Profield runs in scope (professor list, 2026-10-07)

| Run path under `~/src/profield/runs/` | Primary units | Notes |
| --- | --- | --- |
| `dc-2d-image-craft-pedagogy` (+ `20260816`) | I.2 | Drawing / craft pedagogy |
| `dc-3d-form-volume-pedagogy` | I.5 · I.6 | Form + volume |
| `dc-fashion-composition-references-pedagogy` | I.7 | Fashion references |
| `dc-fashion-motion-still-pedagogy` | I.8 · I.9 | Animation + still life |
| `dc-fashion-retouch-pedagogy` | II.1 | Retouch |
| `dc-avatar-digital-fashion-pedagogy` | II.2 | Avatars |
| `dc-digital-fashion-experience-pedagogy` | II.3 | Digital experiences |
| `dc-fashion-video-pedagogy` | II.4 | Video |
| `dc-fashion-portfolio-web-ux` | II.5 | Web / portfolio |
| `dc-ar-hologram-fashion-pedagogy` | II.6 | Holograms / AR |
| `dc-curriculum-gap-harvest` | all | Gap ledger |
| `digital-creativity` | all / I.1 I.3 I.4 | Field + temario |
| `didactics` | assessment / EX10 | Didactic methods |

Canonical unit map (keep in sync): `forge/PROFIELD-UNIT-MAP.md`.

## 2 · DevIAC vector scopes

| `project_slug` | Use for |
| --- | --- |
| `profield-digital-creativity` | Primary DC field discovery |
| `profield-creativity-techniques` | Shared critical layer (Steimberg, Werhane, Munari, transposition) |
| other `profield-*` / scholar libraries | **Broadcast** search when unit theme warrants (fashion communication, design methods, media theory) — record hits in `research-manifest.yml` with slug provenance |

Ingest refresh (studio machine, before EX6):

```bash
cd ~/src/deviac && make health
# known target — extend only with documented Makefiles, do not invent:
make ingest-profield-dc
```

MCP: `search_knowledge` with `knowledge_scope=field_prospection` for
discovery; never paste vector snippets into student HTML.

## 3 · Ahmes

- Vaults for every PDF cited in Wave-1 lessons must resolve via
  `ahmes query` / extraction.db node IDs.
- Cite grade: Chicago public + gated `curriculum-internal` comment with
  coat · node · page (fail-closed if leaked).
- Gap → `gap` in `research-manifest.yml`, never model-filled.

## 4 · Athanor

Optional inject / field search. Not a citation source. Prefer
`local/athanor.sh` wrappers once EX0 lands them (copy pattern from CT
Excellence `local/`).

## 5 · Bibliographies (broadcast)

Search and map into `research-manifest.yml` (EX6):

| Location (examples) | Relevance |
| --- | --- |
| `~/projects/ruvebal/scholar/bibliographies/` (fashion, digital creativity, creativity, design) | Unit themes |
| Sibling course bibliographies already ingested via Ahmes | Critical / method overlap |
| Profield run `pdfs/` trees for the runs in §1 | Primary pedagogy sources |

Rule: **discover broadly, cite narrowly** — only Ahmes-backed, page-checked
works enter student References.

## 6 · Media

Accepted Profield media + open collections under EX4 autopilot policy
(same spirit as CT: record rights, `flagged` not blocking). Never invent
media. Fractal/geometrical backgrounds only for Lab/Workshop openers and
outros per `SESSION-RHYTHM-AND-DELIVERABLES.mdc`.
