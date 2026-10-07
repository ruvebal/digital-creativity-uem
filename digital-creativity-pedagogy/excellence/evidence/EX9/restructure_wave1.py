#!/usr/bin/env python3
"""EX9 Wave-1 lesson structural pass — heading spine only; does not invent citations."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LESSONS = ROOT / "docs" / "lessons"

# Session timing first lines for Workshop (forge SESSION-RHYTHM).
WORKSHOP_FIRST = {
    "i-1": "No Workshop in sessions 1–2: first lessons end after Lab.",
    "i-2": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-3": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-4": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-5": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-6": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-7": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-8": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
    "i-9": "From session 4: Workshop is protected studio time for D2 Transposition and D3 final event (≈ half / half) — not D1 Analysis clock.",
}
WORKSHOP_FIRST_ES = {
    "i-1": "Sin Workshop en las sesiones 1–2: las primeras lecciones terminan tras el Lab.",
    "default": "Desde la sesión 4: el Workshop es tiempo de estudio protegido para D2 Transposición y D3 evento final (≈ mitad / mitad) — no es reloj de D1 Análisis.",
}

TAO_EN = """## Tao of the Image {{#tao-of-the-image}}

Unit epigraph (studio Tao register — not a scholarly quotation):

{epigraph}

Deck and lesson links that target `#tao-of-the-image` resolve here.
"""

TAO_ES = """## Tao de la imagen {{#tao-of-the-image}}

Epígrafe de la unidad (registro Tao de estudio — no es cita académica):

{epigraph}

Los enlaces del deck y de la lección a `#tao-of-the-image` resuelven aquí.
"""

CONCLUSION_EN = """## Conclusion

This unit leaves named gaps on purpose: what the vault can page-verify stays in References; what remains open stays in the Editorial note. Keep Lab traces honest in the portfolio index. Do not invent a graded deliverable that How to Pass does not ask for. The next stake is the session rhythm already named — Analysis defence (D1) from session 3, Workshop from session 4 for Transposition and the final event.
"""

CONCLUSION_ES = """## Conclusión

Esta unidad deja lagunas nombradas a propósito: lo que el vault puede verificar con página queda en Referencias; lo abierto queda en la Nota editorial. Mantén las trazas de Lab honestas en el índice de portfolio. No inventes un entregable evaluable que How to Pass no pide. La siguiente apuesta es el ritmo de sesión ya nombrado — defensa de Análisis (D1) desde la sesión 3; Workshop desde la sesión 4 para Transposición y el evento final.
"""

PLACEHOLDER_LAB_EN = """## Lab (Portfolio)

*Structural placeholder (EX9) — no DCI deck `lab_exercise` slides yet for this unit. Two illustrative exercises keep the Lab rhythm; replace when EX11 / deck wave lands.*

### Exercise 1 — Name the CONTENIDOS move {#lab-exercise-1}

**Time:** 15 minutes.

**Group:** alone.

**Materials:** notebook or laptop; timer; one rights-clear reference image for this unit's CONTENIDOS.

**Steps:**

1. Restate the unit CONTENIDOS anchor in one sentence (no tool brand).
2. Name one craft decision this unit asks you to leave visible in a process note.
3. Write one sentence on what a single-tool workflow would hide.
4. Keep the note for the portfolio index.

**Portfolio trace:** CONTENIDOS sentence + craft-visibility sentence + single-tool caution.

**Judged by:** [Portfolio rubric — process evidence]({{{{ '/assignments/en/digital-creativity-portfolio/' | relative_url }}}}#rubric)

**Source:** Classroom adaptation (deck Labs pending — structural placeholder).

**Example trace:** *(Illustrative · not student work.)* CONTENIDOS: “Volume by hybrid iteration.” Craft left visible: physical maquette fold vs CLO pass. Caution: a CLO-only export would hide the drape correction the hand pass forced.

### Exercise 2 — One process evidence pair {#lab-exercise-2}

**Time:** 20 minutes.

**Group:** alone; optional 2-minute peer share.

**Materials:** the Exercise 1 note; one before/after or physical/digital pair; timer.

**Steps:**

1. Capture one before and one after (or physical vs digital) for the same piece.
2. Write one sentence naming what the second pass revealed that the first did not.
3. Reject any polish that erases the evidence of the pass.
4. File both stills (or photos) under the piece ID.

**Portfolio trace:** before/after pair + revelation sentence.

**Judged by:** [Portfolio rubric — process evidence]({{{{ '/assignments/en/digital-creativity-portfolio/' | relative_url }}}}#rubric)

**Source:** Classroom adaptation (deck Labs pending — structural placeholder).

**Example trace:** *(Illustrative · not student work.)* Before: paper maquette crease at waist. After: digital pass exaggerates the crease. Sentence: “The screen invented tension the cloth did not have — keep the physical photo in the index.”

{{% if site.publication.publish_internal_metadata %}}
<!-- curriculum-internal:
LAB_LINE: exercise=1; method_id=placeholder-contenidos-move; practises=pending-deck; source=EX9 structural placeholder; ACT=none
LAB_LINE: exercise=2; method_id=placeholder-process-pair; practises=pending-deck; source=EX9 structural placeholder; ACT=none
-->
{{% endif %}}
"""

PLACEHOLDER_LAB_ES = """## Lab (Portfolio)

*Marcador estructural (EX9) — aún no hay slides `lab_exercise` de deck DCI para esta unidad. Dos ejercicios ilustrativos mantienen el ritmo de Lab; se sustituyen cuando llegue la ola de decks.*

### Ejercicio 1 — Nombra el movimiento de CONTENIDOS {#lab-exercise-1}

**Time:** 15 minutes.

**Group:** individual.

**Materials:** cuaderno o portátil; temporizador; una imagen de referencia con derechos claros para el CONTENIDOS de esta unidad.

**Steps:**

1. Reformula el ancla de CONTENIDOS en una frase (sin marca de herramienta).
2. Nombra una decisión de oficio que esta unidad pide dejar visible en la nota de proceso.
3. Escribe una frase sobre lo que ocultaría un flujo de una sola herramienta.
4. Guarda la nota para el índice de portfolio.

**Portfolio trace:** frase CONTENIDOS + frase de visibilidad de oficio + cautela mono-herramienta.

**Judged by:** [Rúbrica de portfolio — evidencia de proceso]({{{{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}}}#rubric)

**Source:** Adaptación de aula (Labs de deck pendientes — marcador estructural).

**Example trace:** *(Ilustrativo · no es trabajo de estudiante.)* CONTENIDOS: «Volumen por iteración híbrida.» Oficio visible: pliegue de maqueta física vs pase CLO. Cautela: un export solo CLO ocultaría la corrección de drapeo que forzó la mano.

### Ejercicio 2 — Un par de evidencia de proceso {#lab-exercise-2}

**Time:** 20 minutes.

**Group:** individual; compartir opcional 2 minutos.

**Materials:** la nota del Ejercicio 1; un par antes/después o físico/digital; temporizador.

**Steps:**

1. Captura un antes y un después (o físico vs digital) de la misma pieza.
2. Escribe una frase nombrando lo que el segundo pase reveló que el primero no.
3. Rechaza cualquier pulido que borre la evidencia del pase.
4. Archiva ambas imágenes bajo el ID de pieza.

**Portfolio trace:** par antes/después + frase de revelación.

**Judged by:** [Rúbrica de portfolio — evidencia de proceso]({{{{ '/assignments/es/digital-creativity-portfolio/' | relative_url }}}}#rubric)

**Source:** Adaptación de aula (Labs de deck pendientes — marcador estructural).

**Example trace:** *(Ilustrativo · no es trabajo de estudiante.)* Antes: pliegue de maqueta en papel en la cintura. Después: el pase digital exagera el pliegue. Frase: «La pantalla inventó una tensión que la tela no tenía — conserva la foto física en el índice.»

{{% if site.publication.publish_internal_metadata %}}
<!-- curriculum-internal:
LAB_LINE: exercise=1; method_id=placeholder-contenidos-move; practises=pending-deck; source=EX9 structural placeholder; ACT=none
LAB_LINE: exercise=2; method_id=placeholder-process-pair; practises=pending-deck; source=EX9 structural placeholder; ACT=none
-->
{{% endif %}}
"""


def unit_key(slug: str) -> str:
    m = re.match(r"i-(\d+)", slug)
    return f"i-{m.group(1)}" if m else slug


def extract_epigraph(text: str) -> str:
    m = re.search(r"(^> _.+?$\n(?:^>.*$\n)*)", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"(^> \".+?\"$\n(?:^>.*$\n)*)", text, re.M)
    return m.group(1).strip() if m else "> _(Unit Tao line — see lesson epigraph.)_\n{: .tao-development-quote }"


def ensure_tao(text: str, lang: str) -> str:
    if re.search(r'id="tao-of-the-image"|\{#tao-of-the-image\}', text):
        return text
    epigraph = extract_epigraph(text)
    block = (TAO_EN if lang == "en" else TAO_ES).format(epigraph=epigraph)
    # Insert before References / Referencias
    return re.sub(
        r"(^## (?:References|Referencias)\b)",
        block + "\n---\n\n\\1",
        text,
        count=1,
        flags=re.M,
    )


def ensure_conclusion(text: str, lang: str) -> str:
    if re.search(r"^## (?:Conclusion|Conclusión)\b", text, re.M):
        return text
    block = CONCLUSION_EN if lang == "en" else CONCLUSION_ES
    # Prefer before Tao if present, else before References
    if re.search(r"^## Tao ", text, re.M):
        return re.sub(r"(^## Tao )", block + "\n---\n\n\\1", text, count=1, flags=re.M)
    return re.sub(
        r"(^## (?:References|Referencias)\b)",
        block + "\n---\n\n\\1",
        text,
        count=1,
        flags=re.M,
    )


def fix_learning_objectives(text: str, lang: str) -> str:
    if lang == "en":
        text = re.sub(
            r"^## [^\n]*Learning [Oo]bjectives[^\n]*$",
            "## Learning objectives",
            text,
            count=1,
            flags=re.M,
        )
        text = re.sub(
            r"^## Learning outcomes\b.*$",
            "## Learning objectives",
            text,
            count=1,
            flags=re.M,
        )
    else:
        text = re.sub(
            r"^## [^\n]*Objetivos de aprendizaje[^\n]*$",
            "## Objetivos de aprendizaje",
            text,
            count=1,
            flags=re.M,
        )
    return text


def promote_nested_masterclass(text: str) -> str:
    """I.1/I.2 pattern: B1 Analysis + ### Masterclass + #### ideas."""
    text = re.sub(
        r"^## B1 · Analysis[^\n]*$",
        "## Analysis",
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(
        r"^### Masterclass ideas[^\n]*$",
        "## Masterclass",
        text,
        count=1,
        flags=re.M,
    )
    # Promote idea headings #### → ###
    text = re.sub(r"^#### (\d+ · )", r"### \1", text, flags=re.M)
    return text


def rename_lab_workshop(text: str, ukey: str, lang: str) -> str:
    # Lab
    text = re.sub(
        r"^## B2 · (?:Lab \(Portfolio\)|Studio|Taller)[^\n]*$",
        "## Lab (Portfolio)" if lang == "en" else "## Lab (Portfolio)",
        text,
        count=1,
        flags=re.M,
    )
    # Already ## B2 · Lab without Studio
    text = re.sub(
        r"^## B2 · Lab[^\n]*$",
        "## Lab (Portfolio)",
        text,
        count=1,
        flags=re.M,
    )

    first = (
        WORKSHOP_FIRST.get(ukey, WORKSHOP_FIRST["i-2"])
        if lang == "en"
        else (WORKSHOP_FIRST_ES["i-1"] if ukey == "i-1" else WORKSHOP_FIRST_ES["default"])
    )
    # Workshop / B3 variants
    def workshop_repl(_m: re.Match[str]) -> str:
        return f"## Workshop\n\n{first}\n"

    text = re.sub(
        r"^## B3 · [^\n]+$",
        workshop_repl,
        text,
        count=1,
        flags=re.M,
    )
    # If already ## Workshop without session line, prepend
    m = re.search(r"^## Workshop\n+([^\n]+)", text, re.M)
    if m and not re.search(r"session|sesión", m.group(1), re.I):
        text = re.sub(
            r"^## Workshop\n+",
            f"## Workshop\n\n{first}\n\n",
            text,
            count=1,
            flags=re.M,
        )
    return text


def split_h2(text: str) -> tuple[str, list[tuple[str, str]]]:
    parts = re.split(r"(^## .+)$", text, flags=re.M)
    if len(parts) == 1:
        return text, []
    preamble = parts[0]
    sections: list[tuple[str, str]] = []
    i = 1
    while i < len(parts):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections.append((heading, body))
        i += 2
    return preamble, sections


def reorder_spine(text: str, lang: str) -> str:
    """Force Analysis → Masterclass → Lab → Workshop → Conclusion → Tao → References."""
    if lang == "en":
        names = [
            "Learning objectives",
            "Analysis",
            "Masterclass",
            "Lab (Portfolio)",
            "Workshop",
            "Conclusion",
            "Tao of the Image",
            "References",
        ]
    else:
        names = [
            "Objetivos de aprendizaje",
            "Análisis",
            "Masterclass",
            "Lab (Portfolio)",
            "Workshop",
            "Conclusión",
            "Tao de la imagen",
            "Referencias",
        ]
    preamble, sections = split_h2(text)
    by_key: dict[str, tuple[str, str]] = {}
    for h, b in sections:
        title = re.sub(r"^##\s+", "", h).strip()
        title_plain = re.sub(r"\s*\{[^}]*\}\s*$", "", title).strip()
        for name in names:
            if title_plain == name or title_plain.startswith(name + " "):
                if name.startswith("Tao"):
                    label = (
                        "## Tao of the Image {#tao-of-the-image}"
                        if lang == "en"
                        else "## Tao de la imagen {#tao-of-the-image}"
                    )
                    by_key[name] = (label, b)
                else:
                    by_key[name] = (f"## {name}", b)
                break

    spine_set = set(names)
    pre: list[tuple[str, str]] = []
    mid: list[tuple[str, str]] = []
    post: list[tuple[str, str]] = []
    phase = "pre"
    for h, b in sections:
        title = re.sub(r"^##\s+", "", h).strip()
        title_plain = re.sub(r"\s*\{[^}]*\}\s*$", "", title).strip()
        key = None
        for name in names:
            if title_plain == name or title_plain.startswith(name + " "):
                key = name
                break
        if key == names[0]:
            phase = "mid"
            continue
        if key in spine_set:
            if key in ("References", "Referencias"):
                phase = "post"
            continue
        if re.search(r"Editorial|Nota editorial|AI-assisted|Autoría", title, re.I):
            post.append((h, b))
            continue
        if phase == "pre":
            pre.append((h, b))
        elif phase == "post":
            post.append((h, b))
        else:
            mid.append((h, b))

    fold_pat = re.compile(
        r"^## (?:Where this sits|Critical perspective|Perspectiva crítica)\b",
        re.I,
    )
    analysis_name = names[1]
    remain_mid: list[tuple[str, str]] = []
    folded = ""
    for h, b in mid:
        if fold_pat.match(h) and analysis_name in by_key:
            # Demote to ### so the lesson H2 spine stays unique.
            demoted = re.sub(r"^## ", "### ", h, count=1)
            folded += demoted + b
        else:
            remain_mid.append((h, b))
    if folded and analysis_name in by_key:
        ah, ab = by_key[analysis_name]
        by_key[analysis_name] = (ah, "\n" + folded + ab)

    out = [preamble]
    for h, b in pre:
        out.append(h + b)
    if names[0] in by_key:
        out.append(by_key[names[0]][0] + by_key[names[0]][1])
    for h, b in remain_mid:
        out.append(h + b)
    for name in names[1:]:
        if name in by_key:
            out.append(by_key[name][0] + by_key[name][1])
    for h, b in post:
        out.append(h + b)
    return "".join(out)


def renames_scaffold_i3_plus(text: str, lang: str) -> str:
    """I.3–I.9: B1 Conceptual → Analysis; Why-this-unit → Masterclass when present."""
    analysis_h = "## Analysis" if lang == "en" else "## Análisis"
    text = re.sub(
        r"^## B1 · Conceptual[^\n]*$",
        analysis_h,
        text,
        count=1,
        flags=re.M,
    )
    # Promote Why-this-unit / Por qué to Masterclass if no Masterclass yet
    if not re.search(r"^## Masterclass\b", text, re.M):
        text = re.sub(
            r"^## Why this unit exists[^\n]*$",
            "## Masterclass",
            text,
            count=1,
            flags=re.M,
        )
        text = re.sub(
            r"^## Por qué existe esta unidad[^\n]*$",
            "## Masterclass",
            text,
            count=1,
            flags=re.M,
        )
    # If Analysis is still missing but Critical exists, rename Critical → Analysis
    if not re.search(r"^## (?:Analysis|Análisis)\b", text, re.M):
        text = re.sub(
            r"^## Critical perspective\b.*$",
            "## Analysis" if lang == "en" else "## Análisis",
            text,
            count=1,
            flags=re.M,
        )
        text = re.sub(
            r"^## Perspectiva crítica\b.*$",
            "## Análisis",
            text,
            count=1,
            flags=re.M,
        )
    # Ensure Spanish Analysis label
    if lang == "es":
        text = re.sub(r"^## Analysis\b", "## Análisis", text, flags=re.M)
    return text


def ensure_placeholder_lab(text: str, lang: str) -> str:
    """I.6–I.9: replace thin Studio Lab with placeholder cards if no Exercise headings."""
    lab = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", text, re.M)
    if not lab:
        return text
    body = lab.group(1)
    if re.search(r"^### (?:Exercise|Ejercicio) ", body, re.M):
        return text
    block = PLACEHOLDER_LAB_EN if lang == "en" else PLACEHOLDER_LAB_ES
    # Unescape doubled braces from format-safe template
    block = block.replace("{{{{", "{{").replace("}}}}", "}}").replace("{{%", "{%").replace("%}}", "%}")
    return text[: lab.start()] + block + "\n---\n\n" + text[lab.end() :]


def add_example_traces_en(text: str, ukey: str) -> str:
    """Insert Example trace after each Source: line inside Lab if missing."""
    lab_m = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", text, re.M)
    if not lab_m:
        return text
    lab = lab_m.group(0)
    if lab.count("**Example trace:**") >= 2:
        return text

    traces = {
        "i-1": [
            "**Example trace:** *(Illustrative · not student work.)* Practice: editorial. Agents: photographer + stylist. Venue: lookbook PDF. Interests: brand launch. Sentence: “JPEG is storage; the job is editorial circulation.” Art/commerce: gallery reprint of the same frame.",
            "**Example trace:** *(Illustrative · not student work.)* Head-count scaffold on blank canvas; blocked torso as three volumes; export named `figurin-scaffold-only.png`; proportion sentence: “Eight-head grid survives if waist landmark stays before finish.”",
        ],
        "i-2": [
            "**Example trace:** *(Illustrative · not student work.)* Scaffold layer with shoulder/waist/hip landmarks; garment layer only on a second pass; sentence: “Hip landmark locked the pose before any sleeve finish.”",
            "**Example trace:** *(Illustrative · not student work.)* Three silhouettes scored 3/4/5 on novelty·fit; winner colour-coded construction (blue) vs finish (black); peer: “I still read a coat when finish is hidden.”",
        ],
        "i-3": [
            "**Example trace:** *(Illustrative · not student work.)* Brief: audience = campus drop, channel = Instagram square, claim = “denim reads cooler under tungsten.” Five-swatch strip + one high-contrast alternate; hierarchy note: “Claim forced the mid-blue to lose saturation.”",
            "**Example trace:** *(Illustrative · not student work.)* Relation = proximity. Crop A clusters buttons; crop B spreads them. Peer: “A groups as a placket; B reads as scatter.”",
        ],
        "i-4": [
            "**Example trace:** *(Illustrative · not student work.)* Before/after of one local adjustment with layer named `fx-dodge-cheek`; process note: “Effect is recoverable; flattened export discarded.”",
            "**Example trace:** *(Illustrative · not student work.)* Photobash seam marked; one sentence on light direction mismatch kept visible in the index.",
        ],
        "i-5": [
            "**Example trace:** *(Illustrative · not student work.)* Two orthographic views + one perspective thumbnail; note: “Form read fails when the silhouette alone is trusted.”",
            "**Example trace:** *(Illustrative · not student work.)* Clay vs screen pass of the same volume; sentence: “The hand pass revealed underarm void the mesh smoothed away.”",
        ],
    }.get(ukey, [])

    if not traces:
        return text

    # Append example traces after each **Source:** line within Lab (first two)
    parts = re.split(r"(\*\*Source:\*\*[^\n]+)", lab)
    out = []
    ti = 0
    i = 0
    while i < len(parts):
        out.append(parts[i])
        if parts[i].startswith("**Source:**") and ti < len(traces):
            # peek if next already has Example trace
            nxt = parts[i + 1] if i + 1 < len(parts) else ""
            if "**Example trace:**" not in nxt[:200]:
                out.append("\n\n" + traces[ti] + "\n")
                ti += 1
        i += 1
    new_lab = "".join(out)
    return text[: lab_m.start()] + new_lab + text[lab_m.end() :]


def process_en_unit(path: Path) -> None:
    slug = path.parent.name
    ukey = unit_key(slug)
    text = path.read_text()
    text = fix_learning_objectives(text, "en")

    if ukey in ("i-1", "i-2") or "### Masterclass ideas" in text:
        text = promote_nested_masterclass(text)
    else:
        text = renames_scaffold_i3_plus(text, "en")

    text = rename_lab_workshop(text, ukey, "en")

    if ukey in ("i-6", "i-7", "i-8", "i-9"):
        text = ensure_placeholder_lab(text, "en")

    if ukey in ("i-1", "i-2", "i-3", "i-4", "i-5"):
        text = add_example_traces_en(text, ukey)

    text = ensure_conclusion(text, "en")
    text = ensure_tao(text, "en")
    text = reorder_spine(text, "en")
    path.write_text(text)
    print("EN", slug)


def process_es_unit(path: Path) -> None:
    slug = path.parent.name
    ukey = unit_key(slug)
    text = path.read_text()
    text = fix_learning_objectives(text, "es")

    # Nested masterclass (rare in ES); still rename B1 Analysis if present
    text = re.sub(r"^## B1 · Análisis[^\n]*$", "## Análisis", text, count=1, flags=re.M)
    text = re.sub(r"^## B1 · Analysis[^\n]*$", "## Análisis", text, count=1, flags=re.M)
    text = re.sub(r"^### Masterclass ideas[^\n]*$", "## Masterclass", text, count=1, flags=re.M)
    text = re.sub(r"^#### (\d+ · )", r"### \1", text, flags=re.M)

    text = renames_scaffold_i3_plus(text, "es")
    # i-1 ES may have B1 Conceptual without nested masterclass — Why → Masterclass already handled

    text = rename_lab_workshop(text, ukey, "es")

    if ukey in ("i-6", "i-7", "i-8", "i-9"):
        text = ensure_placeholder_lab(text, "es")

    text = ensure_conclusion(text, "es")
    text = ensure_tao(text, "es")
    text = reorder_spine(text, "es")
    path.write_text(text)
    print("ES", slug)


def process_fashion(path: Path) -> None:
    text = path.read_text()
    text = fix_learning_objectives(text, "en")
    text = re.sub(r"^## B1 · Analysis[^\n]*$", "## Analysis", text, count=1, flags=re.M)
    text = re.sub(
        r"^## Masterclass ideas \(six\)\s*$",
        "## Masterclass",
        text,
        count=1,
        flags=re.M,
    )
    text = re.sub(r"^## B2 · Lab[^\n]*$", "## Lab (Portfolio)", text, count=1, flags=re.M)
    # Fashion ML: no Workshop/Tao required by CT pattern — still add Tao anchor for deck links if any
    if not re.search(r"^## Conclusion\b", text, re.M):
        text = re.sub(
            r"(^## References\b)",
            CONCLUSION_EN + "\n---\n\n\\1",
            text,
            count=1,
            flags=re.M,
        )
    # Example trace for ML lab if exercises exist
    if "**Example trace:**" not in text and re.search(r"^## Lab", text, re.M):
        text = re.sub(
            r"(^## Lab \(Portfolio\)\n)",
            r"\1\n*Illustrative traces below are professor-made examples — not student work.*\n",
            text,
            count=1,
            flags=re.M,
        )
    path.write_text(text)
    print("ML fashion-image-analysis")


def main() -> None:
    en_dir = LESSONS / "en" / "digital-creativity-i"
    es_dir = LESSONS / "es" / "creacion-digital-i"
    for p in sorted(en_dir.glob("i-*/index.md")):
        process_en_unit(p)
    for p in sorted(es_dir.glob("i-*/index.md")):
        process_es_unit(p)
    fashion = LESSONS / "en" / "master-lectures" / "fashion-image-analysis" / "index.md"
    if fashion.exists():
        process_fashion(fashion)


if __name__ == "__main__":
    main()
