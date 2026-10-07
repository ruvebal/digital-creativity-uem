#!/usr/bin/env python3
"""EX9 — inject rights-safe deck figures into Wave-1 Masterclass (EN + ES when present)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FIGURES = json.loads((ROOT / "docs/_data/lesson_figures.json").read_text())

# lesson path relative to docs/lessons → deck key in lesson_figures.json
TARGETS = [
    ("en/digital-creativity-i/i-1-digital-images/index.md", "i-1-fashion-image"),
    ("en/digital-creativity-i/i-2-2d-drawing/index.md", "i-2-2d-drawing"),
    ("en/digital-creativity-i/i-3-color-bitmaps/index.md", "i-3-color-bitmaps"),
    ("en/digital-creativity-i/i-4-effects/index.md", "i-4-effects"),
    ("en/digital-creativity-i/i-5-three-dimensional-form/index.md", "i-5-three-dimensional-form"),
    ("en/master-lectures/fashion-image-analysis/index.md", "fashion-image-analysis"),
    ("es/creacion-digital-i/i-1-imagenes-digitales/index.md", "i-1-fashion-image"),
    ("es/creacion-digital-i/i-2-dibujo-2d/index.md", "i-2-2d-drawing"),
    ("es/creacion-digital-i/i-3-color-bitmaps/index.md", "i-3-color-bitmaps"),
    ("es/creacion-digital-i/i-4-efectos/index.md", "i-4-effects"),
    ("es/creacion-digital-i/i-5-forma-tridimensional/index.md", "i-5-three-dimensional-form"),
]


def figure_block(deck: str, slide: str, fig: dict) -> str:
    src = fig["src"]
    # lesson_figures src may already be site-absolute (/assets/...)
    if src.startswith("http"):
        img_src = src
        img_tag = f'<img src="{img_src}" alt="{fig["alt"]}" loading="lazy" decoding="async">'
    else:
        img_tag = (
            f'<img src="{{{{ \'{src}\' | relative_url }}}}" '
            f'alt="{fig["alt"]}" loading="lazy" decoding="async">'
        )
    return (
        f'<figure class="lesson-figure" id="figure-{slide}" markdown="0">\n'
        f"{img_tag}\n"
        f"<figcaption>"
        f'{{% include lesson-figure.html deck="{deck}" slide="{slide}" %}}'
        f"</figcaption>\n"
        f"</figure>\n"
    )


def pick_slides(deck: str) -> list[str]:
    figs = FIGURES.get(deck, {})
    # Prefer masterclass-1..N then analysis-model; need ≥ half ideas ≈ ≥3 for 6-idea units
    prefer = [f"masterclass-{i}" for i in range(1, 7)] + ["analysis-model", "cover"]
    out = [s for s in prefer if s in figs]
    # At least 3 if available, else all preferred hits
    return out[: max(3, min(6, len(out)))]


def inject(path: Path, deck: str) -> None:
    text = path.read_text()
    if "lesson-figure.html" in text:
        print("skip (already has figures)", path)
        return
    slides = pick_slides(deck)
    if not slides:
        print("skip (no figures)", deck)
        return
    blocks = "\n".join(figure_block(deck, s, FIGURES[deck][s]) for s in slides)
    # Insert after Masterclass heading line
    if not re.search(r"^## Masterclass\b", text, re.M):
        print("skip (no Masterclass)", path)
        return
    text2, n = re.subn(
        r"(^## Masterclass\b[^\n]*\n)",
        r"\1\n" + blocks + "\n",
        text,
        count=1,
        flags=re.M,
    )
    if n != 1:
        raise SystemExit(f"inject failed: {path}")
    path.write_text(text2)
    print("figures", path.relative_to(ROOT), "→", slides)


def main() -> None:
    base = ROOT / "docs/lessons"
    for rel, deck in TARGETS:
        inject(base / rel, deck)


if __name__ == "__main__":
    main()
