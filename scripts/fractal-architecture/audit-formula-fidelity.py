#!/usr/bin/env python3
"""Produce a conservative formula-fidelity report from an Ahmes database.

This script never repairs formulae. It compares page-scoped extracted text with
a human-transcribed oracle and emits candidates for visual verification.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from pathlib import Path


def normalize(value: str) -> str:
    value = value.replace("∞", "infty").replace("∈", "in").replace("∏", "prod")
    value = value.replace("−", "-").replace("–", "-")
    return re.sub(r"[^a-z0-9+*=()'_-]+", "", value.lower())


def load_page_nodes(connection: sqlite3.Connection, page_index: int) -> list[dict]:
    rows = connection.execute(
        """
        SELECT fn.node_id, fn.block_type, fn.block_subtype,
               fn.markdown_content, COALESCE(fn.original_content, '')
        FROM fission_node fn
        JOIN anchor_spatial a ON a.node_id = fn.node_id
        WHERE a.page_index = ?
        ORDER BY a.y0, a.x0
        """,
        (page_index,),
    ).fetchall()
    return [
        {
            "node_id": row[0],
            "block_type": row[1],
            "block_subtype": row[2],
            "markdown": row[3],
            "original": row[4],
        }
        for row in rows
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("database", type=Path)
    parser.add_argument("oracle", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    oracle = json.loads(args.oracle.read_text())
    connection = sqlite3.connect(f"file:{args.database}?mode=ro", uri=True)
    formula_count = connection.execute(
        "SELECT COUNT(*) FROM fission_node WHERE block_type = 'formula'"
    ).fetchone()[0]

    lines = [
        "# Formula fidelity audit",
        "",
        f"- Source: `{oracle['source']}`",
        f"- Database: `{args.database}`",
        f"- First-class `formula` nodes: **{formula_count}**",
        "- Automatic token checks are diagnostic only; final classification requires page-image comparison.",
        "",
        "| Equation | Page | Token retention | Candidate nodes | Automatic disposition |",
        "| --- | ---: | ---: | --- | --- |",
    ]

    for equation in oracle["equations"]:
        nodes = load_page_nodes(connection, equation["db_page_index"])
        joined = "\n".join(node["markdown"] + "\n" + node["original"] for node in nodes)
        normalized = normalize(joined)
        checks = [normalize(token) in normalized for token in equation["required_tokens"]]
        retention = sum(checks) / len(checks) if checks else 0.0
        candidates = [
            node["node_id"][:8]
            for node in nodes
            if any(normalize(token) in normalize(node["markdown"] + node["original"]) for token in equation["required_tokens"])
        ][:6]
        if retention == 1 and formula_count:
            disposition = "VERIFY_VISUALLY"
        elif retention >= 0.6:
            disposition = "USABLE_WITH_REPAIR_CANDIDATE"
        elif retention:
            disposition = "DISCOVERY_ONLY"
        else:
            disposition = "MISSING"
        lines.append(
            f"| `{equation['id']}` | {equation['source_page']} | {retention:.0%} | "
            f"{', '.join(candidates) or 'none'} | **{disposition}** |"
        )

    lines.extend(
        [
            "",
            "## Human verification queue",
            "",
            "For every equation, compare the source-page render against the oracle LaTeX and the full candidate nodes. Record operator, subscript, superscript, delimiter, and line-break defects separately. Do not promote any formula until this queue is signed off.",
            "",
        ]
    )
    report = "\n".join(lines)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
