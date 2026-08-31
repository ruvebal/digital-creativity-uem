"""
Shared design-tokens loader for fractal-architect renderers.

Rule: no renderer script may hardcode a color literal. Every RGB value used
to paint a pixel is read from fractal-render-tokens.json, keyed by the
render brief's palette_hint — so the brief's stated intent and the actual
pixels can never silently diverge.

Author: Rubén Vega Balbás PhD (ECSIT / UDIT)
"""
from __future__ import annotations

import json
from pathlib import Path

_TOKENS_PATH = Path(__file__).parent / "fractal-render-tokens.json"


def load_palette(palette_hint: str) -> dict:
    tokens = json.loads(_TOKENS_PATH.read_text(encoding="utf-8"))
    palettes = tokens.get("palettes", {})
    if palette_hint not in palettes:
        available = ", ".join(repr(k) for k in palettes)
        raise SystemExit(
            f"Refusing to render: no design-token palette for palette_hint={palette_hint!r} "
            f"in {_TOKENS_PATH.name}. Available: {available}"
        )
    return palettes[palette_hint]
