# Catalogue — Digital Creativity fashion-craft methods

Studio craft methods for Creación Digital (figurín, photobash, Gestalt
composition, retouch, bodegón, …). **Not** a fork of Creativity Techniques.

## Regenerate

```bash
python3 digital-creativity-pedagogy/catalogue/build.py
```

Requires PyYAML. Exit gates use Ruby's stdlib YAML. To regenerate:

```bash
python3 -m venv /tmp/dc-ex7-venv && /tmp/dc-ex7-venv/bin/pip install -q pyyaml
/tmp/dc-ex7-venv/bin/python digital-creativity-pedagogy/catalogue/build.py
```

## Source honesty

| `source_status` | Meaning |
| --- | --- |
| `verified` | `primary_source` key exists in `docs/_data/references.yml` with a page/section locator |
| `held` | Profield / library points at a work not yet in `references.yml` |
| `gap` | No page-backed Wave-1 source; classroom adaptation only |

Gap/held attributions must not become student-facing Source lines until EX6-style
procurement lands.
