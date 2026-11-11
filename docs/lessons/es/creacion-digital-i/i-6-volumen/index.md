---
layout: lesson
title: 'I.6 · Volumen'
title_en: 'I.6 · Volume'
slug: i-6-volumen
date: 2026-11-10
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-i/i-6-volumen/
description: 'El volumen es comportamiento — ajuste, caída, respuesta del material y movimiento — diagnosticado entre vistas, no una malla que solo parece tridimensional.'
status: pilot
enable_page_art: false
tags: [digital-creativity-i, volume, material-study, spatial-representation, fashion-image, fit]
deck_url: /tracks/dci/i-6-volumen/
master_idea: 'El volumen es comportamiento: ajuste, caída, respuesta del material y movimiento'
master_idea_en: 'Volume is behaviour: fit, drape, material response, and movement'
practice_anchor: 'Un diagnóstico de ajuste/material en al menos dos vistas o estados, con lo que la simulación revela y lo que no puede'
frontier_signal: 'Las herramientas multi-vista y sensibles al movimiento son frontera; un caso híbrido no prueba un método de aula universal'
references: [galada-2025, coats-2026, cheang-suterwalla-2020, shinkle-2008, kandinsky-2012, panofsky-1993, pacioli-1889, bertol-2016]
cover_quote: 'Un pliegue se vuelve volumen cuando sus bordes se encuentran en el espacio.'
---

<!-- prettier-ignore-start -->

## Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

{% include lesson-semantic-graphic.html %}

## Empieza aquí

**Presentación en clase:** [I.6 · presentación de volumen]({{ '/tracks/dci/i-6-volumen/' | relative_url }}). **Ritmo de clase:** Análisis → clase magistral → dos ejercicios de Lab; esta sesión inicial no incluye taller de proyecto.

## Lugar oficial en la asignatura

**CONTENIDOS:** *Volumen.* Esta unidad continúa *Fundamentos y representación de la forma tridimensional* y se centra en el comportamiento y la interpretación del volumen.

**Competencias de la guía:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Resultados de aprendizaje pertinentes:** *Diferenciar los diferentes recursos técnicos para realizar modelos digitales tridimensionales* · *Reconocer las técnicas de representación tridimensional*.

**Pesos oficiales de evaluación:** Pruebas de evaluación 55% · Caso/problema 15% · Investigaciones y proyectos 20% · Cuaderno de prácticas de laboratorio/taller 10%.

## Objetivos de aprendizaje

- Tratar el volumen como comportamiento — ajuste, caída, respuesta del material, movimiento — no como un aspecto tridimensional pulido.
- Nombrar variables de volumen (caída, tensión, pliegue, vacío, escala, gravedad, cámara, iluminación) y mantener al menos una constante en una comparación justa.
- Diagnosticar una diferencia de ajuste o material en al menos dos vistas o estados; decir qué revela una simulación y qué no puede.
- Hacer una revisión controlada y conservar la evidencia del antes/después con una explicación breve.

## Análisis

Empieza con tela que ocupa espacio — no con un render de moda pulido. Aquí el volumen es lo que el material hace bajo apoyo y gravedad, leído desde más de una vista o estado.

<figure class="lesson-figure" id="figure-analysis-cloth-volume" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fuller-butterfly-1895.webp' | relative_url }}" width="1200" height="1600" alt="Fotografía histórica de una intérprete con vestuario de mariposa cuyas alas y abanico extienden el volumen mucho más allá de la silueta corporal." loading="lazy" decoding="async" />
<figcaption><strong>Volumen como extensión, no pulido de malla.</strong> El vestuario ocupa el espacio mediante estructura y caída — alas, abanico y silueta responden preguntas distintas sobre el mismo volumen llevado. Fotografía de vestuario mariposa, c. 1895. Dominio público · ledger de medios del curso (sin uso previo en lecciones).</figcaption>
</figure>

<figure class="lesson-figure" id="figure-drape-study" markdown="0">
<img src="{{ '/assets/images/deck-media/76f4b32ceaeb1364.webp' | relative_url }}" width="1200" height="1600" alt="Estudio monocromo de draping con pliegues profundos de tela pesada sobre rodillas flexionadas." loading="lazy" decoding="async" />
<figcaption><strong>Signos de ajuste en los pliegues.</strong> Crestas, valles y acumulación son evidencia legible de apoyo y gravedad — el mismo lenguaje diagnóstico que Galada trata como signos de ajuste, no como decoración. Estudio de draping · Wikimedia Commons · registros de medios del curso.</figcaption>
</figure>

**Pregunta de debate:** Si la silueta digital coincide con el contorno físico pero la tensión del cinturón no, ¿qué representación es “correcta” para aprender volumen — el contorno coincidente, la tensión discrepante, o el par conservado junto?

<figure class="lesson-figure lesson-figure--orb" id="figure-material-memory" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-material-memory-e9c611d87b2c.svg' | relative_url }}" width="1600" height="900" aria-label="Izquierda: volumen de tela apoyado con crestas y valles legibles. Derecha: la misma topología como malla digital cuyo contorno discontinuo marca una discrepancia a conservar y comprobar.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-material-memory-e9c611d87b2c.svg' | relative_url }}" width="1600" height="900" alt="Izquierda: volumen de tela apoyado con crestas y valles legibles. Derecha: la misma topología como malla digital cuyo contorno discontinuo marca una discrepancia a conservar y comprobar." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Pliegue físico · malla digital.</strong> Misma topología, dos evidencias: cresta/valle/apoyo a la izquierda; malla más plana a la derecha. El contorno discontinuo es la discrepancia a conservar — no la disimules. Ilustración original de la asignatura · visual-forger · derechos reservados.</figcaption>
</figure>

**Observa:** el contorno del pliegue, los puntos que sostienen el material, la escala del estudio y lo que oculta la vista elegida. Un render uniforme puede describir una forma propuesta; por sí solo, no verifica cómo cae un material concreto.

## Clase magistral

### 1 · El volumen es comportamiento, no pulido de malla

La formación en diseño de moda suele enseñar patronaje plano y draping, pero deja poco espacio a la corrección de ajuste: se espera que el alumnado “intuya” signos de desajuste en tres dimensiones y actúe sobre el patrón bidimensional [(Galada 2025, 1)](#ref-galada-2025). Corregir el ajuste une localizar problemas, manipular patrones y decidir modificaciones mediante visualización espacial [(Galada 2025, 2)](#ref-galada-2025). Arrugas de arrastre, pliegues, huecos y arrugas son signos legibles de desajuste, no decoración que borrar sin diagnóstico [(Galada 2025, 3)](#ref-galada-2025).

**Clavo de la asignatura (evaluable):** un diagnóstico de ajuste/material en al menos dos vistas o estados, con una explicación verbal de lo que la simulación o el segundo medio revela — y de lo que no puede revelar.

<figure class="lesson-figure" id="figure-costume-volume" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fuller-scarf.webp' | relative_url }}" width="1200" height="1600" alt="Intérprete con grandes volúmenes de tela clara girando alrededor del cuerpo en una fotografía de estudio." loading="lazy" decoding="async" />
<figcaption><strong>Volumen blando bajo el gesto.</strong> El volumen de la tela cambia con el movimiento y los puntos de suspensión — un fotograma es un estado, no todo el comportamiento. Fotografía de extensión de tela · dominio público · ledger del curso (sin uso previo en lecciones).</figcaption>
</figure>

Las imágenes de moda pueden mostrar prendas liberadas de consideraciones prácticas como el confort, y un cuerpo depurado de referencias corpóreas — un ‘ideal sintético’ en el que cuerpo y prenda se disuelven en pura representación [(Shinkle 2008, 23)](#ref-shinkle-2008). Esa libertad compositiva no sustituye comprobar cómo se comporta un pliegue bajo apoyo y gravedad.

### Perspectiva crítica · ¿De quién es el volumen por defecto?

Las herramientas de prenda digital suelen tratar el avatar o maniquí como un soporte de medida neutro. La evidencia de un taller híbrido advierte que los avatares digitales no capturan por completo la complejidad de la diversidad corporal humana, y que siguen las discrepancias de ajuste simulado–físico [(Coats 2026, 4)](#ref-coats-2026). Descolonizar la enseñanza de moda no es «añadir un ejemplo diverso a un canon intacto»: exige examinar cómo colonialidad, posición docente y autoridad estructuran qué cuenta como conocimiento del cuerpo y de la prenda [(Cheang and Suterwalla 2020, 1)](#ref-cheang-suterwalla-2020).

**Pregunta antes de confiar en un pase de volumen:** ¿qué medidas, proporciones y postura están construidas en la forma por defecto — y cuáles se tratan como casos especiales?

<figure class="lesson-figure" id="figure-aso-oke-weaving" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-3ba7956f8c799668.jpg' | relative_url }}" width="1600" height="1200" alt="Manos en un telar de Aso-oke, con tensión de urdimbre y volumen estructurado de la tela en producción." loading="lazy" decoding="async" />
<figcaption><strong>El volumen empieza en el tejido.</strong> Tensión, apoyo y estructura ya son variables de volumen antes de cualquier pase digital de ajuste. Tejido Aso-oke · Ayodele Adeniji · <a href="https://commons.wikimedia.org/wiki/File:Aso-oke_weaving.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC BY-SA 4.0.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-adowa-kente-volume" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-ce0a70aac3fbd44e.jpg' | relative_url }}" width="1066" height="1600" alt="Bailarina Adowa con kente en capas; pliegues, vacíos y escala legibles frente al cuerpo." loading="lazy" decoding="async" />
<figcaption><strong>Volumen llevado fuera de una silueta euro-default.</strong> Lee pliegue, vacío y escala en un cuerpo que la asignatura se niega a tratar como «caso especial». Bailarina Adowa con kente · Kwameghana · <a href="https://commons.wikimedia.org/wiki/File:Adowa_Dancer_in_Kente_Cloth.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC BY-SA 4.0.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-andean-weaving-volume" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-d3c5f1f783327685.jpg' | relative_url }}" width="1600" height="1066" alt="Demostración de tejido andino con estructura textil y postura corporal visibles a la vez." loading="lazy" decoding="async" />
<figcaption><strong>Estructura sostenida por cuerpo y telar.</strong> El comportamiento del material es técnica cultural, no un preset físico universal del software. Tejido andino, Museum of Anthropology UBC · Adam Jones · <a href="https://commons.wikimedia.org/wiki/File:Andean_Weaving_Museum_of_Anthropology_UBC_Vancouver.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC BY-SA 2.0.</figcaption>
</figure>

### 2 · Variables de volumen (mantén una constante)

Trátalas como variables inspeccionables, no como menús de software: **caída · tensión · pliegue · vacío · escala · gravedad · cámara · iluminación**. Una comparación justa nombra qué variable cambias y cuál congelas. La fluidez con la herramienta sin ese nombramiento no es comprensión del volumen.

**Gramática de la forma (unidades adyacentes, no un sustituto del diagnóstico de ajuste).** Punto → línea → plano en la gramática bauhausiana de Kandinsky sigue nombrando cómo se construye una composición antes de que la tela cuelgue en el espacio — vocabulario útil al pasar del dibujo de I.2 al volumen multi-vista de I.5/I.6 [(Kandinsky 2012, “Introduction”)](#ref-kandinsky-2012). El equilibrio planar neoplasticista (Mondrian) y el contraste munariano cuadrado-construcción / círculo-dinámico pertenecen a la misma conversación de estudio sobre la forma; **no** sustituyen los signos de desajuste de Galada ni la discrepancia híbrida de Coats.

**Perspectiva como construcción, no como prueba de ajuste.** La perspectiva «central» trata el cuadro como un corte plano del pirámide visual y supone un solo ojo inmóvil — abstracciones audaces respecto de la percepción vivida [(Panofsky 1991, 14)](#ref-panofsky-1993). En ese sentido la perspectiva transforma el espacio psicofisiológico en espacio matemático [(Panofsky 1991, 15)](#ref-panofsky-1993). Las construcciones antiguas podían ser espaciales sin el punto de fuga compartido moderno — una visión agregada, «no moderna», del espacio [(Panofsky 1991, 21)](#ref-panofsky-1993). Frontal / lateral / tres cuartos en esta unidad son *preguntas distintas sobre el mismo volumen*, no una receta que resuelva la tensión del cinturón. Kit de imagen del curso (categorías → diagramas / animación futura): recibo pedagógico *Perspective · volume image kit*.

<figure class="lesson-figure" id="figure-perspective-psycho-vs-math" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p1-psycho-vs-math-5e69c5149013.svg' | relative_url }}" width="1600" height="900" alt="Diagrama en dos paneles: a la izquierda, arcos perceptivos curvos con tamaños irregulares; a la derecha, ojo, plano del cuadro y ortogonales que convergen en un punto de fuga." loading="lazy" decoding="async" />
<figcaption><strong>P1 · Espacio psicofisiológico ≠ matemático.</strong> Izquierda: la percepción sigue siendo finita y desigual. Derecha: la perspectiva central abstrae un solo ojo y un corte plano — útil para la disciplina multi-vista, nunca un sustituto del diagnóstico de ajuste. Ilustración original · perspective-kit · según Panofsky · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-perspective-antique-aggregate" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p2-antique-aggregate-3b41a386a525.svg' | relative_url }}" width="1600" height="900" alt="Varios objetos escorzados con ejes de fuga separados y sin un punto de fuga compartido." loading="lazy" decoding="async" />
<figcaption><strong>P2 · Espacio antiguo / agregado.</strong> Los cuerpos disminuyen sin un solo punto de fuga compartido — un pez de ejes, no una receta de VP. Ilustración original · perspective-kit · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-perspective-gothic-mass" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p3-gothic-mass-interior-70d8ce73e856.svg' | relative_url }}" width="1600" height="900" alt="Planos de masa sólida que se abren hacia un volumen interior hueco." loading="lazy" decoding="async" />
<figcaption><strong>P3 · Masa → interior reabierto.</strong> Los planos se consolidan y luego abren un hueco que el ojo puede entrar. Ilustración original · perspective-kit · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-perspective-space-box" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p4-space-box-b30a812e1dd7.svg' | relative_url }}" width="1600" height="900" alt="Caja espacial cerrada tipo habitación con muros etiquetados que sugieren un cuerpo hueco en profundidad." loading="lazy" decoding="async" />
<figcaption><strong>P4 · Caja espacial (Raumkasten).</strong> Un interior cerrado como cuerpo hueco — fragmento de un mundo, no una retícula infinita. Ilustración original · perspective-kit · superposición Rive en la presentación · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-perspective-central-vp" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p5-central-vp-708c927932cd.svg' | relative_url }}" width="1600" height="900" alt="Ortogonales que convergen en un punto de fuga central sobre el plano del cuadro." loading="lazy" decoding="async" />
<figcaption><strong>P5 · Perspectiva central / sistemática.</strong> El punto de fuga compartido como forma simbólica — sigue sin ser prueba de ajuste. Ilustración original · perspective-kit · superposición Rive en la presentación · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-perspective-fashion-multiview" markdown="0">
<img src="{{ '/assets/images/lesson-figures/perspective-kit/pv-p6-fashion-multiview-71af54a9678b.svg' | relative_url }}" width="1600" height="900" alt="Tres cámaras bloqueadas — frontal, lateral y tres cuartos — con ejes XYZ compartidos enmarcando un mismo volumen de tela." loading="lazy" decoding="async" />
<figcaption><strong>P6 · Multi-vista de moda (clavo del curso).</strong> Frontal / lateral / ¾ responden preguntas distintas; Galada/Coats siguen dueños del ajuste. Ilustración original · perspective-kit · diapositivas de movimiento del deck · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-kente-surface-variables" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-18b94f2235bbb292.jpg' | relative_url }}" width="1600" height="1271" alt="Varias piezas de kente extendidas que muestran escala de rayas, bloques de color y bordes plegados como pistas de volumen." loading="lazy" decoding="async" />
<figcaption><strong>Superficie que aún lleva pistas de volumen.</strong> Escala de rayas, bordes plegados y altura del apilado se leen antes de simular nada. Kente, Tafi, región Volta · Warmglow · <a href="https://commons.wikimedia.org/wiki/File:Different_Kente_cloth,_Tafi,_Volta_region.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC0.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-ychsma-textile-plane" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-a26b3c9030c11a90.jpg' | relative_url }}" width="1600" height="789" alt="Textil Ychsma del siglo XV (Perú) en plano, con el tejido estampado legible como estructura antes de ser llevado." loading="lazy" decoding="async" />
<figcaption><strong>Plano antes de llevarse.</strong> Un textil histórico plano sigue preguntando qué pliegues y vacíos aparecerían al vestirse — nombra la variable antes de inventar una silueta. Textil Ychsma s. XV, Perú · <a href="https://commons.wikimedia.org/wiki/File:15th_century_Ychsma_textile,_Peru.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC0.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-support-and-drape" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-support-and-drape-20261020-r1.svg' | relative_url }}" width="1600" height="900" alt="Un tramo de material entre dos apoyos muestra un contorno estable y una caída mayor bajo carga." loading="lazy" decoding="async" />
<figcaption><strong>La gravedad curva el material.</strong> El mismo tramo de material se representa entre dos apoyos. Los dos contornos hacen visibles la gravedad y el punto de suspensión. Ilustración original de la asignatura · visual-forger 1.3.0 · derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-volume-in-time" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/muybridge-waltz.webp' | relative_url }}" width="1600" height="900" alt="Secuencia de fotogramas de vals que muestra cómo el volumen del vestido se redistribuye en pasos y giros." loading="lazy" decoding="async" />
<figcaption><strong>Volumen a través de estados.</strong> Un solo render congela un arreglo de tela; una secuencia hace visible la redistribución bajo el movimiento — el clavo de la asignatura pide diagnóstico entre vistas o estados. Secuencia de vals de Eadweard Muybridge · dominio público · ledger del curso (sin uso previo en lecciones).</figcaption>
</figure>

Las vistas frontal, lateral y de tres cuartos responden preguntas distintas sobre un mismo volumen — más cerca de elegir una construcción (silueta frente a profundidad frente a pliegue) que de «aplicar perspectiva». Mantenlas alineadas e indica qué aporta cada una: silueta, profundidad, dirección del pliegue o contacto con un apoyo.

<figure class="lesson-figure" id="figure-cloth-on-bodies" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/duncan-dancers-genthe.webp' | relative_url }}" width="1600" height="1200" alt="Varias bailarinas con túnicas sueltas; los volúmenes de tela cuelgan y se balancean de modo distinto en cada cuerpo." loading="lazy" decoding="async" />
<figcaption><strong>Mismo tipo de prenda, cuerpos distintos.</strong> La tela suelta no produce un volumen universal — proporción, gesto y apoyo cambian la caída. Arnold Genthe, bailarinas de Isadora Duncan · dominio público · ledger del curso (sin uso previo en lecciones).</figcaption>
</figure>

### 3 · Aprender por discrepancia y revisar una vez

Un caso docente híbrido con denim informa de que silueta y proporciones pueden alinearse de cerca en simulación mientras el ajuste físico del cinturón sigue revelando discrepancias de tensión — una pista que el alumnado usó para evaluar los límites de las asunciones digitales [(Coats 2026, 5)](#ref-coats-2026). Los flujos híbridos pueden unir fluidez digital e intuición física, pero no son universalmente superiores; su eficacia depende del tipo de prenda, del perfil del aprendiz, de los objetivos y de las demandas sensoriales de la tarea [(Coats 2026, 5)](#ref-coats-2026). En ese módulo, el alumnado también expresó escepticismo sobre afirmaciones de sostenibilidad más amplias del prototipado virtual [(Coats 2026, 4)](#ref-coats-2026) — útil para el debate, no como prueba de que una herramienta arregla la sobreproducción.

Elige una diferencia — un pliegue sin apoyo, una línea de tensión poco verosímil o una silueta alterada. Ajusta una sola variable, conserva el primer pase y anota por qué el cambio mejora la representación.

<figure class="lesson-figure lesson-figure--orb" id="figure-evidence-pair" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-evidence-pair-20c174fd85e2.svg' | relative_url }}" width="1600" height="900" aria-label="Tres etapas del mismo volumen de tela: origen material, simulación más plana y una corrección local marcada en una línea de tiempo compartida.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-evidence-pair-20c174fd85e2.svg' | relative_url }}" width="1600" height="900" alt="Tres etapas del mismo volumen de tela: origen material, simulación más plana y una corrección local marcada en una línea de tiempo compartida." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Origen → simulación → una corrección.</strong> Conserva las tres etapas juntas para inspeccionar el cambio. El pin marca la única variable revisada — no un remallado completo. Ilustración original de la asignatura · visual-forger · derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--orb" id="figure-simulation-break" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-simulation-break-c1d1efc6790d.svg' | relative_url }}" width="1600" height="900" aria-label="Izquierda: la tela cae y termina en dos apoyos. Derecha: un contorno virtual continúa más allá del apoyo; una marca señala la discrepancia a comprobar.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-simulation-break-c1d1efc6790d.svg' | relative_url }}" width="1600" height="900" alt="Izquierda: la tela cae y termina en dos apoyos. Derecha: un contorno virtual continúa más allá del apoyo; una marca señala la discrepancia a comprobar." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Congela el apoyo · prueba el contorno.</strong> El material termina en los postes; la línea virtual sigue. Nombra esa ruptura antes de revisar — congela apoyo/gravedad, cambia una sola variable de contorno. Ilustración original de la asignatura · visual-forger · derechos reservados.</figcaption>
</figure>

### 4 · Costes reubicados (pregunta viva)

El prototipado digital puede reducir muestras físicas mientras desplaza energía, trabajo, expertise y presiones de sobreproducción a otro lugar. El escepticismo de sostenibilidad de Coats sostiene esa discusión; no cierra la contabilidad [(Coats 2026, 4)](#ref-coats-2026).

**Pregunta viva abierta:** ¿Qué se ha reducido exactamente cuando una muestra física se vuelve digital, y qué se ha limitado a moverse a otro sitio? Trae una consecuencia material, laboral, energética o de producción.

## Lab · Portfolio

Estos dos ejercicios dejan rastros de proceso comparables. Se admite una alternativa táctil o de baja tecnología; no hace falta una aplicación 3D concreta. Usa marcas grandes y de alto contraste, y acompaña las imágenes de una descripción oral o escrita breve cuando resulte útil.

### Ejercicio 1 · Construir un pliegue {#lab-exercise-1}

**Tiempo:** 15 minutos · **Formato:** individual.

Construye un volumen pequeño con papel, tela u otro material disponible; fotografía dos vistas y marca dónde cambia el pliegue. Nombra dos variables de volumen visibles en el estudio.

**Rastro para el portfolio:** Dos vistas y una nota sobre el cambio de contorno, apoyo o caída — más las dos variables nombradas.

### Ejercicio 2 · Diagnosticar, contrastar, revisar {#lab-exercise-2}

**Tiempo:** 15 minutos · **Formato:** individual.

Compara el estudio físico con una interpretación digital sencilla (o un segundo medio). Diagnostica una diferencia de ajuste/material en el lenguaje de signos legibles (tensión, arrastre, pliegue sin apoyo, error de escala). Cambia una variable; conserva la vista anterior; di qué reveló el segundo medio y qué aún no puede probar.

**Rastro para el portfolio:** Par antes/después y una frase que explique el cambio — nombra la diferencia (la silueta puede coincidir aunque la tensión no).

## Comprobación de resolución de problemas

1. Dado un flujo híbrido descrito, identifica qué paso fue probablemente analógico frente a digital y por qué.
2. Nombra qué no puede mostrar un render digital plano sobre el volumen que sí puede una vista física o 3D rotatoria.
3. Sin ninguna herramienta, describe cómo cambia el draping al aumentar el volumen — al menos una consecuencia estructural.
4. Di una forma en que un volumen de imagen de moda (ideal sintético) ocultaría la diferencia que acabas de nombrar.

## Conclusión

El volumen se discute mejor cuando el estudio material, la representación digital y una revisión razonada permanecen visibles juntos. Lleva la diferencia pendiente al siguiente ejercicio de forma espacial — y a la pregunta de I.7 sobre cómo las imágenes se vuelven referencias sin borrar lo que ocultan.

**Práctica:** cinco preguntas de repaso con respuestas al pulsar — [I.6 Volumen cuestionario de práctica]({{ '/practice/es/i-6-volumen/' | relative_url }}). No es evaluable; no se registra ninguna respuesta.

## Tao de la Imagen {#tao-of-the-image}

Aforismo de taller; no es una cita académica.

> _“Un pliegue se vuelve volumen cuando sus bordes se encuentran en el espacio.”_

---

## Referencias

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.6; parity=EN canonical; MASTER-IDEAS=I.6; session_prompt=i-6-volume.md; digest=dc-3d-form-volume-pedagogy
PROVENANCE_LINE: claim=I.6.claim.fit-correction-undertaught; status=VERIFIED; public_citation="(Galada 2025, 1)"
PROVENANCE_LINE: claim=I.6.claim.hybrid-discrepancy; status=VERIFIED; public_citation="(Coats 2026, 5)"
PROVENANCE_LINE: claim=I.6.claim.synthetic-ideal-volume; status=VERIFIED; public_citation="(Shinkle 2008, 23)"
MEDIA_RIGHTS_LINE: slots=fuller-butterfly-1895,fuller-scarf,duncan-dancers-genthe,muybridge-waltz,76f4b32ceaeb1364,course-authored-svg,wm-aso-oke,wm-adowa-kente,wm-andean,wm-kente-tafi,wm-ychsma,pv-p1-psycho-vs-math-5e69c5149013; status=OK; note=parity EN; Commons UA download 2026-11-11 + perspective-kit P1
SEMANTIC_GRAPHIC: release=dc-i-06-volume-behaviour-semantic-20261110-r2
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de Innovación docente
{: .lesson-editorial-note }

Galada y Baytar (2025) fundamentan la corrección de ajuste como objeto educativo y los signos de desajuste como lenguaje diagnóstico. Coats (2026) fundamenta un módulo híbrido en el que la discrepancia enseña, los límites de diversidad del avatar y el escepticismo de sostenibilidad. Cheang y Suterwalla (2020) fundamentan una postura docente decolonial — no una lista de maniquíes «diversos». Panofsky (1991) fundamenta el multi-vista como construcciones históricamente plurales (espacio psicofisiológico frente a matemático; agregado antiguo frente a punto de fuga central) — no una receta de perspectiva para el ajuste. Ninguna fuente prueba que el mismo método funcione en todas las cohortes, herramientas o instituciones. La teoría de la imagen de moda (ideal sintético) aclara lo que una imagen pulida puede ocultar — no sustituye el estudio material. Alberti sigue siendo una laguna declarada.

---

## Autoría asistida por IA

Esta lección se redactó con asistencia de IA bajo control editorial del autor.

Declaración de uso de IA: [leer la declaración completa]({{ '/ai-declaration/' | relative_url }}).

{% if site.publication.publish_internal_metadata %}
<!-- lesson_uuid: 13eb3a18-ea89-4303-95f1-28f6f6b2d814
     vault_refs_consulted: 7
     forge_date: 2026-11-10 · harness: lesson-scribe + Profield MASTER-IDEAS + session-prompt + digest
-->
{% endif %}
