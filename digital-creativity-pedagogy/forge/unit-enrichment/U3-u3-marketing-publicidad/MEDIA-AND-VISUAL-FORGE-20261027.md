# U3 media and visual forge receipt · 2026-10-27

## Media order for this and the next NM lessons

For each allocated campaign, search in this order: **campaign video** (official or credited source; embed only through its platform player) → **photo** (only with a source page and reuse/embedding permission recorded) → **course-generated semantic illustration**. If a tier has no verified item, record the gap and move to the next tier. A link to a video page is not proof that the video is embeddable; record the owner/platform setting and provide a readable link plus a text alternative. Never reuse a Profield campaign across units or imply that a supporting film documents a different event.

## Profield image API searches

Both searches used the Profield `media-prospect` API, vocabulary `U3` / `moda, campañas y publicidad en nuevos medios` / `campañas de marca, fashion films, comunicación activista, composición visual, encuadre, prueba e impacto`, `media_type=image`, `licence_actions=embed`, max 12, and `--no-llm`. Raw manifests were written to private temporary run folders, not the public lesson.

1. Initial broad query: `Benetton COLORS Oliviero Toscani campaign advertisement fashion activism archive campaign imagery`; providers Wikimedia Commons and Internet Archive. Result: **0 candidates, 2 provider errors** (DNS/network unavailable).
2. Refined archival query: `Oliviero Toscani United Colors Benetton COLORS magazine 1990s campaign photograph campaign still`; providers Wikimedia Commons, Library of Congress Pictures, and NYPL. Result: **0 candidates, 3 rejections** (Wikimedia and LOC network errors; NYPL token unavailable).

No campaign photo from either query was approved or shipped. Search failure is not a finding that no relevant images exist. Retry from an environment with provider access and credentials; inspect each rights statement individually.

## Verified example-link ledger

“Verified” here means that the destination page and its stated identity were checked on 2026-10-27; it does not mean that an asset licence or current embed setting was verified.

| Allocated U3 case | Video first | Photo / other source | Use limit |
| --- | --- | --- | --- |
| Benetton COLORS | [Vimeo: “We kiss in black”](https://vimeo.com/276410400) — page identifies Vertigo Barcelona and the Benetton Colors Man launch digital campaign. Embedded in lesson. | [Vogue profile](https://www.vogue.com/article/oliviero-toscani-united-colors-benetton); [Google Arts & Culture COLORS archive](https://artsandculture.google.com/story/colors-a-magazine-about-the-rest-of-the-world-torino-graphic-days/0AWBqnutdwqVIw). | Viewing/research links, not cleared image downloads. Vimeo owner controls whether external embedding is enabled and which domains are allowed. |
| Gualeguaychú × Botnia/UPM | No stable campaign/performance video verified. | [Global Nonviolent Action Database](https://nvdatabase.swarthmore.edu/content/argentines-protest-uruguayan-paper-mills-2005-2008); [El País Uruguay contemporary report](https://www.elpais.com.uy/informacion/carnaval-argentino-sera-dedicado-a-botnia). | Context links, not reusable campaign imagery; do not collapse activist performance and brand advertising into one evidence rubric. |
| Fashion to be Free | [Campaign film on YouTube](https://youtu.be/CbBOWHSrB0k) — contemporaneous report links this exact film; ADG-FAD archive confirms the case and credits. Embedded in lesson. | [ADG-FAD project archive](https://adg-fad.org/laus/proyecto/fashion-be-free/); [VEIN interview/report](https://vein.es/?p=16507). | The campaign's claims are the campaign's framing. Invite critique of who speaks, who is represented, and what a short film cannot establish. Transcript/captions not confirmed. |
| Ropa Limpia / SETEM × Inditex | [Al Borde Films project: “¿Sabes lo que es la ropa sucia?”](https://albordefilms.com/proyecto/sabes-lo-que-es-la-ropa-sucia/) — 2019 support film, **not** footage of the 2025 AGM. | [Ropa Limpia report on the shareholders’ meeting](https://ropalimpia.org/noticias/accionistas-y-entidades-sociales-exigen-responsabilidad-climatica-y-social-a-inditex-durante-la-junta-de-accionistas/); [economía solidaria mirror](https://www.economiasolidaria.org/noticias/exigen-a-inditex-responsabilidad-climatica-y-social-en-su-junta-de-accionistas/). | Keep the 2019 campaign support film distinct from evidence of the later AGM action. Direct player URL not verified; link to producer page only. |
| Jigsaw AW21 “Into the Woods” (supplemental) | No campaign film verified; this specific disputed placement was an email image. | [ASA ruling](https://www.asa.org.uk/rulings/robinson-webster--holdings--ltd-g21-1127608-robinson-webster--holdings--ltd.html); [production stills page](https://www.farmlocations.co.uk/work/jigsaw/). | ASA’s finding is limited to the September 2021 email image and its context. Do not republish campaign photos without separate rights clearance. |

## Course-generated visual assets

`artwork/01-message-metric-outcome.svg` maps a message to three distinct indicators and separates those indicators from independently evidenced effects. `artwork/02-campaign-forms.svg` gives each U3 case one critical question. Neither makes empirical claims about the campaigns or reproduces their photographs. Content-addressed SVG/PNG deliveries and `figcaption-data.json` are in `docs/assets/images/lesson-media/u3-campaign/`.

## Brief checklist for the graphic forger

Supply the communication purpose and student audience; the claim/evidence boundary; semantic role of each node, edge, shape, or motif; named Platonic solid and why its faces/vertices aid understanding (or state `geometry_only`); palette, contrast, crop, slide aspect ratio, and space for large type; labels and plain-language alt text; source SVG and rendered PNG; caption, authorship, date, content hash, and any mathematical formula/source. A minimal vegetal motif needs a semantic role (e.g. circulation or growth); otherwise omit it. A conventional polyhedron or custom diagram needs no separate plug-in: the existing visual-forger SVG/diagram path is adequate. Use the fractal-architect only for a recursive/generative structure, with its seed and parameter envelope recorded.

## Embed conditions and text alternatives

Lesson embeds use the repository’s Vimeo and privacy-enhanced YouTube includes, lazy-loaded with descriptive titles. The platform page for a video is verified; owner settings may still disable or domain-restrict Vimeo embedding. The lesson links to each original page and says that a transcript/caption alternative was not confirmed. Recheck the live lesson player and add an accurate transcript or caption file before describing either video as fully accessible.

## Archive-image pass (2026-10-27, second session)

**Source.** No NM or U3 asset is accepted in the Profield review state, and the NM1–NM7 manifests return only PDFs. Candidates were therefore taken from the Profield discovery indexes (`media-index-review.json`, `media-index-fashlex-i1-20260910.json`, `media-index-tc-expanded-20260911.json`), filtered for advertising, poster, catalogue, magazine and protest imagery, then checked one by one against the Commons API (extmetadata + file-page licence template) and Wikidata death years. None is campaign imagery for an allocated U3 case: each is a historical or contextual analogue, and every deck prompt and lesson caption says so (“Fondo: … — no es …”).

| Slot | Asset | Author (d.) | Licence | EU term |
| --- | --- | --- | --- | --- |
| U3.cover | Advertising campaign womenswear.jpg | Devid Campani | CC BY-SA 3.0 (own work) | holder licence |
| U3.masterclass-1 | Johannes Handschin – Pelz Jackets, Lindner Pelze (1929) | Handschin (1948) | PD-old-70 | 1948+70 < 2026 |
| U3.masterclass-2 | Philadelphia Sunday Press poster, 10 May 1895 (MET DP866320) | George Reiter Brill (1918) | CC0 (MET Open Access) | also expired |
| U3.masterclass-4 | Cover of Fashion Street Magazine SS 2019 | FashionStreet.hu | CC BY-SA 4.0, VRT ticket 2019071210004498 | holder licence |
| U3.masterclass-5 | Ende Gelände Nov 2017 front banner | Leonhard Lenz | CC0 | holder dedication |
| U3.masterclass-6 | Regate et chapeau à plumes (1895) | Auguste Donnay (1921) | PD-old-70 | 1921+70 < 2026 |
| U3.lab-1 | Illustrated fashion catalogue, summer 1890 (14781648884) | Bloomingdale Bros. (anonymous corporate) | PD-EU | 70 years from 1890 publication |
| U3.lab-2 | Faragó, Géza – Holzer Fashion Store poster (1902) | Faragó (1928) | PD-old-70 | 1928+70 < 2026 |

**Rejected.** 1965 Hess Brothers window displays (anonymous, published 1965: EU term runs to 2035; source is a Facebook page); Manifestación contra la Troika (CC BY 2.0 is not on the whitelist); Giada SS11/FW09 (brand upload credited to named photographers, no permission ticket); Lautrec's Sescau poster and *The Designer* July 1922 cover (already registered for CD I decks with English alt text — a shared record would give the Spanish deck English alt or the English decks Spanish alt); news-kiosk photo (2025, prominent third-party magazine covers; its file is also used by another deck); Country Gentleman 1928 cover (illustrator's death year unknown).

**Pipeline.** Renditions made with ImageMagick (`sharp` absent): longest side ≤ 1920 px, WebP q75, metadata stripped, 84–302 KB, named `sha256(asset_id)[:16].webp`. Registry: eight new `autopilot-assets.json` records, assignment `nm/U3`, Spanish alt text, curator notes for the dealer watermark (Handschin), identifiable people (Campani, Fashion Street) and the low-resolution Faragó scan. Deck migrated to `schema_version: 2` (stable slide ids, `locale: es`, slide-bound `asset_id` + `image_brief`) and bound with `DECK_ROOTS=…/u3-marketing-publicidad node scripts/rehydrate-student-media.mjs --rights=flag` (8 bound, all `rights_status: ok`, 0 orphans removed). `render-decks.mjs` and the rehydrator's default roots now include `docs/tracks/es/uem/2627-nm`, so the deck is pre-rendered (key-word marks now render) and `lesson_figures.json` feeds the lesson captions. Lesson: eight figures with a “why / look for” lead plus the deck caption (title · author · licence · source).

**Still open.** Allocated-campaign photographs remain uncleared; the naturalistic course photograph is still pending; caption “Source” label is English in the shared caption helper.
