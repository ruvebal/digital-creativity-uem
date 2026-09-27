#!/usr/bin/env python3
"""Rebuild NM U1–U3 Reveal decks from unit-enrichment MAIN-IDEAS.yml (no Thessia).

Usage (from any cwd):
  ~/src/ahmes/.venv/bin/python \\
    digital-creativity-pedagogy/forge/nm_rebuild_decks.py
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

DC = Path(__file__).resolve().parents[2]
ENRICH = DC / "digital-creativity-pedagogy/forge/unit-enrichment"
DECK_ROOT = DC / "docs/tracks/es/uem/2627-nm"

GEO = {
    "analysis": "/assets/images/fractal-pass-track/uem-pass-01-structure-5218b595b4fa.svg",
    "lab": "/assets/images/fractal-pass-track/uem-pass-04-practice-4a190e098ca6.svg",
    "outro": "/assets/images/fractal-pass-track/uem-lsystem-pass-06-coherence-9a61a10b6e79.svg",
}

QUOTES_BY_CHICAGO = {
    "(Nobile 2021, 294)": (
        "The digital transformation has impacted all the facets of fashion. "
        "First of all fashion communication and marketing, through the adoption "
        "of digital tools creates a fertile ground for the improvement of business "
        "and customer relationships"
    ),
    "(United Nations Environment Programme 2023, 27)": (
        "Ultimately this is about the sector's 'brainprint' and not just its footprint; "
        "about the influence what it puts out into the world has on consumption"
    ),
    "(United Nations Environment Programme 2023, 49)": (
        "this is about communicators using their skills and budgets to make the more "
        "sustainable option the most attractive one"
    ),
    "(United Nations Environment Programme 2023, 26)": (
        "Indeed, misinformation and greenwashing has become so ubiquitous, a 2020 study "
        "by the European Commission found 53.3% of environmental claims communicated in "
        "the EU at large were vague, misleading or unfounded"
    ),
}

NOBILE_HISTORY = (
    "Throughout history, technological advancements have shaped the nature of fashion: "
    "the first industrial revolution contributed to the mechanisation of fashion manufacture "
    "by exploiting water and steam power, the second revolution accelerated fashion production "
    "through the invention of electricity"
)

UNITS = {
    "U1": {
        "slug": "u1-historia-nuevos-medios",
        "title": "U1 · Historia y evolución de los nuevos medios",
        "master": (
            "Internet y las plataformas no son un fondo técnico: reconfiguran la relación "
            "marca–público; la historia es un mapa de poder mediático."
        ),
        "contenidos": "Historia de Internet",
        "theme": "¿Qué campaña reescribió más el mapa de poder: PayUp o Levi’s — y por qué?",
        "lab1": "Línea de tiempo: ≥2 campañas del banco (ranks 1,5,6,8,9) + hitos de medios.",
        "lab2": "5 términos del glosario, cada uno anclado a una campaña del ledger (no apps sueltas).",
        "history_quote_for_idea": 1,
    },
    "U2": {
        "slug": "u2-estrategias-comunicacion-digital",
        "title": "U2 · Estrategias de comunicación digital",
        "master": (
            "Una estrategia digital de moda es un sistema de presencia — voz, formatos, "
            "métricas e hipótesis — no un calendario de posts."
        ),
        "contenidos": "Comunicación digital",
        "theme": "¿Qué cuenta como éxito de marca en tu dashboard — y qué queda invisible?",
        "lab1": "Boceto de sistema de presencia: voz · formatos · KPI · hipótesis de fallo (modelo Action Works).",
        "lab2": "Audita un claim (Levi’s rank 8 o Project Earth rank 9): ¿evidencia UNEP o sentimiento?",
        "history_quote_for_idea": None,
    },
    "U3": {
        "slug": "u3-marketing-publicidad",
        "title": "U3 · Marketing y publicidad en nuevos medios",
        "master": (
            "La campaña de moda en red es trabajo de visibilidad, divulgación y confianza "
            "— y a veces vende posición moral sin mostrar la prenda."
        ),
        "contenidos": "Marketing y publicidad en nuevos medios.",
        "theme": "¿Qué métrica eliges — impresiones Benetton o firmas/USD PayUp — y por qué?",
        "lab1": "Elige ranks 5, 8, 1 o 7: Track A/B/C + URL canónica del ledger + métrica vs métrica exigida.",
        "lab2": "En dos frases: ¿por qué PayUp y Benetton no comparten la misma rúbrica de «campaña ética»?",
        "history_quote_for_idea": None,
    },
}


def brief(text: str, n: int = 160) -> str:
    if len(text) <= n:
        return text
    return text[: n - 1].rsplit(" ", 1)[0] + "…"


def write_deck(unit_id: str) -> Path:
    meta = UNITS[unit_id]
    pack_dir = next(ENRICH.glob(f"{unit_id}-*"))
    ideas = yaml.safe_load((pack_dir / "MAIN-IDEAS.yml").read_text())["ideas"]

    slides: list[dict] = [
        {
            "slide_role": "unit_cover",
            "background_kind": "diagram",
            "heading": meta["title"],
            "sentence": meta["master"],
            "prompt": f"CONTENIDOS: {meta['contenidos']}",
            "quote": brief(meta["master"], 120),
            "quote_origin": "tao_invented",
            "semantic_tags": {"themes": ["nuevos-medios", unit_id.lower()]},
        },
        {
            "slide_role": "analysis_opener",
            "background_kind": "geometrical",
            "background_url": GEO["analysis"],
            "heading": "Análisis · lenguaje / medio / soporte",
            "sentence": "Nombra el lenguaje, el medio y el soporte antes de opinar sobre la marca.",
            "caption": "Geometrical · uem-pass-01-structure.svg#5218b595b4fa",
        },
    ]

    for idea in ideas:
        slide: dict = {
            "slide_role": "masterclass",
            "background_kind": "diagram",
            "heading": idea["heading"],
            "sentence": idea["sentence"],
            "prompt": idea.get("case") or "",
        }
        chicago = idea.get("chicago")
        if meta.get("history_quote_for_idea") == idea["id"]:
            text = NOBILE_HISTORY
            chicago = "(Nobile 2021, 294)"
        elif chicago and chicago in QUOTES_BY_CHICAGO:
            text = QUOTES_BY_CHICAGO[chicago]
        elif chicago and idea.get("quote"):
            text = idea["quote"]
        else:
            text = None

        if text and chicago:
            slide["quote"] = brief(text)
            slide["quote_origin"] = "page_verified"
            slide["citation"] = {
                "label": chicago,
                "href": f"/lessons/es/nuevos-medios-moda/{meta['slug']}/#referencias",
            }
        else:
            slide["quote"] = idea["sentence"]
            slide["quote_origin"] = "tao_invented"

        slides.append(slide)

    slides.extend(
        [
            {
                "slide_role": "lab_opener",
                "background_kind": "geometrical",
                "background_url": GEO["lab"],
                "heading": "Laboratorio",
                "sentence": "Dos ejercicios. Todo lo que produzcas entra en tu índice de portfolio / Canvas.",
                "caption": "Geometrical · uem-pass-04-practice.svg#4a190e098ca6",
            },
            {
                "slide_role": "lab_exercise",
                "background_kind": "none",
                "heading": "Ejercicio 1",
                "sentence": meta["lab1"],
                "portfolio_bound": True,
                "portfolio_trace": "Guarda el boceto / análisis en Canvas.",
            },
            {
                "slide_role": "lab_exercise",
                "background_kind": "none",
                "heading": "Ejercicio 2",
                "sentence": meta["lab2"],
                "portfolio_bound": True,
                "portfolio_trace": "Guarda la ficha en Canvas.",
            },
            {
                "slide_role": "outro",
                "background_kind": "geometrical",
                "background_url": GEO["outro"],
                "heading": "Para llevar",
                "sentence": meta["theme"],
                "caption": "Geometrical · uem-lsystem-pass-06-coherence.svg#9a61a10b6e79",
            },
        ]
    )

    content = {
        "unit_label": f"Nuevos medios · {unit_id}",
        "final_event_theme": meta["theme"],
        "media_selection": {
            "unit_id": unit_id,
            "project_id": "nm",
            "collection": "unit-accepted",
            "strategy": "geometrical-first",
            "description": "NM decks: geometrical openers; campaign Caso: from MAIN-IDEAS / ledger ranks.",
        },
        "assets": [],
        "slides": slides,
    }

    deck_dir = DECK_ROOT / meta["slug"]
    data_dir = deck_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "content.json").write_text(
        "---\nlayout: null\n---\n" + json.dumps(content, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    html = f"""---
layout: null
permalink: /tracks/es/uem/2627-nm/{meta['slug']}/
sitemap: false
---
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nuevos medios · {unit_id}</title>
  <link rel="stylesheet" href="{{{{ '/assets/css/reveal.css' | relative_url }}}}">
  <link rel="stylesheet" href="{{{{ '/assets/css/pass-track-deck.css' | relative_url }}}}">
</head>
<body class="student-media-deck" data-content-url="{{{{ '/tracks/es/uem/2627-nm/{meta['slug']}/data/content.json' | relative_url }}}}" data-lesson-url="{{{{ '/lessons/es/nuevos-medios-moda/{meta['slug']}/' | relative_url }}}}">
  <a class="track-back" id="deck-back" href="{{{{ '/lessons/es/nuevos-medios-moda/{meta['slug']}/' | relative_url }}}}" aria-label="Volver a la lección">← Lección</a>
  <div class="reveal"><div class="slides" id="slides"></div></div>
  <script src="{{{{ '/assets/js/reveal.js' | relative_url }}}}"></script>
  <script src="{{{{ '/assets/js/student-media-deck.js' | relative_url }}}}"></script>
</body>
</html>
"""
    (deck_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {deck_dir} ({len(slides)} slides)")
    return deck_dir


def main() -> None:
    for uid in ("U1", "U2", "U3"):
        write_deck(uid)


if __name__ == "__main__":
    main()
