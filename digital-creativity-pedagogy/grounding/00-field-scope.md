<!--
AUTHORITY HOME — digital-creativity-uem
Canonical for Creación Digital teaching/research once emancipated.
Upstream profield path: /Users/ruvebal/src/profield/runs/digital-creativity/
Synced: 2026-08-10 · file: 00-field-scope.md
Re-sync: copy from profield over this file and restore this banner.
PDFs / Ahmes extractions stay in the Ahmes library + profield/pdfs — not duplicated here.
-->

# Field scope — Digital Creativity

_Operator-local scoping note. Not exportable; do not paste into external research surfaces.
Derived from public curricular descriptions of Creación Digital I / II (Fashion Communication
& Management, 2025–2026), without naming internal systems or institutions in FieldSpec
keywords._

## Field definition

**Digital Creativity** (as prospected here) is the research and practice field concerned with
how fashion communication produces, transforms, and circulates visual–audiovisual meaning
through digital tools. It is not “software training” alone, and not general CS creativity
studies alone. Its object is the **creative media stack for fashion brands**: still image →
motion → virtual body/garment → immersive experience → publishable portfolio/web identity.

### Durable core (fundamentals)

From Creación Digital I and the durable half of II:

- digital image literacy (bitmap/vector, colour, effects)
- photographic retouching for fashion images
- 2D animation / animated digital imagery
- fundamentals of 3D form and volume representation
- compositional references for fashion design
- brand-image and audiovisual communication competence

### Volatile frontier (cutting edge)

From Creación Digital II and the 2024–2026 literature horizon:

- digital fashion avatars and virtual garment systems
- digital fashion experiences and content diffusion
- video editing as fashion storytelling
- web / digital portfolio as brand surface
- holograms and augmented reality in fashion presentation
- generative AI as studio collaborator (authorship, ethics, TPACK)

## Curricular anchors (private mapping)

| Unit | Emphasis |
|------|----------|
| Creación Digital I | Digital images, photo retouch, 2D animation, 3D form basics, digital still lifes |
| Creación Digital II | Advanced fashion retouch, avatars, digital fashion experiences, video, web/portfolio, holograms & AR |

Shared competencies (paraphrased): differentiate audiovisual techniques for fashion ideas;
professional digital treatment of image/text/sound; brand-image design; digital
graphic/audiovisual tools for fashion communication; originality under constraint.

## Profield artifacts

- FieldSpec: `fields/digital-creativity.yaml`
- Pass 1 prompt: `runs/digital-creativity/01/pass1.prompt.md`
- Pass 3 checklist: `runs/digital-creativity/01/pass3.prompt.md` (fills after Pass 1/2 ingest)
- Pass 2 requires a Pass-1 reply (`pass1.raw.md`) from a *different* external surface

## Operator rhythm

```bash
cd /Users/ruvebal/src/profield && source .venv/bin/activate
RUN=runs/digital-creativity/01

# 1) Map (external surface A)
# paste pass1.prompt.md → save reply as $RUN/pass1.raw.md
profield ingest pass1 fields/digital-creativity.yaml \
  --from "$RUN/pass1.raw.md" --surface "external-model-a" --run "$RUN"

# 2) Audit (external surface B — different model)
profield prompt pass2 fields/digital-creativity.yaml \
  --prior "$RUN/pass1.raw.md" -o "$RUN/pass2.prompt.md"
# paste → $RUN/pass2.raw.md
profield ingest pass2 fields/digital-creativity.yaml \
  --from "$RUN/pass2.raw.md" --surface "external-model-b" --run "$RUN"

# 3) Tool-verify unresolved citations locally
profield prompt pass3 fields/digital-creativity.yaml -o "$RUN/pass3.prompt.md"
# work the checklist → $RUN/pass3.notes.md
profield ingest pass3 fields/digital-creativity.yaml \
  --from "$RUN/pass3.notes.md" --surface "manual-verify" --run "$RUN"

profield digest fields/digital-creativity.yaml --run "$RUN"
profield lexicum fields/digital-creativity.yaml --run "$RUN"
profield retrieve fields/digital-creativity.yaml --run "$RUN" --email you@example.com
```
