#!/usr/bin/env bash
# PHASE-EX9.exit-gate.sh — lesson structure, exemplars, figures (Wave-1)
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
source "$ROOT/digital-creativity-pedagogy/excellence/gates/common.sh"
cd "$ROOT"

require_file "digital-creativity-pedagogy/excellence/PHASE-EX9.md"
require_file "docs/_includes/lesson-figure.html"
require_file "docs/_data/lesson_figures.json"
require_file "digital-creativity-pedagogy/excellence/evidence/EX9/provenance-baseline.json"

# --- Structure: EN I.1–I.9 ---
python3 - <<'PY' && pass "EN I.1–I.9 section spine" || fail "EN I.1–I.9 section spine"
import pathlib, re, sys
ORDER = [
    "Learning objectives",
    "Analysis",
    "Masterclass",
    "Lab (Portfolio)",
    "Workshop",
    "Conclusion",
    "Tao of the Image",
    "References",
]
bad = []
root = pathlib.Path("docs/lessons/en/digital-creativity-i")
for p in sorted(root.glob("i-*/index.md")):
    t = p.read_text()
    t = re.sub(r"\{% if site\.publication[\s\S]*?\{% endif %\}", "", t)
    h2 = [re.sub(r"\{[^}]*\}", "", h).strip() for h in re.findall(r"^## (.+)$", t, re.M)]
    # Drop emoji-only / TOC / Where this sits / Editorial from order check
    pos = []
    for name in ORDER:
        hits = [i for i, h in enumerate(h2) if h == name or h.startswith(name + " ")]
        if len(hits) != 1:
            bad.append(f"{p.parent.name}: '{name}' headings = {len(hits)}")
            pos.append(-1)
        else:
            pos.append(hits[0])
    if -1 not in pos and pos != sorted(pos):
        bad.append(f"{p.parent.name}: section order {pos}")
    # Workshop first line names session
    m = re.search(r"^## Workshop\n+([^\n]+)", t, re.M)
    if not m or not re.search(r"session", m.group(1), re.I):
        bad.append(f"{p.parent.name}: Workshop first line must name session")
    # Tao anchor
    if not re.search(r'id="tao-of-the-image"|\{#tao-of-the-image\}', t):
        bad.append(f"{p.parent.name}: missing tao-of-the-image anchor")
    # Example traces (≥2)
    lab = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", t, re.M)
    if not lab or lab.group(1).count("**Example trace:**") < 2:
        bad.append(f"{p.parent.name}: example traces < 2")
print("\n".join(bad[:40]))
sys.exit(1 if bad else 0)
PY

# --- Structure: ES I.1–I.9 ---
python3 - <<'PY' && pass "ES I.1–I.9 section spine" || fail "ES I.1–I.9 section spine"
import pathlib, re, sys
ORDER = [
    "Objetivos de aprendizaje",
    "Análisis",
    "Masterclass",
    "Lab (Portfolio)",
    "Workshop",
    "Conclusión",
    "Tao de la imagen",
    "Referencias",
]
bad = []
root = pathlib.Path("docs/lessons/es/creacion-digital-i")
for p in sorted(root.glob("i-*/index.md")):
    t = p.read_text()
    t = re.sub(r"\{% if site\.publication[\s\S]*?\{% endif %\}", "", t)
    h2 = [re.sub(r"\{[^}]*\}", "", h).strip() for h in re.findall(r"^## (.+)$", t, re.M)]
    pos = []
    for name in ORDER:
        hits = [i for i, h in enumerate(h2) if h == name or h.startswith(name + " ")]
        if len(hits) != 1:
            bad.append(f"{p.parent.name}: '{name}' headings = {len(hits)} ({[h for h in h2 if name.split()[0] in h][:3]})")
            pos.append(-1)
        else:
            pos.append(hits[0])
    if -1 not in pos and pos != sorted(pos):
        bad.append(f"{p.parent.name}: section order {pos}")
    m = re.search(r"^## Workshop\n+([^\n]+)", t, re.M)
    if not m or not re.search(r"sesi[oó]n(es)?|session", m.group(1), re.I):
        bad.append(f"{p.parent.name}: Workshop first line must name sesión/session")
    if not re.search(r'\{#tao-of-the-image\}', t):
        bad.append(f"{p.parent.name}: missing tao-of-the-image anchor")
    lab = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", t, re.M)
    if not lab or lab.group(1).count("**Example trace:**") < 2:
        bad.append(f"{p.parent.name}: example traces < 2")
print("\n".join(bad[:40]))
sys.exit(1 if bad else 0)
PY

# --- Fashion master lecture spine (no Workshop/Tao required) ---
python3 - <<'PY' && pass "fashion-image-analysis spine" || fail "fashion-image-analysis spine"
import pathlib, re, sys
t = pathlib.Path("docs/lessons/en/master-lectures/fashion-image-analysis/index.md").read_text()
need = ["Learning objectives", "Analysis", "Masterclass", "Lab (Portfolio)", "Conclusion", "References"]
h2 = [re.sub(r"\{[^}]*\}", "", h).strip() for h in re.findall(r"^## (.+)$", t, re.M)]
bad = []
pos = []
for name in need:
    hits = [i for i, h in enumerate(h2) if h == name or h.startswith(name)]
    if len(hits) != 1:
        bad.append(f"ML: '{name}' = {len(hits)}")
        pos.append(-1)
    else:
        pos.append(hits[0])
if -1 not in pos and pos != sorted(pos):
    bad.append(f"ML order {pos}")
if "lesson-figure.html" not in t:
    bad.append("ML: no lesson figures")
print("\n".join(bad))
sys.exit(1 if bad else 0)
PY

# --- EN+ES B2 cards I.1–I.5 (EX8 labels) ---
python3 - <<'PY' && pass "B2 exercise cards I.1–I.5 EN+ES" || fail "B2 exercise cards I.1–I.5 EN+ES"
import pathlib, re, sys
labels = [
    "Time:", "Group:", "Materials:", "Steps:",
    "Portfolio trace:", "Judged by:", "Source:",
]
pairs = [
    ("docs/lessons/en/digital-creativity-i", "i-1-digital-images"),
    ("docs/lessons/en/digital-creativity-i", "i-2-2d-drawing"),
    ("docs/lessons/en/digital-creativity-i", "i-3-color-bitmaps"),
    ("docs/lessons/en/digital-creativity-i", "i-4-effects"),
    ("docs/lessons/en/digital-creativity-i", "i-5-three-dimensional-form"),
    ("docs/lessons/es/creacion-digital-i", "i-1-imagenes-digitales"),
    ("docs/lessons/es/creacion-digital-i", "i-2-dibujo-2d"),
    ("docs/lessons/es/creacion-digital-i", "i-3-color-bitmaps"),
    ("docs/lessons/es/creacion-digital-i", "i-4-efectos"),
    ("docs/lessons/es/creacion-digital-i", "i-5-forma-tridimensional"),
]
bad = []
for folder, slug in pairs:
    t = (pathlib.Path(folder) / slug / "index.md").read_text()
    b2 = re.search(r"^## Lab \(Portfolio\)\n([\s\S]*?)(?=^## )", t, re.M)
    if not b2:
        bad.append(f"{slug}: Lab missing"); continue
    body = b2.group(1)
    for lab in labels:
        n = body.count(f"**{lab}**")
        if n < 2:
            bad.append(f"{slug}: '{lab}' on {n}/2 cards")
    ex = len(re.findall(r"^### (?:Exercise|Ejercicio) ", body, re.M))
    if ex != 2:
        bad.append(f"{slug}: {ex} Exercise headings (need 2)")
    if "lesson-figure.html" not in t:
        bad.append(f"{slug}: missing lesson figures")
print("\n".join(bad[:40]))
sys.exit(1 if bad else 0)
PY

# --- Provenance / citation non-regression ---
python3 - <<'PY' && pass "provenance/citation non-regression" || fail "provenance/citation non-regression"
import json, pathlib, re, sys
base = json.loads(pathlib.Path(
    "digital-creativity-pedagogy/excellence/evidence/EX9/provenance-baseline.json"
).read_text())
root = pathlib.Path("docs/lessons")
bad = []
for key, want in base.items():
    t = (root / key).read_text()
    now = {
        "PROVENANCE_LINE": len(re.findall(r"PROVENANCE_LINE:", t)),
        "cite_links": len(re.findall(r"\]\(#ref-[^)]+\)", t)),
        "public_citation": len(re.findall(r"public_citation=", t)),
    }
    # LAB_LINE may rise for I.6–I.9 placeholders — never fall for any key that had LAB_LINE
    lab_now = len(re.findall(r"LAB_LINE:", t))
    if lab_now < want.get("LAB_LINE", 0):
        bad.append(f"{key}: LAB_LINE {want['LAB_LINE']}→{lab_now}")
    for field in ("PROVENANCE_LINE", "cite_links", "public_citation"):
        if now[field] < want[field]:
            bad.append(f"{key}: {field} {want[field]}→{now[field]}")
print("\n".join(bad[:40]))
sys.exit(1 if bad else 0)
PY

jekyll_build_ok
publication_safety_ok

# --- hreflang: fashion-image-analysis must not emit hreflang=es to a missing page ---
python3 - <<'PY' && pass "hreflang sane (fashion EN-only)" || fail "hreflang sane (fashion EN-only)"
import pathlib, re, sys
from urllib.parse import urlparse

# Prefer the canonical lessons path (alias under _site/master-lectures may be a thin stub).
preferred = pathlib.Path("_site/lessons/en/master-lectures/fashion-image-analysis/index.html")
if not preferred.is_file():
    print("fashion-image-analysis HTML not found under _site/lessons/en/…")
    sys.exit(1)
html = preferred.read_text(errors="ignore")
bad = []
if 'hreflang="en"' not in html:
    bad.append("missing hreflang=en")
if 'hreflang="x-default"' not in html:
    bad.append("missing hreflang=x-default")
# EN-only: no Spanish alternate (or if present, must resolve to a built page)
es = sorted(set(re.findall(r'hreflang="es"[^>]*href="([^"]+)"', html)
              + re.findall(r'href="([^"]+)"[^>]*hreflang="es"', html)))
for href in es:
    path = urlparse(href).path
    rel = path
    for prefix in ("/digital-creativity-uem",):
        if rel.startswith(prefix):
            rel = rel[len(prefix):]
            break
    candidate = pathlib.Path("_site") / rel.lstrip("/")
    ok = candidate.is_file() or (candidate / "index.html").is_file()
    if not ok:
        bad.append(f"hreflang=es href not built: {href}")
# Soft rule for this EN-only lecture: prefer zero es alternates
if es:
    # Already validated built; still warn via fail if es points at self (wrong)
    for href in es:
        if href.rstrip("/").endswith("/fashion-image-analysis") and "/es/" not in href:
            bad.append(f"hreflang=es declares EN URL as Spanish: {href}")
print("\n".join(bad))
sys.exit(1 if bad else 0)
PY

finish
