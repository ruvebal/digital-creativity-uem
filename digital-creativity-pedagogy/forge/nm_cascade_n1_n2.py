#!/usr/bin/env python3
"""NM cascade N1–N2: scaffold lessons + Thessia cold B1 (one idea per unit)."""
from __future__ import annotations

import json
import subprocess
import uuid
from datetime import date
from pathlib import Path

DC = Path("/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem")
MEMORY = Path("/Users/ruvebal/src/deviac/fine-tuning/thessia-tuning-memory")
PY = Path("/Users/ruvebal/src/deviac/fine-tuning/.venv/bin/python")
THESSIA = Path("/Users/ruvebal/src/deviac/fine-tuning/scripts/thessia_generate.py")
TODAY = date.today().isoformat()

UNITS = [
    {
        "id": "U1",
        "slug_es": "u1-historia-nuevos-medios",
        "slug_en": "u1-history-new-media",
        "title_es": "U1 · Historia y evolución de los nuevos medios",
        "title_en": "U1 · History and evolution of new media",
        "contenidos": "Historia de Internet",
        "competencies": ["CON4"],
        "master_idea_es": "Internet y las plataformas no son un fondo técnico: reconfiguran la relación marca–público; la historia es un mapa de poder mediático.",
        "master_idea_en": "Internet and platforms are not a technical backdrop: they reconfigure the brand–public relation; history is a media-power map.",
        "canvas_activity": "Recursos: glosario de términos clave",
        "thesis": "U1 abre el track situando Internet/RRSS como cambio de relación, no como nostalgia tecnológica.",
        "grounded_path": [
            "Nobile et al. 2021 — digital fashion research as communication/transformation field (Nobile 2021, 2) [SAFE]",
            "United Nations Environment Programme 2023 — communication as part of fashion's consumption system (United Nations Environment Programme 2023, 26) [SAFE]",
        ],
        "athanor": "Synergies: platformization of fashion communication; Gaps: no dedicated general Internet-history monograph in course vault — declare limit.",
        "cite_forms": "(Nobile 2021) (United Nations Environment Programme 2023)",
        "refs_es": [
            "Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education*. https://doi.org/10.1080/17543266.2021.1931476.",
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. https://doi.org/10.59117/20.500.11822/42819.",
        ],
    },
    {
        "id": "U2",
        "slug_es": "u2-estrategias-comunicacion-digital",
        "slug_en": "u2-digital-communication-strategies",
        "title_es": "U2 · Estrategias de comunicación digital",
        "title_en": "U2 · Digital communication strategies",
        "contenidos": "Comunicación digital",
        "competencies": ["CON4", "COMP2", "HAB12"],
        "master_idea_es": "Una estrategia digital de moda es un sistema de presencia — voz, formatos, métricas e hipótesis — no un calendario de posts.",
        "master_idea_en": "A fashion digital strategy is a presence system — voice, formats, metrics, hypotheses — not a posting calendar.",
        "canvas_activity": "Actividad 10 ptos — Diseño y análisis de una estrategia digital para marca de moda",
        "thesis": "U2 convierte el mapa histórico en un plan evaluable (COMP2).",
        "grounded_path": [
            "UNEP 2023 — communicators make sustainable options attractive beyond information-only messages (United Nations Environment Programme 2023, 49) [SAFE]",
            "Nobile et al. 2021 — digital transformation reshapes fashion communication facets (Nobile 2021, 2) [SAFE]",
        ],
        "athanor": "Synergies: brand coherence across platforms; Gaps: tool-specific KPI manuals still open.",
        "cite_forms": "(United Nations Environment Programme 2023) (Nobile 2021)",
        "refs_es": [
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. https://doi.org/10.59117/20.500.11822/42819.",
            "Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education*. https://doi.org/10.1080/17543266.2021.1931476.",
        ],
    },
    {
        "id": "U3",
        "slug_es": "u3-marketing-publicidad",
        "slug_en": "u3-marketing-advertising",
        "title_es": "U3 · Marketing y publicidad en nuevos medios",
        "title_en": "U3 · Marketing and advertising in new media",
        "contenidos": "Marketing y publicidad en nuevos medios.",
        "competencies": ["HAB5", "CON4", "COMP2"],
        "master_idea_es": "La campaña de moda en red es trabajo de visibilidad, divulgación y confianza — no solo creatividad de anuncio.",
        "master_idea_en": "A fashion campaign online is visibility labour, disclosure and trust — not just ad creativity.",
        "canvas_activity": "Actividad 10 ptos — Análisis crítico de una campaña de moda en RRSS",
        "thesis": "U3 es el núcleo crítico del track (mejor corpus SAFE).",
        "grounded_path": [
            "Abidin 2016 — visibility labour on Instagram influencer fashion brands (Abidin 2016, 2) [SAFE]",
            "Alkkiomäki et al. 2024 — CDA of fast fashion legitimation on Instagram (Alkkiomäki 2024, 1) [SAFE — use Alkkiomäki et al.]",
            "Khan et al. 2026 — luxury transparency paradox on TikTok (Khan 2026, 2) [SAFE]",
            "UNEP 2023 — greenwashing / unsubstantiated claims in fashion communication (United Nations Environment Programme 2023, 26) [SAFE]",
        ],
        "athanor": "Synergies: disclosure regimes; Gaps: Spain 2025 influencer code is self-regulatory — not EU law.",
        "cite_forms": "(Abidin 2016) (Alkkiomäki 2024) (Khan 2026) (United Nations Environment Programme 2023)",
        "refs_es": [
            "Abidin, Crystal. 2016. “Visibility Labour: Engaging with Influencers’ Fashion Brands and #OOTD Advertorial Campaigns on Instagram.” *Media International Australia*. https://doi.org/10.1177/1329878X16665177.",
            "Alkkiomäki, Tiia, Henna Syrjälä, Hanna Leipämaa-Leskinen, and Elina Ellonen. 2024. “Critical Discourse Analysis of Fast Fashion Companies’ Legitimation Strategies on Instagram.” *Consumption Markets & Culture*. https://doi.org/10.1080/10253866.2024.2390864.",
            "Khan, Nayla, Valentina Mazzoli, Giampaolo Viglia, and Michaela Merk. 2026. “Luxury Fashion’s Transparency Paradox on TikTok: Balancing Openness and Exclusivity.” *Journal of Advertising Research*. https://doi.org/10.1080/00218499.2026.2645375.",
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. https://doi.org/10.59117/20.500.11822/42819.",
        ],
    },
    {
        "id": "U4",
        "slug_es": "u4-creatividad-contenido",
        "slug_en": "u4-creativity-content",
        "title_es": "U4 · Creatividad y contenido digital",
        "title_en": "U4 · Creativity and digital content",
        "contenidos": "Creatividad aplicada a la comunicación social digital",
        "competencies": ["HAB12", "HAB5", "COMP8"],
        "master_idea_es": "El contenido alineado a marca exige oficio narrativo y criterio de engagement sin vaciar la crítica.",
        "master_idea_en": "Brand-aligned content needs narrative craft and engagement judgement without emptying critique.",
        "canvas_activity": "Actividad 10 ptos — Propuesta creativa de contenido para RRSS",
        "thesis": "U4 lleva HAB12 al studio: planificar contenido editorial bajo presión de plataforma.",
        "grounded_path": [
            "Yu et al. 2024 — AI/CGI influencers and engagement through emotional display (Yu 2024, 3) [SAFE]",
            "Nobile et al. 2021 — field map for digital fashion before/beyond marketing (Nobile 2021, 2) [SAFE]",
            "status open — non-synthetic brand storytelling monograph not Ahmes-SAFE in course project",
        ],
        "athanor": "Synergies: CGI content as engagement apparatus; Gaps: Scolari/transmedia only in official guía biblio, not Ahmes.",
        "cite_forms": "(Yu 2024) (Nobile 2021)",
        "refs_es": [
            "Yu, Joanne, Astrid Dickinger, Kevin Kam Fung So, and Roman Egger. 2024. “Artificial Intelligence-Generated Virtual Influencer: Examining the Effects of Emotional Display on User Engagement.” *Journal of Retailing and Consumer Services*. https://doi.org/10.1016/j.jretconser.2023.103560.",
            "Nobile, Tekila Harley, Alice Noris, Nadzeya Kalbaska, and Lorenzo Cantoni. 2021. “A Review of Digital Fashion Research: Before and Beyond Communication and Marketing.” *International Journal of Fashion Design, Technology and Education*. https://doi.org/10.1080/17543266.2021.1931476.",
        ],
    },
    {
        "id": "U5",
        "slug_es": "u5-herramientas-datos",
        "slug_en": "u5-tools-data",
        "title_es": "U5 · Herramientas digitales y análisis de datos",
        "title_en": "U5 · Digital tools and data analysis",
        "contenidos": "Comunicación digital",
        "competencies": ["CON4", "COMP8"],
        "master_idea_es": "Los datos no hablan solos: cada métrica es una decisión sobre qué cuenta como éxito de marca.",
        "master_idea_en": "Data do not speak alone: every metric is a decision about what counts as brand success.",
        "canvas_activity": "Actividades (sin puntuación listada en extracto Canvas)",
        "thesis": "U5 enseña a leer dashboards como instrumentos políticos de medición.",
        "grounded_path": [
            "UNEP 2023 — communication metrics/claims must be substantiated; misinformation ubiquity (United Nations Environment Programme 2023, 26) [SAFE]",
            "status open — no SAFE Ahmes source dedicated to fashion-analytics tooling pedagogy",
        ],
        "athanor": "Gaps: KPI ethics / dashboard literacy still [BIBLIO-GAP] for tool manuals.",
        "cite_forms": "(United Nations Environment Programme 2023)",
        "refs_es": [
            "United Nations Environment Programme. 2023. *The Sustainable Fashion Communication Playbook*. https://doi.org/10.59117/20.500.11822/42819.",
        ],
    },
    {
        "id": "U6",
        "slug_es": "u6-futuro-comunicacion-digital",
        "slug_en": "u6-future-digital-communication",
        "title_es": "U6 · Futuro de la comunicación digital",
        "title_en": "U6 · Future of digital communication",
        "contenidos": "Presente y futuro de la comunicación digital",
        "competencies": ["CON4", "COMP8", "HAB5"],
        "master_idea_es": "IA y R.A. cambian la escena de moda digital; autenticidad, cuerpo y divulgación son problemas de estudio, no adornos.",
        "master_idea_en": "AI and AR change the digital fashion stage; authenticity, body and disclosure are studio problems, not ornaments.",
        "canvas_activity": "Actividad 10 ptos — Exploración de tecnologías emergentes aplicadas a la moda",
        "thesis": "U6 cierra el arco hacia CD II (avatar/AR) sin VTON.",
        "grounded_path": [
            "Yu et al. 2024 — AI-generated virtual influencers and engagement (Yu 2024, 3) [SAFE]",
            "Lamerichs 2024 — digital fashion/avatars entangled with datafication and platformization (Lamerichs 2024, 3) [SAFE]",
        ],
        "athanor": "Synergies: virtual influencer disclosure; Gaps: Virtual vs Human coat BIBLIO-GAP — excluded.",
        "cite_forms": "(Yu 2024) (Lamerichs 2024)",
        "refs_es": [
            "Yu, Joanne, Astrid Dickinger, Kevin Kam Fung So, and Roman Egger. 2024. “Artificial Intelligence-Generated Virtual Influencer: Examining the Effects of Emotional Display on User Engagement.” *Journal of Retailing and Consumer Services*. https://doi.org/10.1016/j.jretconser.2023.103560.",
            "Lamerichs, Nicolle. 2024. “Towards a Responsible Metaverse.” https://doi.org/10.14361/9783839474624-013.",
        ],
    },
]


def lesson_md(u: dict, lang: str, tuning_record: str | None, b1_paragraph: str | None) -> str:
    if lang == "es":
        title, slug, idea, path_course = u["title_es"], u["slug_es"], u["master_idea_es"], "nuevos-medios-moda"
        permalink = f"/lessons/es/nuevos-medios-moda/{slug}/"
        objectives = f"""Al final de esta unidad podrás:

- Relacionar el tema con el ancla oficial de CONTENIDOS **{u['contenidos']}**.
- Articular la idea central del Masterclass en voz propia.
- Completar el entregable Canvas: {u['canvas_activity']}.
- Nombrar qué evidencia SAFE sostiene el claim y qué queda abierto."""
        b1_heading = "## Masterclass — idea central"
        b2_heading = "## Estudio (Canvas / B2)"
        b3_heading = "## Problema individual (B3)"
        refs_h = "## Referencias"
        ai_h = "## Autoría asistida por IA"
        lang_note = ""
        status = "en-proceso" if b1_paragraph else "scaffold"
        b2 = f"""Modalidad **online**. Entrega en Campus Virtual.

**Actividad:** {u['canvas_activity']}

Tres capas obligatorias en la entrega: **estrategia · crítica · estudio**. No entregues solo capturas de pantalla sin criterio."""
        b3 = "Resuelve en solitario un mini-caso o quiz de cierre de unidad (detalle en Canvas). Evidencia individual — no grupal."
        critic = "La crítica de plataforma (poder, datos, trabajo, divulgación, sostenibilidad) atraviesa esta unidad; no se aplaza a un módulo ético separado."
    else:
        title, slug, idea, path_course = u["title_en"], u["slug_en"], u["master_idea_en"], "nuevos-medios-moda"
        permalink = f"/lessons/en/nuevos-medios-moda/{slug}/"
        objectives = f"""By the end of this unit you will be able to:

- Map the topic to official CONTENIDOS anchor **{u['contenidos']}**.
- State the Masterclass claim in your own words.
- Complete the Canvas deliverable described on the Spanish track (teaching language = ES).
- Name which SAFE evidence supports the claim and what remains open."""
        b1_heading = "## Masterclass — core idea"
        b2_heading = "## Studio (Canvas / B2)"
        b3_heading = "## Individual problem (B3)"
        refs_h = "## References"
        ai_h = "## AI-assisted authorship"
        lang_note = "\n\n**Teaching language for this course is Spanish.** Use the ES lesson for assessed work; this EN page is the S./E. twin.\n"
        status = "scaffold"
        b2 = f"""**Online.** Submission in Campus Virtual (see ES lesson / Canvas).\n\n**Activity:** {u['canvas_activity']}\n\nKeep three layers visible: **strategy · critique · studio**."""
        b3 = "Individual mini-case or unit quiz in Canvas."
        critic = "Platform critique (power, data, labour, disclosure, sustainability) runs through this unit — not a separate ethics week."
        b1_paragraph = None  # EN twin: no separate Thessia pass this wave

    comps = ", ".join(u["competencies"])
    refs = "\n".join(f"- {r}" for r in u["refs_es"])
    if b1_paragraph:
        b1_body = b1_paragraph.strip() + "\n"
        if tuning_record:
            b1_body += f"""
{{% if site.publication.publish_internal_metadata %}}
<!-- curriculum-internal:
tuning_record: {tuning_record}
contenidos: {u['contenidos']}
competencies: [{comps}]
project_slug: profield-nuevos-medios-moda-2026-27
-->
{{% endif %}}
"""
    else:
        b1_body = f"*{idea}*\n\n*(Cold B1 subsection pending / twin — see ES lesson for forged prose.)*\n"

    return f"""---
layout: lesson
title: '{title}'
title_en: '{u['title_en']}'
slug: {slug}
date: {TODAY}
author: 'Rubén Vega Balbás, PhD'
lang: {lang}
permalink: {permalink}
description: '{idea[:160]}'
status: {status}
tags: [nuevos-medios-moda, {u['id'].lower()}, moda-digital, rrss]
master_idea: '{idea.replace("'", "’")}'
practice_anchor: '{u["canvas_activity"].replace("'", "’")}'
---

<!-- prettier-ignore-start -->

## 📋 Tabla de contenidos
{{: .no_toc }}
- TOC
{{:toc}}

<!-- prettier-ignore-end -->
{lang_note}
## Objetivos de aprendizaje

{objectives}

---

{b1_heading}

{b1_body}

### Perspectiva crítica

{critic}

---

{b2_heading}

{b2}

---

{b3_heading}

{b3}

---

{refs_h}

{refs}

---

{ai_h}

Esta lección forma parte del track Nuevos medios (guía UEM 2026-27, REF 4d3415b1).
Los párrafos de Masterclass en ES se borraron en frío con el harness de autoría
asistida del estudio y se revisaron antes de publicarse; el HTML estudiantil no
nombra herramientas internas. Ver declaración del sitio en `/ai-declaration/`
cuando esté enlazada.
"""


def write_prompt(u: dict, record: Path) -> None:
    grounded = "\n".join(f"- {g}" for g in u["grounded_path"])
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

MAIN IDEA:
{u['title_es']}
{u['master_idea_es']}

THESIS (where this idea sits in the course flow):
{u['thesis']}

GROUNDED PATH (cite only these (Author Year) forms, never invent one):
{grounded}

ATHANOR SYNERGIES:
{u['athanor']}

CITATION RULE — non-negotiable:
Every (Author, Year) you emit MUST match one of: {u['cite_forms']}.
Do not invent a name, date, or page. If a claim needs a citation not on the list,
drop it or rephrase as course hypothesis without fake cites.

Return ONLY the paragraph (with [S1]… markers). No preamble. No headings.
"""
    brief = f"""# BRIEF — NM {u['id']} · Masterclass idea 1

**Course:** Nuevos medios: RRSS y plataformas virtuales (UEM)
**Unit:** {u['id']} · {u['title_es']}
**CONTENIDOS:** {u['contenidos']}
**Competencies:** {', '.join(u['competencies'])}
**project_slug:** profield-nuevos-medios-moda-2026-27

## (a) Thesis
{u['thesis']}

## (b) Grounded path
{grounded}

## (c) Athanor findings
{u['athanor']}

## Allowed citation forms
{u['cite_forms']}
"""
    (record / "prompt.md").write_text(prompt)
    (record / "BRIEF.md").write_text(brief)


def run_thessia(u: dict) -> dict:
    rid = f"{TODAY}-{uuid.uuid4().hex[:8]}-nm-{u['id'].lower()}-idea1"
    record = MEMORY / rid
    record.mkdir(parents=True, exist_ok=True)
    write_prompt(u, record)
    out = record / "thessia-raw.md"
    cmd = [
        str(PY),
        str(THESSIA),
        "--prompt",
        (record / "prompt.md").read_text(),
        "--out",
        str(out),
        "--brief",
        str(record / "BRIEF.md"),
        "--model",
        "thessia-scholar-v3",
        "--num-predict",
        "512",
        "--expected-sentences",
        "4",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    (record / "generate.log").write_text(proc.stdout + "\n---STDERR---\n" + proc.stderr)
    result = {
        "unit": u["id"],
        "record": rid,
        "exit_code": proc.returncode,
        "raw_path": str(out),
        "rejected": (record / "thessia-raw.md.rejected").exists(),
    }
    raw = ""
    if out.exists():
        raw = out.read_text()
    elif (record / "thessia-raw.md.rejected").exists():
        raw = (record / "thessia-raw.md.rejected").read_text()
    # strip [Sn] markers for integration
    integrated = raw
    for i in range(1, 8):
        integrated = integrated.replace(f"[S{i}]", "").replace(f"[s{i}]", "")
    integrated = "\n".join(line.rstrip() for line in integrated.strip().splitlines())
    (record / "integrated.md").write_text(integrated + "\n")
    # light evaluation stub — human axes filled after
    eval_md = f"""# Evaluation — {u['id']} idea 1

**Exit code:** {proc.returncode}
**Rejected sidecar:** {result['rejected']}

| Axis | Score | Note |
| --- | --- | --- |
| Sentence-role fidelity | PENDING | operator review |
| Voice | PENDING | |
| Concreteness | PENDING | |
| Citation shape | PENDING | CI3 via wrapper |
| Antilism-in-practice | PENDING | |
| Teenager readable | PENDING | |

Amendments: see amendments.diff after review.
"""
    (record / "evaluation.md").write_text(eval_md)
    (record / "provenance.json").write_text(
        json.dumps(
            {
                "course": "nuevos-medios-moda",
                "unit": u["id"],
                "project_slug": "profield-nuevos-medios-moda-2026-27",
                "contenidos": u["contenidos"],
                "model": "thessia-scholar-v3",
            },
            indent=2,
        )
    )
    result["integrated"] = integrated
    result["raw_len"] = len(raw)
    return result


def main() -> None:
    results = []
    for u in UNITS:
        print(f"=== Thessia {u['id']} ===", flush=True)
        r = run_thessia(u)
        results.append(r)
        print(f"exit={r['exit_code']} rejected={r['rejected']} chars={r['raw_len']}", flush=True)

        es_dir = DC / "docs/lessons/es/nuevos-medios-moda" / u["slug_es"]
        en_dir = DC / "docs/lessons/en/nuevos-medios-moda" / u["slug_en"]
        es_dir.mkdir(parents=True, exist_ok=True)
        en_dir.mkdir(parents=True, exist_ok=True)
        para = r["integrated"] if r["exit_code"] == 0 and r["integrated"].strip() else None
        (es_dir / "index.md").write_text(lesson_md(u, "es", r["record"], para))
        (en_dir / "index.md").write_text(lesson_md(u, "en", None, None))

    (DC / "digital-creativity-pedagogy/forge/NM-THESSIA-PERFORMANCE.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False)
    )
    print("DONE", len(results), "units")


if __name__ == "__main__":
    main()
