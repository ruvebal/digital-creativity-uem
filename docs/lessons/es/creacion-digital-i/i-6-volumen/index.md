---
layout: lesson
title: 'I.6 · Volumen'
title_en: 'I.6 · Volume'
slug: i-6-volumen
date: 2026-11-14
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
references: [galada-2025, coats-2026, cheang-suterwalla-2020, shinkle-2008]
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

**Nota de serie:** La construcción perspectiva, las categorías de Panofsky y la historia de la percepción de profundidad viven en la pista opcional *Volume Perception & Depth* — no en este clavo de *Volumen*. Ver plan `VOLUME-DEPTH-SERIES-PLAN.md`.

## Lugar oficial en la asignatura

**CONTENIDOS:** *Volumen.* Esta unidad continúa *Fundamentos y representación de la forma tridimensional* y se centra en el comportamiento y la interpretación del volumen.

**Competencias de la guía:** `CON1`, `HAB9`, `COMP8`, `COMP9`.

**Resultados de aprendizaje pertinentes:** *Diferenciar los diferentes recursos técnicos para realizar modelos digitales tridimensionales* · *Reconocer las técnicas de representación tridimensional*.

**Pesos oficiales de evaluación:** Pruebas de evaluación 55% · Caso/problema 15% · Investigaciones y proyectos 20% · Cuaderno de prácticas de laboratorio/taller 10%.

## Objetivos de aprendizaje

- Tratar el volumen como comportamiento — ajuste, caída, respuesta del material, movimiento — no como un aspecto tridimensional pulido.
- Nombrar variables de volumen (caída, tensión, pliegue, vacío, escala, gravedad, cámara, iluminación) y congelar al menos una en una comparación justa.
- Diagnosticar un desajuste de ajuste o material en al menos dos vistas o estados; decir qué revela una simulación y qué no puede.
- Hacer una revisión controlada y conservar evidencia antes/después con una explicación breve.

## Análisis

Empieza con tela que ocupa espacio — no un render de prenda pulido. El volumen aquí es lo que el material hace bajo apoyo y gravedad, leído desde más de una vista o estado.

<figure class="lesson-figure" id="figure-analysis-cloth-volume" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fuller-butterfly-1895.webp' | relative_url }}" width="1200" height="1600" alt="Fotografía histórica de una intérprete con un traje de mariposa cuyas alas y estructura en abanico se extienden más allá de la silueta del cuerpo." loading="lazy" decoding="async" />
<figcaption><strong>Volumen como extensión, no como brillo de malla.</strong> El traje ocupa espacio por estructura y caída — alas, abanico y silueta responden preguntas distintas sobre el mismo volumen vestido. Fotografía de traje mariposa, c. 1895. Dominio público · ledger de medios del curso.</figcaption>
</figure>

<figure class="lesson-figure" id="figure-drape-study" markdown="0">
<img src="{{ '/assets/images/deck-media/76f4b32ceaeb1364.webp' | relative_url }}" width="1200" height="1600" alt="Estudio monocromo de drapería con pliegues profundos de tela pesada sobre rodillas flexionadas, con luz fuerte que define crestas y valles en sombra." loading="lazy" decoding="async" />
<figcaption><strong>Signos de ajuste en los pliegues.</strong> Crestas, valles y acumulación son evidencia legible de apoyo y gravedad — el mismo lenguaje diagnóstico que Galada trata como signos de desajuste, no como decoración. Estudio de indumentaria de Leonardo · Wikimedia Commons · registros del curso.</figcaption>
</figure>

**Debate:** Si la silueta digital coincide con el contorno físico pero la tensión del cinturón no, ¿qué representación es «correcta» para aprender volumen — el contorno coincidente, la tensión desajustada, o el par mantenido junto?

<figure class="lesson-figure lesson-figure--orb" id="figure-material-memory" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-material-memory-e9c611d87b2c.svg' | relative_url }}" width="1600" height="900" aria-label="Izquierda: un volumen de tela apoyado con crestas y valles legibles. Derecha: la misma topología como malla digital cuyo contorno discontinuo marca un desajuste a conservar y probar.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-material-memory-e9c611d87b2c.svg' | relative_url }}" width="1600" height="900" alt="Izquierda: un volumen de tela apoyado con crestas y valles legibles. Derecha: la misma topología como malla digital cuyo contorno discontinuo marca un desajuste a conservar y probar." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Pliegue físico · malla digital.</strong> Misma topología de tela, dos evidencias. El contorno discontinuo es el desajuste a conservar — no lo suavices. Ilustración original · visual-forger · todos los derechos reservados.</figcaption>
</figure>

**Busca:** el contorno del pliegue, los puntos que sostienen el material, la escala del estudio y lo que oculta la vista elegida. Un render suave puede describir una forma propuesta; por sí solo no verifica cómo cuelga un material concreto.

## Clase magistral

### 1 · El volumen es comportamiento, no brillo de malla

La educación en diseño de moda a menudo enseña patronaje plano y draping, pero deja la corrección de ajuste poco enseñada — se espera que el estudiante «intuya» signos de desajuste en tres dimensiones y actúe sobre el patrón bidimensional [(Galada 2025, 1)](#ref-galada-2025). La corrección de ajuste une localizar problemas, manipular patrones y decidir modificaciones mediante visualización espacial [(Galada 2025, 2)](#ref-galada-2025). Líneas de arrastre, pliegues, huecos y arrugas son signos legibles de desajuste, no decoración que borrar sin diagnóstico [(Galada 2025, 3)](#ref-galada-2025).

**Clavo del curso (evaluable):** un diagnóstico de ajuste/material en al menos dos vistas o estados, con explicación verbal de lo que la simulación o el segundo medio revela — y lo que no puede revelar.

<figure class="lesson-figure" id="figure-costume-volume" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fuller-scarf.webp' | relative_url }}" width="1200" height="1600" alt="Intérprete con grandes volúmenes de tela clara girando alrededor del cuerpo en una fotografía de estudio." loading="lazy" decoding="async" />
<figcaption><strong>Volumen blando bajo el gesto.</strong> El volumen de tela cambia con el movimiento y los puntos de suspensión — un fotograma es un estado, no todo el comportamiento. Fotografía de bufanda / extensión de tela, dominio público · ledger del curso.</figcaption>
</figure>

Las imágenes de moda pueden mostrar prendas liberadas de consideraciones prácticas como el confort, y un cuerpo purgado de referencias corpóreas — un «ideal sintético» en el que cuerpo y prenda se disuelven en pura representación [(Shinkle 2008, 23)](#ref-shinkle-2008). Esa libertad compositiva no sustituye probar cómo se comporta un pliegue bajo apoyo y gravedad.

### 2 · ¿De quién es el volumen por defecto?

Las herramientas digitales de prenda suelen tratar el avatar o el maniquí como un soporte de medida neutro. La evidencia de estudio híbrido advierte que los avatares digitales no capturan por completo la diversidad corporal humana, y que siguen las discrepancias de ajuste simulado–físico [(Coats 2026, 4)](#ref-coats-2026). Descolonizar la enseñanza de moda no es «añadir un ejemplo diverso a un canon intacto»: exige examinar cómo la colonialidad, la posición docente y la autoridad estructuran qué cuenta como saber del cuerpo y de la prenda [(Cheang and Suterwalla 2020, 1)](#ref-cheang-suterwalla-2020).

**Pregunta antes de confiar en un pase de volumen:** ¿de quién son las medidas, proporciones y posturas inscritas en la forma por defecto — y de quién se trata como caso especial?

<figure class="lesson-figure" id="figure-adowa-kente-volume" markdown="0">
<img src="{{ '/assets/images/lesson-figures/i6-i7/wm-ce0a70aac3fbd44e.jpg' | relative_url }}" width="1066" height="1600" alt="Bailarina Adowa con tela kente en capas, con pliegues, vacíos y escala claros respecto al cuerpo." loading="lazy" decoding="async" />
<figcaption><strong>Volumen vestido fuera de una silueta europor defecto.</strong> Lee pliegue, vacío y escala en un cuerpo que el curso se niega a tratar como «caso especial». Bailarina Adowa en kente · Kwameghana · <a href="https://commons.wikimedia.org/wiki/File:Adowa_Dancer_in_Kente_Cloth.jpg" target="_blank" rel="noopener">Wikimedia Commons</a> · CC BY-SA 4.0.</figcaption>
</figure>

### 3 · Variables de volumen (congela una)

Trátalas como variables inspeccionables, no como menús de software: **caída · tensión · pliegue · vacío · escala · gravedad · cámara · iluminación**. Una comparación justa nombra qué variable cambias y cuál congelas. La fluidez de herramienta sin ese nombramiento no es comprensión del volumen.

Frontal, lateral y tres cuartos responden preguntas distintas sobre el mismo volumen — contorno, profundidad, dirección del pliegue o contacto con un apoyo. Manténlas alineadas y di qué aporta cada una. (La historia sistemática de la perspectiva pertenece a la presentación de enriquecimiento de construcción, no como prueba de ajuste aquí.)

<figure class="lesson-figure lesson-figure--orb" id="figure-support-and-drape" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-support-and-drape-20261020-r1.svg' | relative_url }}" width="1600" height="900" aria-label="Un tramo de material entre dos apoyos muestra un contorno estable y una caída más profunda bajo carga.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-support-and-drape-20261020-r1.svg' | relative_url }}" width="1600" height="900" alt="Un tramo de material entre dos apoyos muestra un contorno estable y una caída más profunda bajo carga." loading="lazy" decoding="async" />
</object>
<figcaption><strong>La gravedad curva el material.</strong> El mismo tramo se dibuja entre dos apoyos. Los dos contornos hacen visibles el papel de la gravedad y el punto de suspensión. Ilustración original · visual-forger · todos los derechos reservados.</figcaption>
</figure>

### 4 · Aprende por discrepancia; revisa una vez

Un caso docente híbrido de denim informa que silueta y proporciones pueden alinearse de cerca en simulación mientras el ajuste físico del cinturón revela discrepancias de tensión — una pista que los estudiantes usaron para evaluar los límites de las asunciones digitales [(Coats 2026, 5)](#ref-coats-2026). Los flujos híbridos pueden unir fluidez digital e intuición física, pero no son universalmente superiores; la eficacia depende del tipo de prenda, el perfil del aprendiz, los objetivos y las demandas sensoriales de la tarea [(Coats 2026, 5)](#ref-coats-2026).

Elige un desajuste — un pliegue sin apoyo, una línea de tensión inverosímil o una silueta cambiada. Ajusta una variable, conserva el primer pase y registra por qué el cambio mejora la representación.

<figure class="lesson-figure lesson-figure--orb" id="figure-evidence-pair" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-evidence-pair-20c174fd85e2.svg' | relative_url }}" width="1600" height="900" aria-label="Tres etapas de un volumen de tela: fuente material, simulación más plana y una corrección local marcada en una línea de tiempo compartida.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-evidence-pair-20c174fd85e2.svg' | relative_url }}" width="1600" height="900" alt="Tres etapas de un volumen de tela: fuente material, simulación más plana y una corrección local marcada en una línea de tiempo compartida." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Fuente → simulación → una corrección.</strong> Mantén las tres etapas juntas. El pin coral marca la única variable revisada — no un remesh completo. Ilustración original · visual-forger · todos los derechos reservados.</figcaption>
</figure>

<figure class="lesson-figure lesson-figure--orb" id="figure-simulation-break" markdown="0">
<object type="image/svg+xml" data="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-simulation-break-c1d1efc6790d.svg' | relative_url }}" width="1600" height="900" aria-label="Izquierda: la tela cuelga y termina en dos apoyos. Derecha: un contorno virtual continúa más allá del apoyo; una ruptura marcada muestra la discrepancia a probar.">
<img src="{{ '/assets/images/lesson-figures/visual-forger/dc-i6-simulation-break-c1d1efc6790d.svg' | relative_url }}" width="1600" height="900" alt="Izquierda: la tela cuelga y termina en dos apoyos. Derecha: un contorno virtual continúa más allá del apoyo; una ruptura marcada muestra la discrepancia a probar." loading="lazy" decoding="async" />
</object>
<figcaption><strong>Congela el apoyo · prueba el contorno.</strong> El material termina en los postes; la línea virtual sigue. Nombra esa ruptura antes de revisar. Ilustración original · visual-forger · todos los derechos reservados.</figcaption>
</figure>

### 5 · Costes reubicados (prompt vivo)

El prototipado digital puede reducir muestras físicas mientras desplaza energía, trabajo, expertise y presiones de sobreproducción. El escepticismo de sostenibilidad de Coats sostiene esa discusión; no cierra la contabilidad [(Coats 2026, 4)](#ref-coats-2026).

**Prompt vivo:** ¿Qué se ha reducido exactamente cuando una muestra física se vuelve digital, y qué solo se ha movido de sitio? Trae una consecuencia material, laboral, energética o de producción.

## Lab · Portafolio

Estos dos ejercicios dejan rastros de proceso comparables. Se acepta un equivalente low-tech o táctil; no se exige una aplicación 3D concreta.

### Ejercicio 1 · Construye un pliegue {#lab-exercise-1}

**Tiempo:** 15 minutos · **Formato:** individual.

Construye un volumen pequeño con papel, tela u otro material; fotografía dos vistas y marca dónde cambia el pliegue. Nombra dos variables de volumen visibles en el estudio.

**Rastro de portafolio:** Dos vistas y una nota sobre el contorno, el apoyo o la caída — más las dos variables nombradas.

### Ejercicio 2 · Diagnostica, compara, revisa {#lab-exercise-2}

**Tiempo:** 15 minutos · **Formato:** individual.

Compara el estudio físico con una interpretación digital simple (u otro medio). Diagnostica un desajuste de ajuste/material en el lenguaje de signos legibles. Cambia una variable; conserva la vista anterior; di qué reveló el segundo medio y qué aún no puede probar.

**Rastro de portafolio:** Par antes/después y una frase que explique el cambio — nombra el desajuste (la silueta puede coincidir mientras la tensión no).

## Comprobación de problemas

1. Dado un flujo híbrido descrito, identifica qué paso fue probablemente analógico frente a digital y por qué.
2. Nombra lo que un render digital plano no puede mostrar del volumen que una vista física o 3D rotatoria sí.
3. Sin ninguna herramienta, describe cómo cambia el draping al aumentar el volumen — al menos una consecuencia estructural.
4. Indica una forma en que un volumen de imagen de moda (ideal sintético) ocultaría el desajuste que acabas de nombrar.

## Conclusión

El volumen es más fácil de discutir cuando el estudio material, la representación digital y una revisión razonada permanecen visibles juntos. Lleva el desajuste no resuelto a la pregunta de I.7 sobre cómo las imágenes se vuelven referencias sin borrar lo que ocultan.

**Práctica:** cinco preguntas de recuerdo con respuesta al clic — [cuestionario I.6 Volumen]({{ '/practice/es/i-6-volumen/' | relative_url }}). Sin nota; no se registra nada.

## Tao of the Image {#tao-of-the-image}

Aforismo de estudio; no es una cita académica.

> _“Un pliegue se vuelve volumen cuando sus bordes se encuentran en el espacio.”_

---

## Referencias

{% include references.html %}

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=I.6; cascade=VOLUME-DEPTH-SERIES/PHASE-V0; panofsky_kit=relocated→ML-B-construction-DRAFT; lang=es
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de innovación docente
{: .lesson-editorial-note }

Galada y Baytar (2025) fundamentan la corrección de ajuste como objeto educativo. Coats (2026) fundamenta un módulo híbrido. Cheang y Suterwalla (2020) fundamentan una postura decolonial. Ninguna fuente prueba un método universal. **Laguna declarada:** la secuencia bodegón → prenda digital y el light-on-form como RCT de moda-HE siguen sin verificar en `dc-3d-form-volume-pedagogy`. La enseñanza de construcción perspectiva / Panofsky se relocó al borrador de enriquecimiento Volume–Depth (cascade PHASE-V0).

---

## Autoría asistida por IA

Esta lección se redactó con asistencia de IA bajo control editorial del autor.

Declaración de autoría asistida por IA: [leer la divulgación completa]({{ '/ai-declaration/' | relative_url }}).
