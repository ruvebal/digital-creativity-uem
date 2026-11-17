---
layout: lesson
title: 'U5 · Herramientas digitales y análisis de datos'
title_en: 'U5 · Digital tools and data analysis'
slug: u5-herramientas-datos
date: 2026-11-17
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/nuevos-medios-moda/u5-herramientas-datos/
description: 'Métricas, KPI y dashboards en la comunicación de moda: qué cuenta cada número, por qué medir no es probar, de dónde salen los datos y quién rinde cuentas.'
status: forged
campaign_ids: [reformation-refscale, norrona-higg-msi-nca, zara-brasil-lista-suja]
tags: [nuevos-medios-moda, u5, plataformas, moda, datos, kpi]
themes: [herramientas-analisis-datos, big-data-comunicacion, medicion-optimizacion]
master_idea: 'Cada métrica es una decisión sobre qué cuenta como éxito: medir no es probar, y los datos tienen origen, coste y dueño.'
practice_anchor: 'Auditoría de dashboard con la ficha KPI + plan de medición con una línea roja'
deck_url: /tracks/es/uem/2627-nm/u5-herramientas-datos/
references: [unep-2023, couldry-mejias-2018]
---

<!-- prettier-ignore-start -->
## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}
<!-- prettier-ignore-end -->

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
unit_id: U5
contenidos: Comunicación digital (herramientas y análisis de datos)
competencies: [CON4, COMP8]
project_slug: profield-nuevos-medios-moda-2026-27
campaign_ledger: 20260925T200000Z (ranks 14, 17) + supplemental regulator case (allocation index 2026-11-17)
forge: master-lecture-forger 1.0 + nm-unit-forge · cold B1 via lesson-scribe (thessia-scholar-v3) · records listed below
grounding:
  creativity: "course operational frame (evidence ladder) — studio stance, no scholarly cite"
  fashion_image: "UNEP 2023, 33 · evaluator-safe (measurement tools and scorecards in fashion claims)"
page_basis: printed page read on the source page (vault.py). UNEP printed = PDF sequence − 5 (footer folio).
PROVENANCE_LINE: claim=U5.measuring-is-hard; status=VERIFIED; page_basis=printed; source={coat=08e2ea03; node=a18e3ed5-4cbf-5e0e-8444-840592c5ca64; pdf_seq=93; printed=88}; public="(United Nations Environment Programme 2023, 88)"; evaluator_safe=yes
PROVENANCE_LINE: claim=U5.governance; status=VERIFIED; page_basis=printed; source={coat=08e2ea03; node=7645b330-6b32-5b9b-9738-c762cf381975; pdf_seq=93; printed=88}; public="(United Nations Environment Programme 2023, 88)"; evaluator_safe=yes
PROVENANCE_LINE: claim=U5.tools-not-fit; status=VERIFIED; page_basis=printed; source={coat=08e2ea03; node=199227dc-2c3a-5b34-9d4f-2caf3a0d537d; pdf_seq=38; printed=33}; public="(United Nations Environment Programme 2023, 33)"; evaluator_safe=yes
PROVENANCE_LINE: claim=U5.nca-misleading; status=VERIFIED; page_basis=printed; source={coat=08e2ea03; node=48bfa4fd-0b99-5837-bb54-594d56e131a4; pdf_seq=38; printed=33}; public="(United Nations Environment Programme 2023, 33)"; evaluator_safe=yes
PROVENANCE_LINE: claim=U5.data-colonialism; status=VERIFIED; page_basis=printed (OnlineFirst 1–14); source={coat=630cb66e; node=4ddbceb0-9a8e-5fce-ae84-ca0939cbd70c; pdf_seq=2; printed=2}; public="(Couldry and Mejias 2018, 2)"; evaluator_safe=yes; resolver prints "(Couldry 2019, 3)" — co-author restored, OnlineFirst year and folio used
CAMPAIGNS (linked, never quoted as scholarship): reformation-refscale (rank 17, Track A) · norrona-higg-msi-nca (supplemental, regulator) · zara-brasil-lista-suja (rank 14, Track B)
THESSIA_RECORDS: see forge/receipts/NM-U5-U6-THESSIA-RAW.json and NM-U5-U6-FORGE-RECEIPT.md
-->
{% endif %}

<div class="lesson-opener" markdown="1">
> **Cada métrica es una decisión sobre qué cuenta como éxito: medir no es probar, y los datos tienen origen, coste y dueño.**

**Diapositivas de clase:** [abrir deck]({{ '/tracks/es/uem/2627-nm/u5-herramientas-datos/' | relative_url }})
</div>

## Sesión de un vistazo (120′)

| Tiempo | Bloque | Qué haces |
| --- | --- | --- |
| 0–15′ | Análisis | Lees un gráfico de 1858 que cambió una política |
| 15–55′ | Masterclass | Cinco ideas: métrica · medir no es probar · extracción · contra-datos · optimizar con criterio |
| 55–105′ | Laboratorio (portafolio) | Ejercicio 1 auditoría de dashboard · Ejercicio 2 plan de medición |
| 105–120′ | Puesta en común | Dos estudiantes muestran un KPI que «miente» |

## Marco: medir en la comunicación de moda

En esta unidad, una **métrica** es un número que una herramienta produce; un **KPI** es la métrica que un equipo eligió como señal de éxito; un **dashboard** es la pantalla donde esas elecciones se vuelven rutina. Ninguno de los tres es neutral: cada uno decide qué se ve y qué desaparece.

La comunicación de moda añade una responsabilidad concreta. Sus números no solo miden campañas: también sostienen **afirmaciones** sobre huella, materiales y condiciones de trabajo. El *Sustainable Fashion Communication Playbook* del PNUMA lo resume con prudencia: medir el impacto de la comunicación «can be a challenge, particularly for complex and long-term social and behaviour change» [(United Nations Environment Programme 2023, 88)](#ref-unep-2023).

<figure class="lesson-figure" id="figure-u5-ladder" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/nm-u5-evidence-ladder-b044bc3280f2.svg' | relative_url }}" width="1600" height="900" alt="Diagrama del curso: seis peldaños de evidencia, de la exposición (impresiones, dato de la plataforma) al resultado independiente (auditoría, inspección o dato público, producido por un tercero)." loading="lazy" decoding="async">
<figcaption><strong>La escalera de la evidencia.</strong> Marco operativo del curso: cada número de esta unidad se sitúa en un peldaño. Diagrama original · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

## Objetivos de aprendizaje

Al final de esta unidad podrás:

1. Explicar por qué una métrica es una **decisión** sobre qué cuenta como éxito, y distinguir **indicador** de **efecto**.
2. Situar cualquier dato de una campaña en un **peldaño de evidencia** y decir quién lo produce.
3. Leer una cifra de sostenibilidad o un índice como **afirmación** que necesita método y verificación.
4. Nombrar el coste de los datos de audiencia (**colonialismo de datos**) y reconocer **contra-datos** públicos que una marca no controla.
5. Diseñar un plan de medición con una **línea roja** explícita.

---

## Análisis · un gráfico de 1858 (15′)

<figure class="lesson-figure" id="figure-u5-nightingale" markdown="0">
<img src="{{ '/assets/images/deck-media/c1de5c6e83b2145b.webp' | relative_url }}" alt="Diagrama de rosa de Florence Nightingale (1858): dos espirales de cuñas azules, rojas y negras comparan las causas de muerte del ejército británico mes a mes." loading="lazy" decoding="async">
<figcaption>Florence Nightingale, <em>Diagram of the Causes of Mortality in the Army in the East</em>, 1858. Dominio público · <a href="https://commons.wikimedia.org/wiki/File:Diagram_of_the_Causes_of_Mortality_in_the_Army_in_the_East._(IA_dr_diagram-of-the-causes-of-mortality-in-the-army-in-the-east-10563002).jpg" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>.</figcaption>
</figure>

Trabaja en parejas con los tres primeros pasos de la [ficha de análisis de imagen de moda]({{ '/lessons/en/master-lectures/fashion-image-analysis/' | relative_url }}):

- **Describe.** Cuñas de colores, mes a mes, en dos espirales. ¿Qué ves primero?
- **Datos.** Las cuñas azules —muertes por enfermedades evitables— son mucho mayores que las rojas de las heridas. El diseño decide qué comparación salta a la vista.
- **Crítica.** Nightingale eligió qué contar y cómo mostrarlo para cambiar la sanidad militar. ¿Qué decide tu dashboard por ti?

---

## Masterclass · cinco ideas (40′)

### 1 · Una métrica decide qué cuenta

<!--B1:U5:1-->

<figure class="lesson-figure" id="figure-u5-mission-control" markdown="0">
<img src="{{ '/assets/images/deck-media/1340167941ac09c8.webp' | relative_url }}" alt="Controladores de vuelo del Apolo 11 celebran en la sala de control de Houston en julio de 1969, con banderas y puros junto a las consolas." loading="lazy" decoding="async">
<figcaption>Sala de control del Apolo 11, Houston, julio de 1969: se celebra lo que las pantallas cuentan. NASA Johnson Space Center · dominio público · <a href="https://commons.wikimedia.org/wiki/File:Inflight_-_Apollo_XI_(Mission_Control_Center_-MCC-)_-_MSC_(S69-40302).jpg" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>.</figcaption>
</figure>

### 2 · Medir no es probar

<!--B1:U5:2-->

> Some of the measurement tools available are critiqued as not fit for purpose and consequently fraught with controversy

<p class="quote-ref" markdown="1">— [(United Nations Environment Programme 2023, 33)](#ref-unep-2023)</p>

**Caso · Reformation RefScale** (rank 17 · Track A). La marca muestra una cifra de huella por prenda y publica su [metodología RefScale 2023](https://media.thereformation.com/image/upload/v1680279343/pdfs/RefScale-Methodology-2023.pdf){:target="_blank" rel="noopener noreferrer"} y una [declaración de verificación independiente](https://media.thereformation.com/image/upload/v1717624075/pdfs/Point%20B%20Independent%20Assurance%20Statement%20-%20Reformation%20RefScale_23%20.pdf){:target="_blank" rel="noopener noreferrer"}. Es transparencia contable de marca, no un movimiento social: léela como afirmación con método.

**Caso crítico suplementario · Norrøna × Higg MSI.** En 2022 la autoridad noruega de consumo consideró engañoso que la marca comparara algodón orgánico y convencional con datos del índice Higg MSI, y las autoridades de consumo de Noruega y Países Bajos publicaron una guía conjunta sobre su uso ([FashionUnited, octubre de 2022](https://fashionunited.uk/news/business/norwegian-and-dutch-watchdogs-publish-guidance-on-higg-msi-use/2022101165634){:target="_blank" rel="noopener noreferrer"} · [Forbrukertilsynet, guía oficial](https://www.forbrukertilsynet.no/eng-articles/consumer-authorities-issue-guidance-on-environmental-claims-to-the-textile-industry){:target="_blank" rel="noopener noreferrer"}). El PNUMA recoge el criterio: esa comparación era

> not evidence-backed when it comes to comparing the environmental footprint of an organic cotton t-shirt with a conventional cotton one, and thus misleading

<p class="quote-ref" markdown="1">— [(United Nations Environment Programme 2023, 33)](#ref-unep-2023)</p>

<figure class="lesson-figure" id="figure-u5-cotton" markdown="0">
<img src="{{ '/assets/images/deck-media/347515a5d720e1f0.webp' | relative_url }}" alt="Campo de algodón maduro en Floyd County, Georgia (2025): miles de cápsulas blancas abiertas hasta el horizonte." loading="lazy" decoding="async">
<figcaption>El algodón no viene con su número puesto. Bubba73 · CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Cotton_field,_Floyd_County,_GA,_US.jpg" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>. No es una imagen de ninguno de los casos.</figcaption>
</figure>

### 3 · Los datos se extraen de la vida

<!--B1:U5:3-->

> Data colonialism combines the predatory extractive practices of historical colonialism with the abstract quantification methods of computing.

<p class="quote-ref" markdown="1">— [(Couldry and Mejias 2018, 2)](#ref-couldry-mejias-2018)</p>

<figure class="lesson-figure" id="figure-u5-servers" markdown="0">
<img src="{{ '/assets/images/deck-media/3c70a8ae4f2e05c6.webp' | relative_url }}" alt="Armario de servidores de un centro de datos en Ontario, California: filas de unidades con luces verdes encendidas." loading="lazy" decoding="async">
<figcaption>La infraestructura física de los datos. Ontariodatacenter · CC BY-SA 4.0 · <a href="https://commons.wikimedia.org/wiki/File:Ontario_Datacenter_California_7.jpg" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>.</figcaption>
</figure>

### 4 · Los datos también rinden cuentas

<!--B1:U5:4-->

**Caso · Zara Brasil** (rank 14 · Track B). La fiscalía laboral documentó trabajo esclavo en talleres proveedores, la justicia responsabilizó a la marca y esta podía entrar en la *lista suja*, el registro público de empleadores sancionados ([Ministério Público do Trabalho, São Paulo](https://www.prt2.mpt.mp.br/513-justica-responsabiliza-zara-por-trabalho-escravo-e-empresa-pode-entrar-na-lista-suja){:target="_blank" rel="noopener noreferrer"} · [dosier de Repórter Brasil](https://reporterbrasil.org.br/wp-content/uploads/2016/08/From-moral-responsibility-to-legal-liability.pdf){:target="_blank" rel="noopener noreferrer"}). Es un expediente, no una anécdota de redes: aquí el dato viene de inspectores y tribunales.

<figure class="lesson-figure" id="figure-u5-hine" markdown="0">
<img src="{{ '/assets/images/deck-media/0af12140980ac367.webp' | relative_url }}" alt="Fotografía de Lewis Hine (1910): una familia cose prendas en casa, en el Upper East Side de Nueva York; adultos y niñas trabajan juntos junto a una ventana." loading="lazy" decoding="async">
<figcaption>Lewis Wickes Hine, <em>Garment workers, Upper East Side, N.Y.C.</em>, 1910, para el National Child Labor Committee: la fotografía como prueba para cambiar leyes. Library of Congress · dominio público · <a href="https://commons.wikimedia.org/wiki/File:Garment_workers._Upper_East_Side,_N.Y.C._LOC_nclc.04080.jpg" target="_blank" rel="noopener noreferrer">Wikimedia Commons</a>. No es el caso brasileño.</figcaption>
</figure>

### 5 · Optimizar con criterio

<!--B1:U5:5-->

El PNUMA pide llevar los principios también al informe interno: el éxito «must not only look like integrating the principles into the communicator's practice, but also into their internal reporting, with an accountability and governance structure created against them» [(United Nations Environment Programme 2023, 88)](#ref-unep-2023).

<figure class="lesson-figure" id="figure-u5-kpi" markdown="0">
<img src="{{ '/assets/images/lesson-figures/visual-forger/nm-u5-kpi-audit-95efe33c02cb.svg' | relative_url }}" width="1600" height="900" alt="Diagrama del curso: cinco preguntas para auditar la tasa de engagement — qué cuenta, qué deja fuera, quién produce el dato, qué decisión provoca y, en rojo, qué prueba falta." loading="lazy" decoding="async">
<figcaption><strong>Ficha de auditoría de un KPI.</strong> Hoja de trabajo del Ejercicio 1. Diagrama original · Rubén Vega Balbás · CC BY-NC-SA 4.0.</figcaption>
</figure>

---

## Laboratorio / portafolio (B2) · 50′

> **Datos y cuidado.** Usa estadísticas de una cuenta tuya o de una marca pública. Anonimiza capturas: ningún nombre, foto ni dato de otras personas. No subas datos de terceros a ninguna herramienta de IA.

### Ejercicio 1 · Auditoría de dashboard (25′)

1. Abre las estadísticas de una cuenta (Instagram, TikTok o la web de una marca).
2. Elige **tres KPI** que el panel muestra en primer plano.
3. Para cada uno, completa la ficha: *qué cuenta · qué deja fuera · quién produce el dato · qué decisión provoca · qué prueba falta*.
4. Sitúa cada KPI en un peldaño de la escalera de la evidencia.

**Ejemplo:** *Tasa de engagement · cuenta reacciones, no lectura · deja fuera a quien mira sin reaccionar · la produce la plataforma · empuja a repetir lo llamativo · falta saber si alguien cambió una conducta.*

### Ejercicio 2 · Plan de medición con criterio (25′)

1. Escribe **un objetivo** de campaña en una frase (no «más seguidores»).
2. Elige **tres indicadores** en peldaños distintos de la escalera.
3. Para cada uno, di qué **decisión** cambiaría si sube o baja.
4. Escribe **una línea roja**: algo que no optimizarías aunque mejorara el número (por ejemplo, no usar urgencia falsa ni datos de menores).

**Entrada de portafolio:** la ficha (Ej. 1) y el plan de una página (Ej. 2). Si usaste alguna herramienta de IA, decláralo según la [guía de declaración de IA]({{ '/ai-declaration/' | relative_url }}).

## Problema individual (B3)

En dos frases: elige un KPI de una campaña de moda real, di qué cuenta y explica qué prueba independiente haría falta para afirmar que la campaña cambió algo.

## Repaso

1. ¿Por qué una métrica es una decisión?
2. ¿Qué diferencia hay entre un indicador y un efecto?
3. ¿Qué decidió en 2022 la autoridad noruega sobre el Higg MSI?
4. ¿Qué es el colonialismo de datos?
5. ¿Qué es la *lista suja* de Brasil?

## Conclusión

Un dashboard cuenta lo que alguien decidió contar. Medir bien empieza por decir qué no prueba cada número, de dónde sale y quién paga su recogida. En [U6]({{ '/lessons/es/nuevos-medios-moda/u6-futuro-comunicacion-digital/' | relative_url }}), cuando la imagen la produce una máquina, la pregunta cambia: ¿qué tendrías que declarar?

## Casos y créditos de campaña

Cada caso pertenece solo a esta unidad dentro del curso. Las imágenes de campaña no se reproducen: se enlazan en su fuente.

| Caso | Tipo | Qué enseña | Fuente |
| --- | --- | --- | --- |
| **Reformation RefScale** | rank 17 · Track A | cifra de huella con método publicado | [Metodología 2023](https://media.thereformation.com/image/upload/v1680279343/pdfs/RefScale-Methodology-2023.pdf){:target="_blank" rel="noopener noreferrer"} · [verificación independiente](https://media.thereformation.com/image/upload/v1717624075/pdfs/Point%20B%20Independent%20Assurance%20Statement%20-%20Reformation%20RefScale_23%20.pdf){:target="_blank" rel="noopener noreferrer"} |
| **Norrøna × Higg MSI** | suplementario · regulador | un índice no basta como prueba de una comparación | [Forbrukertilsynet](https://www.forbrukertilsynet.no/eng-articles/consumer-authorities-issue-guidance-on-environmental-claims-to-the-textile-industry){:target="_blank" rel="noopener noreferrer"} · [FashionUnited](https://fashionunited.uk/news/business/norwegian-and-dutch-watchdogs-publish-guidance-on-higg-msi-use/2022101165634){:target="_blank" rel="noopener noreferrer"} |
| **Zara Brasil** | rank 14 · Track B | contra-datos públicos: inspección, tribunal, registro | [MPT São Paulo](https://www.prt2.mpt.mp.br/513-justica-responsabiliza-zara-por-trabalho-escravo-e-empresa-pode-entrar-na-lista-suja){:target="_blank" rel="noopener noreferrer"} · [Repórter Brasil](https://reporterbrasil.org.br/wp-content/uploads/2016/08/From-moral-responsibility-to-legal-liability.pdf){:target="_blank" rel="noopener noreferrer"} |

## Créditos de imágenes

Fondos del deck y figuras: telar Jacquard (Stephencdickson, CC BY-SA 4.0), diagrama de Florence Nightingale (dominio público), sala de control del Apolo 11 (NASA, dominio público), tarjeta perforada Hollerith (dominio público), campo de algodón (Bubba73, CC BY-SA 4.0), centro de datos (Ontariodatacenter, CC BY-SA 4.0), fotografía de Lewis Hine (Library of Congress, dominio público), catálogo de moda de 1890 (dominio público) y centralita de Salt Lake City, 1907 (dominio público). Cada leyenda enlaza su página de origen. Diagramas originales del curso (CC BY-NC-SA 4.0).

## Referencias

{% include references.html %}

## Nota editorial. Trabajo en progreso. Práctica de innovación docente
{: .lesson-editorial-note }

Las citas del PNUMA y de Couldry y Mejias están verificadas con la página impresa de la fuente. La escalera de la evidencia es un **marco operativo del curso**, no un resultado de investigación. Los casos se enseñan con sus fuentes primarias o periodísticas enlazadas; ninguna cifra de campaña se presenta como resultado independiente. Falta un estudio publicado sobre la enseñanza crítica de KPI en comunicación de moda. **En revisión:** los párrafos de desarrollo de cada idea de la masterclass se están redactando con el modelo local del curso y se incorporarán tras su revisión; mientras tanto, cada idea muestra su tesis, su caso y su cita.

## Autoría asistida por IA

Rubén Vega Balbás, PhD escribió esta lección con asistencia de IA bajo su control editorial: el primer borrador de cada idea de la masterclass se generó con un modelo local y se revisó y corrigió a mano. Declaración de uso de IA (alumnado y docencia): [guía de declaración de IA]({{ '/ai-declaration/' | relative_url }}).
