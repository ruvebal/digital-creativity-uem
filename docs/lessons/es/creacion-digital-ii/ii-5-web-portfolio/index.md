---
layout: lesson
title: 'II.5 · Maquetación, edición y creación de web y portfolio digital'
title_en: 'II.5 · Web Layout, Editing & Digital Portfolio Creation'
slug: ii-5-web-portfolio
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-ii/ii-5-web-portfolio/
description: 'Maquetación de portfolio y web para comunicación de moda: hacer visible el proceso y la autoría, no solo el look terminado.'
status: scaffold
tags: [creacion-digital-ii, portfolio, web, autoria, ia-generativa-taller]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"Entender la documentación es entender el código. Entender el código es entender la mente que lo escribió."_
> — Tao of Development, `qa-010`
{: .tao-development-quote }

> **Declaración de asistencia de IA:** esta unidad está diseñada para un curso donde la IA generativa es una herramienta habitual de taller. Cada pieza que se coloca en un portfolio lleva un rastro de autoría, no solo una imagen terminada.

---

{% include lesson-semantic-graphic.html %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Maquetación, edición y creación de web y portfolio digital.*

**Competencias que sirve (`3-creacion-digital-ii.json`):** `CON1` (diferenciar las técnicas de representación audiovisual y sus medios de difusión), `HAB10` (diseñar la imagen de marca de una firma de moda), `COMP8` (manejar herramientas digitales de representación gráfica o audiovisual en la comunicación de ideas o proyectos de moda), `COMP9` (crear ideas nuevas a partir de conceptos conocidos, resolviendo problemas de forma original).

**Resultados de aprendizaje que sirve esta unidad** (verbatim del `learning_outcomes` de la guía, sin añadidos): *"Maquetar proyectos y trabajos de diseño con calidad profesional."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."* · *"Manejar formatos de archivo digitales propios y genéricos."*

**Pesos de evaluación a los que alimenta la evidencia de esta unidad** (CD II presencial, framework §6): **Investigaciones y proyectos 20%** es donde se puntúa directamente el entregable de portfolio de esta unidad; su rastro de proceso (decisiones, iteraciones, declaración de IA) puede alimentar también **Cuaderno de prácticas de laboratorio/taller 10%**. Esta unidad no toca Pruebas (55%) ni Caso/problema (15%).

---

## 🎯 Objetivos de aprendizaje

Al final de esta unidad podrás:

- **Maquetar una página de portfolio** con calidad profesional, no una rejilla de relleno.
- **Hacer visible el proceso** — las decisiones, iteraciones y el uso de herramientas forman parte de lo que comunica la página, no son un añadido final.
- **Declarar el uso de IA con honestidad** — nombrar qué piezas usaron un generador, para qué, y qué cambiaste después.
- **Distinguir co-creación de borrado de autoría** — dónde está el límite cuando un look se hizo *con* un generador.
- **Entender el límite de la exhibición** — qué hace falta, formalmente, para que una pieza salga de tu propia carpeta y aparezca en una página pública del showroom.

---

## Por qué existe esta unidad: el proceso y la autoría deben ser visibles

**Afirmación:** una página de portfolio es evaluable cuando su proceso y su autoría son visibles en la página, no simplemente cuando las imágenes parecen terminadas. Un acabado sin rastro no es el resultado de aprendizaje que enseña esta unidad.

Una revisión sistemática de IA generativa en educación de moda basada en taller identifica la identidad y autoría del aprendiz como uno de los pilares que configuran la pedagogía de taller, junto con la construcción de conocimiento, la práctica docente y la cultura y ética de estudio, y nombra la tensión directamente: la IA generativa aporta "mayor ideación creativa y eficiencia" junto con "preocupaciones sobre originalidad, responsabilidad ética y acceso equitativo" (Anwar, Raza y Marzouk 2025, 1).

Rizzi y Bertola plantean el diseño de moda asistido por IA no como sustitución de autoría sino como **complemento**: la IA se trata como "suplemento a la creatividad humana natural", con dinámicas colaborativas que recorren *todo* el proceso, no una fase aislada (Rizzi y Bertola 2025, 10).

Garcia estudió un curso de diseño y desarrollo web en el que 176 estudiantes completaron tareas semanales de código hasta producir un portfolio digital autocodificado. El estudio trata el portfolio como evidencia de competencias técnicas y como artefacto de aprendizaje, no solo como contenedor de piezas. Es un análogo de curso técnico útil para exigir trazabilidad de proceso; su diseño de un solo grupo y su contexto informático **no** prueban qué patrón de UX, accesibilidad o presentación funciona mejor para un portfolio de moda (Garcia 2025, 2, 4).

**Qué apoya esto, y qué no.** Anwar et al. (2025), Rizzi y Bertola (2025) y Garcia (2025) apoyan hacer visible la autoría y el proceso cuando la IA generativa forma parte del taller, e integrar la construcción del portfolio con tareas técnicas. **Ninguna fuente revisada valida qué patrones concretos de UX web de portfolio de moda producen mejor comunicación, visibilidad o contratación** — la guía de maquetación de abajo es oficio profesional, no investigación.

**Ancla de práctica (perspectiva de campo):** estructura HTML semántica, arquitectura de información, maquetación responsive, texto alternativo, créditos y rastro de proceso como operaciones de publicación duraderas — separadas de cualquier generador de sitios estáticos o plataforma de alojamiento.

**Señal de frontera (perspectiva de campo):** los generadores de portfolio con IA y los constructores de sitios en un clic pueden producir acabado más rápido que la validación pedagógica; trata cualquier página generada como entrada al juicio, no como prueba de que la autoría está declarada con honestidad.

## Perspectiva crítica

Descolonizar la enseñanza de moda no equivale a añadir ejemplos diversos a un canon intacto: requiere examinar cómo colonialidad, posición docente, afecto y autoridad estructuran aquello que la disciplina reconoce como conocimiento de moda (Cheang y Suterwalla 2020).

Un portfolio es autopresentación y evidencia, mientras plataformas y empleadores a menudo premian métricas de visibilidad por encima del rastro de proceso. Quién decide qué prueba cuenta — el render terminado, el registro de colaboración, la declaración de herramientas — no es neutral: la tensión de autoría en plataformas se sitúa entre lo que la página *muestra* y lo que puede *probar* sobre quien la hizo.

### La pregunta de debate

¿Qué cuenta como "el trabajo" cuando un look se co-creó con un generador? La tensión de autoría de Anwar et al. y el planteamiento de "suplemento, no sustituto" de Rizzi y Bertola son dos respuestas distintas — el taller debe alcanzar su propia postura, por escrito, antes de que venza el entregable de portfolio.

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.video.portfolio-walkthrough" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador abstracto para recorrido de proceso de portfolio; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> un recorrido breve prueba si la navegación, la evidencia del case study y los supuestos de mantenimiento son legibles.</p>
<p><strong>Qué observar:</strong> rastro de proceso frente a presentación solo-imagen — qué puede y qué no puede probar cada una.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.still.process-exemplar" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador para ejemplo de portfolio con proceso y contraejemplo solo-imagen; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> páginas en paralelo prueban legibilidad de autoría, texto alternativo y evidencia de proceso inspeccionable.</p>
<p><strong>Qué observar:</strong> propósito de oficio frente a pulido que oculta la colaboración.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.5.graphic.portfolio-ia" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-05-portfolio-evidence-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador de diagrama para inicio a case study a proceso a declaración de autoría; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> mapea inicio → obra seleccionada → case study → proceso → about/contacto, más un bloque de declaración de autoría.</p>
<p><strong>Qué observar:</strong> dónde deben aparecer las líneas de uso de IA y crédito antes de que la página se lea como terminada.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

Cubierto arriba: marco Anwar/Rizzi/Garcia, perspectiva crítica, debate y marcadores.

### Qué significa "proceso visible" en una página, en concreto

Una pieza de portfolio que solo muestra el render final responde "¿qué hiciste?". Una pieza de portfolio con rastro de proceso responde también "¿cómo lo hiciste, y qué decidiste?". El rastro mínimo para esta unidad:

1. **El brief** — una frase sobre para qué era la pieza.
2. **El proceso** — 2–4 imágenes o notas de proceso (boceto → pase 3D/IA → refinamiento → final), no solo un antes/después.
3. **La línea de uso de IA** — qué herramienta(s), para qué paso, y qué cambiaste después. "Ninguna" es una respuesta válida y honesta.
4. **La línea de crédito** — tu nombre (o nombre de diseñador elegido, ver S2 abajo) y cualquier colaborador.

### Estructura de página de portfolio — **Template**, adapta a tu propio contenido

```html
<!-- Template: sustituye todo el contenido entre corchetes -->
<article class="portfolio-piece">
	<h2>[Título de la pieza]</h2>
	<p class="brief">[Brief en una frase: ¿para qué era esta pieza?]</p>

	<div class="process-trail">
		<h3>Proceso</h3>
		<img src="[boceto.jpg]" alt="[Descripción del boceto inicial]" />
		<img src="[iteracion.jpg]" alt="[Descripción de la iteración intermedia]" />
		<img src="[final.jpg]" alt="[Descripción de la pieza final]" />
	</div>

	<div class="ai-declaration">
		<h3>Uso de IA</h3>
		<p>[Nombre de la herramienta] se usó para [paso concreto]. [Qué cambiaste o verificaste después. O: "No se usaron herramientas de IA en esta pieza."]</p>
	</div>

	<p class="credit">[Tu nombre o nombre de diseñador elegido] · [fecha]</p>
</article>
```

### Estructura mínima de página — **Template**

```html
<!DOCTYPE html>
<html lang="es">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>[Tu nombre] — Portfolio</title>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<header>
			<h1>[Tu nombre o nombre de diseñador elegido]</h1>
			<nav><!-- enlaces a cada pieza --></nav>
		</header>
		<main>
			<!-- un <article class="portfolio-piece"> por pieza -->
		</main>
	</body>
</html>
```

El nivel de calidad es la frase de la propia guía: *"calidad profesional"* — no un curso de meta-framework de Front-End. Una página HTML/CSS estática que carga correctamente, se lee con claridad, y lleva el rastro de proceso de arriba cumple el nivel. No necesitas Astro, React ni un paso de build para aprobar esta unidad.

---

## B2 · Taller — talleres 3 h + investigaciones y proyectos 4 h (contextualizado, tipo entorno laboral)

**Entregable:** una página de portfolio (o pequeño sitio estático) que maqueta tu propio trabajo de Creación Digital con rastro de proceso y declaración de uso de IA, siguiendo la estructura de arriba.

**Definición de terminado:**
- La página existe, en local o alojada, con al menos una pieza completa siguiendo la estructura de arriba.
- Cada pieza tiene un ID de pieza (un slug corto que eliges, p. ej. `look-03-denim-hibrido`) y una carpeta de proceso (bocetos, renders intermedios, notas) — se conserva aunque no se publique todo.
- Hay una declaración de uso de IA para cada pieza, incluidas las piezas donde no se usó IA.
- **No se requiere una URL pública en el showroom.** Este entregable puede estar completo y evaluarse enteramente dentro de tu propia carpeta.

**Si quieres que una pieza se exhiba públicamente** (vShowroom, un espacio compartido que esta cohorte puede llegar a poblar como usuarios reales — ver la página de track), adjunta ahora la lista de verificación de consentimiento **sin firmar** de abajo a la carpeta de proceso de esa pieza. Rellenarla no es lo mismo que firmarla — son borradores para que entiendas qué requeriría la exhibición, no un proceso de consentimiento activo. Todavía no existe aprobación del DPO; nada aquí autoriza una publicación real.

### S1 — Exhibir esta pieza en vShowroom (borrador sin firmar — no firmar)

**Pieza / piece ID:** _________________
**Tipo:** still / avatar / look / video / otro: _______

- [ ] Autorizo a Universidad Europea / los operadores de vShowroom a **mostrar** esta pieza en el showroom (web). Conservo el copyright.
- [ ] La licencia es **revocable**. Tras la retirada, la página pública se retira en un plazo definido por DPO/operaciones (se sugieren 14 días). Las copias en caché pueden persistir brevemente.
- [ ] Esto **no** es una venta, ni un derecho de VTON/prueba virtual, ni un derecho a entrenar modelos con mi trabajo.

Nombre · Fecha · Firma — *(plantilla sin firmar; no es un instrumento de consentimiento activo)*

### S2 — Atribución vs. anonimato (borrador sin firmar — no firmar)

Por defecto: **atribuido** (nombre como lo escribe el estudiante).

- [ ] Mostrar mi nombre / nombre de diseñador elegido: _________________
- [ ] Exhibir **sin** mi nombre civil (solo ID de pieza)

S2 sin S1 no hace nada. S1 sin S2 se atribuye por defecto.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
**Evidencia:** Investigaciones y proyectos 20% (entregable de portfolio); Cuaderno 10% (rastro de proceso + declaración de IA). S1/S2 requeridos solo antes de uso público en vShowroom.
Las referencias a herramientas en esta unidad (cualquier generador de sitios estáticos, editor de imagen o plataforma de alojamiento) son notas de plataforma fechadas, no citas de investigación — comprueba las versiones antes de clase.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, descontextualizado

No es el entregable de portfolio. Problemas cortos que aíslan una habilidad cada uno:

1. **Diagnóstico.** Dado este fragmento HTML roto, indica qué falla y corrígelo:

   ```html
   <!-- Excerpt — roto, solo para diagnóstico -->
   <img src="retrato.jpg" />
   <div>
     <h4>Look 02</h4>
     <p>Borrador de patrón digital, sin editar</p>
   </div>
   ```

   (Pista: sintácticamente no hay nada mal aquí — el problema es lo que *falta* para una imagen que comunica significado en una página de portfolio. Nómbralo y añádelo.)

2. Dada esta descripción de pieza — *"Un estudiante usó un generador para producir una imagen de look completo a partir de un prompt de texto, no hizo más ediciones, y solo se acreditó a sí mismo"* — identifica qué falta en una declaración honesta de uso de IA para esta pieza.

3. **Sin IA, declarado:** sin asistencia de IA, escribe una declaración de uso de IA de dos frases para una pieza donde bocetaste a mano, usaste una herramienta de IA para generar tres variantes de color, y seleccionaste y refinaste una manualmente a mano.

Los bocetos de respuesta del profesor no se publican en esta página — se conservan en notas privadas del instructor.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "portfolio-lineage — fragmentos de proceso convergen en una página verificable con autoría visible"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Referencias

- Anwar, S., A. Raza y R. Marzouk. 2025. “Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.” *European Journal of Business and Management*. https://doi.org/10.65136/ejbm.v10i4.24.
- Cheang, Sarah, y Shehnaz Suterwalla. 2020. “Decolonizing the Curriculum? Transformation, Emotion, and Positionality in Teaching.” *Fashion Theory* 24 (6): 879–900. https://doi.org/10.1080/1362704X.2020.1800989.
- Garcia, M. B. 2025. “Self-Coded Digital Portfolios as an Authentic Project-Based Learning Assessment in Computing Education: Evidence from a Web Design and Development Course.” *Education Sciences* 15 (9): 1150. https://doi.org/10.3390/educsci15091150.
- Rizzi, G. y P. Bertola. 2025. “Exploring the Generative AI Potential in the Fashion Design Process.” *European Journal of Cultural Management and Policy*. https://doi.org/10.3389/ejcmp.2025.13875.

**Vacío declarado — en claro.** Anwar et al. (2025), Rizzi y Bertola (2025) y Garcia (2025) apoyan la visibilidad de autoría y el encuadre portfolio-como-evidencia; **no** prueban que la maquetación HTML, las elecciones de accesibilidad o la estructura de portfolio de esta unidad produzcan mejor comunicación, visibilidad o contratación en moda. Ninguna fuente revisada valida resultados de UX web de portfolio de moda para HE.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=II.5; temario=T2-retouch-video-portfolio.pass1.resultant.mdc § portfolio; subfield_runs=dc-fashion-portfolio-web-ux gap NONE
CRITICAL_ROUTING: unit=II.5; critica=C3 Cheang decolonizing curriculum L277; C1 platform authorship tension; session proof-beyond-polish prompt
PROVENANCE_LINE: claim=II.5.claim.genai-authorship-pillar; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="generative AI studio fashion education authorship Anwar"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Anwar; similarity=null; proposed_use="authorship anchor"}; source={document_coat=0598ec0e; extraction_db=ahmes-library/scholar/documents/generative_ai_in_studio_based_fashion_education_a_systematic_literature_review_0598ec0e/extract/extraction.db; node_id=c9a17328-72f7-56c8-95bf-b9860b1067b8; page_index=0; printed_page=1}; resolver="ahmes query --cite extraction.db:c9a17328-72f7-56c8-95bf-b9860b1067b8 --require-evaluator-safe evaluator_safe=yes"; quote="Learner Identity & Authorship"; public_citation="(Anwar, Raza, and Marzouk 2025, 1)"; supports="GenAI changes studio authorship; visibility is honest response"; does_not_support="which portfolio layout teaches best"
PROVENANCE_LINE: claim=II.5.claim.genai-complement; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="generative AI complement human creativity fashion design Rizzi"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Rizzi; similarity=null; proposed_use="complement anchor"}; source={document_coat=167816a4; extraction_db=ahmes-library/scholar/documents/exploring_the_generative_ai_potential_in_the_fashion_design_process_167816a4/extract/extraction.db; node_id=908f5339-781d-51cc-a803-47dfbf9c0677; page_index=9; printed_page=10}; resolver="ahmes query --cite extraction.db:908f5339-781d-51cc-a803-47dfbf9c0677 --require-evaluator-safe evaluator_safe=yes"; quote="supplement to natural human creativity"; public_citation="(Rizzi and Bertola 2025, 10)"; supports="AI as complement across whole process"; does_not_support="originality guarantee or hiring effect"
PROVENANCE_LINE: claim=II.5.claim.portfolio-pbl-analogue; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="self-coded digital portfolios web design Garcia"; source_locator=T2-retouch-video-portfolio.pass1.resultant.mdc § Garcia; similarity=null; proposed_use="technical analogue"}; source={document_coat=educsci15091150; extraction_db=ahmes-library/scholar/documents/self_coded_digital_portfolios_as_an_authentic_project_based_learning_assessment_e09e72ca/extract/extraction.db; node_id=e09e72ca-5a4b-51dc-823a-1d05ea71ee8f; page_index=1; printed_page=2}; resolver="ahmes query --cite extraction.db:e09e72ca-5a4b-51dc-823a-1d05ea71ee8f --require-evaluator-safe evaluator_safe=yes"; quote="self-coded digital portfolio"; public_citation="(Garcia 2025, 2, 4)"; supports="portfolio as learning artifact and technical evidence"; does_not_support="fashion UX outcomes accessibility hiring causality"
PROVENANCE_LINE: claim=II.5.gap.fashion-portfolio-ux; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="fashion portfolio web UX hiring outcomes"; source_locator=grounding/README.md row II.5; similarity=null; proposed_use="honest gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated fashion-portfolio layout or hiring effect"
PROVENANCE_LINE: claim=II.5.critical.decolonizing-curriculum; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="decolonizing curriculum fashion teaching Cheang Suterwalla"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc L277; similarity=null; proposed_use="critical theoretical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.1080/1362704X.2020.1800989 not in scholar vault; quote=none; public_citation="(Cheang and Suterwalla 2020)"; supports="decolonisation requires examining canon construction not additive diversity"; does_not_support="mandatory reading list assignment"
PROVENANCE_LINE: claim=II.5.critical.platform-authorship; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="portfolio proof beyond polish platform visibility"; source_locator=ii-5-web-portfolio.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming platform authorship tension"; does_not_support="employment outcome claim"
MEDIA_RIGHTS_LINE: slot=II.5.video.portfolio-walkthrough; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.5.still.process-exemplar; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.5.graphic.portfolio-ia; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}
