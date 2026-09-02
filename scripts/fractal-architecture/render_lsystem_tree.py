#!/usr/bin/env python3
"""
Parametric L-system turtle-graphics renderer, driven by a fractal-architect
render brief (AFEL §4.1).

Directly implements the verified production rule (Prusinkiewicz &
Lindenmayer, Eq. 8.2, p.187): A(s) -> F(s)[+A(s/R)][-A(s/R)]F(s)A(s/R), as
a recursive turtle walk rather than a generic string-rewriting L-system
engine — this script draws exactly this one verified rule, not an
arbitrary L-system grammar.

Refuses to render unless fidelity_status and provenance check out (same
guard pattern as render_julia_escape_time.py / render_ifs_chaos_game.py).

Author: Rubén Vega Balbás PhD (ECSIT / UDIT)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _fractal_tokens import load_palette
from _png_writer import write_rgb_png


def _assert_verified_lsystem(brief: dict[str, Any]) -> None:
    if brief.get("fidelity_status") not in ("EXACT", "USABLE_WITH_REPAIR"):
        raise SystemExit(
            f"Refusing to render: fidelity_status={brief.get('fidelity_status')}"
        )
    latex = brief.get("verified_formula") or ""
    if "F(s)" not in latex.replace(" ", "") and "F(s)" not in latex:
        raise SystemExit(
            "Refusing to render: verified_formula is not the F(s)-based turtle "
            f"production rule this script implements (got {latex!r})"
        )
    prov = brief.get("provenance") or {}
    if prov.get("oracle_equation_id") != "eq-1":
        raise SystemExit(
            "Refusing to render: primary provenance must be oracle eq-1 (production rule)"
        )


def walk_tree(
    *,
    iterations: int,
    scale_factor_r: float,
    branch_angle_deg: float,
    segment_length_base: float,
) -> list[tuple[float, float, float, float, int]]:
    """Recursively expand A(s) -> F(s)[+A(s/R)][-A(s/R)]F(s)A(s/R).

    Returns a list of (x0, y0, x1, y1, depth) segments in world coordinates
    (trunk starts at origin, pointing straight up).
    """
    segments: list[tuple[float, float, float, float, int]] = []

    def draw_a(x: float, y: float, heading_deg: float, s: float, depth: int) -> None:
        if depth <= 0 or s < segment_length_base * 0.02:
            return
        rad = math.radians(heading_deg)
        # F(s): forward
        x1 = x + s * math.cos(rad)
        y1 = y + s * math.sin(rad)
        segments.append((x, y, x1, y1, depth))
        # [+A(s/R)]
        draw_a(x1, y1, heading_deg + branch_angle_deg, s / scale_factor_r, depth - 1)
        # [-A(s/R)]
        draw_a(x1, y1, heading_deg - branch_angle_deg, s / scale_factor_r, depth - 1)
        # F(s): forward again
        x2 = x1 + s * math.cos(rad)
        y2 = y1 + s * math.sin(rad)
        segments.append((x1, y1, x2, y2, depth))
        # A(s/R): continue straight, same branch
        draw_a(x2, y2, heading_deg, s / scale_factor_r, depth - 1)

    draw_a(0.0, 0.0, 90.0, segment_length_base, iterations)
    return segments


def _draw_line(
    grid: list[list[tuple[int, int, int] | None]],
    x0: int, y0: int, x1: int, y1: int,
    color: tuple[int, int, int], width: int,
) -> None:
    """Bresenham line, stamped with a square brush of the given width."""
    dx, dy = abs(x1 - x0), -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    height = len(grid)
    width_px = len(grid[0]) if grid else 0
    half = max(0, width // 2)
    while True:
        for ox in range(-half, half + 1):
            for oy in range(-half, half + 1):
                px, py = x + ox, y + oy
                if 0 <= px < width_px and 0 <= py < height:
                    grid[py][px] = color
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy


def render(
    segments: list[tuple[float, float, float, float, int]],
    *,
    width: int,
    height: int,
    viewport: dict[str, float],
    max_depth: int,
    palette: dict,
) -> list[list[tuple[int, int, int]]]:
    x_min = float(viewport.get("x_min", -1.2))
    x_max = float(viewport.get("x_max", 1.2))
    y_min = float(viewport.get("y_min", -0.05))
    y_max = float(viewport.get("y_max", 2.0))
    bg = tuple(palette["background_rgb"])
    trunk = palette["trunk_rgb"]
    tip = palette["tip_rgb"]

    grid: list[list[Any]] = [[None] * width for _ in range(height)]

    def to_px(x: float, y: float) -> tuple[int, int]:
        px = int((x - x_min) / (x_max - x_min) * (width - 1))
        py = int((1 - (y - y_min) / (y_max - y_min)) * (height - 1))
        return px, py

    for x0, y0, x1, y1, depth in segments:
        # depth counts DOWN from max_depth at the trunk to ~0 at the tips —
        # invert so t=0 at the trunk (start color) and t=1 at the tips.
        t = 1.0 - max(0.0, min(1.0, depth / max(max_depth, 1)))
        color = tuple(
            int(trunk[i] + (tip[i] - trunk[i]) * t) for i in range(3)
        )
        px0, py0 = to_px(x0, y0)
        px1, py1 = to_px(x1, y1)
        stroke = max(1, int(1 + 3 * (1.0 - t)))
        _draw_line(grid, px0, py0, px1, py1, color, stroke)

    return [[cell if cell is not None else bg for cell in row] for row in grid]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a parametric L-system tree (Eq. 8.2) from a render brief"
    )
    parser.add_argument("brief", type=Path, help="render-brief-lsystem-tree.private.json")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--width", type=int, default=800)
    parser.add_argument("--height", type=int, default=800)
    args = parser.parse_args()

    brief = json.loads(args.brief.expanduser().read_text(encoding="utf-8"))
    _assert_verified_lsystem(brief)

    envelope = brief.get("parameter_envelope") or {}
    iterations = int(envelope.get("iterations", 7))
    r = float(envelope.get("scale_factor_R", 0.72))
    angle = float(envelope.get("branch_angle_deg", 27.0))
    base_len = float(envelope.get("segment_length_base", 1.0))
    viewport = envelope.get("viewport") or {}

    segments = walk_tree(
        iterations=iterations, scale_factor_r=r,
        branch_angle_deg=angle, segment_length_base=base_len,
    )

    palette = load_palette(brief.get("palette_hint") or "")
    rows = render(
        segments, width=args.width, height=args.height,
        viewport=viewport, max_depth=iterations, palette=palette,
    )

    out_png = args.output.expanduser().resolve()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    write_rgb_png(out_png, rows)

    sidecar = out_png.with_suffix(".provenance.json")
    sidecar.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "renderer": "render_lsystem_tree.py",
                "verified_formula": brief.get("verified_formula"),
                "fidelity_status": brief.get("fidelity_status"),
                "grammar": brief.get("grammar"),
                "seed": brief.get("seed"),
                "parameters": {
                    "iterations": iterations, "scale_factor_R": r,
                    "branch_angle_deg": angle, "segment_length_base": base_len,
                    "segments_drawn": len(segments),
                    "viewport": viewport, "width": args.width, "height": args.height,
                },
                "provenance": brief.get("provenance"),
                "supporting_formulae": brief.get("supporting_formulae"),
                "output_png": str(out_png),
                "output_png_sha256": None,
            },
            indent=2, ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    h = hashlib.sha256()
    h.update(out_png.read_bytes())
    data = json.loads(sidecar.read_text(encoding="utf-8"))
    data["output_png_sha256"] = h.hexdigest()
    sidecar.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"png": str(out_png), "provenance": str(sidecar), "segments": len(segments)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
