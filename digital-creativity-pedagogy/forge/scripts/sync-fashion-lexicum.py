#!/usr/bin/env python3
"""Clone the fashion field from lexfield into the DC curriculum snapshot and Jekyll data.

Upstream (studio engine): ~/src/fieldlex/fields/fashion
Destinations:
  digital-creativity-pedagogy/cv/data/lexicum/
  docs/_data/lexicum.json

Never write discontinued sibling-repo names into public HTML.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[3]
DEFAULT_UPSTREAM = Path.home() / "src" / "fieldlex" / "fields" / "fashion"
CV_ROOT = REPO / "digital-creativity-pedagogy" / "cv" / "data" / "lexicum"
EXPORTS = CV_ROOT / "exports"
JEKYLL_DATA = REPO / "docs" / "_data" / "lexicum.json"
DIST = Path.home() / "src" / "fieldlex" / "dist"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def clone_yaml(upstream: Path) -> None:
    fashion = CV_ROOT / "fashion"
    if fashion.exists():
        shutil.rmtree(fashion)
    fashion.mkdir(parents=True)
    shutil.copy2(upstream / "field.yaml", fashion / "field.yaml")
    for sub in ("fashion_design", "fashion_business", "fashion_communication"):
        dest = fashion / sub
        dest.mkdir(parents=True)
        shutil.copy2(upstream / sub / "concepts.yaml", dest / "concepts.yaml")
    EXPORTS.mkdir(parents=True, exist_ok=True)
    for name in ("fashion.md", "fashion.ttl", "fashion.jsonld"):
        src = DIST / name
        if src.exists():
            shutil.copy2(src, EXPORTS / name)


def compile_public_json() -> dict:
    root = CV_ROOT / "fashion"
    field = _load_yaml(root / "field.yaml")
    if "example.org" in str(field.get("namespace_uri", "")):
        field["namespace_uri"] = "https://crea-comm.net/lexfield/fashion#"

    subfields: list[dict] = []
    concepts_flat: list[dict] = []
    for sub_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        data = _load_yaml(sub_dir / "concepts.yaml")
        concepts = []
        for c in data.get("concepts", []):
            scope = (c.get("scope_note") or "").strip() or None
            if scope:
                # Public snapshot must not carry discontinued sibling-repo prefixes.
                scope = scope.replace("fashlex:", "fashion:")
            item = {
                "slug": c["slug"],
                "pref_label": (c.get("pref_label") or "").strip(),
                "definition": (c.get("definition") or "").strip(),
                "alt_labels": c.get("alt_labels") or [],
                "broader": c.get("broader") or [],
                "narrower": c.get("narrower") or [],
                "related": c.get("related") or [],
                "scope_note": scope,
                "crm_mapping": c.get("crm_mapping"),
                "subfield_slug": data["subfield_slug"],
                "qualified": f"{data['subfield_slug']}.{c['slug']}",
                "uri_local": f"fashion:{c['slug']}",
            }
            concepts.append(item)
            concepts_flat.append(item)
        subfields.append(
            {
                "slug": data["subfield_slug"],
                "title": data.get("title", data["subfield_slug"]),
                "description": (data.get("description") or "").strip(),
                "concept_count": len(concepts),
                "concepts": concepts,
            }
        )

    payload = {
        "schema": "lexfield-public/v1",
        "cloned_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "field": {
            "slug": field["slug"],
            "title": field["title"],
            "description": (field.get("description") or "").strip(),
            "namespace_prefix": field.get("namespace_prefix", "fashion"),
            "namespace_uri": field["namespace_uri"],
        },
        "stats": {"subfields": len(subfields), "concepts": len(concepts_flat)},
        "subfields": subfields,
        "provenance": {
            "author": {
                "name": "Rubén Vega Balbás, PhD",
                "role": "Creative Technologist & Developer",
                "orcid": "https://orcid.org/0000-0001-6862-9081",
                "email": "ruvebal@crea-comm.net",
            },
            "vocabulary_engine": {
                "name": "lexfield",
                "version": "0.1.0",
                "path_hint": "fieldlex (multi-tenant SKOS vocabulary engine)",
            },
            "publication_stack": {
                "static_site": "Jekyll 3.10.0",
                "templates": "Liquid 4.0.4",
                "markdown": "kramdown (GFM)",
                "stylesheet": "PostCSS + Tailwind CSS 3.x",
            },
            "ontology": {
                "skos": {
                    "name": "SKOS",
                    "version": "W3C Recommendation, 2009-08-18",
                    "url": "https://www.w3.org/TR/skos-reference/",
                },
                "cidoc_crm": {
                    "name": "CIDOC-CRM",
                    "version": "7.1.3 (2024-02-13)",
                    "url": "https://gitlab.isl.ics.forth.gr/cidoc-crm/cidoc_crm_rdf",
                },
            },
            "method": (
                "Curriculum-local YAML snapshot compiled from lexfield; "
                "definitions authored as controlled-vocabulary entries with "
                "optional CIDOC-CRM class mappings where heritage-relevant."
            ),
            "prototype_note": (
                "The fashion field is the seed tenant of lexfield; other fields "
                "(e.g. creativity_techniques) reuse the same Field→Subfield→Concept schema."
            ),
        },
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    (CV_ROOT / "fashion.json").write_text(text, encoding="utf-8")
    JEKYLL_DATA.parent.mkdir(parents=True, exist_ok=True)
    JEKYLL_DATA.write_text(text, encoding="utf-8")
    return payload


def write_manifest(upstream: Path, payload: dict) -> None:
    manifest = {
        "schema": "dc-lexicum-clone-manifest/v1",
        "cloned_at": payload["cloned_at"],
        "upstream": {
            "tool": "lexfield",
            "path": str(upstream),
            "note": "Curriculum-local snapshot. Re-run this script to refresh.",
        },
        "stats": payload["stats"],
        "destinations": {
            "yaml_tree": "digital-creativity-pedagogy/cv/data/lexicum/fashion/",
            "public_json": "digital-creativity-pedagogy/cv/data/lexicum/fashion.json",
            "jekyll_data": "docs/_data/lexicum.json",
            "skos_exports": "digital-creativity-pedagogy/cv/data/lexicum/exports/",
        },
        "publication": {
            "route": "/lexicum/",
            "student_surface": "pref_label, definition, alt_labels, relations",
        },
    }
    (CV_ROOT / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--upstream",
        type=Path,
        default=DEFAULT_UPSTREAM,
        help="Path to lexfield fields/fashion directory",
    )
    args = parser.parse_args()
    upstream = args.upstream.expanduser().resolve()
    if not (upstream / "field.yaml").exists():
        raise SystemExit(f"upstream fashion field missing: {upstream}")
    CV_ROOT.mkdir(parents=True, exist_ok=True)
    clone_yaml(upstream)
    payload = compile_public_json()
    write_manifest(upstream, payload)
    print(
        f"synced fashion lexicum · {payload['stats']['concepts']} concepts · "
        f"{payload['stats']['subfields']} schemes · {payload['cloned_at']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
