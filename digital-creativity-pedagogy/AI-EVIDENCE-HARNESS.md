# AI curriculum evidence harness

## Purpose and authority

This harness turns a field prospect into a publishable curriculum change without
letting an LLM, a vector search result, or a copied research UI become citation
authority.

`profield` is the reproducible evidence-and-operations factory. The canonical,
mutable publication heads are:

- FE: `/Users/ruvebal/projects/ruvebal/scholar/udit/web-atelier-udit/frontend-pedagogy`
- DC: `/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem/digital-creativity-pedagogy`

After an artifact passes the gate, author CV, forge, and student-facing edits in
the appropriate publication head. Keep the originating Profield run immutable
except for run receipts, retrieval metadata, and audit records. Until these
roots have Git histories, `grounding/PROFIELD-SYNC.json` is the publication
receipt; it records source run, hashes, evidence status, and the human release
decision.

## Layered pipeline

| Gate | Owner | Output | Cannot decide |
| --- | --- | --- | --- |
| Prospect | FieldSpec + researcher | field/run prompt and scope | source truth |
| Map | Deep Research / researcher | `pass1.raw.md` | bibliographic correctness |
| Registry | deterministic adapters | DOI, ISBN, arXiv resolution ledger | pedagogical meaning |
| Audit | Claude plus local critic | per-field audit + edit ledger | final citation authority |
| Retrieve | Unpaywall/OpenAlex/manual lawful acquisition | checksummed PDFs + rights status | claim entailment |
| Extract | Ahmes | page-addressable extraction DB and metadata coats | broad relevance |
| Discover | Athanor / DevIAC / Tanit | scoped candidate nodes | citable evidence |
| Cite gate | Ahmes + human | `evaluator_safe=yes` node/page citations | unresolved claims |
| Forge | curriculum owner | provenance-grounded CV/lesson change | automatic publication |
| Publish | curriculum root | sync receipt and content change | retrospective evidence repair |

## Agent roles

1. **Identifier sentinel (deterministic first).** Normalize DOI, ISBN-10/13,
   arXiv ID, URL and title/author/year. Resolve DOI with Crossref/DataCite,
   ISBN with Open Library/publisher metadata, arXiv with its API. Emit a JSONL
   receipt containing query, response identifier, match score, mismatch reason,
   timestamp and source URL. Ambiguous results are `needs_human`; an LLM never
   promotes them.
2. **Local critic (Ollama).** Use `thessia-scholar-v3` or Qwen for bounded JSON
   classification: duplicate candidates, malformed citations, title/host/year
   mismatch, rendered capture noise, tag drift, and candidate routing. It may
   propose patches but cannot mark a source verified or evaluator-safe.
3. **Independent semantic auditor (Claude).** Audit each uniquely named field
   artifact for claim scope, evidence-transfer mistakes, unsupported prose,
   vocabulary drift and lesson-readiness. It complements, rather than replaces,
   registry checks: deterministic checks answer “is this record real?”; the
   audit asks “does this source support this curriculum claim?”.
4. **Evidence authority (Ahmes).** Resolve every citation to its extraction DB,
   complete node context and page. Only `evaluator_safe=yes` may become settled
   curriculum evidence. Retain failures as `[BIBLIO-GAP]` with a resolver
   reason.
5. **Publisher (human + curriculum root).** Applies approved amendments and
   creates `PROFIELD-SYNC.json`. No autonomous overwrite of CV or lesson prose.

## Non-negotiable controls

- Vector/RAG hits are discovery only. Never cite Athanor/DevIAC snippets.
- Graph MCP is a walker only when the corpus was actually relation-enriched.
  A Didactics corpus ingested without `--enrich-relations` should return an
  honest empty relation set; use mentions/co-naming/co-occurrence as the
  conversation signal instead. Relation-heavy coats, such as Agre's 218
  relations, are the opposite case: use Graph MCP to walk the graph, then follow
  each hit back to its vault/node before it can ground a claim.
- Never use UI capture text such as `turn...search...`, publisher chips, or
  broken headers as references. Preserve a raw capture, then remove the noise
  only in `pass1.edited.md` with a ledger.
- A source may be relevant to several fields but has one canonical ingest copy.
  Route through existing project slugs; create a new category only when the
  corpus-routing law in `profield-corpus-pipeline` is satisfied and recorded.
- Do not send `.env`, API keys, local extraction databases, or secrets to cloud
  models. A cloud pass transmits only the deliberately attached prompt/artifact
  under that service account. Local Ahmes/Athanor/DevIAC/Ollama processing does
  not consume cloud-model tokens.
- An audit is not an external fact-check. A Claude audit must state whether
  FieldSpec and registry checks were supplied; missing inputs remain blocking
  conditions, not inferred compliance.

## Publication gate

An item is ready to promote only when all applicable checks are recorded:

- FieldSpec areas (not keyword count) are mapped.
- Raw capture, audited edit ledger, and per-field `pass3.notes.md` exist.
- Identifier status is `resolved`, `not_applicable`, or explicit `[BIBLIO-GAP]`.
- Retrieved source has a manifest/checksum and lawful access status.
- Citation claims resolve to Ahmes nodes/pages and are `evaluator_safe=yes`.
- Provenance labels survive into the forge: HE evidence, practitioner evidence,
  platform/vendor documentation, and evidence gaps must not be flattened.
- A content owner approves the curriculum-root change and signs the sync receipt.

## Vocabulary: lexicum versus thesaurus

The existing `grounding/lexicum.yaml` files are controlled vocabularies /
lexica: they classify durable and frontier terms. They are not yet a full
thesaurus. Promote them incrementally to a SKOS-like thesaurus only when useful:
stable concept IDs, preferred and alternative labels, Spanish/English labels,
scope notes, `broader`/`narrower`/`related` relations, source/provenance, and
last-validation date. Do not introduce synonym expansion into retrieval until
the term relation is explicitly reviewed.

## Operating sequence

`prospect → map → registry ledger → audit → edit ledger → retrieve → RIS →
extract → coat → ingest → cite gate → forge → human publish receipt`

For background work, queue durable jobs in the database/ledger with idempotency
keys (field, source hash, operation, version), retries and state transitions.
Do not rely on an untracked terminal background process as the source of truth.
