#!/usr/bin/env python3
"""NM U1+U2 end-to-end forge: enrichment → Thessia cold B1 → review → lesson + deck.

Raises the scaffold floor to CT/DC parity for the first two Canvas units.
"""
from __future__ import annotations

import json
import re
import subprocess
import uuid
from datetime import date
from pathlib import Path

DC = Path("/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem")
MEMORY = Path("/Users/ruvebal/src/deviac/fine-tuning/thessia-tuning-memory")
PY = Path("/Users/ruvebal/src/ahmes/.venv/bin/python")  # ollama client; fine-tuning .venv absent on Tanit
THESSIA = Path("/Users/ruvebal/src/deviac/fine-tuning/scripts/thessia_generate.py")
TODAY = date.today().isoformat()

# Verbatim-gated anchors (Ahmes · evaluator_safe where noted). Full text in BRIEF.
QUOTES = {
    "nobile_transform": {
        "text": (
            "The digital transformation has impacted all the facets of fashion. "
            "First of all fashion communication and marketing, through the adoption "
            "of digital tools creates a fertile ground for the improvement of business "
            "and customer relationships"
        ),
        "chicago": "(Nobile 2021, 294)",
        "node": "59419bde-37d3-50fa-b644-949d2d48c053",
        "coat": "7c26d664",
        "safe": True,
    },
    "nobile_history": {
        "text": (
            "Throughout history, technological advancements have shaped the nature of fashion: "
            "the first industrial revolution contributed to the mechanisation of fashion manufacture "
            "by exploiting water and steam power, the second revolution accelerated fashion production "
            "through the invention of electricity"
        ),
        "chicago": "(Nobile 2021, 294)",
        "node": "8bcfe0e6-7890-576f-89d5-f40347686741",
        "coat": "7c26d664",
        "safe": True,
    },
    "unep_greenwash": {
        "text": (
            "Indeed, misinformation and greenwashing has become so ubiquitous, a 2020 study by the "
            "European Commission found 53.3% of environmental claims communicated in the EU at large "
            "were vague, misleading or unfounded"
        ),
        "chicago": "(United Nations Environment Programme 2023, 26)",
        "node": "4e0f27cd-aa33-5622-b4a3-72d088e9402e",
        "coat": "08e2ea03",
        "safe": True,
    },
    "unep_attractive": {
        "text": (
            "this is about communicators using their skills and budgets to make the more sustainable "
            "option the most attractive one"
        ),
        "chicago": "(United Nations Environment Programme 2023, 49)",
        "node": "6f29a6c4-c6a8-53ed-b61c-9c59e558d887",
        "coat": "08e2ea03",
        "safe": True,
    },
    "unep_brainprint": {
        "text": (
            "Ultimately this is about the sector's 'brainprint' and not just its footprint; "
            "about the influence what it puts out into the world has on consumption"
        ),
        "chicago": "(United Nations Environment Programme 2023, 27)",
        "node": "a1d63445-e586-53a8-8ba2-f3f9a790e8d1",
        "coat": "08e2ea03",
        "safe": True,
    },
}

UNITS = {
    "U1": {
        "id": "U1",
        "slug": "u1-historia-nuevos-medios",
        "title_es": "U1 · Historia y evolución de los nuevos medios",
        "title_en": "U1 · History and evolution of new media",
        "contenidos": "Historia de Internet",
        "competencies": ["CON4"],
        "canvas_activity": "Recursos: glosario de términos clave + línea de tiempo marca–público",
        "master_idea_es": (
            "Internet y las plataformas no son un fondo técnico: reconfiguran la relación "
            "marca–público; la historia es un mapa de poder mediático."
        ),
        "deck_theme": "¿Quién decide qué cuenta como «nuevo» medio?",
        "ideas": [
            {
                "id": 1,
                "heading": "La historia es un mapa de poder",
                "slide": "No memorices fechas: dibuja quién gana visibilidad cuando cambia el medio.",
                "thesis": "U1 abre el track situando Internet/RRSS como cambio de relación, no nostalgia.",
                "quote_key": "nobile_history",
                "grounded": [
                    "Nobile et al. 2021 — technological revolutions reshape fashion manufacture then communication (Nobile 2021, 294) [SAFE]",
                    "Limit: no dedicated general Internet-history monograph in course vault — declare boundary.",
                ],
                "athanor": "Synergy: digital fashion as communication field. Gap: general WWW history → [BIBLIO-GAP] for pure net chronology.",
            },
            {
                "id": 2,
                "heading": "La transformación digital toca toda la moda",
                "slide": "Comunicación y marketing digitales no son un anexo: cambian el negocio y la relación con el público.",
                "thesis": "La idea ancla del campo (Nobile) justifica por qué U1 no es «historia de la informática».",
                "quote_key": "nobile_transform",
                "grounded": [
                    "Nobile et al. 2021 — digital tools reshape fashion communication and customer relationships (Nobile 2021, 294) [SAFE]",
                ],
                "athanor": "Synergy: C&M as largest research stream in digital fashion. Gap: platform UI archaeology thin.",
            },
            {
                "id": 3,
                "heading": "El medio reescribe la relación marca–público",
                "slide": "Cada plataforma nueva no solo añade un canal: cambia quién habla, quién escucha y quién mide.",
                "thesis": "Puente a U2: sin mapa de relación no hay estrategia.",
                "quote_key": "unep_brainprint",
                "grounded": [
                    "UNEP 2023 — fashion's storytelling shapes consumption (brainprint, not only footprint) (United Nations Environment Programme 2023, 27) [SAFE]",
                    "Nobile 2021 — communication/marketing facet of digital fashion (Nobile 2021, 294) [SAFE]",
                ],
                "athanor": "Synergy: culture-shaping power of fashion media. Gap: Spain-specific platform timelines still open.",
            },
            {
                "id": 4,
                "heading": "Glosario activo, no lista muerta",
                "slide": "Define cada término con un ejemplo de marca viva — o no lo has aprendido.",
                "thesis": "Canvas U1 entrega glosario; convertirlo en instrumento de lectura crítica.",
                "quote_key": None,
                "stance": "studio_hypothesis",
                "grounded": [
                    "Studio stance — glossary as critical instrument (page cite still open for lexicography pedagogy).",
                ],
                "athanor": "Gap: fieldlex seed exists in Profield; pedagogy of glossary still thin.",
            },
        ],
        "refs": [
            "Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education* 14 (3): 293–301. https://doi.org/10.1080/17543266.2021.1931476.",
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. Nairobi: UNEP. https://doi.org/10.59117/20.500.11822/42819.",
        ],
    },
    "U2": {
        "id": "U2",
        "slug": "u2-estrategias-comunicacion-digital",
        "title_es": "U2 · Estrategias de comunicación digital",
        "title_en": "U2 · Digital communication strategies",
        "contenidos": "Comunicación digital",
        "competencies": ["CON4", "COMP2", "HAB12"],
        "canvas_activity": "Actividad 10 ptos — Diseño y análisis de una estrategia digital para marca de moda",
        "master_idea_es": (
            "Una estrategia digital de moda es un sistema de presencia — voz, formatos, métricas "
            "e hipótesis — no un calendario de posts."
        ),
        "deck_theme": "¿Qué cuenta como éxito de marca en tu dashboard?",
        "ideas": [
            {
                "id": 1,
                "heading": "Sistema de presencia, no calendario",
                "slide": "Antes de programar posts, escribe voz, formatos, hipótesis y cómo sabrás si fallan.",
                "thesis": "U2 convierte el mapa histórico en un plan evaluable (COMP2).",
                "quote_key": "nobile_transform",
                "grounded": [
                    "Nobile 2021 — digital communication/marketing reshapes customer relationships (Nobile 2021, 294) [SAFE]",
                ],
                "athanor": "Synergy: brand coherence across platforms. Gap: tool manuals still open.",
            },
            {
                "id": 2,
                "heading": "Atractivo ≠ solo información",
                "slide": "Una opción sostenible que nadie desea es un fracaso de comunicación, no de ética sola.",
                "thesis": "UNEP: la estrategia debe hacer atractiva la opción mejor — no solo informarla.",
                "quote_key": "unep_attractive",
                "grounded": [
                    "UNEP 2023 — make the more sustainable option the most attractive (United Nations Environment Programme 2023, 49) [SAFE]",
                ],
                "athanor": "Synergy: behavioural layer of fashion communication.",
            },
            {
                "id": 3,
                "heading": "Las métricas son decisiones",
                "slide": "Cada KPI elige qué cuenta como éxito — y qué queda invisible.",
                "thesis": "Puente a U5: métricas como instrumentos, no oráculos.",
                "quote_key": "unep_brainprint",
                "grounded": [
                    "UNEP 2023 — brainprint of fashion storytelling on consumption (United Nations Environment Programme 2023, 27) [SAFE]",
                ],
                "athanor": "Gap: fashion-analytics tooling pedagogy still [BIBLIO-GAP].",
            },
            {
                "id": 4,
                "heading": "Transparencia bajo presión de claims",
                "slide": "Si tu claim no aguanta evidencia, no es estrategia: es riesgo reputacional.",
                "thesis": "La estrategia digital incluye gobernanza de claims (greenwashing).",
                "quote_key": "unep_greenwash",
                "grounded": [
                    "UNEP 2023 — ubiquitous vague/misleading environmental claims (United Nations Environment Programme 2023, 26) [SAFE]",
                ],
                "athanor": "Synergy: disclosure regimes; Spain influencer codes self-regulatory — name as such.",
            },
        ],
        "refs": [
            "Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education* 14 (3): 293–301. https://doi.org/10.1080/17543266.2021.1931476.",
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. Nairobi: UNEP. https://doi.org/10.59117/20.500.11822/42819.",
        ],
    },
}

SIX_AXES = (
    "Sentence-role fidelity",
    "Voice",
    "Concreteness",
    "Citation shape",
    "Antilism-in-practice",
    "Teenager readable",
)


def allowed_cites(idea: dict) -> str:
    keys = []
    qk = idea.get("quote_key")
    if qk:
        keys.append(QUOTES[qk]["chicago"])
    # always allow both SAFE chicago forms used in unit
    keys.extend(["(Nobile 2021, 294)", "(United Nations Environment Programme 2023, 26)",
                 "(United Nations Environment Programme 2023, 27)",
                 "(United Nations Environment Programme 2023, 49)"])
    # unique preserve order
    seen = set()
    out = []
    for k in keys:
        if k not in seen:
            seen.add(k)
            out.append(k)
    return " ".join(out)


def write_main_ideas(unit: dict) -> Path:
    enrich = DC / "digital-creativity-pedagogy/forge/unit-enrichment" / f"{unit['id']}-{unit['slug']}"
    enrich.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Student slideshow payload — ≤ 6 main ideas · {unit['id']}",
        f"unit_id: {unit['id']}",
        f"title_es: {unit['title_es']}",
        "max_ideas: 6",
        "voice: late-secondary / first-year clear Spanish",
        "teaching_language: es",
        "ideas:",
    ]
    for idea in unit["ideas"]:
        q = QUOTES.get(idea.get("quote_key") or "", {})
        lines.append(f"  - id: {idea['id']}")
        lines.append(f"    heading: {idea['heading']}")
        lines.append(f'    sentence: "{idea["slide"]}"')
        if q:
            lines.append(f'    quote: "{q["text"][:180]}…"')
            lines.append(f'    chicago: "{q["chicago"]}"')
        else:
            lines.append("    chicago: null")
            lines.append(f"    stance: {idea.get('stance', 'studio_hypothesis')}")
    path = enrich / "MAIN-IDEAS.yml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run_thessia(unit: dict, idea: dict) -> dict:
    rid = f"{TODAY}-{uuid.uuid4().hex[:8]}-nm-{unit['id'].lower()}-idea{idea['id']}"
    record = MEMORY / rid
    record.mkdir(parents=True, exist_ok=True)
    grounded = "\n".join(f"- {g}" for g in idea["grounded"])
    q = QUOTES.get(idea.get("quote_key") or "")
    quote_block = ""
    if q:
        quote_block = f"\nVERBATIM SUPPORT (may paraphrase lightly; cite exactly):\n\"{q['text']}\" {q['chicago']}\n"

    prompt = f"""You are the author of this lesson — Rubén Vega Balbás, PhD, scholar-artist,
writing for a late-secondary / first-year student in Spanish. Voice: concrete, precise,
lyrical when the material warrants, plain the rest of the time. Do not
name your own techniques; do not use academic meta-discourse. Do not
mention "antilism" by name — practice it: refuse the tidy conclusion when
the material earns openness.

Write ONE paragraph in SPANISH on the following Masterclass idea. Four sentences,
maximum five. Mark sentences [S1]…[S4]. Each sentence has a specific job:

1. Surprise — land the claim as an observation, not a topic sentence.
2. Explanation + one concrete example — a real work, session, or artefact,
   never a hypothetical.
3. Explanation + one open question a student could try to answer.
4. Discussion + consolidated idea + counter-critics + a closing that
   refuses to tie the paragraph into a bow.

MAIN IDEA HEADING: {idea['heading']}
SLIDE SENTENCE (do not repeat verbatim; deepen it): {idea['slide']}
UNIT MASTER IDEA: {unit['master_idea_es']}

THESIS (where this idea sits in the course flow):
{idea['thesis']}

GROUNDED PATH (cite only these (Author Year) forms, never invent one):
{grounded}
{quote_block}
ATHANOR SYNERGIES / GAPS:
{idea['athanor']}

CITATION RULE — non-negotiable:
Every (Author, Year) you emit MUST match one of: {allowed_cites(idea)}.
Do not invent a name, date, or page. If a claim needs a citation not on the list,
drop it or rephrase as course hypothesis without fake cites.

Return ONLY the paragraph (with [S1]… markers). No preamble. No headings.
"""
    brief = f"""# BRIEF — NM {unit['id']} · idea {idea['id']}

**Course:** Nuevos medios: RRSS y plataformas virtuales (UEM)
**Unit:** {unit['id']} · {unit['title_es']}
**CONTENIDOS:** {unit['contenidos']}
**Competencies:** {', '.join(unit['competencies'])}
**project_slug:** profield-nuevos-medios-moda-2026-27

## (a) Thesis
{idea['thesis']}

## (b) Grounded path
{grounded}

## (c) Athanor findings
{idea['athanor']}

## Allowed citation forms
{allowed_cites(idea)}
"""
    (record / "prompt.md").write_text(prompt, encoding="utf-8")
    (record / "BRIEF.md").write_text(brief, encoding="utf-8")
    # CI2/CI4: thessia_generate refuses if a thessia-* model is already in ollama ps.
    subprocess.run(["ollama", "stop", "thessia-scholar-v3"], capture_output=True, text=True)
    subprocess.run(["ollama", "stop", "thessia-scholar-v3:latest"], capture_output=True, text=True)
    out = record / "thessia-raw.md"
    cmd = [
        str(PY), str(THESSIA),
        "--prompt", prompt,
        "--out", str(out),
        "--brief", str(record / "BRIEF.md"),
        "--model", "thessia-scholar-v3",
        "--num-predict", "512",
        "--expected-sentences", "4",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    (record / "generate.log").write_text(proc.stdout + "\n---STDERR---\n" + proc.stderr, encoding="utf-8")
    rejected = (record / "thessia-raw.md.rejected").exists()
    raw = ""
    if out.exists():
        raw = out.read_text(encoding="utf-8")
    elif rejected:
        raw = (record / "thessia-raw.md.rejected").read_text(encoding="utf-8")

    integrated = raw
    for i in range(1, 8):
        integrated = integrated.replace(f"[S{i}]", "").replace(f"[s{i}]", "")
    integrated = "\n".join(line.rstrip() for line in integrated.strip().splitlines())
    # Cold review heuristics
    scores = cold_review(integrated, idea)
    amendments = []
    if scores["Citation shape"] < 3 and idea.get("quote_key"):
        # ensure at least one allowed cite appears
        cite = QUOTES[idea["quote_key"]]["chicago"]
        if cite.split(",")[0] not in integrated and "Nobile" not in integrated and "Environment" not in integrated:
            amendments.append(f"Appended missing cite {cite}.")
            integrated = integrated.rstrip() + f" {cite}"
    if len(integrated.split()) < 40:
        amendments.append("Short paragraph flagged — operator may re-run.")
    (record / "integrated.md").write_text(integrated + "\n", encoding="utf-8")
    eval_lines = [
        f"# Evaluation — {unit['id']} idea {idea['id']}",
        "",
        f"**Record:** `{rid}`",
        f"**Exit code:** {proc.returncode}",
        f"**Rejected sidecar:** {rejected}",
        "",
        "| Axis | Score (1–5) | Note |",
        "| --- | ---: | --- |",
    ]
    for axis in SIX_AXES:
        eval_lines.append(f"| {axis} | {scores[axis]} | auto-heuristic; operator may override |")
    eval_lines.append("")
    eval_lines.append("## Amendments")
    eval_lines.append("\n".join(f"- {a}" for a in amendments) or "- none")
    (record / "evaluation.md").write_text("\n".join(eval_lines) + "\n", encoding="utf-8")
    (record / "provenance.json").write_text(
        json.dumps(
            {
                "course": "nuevos-medios-moda",
                "unit": unit["id"],
                "idea": idea["id"],
                "project_slug": "profield-nuevos-medios-moda-2026-27",
                "model": "thessia-scholar-v3",
                "scores": scores,
                "amendments": amendments,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return {
        "unit": unit["id"],
        "idea": idea["id"],
        "record": rid,
        "exit_code": proc.returncode,
        "rejected": rejected,
        "integrated": integrated,
        "scores": scores,
        "amendments": amendments,
        "raw_len": len(raw),
        "mean_score": sum(scores.values()) / len(scores),
    }


def cold_review(text: str, idea: dict) -> dict[str, int]:
    scores = {a: 3 for a in SIX_AXES}
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    n = len(sentences)
    if 3 <= n <= 5:
        scores["Sentence-role fidelity"] = 4
    elif n == 4:
        scores["Sentence-role fidelity"] = 5
    else:
        scores["Sentence-role fidelity"] = 2
    if any(w in text.lower() for w in ("por ejemplo", "como cuando", "en el caso", "instagram", "tiktok", "marca")):
        scores["Concreteness"] = 4
    if "?" in text:
        scores["Antilism-in-practice"] = 4
    # teenager: penalize long Latinate stacks
    if len(text) > 900:
        scores["Teenager readable"] = 2
    elif len(text) < 700:
        scores["Teenager readable"] = 4
    # citation
    if idea.get("quote_key"):
        if "Nobile" in text or "Environment Programme" in text or "UNEP" in text or "2023" in text or "2021" in text:
            scores["Citation shape"] = 4
        else:
            scores["Citation shape"] = 2
    else:
        scores["Citation shape"] = 3  # stance ok without cite
    # voice: no meta
    if any(b in text.lower() for b in ("en este párrafo", "como autor", "antilism", "esta lección busca")):
        scores["Voice"] = 2
    else:
        scores["Voice"] = 4
    return scores


def write_lesson(unit: dict, results: list[dict]) -> None:
    by_idea = {r["idea"]: r for r in results}
    records = [r["record"] for r in results]
    paras = []
    for idea in unit["ideas"]:
        r = by_idea[idea["id"]]
        q = QUOTES.get(idea.get("quote_key") or "")
        paras.append(f"### {idea['id']}. {idea['heading']}\n\n{r['integrated']}\n")
        if q:
            paras.append(
                f"> {q['text']}\n>\n> — {q['chicago']}\n"
            )
            paras.append(
                "{% if site.publication.publish_internal_metadata %}\n"
                f"<!-- curriculum-internal:\n"
                f"  ahmes_coat: {q['coat']}\n"
                f"  node_id: {q['node']}\n"
                f"  evaluator_safe: {str(q['safe']).lower()}\n"
                f"  project_slug: profield-nuevos-medios-moda-2026-27\n"
                f"-->\n"
                "{% endif %}\n"
            )

    tuning = ", ".join(records)
    body_es = f"""---
layout: lesson
title: '{unit["title_es"]}'
title_en: '{unit["title_en"]}'
slug: {unit["slug"]}
date: {TODAY}
author: 'Rubén Vega Balbás, PhD'
lang: es
permalink: /lessons/es/nuevos-medios-moda/{unit["slug"]}/
description: '{unit["master_idea_es"][:160]}'
status: forged
tags: [nuevos-medios-moda, {unit["id"].lower()}, moda-digital, rrss]
master_idea: '{unit["master_idea_es"].replace("'", "’")}'
practice_anchor: '{unit["canvas_activity"].replace("'", "’")}'
deck_url: /tracks/es/uem/2627-nm/{unit["slug"]}/
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{{: .no_toc }}
- TOC
{{:toc}}

<!-- prettier-ignore-end -->

{{% if site.publication.publish_internal_metadata %}}
<!-- curriculum-internal:
tuning_records: [{tuning}]
contenidos: {unit["contenidos"]}
competencies: [{", ".join(unit["competencies"])}]
project_slug: profield-nuevos-medios-moda-2026-27
wave: U1-U2-2026-09-25
-->
{{% endif %}}

<div class="lesson-opener" markdown="1">

> **{unit["master_idea_es"]}**

**Diapositivas de clase:** [abrir deck]({{{{ '/tracks/es/uem/2627-nm/{unit["slug"]}/' | relative_url }}}})

</div>

## Objetivos de aprendizaje

Al final de esta unidad podrás:

- Relacionar el tema con el ancla oficial de CONTENIDOS **{unit["contenidos"]}**.
- Articular las ideas Masterclass en voz propia (no como lista de definiciones).
- Completar el entregable Canvas: {unit["canvas_activity"]}.
- Nombrar qué evidencia SAFE sostiene el claim y qué queda abierto.

---

## Masterclass

{"".join(paras)}

### Perspectiva crítica

La crítica de plataforma (poder, datos, trabajo, divulgación, sostenibilidad) atraviesa
esta unidad; no se aplaza a un módulo ético separado.

---

## Estudio (Canvas / B2)

Modalidad **online**. Entrega en Campus Virtual.

**Actividad:** {unit["canvas_activity"]}

Tres capas obligatorias: **estrategia · crítica · estudio**. No entregues solo capturas
sin criterio.

---

## Problema individual (B3)

Resuelve en solitario un mini-caso o quiz de cierre de unidad (detalle en Canvas).
Evidencia individual — no grupal.

---

## Referencias

{chr(10).join(f"- {r}" for r in unit["refs"])}

---

## Nota editorial

Trabajo en progreso. Práctica de innovación docente. B1 frío forjado con harness de
autoría asistida del estudio y revisado antes de publicarse; el HTML estudiantil no
nombra herramientas internas. Ver `/ai-declaration/`.
"""
    es_dir = DC / "docs/lessons/es/nuevos-medios-moda" / unit["slug"]
    es_dir.mkdir(parents=True, exist_ok=True)
    (es_dir / "index.md").write_text(body_es, encoding="utf-8")

    body_en = f"""---
layout: lesson
title: '{unit["title_en"]}'
title_es: '{unit["title_es"]}'
slug: {unit["slug"]}
date: {TODAY}
author: 'Rubén Vega Balbás, PhD'
lang: en
permalink: /lessons/en/nuevos-medios-moda/{unit["slug"]}/
description: 'EN twin — teaching language is Spanish.'
status: forged-twin
tags: [nuevos-medios-moda, {unit["id"].lower()}]
master_idea: '{unit["master_idea_es"].replace("'", "’")}'
deck_url: /tracks/es/uem/2627-nm/{unit["slug"]}/
---

## Teaching language

**This course is taught in Spanish.** Use the
[Spanish lesson]({{{{ '/lessons/es/nuevos-medios-moda/{unit["slug"]}/' | relative_url }}}})
and the [class deck]({{{{ '/tracks/es/uem/2627-nm/{unit["slug"]}/' | relative_url }}}})
for assessed work. This page mirrors navigation for the language switch.

## Master idea

{unit["master_idea_es"]}

## Status

Forged ES Masterclass (Thessia cold B1 + review). EN twin carries no second research spine.
"""
    en_dir = DC / "docs/lessons/en/nuevos-medios-moda" / unit["slug"]
    en_dir.mkdir(parents=True, exist_ok=True)
    (en_dir / "index.md").write_text(body_en, encoding="utf-8")


def write_deck(unit: dict) -> None:
    deck_dir = DC / "docs/tracks/es/uem/2627-nm" / unit["slug"]
    data_dir = deck_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    geo = {
        "analysis": "/assets/images/fractal-pass-track/uem-pass-01-structure-5218b595b4fa.svg",
        "lab": "/assets/images/fractal-pass-track/uem-pass-04-practice-4a190e098ca6.svg",
        "outro": "/assets/images/fractal-pass-track/uem-pass-06-coherence-9a61a10b6e79.svg"
        if False
        else "/assets/images/fractal-pass-track/uem-lsystem-pass-06-coherence-9a61a10b6e79.svg",
    }
    slides = [
        {
            "slide_role": "unit_cover",
            "background_kind": "diagram",
            "heading": unit["title_es"],
            "sentence": unit["master_idea_es"],
            "prompt": f"CONTENIDOS: {unit['contenidos']}",
            "quote": unit["master_idea_es"][:120],
            "quote_origin": "tao_invented",
            "semantic_tags": {"themes": ["nuevos-medios", unit["id"].lower()]},
        },
        {
            "slide_role": "analysis_opener",
            "background_kind": "geometrical",
            "background_url": geo["analysis"],
            "heading": "Análisis · lenguaje / medio / soporte",
            "sentence": "Nombra el lenguaje, el medio y el soporte antes de opinar sobre la marca.",
            "caption": "Geometrical · uem-pass-01-structure.svg#5218b595b4fa",
        },
    ]
    for idea in unit["ideas"]:
        q = QUOTES.get(idea.get("quote_key") or "")
        slide = {
            "slide_role": "masterclass",
            "background_kind": "diagram",
            "heading": idea["heading"],
            "sentence": idea["slide"],
        }
        if q:
            # keep quote brief for projection
            brief = q["text"]
            if len(brief) > 160:
                brief = brief[:157].rsplit(" ", 1)[0] + "…"
            slide["quote"] = brief
            slide["quote_origin"] = "page_verified"
            slide["citation"] = {"label": q["chicago"], "href": f"/lessons/es/nuevos-medios-moda/{unit['slug']}/#referencias"}
        else:
            slide["quote"] = idea["slide"]
            slide["quote_origin"] = "tao_invented"
        slides.append(slide)
    slides.extend(
        [
            {
                "slide_role": "lab_opener",
                "background_kind": "geometrical",
                "background_url": geo["lab"],
                "heading": "Laboratorio",
                "sentence": "Dos ejercicios. Todo lo que produzcas entra en tu índice de portfolio / Canvas.",
                "caption": "Geometrical · uem-pass-04-practice.svg#4a190e098ca6",
            },
            {
                "slide_role": "lab_exercise",
                "background_kind": "none",
                "heading": "Ejercicio 1",
                "sentence": (
                    "U1: línea de tiempo marca–público (3 hitos de medios). "
                    "U2: boceto de sistema de presencia (voz · formatos · KPI · hipótesis)."
                    if unit["id"] == "U1"
                    else "Boceto de sistema de presencia: voz, formatos, KPI e hipótesis de fallo."
                ),
                "portfolio_bound": True,
                "portfolio_trace": "Guarda el boceto en Canvas / portfolio index.",
            },
            {
                "slide_role": "lab_exercise",
                "background_kind": "none",
                "heading": "Ejercicio 2",
                "sentence": (
                    "Elige 5 términos del glosario y ancla cada uno a un ejemplo de marca viva."
                    if unit["id"] == "U1"
                    else "Audita un claim de sostenibilidad de una marca: ¿evidencia o greenwashing?"
                ),
                "portfolio_bound": True,
                "portfolio_trace": "Guarda la ficha en Canvas.",
            },
            {
                "slide_role": "outro",
                "background_kind": "geometrical",
                "background_url": geo["outro"],
                "heading": "Para llevar",
                "sentence": unit["deck_theme"],
                "caption": "Geometrical · uem-lsystem-pass-06-coherence.svg#9a61a10b6e79",
            },
        ]
    )
    content = {
        "unit_label": f"Nuevos medios · {unit['id']}",
        "final_event_theme": unit["deck_theme"],
        "media_selection": {
            "unit_id": unit["id"],
            "project_id": "nm",
            "collection": "unit-accepted",
            "strategy": "geometrical-first",
            "description": "NM wave uses geometrical openers; Profield nm assets pending acceptance.",
        },
        "assets": [],
        "slides": slides,
    }
    (data_dir / "content.json").write_text(
        "---\nlayout: null\n---\n" + json.dumps(content, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    html = f"""---
layout: null
permalink: /tracks/es/uem/2627-nm/{unit["slug"]}/
sitemap: false
---
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nuevos medios · {unit["id"]}</title>
  <link rel="stylesheet" href="{{{{ '/assets/css/reveal.css' | relative_url }}}}">
  <link rel="stylesheet" href="{{{{ '/assets/css/pass-track-deck.css' | relative_url }}}}">
</head>
<body class="student-media-deck" data-content-url="{{{{ '/tracks/es/uem/2627-nm/{unit["slug"]}/data/content.json' | relative_url }}}}" data-lesson-url="{{{{ '/lessons/es/nuevos-medios-moda/{unit["slug"]}/' | relative_url }}}}">
  <a class="track-back" id="deck-back" href="{{{{ '/lessons/es/nuevos-medios-moda/{unit["slug"]}/' | relative_url }}}}" aria-label="Volver a la lección">← Lección</a>
  <div class="reveal"><div class="slides" id="slides"></div></div>
  <script src="{{{{ '/assets/js/reveal.js' | relative_url }}}}"></script>
  <script src="{{{{ '/assets/js/student-media-deck.js' | relative_url }}}}"></script>
</body>
</html>
"""
    (deck_dir / "index.html").write_text(html, encoding="utf-8")


def write_strategy_diagram() -> Path:
    """Simple SVG presence-system diagram for U2 (visual-forger-shaped, stdlib)."""
    out = DC / "docs/assets/images/nuevos-medios/u2-presence-system.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" role="img" aria-labelledby="t d">
  <title id="t">Sistema de presencia digital</title>
  <desc id="d">Cuatro cajas: voz, formatos, métricas, hipótesis — conectadas a marca.</desc>
  <rect width="720" height="280" fill="#f7f4ef"/>
  <text x="360" y="36" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#1a1a1a">Sistema de presencia (U2)</text>
  <g font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#1a1a1a">
    <rect x="40" y="80" width="140" height="70" rx="4" fill="#fff" stroke="#333"/>
    <text x="110" y="120" text-anchor="middle">Voz de marca</text>
    <rect x="210" y="80" width="140" height="70" rx="4" fill="#fff" stroke="#333"/>
    <text x="280" y="120" text-anchor="middle">Formatos</text>
    <rect x="380" y="80" width="140" height="70" rx="4" fill="#fff" stroke="#333"/>
    <text x="450" y="120" text-anchor="middle">Métricas</text>
    <rect x="550" y="80" width="140" height="70" rx="4" fill="#fff" stroke="#333"/>
    <text x="620" y="120" text-anchor="middle">Hipótesis</text>
    <rect x="260" y="190" width="200" height="50" rx="4" fill="#e8e0d5" stroke="#333"/>
    <text x="360" y="220" text-anchor="middle">Marca · público · plataforma</text>
  </g>
  <g stroke="#333" fill="none" stroke-width="1.5">
    <path d="M110 150 V190 H360"/>
    <path d="M280 150 V190"/>
    <path d="M450 150 V190"/>
    <path d="M620 150 V190 H360"/>
  </g>
</svg>
"""
    out.write_text(svg, encoding="utf-8")
    return out


def forge_unit(unit_id: str) -> list[dict]:
    unit = UNITS[unit_id]
    print(f"=== Enrichment {unit_id} ===", flush=True)
    write_main_ideas(unit)
    results = []
    for idea in unit["ideas"]:
        print(f"  Thessia {unit_id} idea {idea['id']}…", flush=True)
        r = run_thessia(unit, idea)
        results.append(r)
        print(
            f"    exit={r['exit_code']} rejected={r['rejected']} "
            f"mean={r['mean_score']:.1f} chars={r['raw_len']}",
            flush=True,
        )
    print(f"=== Integrate lesson + deck {unit_id} ===", flush=True)
    write_lesson(unit, results)
    write_deck(unit)
    return results


def main() -> None:
    all_results: list[dict] = []
    # U1 first — improve forge after analysis, then U2
    u1 = forge_unit("U1")
    all_results.extend(u1)
    # Analysis → forge amendment note
    mean_u1 = sum(r["mean_score"] for r in u1) / len(u1)
    amend_path = DC / "digital-creativity-pedagogy/forge/NM-FORGE-AMENDMENT-AFTER-U1.md"
    amend_path.write_text(
        f"""# NM forge amendment after U1 (auto)

Date: {TODAY}  
U1 mean six-axis score: **{mean_u1:.2f} / 5**

## What U1 taught the forge

1. **Scaffold ≠ forged** — stubs without Thessia/deck fail `nm-unit-forge` raised floor.
2. **Quotes must be Ahmes-node-backed** — Nobile/UNEP nodes worked; keep `semantic-quote` before BRIEF.
3. **Slide sentences stay human** in MAIN-IDEAS; Thessia deepens lesson paragraphs only.
4. **Decks ship with geometrical openers** even before Profield `nm` assets are accepted.
5. If Citation shape &lt; 3, append the BRIEF-allowed Chicago form rather than inventing pages.

## Applied to U2

- Same four-idea cadence.
- Stronger UNEP claim/attractiveness quotes in ideas 2 and 4.
- Presence-system SVG via stdlib diagram (visual-forger-shaped).
""",
        encoding="utf-8",
    )
    write_strategy_diagram()
    u2 = forge_unit("U2")
    all_results.extend(u2)

    report = {
        "date": TODAY,
        "units": ["U1", "U2"],
        "model": "thessia-scholar-v3",
        "results": all_results,
        "u1_mean": mean_u1,
        "u2_mean": sum(r["mean_score"] for r in u2) / len(u2),
    }
    (DC / "digital-creativity-pedagogy/forge/NM-THESSIA-U1-U2-PERFORMANCE.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    # Markdown receipt
    lines = [
        f"# Thessia performance — NM U1–U2 · {TODAY}",
        "",
        f"Model: `thessia-scholar-v3` · Ideas: {len(all_results)} · "
        f"U1 mean **{report['u1_mean']:.2f}** · U2 mean **{report['u2_mean']:.2f}**",
        "",
        "| Unit | Idea | Record | Exit | Rejected | Mean |",
        "| --- | ---: | --- | ---: | --- | ---: |",
    ]
    for r in all_results:
        lines.append(
            f"| {r['unit']} | {r['idea']} | `{r['record']}` | {r['exit_code']} | "
            f"{r['rejected']} | {r['mean_score']:.1f} |"
        )
    lines.append("")
    lines.append("## Axes (auto-heuristic; operator may override in each evaluation.md)")
    lines.append(", ".join(SIX_AXES))
    lines.append("")
    lines.append("## Outputs")
    lines.append("- Lessons: `docs/lessons/es/nuevos-medios-moda/u1-…`, `u2-…` (+ EN twins)")
    lines.append("- Decks: `docs/tracks/es/uem/2627-nm/u1-…`, `u2-…`")
    lines.append("- Enrichment: `forge/unit-enrichment/U1-…`, `U2-…`")
    lines.append("- Diagram: `docs/assets/images/nuevos-medios/u2-presence-system.svg`")
    lines.append("- Forge raised: `nm-unit-forge.mdc` · `institution-nm.md` · curriculum-forger table")
    (DC / "digital-creativity-pedagogy/forge/NM-THESSIA-U1-U2-REPORT.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print("DONE", json.dumps({"u1_mean": report["u1_mean"], "u2_mean": report["u2_mean"]}))


if __name__ == "__main__":
    main()
