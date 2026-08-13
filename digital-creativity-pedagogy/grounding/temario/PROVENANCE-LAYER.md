# Temario provenance layer — worked demo

- **Date:** 2026-08-11
- **Field:** Digital Creativity (UEM) · Profield run `digital-creativity`
- **Project slug:** `profield-digital-creativity`
- **Vault:** `scholar`
- **Scope:** `field_prospection`
- **Athanor SoTA:** `/Users/ruvebal/src/athanor/docs/DEV_PLAN/PHASE-P6-REPORT.md` (agnostic inject/search; same CLI contract)
- **Policy home:** [`../README.md`](../README.md) (retrieval vs citation + bounce to forge)
- **Machine JSON:** [`PROVENANCE-LAYER.json`](PROVENANCE-LAYER.json)

> This file is a **session artefact**, not a second policy. Durable rules live in [`../README.md`](../README.md). Process table and forge bounce path are documented there (§ Process · § Bounce path). Cross-field re-runs: Cursor skill `provenance-layer` (`~/.cursor/skills/provenance-layer/`, profile `digital-creativity`).

## Contract (do not collapse)

| Layer | Tool | Role |
| ----- | ---- | ---- |
| **Discovery (derived)** | DevIAC vectors `POST /vectors/search` | Find candidates — **never cite** |
| **Field search (cite-grade index)** | `athanor search … --project-slug profield-digital-creativity --vault scholar` | Rank fission nodes already injected from Ahmes coats |
| **Evidence** | Ahmes `extraction.db` + `ahmes query --cite` + optional `ahmes ground` | Page-anchored quote + CitationKey + provenance ledger |

> Tri-anchor label: `⟨coat_slug⟩ · nodo · p.` — the only form allowed in guías / lessons.

## Inject state (this session)

After DevIAC ingest (62 ok), Athanor still had **43** docs from the earlier P5/P6 inject. Re-ran:

```bash
cd ~/src/athanor && source .venv/bin/activate && set -a && source .env && set +a
athanor inject --from-manifest \
  ~/src/profield/runs/digital-creativity/01/pdfs/.ahmes/batch-manifest.json \
  --project-slug profield-digital-creativity --vault scholar
# summary: injected 19 · skipped_noop 43 · twin 1 · failed 0
# inventory: 62 docs / 19 390 nodes
```

## Operator recipe (one resultant claim)

```bash
# 0) env
cd ~/src/athanor && source .venv/bin/activate && set -a && source .env && set +a
cd ~/src/ahmes && source .venv/bin/activate

# 1) Discover (DERIVED — do not paste into syllabus)
curl -s -X POST http://localhost:8100/vectors/search \
  -H 'Content-Type: application/json' \
  -d '{"query":"…","project_slug":"profield-digital-creativity","knowledge_scope":"field_prospection","n_results":5}'

# 2) Field search (cite-grade index)
athanor search "…" --project-slug profield-digital-creativity --vault scholar --top-k 5
# → metadata.node_id, source_hash, page_index, file_name

# 3) Resolve coat by source_hash[:8]
DB=~/ahmes-library/scholar/documents/*_<hash8>/extract/extraction.db

# 4) Cite + quote from Ahmes (authoritative)
ahmes query --cite "$DB:<node_id>" --style chicago-author-date
ahmes query "$DB" --nodes -p <page_index>

# 5) Optional: ledger a paraphrase/synthesis (not the discovery snippet)
ahmes ground --library ~/ahmes-library \
  --content "…" --model composer --span-type paraphrase \
  --cites scholar/documents/<slug>/extract/extraction.db:<node_id>
```

## Per-resultant matches

Each block: **query → Athanor top → Ahmes cite/quote**. DevIAC listed as corroborating discovery only.

### T1 · `T1-image-2d-volume.pass1.resultant.mdc` (Technique)

**Query:** `volumetric imaging 2D fashion photography spatial volume digital image`

| | |
| --- | --- |
| Athanor #1 sim | **0.7208** |
| Document | Fashion as Photograph |
| File | `Eugenie Shinkle - Fashion as Photograph_ Viewing and Reviewing Images of Fashion (2008, I. B. Tauris).pdf` |
| Discovery node | `01d38c38-3d8a-5d56-9040-fec3d7781c90` · p.`3` |
| Coat | `eugenie_shinkle_fashion_as_photograph_viewing_and_reviewing_images_of_fashion_2008_i_b_tauris_1936070c` |
| Tri-anchor (quote surface) | `⟨eugenie_shinkle_fashion_as_photograph_viewing_and_reviewing_images_of_fashion_2008_i_b_tauris_1936070c⟩ · nodo c1cb2f51… · p.248` |
| Ahmes `--cite` | `(Shinkle 2008, 249)  [c1cb2f51-674b-54f7-9b26-8f72ed572988]  page_index=248` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> | Hudson, Kate 128                                                               | Kidman, Nicole 128, 138                                        | |--------------------------------------------------------------------------------|----------------------------------------------------------------| | Hutcheon, Linda 13                                                             | Kismaric, Susan 6-7, 29-45 , 228 Klein, Calvin 132, 137, 207   | | i-D magazine 8, 11, 33, 36, 52, 91, 102, 106, 189, 190…

**DevIAC (derived only):** sim `0.6697` · `ahmes/10_3389_fpsyg_2023_1276856_virtual_fashion_experiences_in_virtual_reality_fashion_show_ddb20bc5/index.md`

### T2 · `T2-retouch-video-portfolio.pass1.resultant.mdc` (Technique)

**Query:** `fashion retouching photo editing social media self-perceived attractiveness`

| | |
| --- | --- |
| Athanor #1 sim | **0.8935** |
| Document | Open Access |
| File | `s40359-023-01143-0.pdf` |
| Discovery node | `af07aa72-4ab5-5607-96e6-6406cce96453` · p.`0` |
| Coat | `10_1186_s40359_023_01143_0_how_photo_editing_in_social_media_shapes_self_perceived_attr_4abbe095` |
| Tri-anchor (quote surface) | `⟨10_1186_s40359_023_01143_0_how_photo_editing_in_social_media_shapes_self_perceived_attr_4abbe095⟩ · nodo e97327cd… · p.1` |
| Ahmes `--cite` | `[BIBLIO-GAP] e97327cd-ef56-5806-8ddd-ef03c418c658` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> Photo  editing  behavior  increases  the  options  available  for  self-presentation  on  social  network  sites  and constitutes a significant restriction on verifiability of the accuracy of profile photos. In addition, it is likely to be negatively  correlated  with  self-perceived  attractiveness. Therefore,  the  importance  of  photo  editing  behavior  in the context of social network sites is high.

**DevIAC (derived only):** sim `0.8426` · `ahmes/10_1186_s40359_023_01143_0_how_photo_editing_in_social_media_shapes_self_perceived_attr_4abbe095/index.md`

> **Honesty:** Ahmes returned `[BIBLIO-GAP]` — node is quoteable; bibliographic coat is incomplete. Re-run `make athanor-ready-dc` / `profield-meta-enrich` before CV forge cites this coat as SAFE.

### T3 · `T3-avatars-experiences-ar.pass1.resultant.mdc` (Technique)

**Query:** `avatars augmented reality virtual try-on fashion immersive experience`

| | |
| --- | --- |
| Athanor #1 sim | **0.8571** |
| Document | VR Designer: enhancing fashion showcases through immersive virtual garment fitting |
| File | `10.1007_s10055-024-00945-w__VR_Designer_enhancing_fashion_showcases_through_immersive_vi.pdf` |
| Discovery node | `04f04672-8886-5038-818b-1258db617409` · p.`0` |
| Coat | `10_1007_s10055_024_00945_w_vr_designer_enhancing_fashion_showcases_through_immersive_vi_d3d4e2e6` |
| Tri-anchor (quote surface) | `⟨10_1007_s10055_024_00945_w_vr_designer_enhancing_fashion_showcases_through_immersive_vi_d3d4e2e6⟩ · nodo 54d6cfa5… · p.15` |
| Ahmes `--cite` | `(Hafliger 2024, 16)  [54d6cfa5-86bd-5684-b01a-a4fb29aa63e7]  page_index=15` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> Sarakatsanos O, Chatzilari E, Nikolopoulos S, Kompatsiaris I, Gavilan D, Downing J (2021) A vr application for the virtual fitting of fashion garments on avatars. In 2021 IEEE international symposium on mixed and augmented reality adjunct (ISMAR-Adjunct)

**DevIAC (derived only):** sim `0.8474` · `ahmes/10_1007_s10055_024_00945_w_vr_designer_enhancing_fashion_showcases_through_immersive_vi_d3d4e2e6/index.md`

### C1 · `C1-fashion-digital-world.pass1.resultant.mdc` (Critical)

**Query:** `platformisation fashion digital capitalism mediatization brand culture`

| | |
| --- | --- |
| Athanor #1 sim | **0.7739** |
| Document | Towards a Responsible Metaverse |
| File | `10.1515_9783839474624-013.pdf` |
| Discovery node | `c8036241-1991-55bc-b0c4-acde6fbbb3ea` · p.`2` |
| Coat | `10_1515_9783839474624_013_2ebbda3a` |
| Tri-anchor (quote surface) | `⟨10_1515_9783839474624_013_2ebbda3a⟩ · nodo c8036241… · p.2` |
| Ahmes `--cite` | `(10.1515 9783, 3)  [c8036241-1991-55bc-b0c4-acde6fbbb3ea]  page_index=2` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> Digital fashion opens us up to new ways of being and forms of embodiment. The construction of our avatars is a kind of digital cosplay that relates to performance and dress-up, as well as the construction of a virtual identity overall. Aesthetics, social, technical, and economic worlds come together here. 7 However, this datafication and monetization of our identity and assets is also problematic. It is intimately connected to platformization, or 'the rise of the platform as the dominant infrast…

**DevIAC (derived only):** sim `0.7612` · `ahmes/978_3_031_99481_4_72e535d7/index.md`

### C2 · `C2-fashion-virtuality.pass1.resultant.mdc` (Critical)

**Query:** `digital fashion virtuality metaverse identity virtual worlds avatars`

| | |
| --- | --- |
| Athanor #1 sim | **0.9007** |
| Document | Towards a Responsible Metaverse |
| File | `10.1515_9783839474624-013.pdf` |
| Discovery node | `56b6e6c2-3d0e-5a67-b97d-03e119b453bf` · p.`0` |
| Coat | `10_1515_9783839474624_013_2ebbda3a` |
| Tri-anchor (quote surface) | `⟨10_1515_9783839474624_013_2ebbda3a⟩ · nodo 769eaad4… · p.4` |
| Ahmes `--cite` | `(10.1515 9783, 5)  [769eaad4-8271-5232-bcd3-2fccaf837c72]  page_index=4` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> Finally, digital fashion can be tokenized and certified on a blockchain. Since digital fashion is usually unique and scarce, the tokens used are often NFTs. They are essentially unique digital items certified on the blockchain. 'Non-fungible' means that these items are unique, cannot be interchanged, and can't be replaced. The NFT itself is best understood as its history and proof of ownership, which is stored on a blockchain, such as Ethereum. NFTs are tokens that are different from cryptocurre…

**DevIAC (derived only):** sim `0.7846` · `ahmes/978_3_031_99481_4_72e535d7/index.md`

### C3 · `C3-gender-minorities-silences.pass1.resultant.mdc` (Critical)

**Query:** `gender minorities fat bodies digital screens fashion representation silence`

| | |
| --- | --- |
| Athanor #1 sim | **0.715** |
| Document | Corpos gordos e corpos obesos em telas digitais: um  olhar  analítico  para  imagens  propagadas pelo Google |
| File | `Campinho_et_al_corpos_gordos_telas_digitais_2025.pdf` |
| Discovery node | `5d8af160-80f8-5b60-a1b2-effe3189d7e9` · p.`0` |
| Coat | `campinho_et_al_corpos_gordos_telas_digitais_2025_31a9a359` |
| Tri-anchor (quote surface) | `⟨campinho_et_al_corpos_gordos_telas_digitais_2025_31a9a359⟩ · nodo 29e0b3cf… · p.1` |
| Ahmes `--cite` | `(Campinho_et_al_corpos_gordos_telas_digitais 2025, 2)  [29e0b3cf-bd30-5373-bfbe-d208de8c3a3b]  page_index=1` |

**Quote (Ahmes fission text — not the DevIAC chunk):**

> The associations between body and image in terms of image production take on immeasurable contours in  digital  media,  reinforcing  the  visuality  of  the body in our scenario. This article aims to study the image production of fat bodies and obese bodies on Google  images,  considering  the  similarity  of  such corporealities  in  the  sociocultural  imaginary.  This is  a  qualitative,  exploratory  study  carried  out  on the Google platform, with reflection inspired by the method of semio…

**DevIAC (derived only):** sim `0.6124` · `ahmes/10_1007_s10728_016_0327_1_altered_images_understanding_the_influence_of_unrealistic_im_984f4f11/index.md`

## Grounding ledger demo (C2)

Recorded a paraphrase span citing the C2 coat (library-relative `source_db`):

```text
generated_span: 975b8dc9-8bb7-5e31-aa01-b18b0fd31244
provenance.db: ~/ahmes-library/provenance.db
role: cited · span_type: paraphrase · model: composer-demo-provenance
```

Inspect:

```bash
ahmes query --library ~/ahmes-library --span-provenance 975b8dc9-8bb7-5e31-aa01-b18b0fd31244
```

## What this proves for temario → lesson forge

1. Every INDEX resultant strand has **live Athanor hits** in the DC project (sim ≈ 0.72–0.90).
2. Those hits resolve to **Ahmes coats** via `source_hash` → Tri-Anchor.
3. DevIAC agrees directionally but stays **DERIVED** (`authority_level=derived`).
4. Inject must track Ahmes vault growth (43 → **62** this session) or field search lags discovery.
5. `[BIBLIO-GAP]` and weak metadata titles (e.g. T2 “Open Access”) are **features of honesty**, not search failure — still quote from fission text; fix coats before publishing citations in guías.

