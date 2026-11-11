# Perspective · volume image kit (indexed)

**Purpose:** teach perspective *and* volume as image-grammar principles — technical precision + artistic elegance — without replacing I.6 fit diagnosis.  
**Authority:** Panofsky categories in [`I6-FORM-GRAMMAR-VAULT-CHECK-20261111.md`](I6-FORM-GRAMMAR-VAULT-CHECK-20261111.md).  
**Pipeline:** `curriculum-forger` / `dc-unit-forge` prompt → `visual-forger` (diagram/SVG) → optional `svg-to-rive-3d` → `rive-animascript-3d` (true-3D motion) → append this index.

## Forge prompt (lesson forgers — copy when a unit needs perspective/volume figures)

```
Subject: One Panofsky category P1–P5 as a spatial construction, paired with
         one I.6 volume variable (drape|tension|fold|void|scale|camera).
Reader: CD I students · front/side/¾ evidence · no vanishing-point as fit proof.
Mode: imagine (diagram) first; promote to rive-3d only if occlusion/depth buffer
      is the claim. Formula mode if a construction law must survive print.
Elegance: one composition, edge-to-edge diagram plane, course palette tokens,
          no dashboard chrome, no decorative polyhedra without kit_id.
Grounding: Panofsky / Pacioli / Bertol only with evaluator_safe cites (page-spot).
           Caption: Chicago author-date only.
Kit: append one row below with kit_id, category, outputs, sha256, forge date.
```

## Skill chain

| Step | Skill | Owns |
| --- | --- | --- |
| 1 | `curriculum-forger` §5.2 / `dc-unit-forge` | When to request a figure; CLT gate |
| 2 | `visual-forger` mode **`perspective-kit`** | SVG+PNG, caption law, content-hash |
| 3 | `platonic-solids` | Only if P2 packing / solid volumes |
| 4 | `svg-to-rive-3d` | Extrude kit SVG → geometry provider |
| 5 | `rive-animascript-3d` | Portable 3D scene, camera channels, fallback |
| 6 | `canvas-25d-content-hero` | When painter-order 2.5D is enough (P3) |

## Index (append-only)

| kit_id | Panofsky cat. | Motion grammar | Status | Outputs |
| --- | --- | --- | --- | --- |
| `pv-p1-psycho-vs-math-20261111` | P1 | Dual overlay (static SVG; Rive toggle TBD) | **shipped static** | `docs/assets/images/lesson-figures/perspective-kit/pv-p1-psycho-vs-math-5e69c5149013.svg` |
| `pv-p2-antique-aggregate-20261111` | P2 | No shared VP · multi-object | **shipped SVG + local .riv** | SVG `…/pv-p2-antique-aggregate-3b41a386a525.svg` · riv `…/rive/pv-p2-antique-aggregate-567c82c645a6.riv` · forge `digital-creativity-pedagogy/forge/perspective-kit/rive/p2-antique-aggregate/` |
| `pv-p3-gothic-mass-interior-20261111` | P3 | Planes → hollow | **shipped SVG + local .riv** | SVG `…/pv-p3-gothic-mass-interior-70d8ce73e856.svg` · riv `…/rive/pv-p3-gothic-mass-interior-a95a9b08328a.riv` · forge `…/p3-gothic-mass-interior/` |
| `pv-p4-space-box-20261111` | P4 | Camera enter room | **shipped SVG + local .riv** | SVG `…/pv-p4-space-box-e82143f11966.svg` · riv `…/rive/pv-p4-space-box-2889af99eda4.riv` · forge `…/p4-space-box/` |
| `pv-p5-central-vp-20261111` | P5 | Shared VP · depth | **shipped SVG + local .riv** | SVG `…/pv-p5-central-vp-bdbfcffbe72c.svg` · riv `…/rive/pv-p5-central-vp-5a0b4095b188.riv` · forge `…/p5-central-vp/` |
| `pv-p6-fashion-multiview-20261111` | P6 | Three locked cameras | **shipped SVG + local .riv** | SVG `…/pv-p6-fashion-multiview-d0cf3c150102.svg` · riv `…/rive/pv-p6-fashion-multiview-7e85e61256d6.riv` · forge `…/p6-fashion-multiview/` |

### Compile note (2026-11-11)

- CLI: Rive 1.9.2 · `rive . --verify` then `rive . --publish=local` per project.
- Paint API: `PaintStyle.stroke` (not `Paint.Style.Stroke`).
- Published builds carry **Rive splash watermark** (ruvebal free-plan CLI); upgrade plan before classroom-clean embeds.
- **Embedded 2026-11-11:** I.6 EN/ES lesson `page_art` + deck slides (cover / analysis-model / masterclass-2–3) mount `.riv` as ambient overlays via `docs/assets/js/rive-background.js` + vendored `@rive-app/canvas`; static SVG/webp remain the Reveal/`page-art` background (reduced-motion safe).
- Deck also binds Profield-cleared drapery/volume stills (Leonardo PD; drapery + Kawakubo 02/03 flagged under `--rights=flag`).

## Delivery rules

- Student HTML: `<figure><img><figcaption>` only; no Ahmes IDs.  
- Reduced motion: static SVG twin mandatory before any Rive ship.  
- Never overwrite bytes at an existing path; new hash = new row.
