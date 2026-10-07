---
layout: lesson
title: 'I.2 · Tecnología digital 2D: Herramientas de dibujo'
title_en: 'I.2 · 2D Digital Technology: Drawing Tools'
slug: i-2-dibujo-2d
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-i/i-2-dibujo-2d/
description: 'El dibujo exterioriza el pensamiento visual — pedagogía de taller por tareas que integra la técnica de software en problemas visuales, con lagunas declaradas para secuencias específicas de moda.'
status: scaffold
tags: [creacion-digital-i, dibujo-2d, ilustracion-vectorial, croquis-moda]
deck_url: /tracks/dci/i-2-2d-drawing/
references: [huppauf-wulf-2009, rubin-2023]
---

{% if site.publication.publish_internal_metadata %}
<!--  curriculum-internal:
description: 'El dibujo vectorial como disciplina de describir la forma como relación, no como píxeles — unidad de laguna declarada: ninguna fuente del vault valida una secuencia de enseñanza de herramientas de dibujo.'
-->
{% endif %}

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"El SVG escala infinitamente, y sigue siendo exactamente lo que es. Sé como el SVG."_
<!-- Ajuste TTDO: ajuste directo — el dibujo vectorial es exactamente esa propiedad de "escalar sin perder identidad" que enseña esta unidad. -->
> — Tao of Development, `img-004`
{: .tao-development-quote }

---

{% include lesson-semantic-graphic.html %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Tecnología digital 2D: Herramientas de dibujo.*

**Competencias que sirve:** `CON1`, `HAB9`, `COMP8`, `COMP9` (mismo conjunto que I.1 — ver esa unidad para el texto completo).

**Resultados de aprendizaje:** *"Seleccionar las herramientas de dibujo vectorial aplicadas al diseño y la comunicación"* — la única frase de `learning_outcomes` de la guía que nombra directamente el anclaje de esta unidad.

**Presentación en clase:** [Diapositivas I.2]({{ '/tracks/dci/i-2-2d-drawing/' | relative_url }})

**Cada clase ordinaria:** Análisis → Masterclass → **Lab (Portfolio)** → **Workshop (Entregable)**. Lab ≠ Workshop. Ver [Cómo aprobar]({{ '/tracks/dci/how-to-pass-this-track/' | relative_url }}).

**Pesos de evaluación:** Investigaciones y proyectos 20% puntúa la pieza de taller; Cuaderno 10% puede tomar la nota de proceso. Pruebas (55%) y Caso/problema (15%) no se tocan aquí.

---

## Objetivos de aprendizaje

- **Describir el dibujo vectorial como una relación** (puntos de anclaje, curvas, rellenos) y no como una cuadrícula de píxeles.
- **Explicar el dibujo digital en taller por tareas** como el modelo pedagógico contemporáneo más claro para integrar técnica de software en problemas visuales en vez de comandos aislados (Curcic 2024).
- **Producir una ilustración vectorial de una silueta de moda sencilla** con **tres alternativas visiblemente distintas** y una breve justificación de selección.
- **Distinguir una función de herramienta de un concepto de dibujo transferible** y nombrar lo que sigue sin validar para secuencias 2D específicas de moda.

---

## Análisis
### Perspectiva crítica

Los propios manuales con los que se enseña moda pueden constituir una infraestructura de exclusión: análisis sistemáticos encuentran sesgos simultáneos de raza, género y cuerpo antes de que el estudiante llegue a producir obra propia — audita quién cuenta como cuerpo «normal», diseñador legítimo y sujeto de moda antes de fijar briefs (Reddy-Best et al. 2018).

La fluidez con herramientas puede premiar el acceso previo a hardware, software y convenciones de taller más que el juicio de dibujo. Nombra una alternativa de baja tecnología o una barrera de acceso que tu flujo da por sentada, y qué cualidades de línea tu rúbrica trata como «profesionales» por defecto.

### La pregunta de debate

**¿Empezar por lo vectorial (en vez de por el dibujo libre en mapa de bits) cambia lo que un principiante nota sobre la silueta de una prenda?** Curcic enmarca la habilidad previa heterogénea como problema de calibración sin resolver; la evidencia de taller de hoy es el único dato específico de moda en la sala.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.2.video.drawing-process" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-02-drawing-thinking-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador abstracto para captura de decisiones de dibujo vectorial; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> un clip breve de proceso permite congelar el instante en que un trazado o capa cambia la silueta.</p>
<p><strong>Qué observar:</strong> elección de herramienta, reversibilidad y orden de capas — no fidelidad a marca.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.2.still.contour-exemplar" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-02-drawing-thinking-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador para ejemplos de contorno vectorial y textura raster; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> ejemplos en paralelo separan contorno legible de textura que oculta la silueta.</p>
<p><strong>Qué observar:</strong> jerarquía de línea y legibilidad constructiva.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.2.graphic.revision-loop" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-i-02-drawing-thinking-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador de diagrama para bucle brief-línea-capa-revisión-exportación; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> mapea el bucle de revisión que evalúa esta unidad: alternativas, justificación, exportación.</p>
<p><strong>Qué observar:</strong> dónde divergen y convergen las ramas raster y vector.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

---



Cubierto arriba: marco Curcic, vector como relación, auditoría crítica, debate y marcadores de proyección. Las demostraciones de herramienta siguen siendo mínimas y etiquetadas `[PLATFORM]`.

---

## Masterclass

<figure class="lesson-figure" id="figure-masterclass-1" markdown="0">
<img src="{{ '/assets/images/deck-media/3e1406d573d0b92f.webp' | relative_url }}" alt="Costumes civils HISTORICAL CLOTHING OF FRANCE civilian costumes male female dress fashion design c 1640-1925 Public domain French illustration Larousse du XXème siècle 1932.jpg" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-1" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-2" markdown="0">
<img src="{{ '/assets/images/deck-media/a9a618606b3c129a.webp' | relative_url }}" alt="Vector graphic scaling 2.png" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-2" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-3" markdown="0">
<img src="{{ '/assets/images/deck-media/6b29a718e96503e0.webp' | relative_url }}" alt="The composite capital in perspective." loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-3" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-4" markdown="0">
<img src="{{ '/assets/images/deck-media/c394ec960555ef46.webp' | relative_url }}" alt="The The Designer Women’s Magazine, July 1922 cover, illustration by Edward Mason Eggleston.png" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-4" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-5" markdown="0">
<img src="{{ '/assets/images/deck-media/57d691cb5d3028d5.webp' | relative_url }}" alt="Vector graphic design made with Inkscape.svg" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-5" %}</figcaption>
</figure>

<figure class="lesson-figure" id="figure-masterclass-6" markdown="0">
<img src="{{ '/assets/images/deck-media/a8e81ebc3c86799c.webp' | relative_url }}" alt="Raster graphic fish 40x46 20x23 overlay hdtv-sdtv-example.png" loading="lazy" decoding="async">
<figcaption>{% include lesson-figure.html deck="i-2-2d-drawing" slide="masterclass-6" %}</figcaption>
</figure>


**Afirmación:** el modelo pedagógico contemporáneo más claro es el aprendizaje en taller por tareas en el que la técnica de software se integra en problemas visuales en lugar de enseñarse solo como comandos aislados. El estudio de Dibujo Digital de Curcic en educación superior combina explícitamente dibujo libre a mano alzada en mapa de bits con línea, volumen, valor, luz, textura, color, perspectiva y composición, junto con técnicas vectoriales; las tareas rediseñadas ajustadas al punto de partida del alumnado mejoraron los resultados (Curcic 2024).

El dibujo vectorial en este curso se enseña como **pensamiento visual exteriorizado** — puntos de anclaje, curvas y revisión visibles antes del acabado — no como fluidez de botones. Las convenciones del dibujo de moda (proporción, croquis, planos) aportan una gramática visual transferible tanto a mano, mapa de bits o vector (Abling 2023).

**Qué sostiene esto y qué no.** Curcic (2024) sostiene el rediseño de tareas, la dificultad diferenciada y la separación entre competencia de software y fundamentos artísticos. **No** establece una secuencia de enseñanza de herramientas 2D *específica de diseño de moda* validada; la literatura de pedagogía de moda sigue siendo escasa en una «pedagogía del dibujo digital» nombrada (Yu 2025). La documentación de herramienta fundamenta *cómo* funciona el software — etiqueta `[PLATFORM]`, nunca investigación.

**Anclaje de práctica (perspectiva de campo):** pedagogía de taller por tareas y fundamentos visuales dentro de flujos raster/vector (Curcic 2024).

**Señal de frontera (perspectiva de campo):** la ideación de moda se desplaza hacia boceto colaborativo humano–IA y generación controlable. Cualquier variante de IA es entrada al juicio, no sustituto de decisiones de dibujo — la evidencia de aula sobre boceto con IA sigue siendo una laguna de investigación abierta.

## Lab (Portfolio)

*Bloque de sesión · Una diapositiva geométrica anuncia el Lab: **dos** ejercicios. Todo lo que produzcas en Lab entra en tu **índice de portfolio**. Los Labs practican ideas de Masterclass y alimentan el oficio ACT — no son un segundo canal evaluable de Campus Virtual.*

### Ejercicio 1 — Croquis proportion scaffold {#lab-exercise-1}

Practises Masterclass ideas **1** (drawing as thinking) and **4** (fashion visual grammar).

**Time:** 20 minutes.

**Group:** alone.

**Materials:** vector or raster drawing app; tablet or mouse; timer; your I.1 scaffold if you have it.

**Steps:**

1. Choose a head-count or grid scaffold and draw it alone first.
2. Place landmarks (shoulder, waist, hip, knee) before contour.
3. Trace a second pass for garment only on a separate layer.
4. Compare scaffold vs finish; mark one collapsed decision.
5. Keep construction marks visible in the export.

**Portfolio trace:** scaffold layer + garment layer pair; one sentence on the landmark that locked the pose.

**Judged by:** [Portfolio rubric — process evidence and craft]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation (croquis / Abling page cite held).

**Example trace:** *(Illustrative · not student work.)* Scaffold layer with shoulder/waist/hip landmarks; garment layer only on a second pass; sentence: “Hip landmark locked the pose before any sleeve finish.”


### Ejercicio 2 — Three alternatives, then construction vs finish {#lab-exercise-2}

Practises Masterclass ideas **6** (three alternatives) and **2** (vector as relationship).

**Time:** 25 minutes (about 15 for alternatives, 10 for the audit + peer check).

**Group:** alone for the alternatives; one peer for the hide-finish check.

**Materials:** your silhouette file; colour for coding lines; timer.

**Steps:**

1. Make three visibly different versions of the silhouette.
2. Score novelty and fit (1–5). Rank and defend the winner in one paragraph.
3. On the winner, colour-code **construction** lines vs **finish** lines.
4. Hide finish; ask a peer what garment they still understand.
5. Restore finish only where it adds information. Write one sentence: which line type carried the silhouette.

**Portfolio trace:** three versions + scoring sheet + construction/finish audit + defence paragraph.

**Judged by:** [Portfolio rubric — selection and judgement]({{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}#rubric)

**Source:** Classroom adaptation for the three-alternative drill; critical frame that imagination ≠ creativity ≠ fantasy [(Hüppauf and Wulf 2009, 32)](#ref-huppauf-wulf-2009) — do not treat “more finish” as “more creative.”

**Example trace:** *(Illustrative · not student work.)* Three silhouettes scored 3/4/5 on novelty·fit; winner colour-coded construction (blue) vs finish (black); peer: “I still read a coat when finish is hidden.”


{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
LAB_LINE: exercise=1; method_id=croquis-proportion-scaffold; practises=masterclass-1,masterclass-4; source=held/classroom adaptation; ACT=ACT1
LAB_LINE: exercise=2; method_id=construction-vs-finish-lines; practises=masterclass-2,masterclass-6; source=huppauf-wulf-2009 p.32 (critical frame, verified) + classroom steps; ACT=ACT1
-->
{% endif %}

---

## Workshop

Desde la sesión 4: el Workshop es tiempo de estudio protegido para D2 Transposición y D3 evento final (≈ mitad / mitad) — no es reloj de D1 Análisis.


1. **Diagnóstico.** Dado un trazado vectorial con un manejador de curva visiblemente incorrecto, identifica qué está mal y qué haría un manejador correcto.
2. Describe, por escrito y sin ninguna herramienta abierta, cómo construir una forma vectorial sencilla a partir de primitivas. **Sin IA — declarado como tal.**
3. Explica por qué "lo dibujé en una app de mapa de bits" no satisface el anclaje CONTENIDOS de esta unidad.

Los borradores de respuesta del profesor no se publican en esta página.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "curve-diagnosis — manejadores expuestos conducen de un trazado fallido a una curva intencional"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Conclusión

Esta unidad deja lagunas nombradas a propósito: lo que el vault puede verificar con página queda en Referencias; lo abierto queda en la Nota editorial. Mantén las trazas de Lab honestas en el índice de portfolio. No inventes un entregable evaluable que How to Pass no pide. La siguiente apuesta es el ritmo de sesión ya nombrado — defensa de Análisis (D1) desde la sesión 3; Workshop desde la sesión 4 para Transposición y el evento final.

---

## Tao de la imagen {#tao-of-the-image}

Epígrafe de la unidad (registro Tao de estudio — no es cita académica):

> _"El SVG escala infinitamente, y sigue siendo exactamente lo que es. Sé como el SVG."_

Los enlaces del deck y de la lección a `#tao-of-the-image` resuelven aquí.

---

## Referencias

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.2; temario=T1-image-2d-volume.pass1.resultant.mdc § "Herramientas y flujos de dibujo digital 2D"; subfield_runs=dc-2d-image-craft-pedagogy/20260816/pass1.edited.md; adjacent=T1 Abling/Smith/Cheng (craft literacy, not sequence proof)
CRITICAL_ROUTING: unit=I.2; critica=C3-gender-minorities-silences.pass1.resultant.mdc § Classroom implication L265 Reddy-Best; C1 tool/access (session prompt field tension)
PROVENANCE_LINE: claim=I.2.claim.studio-assignment-pedagogy; status=[BIBLIO-GAP]; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="digital drawing assignment redesign higher education Curcic"; source_locator=dc-2d-image-craft-pedagogy/pass1.edited.md L8; similarity=null; proposed_use="primary pedagogy anchor"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.46328/ijtes.576 in PENDING-procurement no_oa — no extraction.db to enrich; quote="redesigned assignments matched to students' starting drawing ability produced improved outcomes"; public_citation="(Curcic 2024)"; supports="studio-based assignment-driven digital drawing pedagogy"; does_not_support="fashion-specific classroom sequence or vector-first superiority"
PROVENANCE_LINE: claim=I.2.claim.visual-grammar; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/02-temario-contenidos; knowledge_scope=field_prospection; query="fashion drawing conventions croquis flats"; source_locator=T1-image-2d-volume.pass1.resultant.mdc § Abling; similarity=null; proposed_use="transferable visual grammar"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Abling 2023 not in scholar vault; quote=none; public_citation="(Abling 2023)"; supports="fashion drawing conventions transfer to digital tools"; does_not_support="digital-tool pedagogy efficacy"
PROVENANCE_LINE: claim=I.2.gap.fashion-specific-sequence; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion design digital drawing pedagogy validated sequence"; source_locator=null; similarity=null; proposed_use="gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated fashion-HE 2D tool teaching method"
PROVENANCE_LINE: claim=I.2.emerging.genai-sketching; status=[BIBLIO-GAP]; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="generative AI collaborative fashion ideation sketching education"; source_locator=MASTER-IDEAS I.2; similarity=null; proposed_use="frontier signal only"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming human-AI sketching as open question"; does_not_support="classroom prescription for GenAI drawing"
PROVENANCE_LINE: claim=I.2.critical.textbook-audit; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="fashion textbooks race gender body"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc § Classroom implication; similarity=null; proposed_use="critical studio practice"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=Reddy-Best 2018 not in scholar vault; quote=none; public_citation="(Reddy-Best et al. 2018)"; supports="auditing studio reference infrastructure"; does_not_support="validated efficacy of audit assignment"
PROVENANCE_LINE: claim=I.2.critical.tool-access; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="digital drawing tool access studio conventions"; source_locator=i-2-2d-drawing.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming access and rubric defaults as studio questions"; does_not_support="empirical claim about access barriers in this cohort"
MEDIA_RIGHTS_LINE: slot=I.2.video.drawing-process; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.2.still.contour-exemplar; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=I.2.graphic.revision-loop; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de Innovación docente
{: .lesson-editorial-note }

**Laguna declarada — con claridad.** Curcic (2024) es dibujo digital en educación superior, no una secuencia de herramientas validada específica de moda. Yu (2025) señala que la literatura de pedagogía de diseño de moda sigue siendo limitada. No cites esta unidad como prueba de que vectorial primero supera a mapa de bits en moda.

Esta nota forma parte de una *Práctica de Innovación docente* en curso — los límites epistémicos van aquí, no entre párrafos de Masterclass.

---

## Autoría asistida por IA

Esta lección se redactó con asistencia local de IA bajo control editorial del autor. Declaración de uso de IA (alumnado y docencia): [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).

{% if site.publication.publish_internal_metadata %}
<!-- forge_date: 2026-09-22 · Studio: crea-comm.net · harness: local drafting tools v0.1 · prompt-v2.1
      lesson_uuid: 460fdfe8-d4bb-4415-bdb1-ea1402d1c984
     vault_refs_consulted: 4
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
