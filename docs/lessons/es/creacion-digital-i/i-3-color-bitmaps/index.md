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
status: scaffold
tags: [creacion-digital-i, color, mapa-de-bits, imagen-de-trama]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"La imagen de trama teme el zoom. El SVG lo recibe con los brazos abiertos."_
<!-- Ajuste TTDO: ajuste directo — el propio anclaje de esta unidad es la imagen de mapa de bits/trama específicamente, en contraste con el vector de la I.2. -->
> — Tao of Development, `img-016`
{: .tao-development-quote }

---

{% include lesson-semantic-graphic.html %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Color, imágenes con mapas de bits.*

**Competencias que sirve:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Resultados de aprendizaje:** *"Asociar los diferentes programas de efectos y recursos de edición de imagen digital"* es la frase de la guía más cercana, compartida con I.4 — las herramientas de color son uno de los "recursos de edición" que nombra; ninguna frase es exclusiva solo de color/mapas de bits.

**Pesos de evaluación:** Investigaciones y proyectos 20% (pieza de taller); Cuaderno 10% (nota de proceso).

---

## 🎯 Objetivos de aprendizaje

- **Describir una imagen de mapa de bits como una cuadrícula fija de valores de color** — y explicar qué cierra una decisión de color dada (modo, profundidad, gama) para más adelante.
- **Explicar el color como relacional y perceptivo** — paletas digitales enseñadas mediante interacción, contraste y contexto, no sliders RGB aislados (Albers 2013).
- **Nombrar cómo las tecnologías de creadores producen convenciones cromáticas y tonales ligadas al tiempo** en plataformas (Roivainen 2025, 8).
- **Producir una comparación de color** (no una paleta «final» única): qué cambió, qué siguió legible y qué código de plataforma o cultural invocaste.
- **Distinguir "corrección de color" de "cambio de color"** — una pregunta de divulgación, no técnica.

---

## Por qué existe esta unidad — el color como relación, no como paleta única

**Afirmación:** el color es relacional y perceptivo, por lo que las paletas digitales deben enseñarse mediante interacción, contraste y contexto — no como muestras fijas ni valores RGB aislados (Albers 2013).

Una imagen de mapa de bits es una cuadrícula fija de valores de color; cada decisión sobre modo, profundidad de bits o gama es también una decisión sobre lo que la imagen no podrá volver a ser sin pérdida. El trabajo digital experto produce visualidades que reflejan estilos de edición populares en un momento dado — iluminación, tendencias cromáticas y tonos que hacen que las imágenes parezcan «profesionales» o «únicas» (Roivainen 2025, 8).

**Qué sostiene esto y qué no.** Albers (2013) sostiene la enseñanza perceptiva del color más allá de los menús de herramienta. Roivainen (2025) sostiene nombrar convenciones de edición nativas de plataforma y ligadas al tiempo — adyacente a la moda, no un temario de color de moda validado. Ninguno valida una **secuencia de enseñanza de gestión del color** para moda en educación superior; la documentación de herramienta fundamenta operaciones — etiqueta `[PLATFORM]`, nunca investigación.

**Anclaje de práctica (perspectiva de campo):** color relacional y alfabetización en mapa de bits (Albers 2013; operaciones técnicas de color en T1).

**Señal de frontera (perspectiva de campo):** los estilos de edición nativos de plataforma circulan con rapidez; trata los tonos en tendencia como señales históricas a comparar, no como valores por defecto a copiar.

## Perspectiva crítica

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

## B1 · Conceptual — magistral 1 h + seminarios 2 h + debates 1 h

Cubierto arriba: afirmación de color relacional, estilos Roivainen, perspectiva crítica, debate y marcadores.

---

## B2 · Taller — talleres 1 h + investigaciones y proyectos 2 h

**Entregable:** una **comparación de color** — dos paletas o versiones de modo de color de la misma imagen de moda — con una nota de proceso que nombre qué cambió, qué siguió legible y qué código de plataforma o cultural invocaste.

**Definición de terminado:** ID de pieza; carpeta de proceso; la nota de comparación presente y específica.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidencia:** Investigaciones y proyectos 20% (pieza); Cuaderno 10% (nota). Sin S1/S2 — ROL DE ARTEFACTO ninguno.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, descontextualizada

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

## Referencias

- Albers, Josef. 2013. *Interaction of Color: 50th Anniversary Edition*. New Haven: Yale University Press. ISBN 9780300179354.
- AlDahoul, Nouar, Talal Rahwan, and Yasir Zaki. 2025. "AI-Generated Faces Influence Gender Stereotypes and Racial Homogenization." *Scientific Reports* 15: 14449. https://doi.org/10.1038/s41598-025-99623-3.
- Roivainen, Ida. 2025. "'How I Edit My Instagram Images': Investigating Skilled Vision in the Work of YouTube's Lifestyle-Content Creators." *Visual Studies* 40 (3): 569–585. https://doi.org/10.1080/1472586X.2024.2353689.

**Laguna declarada — con claridad.** Ninguna fuente revisada valida una **secuencia de enseñanza de gestión del color** para moda en educación superior. Albers y Roivainen sostienen alfabetización perceptiva y de color en plataforma; no prueban que este flujo de aula enseñe mejor que una alternativa.

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
