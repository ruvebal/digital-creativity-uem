#!/usr/bin/env python3
"""Audit public page locators against the printed folio of the source PDF.

Why: the citation resolver reports `scheme=pdf_order` (PDF sequence = page_index + 1),
which is NOT the printed page whenever a book has front matter. This script reads every
gated PROVENANCE_LINE in the student lessons, finds the node's page_index in the
extraction database, extracts the printed folio from the running header/footer of that
PDF page (pdftotext), and compares it with the page in the public citation.

    python3 digital-creativity-pedagogy/forge/scripts/verify_printed_folios.py [paths...]

Exit 1 on any mismatch. EPUB sources have no printed folio: they are reported as
`section-only` and must be cited by section, never by page_index.
Read-only: never edits lessons or the extraction library.
"""
import glob
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LIB = Path.home() / "ahmes-library"
LINE = re.compile(r"PROVENANCE_LINE:[^\n]*")
COAT = re.compile(r"(?:document_)?coat=([0-9a-f]{8})")
NODE = re.compile(r"node(?:_id)?=([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})")
PUBLIC = re.compile(r'public(?:_citation)?="\(([^"]*?)(?:, ([^",)]+))?\)"')


def source_dir(coat):
    hits = glob.glob(str(LIB / "*" / "documents" / f"*_{coat}"))
    return Path(hits[0]) if hits else None


def page_index(doc, node):
    db = doc / "extract" / "extraction.db"
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    row = con.execute("select page_index from anchor_spatial where node_id=?", (node,)).fetchone()
    return row[0] if row else None


def printed_folio(pdf, seq):
    """Folio = a bare 1–4 digit number at the start or end of the first/last text lines."""
    out = subprocess.run(["pdftotext", "-f", str(seq), "-l", str(seq), "-layout", str(pdf), "-"],
                         capture_output=True, text=True).stdout
    rows = [r.strip() for r in out.splitlines() if r.strip()]
    # A lone number on the last line is a footer folio (chapter openers put the
    # chapter number at the top, so check the footer first).
    if rows and re.fullmatch(r"\d{1,4}", rows[-1]):
        return int(rows[-1])
    for r in rows[:2] + rows[-2:]:
        m = re.match(r"^(\d{1,4})\s{2,}\S", r) or re.search(r"\S\s{2,}(\d{1,4})$", r) or re.fullmatch(r"(\d{1,4})", r)
        if m:
            return int(m.group(1))
    return None


def main(paths):
    files = paths or sorted(glob.glob(str(ROOT / "docs/lessons/**/*.md"), recursive=True))
    bad = 0
    for f in files:
        text = Path(f).read_text(encoding="utf-8")
        for line in LINE.findall(text):
            coat, node, pub = COAT.search(line), NODE.search(line), PUBLIC.search(line)
            if not (coat and node and pub):
                continue
            label = f"{Path(f).relative_to(ROOT)} · ({pub.group(1)}, {pub.group(2)})"
            doc = source_dir(coat.group(1))
            if not doc:
                print(f"MISSING-SOURCE  {label}")
                bad += 1
                continue
            pdfs = list((doc / "source").rglob("*.pdf"))
            idx = page_index(doc, node.group(1))
            if not pdfs:
                state = "ok" if not (pub.group(2) or "").strip().isdigit() else "PAGE-ON-EPUB"
                print(f"{'section-only' if state == 'ok' else state:<15} {label}")
                bad += state != "ok"
                continue
            folio = printed_folio(pdfs[0], idx + 1) if idx is not None else None
            cited = (pub.group(2) or "").strip()
            if folio is None:
                print(f"NO-FOLIO        {label} · pdf_seq={idx + 1 if idx is not None else '?'} (check by eye)")
            elif cited != str(folio):
                print(f"MISMATCH        {label} · printed={folio} pdf_seq={idx + 1}")
                bad += 1
            else:
                print(f"ok              {label}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
