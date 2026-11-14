# Technical Research Report

## Human Construction of Volume Perception and the Representation of Depth in Two-Dimensional Images

### From Classical Optics to Computational Vision

**Status:** instructor-side creation-led research framework (not student HTML; not published on Pages).  
**Feeds:** CD I units **I.5** (forma tridimensional) · **I.6** (volumen) · perspective/volume image kit · drawing→volume bridge in I.2.  
**URL rule:** links below were HTTP-checked 2026-11-13 from this studio; **P2 OK** = 200 (or JoVE 202). Do not promote Wikipedia/secondary pages or Commons candidates into evaluator-safe lesson citations until Ahmes nodes resolve — discover elsewhere, cite vaults. Image leads remain `needs_human_review` until `media-accept`.

Prepared as a creation-led research framework for undergraduate students in Design, Visual Communication, Art, Illustration, Animation, Photography, and Digital Media.

**Profield image research (triggered 2026-11-13):** Wikimedia-only `media-prospect` runs under `~/src/profield/runs/media-prospector/` — I.5: `20261113-perspective-vanishing`, `20261113-aerial-perspective`, `20261113-alberti-perspective`, `20261113-texture-gradient`, `20261113-foreshortening`, `20261113-projection-matrix`; I.6: `20261113-visual-cliff` (0 assets), `20261113-occlusion` (0 assets). Broad book-PDF noise is common; prefer Wikipedia article lead images + diagram Files listed in-section.

---

## Executive Summary

A fundamental paradox underlies all image-making:

The retina receives a two-dimensional projection of light, yet humans experience a stable three-dimensional world.

Every representational system in art, architecture, photography, cinema, virtual reality, and computer graphics attempts to exploit the mechanisms through which the visual system reconstructs depth from incomplete information.

The history of perspective may therefore be understood not merely as a history of drawing techniques, but as a history of hypotheses about human perception.

This study traces that problem from Classical Greek optics through Renaissance perspective, nineteenth-century physiological optics, twentieth-century perceptual psychology, and contemporary computational imaging. The line from Euclid's visual-ray geometry to Alberti's picture plane, from Helmholtz's unconscious inference to Marr's computational vision, and on to digital rendering engines is one continuous attempt to explain how flat images can generate convincing experiences of volumetric space.

**Orientation (P2 OK):** [Depth perception (Wikipedia)](https://en.wikipedia.org/wiki/Depth_perception) · [Perspective (graphical)](https://en.wikipedia.org/wiki/Perspective_(graphical)) · overview diagram [File:Depth cues 1.png](https://commons.wikimedia.org/wiki/File:Depth_cues_1.png) (CC BY-SA 3.0; Profield `conforming_sharealike`, still needs human review).

---

## 1. The Epistemological Problem of Spatial Vision

Light reflected by the environment forms a two-dimensional retinal projection. Phenomenologically, observers experience depth relations, volumetric objects, distances, occlusions, and stable spatial structures.

Formulated as a foundational problem:

> How does the visual system recover three-dimensional structure from two-dimensional retinal stimulation?

Modern neuroscience treats this as an **inverse problem**: multiple external realities may generate identical retinal projections. Perception cannot be mere image registration; it must involve interpretation, inference, prediction, or ecological information detection.

The retinal image is bidimensional, inverted, and continuously changing — yet humans perceive volume, distance, scale, spatial continuity, and object permanence. Every representational medium (painting, architecture, photography, cinema, VR, games, scientific visualization, generative AI) depends on assumptions about how observers derive depth from visual stimuli.

**Verified reading:** [Depth Perception (PsychWeb)](https://www.psywww.com/intropsych/ch04-senses/depth-perception.html) · **P2 OK** · JoVE education clip [Depth Perception and Spatial Vision](https://www.jove.com/science-education/v/17768/depth-perception-and-spatial-vision) · **P2 soft** (HTTP 202).

---

## 2. Classical Foundations: Euclid and the Geometry of Seeing

The earliest systematic treatment of vision in the Hellenistic tradition is Euclid's *Optica*.

Although historically superseded as a physiological theory, the text established a geometric conception of vision. Euclid modeled perception through visual rays extending from the observer toward objects. Size, distance, and spatial relationships became geometrical problems rather than purely philosophical questions.

Principles that survived for nearly two millennia:

- Visual space can be modeled mathematically.
- Apparent size varies with distance.
- Observation is structured through lines of sight.
- Spatial representation may be formalized geometrically.

These assumptions later underpin Renaissance perspective and, ultimately, the projective geometry of computer graphics.

**Image / concept bridge (P2 OK):** one-point construction [File:1ptPerspective.svg](https://commons.wikimedia.org/wiki/File:1ptPerspective.svg) · comparison of projections [File:Comparison of graphical projections.svg](https://commons.wikimedia.org/wiki/File:Comparison_of_graphical_projections.svg) (also lead image on [3D projection](https://en.wikipedia.org/wiki/3D_projection)).

---

## 3. Classical Theories of Depth Perception

### 3.1 Hermann von Helmholtz (1821–1894) — Unconscious Inference

Helmholtz argued that vision is not passive reception but active interpretation. The visual system effectively performs unconscious hypotheses about the external world: depth emerges because the observer has learned statistical regularities connecting retinal patterns and environmental structures.

> The brain infers three-dimensional reality from ambiguous visual information.

**Relevance for artists.** A successful image need not reproduce reality itself. It must activate inferential processes that normally produce perceptions of depth, volume, and spatial coherence. Many optical illusions demonstrate precisely this principle.

**Verified:** [Hermann von Helmholtz (Wikipedia)](https://en.wikipedia.org/wiki/Hermann_von_Helmholtz) · **P2 OK** · [Visual perception theories (SimplyPsychology)](https://www.simplypsychology.org/perception-theories.html) · **P2 OK**.

### 3.2 James J. Gibson (1904–1979) — Ecological Optics

Gibson rejected the idea that perception is primarily inferential. He argued that information sufficient for perception already exists in the optic array; observers detect invariant structures rather than constructing hypothetical interpretations.

Important Gibsonian concepts: texture gradients, optical flow, affordances, invariants, horizon relationships, motion parallax.

These became highly influential in visual design, robotics, UX, computer vision, and VR research. Contemporary “immersive environments” owe much to ecological emphasis on active movement through space.

**Verified:** [James J. Gibson (Wikipedia)](https://en.wikipedia.org/wiki/James_J._Gibson) · **P2 OK** · [Visual cliff](https://en.wikipedia.org/wiki/Visual_cliff) · **P2 OK** · SimplyPsychology [Visual Cliff Experiment](https://www.simplypsychology.org/visual-cliff-experiment.html) · **P2 OK**.  
**Wikimedia lead:** [File:NIH visual cliff experiment (cropped).png](https://commons.wikimedia.org/wiki/File:NIH_visual_cliff_experiment_(cropped).png) · **P2 OK** (Profield I.6 visual-cliff search returned 0 assets — use this Wikipedia lead instead).  
**Optical flow:** [Optical flow (Wikipedia)](https://en.wikipedia.org/wiki/Optical_flow) · **P2 OK** · [File:Opticfloweg.png](https://commons.wikimedia.org/wiki/File:Opticfloweg.png) · [File:Optical flow example v2.png](https://commons.wikimedia.org/wiki/File:Optical_flow_example_v2.png) · **P2 OK**.

### 3.3 David Marr — The Computational Turn (*Vision*, 1982)

Marr proposed that vision must be analyzed at three levels:

| Level | Question |
| --- | --- |
| **Computational** | What problem is being solved? |
| **Algorithmic** | What procedures solve it? |
| **Implementational** | How is it physically realized? |

For Marr, perception constructs increasingly sophisticated representations: **primal sketch** → **2.5D sketch** → **three-dimensional model**. Modern depth estimation, neural rendering, and photogrammetric pipelines reproduce operations analogous to that hierarchy. The framework remains fundamental in AI, neuroscience, and computer vision.

**Verified:** [David Marr (neuroscientist)](https://en.wikipedia.org/wiki/David_Marr_(neuroscientist)) · **P2 OK**.

---

## 4. Depth Cues Used by the Human Visual System

### A. Binocular cues

1. **Retinal disparity** — Horizontally separated eyes receive slightly different images; the brain derives depth (stereopsis).
2. **Convergence** — Near objects drive inward eye-muscle rotation; muscular information contributes to depth judgement.

### B. Monocular (pictorial) cues

These explain why depth can be represented on a flat surface.

| Cue | Mechanism | Verified image / page (P2 OK) |
| --- | --- | --- |
| **Linear perspective** | Parallel lines converge toward a vanishing point. | [Vanishing point](https://en.wikipedia.org/wiki/Vanishing_point) · [File:Railroad-Tracks-Perspective.jpg](https://commons.wikimedia.org/wiki/File:Railroad-Tracks-Perspective.jpg) · diagram [File:Eye level and vanishing point diagram japanese.svg](https://commons.wikimedia.org/wiki/File:Eye_level_and_vanishing_point_diagram_japanese.svg) (CC0; Profield `conforming_public`) |
| **Occlusion** | Nearer object blocks farther one. | Covered in [Depth cues 1.png](https://commons.wikimedia.org/wiki/File:Depth_cues_1.png); Profield I.6 occlusion search = 0 assets |
| **Relative size** | Smaller known objects read as farther. | Same overview diagram |
| **Texture gradient** | Texture compresses with distance. | [Texture gradient](https://en.wikipedia.org/wiki/Texture_gradient) · Caillebotte street as article lead [File:Gustave Caillebotte - Paris Street; Rainy Day…](https://commons.wikimedia.org/wiki/File:Gustave_Caillebotte_-_Paris_Street;_Rainy_Day_-_Google_Art_Project.jpg) |
| **Aerial perspective** | Distance reduces contrast / saturation / sharpness. | [Aerial perspective](https://en.wikipedia.org/wiki/Aerial_perspective) · [File:MonNatForest.jpg](https://commons.wikimedia.org/wiki/File:MonNatForest.jpg) · [File:Frans Koppelaar - Landscape near Bologna.jpg](https://commons.wikimedia.org/wiki/File:Frans_Koppelaar_-_Landscape_near_Bologna.jpg) |
| **Shading / cast shadows** | Luminance implies curvature. | Overview [Depth cues 1.png](https://commons.wikimedia.org/wiki/File:Depth_cues_1.png) |
| **Motion parallax** | Near objects sweep the retina faster. | [File:Parallax scroll.gif](https://commons.wikimedia.org/wiki/File:Parallax_scroll.gif) (on Depth perception article) |

**Empirical papers (P2 OK):** Kitazaki et al. via [PLOS ONE pictorial / disparity / parallax](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0003177) · Li et al. 2025 [PMC12115827](https://pmc.ncbi.nlm.nih.gov/articles/PMC12115827/).

---

## 5. The Renaissance Revolution

### Leon Battista Alberti and *De pictura* (1435)

The decisive breakthrough was geometric, not neuroscientific. Alberti transformed geometrical optics into a practical method for image construction. The painting is “an open window through which I see what is to be painted” — one of the most consequential metaphors in Western visual culture.

Before Alberti, pictorial space often functioned symbolically or theologically; scale reflected spiritual importance. Alberti proposed that image construction should emulate the geometrical structure of vision itself.

| Concept | Theoretical function |
| --- | --- |
| **Picture plane** | Interface between observer and scene |
| **Vanishing point** | Projection of recession in depth |
| **Orthogonals** | Spatial organization of distance |
| **Visual pyramid** | Geometric model of observation (object → rays → eye; image = intersection with the picture plane) |

**Consequences.** Perspective became measurable, repeatable, teachable. The image represented optical space rather than symbolic space. This construction remains fundamentally identical to virtual-camera models in computer graphics pipelines.

**Verified texts / bio:** [*De pictura* (Wikipedia)](https://en.wikipedia.org/wiki/De_Pictura) · **P2 OK** · [Leon Battista Alberti](https://en.wikipedia.org/wiki/Leon_Battista_Alberti) · **P2 OK** · Internet Archive *On Painting* [1991 ed.](https://archive.org/details/onpainting0000albe) · [1966 ed.](https://archive.org/details/onpainting0000albe_d2k5) · **P2 OK**. Britannica *On Painting* returned **HTTP 403** from this environment — do not treat as live.  
**Wikimedia:** [File:Leon Battista Alberti, Self-Portrait, c. 1435, NGA 43845.jpg](https://commons.wikimedia.org/wiki/File:Leon_Battista_Alberti,_Self-Portrait,_c._1435,_NGA_43845.jpg) · **P2 OK**. Profield Alberti search mostly returned unrelated IA book PDFs — low teaching value; prefer Wikipedia/Commons leads above.

---

## 6. Piero della Francesca — *De Prospectiva Pingendi*

If Alberti created perspective theory, Piero transformed it into mathematical procedure: foreshortening, polyhedra, projection methods — anticipating descriptive geometry. Often regarded as the first truly mathematical painter.

**Verified:** [Piero della Francesca](https://en.wikipedia.org/wiki/Piero_della_Francesca) · **P2 OK** · [Foreshortening](https://en.wikipedia.org/wiki/Foreshortening) · **P2 OK**.  
**Wikimedia (volume in painting):** [File:Madonna del parto piero della Francesca.jpg](https://commons.wikimedia.org/wiki/File:Madonna_del_parto_piero_della_Francesca.jpg) · **P2 OK**. Profield foreshortening run returned duplicate Hayter perspective manuals (PD PDFs) — usable as historical pedagogy sources, weak as classroom stills.

---

## 7. Leonardo da Vinci

Where Alberti addressed geometry, Leonardo addressed perception. Geometric projection alone fails to explain visual experience; atmospheric conditions alter perceived distance through color, contrast, and clarity.

1. **Linear perspective** — geometrical projection.
2. **Color perspective** — chromatic change over distance.
3. **Aerial perspective** — atmospheric degradation.

Modern vision science confirms that perceived depth also depends on luminance gradients, chromatic attenuation, edge contrast, and environmental scattering — principles Leonardo anticipated within ecological and computational models of vision.

**Verified primary scan (Profield aerial run):** [File:A treatise on painting (IA davincionpainting00leon).pdf](https://commons.wikimedia.org/wiki/File:A_treatise_on_painting_(IA_davincionpainting00leon).pdf) · **P2 OK** · `conforming_public` / Public domain — still `needs_human_review` before classroom crop/embed.

---

## 8. Erwin Panofsky's Revolution — *Perspective as Symbolic Form* (1927)

Perspective is not merely a technical solution. It is a **cultural model**: a society chooses how space should be represented. Different civilizations construct different spatial worlds.

**Research implication.** Perspective is neither universal nor neutral. It is both perceptual and ideological.

*(Course link: Panofsky categories already govern the perspective · volume image kit under `forge/receipts/PERSPECTIVE-VOLUME-IMAGE-KIT.md`.)*

**Verified:** [Erwin Panofsky](https://en.wikipedia.org/wiki/Erwin_Panofsky) · **P2 OK** · Archive text PDF [Perspective as Symbolic Form](https://archive.org/download/ErwinPanofskyPerspectiveAsSymbolicForm/Erwin%20Panofsky%20-%20Perspective%20as%20Symbolic%20Form_text.pdf) · **P2 OK** · [JSTOR 3700512](https://www.jstor.org/stable/3700512) · **P2 OK** · [Project MUSE](https://muse.jhu.edu/book/79031/) · **P2 OK**. Princeton UP product page returned **HTTP 403** here — keep as known imprint only, not a live link.

---

## 9. Why Perspective Works

Perspective succeeds because it exploits depth cues already used by the visual system.

| Human cue | Artistic equivalent |
| --- | --- |
| Relative size | Scale reduction |
| Convergence | Vanishing points |
| Occlusion | Overlapping forms |
| Texture gradient | Surface treatment |
| Atmospheric depth | Aerial perspective |
| Motion parallax | Animation / cinema |

Perspective is therefore not an invention. It is an engineering solution built around perceptual mechanisms.

**Teaching stills (P2 OK):** three-point diagram [File:3-punktperspektive 1.svg](https://commons.wikimedia.org/wiki/File:3-punktperspektive_1.svg) · railway recession [File:Railroad-Tracks-Perspective.jpg](https://commons.wikimedia.org/wiki/File:Railroad-Tracks-Perspective.jpg).

---

## 10. Digital Perspective: Alberti in Linear Algebra

Computer graphics inherits Renaissance perspective almost unchanged. The digital camera model is Alberti translated into linear algebra. Every perspective rendering engine in OpenGL, DirectX, Vulkan, Unreal Engine, and Unity ultimately reproduces the same geometric principles.

**Perspective projection:**

\[
x' = \frac{x}{z}, \quad y' = \frac{y}{z}
\]

Distance produces diminution; parallel lines converge; objects recede toward vanishing points. What Renaissance artists constructed with straightedges is now implemented through matrix multiplication billions of times per second.

**Digital depth cues** combine:

- **Geometric** — perspective, scaling, shadows
- **Physiological** — stereoscopy, binocular disparity
- **Dynamic** — optical flow, motion parallax
- **Computational** — depth maps, Z-buffer data, neural depth estimation

**Verified math primers (P2 OK):** [Scratchapixel — building a perspective projection matrix](https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/building-basic-perspective-projection-matrix.html) · [OGLDev Tutorial 12](https://ogldev.org/www/tutorial12/tutorial12.html) · [UNM perspective projections PDF](https://www.cs.unm.edu/~angel/AW/chap05c.pdf) · [WebGL perspective math](http://webgl.brown37.net/09_projections/04_projections_perspective_math.html) · Wikipedia [Camera matrix](https://en.wikipedia.org/wiki/Camera_matrix) · [3D projection](https://en.wikipedia.org/wiki/3D_projection).  
**Profield note:** `20261113-projection-matrix` returned 1 off-topic luminance-probe PDF — ignore; use primers + Commons projection SVGs above.

---

## 11. AI and the Future of Perspective

Generative systems (Midjourney, DALL·E, Stable Diffusion, GPT-image systems) do not explicitly construct perspective using Renaissance geometry. They learn statistical regularities from millions of images.

> Has AI learned perspective, or has it learned visual plausibility?

That distinction may define visual-culture research over the next decade.

---

## Original Contribution for Creation-Led Research

For contemporary design students, the most productive research question is no longer *How is perspective constructed?* but:

> Which perceptual assumptions remain stable across painting, photography, cinema, CGI, virtual reality, and generative artificial intelligence?

This shifts the focus from representation toward cognition. Core hypothesis:

> Images appear realistic not because they reproduce the world, but because they successfully engage the perceptual mechanisms through which observers construct the experience of a world.

That proposition bridges Alberti, Helmholtz, Marr, Unreal Engine, NeRFs, Stable Diffusion, and contemporary computational image synthesis.

### Bachelor research axes (operational)

| Axis | Focus |
| --- | --- |
| **1 · Historical evolution** | Euclid → Alberti → Piero → Leonardo → Panofsky |
| **2 · Vision science** | Helmholtz → Gibson → Marr → contemporary neuroscience |
| **3 · Image construction** | drawing · painting · photography · cinema · animation |
| **4 · Digital representation** | cameras · game engines · CGI · VR/AR |
| **5 · AI-generated imagery** | latent spatial models · synthetic realism · perceptual plausibility · machine perspective |

### Deferred: graduate-level reader (not this file)

If expanded to a 30–50 page fully referenced scholarly Markdown monograph, next layers would be: Chicago citations; DOI-verified references only where available; direct quotations from *Optica*, *De pictura*, *De Prospectiva Pingendi*, *Treatise on Painting*, and *De Divina Proportione*; historiographical debates (Panofsky, Gombrich, Damisch, Kubovy, Kemp); neuroscience of stereopsis and motion parallax; computer-graphics mathematics; generative-AI spatial modeling; annotated bibliography; figures list; glossary; student research assignments and studio exercises. That would be an introductory graduate reader, not a class handout — keep it out of student HTML until Ahmes-grounded.

---

## Essential Bibliography (Verified Core Corpus)

### Primary sources

- Euclid — *Optica*
- Leon Battista Alberti — *De pictura* (1435) — page **P2 OK** above
- Piero della Francesca — *De Prospectiva Pingendi*
- Leonardo da Vinci — *Treatise on Painting* — Commons PDF **P2 OK** above
- Luca Pacioli — *De Divina Proportione*

### Foundational modern texts

- Helmholtz, H. von. *Handbook of Physiological Optics*
- Gibson, J. J. *The Ecological Approach to Visual Perception* (1979)
- Marr, D. *Vision* (1982)
- Panofsky, E. *Perspective as Symbolic Form* — Archive PDF **P2 OK** above

### Contemporary vision science

- Gibson & Walk, “The Visual Cliff” (1960) — Wikipedia + SimplyPsychology **P2 OK** above
- Kitazaki, Kobiki & Maloney (2008) — PLOS ONE **P2 OK** above
- Li et al. (2025) — PMC **P2 OK** above

---

## Final Thesis

The history of perspective, from Alberti's window to neural rendering, is ultimately the history of a single problem:

> How can a flat image trigger the perceptual mechanisms by which humans infer a volumetric world?

All visual culture, from Renaissance frescoes to virtual reality and generative AI, consists of progressively more sophisticated answers to that question.

---

## Course bounce map (internal)

| Consumer | Use |
| --- | --- |
| `forge/session-prompts/i-5-three-dimensional-form.md` | Spatial literacy / representation hypotheses |
| `forge/session-prompts/i-6-volume.md` | Volume as behaviour — why flat evidence can still “read” as volume |
| `forge/receipts/PERSPECTIVE-VOLUME-IMAGE-KIT.md` | Panofsky categories ↔ pictorial cues |
| `grounding/gap-fields/dc-3d-form-volume-pedagogy.pass1.edited.md` | Fashion HE pedagogy evidence (separate genre — do not merge) |
| `~/src/profield/runs/media-prospector/I.{5,6}/20261113-*` | Raw manifests; discovery ≠ clearance |
| Student lessons | Chicago author-date only after Ahmes `evaluator_safe=yes` |
