#!/usr/bin/env python3
"""Regenerate catalogue artefacts from emit_catalogue.METHODS (or methods.base.yml).

Preferred: edit emit_catalogue.py METHODS, then:

    python3 digital-creativity-pedagogy/catalogue/build.py

This wrapper keeps the CT EX7 habit of a named `build.py` entrypoint.
"""
from __future__ import annotations

import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("emit_catalogue.py")), run_name="__main__")
