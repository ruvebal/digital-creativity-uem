#!/usr/bin/env python3
"""
Escape-time Julia renderer driven by fractal-architect render brief (§11).

Reads verified_formula governance from render-brief.private.json; implements
p_c(z)=z^2+c only when brief confirms EXACT iteration law from Drakopoulos oracle.
Writes PNG + provenance sidecar JSON (traceability).

Author: Rubén Vega Balbás PhD (ECSIT / UDIT)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from _fractal_tokens import load_palette
from _png_writer import write_rgb_png


def _parse_c_param(envelope: dict[str, Any]) -> complex:
    cp = envelope.get("c_parameter") or {}
    return complex(float(cp.get("real", -0.7269)), float(cp.get("imag", 0.1889)))


def _assert_quadratic_map(brief: dict[str, Any]) -> None:
    if brief.get("fidelity_status") not in ("EXACT", "USABLE_WITH_REPAIR"):
        raise SystemExit(
            f"Refusing to render: fidelity_status={brief.get('fidelity_status')}"
        )
    latex = brief.get("verified_formula") or ""
    if "z^2" not in latex.replace(" ", "") and "z^{2}" not in latex:
        raise SystemExit(
            "Refusing to render: verified_formula is not the quadratic Julia map "
            f"(expected z^2 in LaTeX, got {latex!r})"
        )
    prov = brief.get("provenance") or {}
    if prov.get("oracle_equation_id") != "eq-1":
        raise SystemExit(
            "Refusing to render: primary provenance must be oracle eq-1 (iteration law)"
        )


def escape_time_julia(
    width: int,
    height: int,
    *,
    c: complex,
    max_iter: int,
    bailout: float,
    viewport: dict[str, float],
) -> list[list[int]]:
    x_min = float(viewport.get("x_min", -1.5))
    x_max = float(viewport.get("x_max", 1.5))
    y_min = float(viewport.get("y_min", -1.5))
    y_max = float(viewport.get("y_max", 1.5))

    grid: list[list[int]] = []
    for py in range(height):
        row: list[int] = []
        zy = y_min + (y_max - y_min) * py / max(height - 1, 1)
        for px in range(width):
            zx = x_min + (x_max - x_min) * px / max(width - 1, 1)
            z = complex(zx, zy)
            n = 0
            while abs(z) <= bailout and n < max_iter:
                z = z * z + c
                n += 1
            row.append(n)
        grid.append(row)
    return grid


def iter_to_rgb(n: int, max_iter: int, palette: dict) -> tuple[int, int, int]:
    if n >= max_iter:
        return tuple(palette["bounded_rgb"])
    t = n / max_iter
    start = palette["exterior_start_rgb"]
    end = palette["exterior_end_rgb"]
    r = int(start[0] + (end[0] - start[0]) * t)
    g = int(start[1] + (end[1] - start[1]) * t)
    b = int(start[2] + (end[2] - start[2]) * t)
    return (r, g, b)


def write_png(path: Path, grid: list[list[int]], max_iter: int, palette: dict) -> None:
    rows = [[iter_to_rgb(n, max_iter, palette) for n in row] for row in grid]
    write_rgb_png(path, rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Julia set from render brief")
    parser.add_argument("brief", type=Path, help="render-brief.private.json")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--width", type=int, default=800)
    parser.add_argument("--height", type=int, default=800)
    args = parser.parse_args()

    brief = json.loads(args.brief.expanduser().read_text(encoding="utf-8"))
    _assert_quadratic_map(brief)

    envelope = brief.get("parameter_envelope") or {}
    max_iter = int(envelope.get("iterations", [256])[-1])
    bailout = float(envelope.get("bailout_radius", [4.0])[-1])
    c = _parse_c_param(envelope)
    viewport = envelope.get("viewport") or {}

    grid = escape_time_julia(
        args.width,
        args.height,
        c=c,
        max_iter=max_iter,
        bailout=bailout,
        viewport=viewport,
    )

    palette = load_palette(brief.get("palette_hint") or "")

    out_png = args.output.expanduser().resolve()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    write_png(out_png, grid, max_iter, palette)

    sidecar = out_png.with_suffix(".provenance.json")
    sidecar.write_text(
        json.dumps(
            {
                "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "renderer": "render_julia_escape_time.py",
                "verified_formula": brief.get("verified_formula"),
                "fidelity_status": brief.get("fidelity_status"),
                "grammar": brief.get("grammar"),
                "seed": brief.get("seed"),
                "parameters": {
                    "c": {"real": c.real, "imag": c.imag},
                    "max_iter": max_iter,
                    "bailout": bailout,
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

    import hashlib

    h = hashlib.sha256()
    h.update(out_png.read_bytes())
    data = json.loads(sidecar.read_text(encoding="utf-8"))
    data["output_png_sha256"] = h.hexdigest()
    sidecar.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({"png": str(out_png), "provenance": str(sidecar)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
