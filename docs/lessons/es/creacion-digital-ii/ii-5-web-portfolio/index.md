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
status: draft
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

> **Declaración de asistencia de IA:** esta unidad está diseñada para un curso donde la IA generativa es una herramienta habitual de taller. Cada pieza que se coloca en un portfolio lleva un rastro de autoría, no solo una imagen terminada.

---

## Convenciones de código en esta unidad

- **CodeSandbox-ready** — archivo completo, se copia y pega, funciona tal cual.
- **Excerpt** — patrón parcial, ilustrativo. **No** funciona tal cual.
- **Template** — copiar y sustituir los valores marcados antes de usar.

Los bloques HTML/CSS de esta unidad están etiquetados individualmente; la mayoría son **Template** — una estructura de partida para adaptar a tu propio contenido de portfolio, no un sitio terminado.

---

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Maquetación, edición y creación de web y portfolio digital.*

**Competencias que sirve (`3-creacion-digital-ii.json`):** `CON1` (diferenciar las técnicas de representación audiovisual y sus medios de difusión), `HAB10` (diseñar la imagen de marca de una firma de moda), `COMP8` (manejar herramientas digitales de representación gráfica o audiovisual en la comunicación de ideas o proyectos de moda), `COMP9` (crear ideas nuevas a partir de conceptos conocidos, resolviendo problemas de forma original).

**Resultados de aprendizaje que sirve esta unidad** (verbatim del `learning_outcomes` de la guía, sin añadidos): *"Maquetar proyectos y trabajos de diseño con calidad profesional."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."* · *"Manejar formatos de archivo digitales propios y genéricos."*

**Pesos de evaluación a los que alimenta la evidencia de esta unidad** (CD II presencial, framework §6): **Proyectos 10%** es donde se puntúa directamente el entregable de portfolio de esta unidad; su rastro de proceso (decisiones, iteraciones, declaración de IA) puede alimentar también **Informes y escritos 15%**. Esta unidad no toca Pruebas (55%) ni Caso/problema (20%).

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

No es una preferencia de estilo. Una revisión sistemática de IA generativa en educación de moda basada en taller (28 fuentes académicas, 2018–2025) identifica **Learner Identity & Authorship** (identidad del aprendiz y autoría) como uno de cuatro pilares temáticos centrales que dan forma a cómo la IA generativa cambia la pedagogía de taller — junto a Construcción de Conocimiento, Práctica Docente, y Cultura y Ética de Taller — y nombra la tensión directamente: la IA generativa aporta "mayor ideación creativa y eficiencia" junto con "preocupaciones sobre originalidad, responsabilidad ética y acceso equitativo" (Anwar, Raza y Marzouk 2025, 1 — coat Ahmes `0598ec0e`, nodo `c9a17328-72f7-56c8-95bf-b9860b1067b8`).

Un estudio de laboratorio independiente sobre diseño de moda asistido por IA ("Artificial A(i)rchive") plantea la relación no como sustitución de autoría sino como **complemento**: la IA se trata como "suplemento a la creatividad humana natural", examinada a través de seis capacidades — Percibir, Pensar, Expresar, Colaborar, Construir, Probar — con el hallazgo de que la dinámica colaborativa recorre *todo* el proceso, no una fase aislada (Rizzi y Bertola 2025, 10 — coat Ahmes `167816a4`, nodo `908f5339-781d-51cc-a803-47dfbf9c0677`).

Leídos juntos: el campo coincide en que la IA generativa cambia la autoría de taller, y coincide en que la respuesta honesta es la visibilidad — mostrar la colaboración, no ocultarla ni fingir que no ocurrió.

### Vacío declarado — leer esto antes de asumir que el formato del portfolio en sí está validado

**Lo que está fundamentado arriba:** *por qué* la autoría y el proceso deben ser visibles cuando la IA generativa forma parte del taller. **Lo que NO está fundamentado:** qué patrones concretos de UX web de portfolio, maquetación o accesibilidad ayudan realmente a que un portfolio de moda consiga trabajo, se vea, o comunique bien. Esa pregunta queda fuera del corpus actual — es un `[UNVERIFIED-GAP]` declarado en el mapa de campo, no un problema resuelto que se enseñe como investigación asentada. La documentación de HTML/CSS/herramientas en esta unidad fundamenta **cómo** construir la página; no fundamenta **por qué esta maquetación enseña o consigue trabajo mejor que otra**. No leas la guía de maquetación de abajo como ciencia de UX respaldada por investigación — es asesoramiento de oficio profesional, etiquetado como tal.

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

### La pregunta de debate

Plantea esto al grupo antes de construir nada: **¿qué cuenta como "el trabajo" cuando un look se co-creó con un generador?** La tensión de autoría de Anwar et al. y el planteamiento de "suplemento, no sustituto" de Rizzi y Bertola son dos respuestas distintas — el taller debe alcanzar su propia postura, por escrito, antes de que venza el entregable de portfolio.

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

## B2 · Taller — talleres 3 h + proyectos 4 h (contextualizado, tipo entorno laboral)

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

**Evidencia a la que alimenta este entregable:** Evaluación → **Proyectos (10%)** directamente; el rastro de proceso y la declaración de IA también pueden apoyar **Informes y escritos (15%)** si el profesor pide una reflexión escrita junto a la pieza. Esta unidad no inventa un cuarto peso de evaluación — solo se reclaman estos dos.

Las referencias a herramientas en esta unidad (cualquier generador de sitios estáticos, editor de imagen o plataforma de alojamiento) son notas de plataforma fechadas, no citas de investigación — comprueba las versiones antes de clase.

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

---

## Trazabilidad y puerta de evidencia

- Anwar, S., Raza, A. y Marzouk, R. (2025). *Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.* European Journal of Business and Management, `10.65136/ejbm.v10i4.24`. Coat Ahmes `0598ec0e`, nodo `c9a17328-72f7-56c8-95bf-b9860b1067b8`, p.1. `(Anwar 2025, 1)`. Resuelto vía `ahmes query --cite`, `evaluator_safe=yes`.
  <!-- provenance: cita/nodo nombrado en la fila II.5 de la matriz digital-creativity-pedagogy/grounding/README.md y reconfirmado en vivo esta sesión vía `ahmes query --cite <db>:<node_id> --require-evaluator-safe --style chicago-author-date`; texto del nodo leído directamente de fission_node.markdown_content, no de una vista previa de vector/Athanor -->
- Rizzi, G. y Bertola, P. (2025). *Exploring the generative AI potential in the fashion design process.* European Journal of Cultural Management and Policy, `10.3389/ejcmp.2025.13875`. Coat Ahmes `167816a4`, nodo `908f5339-781d-51cc-a803-47dfbf9c0677`, p.9(→10). `(Rizzi 2025, 10)`. Resuelto vía `ahmes query --cite`, `evaluator_safe=yes`.
  <!-- provenance: cita/nodo nombrado en la fila II.5 de la matriz digital-creativity-pedagogy/grounding/README.md y reconfirmado en vivo esta sesión vía `ahmes query --cite <db>:<node_id> --require-evaluator-safe --style chicago-author-date`; texto del nodo leído directamente de fission_node.markdown_content -->
- **Evidencia ausente — declarada, no disimulada:** el mapa de campo mantiene un `[UNVERIFIED-GAP]` sobre **UX web de portfolio de moda** — ningún corpus establece qué patrones de maquetación, accesibilidad o presentación hacen que un portfolio comunique mejor, se vea, o consiga trabajo. Todo lo que aparece en la guía de maquetación/template de B1 es consejo de oficio profesional, no evidencia de investigación. No lo cites como si lo fuera.
