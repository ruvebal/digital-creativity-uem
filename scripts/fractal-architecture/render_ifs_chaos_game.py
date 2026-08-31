#!/usr/bin/env python3
"""
Chaos-game IFS renderer driven by fractal-architect render brief (AFEL §4.1).

Reads the verified Hutchinson-operator iteration law (eq-1, P = ∪ w_i(P))
from render-brief-ifs.private.json and instantiates it with the parameter
envelope's map set; refuses to render if fidelity or provenance don't check
out. Writes PNG + provenance sidecar JSON (traceability).

Author: Rubén Vega Balbás PhD (ECSIT / UDIT)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _fractal_tokens import load_palette
from _png_writer import write_rgb_png


def _assert_hutchinson_law(brief: dict[str, Any]) -> None:
    if brief.get("fidelity_status") not in ("EXACT", "USABLE_WITH_REPAIR"):
        raise SystemExit(
            f"Refusing to render: fidelity_status={brief.get('fidelity_status')}"
        )
    latex = brief.get("verified_formula") or ""
    if "cup" not in latex:
        raise SystemExit(
            "Refusing to render: verified_formula is not a Hutchinson-operator "
            f"union law (expected \\cup in LaTeX, got {latex!r})"
        )
    prov = brief.get("provenance") or {}
    if prov.get("oracle_equation_id") != "eq-1":
        raise SystemExit(
            "Refusing to render: primary provenance must be oracle eq-1 (iteration law)"
        )


def chaos_game(
    width: int,
    height: int,
    *,
    maps: list[dict[str, float]],
    iterations: int,
    warmup_discard: int,
    viewport: dict[str, float],
    seed: int,
) -> list[list[int]]:
    x_min = float(viewport.get("x_min", 0.0))
    x_max = float(viewport.get("x_max", 1.0))
    y_min = float(viewport.get("y_min", 0.0))
    y_max = float(viewport.get("y_max", 1.0))

    weights = [float(m["p"]) for m in maps]
    rng = random.Random(seed)

    counts = [[0] * width for _ in range(height)]
    x, y = 0.5, 0.5
    for i in range(iterations):
        m = rng.choices(maps, weights=weights, k=1)[0]
        x, y = (
            m["a"] * x + m["b"] * y + m["e"],
            m["c"] * x + m["d"] * y + m["f"],
        )
        if i < warmup_discard:
            continue
        if not (x_min <= x <= x_max and y_min <= y <= y_max):
            continue
        px = int((x - x_min) / (x_max - x_min) * (width - 1))
        py = int((1 - (y - y_min) / (y_max - y_min)) * (height - 1))
        counts[py][px] += 1
    return counts


def density_to_rgb(count: int, max_count: int, palette: dict) -> tuple[int, int, int]:
    bg = palette["background_rgb"]
    accent = palette["accent_rgb"]
    if count <= 0 or max_count <= 0:
        return tuple(bg)
    # Log-compressed density so sparse orbit tails stay visible against dense cores.
    t = math.log1p(count) / math.log1p(max_count)
    r = int(bg[0] + (accent[0] - bg[0]) * t)
    g = int(bg[1] + (accent[1] - bg[1]) * t)
    b = int(bg[2] + (accent[2] - bg[2]) * t)
    return (r, g, b)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render an IFS attractor (chaos game) from a render brief"
    )
    parser.add_argument("brief", type=Path, help="render-brief-ifs.private.json")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--width", type=int, default=800)
    parser.add_argument("--height", type=int, default=800)
    args = parser.parse_args()

    brief = json.loads(args.brief.expanduser().read_text(encoding="utf-8"))
    _assert_hutchinson_law(brief)

    envelope = brief.get("parameter_envelope") or {}
    maps = envelope.get("maps") or []
    if not maps:
        raise SystemExit("Refusing to render: parameter_envelope.maps is empty")
    iterations = int(envelope.get("iterations", 60000))
    warmup = int(envelope.get("warmup_discard", 20))
    viewport = envelope.get("viewport") or {}
    seed = int(brief.get("seed", 42))

    counts = chaos_game(
        args.width,
        args.height,
        maps=maps,
        iterations=iterations,
        warmup_discard=warmup,
        viewport=viewport,
        seed=seed,
    )
    max_count = max((max(row) for row in counts), default=0)

    palette = load_palette(brief.get("palette_hint") or "")
    rows = [[density_to_rgb(c, max_count, palette) for c in row] for row in counts]

    out_png = args.output.expanduser().resolve()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    write_rgb_png(out_png, rows)

    sidecar = out_png.with_suffix(".provenance.json")
    sidecar.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "renderer": "render_ifs_chaos_game.py",
                "verified_formula": brief.get("verified_formula"),
                "fidelity_status": brief.get("fidelity_status"),
                "grammar": brief.get("grammar"),
                "seed": seed,
                "parameters": {
                    "iterations": iterations,
                    "warmup_discard": warmup,
                    "maps": maps,
                    "viewport": viewport,
                    "width": args.width,
                    "height": args.height,
                },
                "provenance": brief.get("provenance"),
                "supporting_formulae": brief.get("supporting_formulae"),
                "output_png": str(out_png),
                "output_png_sha256": None,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    h = hashlib.sha256()
    h.update(out_png.read_bytes())
    data = json.loads(sidecar.read_text(encoding="utf-8"))
    data["output_png_sha256"] = h.hexdigest()
    sidecar.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"png": str(out_png), "provenance": str(sidecar)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
