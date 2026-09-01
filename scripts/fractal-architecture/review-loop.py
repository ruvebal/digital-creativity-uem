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
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Optional

AHMES = Path.home() / "src/ahmes/.venv/bin/ahmes"
REVIEW_TMP_DIR = Path(tempfile.gettempdir()) / "afel-review-crops"
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


def _close_previous_review_windows() -> None:
    """Close only Preview windows this script opened (name prefix afel_),
    never touching unrelated windows the user has open elsewhere.

    Best-effort: needs macOS Automation permission for whatever runs this
    script to control Preview (System Settings > Privacy & Security >
    Automation) — first run may prompt for it. If it's denied or not yet
    granted, this silently no-ops (AppleScript's `close` on a window doesn't
    raise even when blocked) — windows will pile up, but each is still
    labeled with its candidate_id, which is the actual fix for "can't match
    pngs and terminal text." Closing old ones is cosmetic on top of that."""
    script = '''
    tell application "Preview"
        if it is running then
            try
                close (every window whose name starts with "afel_")
            end try
        end if
    end tell
    '''
    subprocess.run(["osascript", "-e", script], capture_output=True)


def open_crop_labeled(crop_path: Path, candidate_id: str, page_index: Any) -> Path:
    """Copy the crop to a temp file named with the candidate_id, so the
    Preview window title is matchable against the terminal — the original
    crop filename is the *node_id*, a different UUID with no visible
    relation to candidate_id, which is what made this unmatchable before."""
    REVIEW_TMP_DIR.mkdir(parents=True, exist_ok=True)
    short_id = candidate_id.split("-")[0]
    labeled_path = REVIEW_TMP_DIR / f"afel_{short_id}_p{page_index}{crop_path.suffix}"
    shutil.copyfile(crop_path, labeled_path)
    _close_previous_review_windows()
    subprocess.run(["open", str(labeled_path)])
    return labeled_path


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
            labeled = open_crop_labeled(crop_path, candidate["candidate_id"], candidate["page_index"])
            print(f"crop          {crop_path}")
            print(f"  → opened as {labeled.name}  (Preview window title matches this — "
                  f"candidate_id starts with the same '{candidate['candidate_id'].split('-')[0]}')")
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
