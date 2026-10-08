---
layout: lesson
title: 'I.4 · Efectos'
title_en: 'I.4 · Effects'
slug: i-4-efectos
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-i/i-4-efectos/
description: 'Un efecto es una transformación con un antes — operaciones de filtrado y composición más conciencia ética de la imagen retocada en moda, con una laguna honesta sobre pedagogía de efectos.'
status: scaffold
tags: [creacion-digital-i, efectos, filtros, divulgacion]
deck_url: /tracks/dci/i-4-effects/
references: [shinkle-2008, roivainen-2025, aldahoul-2025]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"El offset no es matemática — es empatía. Debes recordar lo que vino antes."_
<!-- Ajuste TTDO: usado de forma analógica aquí — su campo `teaches` propio trata del offset/posicionamiento en interfaz, no de efectos de imagen; el ajuste se declara: un efecto aplicado a una imagen es una transformación que debe recordar, no borrar, el original. -->
> — Tao of Development, `arch-018`
{: .tao-development-quote }

---

{% include lesson-semantic-graphic.html %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Efectos.*

**Competencias que sirve:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Resultados de aprendizaje:** *"Asociar los diferentes programas de efectos y recursos de edición de imagen digital"* — compartida con I.3, es la frase de la guía que nombra directamente "efectos".

**Pesos de evaluación:** Investigaciones y proyectos 20% (pieza de taller); Cuaderno 10% (nota de proceso).

---

## Objetivos de aprendizaje

- **Nombrar filtrado, mejora, transformación del color y corrección** como operaciones bitmap centrales del postprocesado digital (Gonzalez y Woods 2018).
- **Tratar los efectos como parte de problemas visuales**, no como un catálogo autónomo de filtros (Curcic 2024).
- **Producir un par antes/después** con el "antes" conservado y una línea de divulgación de qué cambió.
- **Conectar el postprocesado con la lectura crítica** de imágenes retocadas en moda, belleza y publicidad (McBride et al. 2019).
- **Distinguir "efecto" (estilización divulgada) de "manipulación" (engaño no divulgado).**

---

## Análisis
### Perspectiva crítica

TikTok, ASMR, nostalgia, realidad aumentada y otras formas de circulación digital muestran cómo las tendencias de moda contemporáneas se organizan crecientemente en torno al afecto y la experiencia audiovisual (Crepax 2024) — un efecto que "aclara el estado de ánimo" puede también fabricar un mundo más deseable mientras parece meramente técnico.

El retoque en moda y belleza requiere alfabetización técnica más conciencia ética de imágenes publicitarias manipuladas (McBride et al. 2019). ¿En qué punto la transformación se convierte en una afirmación sobre una persona, una prenda o una realidad, y no en un tratamiento visual — y quién tiene autoridad para decidir ese umbral?

### La pregunta de debate

**¿Hay una línea con sentido entre un "efecto" (estilización, divulgada) y una "manipulación" (engaño, no divulgado) — y se mueve esa línea según el contexto (editorial frente a publicitario)?** Ninguna fuente lo resuelve para vuestra cohorte; declara la línea de trabajo propia del grupo en vez de asumir una.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.4.video.effect-breakdown" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-04-effects-meaning-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador abstracto para demostración de desglose de efectos; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> un desglose breve hace una pausa antes de la revelación para que el estudiantado prediga la lógica de capas.</p>
<p><strong>Qué observar:</strong> fuente, máscara, transformación y qué cierra cada paso.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.4.still.before-after" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-04-effects-meaning-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador para ejemplo de efecto intencional y contraejemplo sobreprocesado; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> imágenes en paralelo prueban legibilidad, contención y qué sigue siendo legible tras la transformación.</p>
<p><strong>Qué observar:</strong> propósito expresivo frente a exceso decorativo.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.4.graphic.layer-stack" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-04-effects-meaning-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador de diagrama para pila de capas fuente-máscara-transformación-exportación; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> mapea fuente → máscara → transformación → composición → verificación → exportación.</p>
<p><strong>Qué observar:</strong> dónde un paso destructivo podría sustituirse por uno reversible.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

---



Cubierto arriba: marco técnico Gonzalez/Curcic, ética McBride, perspectiva crítica, debate y marcadores.

---

## Masterclass

<figure class="lesson-figure" id="figure-masterclass-1" markdown="0">
<img src="{{ '/assets/images/deck-media/684484de753f97f5.webp' | relative_url }}" alt="A fashion sketch design study" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-4-effects" slide="masterclass-1" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-2" markdown="0">
<img src="{{ '/assets/images/deck-media/c2c1b5e1ab5b5c82.webp' | relative_url }}" alt="Jun Takahashi dress for Undercover (51492).jpg" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-4-effects" slide="masterclass-2" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-3" markdown="0">
<img src="{{ '/assets/images/deck-media/37ef9f5bda8f9a93.webp' | relative_url }}" alt="An exhibition poster composition" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-4-effects" slide="masterclass-3" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-analysis-model" markdown="0">
<img src="{{ '/assets/images/deck-media/4e655e0f068fdc07.webp' | relative_url }}" alt="Dresses by Rei Kawakubo in a second exhibition view" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-4-effects" slide="analysis-model" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-cover" markdown="0">
<img src="{{ '/assets/images/deck-media/8243faeb5945da08.webp' | relative_url }}" alt="Dresses by Rei Kawakubo in an exhibition view" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-4-effects" slide="cover" %}</figcaption>
</figure>


**Afirmación:** el filtrado, la mejora, la transformación del color y la corrección son operaciones bitmap centrales del postprocesado digital — las familias técnicas que nombra esta unidad antes de cualquier menú de filtros de marca (Gonzalez y Woods 2018).

Los currículos contemporáneos de dibujo digital combinan trabajo expresivo con variables de imagen fundamentales — valor, luz, textura y color — en lugar de tratar los efectos como un catálogo autónomo (Curcic 2024). Un efecto aplicado a una imagen es siempre una transformación con un **antes**; el riesgo de oficio es perder la pista de ese antes, no dominar un preset concreto.

**Qué sostiene y qué no.** Gonzalez y Woods (2018) sostienen la explicación técnica de píxeles, canales, filtros y corrección. Curcic (2024) sostiene pedagogía de taller basada en encargos donde los efectos sirven a problemas visuales. McBride et al. (2019) sostienen conciencia ética de imágenes publicitarias manipuladas — adyacente a la divulgación en moda, no una prescripción de política de aula. **Ninguna fuente revisada valida una secuencia de enseñanza de efectos o filtros** para moda en educación superior; la documentación de herramienta fundamenta operaciones — etiqueta `[PLATFORM]`, nunca investigación.

**Ancla de práctica (perspectiva de campo):** edición no destructiva, composición, máscaras y corrección tonal como clases de operación duraderas — separadas de la interfaz de cualquier aplicación.

**Señal de frontera (perspectiva de campo):** los píxeles generativos pueden oscurecer las decisiones visuales y los procesos de oficio en los que tradicionalmente descansa la crítica de taller (Park et al. 2025). Trata cualquier relleno asistido por IA como entrada al juicio, no como sustituto de nombrar qué cambió.

## Lab (Portfolio)

*Bloque de sesión · Una diapositiva geométrica anuncia el Lab: **dos** ejercicios. Todo lo que produzcas en Lab entra en tu **índice de portfolio**. Los Labs practican ideas de Masterclass y alimentan el oficio ACT — no son un segundo canal evaluable de Campus Virtual.*

### Ejercicio 1 — Contact sheet, then one photobash integration {#lab-exercise-1}

Practises Masterclass ideas **1** (keep the before) and **2** (a filter is an argument).

**Time:** 25 minutes.

**Group:** alone for integration; pairs OK for the rights/attribution check on the contact sheet.

**Materials:** ≤12 candidate stills you can attribute; bitmap editor with layers; timer.

**Steps:**

1. Grid candidate stills with attribution lines visible; strike anything you cannot attribute.
2. Only then enter the photobash canvas.
3. Cut and layer fragments so seams are intentional; unify light/colour with adjustment layers only (keep originals recoverable).
4. Check Gestalt grouping: what reads as one figure vs background noise?
5. Export flat + layered; list three integration decisions.

**Portfolio trace:** attributed contact sheet + flat export + layered file + three integration decisions.

**Judged by:** [Portfolio rubric — process evidence and craft]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (photobash craft gap — no Wave-1 verified primary pedagogy source).

**Example trace:** *(Illustrative · not student work.)* Before/after of one local adjustment with layer named `fx-dodge-cheek`; process note: “Effect is recoverable; flattened export discarded.”


### Ejercicio 2 — Before → after strip + disclosure {#lab-exercise-2}

Practises Masterclass ideas **1** (keep the before) and **3** (disclosure is part of craft).

**Time:** 15 minutes.

**Group:** alone.

**Materials:** your photobash or another effects master; timer.

**Steps:**

1. Save a dated before flat at the start of effects work (if you skipped it, restart from a recoverable layer).
2. Apply one purposeful transformation.
3. Build a horizontal before|after strip.
4. Caption the transformation in ≤12 words without hype.
5. Add one disclosure sentence: what changed, why, and what you refused to do.

**Portfolio trace:** before|after strip + disclosure sentence.

**Judged by:** [Portfolio rubric — authorship and disclosure]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (effects disclosure craft).

**Example trace:** *(Illustrative · not student work.)* Photobash seam marked; one sentence on light direction mismatch kept visible in the index.


**Definition of done:** before/after strip saved; disclosure line present; piece ID; process folder.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidence:** Investigaciones y proyectos 20% (pair); Cuaderno 10% (disclosure). No S1/S2 — ARTEFACT ROLE none.
LAB_LINE: exercise=1; method_id=photobash-integration; practises=masterclass-1,masterclass-2; source=gap/classroom adaptation; ACT=ACT2
LAB_LINE: exercise=2; method_id=compositing-before-after-strip; practises=masterclass-1,masterclass-3; source=gap/classroom adaptation; ACT=ACT2
-->
{% endif %}

---

## Workshop

Desde la sesión 4: el Workshop es tiempo de estudio protegido para D2 Transposición y D3 evento final (≈ mitad / mitad) — no es reloj de D1 Análisis.


1. **Diagnóstico.** Dada una imagen "después" sin "antes" conservado, nombra qué falta para un flujo de efectos honesto.
2. Escribe a mano la línea de divulgación para un efecto descrito, sin herramienta abierta. **Sin IA — declarado como tal.**
3. Distingue "efecto" de "manipulación" para un caso descrito, usando el marco de B1.

Los borradores de respuesta del profesor no se publican en esta página.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "traceable-transform — cada estado transformado permanece unido a una traza de declaración"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Conclusión

Esta unidad deja lagunas nombradas a propósito: lo que el vault puede verificar con página queda en Referencias; lo abierto queda en la Nota editorial. Mantén las trazas de Lab honestas en el índice de portfolio. No inventes un entregable evaluable que How to Pass no pide. La siguiente apuesta es el ritmo de sesión ya nombrado — defensa de Análisis (D1) desde la sesión 3; Workshop desde la sesión 4 para Transposición y el evento final.

---

## Tao de la imagen {#tao-of-the-image}

Epígrafe de la unidad (registro Tao de estudio — no es cita académica):

> _"El offset no es matemática — es empatía. Debes recordar lo que vino antes."_

Los enlaces del deck y de la lección a `#tao-of-the-image` resuelven aquí.

---

## Referencias

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.4; temario=T1-image-2d-volume.pass1.resultant.mdc § digital effects and post-processing; subfield_runs=dc-2d-image-craft-pedagogy/pass1.edited.md § 3 Digital effects
CRITICAL_ROUTING: unit=I.4; critica=C1 Crepax affective trends L119; T1 McBride retouch ethics; session disclosure threshold prompt
PROVENANCE_LINE: claim=I.4.claim.bitmap-operations; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="filtering enhancement colour transformation correction bitmap"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Gonzalez; similarity=null; proposed_use="technical anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Gonzalez Woods 2018 not in scholar vault; quote=none; public_citation="(Gonzalez and Woods 2018)"; supports="core bitmap post-processing operations"; does_not_support="fashion-specific filter pedagogy"
PROVENANCE_LINE: claim=I.4.claim.effects-not-catalogue; status=[BIBLIO-GAP]; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="digital drawing effects not autonomous catalogue Curcic"; source_locator=dc-2d-image-craft-pedagogy/pass1.edited.md L107; similarity=null; proposed_use="studio pedagogy anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.46328/ijtes.576 in PENDING-procurement no_oa; quote="rather than treating effects as an autonomous catalogue"; public_citation="(Curcic 2024)"; supports="effects embedded in visual problems"; does_not_support="fashion-specific effects sequence"
PROVENANCE_LINE: claim=I.4.claim.retouch-ethics; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="fashion beauty retouching ethical advertising images McBride"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § McBride; similarity=null; proposed_use="ethical critical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=McBride 2019 not in scholar vault; quote=none; public_citation="(McBride et al. 2019)"; supports="ethical awareness of manipulated advertising imagery"; does_not_support="classroom disclosure policy prescription"
PROVENANCE_LINE: claim=I.4.gap.effects-pedagogy-sequence; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion HE effects masking compositing pedagogy validated sequence"; source_locator=pass1.edited.md L115 UNVERIFIED; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated effects/filter teaching method for fashion students"
PROVENANCE_LINE: claim=I.4.emerging.genai-opacity; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=dc-2d-image-craft-pedagogy; knowledge_scope=field_prospection; query="GenAI studio critique opacity Park"; source_locator=pass1.edited.md L148; similarity=null; proposed_use="frontier signal"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Park IASDR 2025 not in scholar vault; quote=none; public_citation="(Park et al. 2025)"; supports="naming GenAI opacity in studio critique"; does_not_support="ban or mandate GenAI in effects assignments"
PROVENANCE_LINE: claim=I.4.critical.affective-trends; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="TikTok ASMR affective fashion trends digital circulation"; source_locator=C1-fashion-digital-world.pass1.resultant.mdc L119; similarity=null; proposed_use="critical platform aesthetics"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Crepax 2024 not in scholar vault; quote=none; public_citation="(Crepax 2024)"; supports="affect and audiovisual experience organise fashion trends"; does_not_support="which effects students should apply"
PROVENANCE_LINE: claim=I.4.critical.disclosure-threshold; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="effect manipulation disclosure consent refusal"; source_locator=i-4-effects.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming disclosure threshold as studio question"; does_not_support="empirical claim about cohort norms"
MEDIA_RIGHTS_LINE: slot=I.4.video.effect-breakdown; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.4.still.before-after; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.4.graphic.layer-stack; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de Innovación docente
{: .lesson-editorial-note }

**Laguna declarada — con claridad.** Ninguna fuente revisada valida una **secuencia de enseñanza de efectos o filtros** para moda en educación superior. Gonzalez y Curcic sostienen el marco técnico y de taller; McBride sostiene la lectura ética de imagen retocada; no prueban que este flujo de aula enseñe mejor que una alternativa.

Esta nota forma parte de una *Práctica de Innovación docente* en curso — los límites epistémicos van aquí, no entre párrafos de Masterclass.

---

## Autoría asistida por IA

Esta lección se redactó con asistencia local de IA bajo control editorial del autor. Declaración de uso de IA (alumnado y docencia): [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).

{% if site.publication.publish_internal_metadata %}
<!-- forge_date: 2026-09-22 · Studio: crea-comm.net · harness: local drafting tools v0.1 · prompt-v2.1
      lesson_uuid: 91dab705-35c9-48e8-ae51-c0c9cd9f705a
     vault_refs_consulted: 5
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
