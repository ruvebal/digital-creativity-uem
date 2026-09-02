# Media placeholder contract — Phase B (non-blocking)

**Status:** active for curriculum orchestrator Phase B  
**Upstream prospector:** `~/src/profield/docs/DEV_PLAN/MEDIA-PROSPECTOR/` (MP0–MP5)  
**Principle:** pedagogy ships on **what the media is for**; pixels and URLs are swappable.

## PM decision

**Do not wait for Profield Media Prospector** to run the curriculum orchestrator.
Phase A (provenance + deep lesson reconcile) and Phase B placeholders run in
parallel with profield MP0→MP5. When a manifest arrives, swap by
`media_slot_id` — do not rewrite B1/B2/B3 or master ideas.

## What matters now (caption-first)

Every media slot in a lesson must carry:

| Field | Required | Student-visible |
| --- | --- | --- |
| `media_slot_id` | stable, e.g. `I.1.video.practice-boundary` | no |
| `media_role` | `video` \| `still` \| `graphic` | yes (as label) |
| `studio_semantics` | from SESSION-PROMPT-FORGE enum | in caption |
| `why_this_is_here` | one sentence — the teaching function | **figcaption lead** |
| `viewing_question` | what students must notice | **figcaption** |
| `accessibility_fallback` | text-only / static poster path | yes |
| `placeholder` | `true` until prospector accepts asset | no |
| `placeholder_kind` | `fractal-svg` \| `semantic-diagram` \| `poster-still` | no |

The **why** and **viewing question** are the durable contract. A video slot may
ship as a static poster + caption until rights-cleared embed exists.

## Placeholder production

| Slot | Tool | Rules |
| --- | --- | --- |
| `graphic` | `visual-forger` + `fractal-architect` | UEM palette only; formula/SVG; full alt text; no internal corpus IDs in artwork |
| `still` (exemplar/counterexample) | semantic diagram or labelled frame | must show *what to compare*, not decorative fashion stock |
| `video` | `poster-still` + transcript stub | mark `embed_pending: true`; never fake a YouTube ID |

Tag generated assets:

```yaml
placeholder: true
placeholder_kind: fractal-svg
media_slot_id: II.4.video.consent-before-cuts
replaces_when: profield-media-prospector MP5 accept
```

## HTML pattern (lessons)

Use semantic `<figure>` / `<figcaption>`:

```html
<figure class="lesson-media lesson-media--placeholder" data-media-slot="I.1.video.practice-boundary">
  <img src="…" alt="…" loading="lazy" />
  <figcaption>
    <p><strong>Why this is here:</strong> … studio_semantics rationale …</p>
    <p><strong>Look for:</strong> … viewing_question …</p>
    <p class="media-note">Placeholder visual — licensed media pending review.</p>
  </figcaption>
</figure>
```

Video upgrade path: replace `<img>` with privacy-enhanced embed when
`MEDIA_RIGHTS_LINE` is resolved; **keep the same figcaption text** unless the
viewing question changes.

## Swap-in (after Media Prospector)

1. Import accepted manifest row to `docs/_data/media-packs/{unit_id}.yml` (MP5).
2. Match `media_slot_id`.
3. Set `placeholder: false`; add `MEDIA_RIGHTS_LINE` in gated comment.
4. Re-run `npm run verify:publication` and `npm run build`.

## Forge failure

- Caption missing `why_this_is_here` or `viewing_question`
- Decorative image with no studio_semantics rationale
- Placeholder presented as final licensed media (must say pending)
- Invented URL, licence, or video ID
