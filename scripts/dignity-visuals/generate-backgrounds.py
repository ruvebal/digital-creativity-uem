#!/usr/bin/env python3
"""Dignity studio 1.0.0: original geometry, not a cited mathematical model.

Reproducible release: python3 scripts/dignity-visuals/generate-backgrounds.py
Needs rsvg-convert. Each delivery is byte-identical to its native source export.
"""
from pathlib import Path
import hashlib
import json
import math
import random
import shutil
import subprocess
import uuid

VERSION = "1.0.0"
SEED = 20261020
WIDTH, HEIGHT = 2390, 1000
MAX_DEPTH = 5
DATE = "2026-10-20"
ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ROOT / "digital-creativity-pedagogy/dignity/visuals"
DELIVERY = ROOT / "docs/assets/images/dignity/backgrounds"
HEX = Path("/Users/ruvebal/src/.cursor/skills/hex-color-tools/scripts/hex_color_tools.py")
SKILLS = {
    "visual-forger": Path("/Users/ruvebal/src/.cursor/skills/visual-forger/SKILL.md"),
    "fractal-architect": ROOT / "digital-creativity-pedagogy/.cursor/skills/fractal-architect/SKILL.md",
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dark(hex_color):
    return subprocess.check_output(["python3", str(HEX), "invert-lightness", hex_color], text=True).strip()

def path(points):
    return " ".join(f"{x:.2f},{y:.2f}" for x, y in points)

def artwork(site, mode):
    """Two recursive grammars. Static, bounded, no motion or stochastic noise."""
    rng = random.Random(SEED + (100 if site == "tc" else 0))
    paper = "#f2f4f7" if site == "dc" else "#fffaf5"
    ink = "#00295e" if site == "dc" else "#b34a09"
    accent = "#c9c932" if site == "dc" else "#c93532"
    bg = paper if mode == "light" else dark(paper)
    line = ink if mode == "light" else dark(ink)
    accent = accent if mode == "light" else dark(accent)
    title = "Relational folds" if site == "dc" else "Open assemblies"
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
             f'<title>{title}</title>',
             '<desc>Original recursive geometric background with an uninterrupted upper-left field. No text or empirical claim.</desc>',
             '<defs>',
             f'<linearGradient id="surface" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{bg}"/><stop offset="1" stop-color="{line}" stop-opacity=".13"/></linearGradient>',
             f'<linearGradient id="fold" x1="0" y1="0" x2="1" y2=".4"><stop stop-color="{line}" stop-opacity=".015"/><stop offset=".58" stop-color="{line}" stop-opacity=".13"/><stop offset="1" stop-color="{accent}" stop-opacity=".10"/></linearGradient>',
             '<linearGradient id="quiet"><stop offset="0" stop-color="white" stop-opacity="0"/><stop offset=".43" stop-color="white" stop-opacity="0"/><stop offset=".68" stop-color="white"/><stop offset="1" stop-color="white"/></linearGradient>',
             '<mask id="edge"><rect width="2390" height="1000" fill="url(#quiet)"/></mask>',
             '</defs>', f'<rect width="2390" height="1000" fill="{bg}"/>',
             '<rect width="2390" height="1000" fill="url(#surface)"/>',
             '<g mask="url(#edge)">']
    if site == "dc":
        # Fold bands subdivide their separation recursively. The stopping rule
        # is depth=5, exactly 32 bands; no infinity or fractal-dimension claim.
        def fold_band(low, high, depth):
            if depth < MAX_DEPTH:
                split = (low + high) / 2
                fold_band(low, split, depth + 1)
                fold_band(split, high, depth + 1)
                return
            y = low
            spread = high - low
            bend = 760 + 220 * math.sin(low / 440)
            d = f'M 780,{y:.2f} C 1200,{y-120:.2f} 1480,{bend:.2f} 2480,{y-150:.2f} L 2480,{y-150+spread:.2f} C 1480,{bend+spread:.2f} 1200,{y-120+spread:.2f} 780,{y+spread:.2f} Z'
            parts.append(f'<path d="{d}" fill="url(#fold)" stroke="{line}" stroke-opacity=".075" stroke-width="1.1"/>')
        fold_band(-250, 1300, 0)
        for offset in (0, 180, 360):
            parts.append(f'<path d="M 1300,{950-offset} C 1710,{450-offset} 2030,{1150-offset} 2480,{240-offset}" fill="none" stroke="{accent}" stroke-opacity=".28" stroke-width="1.5"/>')
    else:
        # Original recursive triangular tessellation; this is not presented as
        # an instance of a named or source-verified fractal construction.
        def triangles(a, b, c, depth):
            if depth == MAX_DEPTH:
                opacity = rng.uniform(.025, .12)
                fill = accent if rng.random() < .14 else line
                parts.append(f'<polygon points="{path([a,b,c])}" fill="{fill}" fill-opacity="{opacity:.3f}" stroke="{line}" stroke-opacity=".075" stroke-width="1"/>')
                return
            if depth % 2 == 0:
                midpoint = ((a[0]+b[0])/2, (a[1]+b[1])/2)
                triangles(c, a, midpoint, depth + 1)
                triangles(b, c, midpoint, depth + 1)
            else:
                midpoint = ((b[0]+c[0])/2, (b[1]+c[1])/2)
                triangles(a, b, midpoint, depth + 1)
                triangles(c, a, midpoint, depth + 1)
        for tri in [((1040,1120),(2440,940),(2130,-140)), ((920,1180),(2130,-140),(1280,450))]:
            triangles(*tri, 0)
        parts.append(f'<path d="M 1190,1000 L 2130,-140 M 1280,450 L 2440,940" fill="none" stroke="{accent}" stroke-opacity=".26" stroke-width="1.5"/>')
    parts += ['</g>', '</svg>']
    return "\n".join(parts).encode(), {"paper": bg, "line": line, "accent": accent}

def main():
    PRIVATE.mkdir(parents=True, exist_ok=True)
    DELIVERY.mkdir(parents=True, exist_ok=True)
    records, proof = [], []
    for site in ("dc", "tc"):
        for mode in ("light", "dark"):
            svg, palette = artwork(site, mode)
            digest = sha(svg)
            stem = f"dignity-{site}-folds-{mode}-{digest[:12]}"
            native = PRIVATE / "fractal-source-releases" / digest
            native.mkdir(parents=True, exist_ok=True)
            native_svg = native / f"{stem}.svg"
            native_png = native / f"{stem}.png"
            if native_svg.exists():
                assert native_svg.read_bytes() == svg
            else:
                native_svg.write_bytes(svg)
            if not native_png.exists():
                subprocess.run(["rsvg-convert", "--width", str(WIDTH), "--height", str(HEIGHT), "--output", str(native_png), str(native_svg)], check=True)
            for source in (native_svg, native_png):
                dest = DELIVERY / source.name
                if dest.exists():
                    assert dest.read_bytes() == source.read_bytes(), "Immutable delivery collision"
                else:
                    shutil.copyfile(source, dest)
            record = {
                "uuid": str(uuid.uuid5(uuid.NAMESPACE_URL, "https://ruvebal.github.io/dignity/" + digest)),
                "fractal_hash256": digest,
                "title": ("Relational folds" if site == "dc" else "Open assemblies") + f" — {mode}",
                "description": "Original recursive geometric composition; folded bands" if site == "dc" else "Original recursive geometric composition; triangular assemblies",
                "authorship": {"studio": "@ruvebal", "roles": ["visual-forger 1.3.0", "fractal-architect 1.2.1"], "generator": "dignity-background-studio " + VERSION},
                "created": DATE,
                "site": site,
                "mode": mode,
                "status": "geometry_only",
                "formulas": [],
                "mathematical_claim": "None. Original decorative geometry; no ethical or empirical claim is inferred from its structure.",
                "delivery": {"svg": f"/assets/images/dignity/backgrounds/{stem}.svg", "png": f"/assets/images/dignity/backgrounds/{stem}.png"},
                "viewport": {"width": WIDTH, "height": HEIGHT, "aspect_ratio": "2.39:1"},
                "title_safe": {"corner": "top-left", "x": [0, .40], "y": [0, .50]},
                "palette": palette,
                "motion": "none",
                "caption_en": "Original recursive geometry by @ruvebal, composed with visual-forger 1.3.0 and fractal-architect 1.2.1. Decorative artwork; it does not establish an ethical claim.",
                "caption_es": "Geometría recursiva original de @ruvebal, compuesta con visual-forger 1.3.0 y fractal-architect 1.2.1. Obra decorativa; no fundamenta una afirmación ética.",
            }
            records.append(record)
            proof.append({"uuid": record["uuid"], "svg_sha256": digest, "png_sha256": sha(native_png.read_bytes()), "source": str(native), "delivery_directory": str(DELIVERY), "source_delivery_identical": True})
    manifest = {"schema": "dignity.figcaption-data/1", "release": DATE + ".1", "figures": records}
    manifest_data = (json.dumps(manifest, indent=2, ensure_ascii=False)+"\n").encode()
    manifest_name = "figcaption-data-" + sha(manifest_data)[:12] + ".json"
    manifest_path = DELIVERY / manifest_name
    if manifest_path.exists():
        assert manifest_path.read_bytes() == manifest_data
    else:
        manifest_path.write_bytes(manifest_data)
    index_path = DELIVERY / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {"schema": "dignity.background-release-index/1", "releases": []}
    if not any(r["manifest"] == manifest_name for r in index["releases"]):
        index["releases"].append({"release": manifest["release"], "manifest": manifest_name})
    index["current"] = manifest_name
    index_path.write_text(json.dumps(index, indent=2)+"\n")
    receipt = {"date": DATE, "generator_version": VERSION, "generator_sha256": sha(Path(__file__).read_bytes()), "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(), "seed": SEED, "maximum_depth": MAX_DEPTH, "stop_rule": "Stop each recursion at depth 5; DC 32 bands, TC 64 leaf triangles.", "evidence_status": "geometry_only; no borrowed canonical formula or bibliographic citation is claimed", "skills": {name: {"path": str(p), "sha256": sha(p.read_bytes()), "version": p.with_name("VERSION").read_text().strip()} for name,p in SKILLS.items()}, "exports": proof, "review": {"machine_rendered": True, "human_review": False}}
    (PRIVATE / "fractal-proof-20261020-v1.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps({"manifest": str(manifest_path), "assets": [r["delivery"] for r in records]}, indent=2))

if __name__ == "__main__":
    main()
