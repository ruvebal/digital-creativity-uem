---
layout: lesson
title: 'II.2 · Creación de avatares'
title_en: 'II.2 · Avatar Creation'
slug: ii-2-avatares
date: 2026-08-20
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/creacion-digital-ii/ii-2-avatares/
description: 'Un avatar es una afirmación de identidad, no un maniquí neutro — decidir qué representa es la habilidad evaluada, no la herramienta de modelado.'
status: scaffold
tags: [creacion-digital-ii, avatares, identidad, representacion, ia-generativa-taller]
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{: .no_toc }
- TOC
{:toc}

<!-- prettier-ignore-end -->

---

> _"En un bosque, cada árbol debe ser él mismo. La reutilización es sabiduría, pero la identidad es sagrada."_
> — Tao of Development, `arch-017`
{: .tao-development-quote }

> **Declaración de asistencia de IA:** los avatares pueden modelarse a mano, generarse con IA, o ser un híbrido. Cada pieza de avatar lleva una nota de intención de identidad y, cuando se usó un generador, una declaración de uso de IA — la misma disciplina que las piezas de portfolio de II.5.

---

{% include lesson-semantic-graphic.html %}

## Dónde se sitúa — CONTENIDOS y competencias

**Anclaje CONTENIDOS (verbatim, guía oficial):** *Creación de avatares.*

**Competencias que sirve (`3-creacion-digital-ii.json`):** `CON1` (diferenciar las técnicas de representación audiovisual y sus medios de difusión), `HAB1` (representar gráficamente ideas de moda), `COMP8` (manejar herramientas digitales de representación gráfica o audiovisual en la comunicación de moda), `COMP9` (crear ideas nuevas a partir de conceptos conocidos, resolviendo problemas de forma original).

**Resultados de aprendizaje que sirve esta unidad** (verbatim del `learning_outcomes`): *"Aplicar herramientas informáticas avanzadas en la creación y la representación digital de creaciones de moda."* · *"Diseñar estrategias creativas de comunicación digital en empresas de moda."*

**Pesos de evaluación a los que alimenta la evidencia de esta unidad** (CD II presencial, framework §6): **Investigaciones y proyectos 20%** puntúa la pieza de avatar; la nota de intención de identidad puede alimentar **Cuaderno de prácticas de laboratorio/taller 10%**.

---

## 🎯 Objetivos de aprendizaje

Al final de esta unidad podrás:

- **Construir una pieza de avatar** — modelada a mano, asistida por IA, o híbrida — con un estándar de oficio profesional.
- **Escribir una nota de intención de identidad** — qué tipo de cuerpo, tono de piel y decisiones de estilismo se tomaron, y por qué.
- **Declarar el uso de IA con honestidad** cuando un generador formó parte del proceso.
- **Distinguir creación de avatar de VTON** — el avatar de esta unidad representa una identidad, no una prueba virtual de ajuste de prenda.
- **Conectar decisiones de avatar con investigación adyacente sobre autoría y encarnación** — la enseñanza de autoría híbrida puede reforzar la voz del estudiante cuando los límites de autoría son explícitos (Anwar 2025, 1); la personalización en primera frente a tercera persona puede cambiar la experiencia de encarnación (Gonzalez-Franco et al. 2024, 12).

---

## Por qué existe esta unidad: un avatar es primero una afirmación de identidad

**Afirmación:** un avatar es una afirmación de identidad, no un maniquí neutro. Cada valor por defecto que el estudiante *no* elige deliberadamente — tipo de cuerpo, tono de piel, proporciones — sigue siendo una elección, hecha por los valores por defecto de la herramienta en lugar de por el estudiante.

Un hallazgo acotado de la revisión sistemática de Anwar, Raza y Marzouk sirve como **guardarraíl adyacente**, no como evidencia de un método de avatar: los autores recomiendan que la enseñanza haga explícitos los límites de autoría, copyright y propiedad mediante talleres de autoría híbrida y crítica. La traducción concreta al taller es esta: cada avatar conserva una nota de intención de identidad, una declaración de herramientas/materiales y un punto de decisión humana verificable. La revisión **no** establece qué flujo de avatar ni qué secuencia de evaluación funciona mejor (Anwar 2025, 1).

Un experimento de realidad virtual ofrece un segundo anclaje, deliberadamente estrecho: la personalización del avatar desde una perspectiva en primera persona se comparó con una configuración en tercera persona. En ese estudio, la condición en tercera persona redujo la experiencia de encarnación del avatar de mayor tamaño, mientras que la condición en primera persona no mostró esa reducción. Para el taller, esto convierte la perspectiva de edición y la representación corporal en decisiones que deben justificarse; **no** demuestra que una secuencia concreta enseñe mejor a modelar avatares ni autoriza a generalizar desde una muestra pequeña (Gonzalez-Franco et al. 2024, 12).

**Qué apoya esto, y qué no.** Anwar (2025) apoya hacer explícitos los límites de autoría, copyright y propiedad en la enseñanza de taller. Gonzalez-Franco et al. (2024) apoya tratar la perspectiva de edición y la representación corporal como decisiones a justificar. **Ninguna fuente revisada valida una secuencia de enseñanza del modelado de avatares** para HE; la documentación de herramientas fundamenta operaciones solo — etiqueta `[PLATFORM]`, nunca investigación.

**El VTON/prueba virtual queda explícitamente fuera de alcance.** El avatar de esta unidad existe para representar un cuerpo/identidad; no simula una prueba de ajuste de prenda sobre ese cuerpo.

**Ancla de práctica (perspectiva de campo):** cuerpo paramétrico o malla, asignación de piel/material, pose, cámara y acoplamiento de prenda como clases de operación duraderas — separadas de la interfaz o la biblioteca de presets de cualquier aplicación de avatar.

**Señal de frontera (perspectiva de campo):** los pipelines generativos de avatar y las herramientas asistidas por IA pueden acelerar la producción más rápido que la validación pedagógica; trata cualquier cuerpo generado como entrada al juicio de identidad, no como prueba de que una nota de intención es honesta o completa.

## Perspectiva crítica

Las bibliotecas de avatares no son representaciones neutrales del cuerpo: las categorías, tonos de piel y rasgos disponibles condicionan qué identidades pueden reconocerse y estudiarse en entornos virtuales (mapa de campo C2, hallazgo establecido).

Los sistemas contemporáneos de generación y clasificación visual pueden reproducir desigualdades interseccionales de género y racialización, por lo que las herramientas empleadas para producir imágenes de moda no deben tratarse como infraestructuras representacionales neutrales (AlDahoul, Rahwan y Zaki 2025).

### La pregunta de debate

¿Debería un avatar de estudiante declarar que no es una fotografía del estudiante? ¿Cambia esa respuesta si el avatar se generó con IA frente a si se modeló a mano?

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.video.avatar-breakdown" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador abstracto para demostración de desglose de diseño de avatar; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> un desglose breve pausa antes de cada decisión de identidad para que el alumnado etiquete cuerpo, pose, prenda y punto de vista.</p>
<p><strong>Qué observar:</strong> preset por defecto, anulación deliberada, efecto representacional y qué cierra cada paso.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.still.identity-exemplar" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador para ejemplo respetuoso de avatar y contraejemplo de estereotipo; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> imágenes en paralelo prueban legibilidad, contención y qué permanece legible tras la configuración de identidad.</p>
<p><strong>Qué observar:</strong> elección de identidad autorizada frente a valor por defecto no examinado.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

<figure class="lesson-media lesson-media--placeholder" data-media-slot="II.2.graphic.component-map" markdown="0">
<img src="{{ '/assets/images/lesson-covers/dc-ii-02-avatar-identity-semantic.svg' | relative_url }}" width="1600" height="560" alt="Marcador de diagrama para cadena identidad-cuerpo-pose-prenda-cámara-procedencia; no representa personas ni prendas." loading="lazy" />
<figcaption>
<p><strong>Por qué está aquí:</strong> mapea ficción de identidad → cuerpo → pose → prenda → cámara → declaración de autoría.</p>
<p><strong>Qué observar:</strong> dónde un valor por defecto podría sustituirse por una decisión de identidad deliberada.</p>
<p class="media-note">Marcador visual — medios con licencia pendientes de revisión.</p>
</figcaption>
</figure>

---

## B1 · Conceptual — magistral 2 h + seminarios 3 h + debates 1 h

Cubierto arriba: marco Anwar/Gonzalez-Franco, perspectiva crítica, debate y marcadores. Cubre la técnica de creación de avatares (la herramienta que use el taller) como oficio, y empareja cada técnica con la pregunta de identidad que plantea: *si acepto este valor por defecto, ¿qué identidad estoy afirmando que no elegí?* Realiza la pregunta de debate de arriba antes de cualquier trabajo práctico. Deja explícito: se evalúa la *decisión de identidad*, no qué herramienta produjo la malla.

---

## B2 · Taller — talleres 2 h + investigaciones y proyectos 3 h (contextualizado, tipo entorno laboral)

**Entregable:** una pieza de avatar con una **nota de intención de identidad** escrita (tipo de cuerpo, tono de piel, decisiones de estilismo — qué y por qué) y una declaración de uso de IA si se usó un generador ("ninguna" es válida).

**Definición de terminado:**
- La pieza existe; nota de intención de identidad presente y específica (no un genérico "hecho en [herramienta]").
- ID de pieza asignado; carpeta de proceso conservada aunque no se publique.

**Si quieres que esta pieza se exhiba públicamente** (vShowroom), adjunta ahora la lista de verificación de consentimiento **sin firmar** de abajo a la carpeta de proceso. Rellenarla no es firmarla — todavía no existe aprobación del DPO.

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
**Evidencia:** Investigaciones y proyectos 20% (pieza de avatar); Cuaderno 10% (nota de intención de identidad). S1/S2 opcionales para exhibición en vShowroom — adjuntar borradores sin firmar únicamente; no es un instrumento de consentimiento activo.
Las referencias a herramientas (cualquier software de 3D/avatar) son notas de plataforma fechadas, no citas de investigación — comprueba las versiones antes de clase.
-->
{% endif %}

---

## B3 · Resolución de problemas — 1 h · individual, descontextualizado

1. **Diagnóstico.** Dado un brief de generación de avatar donde cada rasgo personalizable por defecto va a un único tipo de cuerpo estrecho, indica el problema representacional y cómo lo corregirías.
2. Escribe la nota de intención de identidad (tipo de cuerpo, tono de piel, estilismo, y por qué) para un concepto de avatar descrito — sin usar ningún generador.
3. **Sin IA, declarado:** en dos frases, explica por qué el avatar de esta unidad no es una simulación de VTON/prueba virtual.

Los bocetos de respuesta del profesor no se publican en esta página — se conservan en notas privadas del instructor.

{% comment %}
outcome-graphic-selection:
  source-section: "B3 · Resolución de problemas"
  visual-grammar: "identity-parameters — un valor por defecto estrecho se ramifica en configuraciones de identidad con igual peso"
{% endcomment %}
{% include lesson-outcome-graphic.html %}

---

## Referencias

- AlDahoul, Nouar, Talal Rahwan y Yasir Zaki. 2025. "AI-generated faces influence gender stereotypes and racial homogenization." *Scientific Reports* 15: 14449. <a href="https://doi.org/10.1038/s41598-025-99623-3" target="_blank" rel="noopener noreferrer">https://doi.org/10.1038/s41598-025-99623-3</a>.
- Anwar, S., A. Raza y R. Marzouk. 2025. "Generative AI in Studio-Based Fashion Education: A Systematic Literature Review." *European Journal of Business and Management*. <a href="https://doi.org/10.65136/ejbm.v10i4.24" target="_blank" rel="noopener noreferrer">https://doi.org/10.65136/ejbm.v10i4.24</a>.
- Gonzalez-Franco, M., A. Steed, C. C. Berger y A. Tajadura-Jiménez. 2024. "The Impact of First-Person Avatar Customization on Embodiment in Immersive Virtual Reality." *Frontiers in Virtual Reality* 5: 1436752. <a href="https://doi.org/10.3389/frvir.2024.1436752" target="_blank" rel="noopener noreferrer">https://doi.org/10.3389/frvir.2024.1436752</a>.

**Vacío declarado — en claro.** Anwar (2025) y Gonzalez-Franco et al. (2024) apoyan guardarraíles de autoría y perspectiva de encarnación respectivamente; **no** prueban que la secuencia de avatar, la rúbrica de intención de identidad o el entregable de este aula enseñen mejor la creación de avatares que una alternativa. Ninguna fuente revisada valida un método de modelado de avatar para educación de moda. La investigación sobre antropomorfismo en contextos de IA y moda puede informar por qué importan las afirmaciones de identidad, pero esa literatura permanece fuera de la bibliografía verificada de esta unidad. El VTON o prueba virtual queda fuera del alcance de esta unidad y no se aborda, por diseño.

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROFIELD_ROUTING: unit=II.2; temario=T2-avatars-experiences.pass1.resultant.mdc § avatars; subfield_runs=digital-creativity/03-temario-critica/C2-fashion-virtuality.pass1.resultant.mdc
CRITICAL_ROUTING: unit=II.2; critica=C2 avatar libraries L17; C3 gender/race generation L17; session identity-agency prompt
PROVENANCE_LINE: claim=II.2.claim.hybrid-authorship-guardrail; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="hybrid authorship workshops critique GenAI fashion education Anwar"; source_locator=T2-avatars-experiences.pass1.resultant.mdc § Anwar; similarity=null; proposed_use="adjacent guardrail"}; source={document_coat=ejbm_v10i4_24; extraction_db=ahmes-library/scholar/documents/generative_ai_in_studio_based_fashion_education_a_systematic_literature_review_ejbm_v10i4_24/extract/extraction.db; node_id=cd329fc8-be24-5335-ad0d-4fe91dd97693; page_index=0; printed_page=1}; resolver="ahmes query --cite extraction.db:cd329fc8-be24-5335-ad0d-4fe91dd97693 --require-evaluator-safe evaluator_safe=yes"; quote="authorship, copyright, and ownership limits explicit through hybrid-authorship workshops and critique"; public_citation="(Anwar 2025, 1)"; supports="explicit authorship/copyright/ownership instruction in studio"; does_not_support="avatar modelling method or assessment sequence"
PROVENANCE_LINE: claim=II.2.claim.embodiment-perspective; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="first-person third-person avatar customization embodiment Gonzalez-Franco"; source_locator=T2-avatars-experiences.pass1.resultant.mdc § Gonzalez-Franco; similarity=null; proposed_use="perspective ethics anchor"}; source={document_coat=10_3389_frvir_2024_1436752; extraction_db=ahmes-library/scholar/documents/the_impact_of_first_person_avatar_customization_on_embodiment_in_immersive_virtual_reality_10_3389_frvir_2024_1436752/extract/extraction.db; node_id=c17b40cf-11e0-57d4-86c2-eefca69448c0; page_index=11; printed_page=12}; resolver="ahmes query --cite extraction.db:c17b40cf-11e0-57d4-86c2-eefca69448c0 --require-evaluator-safe evaluator_safe=yes"; quote="third-person condition reduced embodiment of the larger avatar"; public_citation="(Gonzalez-Franco et al. 2024, 12)"; supports="editing perspective affects embodiment experience"; does_not_support="avatar modelling teaching sequence or fashion-education assessment"
PROVENANCE_LINE: claim=II.2.gap.avatar-modelling-sequence; status=NONE; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="validated avatar modelling teaching sequence fashion HE"; source_locator=T2-avatars-experiences.pass1.resultant.mdc; similarity=null; proposed_use="honest gap retained"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports=none; does_not_support="validated avatar-modelling method for fashion students"
PROVENANCE_LINE: claim=II.2.critical.avatar-libraries; status=NONE; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="bibliotecas avatares no representaciones neutrales cuerpo"; source_locator=C2-fashion-virtuality.pass1.resultant.mdc L17; similarity=null; proposed_use="critical established"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote="Las bibliotecas de avatares no son representaciones neutrales del cuerpo"; public_citation=OMITTED; supports="avatar libraries condition recognisable identities"; does_not_support="mandatory VALID library assignment"
PROVENANCE_LINE: claim=II.2.critical.generation-bias; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=digital-creativity/03-temario-critica; knowledge_scope=field_prospection; query="generacion clasificacion visual desigualdades genero racializacion Stable Diffusion"; source_locator=C3-gender-minorities-silences.pass1.resultant.mdc L17; similarity=null; proposed_use="critical technical"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; ahmes_attempt=DOI 10.1038/s41598-025-99623-3 not in scholar vault; quote=none; public_citation="(AlDahoul, Rahwan, and Zaki 2025)"; supports="generation systems reproduce gender and racial inequalities"; does_not_support="which avatar tool students must use"
PROVENANCE_LINE: claim=II.2.critical.anthropomorphism; status=[BIBLIO-GAP]; discovery={service=profield; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="antropomorfismo IA moda Rodriguez-Borlado"; source_locator=grounding matrix II.2; similarity=null; proposed_use="adjacent mechanism naming"}; source={document_coat=rodriguez_borlado_perez_curiel_universitas_ia_moda_2024_f711009d; extraction_db=ahmes-library/scholar/documents/rodriguez_borlado_perez_curiel_universitas_ia_moda_2024_f711009d/extract/extraction.db; node_id=b6b4d953-b4af-596c-affe-0bc4a44aae9a; page_index=3; printed_page=4}; resolver=OMITTED; ahmes_attempt=evaluator_safe=no host registry mismatch; quote=none; public_citation=OMITTED; supports="anthropomorphism mechanism worth naming to students"; does_not_support="avatar modelling method or CV bibliography entry"
PROVENANCE_LINE: claim=II.2.critical.identity-agency-prompt; status=NONE; discovery={service=session-prompt; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query="avatar agency identity defaults"; source_locator=ii-2-avatars.md § Critical field lens; similarity=null; proposed_use="living prompt"}; source={document_coat=none; extraction_db=none; node_id=none; page_index=null; printed_page=null}; resolver=OMITTED; quote=none; public_citation=OMITTED; supports="naming identity agency as studio question"; does_not_support="empirical claim about cohort norms"
MEDIA_RIGHTS_LINE: slot=II.2.video.avatar-breakdown; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.2.still.identity-exemplar; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
MEDIA_RIGHTS_LINE: slot=II.2.graphic.component-map; status=PENDING; licence=none; canonical_source=none; swap_phase=MP5
-->
{% endif %}

---

## Nota editorial. Trabajo en curso. Práctica de Innovación docente
{: .lesson-editorial-note }

Esta nota forma parte de una *Práctica de Innovación docente* en curso — los límites epistémicos van aquí, no entre párrafos de Masterclass.

---

## Autoría asistida por IA

Rubén Vega Balbás, PhD (`ruvebal@crea-comm.net`) escribió esta lección en el
entorno de estudio crea-comm.net — un harness agentic local con recuperación
vía MCP, contexto RAG del vault curricular y un modelo de voz académica
afinado sobre su propia escritura. La forja consultó **3** fuentes del vault;
cada `(Autor, Año)` público se comprobó contra ese vault antes de aceptarlo.
Prompts, borradores del modelo y enmiendas humanas se archivan para evaluación
posterior. El juicio editorial y la responsabilidad del texto final permanecen
en el autor.

Declaración de uso de IA (alumnado y docencia): [/digital-creativity-uem/ai-declaration/]({{ '/ai-declaration/' | relative_url }}).

*Fecha de forja: 2026-09-22 · Studio: crea-comm.net · harness: `lesson-scribe` v0.1 · prompt-v2.1*


{% if site.publication.publish_internal_metadata %}
<!-- lesson_uuid: 7b7b491c-6093-4df4-a2b0-0b8c8f989b68
     vault_refs_consulted: 3
     forge_pass: editorial-ai-footer-law-2026-09-22
-->
{% endif %}
