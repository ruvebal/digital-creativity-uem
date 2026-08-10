# Publishing

Jekyll builds from `docs/` at the **repository root** (emancipation pattern = `hc-app-design`, not a nested `web-foundations/` folder inside a monorepo).

## GitHub Pages

- **URL:** `https://ruvebal.github.io/digital-creativity-uem/`
- **Workflow:** `.github/workflows/pages.yml`
- **`baseurl`:** `/digital-creativity-uem` in `_config.yml`

## Excluded from the public site

| Path | Reason |
| ---- | ------ |
| `docs/_research/` | `exclude:` in `_config.yml` |
| `digital-creativity-pedagogy/` | Outside `source: docs` + listed in `exclude` — **authority / research home** |
| `student-project-template/` | Outside `source: docs` |
| `private/` | Outside `source: docs` |

## Verify locally

```bash
JEKYLL_ENV=production npm run build
test ! -d _site/_research
test ! -d _site/digital-creativity-pedagogy
test ! -d _site/student-project-template
```

## Custom domain (optional)

Point DNS to GitHub Pages and set `url` / `baseurl` in `_config.yml` accordingly.
