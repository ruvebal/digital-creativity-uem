# Grounding — digital creativity authorities

Synced edited maps and directories for Creación Digital. **Not published** on GitHub Pages.

See parent [`../README.mdc`](../README.mdc) for layout, re-sync commands, and Ladder A/B discipline.

| File | Role |
| ---- | ---- |
| `00-field-scope.md` | Field scope |
| `profield-digital-creativity.md` | Edited field map |
| `profield-authorities-directory.md` | Journals · FACTUM · awards · labs |
| `corpus-seed-list.md` / `corpus-seed-list-ibero.md` | Seed lists |
| `lexicum.yaml` | Controlled vocabulary |
| `FINAL.md` | Run wrap |
| [`TEMARIO-PROSPECTION.md`](./TEMARIO-PROSPECTION.md) | Technique + critical Contidos prompts & Ahmes path |
| [`temario/`](./temario/) | **Canonical** T1–T3 + C1–C3 `.pass1.resultant.mdc` (mirrored from profield `01/temario/`) |
| [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md) | **Worked demo** — how discovery bounced to Tri-Anchors for each resultant |
| [`temario/PROVENANCE-LAYER.json`](./temario/PROVENANCE-LAYER.json) | Machine harvest of that demo (queries, sims, cites, quotes) |

Upstream pipeline: `/Users/ruvebal/src/profield/runs/digital-creativity/`  
Ahmes PDFs / vaults: stay in Ahmes library + `profield/.../pdfs/` — **never duplicate binaries here**.

---

## Retrieval vs citation — durable rule

Three layers; **only one may be cited** in guías or lessons:

| Layer | Role | Cite? |
| ----- | ---- | ----- |
| **Ahmes vault** — `extraction.db` node + page | Authoritative claim + quote | ✅ **Yes — only citable layer** |
| **DevIAC vectors** — `search_knowledge` / HTTP `/vectors/search`, `project_slug=profield-digital-creativity`, `knowledge_scope=field_prospection` | Fast semantic discovery (DERIVED) | ❌ Never cite a snippet |
| **Athanor inject + search** | Cite-grade **index** over injected fission nodes (`--vault` + `--project-slug`) | ❌ Not evidence itself — returns pointers **to** Ahmes nodes |

**Discover in vectors / Athanor, cite from Ahmes nodes.** A vector hit is a pointer: no stable page, may be mid-argument truncated, cannot show surrounding qualification. Citation form: `⟨coat⟩ · nodo ⟨id⟩ · p. ⟨n⟩`.

This README is the **policy**. The provenance layer is the **worked proof** that the policy runs end-to-end on the temario resultants. See § Process below.

### Cross-project vaults (2026-08-13) — first entry, pattern borrowed from FE

FE's twin file (`web-atelier-udit/frontend-pedagogy/grounding/README.mdc`) has run a
"cross-project vaults" table since 2026-08-11 — MSCA sources usable here with labelled scope
rules, never duplicated as PDFs. This repo didn't have one yet; starting it now with the first
real case rather than as an empty template.

| Vault | Class | Use for | Never use for |
| --- | --- | --- | --- |
| `MSCA/SVCM/research/computational-authorship` — Göbels et al. 2026, *Aligning AI with human values: Design principles for human-centered AI* (Procedia CIRP, CIRP Design 2026) | Peer-reviewed, general HCI/AI-design principles | Framing AI-assisted design tooling in the CD curriculum as *responsible*, not just *productive* — the same design-principles register `dc-unit-forge.mdc` already asks for when a unit touches AI-assisted authoring | Any fashion/CD-domain-specific claim — the paper is general, not fashion or 3D-specific |

Extraction lives once, in MSCA's `computational-authorship` workstream — cite the node from
here, never copy the PDF into this repo's `pdfs/`.

### Keep the corpus searchable

```bash
cd ~/src/deviac
make health                    # stack must be green
make ingest-profield-dc        # Ahmes vaults → vectors (after batch extract)

# Cite-grade field index (separate from DevIAC ingest)
cd ~/src/athanor && source .venv/bin/activate && set -a && source .env && set +a
athanor inject --from-manifest \
  ~/src/profield/runs/digital-creativity/01/pdfs/.ahmes/batch-manifest.json \
  --project-slug profield-digital-creativity --vault scholar
```

Smoke:

```bash
curl -s -X POST http://localhost:8100/vectors/search \
  -H "Content-Type: application/json" \
  -d '{"query":"generative AI fashion studio education","project_slug":"profield-digital-creativity","knowledge_scope":"field_prospection","n_results":5}'
```

Meta coats are **not** required for MCP/HTTP discovery; ingest reads `extract/index.md` from each vault. Re-run ingest **and** Athanor inject when the Ahmes batch gains vaults (DevIAC alone leaves Athanor stale — see provenance demo inject 43 → 62).

FE pedagogy twin: `project_slug=profield-frontend-pedagogy`. MSCA twin: `vault=svcm`, slug `svcm-*`, scope opaque (e.g. `work_package`) — same CLI, different namespace (`/Users/ruvebal/src/athanor/docs/DEV_PLAN/PHASE-P6-REPORT.md`).

---

## Process — how the provenance layer was built (2026-08-11)

Not a second policy: a **session recipe** that operationalises this README against `temario/INDEX.md`.

| Step | Action | Tool |
| ---- | ------ | ---- |
| 0 | Confirm corpus coated / ingestable | Ahmes batch + `make athanor-ready-dc` (profield) |
| 1 | Refresh **DERIVED** discovery | `make ingest-profield-dc` |
| 2 | Sync **cite-grade index** to vault growth | `athanor inject --from-manifest …` (idempotent; skipped 43, injected 19) |
| 3 | One query per resultant strand (T1–T3 · C1–C3) | Theme phrase from resultant focus — not DOI scraping |
| 4 | Rank candidates | `athanor search` (primary) + DevIAC (corroboration only) |
| 5 | Resolve coat | `source_hash[:8]` → `~/ahmes-library/scholar/documents/*_<hash8>/` |
| 6 | Cite + quote | `ahmes query --cite "$DB:<node_id>"` + fission `markdown_content` (prefer body text over thin headings) |
| 7 | Optional ledger | `ahmes ground` with **library-relative** `scholar/documents/…/extraction.db:<node_id>` |
| 8 | Persist | `PROVENANCE-LAYER.json` + human `PROVENANCE-LAYER.md`; link from `temario/INDEX.md` |

**Honesty gates observed:** `[BIBLIO-GAP]` stays visible (T2); incomplete meta titles are not papered over; vector snippets never become lesson prose.

Full operator recipe + per-resultant table: [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md).

---

## Bounce path — provenance → CV forge → unit forge → lessons

```text
temario/*.pass1.resultant.mdc     claims + DOI/ISBN (bibliography intent)
        │
        ▼
PROVENANCE-LAYER.{md,json}        live Tri-Anchors proving vault coverage
        │
        ├─► grounding/README evidence matrix   (unit row = coat·node·page)
        │
        ├─► dc-cv-forge.mdc Step A/B           bibliografía + scholarly notes
        │         only SAFE / evaluator-safe cites in published CV
        │
        └─► dc-unit-forge.mdc Step A           lesson WHY grounded in nodes
                  └─► docs/lessons/{en,es}/…   student-facing; Tri-Anchor in research note
                      B1 conceptual / B2 studio / B3 exercises
```

| Forge gate | Uses provenance layer how |
| ---------- | ------------------------- |
| **Evidence matrix** (below) | Promote demo Tri-Anchors into unit rows when forging; else **NONE** + declared gap |
| **`dc-cv-forge`** | Temario resultants supply reading-list structure; Ahmes cites supply checkable bibliography lines; PENDING ISBN/DOI stay honest |
| **`dc-unit-forge` Step A** | Query must hit the same project; lesson claims copy **Ahmes quote + Tri-Anchor**, not JSON `content_preview` from DevIAC/Athanor |
| **Published Pages** | Never ship `digital-creativity-pedagogy/` or provenance JSON; only forged lesson prose that already resolved cites |

Until matrix rows exist, forges must treat units as **NONE**.

---

## Evidence matrix — fill before forging units

Rows are authored as units are forged ([`../dc-unit-forge.mdc`](../dc-unit-forge.mdc)). Seed candidates from [`temario/PROVENANCE-LAYER.md`](./temario/PROVENANCE-LAYER.md). Until a row exists, treat the unit as **NONE** and declare the gap.

| Course · Unit | CONTENIDOS anchor | Vault evidence | Authoring instruction |
| ------------- | ----------------- | -------------- | --------------------- |
| CD I · *(TBD)* | Forma 3D · Volumen | *pending — see T1 provenance hits* | Forge only after Step A query |
| CD II · *(TBD)* | Avatares · experiencias · portfolio · AR | *pending — see T3 / C2 hits* | Same; VTON stays out of scope |

**Rule:** if a lesson cites a layer, that layer must be reconstructable from this repo’s maps + Ahmes vaults. Curriculum may not cite grounding the teaching repo does not carry (maps) or the library does not hold (vaults).

---

## Improvements — skill / agent / MSCA twin

**Skill (generic):** `~/.cursor/skills/provenance-layer/` — field-agnostic harvest (`SKILL.md` + `profiles.md` + `scripts/harvest_provenance_layer.py`). Profiles: digital-creativity · frontend-pedagogy · msca-svcm.

| Gap | Improvement |
| --- | ----------- |
| Athanor lag after ingest | Makefile target: ingest → inject-if-stale → `harvest_provenance_layer.py` |
| Claim ↔ DOI mismatch | Second pass: for each resultant `doi:` / `isbn:`, search vault by identifier |
| Evidence matrix empty | After harvest: propose matrix rows; human accepts before forge |
| MSCA / SVCM | Use profile `msca-svcm` (`vault=svcm`); do not mix `scholar` coats into Part B without the SVCM ledger |

**Not recommended:** citing Athanor/DevIAC payloads; auto-filling CV bibliography from sim scores alone; collapsing MSCA `work_package` scope into `field_prospection`.
