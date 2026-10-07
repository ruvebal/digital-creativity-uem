---
layout: lesson
title: 'I.3 · Color, imágenes con mapas de bits'
title_en: 'I.3 · Colour, Bitmap Images'
slug: i-3-color-bitmaps
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-i/i-3-color-bitmaps/
description: 'El color es relacional y sensible al tiempo — teoría perceptiva del color más estilos de edición en plataforma, con laguna honesta en pedagogía de gestión del color.'
status: pilot
tags: [creacion-digital-i, color, mapa-de-bits, imagen-de-trama]
deck_url: /tracks/dci/i-3-color-bitmaps/
master_idea: 'El color es una relación — muestreado, mostrado, nombrado e interpretado — no una muestra fija'
practice_anchor: 'Alfabetización de mapa de bits: modo, profundidad, gama, contraste y una paleta alternativa accesible visible en el registro de proceso'
frontier_signal: 'Los estilos de edición en plataforma circulan rápido; las secuencias de gestión del color en HE de moda siguen sin validar'
references: [roivainen-2025, aldahoul-2025]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

<div class="lesson-opener" markdown="1">

> _"La imagen de trama teme el zoom. El SVG lo recibe con los brazos abiertos."_
<!-- Ajuste TTDO: ajuste directo — el propio anclaje de esta unidad es la imagen de mapa de bits/trama específicamente, en contraste con el vector de la I.2. -->
> — Tao of Development, `img-016`
{: .tao-development-quote }

{% include lesson-semantic-graphic.html %}

</div>

{% comment %}
cover-agentic:
  unit: I.3
  contenidos: "Color, imágenes con mapas de bits."
  competencies: [CON1, HAB9, COMP8, COMP9]
  one_line: "El color es relacional — el mapa de bits lo muestrea bajo supuestos de pantalla y cultura."
  class_rhythm: "Análisis → Masterclass → Lab (Portfolio) — sin Workshop en sesiones tempranas"
  evaluation_feed: "Investigaciones y proyectos 20%; Cuaderno 10%"
  how_to_pass: "/tracks/dci/how-to-pass-this-track/"
{% endcomment %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Color, imágenes con mapas de bits.*

**Competencias que sirve:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Resultados de aprendizaje:** *"Asociar los diferentes programas de efectos y recursos de edición de imagen digital"* es la frase de la guía más cercana, compartida con I.4 — las herramientas de color son uno de los "recursos de edición" que nombra; ninguna frase es exclusiva solo de color/mapas de bits.

**Pesos de evaluación:** Investigaciones y proyectos 20% (pieza de taller); Cuaderno 10% (nota de proceso).

---

## Objetivos de aprendizaje

- **Describir una imagen de mapa de bits como una cuadrícula fija de valores de color** — y explicar qué cierra una decisión de color dada (modo, profundidad, gama) para más adelante.
- **Explicar el color como relacional y perceptivo** — paletas digitales enseñadas mediante interacción, contraste y contexto, no sliders RGB aislados (Albers 2013).
- **Nombrar cómo las tecnologías de creadores producen convenciones cromáticas y tonales ligadas al tiempo** en plataformas (Roivainen 2025, 8).
- **Producir una comparación de color** (no una paleta «final» única): qué cambió, qué siguió legible y qué código de plataforma o cultural invocaste.
- **Distinguir "corrección de color" de "cambio de color"** — una pregunta de divulgación, no técnica.

---

## Análisis
### Perspectiva crítica

Los sistemas contemporáneos de generación y clasificación visual pueden reproducir desigualdades interseccionales de género y racialización — las herramientas empleadas para producir imágenes de moda no deben tratarse como infraestructuras representacionales neutrales (AlDahoul et al. 2025).

¿Quién es tratado como espectador por defecto cuando una paleta se llama precisa, bella o accesible? Nombra una prueba de contraste, un desajuste de pantalla o un contexto de piel/prenda excluido que tu cadena de exportación da por sentado.

### La pregunta de debate

**¿Cuándo "corregir" un color se convierte en "cambiar" la prenda que representa?** Es la misma pregunta de divulgación que la unidad de retoque de CD II (II.1) plantea sobre los cuerpos — planteada aquí a nivel del color. El grupo decide junto y declara la decisión.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.video.colour-workflow" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador abstracto para demostración de flujo de color; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> un clip breve se detiene cada vez que cambia un perfil, espacio o supuesto de exportación.</p>
<p><strong>Qué observar:</strong> puntos de conversión y qué cierra cada paso.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.still.palette-contrast" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador para ejemplos de contraste de paleta; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> paletas en paralelo prueban legibilidad, jerarquía y atmósfera.</p>
<p><strong>Qué observar:</strong> pares que fallan el contraste en una pantalla pero pasan en otra.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.3.graphic.colour-chain" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-03-colour-relations-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador de diagrama para cadena color fuente-exportación; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> mapea color fuente → perfil/espacio → pantalla/exportación → espectador.</p>
<p><strong>Qué observar:</strong> dónde se rompe la cadena si cambia un dispositivo.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

---



Cubierto arriba: afirmación de color relacional, estilos Roivainen, perspectiva crítica, debate y marcadores.

---

## Masterclass

<figure class="lesson-figure" id="figure-masterclass-1" markdown="0">
<img src="{{ '/assets/images/deck-media/750f32a08550dcff.webp' | relative_url }}" alt="This is a digital graphic or print design, not a photograph, painting, or document. It features a 2x2 grid of solid color blocks—cyan (top-left), magenta (top-right), yellow (bottom-left), and black (bottom-right)—each containing a large, bold, white or black capital letter: “C”" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-1" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-2" markdown="0">
<img src="{{ '/assets/images/deck-media/7a2791f63dcc1d31.webp' | relative_url }}" alt="Nokia 8-display pixel pattern PNr°0495.jpg" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-2" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-3" markdown="0">
<img src="{{ '/assets/images/deck-media/67e8367fb0719e25.webp' | relative_url }}" alt="Fashion illustration" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-3" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-4" markdown="0">
<img src="{{ '/assets/images/deck-media/c425a4f37ec39601.webp' | relative_url }}" alt="Fashion illustration" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-4" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-5" markdown="0">
<img src="{{ '/assets/images/deck-media/37ef9f5bda8f9a93.webp' | relative_url }}" alt="An exhibition poster composition" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-5" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-6" markdown="0">
<img src="{{ '/assets/images/deck-media/9399010fa60a83d5.webp' | relative_url }}" alt="Test - image size comparison (Jpeg vs Png vs Jpeg XL vs Heic).png" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-3-color-bitmaps" slide="masterclass-6" %}</figcaption>
</figure>


**Afirmación:** el color es relacional y perceptivo, por lo que las paletas digitales deben enseñarse mediante interacción, contraste y contexto — no como muestras fijas ni valores RGB aislados (Albers 2013).

Una imagen de mapa de bits es una cuadrícula fija de valores de color; cada decisión sobre modo, profundidad de bits o gama es también una decisión sobre lo que la imagen no podrá volver a ser sin pérdida. El trabajo digital experto produce visualidades que reflejan estilos de edición populares en un momento dado — iluminación, tendencias cromáticas y tonos que hacen que las imágenes parezcan «profesionales» o «únicas» (Roivainen 2025, 8).

**Qué sostiene esto y qué no.** Albers (2013) sostiene la enseñanza perceptiva del color más allá de los menús de herramienta. Roivainen (2025) sostiene nombrar convenciones de edición nativas de plataforma y ligadas al tiempo — adyacente a la moda, no un temario de color de moda validado. Ninguno valida una **secuencia de enseñanza de gestión del color** para moda en educación superior; la documentación de herramienta fundamenta operaciones — etiqueta `[PLATFORM]`, nunca investigación.

**Anclaje de práctica (perspectiva de campo):** color relacional y alfabetización en mapa de bits (Albers 2013; operaciones técnicas de color en T1).

**Señal de frontera (perspectiva de campo):** los estilos de edición nativos de plataforma circulan con rapidez; trata los tonos en tendencia como señales históricas a comparar, no como valores por defecto a copiar.

## Lab (Portfolio)

*Bloque de sesión · Una diapositiva geométrica anuncia el Lab: **dos** ejercicios. Todo lo que produzcas en Lab entra en tu **índice de portfolio**. Los Labs practican ideas de Masterclass y alimentan el oficio ACT — no son un segundo canal evaluable de Campus Virtual.*

### Ejercicio 1 — Lock the key-visual brief, then sample a palette {#lab-exercise-1}

Practises Masterclass ideas **1** (colour is a relation) and **6** (correcting vs changing).

**Time:** 20 minutes.

**Group:** alone for craft; pairs OK for a 2-minute brief critique.

**Materials:** laptop; one rights-clear garment/fabric photo; timer; notes app.

**Steps:**

1. Write **audience**, **channel**, and a **single claim** before opening the canvas.
2. Sample five colours from the garment photo; build a palette strip (no moodboard tiles yet).
3. Build one accessible alternate (contrast-aware) without inventing a second claim.
4. Reject any swatch that does not serve the claim.
5. Note one hierarchy decision the clash forced.

**Portfolio trace:** brief text + five-colour strip + accessible alternate + hierarchy note.

**Judged by:** [Portfolio rubric — process evidence and craft]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (key-visual / palette craft gap — no Wave-1 verified pedagogy sequence).

**Example trace:** *(Illustrative · not student work.)* Brief: audience = campus drop, channel = Instagram square, claim = “denim reads cooler under tungsten.” Five-swatch strip + one high-contrast alternate; hierarchy note: “Claim forced the mid-blue to lose saturation.”


### Ejercicio 2 — One Gestalt pass on a key-visual crop {#lab-exercise-2}

Practises Masterclass ideas **2** (a bitmap has limits) and **4** (the display participates).

**Time:** 20 minutes.

**Group:** alone for the two crops; pairs for the peer vote.

**Materials:** a key-visual or fashion crop; bitmap editor; timer.

**Steps:**

1. Name one Gestalt relation to test (proximity, similarity, closure, continuity, or figure–ground).
2. Apply the relation once to the crop.
3. Invert or break the relation in a second version; keep both.
4. Peer names which version groups more clearly and why (one sentence).
5. Record the chosen relation in the process note.

**Portfolio trace:** two crops + peer sentence + process note naming the relation.

**Judged by:** [Portfolio rubric — composition judgement]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (Gestalt pedagogy gap — Arnheim not in Wave-1 references).

**Example trace:** *(Illustrative · not student work.)* Relation = proximity. Crop A clusters buttons; crop B spreads them. Peer: “A groups as a placket; B reads as scatter.”


**Definition of done (studio slice):** piece ID; process folder; colour/Gestalt pair present and specific — the Lab traces are the cuaderno evidence.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidence:** Investigaciones y proyectos 20% (piece); Cuaderno 10% (note). No S1/S2 — ARTEFACT ROLE none.
LAB_LINE: exercise=1; method_id=key-visual-brief-lock; practises=masterclass-1,masterclass-6; source=gap/classroom adaptation; ACT=ACT2
LAB_LINE: exercise=2; method_id=gestalt-composition; practises=masterclass-2,masterclass-4; source=gap/classroom adaptation; ACT=ACT2
-->
{% endif %}

---

## Workshop

Desde la sesión 4: el Workshop es tiempo de estudio protegido para D2 Transposición y D3 evento final (≈ mitad / mitad) — no es reloj de D1 Análisis.


1. **Diagnóstico.** Dadas dos versiones del mismo mapa de bits con distinta profundidad de bits, identifica qué artefacto muestra cada una y por qué.
2. Describe a mano, sin herramienta abierta, la diferencia visual entre una paleta limitada y una completa para una imagen descrita. **Sin IA — declarado como tal.**
3. Distingue "corrección de color" de "cambio de color" para una edición descrita, usando el marco de divulgación de B1.

Los borradores de respuesta del profesor no se publican en esta página.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "palette-depth — campos de píxel restringido y matizado separados por un umbral de corrección"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Conclusión

Esta unidad deja lagunas nombradas a propósito: lo que el vault puede verificar con página queda en Referencias; lo abierto queda en la Nota editorial. Mantén las trazas de Lab honestas en el índice de portfolio. No inventes un entregable evaluable que How to Pass no pide. La siguiente apuesta es el ritmo de sesión ya nombrado — defensa de Análisis (D1) desde la sesión 3; Workshop desde la sesión 4 para Transposición y el evento final.

---

## Tao de la imagen {#tao-of-the-image}

Epígrafe de la unidad (registro Tao de estudio — no es cita académica):

> _"La imagen de trama teme el zoom. El SVG lo recibe con los brazos abiertos."_

Los enlaces del deck y de la lección a `#tao-of-the-image` resuelven aquí.

---

## Referencias

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.3; temario=T1-image-2d-volume.pass1.resultant.mdc § "Color; mapas de bits"; subfield_runs=dc-2d-image-craft-pedagogy/pass1.edited.md § colour management
CRITICAL_ROUTING: unit=I.3; critica=C1 algorithmic colour trends; C3 AlDahoul image-generation bias; session default-viewer prompt
PROVENANCE_LINE: claim=I.3.claim.relational-colour; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="Albers perceptual colour digital palettes"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Albers; similarity=null; proposed_use="perceptual anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Albers 2013 not in scholar vault; quote=none; public_citation="(Albers 2013)"; supports="relational perceptual colour teaching"; does_not_support="colour-management pedagogy sequence"
PROVENANCE_LINE: claim=I.3.claim.platform-editing-styles; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="skilled vision Instagram editing colour trends"; source_locator=MASTER-IDEAS I.3; similarity=null; proposed_use="frontier/platform colour conventions"}; source={document_coat=47ce5b17; extraction_db=ahmes-library/scholar/documents/how_i_edit_my_instagram_images_investigating_skilled_vision_in_the_work_of_youtube_s_lifestyle_content_creators_47ce5b17/extract/extraction.db; node_id=307e67e0-f3a3-5fa3-a623-ceebc74fd70c; page_index=7; printed_page=8}; resolver="ahmes query --cite extraction.db:307e67e0-f3a3-5fa3-a623-ceebc74fd70c --require-evaluator-safe evaluator_safe=yes"; quote="editing styles that are popular at a given moment"; public_citation="(Roivainen 2025, 8)"; supports="time-bound platform colour and tonal conventions"; does_not_support="fashion-specific colour syllabus or classroom efficacy"
PROVENANCE_LINE: claim=I.3.gap.colour-management-pedagogy; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion higher education colour management pedagogy validated"; source_locator=null; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated colour-management teaching method for fashion students"
PROVENANCE_LINE: claim=I.3.critical.generative-bias; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="AI generated faces gender racial bias fashion"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc § AlDahoul; similarity=null; proposed_use="critical technical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=AlDahoul 2025 not in scholar vault; quote=none; public_citation="(AlDahoul et al. 2025)"; supports="image tools are not representationally neutral"; does_not_support="classroom policy prescription"
PROVENANCE_LINE: claim=I.3.critical.default-viewer; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="colour accuracy default viewer accessibility"; source_locator=i-3-colour-bitmaps.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming default viewer and contrast assumptions"; does_not_support="empirical accessibility claim for cohort"
MEDIA_RIGHTS_LINE: slot=I.3.video.colour-workflow; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.3.still.palette-contrast; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.3.graphic.colour-chain; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de Innovación docente
{: .lesson-editorial-note }

**Laguna declarada — con claridad.** Ninguna fuente revisada valida una **secuencia de enseñanza de gestión del color** para moda en educación superior. Albers y Roivainen sostienen alfabetización perceptiva y de color en plataforma; no prueban que este flujo de aula enseñe mejor que una alternativa.

Esta nota forma parte de una *Práctica de Innovación docente* en curso — los límites epistémicos van aquí, no entre párrafos de Masterclass.

---

## Autoría asistida por IA

Esta lección se redactó con asistencia local de IA bajo control editorial del autor. Declaración de uso de IA (alumnado y docencia): [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).

{% if site.publication.publish_internal_metadata %}
<!-- forge_date: 2026-09-22 · Studio: crea-comm.net · harness: local drafting tools v0.1 · prompt-v2.1
      lesson_uuid: deeb9179-2bef-4d0e-8f51-52d1a5186f95
     vault_refs_consulted: 3
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
