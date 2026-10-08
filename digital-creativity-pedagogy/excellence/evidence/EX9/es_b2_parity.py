#!/usr/bin/env python3
"""EX9 — ES B2 card parity from EN Labs (I.1–I.5). Keeps EX8 English field labels."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
EN = ROOT / "docs/lessons/en/digital-creativity-i"
ES = ROOT / "docs/lessons/es/creacion-digital-i"

# EN lesson slug → ES lesson slug
MAP = {
    "i-1-digital-images": "i-1-imagenes-digitales",
    "i-2-2d-drawing": "i-2-dibujo-2d",
    "i-3-color-bitmaps": "i-3-color-bitmaps",
    "i-4-effects": "i-4-efectos",
    "i-5-three-dimensional-form": "i-5-forma-tridimensional",
}

INTRO_ES = (
    "*Bloque de sesión · Una diapositiva geométrica anuncia el Lab: **dos** ejercicios. "
    "Todo lo que produzcas en Lab entra en tu **índice de portfolio**. "
    "Los Labs practican ideas de Masterclass y alimentan el oficio ACT — no son un segundo canal evaluable de Campus Virtual.*\n\n"
)


def extract_lab(text: str) -> str | None:
    m = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", text, re.M)
    return m.group(0) if m else None


def localize(lab: str) -> str:
    lab = re.sub(r"^### Exercise ", "### Ejercicio ", lab, flags=re.M)
    lab = lab.replace("/assignments/en/", "/assignments/es/")
    # Replace EN intro paragraph(s) before first exercise with ES intro
    lab = re.sub(
        r"^## Lab \(Portfolio\)\n+[\s\S]*?(?=^### Ejercicio )",
        "## Lab (Portfolio)\n\n" + INTRO_ES,
        lab,
        count=1,
        flags=re.M,
    )
    return lab


def main() -> None:
    for en_slug, es_slug in MAP.items():
        en_path = EN / en_slug / "index.md"
        es_path = ES / es_slug / "index.md"
        en_lab = extract_lab(en_path.read_text())
        if not en_lab:
            raise SystemExit(f"missing EN lab: {en_slug}")
        es_text = es_path.read_text()
        if not re.search(r"^## Lab \(Portfolio\)\n", es_text, re.M):
            raise SystemExit(f"missing ES lab heading: {es_slug}")
        new_lab = localize(en_lab)
        es_text2, n = re.subn(
            r"^## Lab \(Portfolio\)\n[\s\S]*?(?=^## )",
            new_lab,
            es_text,
            count=1,
            flags=re.M,
        )
        if n != 1:
            raise SystemExit(f"replace failed: {es_slug}")
        es_path.write_text(es_text2)
        print("ES B2", es_slug)


if __name__ == "__main__":
    main()
