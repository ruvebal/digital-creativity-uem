---
layout: lesson
title: 'Master Lecture · Danza, cine y moda'
title_en: 'Master Lecture · Dance, cinema and fashion'
slug: danza-cine-moda
date: 2026-10-28
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/master-lectures/danza-cine-moda/
description: 'Una prenda cambia lo que un cuerpo en movimiento puede mostrar y hacer; una cámara cambia lo que vemos de ambos. Seis ideas, siete películas de dominio público, dos labs con la cámara del móvil y una auditoría de IA.'
status: pilot
tags: [master-lecture, danza, cine, vestuario, movimiento, fashion-film, camara-movil, auditoria-ia-generativa]
master_idea: 'Una prenda cambia lo que un cuerpo en movimiento puede mostrar y hacer; una cámara y un montaje cambian lo que vemos de ambos. Afirma solo hasta donde llegue tu evidencia.'
practice_anchor: 'Capturar movimiento con la cámara del móvil, transformarlo en Photoshop o Firefly y auditar lo que inventó la máquina'
frontier_signal: 'La influencia entre escena, pantalla y moda es fácil de ver y difícil de probar: hasta en casos famosos las fechas y los testimonios no coinciden.'
references: [shinkle-2008, sill-2008, de-perthuis-2008, kandinsky-2012, eckersall-2017, pfeiffer-2009, diaz-soloaga-2016, navarro-gavino-2022, mejias-couldry-2024]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
unit_id: ML-DCF (ES twin of /lessons/en/master-lectures/dance-cinema-fashion/)
provenance: identical PROVENANCE_LINE set to the EN canonical page (printed folios read from source PDFs; EPUB sections for Kandinsky and Mejias & Couldry).
quotes: Spanish renderings of English-language sources are course translations; the original wording and page are in the EN page and the ledger.
forge: digital-creativity-pedagogy/forge/DANCE-CINEMA-FASHION-FORGE.mdc · ledger: DANCE-CINEMA-FASHION-SOURCE-MEDIA-LEDGER.md
-->
{% endif %}

<style>
.dcf-media { margin: 1.5rem 0; }
.dcf-media video, .dcf-media img { display: block; width: 100%; height: auto; border-radius: 6px; background: #111; }
.dcf-media figcaption { font-size: .88rem; line-height: 1.45; margin-top: .45rem; opacity: .9; }
.dcf-grid { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); margin: 1.5rem 0; }
.dcf-grid .dcf-media { margin: 0; }
.dcf-grid--2 { grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); }
.dcf-diagram img { background: #F7F2E8; border: 1px solid rgba(0,0,0,.15); }
.dcf-prompt { border: 1px solid currentColor; border-left-width: 6px; border-radius: 6px; padding: .8rem 1rem; margin: 1rem 0; }
.dcf-prompt > p:first-child { margin-top: 0; }
.dcf-prompt code { white-space: normal; }
.dcf-watch { border: 1px dashed currentColor; border-radius: 6px; padding: .7rem 1rem; margin: 1rem 0; }
.dcf-guard { border-radius: 6px; padding: .8rem 1rem; margin: 1rem 0; background: rgba(180,68,44,.10); }
</style>

{% include lesson-semantic-graphic.html %}

<div class="lesson-opener" markdown="1">

> **Una prenda cambia lo que un cuerpo en movimiento puede mostrar y hacer. Una cámara y un montaje cambian lo que vemos de ambos.**

Esta es una **Master Lecture** de Creación Digital I. Su casa principal es el contenido oficial *Fuentes y referencias compositivas en el diseño de moda* (I.7): la danza, el cine y el vestuario escénico son fuentes compositivas para la moda. El ejercicio de animación del final (Ej 2 · T5) toca *Creación de imágenes digitales animadas* (I.8). **No** es una unidad, entrega ni nota nueva: lo que hagas va a tu portfolio como evidencia de Lab.

**Trae:** el móvil (cargado y con espacio), una prenda que se mueva (pañuelo, camisa, abrigo, falda) y tu acceso a Adobe Creative Cloud.

[English version]({{ '/lessons/en/master-lectures/dance-cinema-fashion/' | relative_url }})

</div>

<figure class="dcf-media dcf-diagram" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-session-flow.es.svg' | relative_url }}" alt="Ritmo de la sesión, 120 minutos: análisis 0 a 15, masterclass 15 a 55, apertura del Lab 55 a 60, ejercicio 1 capturar 60 a 85, ejercicio 2 transformar 85 a 110, compartir y declaración de IA 110 a 120." loading="lazy" decoding="async">
</figure>

## Objetivos de aprendizaje

Al terminar la sesión puedes:

1. Nombrar qué le hace una prenda al movimiento — **drapeado, extensión, tensión o reorganización** — y señalar el fotograma que lo muestra.
2. Explicar cómo **el tamaño del plano y el corte** deciden lo que una película nos deja ver de un cuerpo vestido.
3. Situar una afirmación de influencia en la **escalera de evidencia** (analogía → cita → intercambio → influencia documentada) y preguntar a quién se acredita.
4. Capturar movimiento con la **cámara del móvil**, transformarlo con **Photoshop o Firefly**, y **auditar y declarar** lo que inventó la IA.

---

## Análisis · un fotograma (15′)

Antes de los vídeos, lee una imagen con la [tarjeta de ocho pasos]({{ '/lessons/en/master-lectures/fashion-image-analysis/' | relative_url }}#quick-card-printable). En parejas, tres minutos por bloque.

<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/top-hat-1935.webp' | relative_url }}" alt="Fotografía promocional en blanco y negro: Ginger Rogers, con vestido largo claro y mangas de plumas, se inclina hacia atrás en el brazo de Fred Astaire, de frac. Las plumas se abren desde su brazo como un abanico." loading="lazy" decoding="async">
<figcaption>Ginger Rogers y Fred Astaire, fotografía promocional de <em>Top Hat</em> (Sombrero de copa) · RKO Radio Pictures · 1935. Dominio público (según Commons) · <a href="https://commons.wikimedia.org/wiki/File:Top-Hat-Rogers-Astaire.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>

1. **Describe:** cuerpos, prendas, luz, encuadre. **Formas:** ¿hacia dónde va la línea del vestido y dónde se corta?
2. **Origen / producción:** es una *foto promocional*, no un fotograma de la película. ¿Quién la posó y para quién?
3. **Crítica:** ¿quién se inclina y quién sostiene? ¿Qué congela la foto que el baile nunca detendría?

---

## Masterclass · seis ideas (40′)

### 1 · El cuerpo vestido en movimiento

Una prenda no es vestuario hasta que se mueve. Mirar movimiento también es corporal: ante un cuerpo representado, «proyectamos esas posturas y gestos sobre nuestro propio cuerpo, sintiéndolos en nuestra piel y nuestros huesos» [(Shinkle 2008, 222)](#ref-shinkle-2008).

<figure class="dcf-media" markdown="0">
<video controls preload="none" playsinline muted loop poster="{{ '/assets/images/master-lectures/dance-cinema-fashion/muybridge-woman-dress-dancing-poster.webp' | relative_url }}">
<source src="{{ '/assets/video/dance-cinema-fashion/muybridge-woman-dress-dancing.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption><strong>Bucle mudo, 2 s.</strong> Una mujer con un vestido fino y suelto levanta el bajo con las dos manos y gira; la tela sigue a las piernas con retraso y luego se asienta. Animación de la lámina de Eadweard Muybridge «Woman dancing (Miss Larrigan)», <em>Animal Locomotion</em> (1887). Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Woman_in_dress_dancing_(1887).gif" target="_blank" rel="noopener">Wikimedia Commons</a>. <em>Mira:</em> la tela llega <strong>después</strong> del cuerpo. Ese retraso es lo que fotografiarás en el Lab.</figcaption>
</figure>

<div class="dcf-grid" markdown="0">
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/duncan-genthe-dancing.webp' | relative_url }}" alt="Isadora Duncan, descalza, con una túnica suelta a la rodilla y un brazo alzado, fotografiada sobre fondo oscuro." loading="lazy" decoding="async">
<figcaption>Arnold Genthe, «Isadora Duncan dancing» (rango de fechas de la Library of Congress 1915–1942). Dominio público · Library of Congress vía <a href="https://commons.wikimedia.org/wiki/File:Isadora_Duncan_dancing_LOC_agc.7a09881.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fortuny-delphos-museo-traje.webp' | relative_url }}" alt="Vestido largo de seda negra con plisado muy fino sobre maniquí, en forma de columna, mangas cortas y un cinturón estrecho de cuentas." loading="lazy" decoding="async">
<figcaption>Mariano Fortuny y Madrazo (Granada, 1871), vestido Delphos, raso de seda negro. Museo del Traje, Madrid, MT111885. CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Museo_del_Traje_-_MT111885_-_Vestido_Delphos.jpg" target="_blank" rel="noopener">Museo del Traje / Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/fortuny-delphos-pink.webp' | relative_url }}" alt="Vestido Delphos rosa plisado sobre figura de exposición; los pliegues caen rectos hasta un charco de tela en el suelo." loading="lazy" decoding="async">
<figcaption>Fortuny, vestido Delphos rosa, años 20. Fotografía Mabalu, CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Pink_Delphos_dress_by_Fortuny,_1920s.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
</div>

La túnica «griega» de Duncan y la columna plisada de Fortuny toman prestada una idea de la Antigüedad. Se conoce muy poca película de Duncan bailando; su danza nos llega sobre todo por fotografías como las de Genthe — un medio quieto para un arte en movimiento.

**Pregunta:** ¿Qué cuerpo «clásico» se convierte aquí en ideal universal — y qué cuerpos e historias quedan fuera de ese ideal?

### 2 · El vestuario hace la coreografía

Hay vestuarios que siguen al cuerpo y otros que se convierten en la danza. Loïe Fuller patentó en 1894 una «prenda para bailarinas»: una falda amplia colgada de la cabeza, con varillas ligeras de aluminio o bambú para lanzar la tela en olas y alas — abre la [patente](https://patents.google.com/patent/US518347A/en){:target="_blank" rel="noopener"} como documento primario.

Y pasó algo que importa a quien estudia referencias: **la danza serpentina se copió por todas partes, y casi todas las primeras películas tituladas «Loïe Fuller» muestran a otras bailarinas.** Mira tres como evidencia, no como ilustración.

<div class="dcf-grid dcf-grid--2" markdown="0">
<figure class="dcf-media" markdown="0">
<video controls preload="none" playsinline muted poster="{{ '/assets/images/master-lectures/dance-cinema-fashion/annabelle-1894-poster.webp' | relative_url }}">
<source src="{{ '/assets/video/dance-cinema-fashion/annabelle-1894.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption><strong>Muda, 36 s.</strong> Cartón «Serpentine Dances». Una bailarina con tocado de estrellas hace girar una falda larga en un escenario pequeño; los últimos planos están teñidos a mano de amarillo y rojo para que la tela se lea como luz de color. <em>Serpentine Dances</em>, interpretada por Annabelle Whitford; Edison Manufacturing Company, W. K. L. Dickson, 1894. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Annabelle_Serpentine.ogv" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<video controls preload="none" playsinline muted poster="{{ '/assets/images/master-lectures/dance-cinema-fashion/lumiere-serpentine-1897-poster.webp' | relative_url }}">
<source src="{{ '/assets/video/dance-cinema-fashion/lumiere-serpentine-1897.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption><strong>Muda, 53 s.</strong> Ante un fondo marrón una bailarina gira enormes mangas de tela; cada vuelta tiene otro color — rosa, magenta, amarillo — y la tela se vuelve una secuencia de flores. <em>Danse serpentine</em>, producción Lumière, 1897; intérprete y operador sin identificar. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Danse_serpentine_(Lumi%C3%A8re,_1897).webm" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<video controls preload="none" playsinline muted poster="{{ '/assets/images/master-lectures/dance-cinema-fashion/serpentine-pathe-chomon-1902-poster.webp' | relative_url }}">
<source src="{{ '/assets/video/dance-cinema-fashion/serpentine-pathe-chomon-1902.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption><strong>Muda, 82 s.</strong> Cartón en catalán: «Loïe Fuller (1902) · Producció: Pathé (766) · L'original, acolorit a mà per Segundo de Chomón en el seu taller de Barcelona». Al aire libre, ante un jardín pintado, una bailarina abre alas blancas de tela con varillas. Commons fecha esta copia en 1901; el cartón dice 1902; no está establecido que baile la propia Fuller. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Loie_Fuller_(1901).ogv" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/toulouse-lautrec-fuller-1893.webp' | relative_url }}" alt="Boceto pintado, suelto, sobre cartón marrón: una figura casi desaparece dentro de remolinos de tela verde, blanca y violeta; se ven las piernas debajo." loading="lazy" decoding="async">
<figcaption>Henri de Toulouse-Lautrec, <em>Loïe Fuller aux Folies-Bergère</em> (1893), Musée Toulouse-Lautrec, Albi. Dominio público · fotografía Didier Descouens vía <a href="https://commons.wikimedia.org/wiki/File:(Albi)_-_La_Lo%C3%AFe_Fuller_aux-Folies-Berg%C3%A8re_-_Toulouse-Lautrec_(1893)_MTL.152.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>. Un pintor responde a la danza con línea emborronada, no con contorno.</figcaption>
</figure>
</div>

El cuaderno de la Bauhaus de Kandinsky te da una herramienta para mirar estas películas: «el cuerpo entero del bailarín, hasta la punta de los dedos, es en cada instante una composición ininterrumpida de líneas» — él atribuye la observación a la bailarina Gret Palucca [(Kandinsky 2012, “Line”)](#ref-kandinsky-2012).

En el polo opuesto, el *Ballet triádico* de Oskar Schlemmer (estreno en Stuttgart, 30 de septiembre de 1922) construyó **figuras rígidas y geométricas** que deciden cómo puede pisar y girar el cuerpo.

<div class="dcf-grid" markdown="0">
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/schlemmer-triadic-200.webp' | relative_url }}" alt="Fotografía en blanco y negro de figuras con vestuario en un escenario embaldosado: una con falda cónica de pinchos y un brazo como una maza, otra con forma oscura abombada; el vestuario oculta la anatomía." loading="lazy" decoding="async">
<figcaption>Figuras del <em>Ballet triádico</em>, reproducidas en Schlemmer, Moholy-Nagy y Molnár, <em>Die Bühne im Bauhaus</em> (1925); fotógrafo sin identificar. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Oskar_Schlemmer_Triadisches_Ballett_200.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/schlemmer-triadic-100.webp' | relative_url }}" alt="Dibujo lineal en tres columnas: pequeñas figuras esquemáticas hechas de conos, esferas, discos y espirales, ordenadas como un cuadro." loading="lazy" decoding="async">
<figcaption>Oskar Schlemmer, plan de figuras del <em>Ballet triádico</em> (1922). Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Oskar_Schlemmer_Triadisches_Ballett_100.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/schlemmer-staatsgalerie-2017.webp' | relative_url }}" alt="Sala de museo con paredes oscuras: tres figuras de vestuario sobre peanas bajas — un cuerpo de esfera dorada con piernas rayadas, una figura blanca con un disco, una figura cubierta de espirales." loading="lazy" decoding="async">
<figcaption>Figuras del <em>Ballet triádico</em> en la Staatsgalerie de Stuttgart, 2017 — una exposición de museo, no una función. Fotografía José Luiz Bernardes Ribeiro, CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Triadisches_Ballett_by_Oskar_Schlemmer_-_Staatsgalerie_-_Stuttgart_-_Germany_2017.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/schlemmer-programme-1922.webp' | relative_url }}" alt="Página de programa impresa en alemán, tipografía de palo seco: el orden de doce danzas en tres series, amarilla, rosa y negra." loading="lazy" decoding="async">
<figcaption>Programa del estreno, Stuttgart, 30 de septiembre de 1922 (p. 3); diseño gráfico de Oskar Schlemmer. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Das_Triadische_Ballett,_Programmzettel_1922.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>. Un documento, no una foto del estreno.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/graham-lamentation-eilber-1976.webp' | relative_url }}" alt="Una bailarina sentada, envuelta por completo en un tubo de tela clara estirada; solo se ven cara, manos y pies; la tela se tensa en diagonales." loading="lazy" decoding="async">
<figcaption>Janet Eilber interpreta <em>Lamentation</em> (1930) de Martha Graham, East Room de la Casa Blanca, 14 de octubre de 1976. National Archives (EE. UU.), dominio público · <a href="https://commons.wikimedia.org/wiki/File:Janet_Eilber_Performing_Martha_Graham%E2%80%99s_%E2%80%9CLamentation%E2%80%9D_in_the_East_Room_of_the_White_House_-_NARA_-_30805967.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
</div>

<figure class="dcf-media dcf-diagram" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-affordance-map.es.svg' | relative_url }}" alt="Diagrama del curso, dos por dos. Ejes: la prenda sigue o rediseña el cuerpo; amplifica o restringe el movimiento. Drapeado (túnica Duncan, Delphos de Fortuny), Extensión (Fuller: seda, varillas, luz eléctrica), Tensión (el tubo de punto de Graham), Reorganización (figuras triádicas de Schlemmer). Marcado como hipótesis del curso." loading="lazy" decoding="async">
<figcaption>Diagrama del curso (CC BY-NC-SA 4.0). Un mapa para discutir, no un hecho: coloca cada vídeo e imagen y defiende la posición con un fotograma.</figcaption>
</figure>

**Pregunta:** ¿Quién hizo estas prendas, quién podía moverse con ellas y quién se lleva el crédito de autoría — la bailarina, el diseñador, la costurera o quien firmó la patente?

### 3 · El cine encuadra el cuerpo en movimiento

Una cámara no se limita a registrar un baile: elige un encuadre, una distancia y un corte. Aun así, las cámaras «en la mayoría de los casos siguen pegadas a los movimientos concretos del cuerpo», y la cámara lenta o los cambios de perspectiva dramatizan lo que la percepción ordinaria no capta [(Pfeiffer 2009, 198)](#ref-pfeiffer-2009).

<figure class="dcf-media dcf-diagram" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-framing.es.svg' | relative_url }}" alt="Diagrama del curso: una figura con falda larga y tres encuadres discontinuos, figura entera, plano medio y primer plano. Dos líneas de tiempo de los mismos 30 segundos: una toma o seis cortes. Preguntas: ¿están los pies y el bajo en plano?, ¿quién decide el corte?, ¿qué vende el primer plano, el vestido o la estrella?" loading="lazy" decoding="async">
</figure>

<div class="dcf-grid" markdown="0">
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/swing-time-1936.webp' | relative_url }}" alt="Rogers con un vestido claro de volantes y Astaire de frac bailan sobre un suelo brillante; la falda se abre en el giro." loading="lazy" decoding="async">
<figcaption>Rogers y Astaire, <em>Swing Time</em> (En alas de la danza) · RKO · 1936, foto promocional. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Swing_Time_(1936).jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/follow-the-fleet-1936.webp' | relative_url }}" alt="Rogers con vestido claro de falda amplia, a medio paso junto a Astaire de frac, ambos en movimiento sobre una pista brillante." loading="lazy" decoding="async">
<figcaption>Rogers y Astaire, <em>Follow the Fleet</em> (Sigamos la flota) · RKO · 1936, foto promocional. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Ginger_Rogers_and_Fred_Astaire_-_Follow_the_Fleet_(1936).jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
</div>

<div class="dcf-watch" markdown="1">
**Ver en la fuente (pantalla del profesor, copia con licencia):** el número «Cheek to Cheek» de *Top Hat* (1935). No hay una inserción oficial verificada para esta página, así que el profesor lo reproduce desde una copia con licencia. **Mientras corre, cuenta:** ¿cuántos cortes? ¿Están los pies y el bajo en plano? ¿Cuándo se acerca la cámara y qué pierde?
</div>

Los estudios lo sabían. Hollywood usó la fotografía de moda para dar a sus estrellas un *look* de marca y presentó a la estrella como referente de moda [(Sill 2008, 130)](#ref-sill-2008) — aunque «es el público quien hace a la estrella» [(Sill 2008, 127)](#ref-sill-2008).

**Un pionero español encuadra la serpentina.** Segundo de Chomón (Teruel 1871 – París 1929) coloreó películas a mano y con plantilla en Barcelona y París, y convirtió la serpentina en efectos especiales — la danza como animación.

<figure class="dcf-media" markdown="0">
<video controls preload="none" playsinline muted poster="{{ '/assets/images/master-lectures/dance-cinema-fashion/chomon-serpentine-1908-poster.webp' | relative_url }}">
<source src="{{ '/assets/video/dance-cinema-fashion/chomon-serpentine-1908.mp4' | relative_url }}" type="video/mp4">
</video>
<figcaption><strong>Muda aquí (se eliminó la banda sonora añadida por quien la subió), 113 s, fragmento de una versión coloreada.</strong> En un interior pintado, un ilusionista hace aparecer a una bailarina cuyas faldas se abren en alas amarillas, rosas y violetas; fundidos y cortes hacen que la tela aparezca y desaparezca. Segundo de Chomón, <em>Création de la serpentine</em> (1908). Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Cr%C3%A9ation_de_la_serpentine_France_1908_Segundo_de_Chom%C3%B3n_(extrait_version_colorisl%C3%A9e)_-_Copie.webm" target="_blank" rel="noopener">Wikimedia Commons</a>. Aquí es el montaje, no la bailarina, lo que transforma el vestuario.</figcaption>
</figure>

**Pregunta:** ¿Cómo reparten nuestra atención el encuadre, el trabajo de los bailarines, el estrellato y el fotógrafo acreditado?

### 4 · El movimiento viaja con su contexto

Las referencias viajan: de la escena al cine, del cine a la pasarela, de un país a otro. Pero una referencia no lleva su historia consigo de forma automática. Usa la escalera: **sube solo hasta donde llegue tu evidencia**.

<figure class="dcf-media dcf-diagram" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-evidence-ladder.es.svg' | relative_url }}" alt="Diagrama del curso, escalera de evidencia: 1 analogía visual, nunca basta sola; 2 cita, un título o crédito nombra la fuente; 3 intercambio, un registro fechado de trabajo conjunto; 4 influencia documentada, testimonio, fechas y obras coinciden. Ejemplos: Admiring La Argentina de Kazuo Ohno (1977), con fuentes que dan 1926, 1927 o 1929 para cuando la vio bailar; Forsythe y Miyake, Fráncfort 1991 o 1992, hacia Pleats Please 1993. Panel lateral: la apropiación no es un peldaño sino una cuestión de poder." loading="lazy" decoding="async">
</figure>

**Caso · Madrid → Tokio.** Antonia Mercé, *La Argentina* (Buenos Aires, 1890 – 1936), llevó la danza española a escenarios internacionales. El bailarín japonés Kazuo Ohno la vio actuar de joven y, unos cincuenta años después, creó un solo con su nombre, *Admiring La Argentina* (1977, dirigido por Tatsumi Hijikata). El título es una **cita** comprobable; el año en que Ohno la vio no está claro — los archivos que puedes abrir dan 1926, 1927 y 1929.

<div class="dcf-grid" markdown="0">
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/la-argentina-bacarisas-poster.webp' | relative_url }}" alt="Cartel litográfico en color: una bailarina flamenca con vestido claro de volantes y mantón verde, brazos en alto, castañuelas; grandes letras «Antonia Mercé» y «Argentina»." loading="lazy" decoding="async">
<figcaption>Gustavo Bacarisas, cartel para Antonia Mercé, <em>La Argentina</em>; impreso por Rivadeneyra, Madrid. Dominio público · Bibliothèque nationale de France vía <a href="https://commons.wikimedia.org/wiki/File:Antonia_Merc%C3%A9._Argentina_-_affiche_-_G._Bacarisas_-_btv1b53229920q.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/la-argentina-genthe.webp' | relative_url }}" alt="La Argentina bailando con bata de cola de volantes, un brazo en alto, sobre escenario oscuro." loading="lazy" decoding="async">
<figcaption>Arnold Genthe, «La Argentina dancing» (entre 1928 y 1942). Dominio público · Library of Congress vía <a href="https://commons.wikimedia.org/wiki/File:La_Argentina_dancing_LOC_agc.7a09934.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
<figure class="dcf-media" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/kazuo-ohno-1986.webp' | relative_url }}" alt="Retrato cercano de Kazuo Ohno, anciano, cara pintada de blanco, ojos maquillados de azul y labios rojos, sonriendo suavemente." loading="lazy" decoding="async">
<figcaption>Kazuo Ohno, octubre de 1986. Fotografía subida por Ras67, CC BY 3.0 · <a href="https://commons.wikimedia.org/wiki/File:Kazuo_Ohno.jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>
</div>

<div class="dcf-watch" markdown="1">
**Ver en la fuente:** *Admiring La Argentina*, grabación de Charles Picq para la Maison de la Danse (1986) — [Numeridanse](https://numeridanse.com/en/dance-videotheque/admiring-la-argentina/){:target="_blank" rel="noopener"}. Mira un minuto y pregúntate qué cita Ohno: ¿un vestuario?, ¿un gesto?, ¿un sentimiento? Ninguno se ve como copia.
</div>

**Caso · escena → producto.** Los plisados de Issey Miyake para el Ballet de Fráncfort de William Forsythe (*The Loss of Small Detail*, 1991; algunas fuentes dicen 1992) se describen como prototipo de la línea Pleats Please (1993). Es un **intercambio** que termina en producto — y sigue siendo una afirmación que rastrear en registros fechados.

**Caso · ¿quién interpreta la cultura de quién?**

<figure class="dcf-media" style="max-width: 360px" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/st-denis-radha.webp' | relative_url }}" alt="Ruth St. Denis con un vestuario enjoyado y con flecos, vientre descubierto, brazos extendidos, con pequeños címbalos, en un retrato de estudio." loading="lazy" decoding="async">
<figcaption>Otto Sarony, Ruth St. Denis en <em>Radha</em>, 1908–09. New York Public Library, Denishawn Collection, sin restricciones conocidas · <a href="https://commons.wikimedia.org/wiki/File:Ruth_St._Denis_in_Radha._(3110871798).jpg" target="_blank" rel="noopener">Wikimedia Commons</a>.</figcaption>
</figure>

Una bailarina estadounidense se presenta como diosa hindú ante públicos occidentales. **Pregunta:** ¿a quién se nombra, se paga o se desplaza cuando una práctica entra en un mercado nuevo? ¿Qué registro separaría influencia, intercambio, apropiación y simple analogía visual?

### 5 · ¿A quién se vuelve extraño?

La moda lleva mucho tiempo alejando el cuerpo de la proporción «natural»; Henri Focillon escribió que «la moda inventa una humanidad artificial» (Focillon, citado en [de Perthuis 2008, 169](#ref-de-perthuis-2008)). Las imágenes de moda también pueden rechazar la gracia a propósito: Shinkle describe a una modelo «zarandeada como un maniquí de pruebas de choque», fuera del léxico habitual de poses [(Shinkle 2008, 222)](#ref-shinkle-2008).

De diseñadores españoles como **David Delfín** o **Ana Locking** se ha hablado en términos de provocación y cuerpo extraño; la marca parisina **Matières Fécales** trabaja con el choque. La *abyección* es una teoría sobre a quién se expulsa — **no** un sinónimo de «imagen impactante». Esta sesión no da veredicto sobre ellos: en tu propia investigación, trae **evidencia, no adjetivos** — la declaración del diseñador, la recepción en prensa, quién vestía y a quién se hizo parecer extraño.

La imagen en movimiento también puede abrir espacio: una investigación sobre fashion films entre 2010 y 2020 aborda la representación *queer* a través de la participación, las experiencias y los discursos narrados en ese formato [(Navarro Gaviño 2022, 195)](#ref-navarro-gavino-2022).

**Pregunta:** ¿Esta provocación discute una norma — o convierte cuerpos excluidos en espectáculo? ¿Qué relato y qué evidencia de recepción permitirían distinguirlo?

### 6 · El butoh tiene historias, no un *look*

El *butō* nació en el Japón de posguerra (Tatsumi Hijikata, Kazuo Ohno) y se extendió en muchas direcciones, incluida una larga recepción en Argentina. Sus imágenes más conocidas — cuerpo pintado de blanco, distorsión lenta — son lo más fácil de copiar y lo que menos informa. **Una pose sola no puede decirnos de dónde viene un movimiento.** Fíjate en que el solo más famoso de Ohno, de la idea 4, es un homenaje a una bailarina española: la historia cruza el *look*.

Es también lo que pasa cuando un generador de imágenes aprende de imágenes recolectadas en masa. Mejias y Couldry llaman a la captura masiva de datos «extensos actos de apropiación» y sostienen que el atractivo de la «IA generativa» es sobre todo un dispositivo para distraer de ello [(Mejias and Couldry 2024, introduction)](#ref-mejias-couldry-2024). Lo pondrás a prueba en la auditoría del Lab.

**Pregunta:** ¿Quién puede nombrar una tradición, quién gana con su circulación y cuándo el exotismo borra el contexto?

---

## Lab (portfolio) · 50′

Dos ejercicios. Cada uno ofrece un **menú de propuestas** — elige; no las hagas todas. Todo lo que hagas va a tu índice de portfolio / Canvas con una nota breve.

<div class="dcf-guard" markdown="1">
**Consentimiento y cuidado (innegociable).** Fotografía a un compañero solo si dice que sí, y enséñale el resultado. La cara es opcional — manos, bajos, sombras y espaldas bastan. **Nunca subas la imagen de un compañero a Firefly ni a ninguna IA en la nube sin su consentimiento explícito**; en caso de duda, usa tu propio cuerpo, tu prenda o un objeto. Borra si te lo piden. El trabajo del estudiante es de su autoría: nada se expone sin un permiso aparte.
</div>

<figure class="dcf-media dcf-diagram" markdown="0">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-onion-skin.es.svg' | relative_url }}" alt="Diagrama del curso del método del Lab: 1 dispara una ráfaga de unas doce fotos de un giro; 2 quédate seis; 3 apílalas como capas de Photoshop al 25 por ciento o con fusión Aclarar; 4 una sola imagen muestra cómo viajó la prenda en el tiempo." loading="lazy" decoding="async">
</figure>

### Ejercicio 1 · Capturar con la cámara del móvil (25′)

Elige **dos** propuestas. Pared lisa, luz lateral (una ventana o la linterna del móvil de un compañero). Dispara mucho; quédate con poco.

<div class="dcf-prompt" markdown="1">
**C1 · Estudio serpentina (a partir de Fuller).** Gira con un pañuelo, camisa o abrigo extendido en los brazos o en dos bolígrafos como «varillas». Graba 5 segundos en **Cámara lenta** (iPhone *Slo-mo* / Android *Slow motion*). Oscurece la esquina y colorea la luz: pon un color a pantalla completa en otro móvil y úsalo como filtro.
</div>

<div class="dcf-prompt" markdown="1">
**C2 · Cronofotografía (a partir de Muybridge).** Un giro, **modo ráfaga** (mantén el disparador o deslízalo a la izquierda en iPhone), unas 12 fotos, con el móvil fijo contra una mochila o la pared. Necesitas estas fotos para el Ej 2 · T1.
</div>

<div class="dcf-prompt" markdown="1">
**C3 · El mismo baile, otra película (a partir de Astaire).** Una frase de 8 tiempos, dos veces: **A** una toma, figura entera, pies y bajo en plano; **B** tres primeros planos cortos (bajo, manos, cara) montados en el editor del móvil. Compara con el diagrama de encuadre: ¿qué vende B?
</div>

<div class="dcf-prompt" markdown="1">
**C4 · Vestuario de restricción (a partir de Schlemmer).** En cinco minutos, construye una extensión rígida — cono de papel, disco de cartón, percha, cinta — en un brazo, la cabeza o el bajo. Graba el movimiento que **obliga**. Una frase: ¿qué paso se volvió imposible y qué paso nuevo apareció?
</div>

<div class="dcf-prompt" markdown="1">
**C5 · El bailarín dibuja líneas (a partir de Kandinsky).** Larga exposición: en iPhone **Live Photo → efecto Exposición larga**; en Android modo **Noche / Pro** a 1–2 s. Mueve una prenda con la linterna de un móvil metida dentro. La luz se vuelve la línea que dibuja el cuerpo.
</div>

### Ejercicio 2 · Transformar con Photoshop o Firefly — y auditar (25′)

Elige **una** transformación. La **auditoría es obligatoria** para quien use IA generativa. Mantén activadas las **Content Credentials** (credenciales de contenido) al exportar.

<div class="dcf-prompt" markdown="1">
**T1 · Una imagen del tiempo (sin IA).** Photoshop: *Archivo → Secuencias de comandos → Cargar archivos en pila* con seis fotos de C2. Pon cada capa en **Aclarar** (pared oscura) o al 25 % de opacidad. Enmascara el temblor. Resultado: el recorrido de la prenda en una imagen.
</div>

<div class="dcf-prompt" markdown="1">
**T2 · Reencuadrar para cine (Expansión generativa).** Toma una foto vertical de C1/C3. Photoshop **herramienta Recortar → Relleno: Expansión generativa** a 16:9. Después dibuja un contorno rojo alrededor de cada píxel que inventó la IA. Pregunta: ¿quién decidió lo que queda fuera de campo — y qué supuso sobre el espacio, el público, el cuerpo?
</div>

<div class="dcf-prompt" markdown="1">
**T3 · Extender la prenda (Relleno generativo).** Selecciona con el lazo alrededor de la manga o el bajo y escribe uno de estos *prompts* (en inglés suelen dar resultados más estables):
`pleated silk unfolding into wide wings, theatrical side light, motion blur`
`rigid painted geometric shell around the arm, disc and cone forms, stage spotlight`
Genera tres variantes. ¿En cuál podría moverse un cuerpo de verdad? Anota por qué.
</div>

<div class="dcf-prompt" markdown="1">
**T4 · Firefly con tu foto como estructura.** Firefly **Texto a imagen**, sube tu foto de C como **Referencia de composición** (intensidad alta). Plantilla:
`[prenda + material] en movimiento, [luz: lateral / contraluz / de color], figura entera, pared lisa, fotografía documental`
Conserva tu pose; cambia solo la prenda. Compara: ¿qué conservó el modelo de tu movimiento y qué suavizó?
</div>

<div class="dcf-prompt" markdown="1">
**T5 · Animar una foto (vídeo de Firefly · puente a I.8).** Firefly **Generar vídeo → Imagen a vídeo** desde tu mejor foto de C, unos 5 s:
`the fabric keeps swirling, camera static, same lighting`
Ponlo al lado de tu cámara lenta real de C1. ¿Qué física inventó el modelo para la tela?
</div>

<div class="dcf-prompt" markdown="1">
**AUDITORÍA (obligatoria con cualquier paso generativo).** En Firefly, genera cuatro imágenes para `butoh dancer` **o** `flamenco dancer`. Anota lo que supone el modelo: piel, maquillaje, género, edad, escenario, vestuario. Después escribe **una frase** con la escalera de evidencia: *¿a qué peldaño puede llegar una imagen generada?* (Pista: solo puede parecerse — peldaño 1.)
</div>

**Entrada de portfolio:** una captura (Ej 1) + una transformación (Ej 2) + tu frase de auditoría + una declaración de IA de dos líneas — herramienta, qué aportó, qué comprobaste — según la [declaración de IA del curso]({{ '/ai-declaration/' | relative_url }}). Los créditos generativos y funciones dependen de tu plan de Adobe; si una función no está disponible, haz T1.

### Hacia dónde va esto

El fashion film es heredero de la publicidad audiovisual, el cine, el cortometraje, el videoclip y el videoarte, y una forma de contenido de marca [(Díaz Soloaga and García Guerrero 2016, 49)](#ref-diaz-soloaga-2016). Los escenarios interactivos van más lejos: en *Glow*, de Chunky Move, una cámara cenital sigue a la bailarina para que un proyector mapee luz y gráficos con precisión sobre las coordenadas de su cuerpo [(Eckersall, Grehan, and Scheer 2017, 47)](#ref-eckersall-2017) — el cuerpo pasa a producir «la forma concreta de su entorno digital inmediato» [(Eckersall, Grehan, and Scheer 2017, 48)](#ref-eckersall-2017). La proyección siempre plantea «quién y qué es visible» y «quién mira» [(Eckersall, Grehan, and Scheer 2017, 25)](#ref-eckersall-2017).

---

## Tarjeta rápida (imprimible)

<div class="quick-card not-prose" markdown="0">
<p class="quick-card__nav"><button type="button" class="quick-card__print">Imprimir esta tarjeta</button></p>
<p class="quick-card__title">Tarjeta de movimiento</p>
<figure class="quick-card__graph">
<img src="{{ '/assets/images/master-lectures/dance-cinema-fashion/dcf-affordance-map.es.svg' | relative_url }}" alt="Mapa de dos por dos: drapeado, extensión, tensión, reorganización." width="760" height="470">
</figure>
<ol class="quick-card__fields">
<li><span>Vídeo / imagen + crédito</span><span class="quick-card__line"></span></li>
<li><span>La prenda hace (drapeado · extensión · tensión · reorganización)</span><span class="quick-card__line"></span></li>
<li><span>Tamaño de plano · número de cortes</span><span class="quick-card__line"></span></li>
<li><span>Lo que oculta el encuadre</span><span class="quick-card__line"></span></li>
<li><span>Afirmación de influencia + peldaño (1–4)</span><span class="quick-card__line"></span></li>
<li class="quick-card__critical"><span>¿A quién se acredita, se paga, se desplaza?</span><span class="quick-card__line"></span></li>
<li><span>IA usada · aportación · qué comprobé</span><span class="quick-card__line"></span></li>
</ol>
</div>

---

## Conclusión

Tres hábitos salen contigo de esta aula. Mira **qué hace la tela después de que se mueve el cuerpo**. Cuenta **los cortes** antes de elogiar el baile. Y sube **solo hasta donde llegue tu evidencia** — hasta las historias de influencia famosas tienen fechas en disputa. La auditoría de IA es el mismo hábito aplicado a las máquinas: una imagen generada puede parecerse a una tradición; no puede documentarla.

## Créditos de medios

Todas las películas e imágenes son de dominio público o con licencia abierta; cada pie nombra autor, licencia y página de origen. Las películas se alojan como copias mudas recodificadas de los originales de dominio público (se eliminó una banda sonora añadida por quien la subió). Los diagramas son del curso (CC BY-NC-SA 4.0). Las obras con derechos (*Top Hat*, *Admiring La Argentina*) no se insertan: se ven en la fuente.

## Referencias

{% include references.html %}

---

## Nota editorial · Trabajo en curso · Práctica de Innovación Docente

**Laguna declarada:** la bibliografía específica sobre Fuller, Duncan, Schlemmer, Graham, el encuadre de Astaire, la recepción transnacional del butoh y la abyección en moda aún no está verificada por página en la bibliografía del curso; esas partes se enseñan con documentos primarios (patente, programa, copias de películas, páginas de archivo) y preguntas abiertas, no con citas. Las citas en castellano de fuentes en inglés son traducciones del curso.  
**Evidencia faltante:** el año en que Ohno vio por primera vez a La Argentina (1926, 1927 o 1929 según los archivos); el año del estreno de *The Loss of Small Detail* de Forsythe con vestuario de Miyake (1991 o 1992); la identidad de las bailarinas de las primeras películas serpentinas; una copia oficial insertable de *Top Hat*.  
**Nota al editor:** esta sesión pide al alumnado usar las herramientas generativas en la nube de Adobe con su propia licencia de Creative Cloud, a petición del profesor, con una regla de consentimiento para imágenes de compañeros y una auditoría obligatoria; los materiales del curso no usan imágenes generativas.

## Autoría asistida por IA

Esta lección se redactó con asistencia de IA bajo el control editorial del autor. Declaración de IA del alumnado y la docencia: [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).
