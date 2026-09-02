---
layout: methodology
title: 'Guía práctica de IA: El libro del prompt tejido'
title_en: 'AI Practical Guide: The Book of the Woven Prompt'
slug: ai-practical-guide
date: 2026-08-31
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /methodology/es/ai-practical-guide/
description: 'Un libro de sabiduría para la creatividad digital y de moda: usa la IA con intención, cuestiona sus espejos y haz visible la autoría.'
tags: [ia, metodologia, etica, moda, autoria, creacion-digital]
---

## 📜 Tabla de contenidos
{: .no_toc }

- TOC
{:toc}

<div class="ai-guide">

<figure class="ai-guide__hero" markdown="0">
<img src="/digital-creativity-uem/assets/images/ai-guide/book-of-the-woven-prompt-cv-index-20260831-v2.png" width="1600" height="900" alt="Un hilo rojo cruza el campo visual geométrico del índice de Creación Digital y pasa por una aguja, un círculo reflectante, un patrón de moda y una máquina parecida a un farol." fetchpriority="high" />
<figcaption>El índice principal de la asignatura se convierte en campo de cartel: el hilo cruza intención, sugerencia, reflexión y juicio.</figcaption>
</figure>

<p class="ai-guide__kicker">Un libro breve para preguntas grandes · Creación Digital · UEM</p>

<div class="ai-guide__orientation">
<p><strong>Para:</strong> estudiantes que crean imágenes, prendas, avatares, piezas audiovisuales, experiencias digitales o portfolios con IA cerca.</p>
<p><strong>No para:</strong> asesoramiento legal, promesas de neutralidad del modelo ni sustituto del aprendizaje del oficio que entregas.</p>
<p><strong>Propósito:</strong> usar la IA para ampliar una intención humana y dejar visible el hilo suficiente para que otra persona pueda comprender, preguntar y confiar en la obra.</p>
</div>

<blockquote class="ai-guide__ttod">
  <p>«La ingeniera de IA honesta no se miente sobre sus herramientas. Sabe qué pueden y qué no pueden hacer, y diseña su flujo para amplificar sus fortalezas.»</p>
  <cite>— The Tao of Development, <code>arch-037</code></cite>
</blockquote>

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROVENANCE_LINE: claim=guide.instructions.tested-comprehension; status=[BIBLIO-GAP]; discovery={service=studio-guide-forge; source=CPSC Manufacturer's Guide to Developing Consumer Product Instructions; proposed_use=audience-match-and-evaluate-the-instructions}; source={document_coat=studio-guides; extraction_db=ahmes-library/studio_guides/documents/manufacturers_guide_to_developing_consumer_product_instructions_cb1f154e/extract/extraction.db; node_id=82b3b541-0cf2-5f0a-adb9-7470db8f8a71; page_index=null}; resolver=surface-B-only; public_citation=OMITTED; supports=write-for-reader-and-test-comprehension; does_not_support=fashion-AI pedagogy
-->
{% endif %}

---

## Prólogo · Cómo leer este libro

Los proverbios son breves porque una herramienta puede producir una respuesta larga antes de que tú hayas formulado una pregunta clara. Lee uno, detente y realiza el pequeño acto que lo acompaña. El acto es la lección.

El estándar del estudio es la asistencia local mediante Ollama y el modelo instalado `qwen3.8:27b` cuando la tarea realmente se beneficia de la IA. Los modelos cambian; el pacto no: mantén el trabajo local cuando corresponda, declara la asistencia y cuestiona cada resultado.

### Los dos giros

1. **El giro de preguntar:** escribe tu intención, restricciones, referencias y aquello que quieres variar.
2. **El giro de juzgar:** compara el resultado con tu intención, rechaza los automatismos, rehace lo importante y registra qué cambió.

Si falta el segundo giro, la máquina no ha asistido a tu práctica: ha sustituido la parte que debías aprender.

---

## I · La mano antes del prompt

<blockquote class="ai-guide__aphorism"><p>La mano que nombra la pregunta sigue siendo la primera autora del viaje.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Antes de pedir una imagen, di qué debe hacer sentir, notar o comprender.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Una intención vaga invita a un extraño hermoso; una intención situada invita a un colaborador útil.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito de la primera puntada</strong></p>
<ol>
  <li>Escribe el brief con tus propias palabras.</li>
  <li>Nombra la audiencia, el material y la decisión que debe seguir siendo tuya.</li>
  <li>Solo entonces redacta el prompt; conserva la primera versión junto al resultado.</li>
</ol>
</div>

---

## II · El hilo de la intención

<blockquote class="ai-guide__aphorism"><p>Un prompt no es un hechizo: es un hilo entre la intención y el experimento.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Pide alternativas, no permiso para dejar de pensar.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>El primer resultado es una propuesta. La segunda mirada es donde comienza la autoría.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito de las tres variaciones</strong></p>
<ol>
  <li>Pide tres direcciones materialmente distintas, no tres adornos casi iguales.</li>
  <li>Para cada una, escribe: <em>¿qué revela y qué oculta?</em></li>
  <li>Conserva el camino descartado si te enseña algo sobre tu propio gusto.</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>La estudiante preguntó: «¿Qué imagen es mía?»</p>
  <p>La maestra respondió: «Enséñame la que rechazaste.»</p>
  <cite>Koan de la imagen descartada</cite>
</blockquote>

---

## III · El espejo que solo muestra una parte

<blockquote class="ai-guide__aphorism"><p>Cada cuerpo generado es también una lección sobre los cuerpos que el sistema no imaginó.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Un automatismo pulido sigue siendo una decisión; pregunta quién la tomó, quién gana y quién desaparece.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>No llames inclusiva a una imagen porque contiene diferencia; pregunta si la diferencia tiene agencia.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito de las cuatro preguntas</strong></p>
<ol>
  <li>¿Quién está representado?</li>
  <li>¿Quién falta o se vuelve imposible?</li>
  <li>¿Qué hábitos visuales repite el resultado?</li>
  <li>¿Qué vas a cambiar, contextualizar o rechazar?</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>El espejo mostró a la estudiante una modelo perfecta.</p>
  <p>«¿Perfecta para quién?», preguntó la maestra.</p>
  <p>El espejo se convirtió en una pregunta.</p>
  <cite>Koan de la superficie pulida</cite>
</blockquote>

{% if site.publication.publish_internal_metadata %}
<!-- curriculum-internal:
PROVENANCE_LINE: claim=guide.fashion-ai-ethics; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query=fashion AI human authorship identity cultural ethics; source_locator=grounding matrix II.5 and C1 fashion digital world; proposed_use=critical framing only}; source={document_coat=anwar_raza_marzouk_0598ec0e; extraction_db=ahmes-library/scholar/documents/anwar_raza_marzouk_generative_ai_in_studio_based_fashion_education_slr_ejbm_2025_0598ec0e/extract/extraction.db; node_id=c9a17328-72f7-56c8-95bf-b9860b1067b8; page_index=0}; resolver=ahmes query --cite extraction.db:c9a17328-72f7-56c8-95bf-b9860b1067b8 --style chicago-author-date; quote=knowledge construction, learner identity and authorship, teaching practice, studio culture and ethics; public_citation=(Anwar, Raza, and Marzouk 2025, 1); supports=ethical and authorship dimensions belong in studio AI instruction; does_not_support=universal image-bias measurement or a validated portfolio UX method
PROVENANCE_LINE: claim=guide.critical-mediated-world; status=[BIBLIO-GAP]; discovery={service=Athanor; project_slug=profield-stem-code-ai-epistemology-critique; knowledge_scope=field_prospection; query=digital mediated world ethics AI representation agency; proposed_use=question prompts only}; source={document_coat=multiple critical-AI candidates; node_id=none}; resolver=not promoted; public_citation=OMITTED; supports=critical questions about representation, expertise, and accountability; does_not_support=settled fashion-specific pedagogy
PROVENANCE_LINE: claim=guide.ethical-authorship; status=VERIFIED; discovery={service=Athanor; project_slug=profield-digital-creativity; knowledge_scope=field_prospection; query=fashion AI human authorship identity cultural ethics}; source={document_coat=anwar_raza_marzouk_0598ec0e; extraction_db=ahmes-library/scholar/documents/anwar_raza_marzouk_generative_ai_in_studio_based_fashion_education_slr_ejbm_2025_0598ec0e/extract/extraction.db; node_id=cd329fc8-be24-5335-ad0d-4fe91dd97693; page_index=8}; resolver=ahmes query --cite extraction.db:cd329fc8-be24-5335-ad0d-4fe91dd97693 --style chicago-author-date; public_citation=(Anwar, Raza, and Marzouk 2025, 9); supports=ethical authorship, copyright, ownership, hybrid authorship, and preserving student voice; does_not_support=legal advice or a universal rights determination
-->
{% endif %}

---

## IV · El registro de la autoría

<blockquote class="ai-guide__aphorism"><p>Si la máquina ofreció una posibilidad, tu registro debe nombrar la elección.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>La autoría no es una sensación de familiaridad: es poder explicar los movimientos decisivos.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Oculta el proceso y el acabado se vuelve máscara; muestra el proceso y la crítica se vuelve herramienta.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito del registro visible</strong></p>
<p>Para cada pieza asistida por IA, registra:</p>
<ul>
  <li><strong>Herramienta:</strong> el modelo o interfaz local utilizado.</li>
  <li><strong>Aportación:</strong> qué sugirió, transformó, organizó o generó.</li>
  <li><strong>Verificación humana:</strong> qué comprobaste, cambiaste, rechazaste y puedes defender.</li>
</ul>
</div>

<p>La investigación sobre educación de moda sitúa la identidad del alumnado, la autoría y la cultura de estudio junto a la construcción de conocimiento y la práctica docente; su propuesta incluye trabajar de forma explícita la autoría ética, el copyright, la propiedad y la autoría híbrida (Anwar, Raza, and Marzouk 2025, 1, 9). Por eso la declaración debe estar junto a la obra, no escondida en una nota.</p>

---

## V · El pequeño fuego local

<blockquote class="ai-guide__aphorism"><p>Un modelo local está más cerca de tu estudio, no más cerca de la verdad.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Mantén el material sensible fuera del prompt; la privacidad también compone.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Cuando la respuesta suene segura, haz más paciente la comprobación.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito del farol</strong></p>
<ol>
  <li>Prepara una entrada pequeña y limpia; retira nombres, rostros, secretos y materiales que no puedas compartir.</li>
  <li>Pide una tarea acotada: variaciones, preguntas, crítica o transformación.</li>
  <li>Inspecciona el resultado frente al brief y frente al mundo que pretende representar.</li>
  <li>Guarda prompt, resultado útil y edición humana que lo convirtió en tuyo.</li>
</ol>
</div>

<blockquote class="ai-guide__koan">
  <p>«El modelo me ha dado la respuesta», dijo la estudiante.</p>
  <p>«Bien», respondió la maestra. «Ahora pregúntale qué haría falsa esa respuesta.»</p>
  <cite>Koan de la segunda pregunta</cite>
</blockquote>

<p class="ai-guide__note"><strong>Recuerda:</strong> la asistencia de IA puede acelerar una búsqueda o ensanchar un boceto, pero no puede hacer tu observación, tu juicio ético ni tu responsabilidad sobre la imagen final.</p>

<p>La literatura de estudio describe tanto una mayor capacidad de ideación y eficiencia como tensiones en torno a la originalidad, el uso ético y el acceso equitativo; por eso el flujo prudente mantiene acotada la herramienta y visible el juicio (Anwar, Raza, and Marzouk 2025, 10).</p>

---

## VI · El portfolio como testigo

<blockquote class="ai-guide__aphorism"><p>Un portfolio no es una sala donde posan las cosas terminadas: es un camino que otra persona puede recorrer.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Coloca el brief, el giro, el fallo y la decisión junto a la superficie pulida.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>El buen caso no dice «mira lo que hizo la herramienta»; dice «mira por qué elegí esto».</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito de los cuatro testigos</strong></p>
<ol>
  <li><strong>Intención:</strong> ¿qué pregunta o brief inició la pieza?</li>
  <li><strong>Rastro:</strong> ¿qué referencias, prompts, archivos e iteraciones la formaron?</li>
  <li><strong>Juicio:</strong> ¿qué alternativas rechazaste y por qué?</li>
  <li><strong>Declaración:</strong> ¿dónde ayudó la IA y dónde siguió siendo decisiva la autoría humana?</li>
</ol>
</div>

<p>Un laboratorio experimental de diseño de moda describe el trabajo humano–IA como una colaboración cuya dinámica debe analizarse a través del proceso de diseño, no deducirse solo del resultado final (Rizzi and Bertola 2025, 10). Tu portfolio vuelve legible ese proceso.</p>

---

## VII · La puerta del cuidado

<blockquote class="ai-guide__aphorism"><p>No tomes prestados un rostro, un cuerpo, una prenda o una historia solo porque una máquina hizo fácil tomarlos.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Pregunta por el consentimiento antes de circular; pregunta por la atribución antes de exhibir.</p><cite>Proverbio</cite></blockquote>
<blockquote class="ai-guide__aphorism"><p>Una imagen accesible lleva su significado más allá del ojo que la imaginó primero.</p><cite>Proverbio</cite></blockquote>

<div class="ai-guide__rite">
<p><strong>Rito antes de publicar</strong></p>
<ul>
  <li>Usa material propio, licenciado o claramente permitido.</li>
  <li>No generes ni publiques la imagen identificable de una persona sin permiso.</li>
  <li>Escribe texto alternativo con propósito; marca como decorativas las imágenes decorativas.</li>
  <li>Acredita referencias, colaboraciones y materiales de origen.</li>
  <li>Conserva un antes/después o rastro de proceso cuando la transformación cambie el significado.</li>
  <li>No recojas ni exhibas el trabajo de otra persona sin el proceso de consentimiento requerido.</li>
</ul>
</div>

---

## Epílogo · La declaración en la puerta

Escribe esto junto a la obra terminada, con palabras sencillas:

> **Declaración de uso de IA**
>
> **Herramienta:** [herramienta/modelo local]
>
> **Aportación:** [qué sugirió, generó, transformó u organizó]
>
> **Decisiones humanas:** [qué seleccioné, cambié, rechacé, verifiqué y asumo]

<blockquote class="ai-guide__ttod">
  <p>«Usa las imágenes para reforzar el mensaje, no para ser el mensaje. Las palabras permanecen cuando fallan las imágenes.»</p>
  <cite>— The Tao of Development, <code>img-053</code></cite>
</blockquote>

Lo mismo vale para la IA: deja que refuerce la práctica, no que se convierta en la práctica. Si puedes mostrar el hilo, nombrar las elecciones y defender el cuidado, la obra conserva un centro humano.

<p class="ai-guide__signature"><em>Forjado para el estudio de Creación Digital · Edición 2026-08-31 · Autoría humana, asistencia local, declaración abierta.</em></p>

## Referencias

- Anwar, Rabia, Fahd Ali Raza, and Mostafa El-Sayed Marzouk. 2025. “Generative AI in Studio-Based Fashion Education: A Systematic Literature Review.” <em>Electronic Journal of Business and Management</em> 10 (4): 17–28. <a href="https://doi.org/10.65136/ejbm.v10i4.24">https://doi.org/10.65136/ejbm.v10i4.24</a>.
- Rizzi, Greta, and Paola Bertola. 2025. “Exploring the Generative AI Potential in the Fashion Design Process: An Experimental Experience on the Collaboration between Fashion Design Practitioners and Generative AI Tools.” <em>European Journal of Cultural Management and Policy</em> 15: 13875. <a href="https://doi.org/10.3389/ejcmp.2025.13875">https://doi.org/10.3389/ejcmp.2025.13875</a>.

</div>

<style>
.ai-guide { --ink: #172033; --muted: #5d6674; --paper: #f8f4eb; --gold: #b88746; --red: #a83d2d; --night: #0b1622; max-width: 980px; margin: 0 auto; }
.ai-guide__hero { margin: 0 0 2rem; background: var(--night); border: 1px solid rgba(184, 135, 70, .45); box-shadow: 0 18px 50px rgba(11, 22, 34, .18); }
.ai-guide__hero img { display: block; width: 100%; height: auto; }
.ai-guide__hero figcaption { margin: 0; padding: .8rem 1rem 1rem; color: #e8dcc6; font: 500 .88rem/1.45 Georgia, serif; }
.ai-guide__kicker { color: var(--red); font: 700 .75rem/1.2 ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .14em; text-transform: uppercase; }
.ai-guide__orientation { padding: 1rem 1.2rem; border: 1px solid rgba(184, 135, 70, .55); background: linear-gradient(120deg, rgba(184, 135, 70, .1), rgba(168, 61, 45, .06)); }
.ai-guide__orientation p { margin: .35rem 0; }
.ai-guide__ttod, .ai-guide__koan { border-left: 4px solid var(--gold); padding: 1rem 1.2rem; background: rgba(184, 135, 70, .08); }
.ai-guide__ttod p, .ai-guide__koan p { margin: .2rem 0; }
.ai-guide__ttod cite, .ai-guide__koan cite { display: block; margin-top: .7rem; color: var(--muted); font-size: .82rem; }
.ai-guide__aphorism { margin: 1.7rem 0; padding: 1rem 1.2rem; border-left: 2px solid var(--red); background: rgba(168, 61, 45, .055); }
.ai-guide__aphorism p { margin: 0; color: var(--ink); font: 600 clamp(1.15rem, 2.2vw, 1.5rem)/1.35 Georgia, serif; }
.ai-guide__aphorism cite { display: block; margin-top: .45rem; color: var(--muted); font-size: .78rem; font-style: normal; text-transform: uppercase; letter-spacing: .08em; }
.ai-guide__rite { margin: 1.5rem 0 2rem; padding: 1rem 1.25rem; border: 1px solid rgba(23, 32, 51, .2); background: rgba(23, 32, 51, .04); }
.ai-guide__rite p:first-child { margin-top: 0; color: var(--red); }
.ai-guide__rite p:last-child, .ai-guide__rite ol:last-child, .ai-guide__rite ul:last-child { margin-bottom: 0; }
.ai-guide__note { padding: 1rem 1.2rem; background: #fff4d8; border: 1px solid #e5c27c; }
.ai-guide__signature { margin: 2rem 0 0; color: var(--muted); font-size: .9rem; }
@media (prefers-color-scheme: dark) {
  .ai-guide__orientation, .ai-guide__aphorism, .ai-guide__rite { color: #e7e1d7; }
  .ai-guide__aphorism p { color: #f4ead9; }
  .ai-guide__rite { border-color: rgba(232, 220, 198, .25); background: rgba(232, 220, 198, .06); }
  .ai-guide__note { color: #3b2d14; }
}
</style>
