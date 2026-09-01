#!/usr/bin/env python3
"""
Interactive AFEL review loop — a convenience wrapper around
`ahmes formula review-next` / `review-record` (12H.FC2, §4).

The ahmes CLI itself stays flag-driven and scriptable by design — this
script is the human-facing loop on top of it: auto-opens each candidate's
crop, prompts for a decision, and records it, so a real review session
doesn't mean re-typing candidate_id/paths by hand for all 318 candidates.

`ahmes formula review-record` remains the only thing that actually writes a
receipt — this script only decides *which* candidate to show next (reading
the queue + receipts + a local skip list directly) and shells out for the
write, so validation stays in one place.

Usage:
    python3 review-loop.py

Author: Rubén Vega Balbás PhD (ECSIT / UDIT)
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

AHMES = Path.home() / "src/ahmes/.venv/bin/ahmes"
QUEUE = (
    Path.home()
    / "projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem"
    / "digital-creativity-pedagogy/grounding/fractal-architecture/runs"
    / "20260830T-afel-fc1-candidates/reduced-review-queue.private.json"
)
RECEIPTS = QUEUE.parent / "review-receipts.jsonl"
SKIPPED = QUEUE.parent / "review-skipped.txt"
REVIEWER = "Rubén Vega Balbás"

FIDELITY_CHOICES = ["EXACT", "USABLE_WITH_REPAIR", "DISCOVERY_ONLY", "MISSING", "REJECTED"]
ROLE_CHOICES = ["CANONICAL", "DERIVATION_STEP", "WORKED_EXAMPLE"]


def _load_queue() -> list[dict[str, Any]]:
    return json.loads(QUEUE.read_text(encoding="utf-8")).get("candidates", [])


def _reviewed_ids() -> set[str]:
    if not RECEIPTS.is_file():
        return set()
    ids = set()
    for line in RECEIPTS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            ids.add(json.loads(line)["candidate_id"])
    return ids


def _skipped_ids() -> set[str]:
    if not SKIPPED.is_file():
        return set()
    return {line.strip() for line in SKIPPED.read_text(encoding="utf-8").splitlines() if line.strip()}


def _mark_skipped(candidate_id: str) -> None:
    with SKIPPED.open("a", encoding="utf-8") as handle:
        handle.write(candidate_id + "\n")


def next_candidate() -> Optional[dict[str, Any]]:
    handled = _reviewed_ids() | _skipped_ids()
    for candidate in _load_queue():
        if candidate["candidate_id"] not in handled:
            return candidate
    return None


def prompt_choice(label: str, choices: list[str], allow_blank: bool = False) -> str:
    options = "/".join(choices) + ("/<blank>" if allow_blank else "")
    while True:
        raw = input(f"{label} [{options}]: ").strip().upper()
        if raw in choices:
            return raw
        if allow_blank and raw == "":
            return ""
        print(f"  invalid — choose one of: {', '.join(choices)}")


def record(candidate: dict[str, Any], *, fidelity: str, role: str, defects: str,
           latex: str, latex_source: str, mathml: str, repair_note: str,
           citation: str) -> None:
    args = [
        str(AHMES), "formula", "review-record", candidate["candidate_id"],
        "--queue", str(QUEUE), "--receipts", str(RECEIPTS),
        "--reviewer", REVIEWER, "--fidelity", fidelity,
    ]
    if role:
        args += ["--derivation-role", role]
    if defects:
        args += ["--defects", defects]
    if latex:
        args += ["--latex", latex, "--latex-source", latex_source]
    if mathml:
        args += ["--mathml", mathml]
    if repair_note:
        args += ["--repair-note", repair_note]
    if citation:
        args += ["--citation", citation]

    result = subprocess.run(args, capture_output=True, text=True)
    print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr.strip(), file=sys.stderr)


def main() -> int:
    if not AHMES.is_file():
        print(f"ahmes not found at {AHMES}", file=sys.stderr)
        return 1
    if not QUEUE.is_file():
        print(f"queue not found at {QUEUE}", file=sys.stderr)
        return 1

    reviewed_count = len(_reviewed_ids())
    total = len(_load_queue())
    print(f"AFEL review loop — {reviewed_count}/{total} already reviewed.\n")

    while True:
        candidate = next_candidate()
        if candidate is None:
            print("Queue exhausted — nothing left to review or skip.")
            return 0

        print("=" * 78)
        print(f"candidate_id  {candidate['candidate_id']}")
        print(f"document_id   {candidate['document_id']}   page {candidate['page_index']}")
        print(f"raw_text      {candidate.get('raw_text', '')}")
        for b in candidate.get("context_before", []):
            text = b.get("text") if isinstance(b, dict) else b
            print(f"  before: {text}")
        for a in candidate.get("context_after", []):
            text = a.get("text") if isinstance(a, dict) else a
            print(f"  after:  {text}")

        crop_relpath = candidate.get("crop_relpath")
        library_root = Path.home() / "ahmes-library/scholar/documents"
        crop_path = None
        if crop_relpath:
            for db in library_root.glob("*/extract/extraction.db"):
                candidate_bundle = db.parent
                candidate_crop = candidate_bundle / crop_relpath
                if candidate_crop.is_file():
                    crop_path = candidate_crop
                    break
        if crop_path:
            print(f"crop          {crop_path}")
            subprocess.run(["open", str(crop_path)])
        else:
            print("crop          (not found on disk)")
        print("=" * 78)

        answer = input("\n[r]eview, [s]kip for now, [q]uit: ").strip().lower()
        if answer == "q":
            print(f"Stopped. {len(_reviewed_ids())}/{total} reviewed so far.")
            return 0
        if answer == "s":
            _mark_skipped(candidate["candidate_id"])
            print("Skipped — will not show again this or future runs "
                  f"(remove its line from {SKIPPED.name} to bring it back).\n")
            continue
        if answer != "r":
            print("  (unrecognized, treating as skip-for-this-loop-only)")
            continue

        fidelity = prompt_choice("fidelity_status", FIDELITY_CHOICES)
        role = prompt_choice("derivation_role", ROLE_CHOICES, allow_blank=True)
        defects = input("defects (comma-separated, blank for none): ").strip()
        latex = input("latex (blank to skip): ").strip()
        latex_source = "human_transcription"
        mathml = ""
        repair_note = ""
        citation = ""
        if latex:
            ls = input("latex_source [human_transcription/trusted_source_tex/oracle] "
                       "(blank = human_transcription): ").strip()
            if ls:
                latex_source = ls
        if fidelity == "USABLE_WITH_REPAIR":
            repair_note = input("repair_note (required): ").strip()

        record(
            candidate, fidelity=fidelity, role=role, defects=defects,
            latex=latex, latex_source=latex_source, mathml=mathml,
            repair_note=repair_note, citation=citation,
        )
        print()


if __name__ == "__main__":
    raise SystemExit(main())
