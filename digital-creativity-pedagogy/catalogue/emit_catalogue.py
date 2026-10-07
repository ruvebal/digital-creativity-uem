#!/usr/bin/env python3
"""EX7 — emit fashion-craft method catalogue artefacts (private + public seed).

Edit METHODS below, then re-run. Do not invent page cites: verified sources must
already appear in docs/_data/references.yml (EX6). Gaps/held are honest.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CAT = Path(__file__).resolve().parent
REFS = ROOT / "docs" / "_data" / "references.yml"
SEED = ROOT / "docs" / "_data" / "fashion_craft_methods.seed.yml"
CARDS_DIR = ROOT / "docs" / "methods" / "en" / "cards"

# Families are fashion-craft studio families — NOT CT technique families.
FAMILIES = (
    "drawing",
    "colour",
    "composition",
    "bitmap",
    "form-volume",
    "retouch",
    "still-motion",
    "research",
    "presentation",
    "critical-craft",
)
CRAFT_MODES = ("constructive", "synthetic", "critical", "workflow")
SOURCE_STATUSES = ("verified", "held", "gap")

# required ACT1/ACT2 anchors (acceptance)
REQUIRED_IDS = ("figurin-digital", "photobash-integration", "gestalt-composition")


def M(
    id: str,
    name: str,
    family: str,
    craft_mode: str,
    units: list[str],
    steps: list[str],
    *,
    primary_source: str = "gap",
    source_status: str = "gap",
    source_locator: str | None = None,
    gap_work: str | None = None,
    held_note: str | None = None,
    profield_runs: list[str] | None = None,
    didactics: list[str] | None = None,
    sandra_acts: list[str] | None = None,
    time_min: int = 30,
    group_size: str = "individual",
    materials: list[str] | None = None,
    evidence: str = "untested",
    accessibility: str = "Keyboard and typed alternatives accepted where mark-making is required.",
    summary: str = "",
) -> dict:
    assert family in FAMILIES, family
    assert craft_mode in CRAFT_MODES, craft_mode
    assert source_status in SOURCE_STATUSES, source_status
    assert 3 <= len(steps) <= 8, id
    return {
        "id": id,
        "name": name,
        "family": family,
        "craft_mode": craft_mode,
        "primary_source": primary_source,
        "source_status": source_status,
        "source_locator": source_locator,
        "gap_work": gap_work,
        "held_note": held_note,
        "profield_runs": profield_runs or [],
        "didactics": didactics or [],
        "sandra_acts": sandra_acts or [],
        "steps_basis": (
            "classroom adaptation in course wording; not quoted from, "
            "and not a claim that the source prescribes this sequence"
        ),
        "steps": steps,
        "time_min": time_min,
        "group_size": group_size,
        "materials": materials
        or ["laptop or tablet", "drawing/photo app", "timer"],
        "units": units,
        "evidence": evidence,
        "accessibility": accessibility,
        "summary": summary
        or f"Studio craft method ({family}): {name}.",
    }


METHODS: list[dict] = [
    # ——— ACT1 / ACT2 required ———
    M(
        "figurin-digital",
        "Digital figurín (fashion croquis figure)",
        "drawing",
        "constructive",
        ["I.1", "I.2"],
        [
            "Set a visible proportion scaffold (head-count or grid) on a blank canvas.",
            "Block the figure as simple volumes before any garment detail.",
            "Add garment silhouette with construction lines distinct from finish lines.",
            "Export a process pair: scaffold-only + finished figurín.",
            "Note one proportion decision that would survive a medium change (hand → raster → vector).",
        ],
        primary_source="gap",
        source_status="held",
        gap_work="Abling 2023 (manifest key abling-2023; fashion drawing conventions; page cite open)",
        held_note="Lesson I.2 already flags Abling page cite as open procurement.",
        profield_runs=["dc-2d-image-craft-pedagogy", "digital-creativity"],
        sandra_acts=["ACT1"],
        time_min=45,
        evidence="gap: fashion-HE figurín sequence not page-verified in Wave-1 references",
        summary="Proportion-first digital fashion figure for ACT1 craft.",
        accessibility="Accept typed proportion notes or photo of a paper croquis as equivalent evidence.",
    ),
    M(
        "photobash-integration",
        "Photobash integration (key-visual collage craft)",
        "bitmap",
        "synthetic",
        ["I.3", "I.4"],
        [
            "Collect a short, attributed contact sheet (≤12 stills) for one key-visual brief.",
            "Cut and layer fragments so seams are intentional, not accidental.",
            "Unify light/colour with adjustment layers only (keep originals recoverable).",
            "Check Gestalt grouping: what reads as one figure vs background noise?",
            "Export flat + layered file; list three integration decisions in a process note.",
        ],
        primary_source="gap",
        source_status="gap",
        gap_work="Practitioner/commercial photobash craft; no Wave-1 verified primary pedagogy source",
        profield_runs=[
            "dc-fashion-composition-references-pedagogy",
            "digital-creativity",
        ],
        sandra_acts=["ACT2"],
        time_min=60,
        group_size="pairs",
        evidence="untested — classroom craft aligned to Sandra ACT2 key visual",
        summary="Layered photographic integration for ACT2 key visual.",
        accessibility="Pair roles may split cutting vs colour-match; spoken process notes accepted.",
    ),
    M(
        "gestalt-composition",
        "Gestalt composition pass (grouping / figure–ground)",
        "composition",
        "constructive",
        ["I.3", "I.4", "I.7", "I.9"],
        [
            "Name one Gestalt relation to test (proximity, similarity, closure, continuity, or figure–ground).",
            "Apply the relation once to a key visual or bodegón draft.",
            "Invert or break the relation in a second version; keep both.",
            "Peer names which version groups more clearly and why (one sentence).",
            "Record the chosen relation in the process note for portfolio.",
        ],
        primary_source="gap",
        source_status="gap",
        gap_work="Arnheim 2004 (manifest key arnheim-2004) — not in references.yml; Gestalt laws as classroom craft until procured",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=25,
        group_size="pairs",
        evidence="gap: Arnheim / Gestalt pedagogy not Wave-1 verified",
        summary="One intentional Gestalt law applied to fashion image layout.",
        accessibility="Oral peer response OK; diagram annotation may replace redraw.",
    ),
    # ——— drawing ———
    M(
        "croquis-proportion-scaffold",
        "Croquis proportion scaffold",
        "drawing",
        "constructive",
        ["I.2"],
        [
            "Choose a head-count or grid scaffold and draw it alone first.",
            "Place landmarks (shoulder, waist, hip, knee) before contour.",
            "Trace a second pass for garment only on a separate layer.",
            "Compare scaffold vs finish; mark one collapsed decision.",
        ],
        source_status="held",
        gap_work="Abling 2023 (abling-2023)",
        held_note="I.2 text treats croquis as proportion habit across media.",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT1"],
        time_min=20,
        evidence="gap",
        summary="Scaffold-first croquis before garment finish.",
    ),
    M(
        "flat-sketch-tech-pack-lite",
        "Flat sketch (tech-pack lite)",
        "drawing",
        "constructive",
        ["I.2", "I.5"],
        [
            "Draw front flat with seams and closures as readable symbols.",
            "Add one callout (pocket, placket, hem) with a short label.",
            "Check symmetry and scale against a figurín from the same brief.",
            "Export PNG + note one construction ambiguity left unresolved.",
        ],
        source_status="held",
        gap_work="Abling 2023 / industry flats practice (page cite open)",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT1"],
        time_min=35,
        evidence="gap",
        summary="Orthographic garment flat with one technical callout.",
    ),
    M(
        "gesture-line-pass",
        "Gesture line pass",
        "drawing",
        "constructive",
        ["I.2"],
        [
            "Set a 60-second timer; draw the pose as continuous line only.",
            "Repeat three poses; keep all three without erasing.",
            "Circle the pass with clearest weight/axis.",
            "Use that axis under a slower figurín on a new layer.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=15,
        evidence="untested",
        summary="Timed gesture lines to recover pose axis.",
        accessibility="Voice-timed session or longer timer on request.",
    ),
    M(
        "construction-vs-finish-lines",
        "Construction vs finish line audit",
        "drawing",
        "critical",
        ["I.2"],
        [
            "Colour-code construction lines vs finish lines on one drawing.",
            "Hide finish; ask a peer what garment they still understand.",
            "Restore finish only where it adds information.",
            "Write one sentence: which line type carried the silhouette.",
        ],
        primary_source="huppauf-wulf-2009",
        source_status="verified",
        source_locator="p. 32 (imagination / creativity / fantasy as non-identical — used as critical frame for what 'more creative' finish may only be freer fantasy)",
        evidence="Hüppauf and Wulf 2009, 32 — framing only; not a drawing-sequence study",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT1"],
        time_min=20,
        summary="Separate scaffold information from cosmetic finish.",
    ),
    M(
        "vector-vs-raster-silhouette",
        "Vector vs raster silhouette test",
        "drawing",
        "constructive",
        ["I.2", "I.3"],
        [
            "Draw the same silhouette once in raster and once in vector.",
            "List three decisions that died in the medium change.",
            "Keep the version that preserves proportion landmarks.",
            "Archive both with a two-line medium note.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=30,
        evidence="untested — mirrors I.2 debate prompt without inventing efficacy claims",
        summary="Same silhouette across raster and vector to expose medium loss.",
    ),
    # ——— colour ———
    M(
        "rgb-cmyk-intent-check",
        "RGB/CMYK intent check",
        "colour",
        "workflow",
        ["I.3"],
        [
            "State the output intent (screen campaign vs print swatch).",
            "Convert or soft-proof once; screenshot before/after.",
            "Name one colour that shifted and whether the brief still holds.",
            "Save with profile noted in the filename or sidecar.",
        ],
        source_status="gap",
        gap_work="Platform colour-management docs [PLATFORM]; Profield colour literacy map",
        profield_runs=["dc-2d-image-craft-pedagogy", "digital-creativity"],
        time_min=20,
        evidence="gap — technical literacy from field map, not a verified HE sequence",
        summary="Output-intent colour check before polish.",
    ),
    M(
        "platform-tonal-edit-study",
        "Platform tonal/colour edit study",
        "colour",
        "critical",
        ["I.3"],
        [
            "Pick one own image and apply a time-bound platform look (not a brand template claim).",
            "List the tonal moves (contrast, warmth, saturation) without vendor myth.",
            "Compare to an unedited proof; mark what the edit sells.",
            "Write whether the edit is corrective or stylistic for this brief.",
        ],
        primary_source="roivainen-2025",
        source_status="verified",
        source_locator="p. 8 (time-bound platform colour/tonal editing conventions)",
        evidence="Roivainen 2025, 8",
        profield_runs=["digital-creativity"],
        time_min=25,
        summary="Study platform colour conventions as time-bound craft.",
    ),
    M(
        "palette-from-garment",
        "Palette from garment (not from trend tile)",
        "colour",
        "constructive",
        ["I.3", "I.7"],
        [
            "Sample five colours from a garment or fabric photo you own/rights-clear.",
            "Build a palette strip; forbid adding colours from moodboard tiles yet.",
            "Test the palette on a flat and on a key-visual crop.",
            "Note one clash that forced a hierarchy decision.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy", "dc-fashion-composition-references-pedagogy"],
        time_min=25,
        evidence="untested",
        summary="Derive palette from material evidence first.",
    ),
    M(
        "contrast-accessibility-pass",
        "Contrast / use-of-colour accessibility pass",
        "colour",
        "critical",
        ["I.3", "I.4"],
        [
            "Check text-on-image or label contrast against WCAG-minded thresholds for the deliverable class.",
            "Fix one failure without flattening the whole palette.",
            "State whether colour alone carries meaning; add a non-colour cue if yes.",
            "Record the check in the process note.",
        ],
        source_status="gap",
        gap_work="WCAG 2.2 [PLATFORM/standard]; Profield colour accessibility map",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=20,
        evidence="gap — standards literacy, not fashion-HE efficacy study",
        summary="Accessibility pass that separates contrast from colour-meaning.",
        accessibility="This method is itself an accessibility checkpoint.",
    ),
    M(
        "generative-face-bias-pause",
        "Generative-face bias pause",
        "colour",
        "critical",
        ["I.3", "I.4"],
        [
            "If using a generative face or skin tile, stop before compositing.",
            "Compare three outputs for homogenization patterns you can name.",
            "Either discard generative faces or document the bias risk in the process note.",
            "Prefer photographed or drawn faces you can attribute.",
        ],
        primary_source="aldahoul-2025",
        source_status="verified",
        source_locator="Scientific Reports 15 — generative faces and racial homogenization (Wave-1 verified claim)",
        evidence="AlDahoul et al. 2025 — tools not representationally neutral",
        profield_runs=["digital-creativity"],
        time_min=15,
        summary="Mandatory pause before generative face tiles enter a key visual.",
    ),
    # ——— composition ———
    M(
        "point-line-plane-looking",
        "Point / line / plane looking order",
        "composition",
        "constructive",
        ["I.4", "I.9", "ML-FIA"],
        [
            "On a still image, mark one point, one line, one plane that organise the read.",
            "Reorder emphasis (enlarge/reduce) once without changing content.",
            "Ask a peer which looking order they followed.",
            "Keep the annotated overlays with the deliverable.",
        ],
        primary_source="kandinsky-2012",
        source_status="verified",
        source_locator="p. 9 (point / line / plane looking order)",
        evidence="Kandinsky 2012, 9",
        profield_runs=["digital-creativity"],
        sandra_acts=["ACT2"],
        time_min=20,
        summary="Compositional looking order via point, line, plane.",
    ),
    M(
        "crop-as-argument",
        "Crop as argument",
        "composition",
        "critical",
        ["I.4", "I.7"],
        [
            "Make three crops of the same source with different claims (product, body, context).",
            "Caption each crop's claim in ≤8 words.",
            "Choose one; reject the others with a reason that is not 'looks better'.",
            "Archive rejects as process evidence.",
        ],
        primary_source="shinkle-2008",
        source_status="verified",
        source_locator="Fashion as Photograph — fashion photography as discursive practices (Wave-1 verified field claim)",
        evidence="Shinkle 2008 — framing crop as discursive choice",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=20,
        summary="Treat cropping as a claim, not a tidy-up.",
    ),
    M(
        "figure-ground-reversal",
        "Figure–ground reversal test",
        "composition",
        "constructive",
        ["I.4", "I.9"],
        [
            "Produce version A where the garment is figure; B where the setting is figure.",
            "Flip only masks/layers — do not redraw content if avoidable.",
            "Name which version serves the brief.",
            "Keep both for critique.",
        ],
        source_status="gap",
        gap_work="Gestalt figure–ground (arnheim-2004 gap)",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=25,
        evidence="gap",
        summary="Swap figure and ground to test hierarchy.",
    ),
    M(
        "visual-hierarchy-three-beats",
        "Visual hierarchy — three beats",
        "composition",
        "constructive",
        ["I.4", "I.7", "I.9"],
        [
            "Mark first / second / third read on a key visual with numbers.",
            "Force a reordering by changing scale or contrast once.",
            "Peer times the order with a finger-trace (no talking).",
            "Lock hierarchy that matches the brief's priority.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=20,
        evidence="untested",
        summary="Explicit first/second/third read for fashion images.",
    ),
    M(
        "iconic-vs-graphic-code",
        "Iconic vs graphic code split",
        "composition",
        "critical",
        ["I.7"],
        [
            "On a moodboard/key visual, label iconic meaning (what it depicts) vs graphic code (layout, type, format).",
            "Change only the graphic code once; keep iconic tiles fixed.",
            "State what the graphic change argued.",
            "Cite source tiles with creator/date/URL where known.",
        ],
        source_status="held",
        gap_work="Torri, Rodriguez Schon & Celi 2025 moodboard guideline (manifest gap keys nearby; not Wave-1 verified)",
        held_note="Profield composition run marks iconic/graphic split as emerging HE teaching aid.",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=30,
        evidence="held — Torri et al. 2025 not in references.yml",
        summary="Separate depicted meaning from layout code on boards.",
    ),
    # ——— bitmap ———
    M(
        "non-destructive-layer-discipline",
        "Non-destructive layer discipline",
        "bitmap",
        "workflow",
        ["I.3", "I.4", "II.1"],
        [
            "Forbid flattening until export; keep source layers named.",
            "Use adjustment layers / masks for every tonal move.",
            "Demonstrate undo of one local edit without affecting global grade.",
            "Hand in layered file + flat proof.",
        ],
        source_status="held",
        gap_work="FIT photographic post-production learning objectives / Adobe [PLATFORM] — Profield retouch map",
        held_note="Profield retouch run: non-destructive editing is HE learning objective language, not a page-verified sequence here.",
        profield_runs=["dc-fashion-retouch-pedagogy", "dc-2d-image-craft-pedagogy"],
        time_min=25,
        evidence="held",
        summary="Reversible layer workflow before any retouch claim.",
    ),
    M(
        "mask-precision-ladder",
        "Mask precision ladder",
        "bitmap",
        "constructive",
        ["I.4"],
        [
            "Cut the same subject with three mask qualities: rough, medium, precise.",
            "Composite each on an identical background.",
            "Pick the coarsest mask that still serves the brief.",
            "Note when precision became vanity.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=30,
        evidence="untested",
        summary="Stop masking past the brief's required precision.",
    ),
    M(
        "blend-mode-as-light",
        "Blend mode as light, not effect salad",
        "bitmap",
        "constructive",
        ["I.4"],
        [
            "Apply at most two blend modes with a stated lighting intent.",
            "Disable each to show contribution.",
            "Reject any mode you cannot explain in one sentence.",
            "Export with before/after strip.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=20,
        evidence="untested",
        summary="Limit blend modes to explainable light intent.",
    ),
    M(
        "contact-sheet-before-bash",
        "Contact sheet before photobash",
        "bitmap",
        "workflow",
        ["I.4", "I.7"],
        [
            "Grid all candidate stills with attribution lines visible.",
            "Strike images you cannot attribute or that fail rights.",
            "Only then enter the photobash canvas.",
            "Keep the contact sheet in the process folder.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=20,
        evidence="untested — supports visual citation discipline from Profield map",
        summary="Attributed contact sheet gate before collage.",
    ),
    M(
        "seam-honesty-check",
        "Seam honesty check",
        "bitmap",
        "critical",
        ["I.4"],
        [
            "Zoom to every photobash seam at 100%.",
            "Either craft the seam or leave it visible as collage grammar.",
            "Forbid 'auto-heal everything' as a default.",
            "Peer spots one dishonest seam; you fix or own it.",
        ],
        source_status="gap",
        profield_runs=["digital-creativity"],
        sandra_acts=["ACT2"],
        time_min=15,
        group_size="pairs",
        evidence="untested",
        summary="Own collage seams instead of hiding authorship.",
    ),
    # ——— form-volume ———
    M(
        "2d-to-3d-sequence-sketch",
        "2D→3D sequence sketch",
        "form-volume",
        "constructive",
        ["I.5", "I.6"],
        [
            "Sketch flat → side elevation → simple volume for one garment region.",
            "Mark one ambiguity that only 3D can resolve.",
            "State what you will test in digital volume next (without requiring CLO).",
            "Keep the three sketches as one strip.",
        ],
        primary_source="papahristou-2024",
        source_status="verified",
        source_locator="pp. 3, 5 (sequenced 2D→3D teaching structure in programmes)",
        evidence="Papahristou and Zolota Tatsi 2024, 3–5",
        profield_runs=["dc-3d-form-volume-pedagogy"],
        time_min=30,
        summary="Sketch the 2D→3D handoff before software volume.",
    ),
    M(
        "silhouette-from-volume",
        "Silhouette from volume study",
        "form-volume",
        "constructive",
        ["I.5", "I.6"],
        [
            "Block a garment as 2–4 volumes (no surface detail).",
            "Cast a single light; shade only mass.",
            "Trace the outer silhouette; discard interior noise.",
            "Compare to a flat of the same design.",
        ],
        source_status="held",
        gap_work="Moritz & Youn 2022 spatial visualization (manifest gap moritz-youn-2022)",
        held_note="Profield 3D map: spatial visualization / silhouette as durable terms.",
        profield_runs=["dc-3d-form-volume-pedagogy"],
        time_min=25,
        evidence="held",
        summary="Read silhouette from mass before detail.",
    ),
    M(
        "drape-observation-lite",
        "Drape observation (lite)",
        "form-volume",
        "constructive",
        ["I.5", "I.6"],
        [
            "Photograph or observe one fabric fold on a real object (rights-clear).",
            "Draw the fold as volume, then as line.",
            "Note stretch vs compression regions in one sentence each.",
            "Transfer one fold insight into a digital figurín sleeve or skirt.",
        ],
        source_status="gap",
        profield_runs=["dc-3d-form-volume-pedagogy", "dc-curriculum-gap-harvest"],
        time_min=30,
        evidence="gap — still-life→volume pipeline blank in Profield map",
        summary="Observe real drape once before digital cloth claims.",
        accessibility="Use a scarf on a chair if no dress form; photos OK.",
    ),
    M(
        "hybrid-analogue-digital-iteration",
        "Hybrid analogue/digital iteration",
        "form-volume",
        "workflow",
        ["I.6"],
        [
            "Make one analogue move (paper fold, tape, chalk) related to the brief.",
            "Photograph it; continue digitally without pretending the photo is final.",
            "State what digital could not invent without the analogue step.",
            "Keep both stages in the process trail.",
        ],
        primary_source="coats-2026",
        source_status="verified",
        source_locator="p. 8 (hybrid analogue/digital iteration; digital alone caveat)",
        evidence="Coats 2026, 8",
        profield_runs=["dc-3d-form-volume-pedagogy"],
        time_min=40,
        summary="Force one analogue step inside a digital volume brief.",
    ),
    M(
        "negative-space-garment",
        "Negative-space garment read",
        "form-volume",
        "constructive",
        ["I.5", "I.9"],
        [
            "Fill only the background around a garment silhouette.",
            "Judge volume from the leftover air.",
            "Correct the silhouette where negative space lies.",
            "Restore interior only after the air reads.",
        ],
        source_status="gap",
        profield_runs=["dc-3d-form-volume-pedagogy"],
        time_min=20,
        evidence="untested",
        summary="Use negative space to correct silhouette mass.",
    ),
    # ——— retouch ———
    M(
        "retouch-ethics-threshold",
        "Retouch ethics threshold",
        "retouch",
        "critical",
        ["I.4", "II.1"],
        [
            "List every planned body/skin/garment alteration before editing.",
            "Mark each as corrective, stylistic, or identity-altering.",
            "Refuse or disclose identity-altering edits for this brief.",
            "Peer challenges one borderline item.",
        ],
        source_status="gap",
        gap_work="McBride et al. 2019 (manifest mcbride-2019 gap); Profield retouch ethics map",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=20,
        group_size="pairs",
        evidence="gap — ethics awareness without invented syllabus efficacy",
        summary="Classify retouch intent before pixels move.",
    ),
    M(
        "beauty-vs-product-retouch-split",
        "Beauty vs product retouch split",
        "retouch",
        "workflow",
        ["II.1"],
        [
            "Separate layers: product geometry vs skin/beauty vs background.",
            "Complete product legibility first.",
            "Only then decide whether beauty retouch is needed for the brief.",
            "Export with layer groups intact.",
        ],
        source_status="held",
        held_note="Profield retouch map: beauty/product as practice descriptors, not settled pedagogy terms.",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=35,
        evidence="held",
        summary="Sequence product legibility before beauty polish.",
    ),
    M(
        "dodge-burn-discipline",
        "Dodge-and-burn discipline (local light)",
        "retouch",
        "constructive",
        ["II.1", "I.4"],
        [
            "On a soft-light grey layer, paint local light/shadow only.",
            "No liquify or generative fill in this pass.",
            "Toggle layer to prove contribution.",
            "Stop when form reads; do not chase skin perfection.",
        ],
        source_status="gap",
        gap_work="Professional craft; Profield notes no HE comparative sequence for dodge-burn vs frequency separation",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=25,
        evidence="gap",
        summary="Local light modelling without body reshape tools.",
    ),
    M(
        "disclosure-label-skepticism",
        "Disclosure-label skepticism drill",
        "retouch",
        "critical",
        ["II.1", "I.4"],
        [
            "Write a one-line 'retouched' disclaimer for your image.",
            "Argue why a disclaimer may not protect viewers (classroom discussion).",
            "Replace disclaimer-only thinking with a concrete edit refusal or redesign.",
            "Document the redesign choice.",
        ],
        source_status="held",
        gap_work="Danthinne et al. 2020 Body Image review (cited in Profield retouch map; not Wave-1 references.yml)",
        held_note="Profield: little support for disclaimer labels as protection — transfer boundary to studio practice.",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=20,
        evidence="held",
        summary="Do not treat disclaimer text as ethical completion.",
    ),
    # ——— still-motion ———
    M(
        "bodegon-balance-pass",
        "Digital bodegón balance pass",
        "still-motion",
        "synthetic",
        ["I.9"],
        [
            "Arrange 3–7 fashion objects; photograph or composite one frame.",
            "Name the heaviest visual weight and lighten or counter it once.",
            "Cross-reference one decision each from I.1–I.4 in the process note.",
            "Declare the gap: no verified bodegón teaching sequence.",
        ],
        source_status="gap",
        gap_work="Lesson I.9 declared gap; Profield still-life map",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=50,
        evidence="gap — synthesis exercise across prior units",
        summary="Balanced digital still-life as CD I synthesis craft.",
    ),
    M(
        "still-life-lighting-transfer",
        "Still-life lighting transfer",
        "still-motion",
        "constructive",
        ["I.9", "I.8"],
        [
            "Light a physical object with one key + fill (phone lights OK).",
            "Match the light direction in a digital composite of related products.",
            "List mismatches you could not solve in post.",
            "Prefer re-light over fake glow when possible.",
        ],
        source_status="held",
        held_note="Profield motion/still map: lighting/composition durable; transfer to digital blank.",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=40,
        evidence="held",
        summary="Match physical light before digital glow.",
        accessibility="Use window light if no lamps; document direction with a photo.",
    ),
    M(
        "solid-drawing-in-motion-frame",
        "Solid drawing check on a motion frame",
        "still-motion",
        "constructive",
        ["I.8"],
        [
            "Export one frame from a short fashion motion test.",
            "Redraw volume/weight/light on a tracing layer.",
            "Fix the motion pose where volume collapses.",
            "Reinsert the corrected still as a timing reference.",
        ],
        source_status="gap",
        gap_work="Animation 'solid drawing' principle as classroom craft; fashion animation pedagogy blank in Profield",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=30,
        evidence="gap",
        summary="Restore volume on a single motion frame.",
    ),
    M(
        "timing-vs-polish-split",
        "Timing vs polish split",
        "still-motion",
        "workflow",
        ["I.8"],
        [
            "Lock timing/holds on a rough pass with ugly placeholders.",
            "Only then replace placeholders with finished assets.",
            "Forbid polishing frames that will be cut.",
            "Show tutor the rough timing cut first.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=35,
        evidence="untested",
        summary="Separate motion timing from asset polish.",
    ),
    # ——— research ———
    M(
        "moodboard-as-research",
        "Moodboard as research (not collage décor)",
        "research",
        "critical",
        ["I.7"],
        [
            "State a research question the board must answer.",
            "Select images that argue; reject pretty-but-mute tiles.",
            "Annotate each tile with why it earns its place.",
            "Write a five-line synthesis that the board alone cannot say.",
        ],
        source_status="held",
        gap_work="Garner & McDonagh-Philp 2001; Cassidy 2011; de Wet 2017 (Profield composition run)",
        held_note="Profield ESTABLISHED: moodboard as qualitative design-research tool.",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=40,
        evidence="held — primary articles not yet in references.yml",
        summary="Force research question before moodboard aesthetics.",
    ),
    M(
        "critical-image-selection",
        "Critical image selection drill",
        "research",
        "critical",
        ["I.7"],
        [
            "Gather 20 candidates; keep 6 with written selection criteria.",
            "Name one surface-learning trap you avoided (familiarity, trend copy).",
            "Peer challenges one keep.",
            "Log rejected notables with reasons.",
        ],
        source_status="held",
        gap_work="de Wet 2017 fashion moodboard action research (Profield)",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=30,
        group_size="pairs",
        evidence="held",
        summary="Criteria-led selection against surface collage.",
    ),
    M(
        "visual-citation-block",
        "Visual citation block",
        "research",
        "workflow",
        ["I.7"],
        [
            "For every tile, record creator, title/desc, date, source URL/repo, license if known.",
            "Flag missing fields; replace or drop the tile.",
            "Print a citation block beside the board or in a sidecar file.",
            "No anonymous screenshots.",
        ],
        source_status="gap",
        gap_work="ACRL visual literacy standards (Profield); fashion consensus rubric blank",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        didactics=["didactics"],
        time_min=25,
        evidence="gap",
        summary="Bibliographic integrity for image tiles.",
    ),
    M(
        "search-politics-audit",
        "Search-politics audit",
        "research",
        "critical",
        ["I.7"],
        [
            "Run the same query in two engines or filters; capture first-screen grids.",
            "Name whose bodies/contexts dominate.",
            "Change one query term to surface missing contexts.",
            "Keep both grids as process evidence.",
        ],
        primary_source="campinho-2025",
        source_status="verified",
        source_locator="p. 2 (search results carry representational politics)",
        evidence="Campinho et al. 2025, 2",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=25,
        summary="Audit search grids before moodboard capture.",
    ),
    M(
        "trend-signal-to-board",
        "Trend signal → board translation",
        "research",
        "synthetic",
        ["I.7"],
        [
            "Name one cultural signal (not a brand drop).",
            "Collect evidence tiles that support or complicate it.",
            "Translate into colour/material/finish cues on the board.",
            "Write what remains speculation.",
        ],
        source_status="held",
        gap_work="Torri et al. 2025 Metadesign/trend→moodboard (Profield)",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=35,
        evidence="held",
        summary="Translate a cultural signal into visual research, not logo hunting.",
    ),
    # ——— presentation ———
    M(
        "key-visual-brief-lock",
        "Key-visual brief lock",
        "presentation",
        "workflow",
        ["I.3", "I.4"],
        [
            "Write audience, channel, and single claim before opening the canvas.",
            "Reject any layer that does not serve the claim.",
            "Export at channel size with margin/safe area checked.",
            "Attach the brief text to the submission.",
        ],
        source_status="gap",
        sandra_acts=["ACT2"],
        profield_runs=["digital-creativity"],
        time_min=15,
        evidence="untested — studio process for Sandra ACT2",
        summary="Lock key-visual brief before craft begins.",
    ),
    M(
        "export-for-channel",
        "Export for channel (web/print/social)",
        "presentation",
        "workflow",
        ["I.3", "I.4", "II.5"],
        [
            "Name target channel and max dimension/colour mode.",
            "Export proof; open on a second device or viewer.",
            "Fix one readability failure found off-canvas.",
            "Keep master layered file separate from delivery flat.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-portfolio-web-ux"],
        time_min=20,
        evidence="untested",
        summary="Channel-specific export with off-canvas check.",
    ),
    M(
        "portfolio-sequence-of-three",
        "Portfolio sequence of three",
        "presentation",
        "synthetic",
        ["I.9", "II.5"],
        [
            "Pick three process artefacts that show decision, not only finish.",
            "Order them so a stranger can reconstruct the argument.",
            "Write a 40-word caption for the set.",
            "Remove any image that only flatters.",
        ],
        source_status="gap",
        didactics=["didactics"],
        profield_runs=["dc-fashion-portfolio-web-ux"],
        time_min=25,
        evidence="untested",
        summary="Process-led portfolio trio for critique.",
    ),
    M(
        "taste-listening-counterpoint",
        "Taste / listening counterpoint",
        "presentation",
        "critical",
        ["I.1", "I.2"],
        [
            "Before tool polish, state what you are listening for in the work (material, mood, audience).",
            "Do one silent look at peer work without commenting on software.",
            "Return to your piece; change one decision that tools cannot make for you.",
            "Note the change without brand-tool language.",
        ],
        primary_source="rubin-2023",
        source_status="verified",
        source_locator="p. 123 (practitioner taste/listening counterpoint — Wave-1 verified locator)",
        evidence="Rubin 2023, 123 — practitioner counterpoint, not peer-reviewed pedagogy",
        profield_runs=["digital-creativity"],
        time_min=20,
        group_size="pairs",
        summary="Re-centre judgement over tool fluency.",
    ),
    # ——— critical-craft ———
    M(
        "authorship-declaration-strip",
        "Authorship declaration strip",
        "critical-craft",
        "critical",
        ["I.1", "I.4", "II.1"],
        [
            "List human decisions, automated assists, and generative assists used.",
            "Attach the strip to the deliverable footer or sidecar.",
            "Update the strip whenever the pipeline changes.",
            "Refuse empty 'AI-assisted' as a substitute for the list.",
        ],
        source_status="gap",
        didactics=["didactics"],
        profield_runs=["dc-fashion-retouch-pedagogy", "digital-creativity"],
        time_min=10,
        evidence="untested — aligns with course AI declaration practice",
        summary="Concrete authorship strip for craft pipelines.",
    ),
    M(
        "provenance-aware-export",
        "Provenance-aware export note",
        "critical-craft",
        "workflow",
        ["II.1", "I.4"],
        [
            "When tools offer Content Credentials / edit history, enable or document why not.",
            "Export a short edit ledger (manual is fine).",
            "State what a viewer cannot see from the flat alone.",
            "File the ledger with the master.",
        ],
        source_status="held",
        held_note="Profield retouch map: C2PA Content Credentials as emerging adjacent term.",
        gap_work="C2PA technical specs [PLATFORM/standard]",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=15,
        evidence="held",
        summary="Leave an inspectable edit ledger with the flat.",
    ),
    M(
        "refuse-harmful-ideal-edit",
        "Refuse harmful ideal edit",
        "critical-craft",
        "critical",
        ["II.1", "I.4"],
        [
            "Identify one edit that would slim/idealise a body beyond the brief's product need.",
            "Refuse it in writing; propose an alternative art direction.",
            "Peer confirms the refusal is real (not postponed).",
            "Keep the refusal note in process evidence.",
        ],
        source_status="gap",
        gap_work="Body-image transfer literature in Profield retouch map (not a studio efficacy RCT)",
        profield_runs=["dc-fashion-retouch-pedagogy"],
        time_min=15,
        group_size="pairs",
        evidence="gap",
        summary="Practise refusal of harmful idealisation as craft skill.",
    ),
    M(
        "fashion-photograph-reading",
        "Fashion photograph discursive reading",
        "critical-craft",
        "critical",
        ["I.1", "ML-FIA"],
        [
            "Choose one fashion photograph (rights-clear or course set).",
            "Name art/commerce tensions and who the image addresses.",
            "List three practices the image participates in (editorial, advertising, vernacular…).",
            "Connect one observation to your own making this week.",
        ],
        primary_source="shinkle-2008",
        source_status="verified",
        source_locator="Fashion as Photograph — wide array of practices; permeable art/commerce boundary",
        evidence="Shinkle 2008 — Wave-1 verified field claim",
        profield_runs=["digital-creativity"],
        time_min=25,
        summary="Read fashion photographs as discursive practices before remaking them.",
    ),
    M(
        "agency-in-reception-note",
        "Agency in reception note",
        "critical-craft",
        "critical",
        ["ML-FIA", "I.1"],
        [
            "Describe who acts when your image is viewed (author, platform, viewer).",
            "Mark one place where reception can refuse your intended claim.",
            "Adjust the craft once to leave room for that agency — or document why not.",
            "Keep the note with the critique sheet.",
        ],
        primary_source="eckersall-2017",
        source_status="verified",
        source_locator="pp. 218–219 (agency in reception; art vs media functions)",
        evidence="Eckersall, Grehan, and Scheer 2017, 218–219",
        profield_runs=["digital-creativity"],
        time_min=20,
        summary="Account for viewer agency in fashion-image craft.",
    ),
    # ——— extra craft coverage to reach ~55–65 ———
    M(
        "texture-sample-board",
        "Texture sample board",
        "research",
        "constructive",
        ["I.3", "I.7"],
        [
            "Photograph or scan three fabric textures you control rights for.",
            "Place them at equal scale; note weave/knit differences.",
            "Map each to a possible garment region on a flat.",
            "Forbid downloads of unlabeled texture packs.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-composition-references-pedagogy"],
        time_min=25,
        evidence="untested",
        summary="Rights-clear texture samples for digital material claims.",
    ),
    M(
        "line-weight-hierarchy",
        "Line-weight hierarchy",
        "drawing",
        "constructive",
        ["I.2"],
        [
            "Assign three line weights: structure, seam, surface.",
            "Apply consistently across one flat + figurín pair.",
            "Peer identifies structure without colour.",
            "Correct any weight that fights hierarchy.",
        ],
        source_status="gap",
        sandra_acts=["ACT1"],
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=20,
        evidence="untested",
        summary="Consistent line weights as readable craft grammar.",
    ),
    M(
        "colourway-swap-test",
        "Colourway swap test",
        "colour",
        "constructive",
        ["I.3"],
        [
            "Duplicate a finished flat; change only the colourway once.",
            "Check whether seams and logos still read.",
            "Decide which colourway carries the brief's claim.",
            "Archive both colourways.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        time_min=20,
        evidence="untested",
        summary="Swap colourways without redesigning construction.",
    ),
    M(
        "compositing-before-after-strip",
        "Compositing before/after strip",
        "bitmap",
        "workflow",
        ["I.4"],
        [
            "Save a dated before flat at the start of effects work.",
            "After compositing, build a horizontal before|after strip.",
            "Caption the transformation in ≤12 words without hype.",
            "Submit strip with the master.",
        ],
        source_status="gap",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT2"],
        time_min=15,
        evidence="untested",
        summary="Mandatory before/after strip for effects accountability.",
    ),
    M(
        "scale-consistency-pass",
        "Scale consistency pass",
        "composition",
        "constructive",
        ["I.4", "I.9"],
        [
            "Place a known reference (hand, card, mannequin) in frame or as overlay.",
            "Check every object against that scale.",
            "Fix or intentionally break scale with a written reason.",
            "Remove the reference for final only after the check.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=15,
        evidence="untested",
        summary="Scale audit before photoreal claims.",
    ),
    M(
        "avatar-fit-sanity",
        "Avatar fit sanity check",
        "form-volume",
        "critical",
        ["II.2", "I.5"],
        [
            "On a digital avatar/body form, list three fit risks visible from silhouette alone.",
            "Mark which risks need pattern change vs camera cheat.",
            "Refuse camera cheat for at least one risk; redesign instead.",
            "Document the choice.",
        ],
        source_status="gap",
        gap_work="Wave-1 firewall for CD II; method seeded for II.2 handoff",
        profield_runs=["dc-avatar-digital-fashion-pedagogy", "dc-3d-form-volume-pedagogy"],
        time_min=20,
        evidence="gap",
        summary="Fit risks before avatar glamour shots (CD II handoff seed).",
    ),
    M(
        "web-portfolio-chunking",
        "Web portfolio chunking",
        "presentation",
        "workflow",
        ["II.5"],
        [
            "Chunk one project into problem → process → outcome on three scroll sections.",
            "One image hero per section maximum.",
            "Check mobile width once.",
            "Remove decorative carousels that hide process.",
        ],
        source_status="gap",
        profield_runs=["dc-fashion-portfolio-web-ux"],
        time_min=30,
        evidence="untested",
        summary="Process-visible portfolio chunking for web (CD II handoff seed).",
    ),
    M(
        "motion-accessibility-check",
        "Motion accessibility check",
        "still-motion",
        "critical",
        ["I.8"],
        [
            "Verify pause/stop control for any looping motion.",
            "Check flash/strobe risk; reduce if unsure.",
            "Add captions or a still alternative for narrative motion.",
            "Record the WCAG-minded checks you ran.",
        ],
        source_status="gap",
        gap_work="WCAG 2.2 time-based media (Profield motion map)",
        profield_runs=["dc-fashion-motion-still-pedagogy"],
        time_min=15,
        evidence="gap",
        summary="Accessibility gate for fashion motion deliverables.",
        accessibility="This method is an accessibility checkpoint.",
    ),
    M(
        "productive-struggle-scaffold",
        "Productive-struggle scaffold (assignment-driven drawing)",
        "drawing",
        "workflow",
        ["I.2"],
        [
            "State the hard part of the brief before opening advanced tools.",
            "Complete a low-tool attempt that must fail informatively.",
            "Only then unlock one advanced tool that addresses the failure.",
            "Reflect: what did struggle teach that demos hid?",
        ],
        source_status="held",
        gap_work="Curcic 2024 studio drawing pedagogy (manifest curcic-2024 gap); Studio Thinking Engage & Persist (Profield 2D map)",
        held_note="Profield 2D map: scaffolding / differentiated assignment as durable terms.",
        profield_runs=["dc-2d-image-craft-pedagogy"],
        sandra_acts=["ACT1"],
        time_min=35,
        evidence="held",
        summary="Scaffold struggle before tool demos erase judgement.",
    ),
    M(
        "effects-disclosure-threshold",
        "Effects disclosure threshold",
        "bitmap",
        "critical",
        ["I.4"],
        [
            "Name the before state of the image (capture or base composite).",
            "List each effect as treatment vs claim-about-reality.",
            "Group decides a disclosure threshold for the cohort brief.",
            "Apply the threshold to your piece; document compliance.",
        ],
        source_status="gap",
        gap_work="I.4 McBride ethics gap; lesson declared effects-sequence gap",
        profield_runs=["digital-creativity"],
        sandra_acts=["ACT2"],
        time_min=20,
        group_size="small group",
        evidence="gap",
        summary="Cohort threshold for when effects become claims.",
    ),
]


def load_ref_keys() -> set[str]:
    data = yaml.safe_load(REFS.read_text())
    if isinstance(data, dict):
        return {str(k) for k in data.keys()}
    return set()


def validate(methods: list[dict], ref_keys: set[str]) -> None:
    bad: list[str] = []
    ids = [m["id"] for m in methods]
    if not (40 <= len(methods) <= 80):
        bad.append(f"count {len(methods)} outside 40..80")
    if len(ids) != len(set(ids)):
        bad.append("duplicate ids")
    for rid in REQUIRED_IDS:
        if rid not in ids:
            bad.append(f"missing required {rid}")
    for m in methods:
        if m["source_status"] == "verified":
            if m["primary_source"] not in ref_keys:
                bad.append(f"{m['id']}: verified but source not in references.yml")
            if not m.get("source_locator"):
                bad.append(f"{m['id']}: verified missing source_locator")
        if m["primary_source"] != "gap" and m["primary_source"] not in ref_keys:
            if m["source_status"] == "verified":
                pass  # already flagged
            elif m["source_status"] not in ("held", "gap"):
                bad.append(f"{m['id']}: bad source_status for unknown key")
        # Forbid CT-only technique language in ids/names
        blob = f"{m['id']} {m['name']}".lower()
        for needle in (
            "scamper",
            "six-thinking",
            "brainwriting",
            "oblique-strategies",
            "osborn",
            "synectic",
            "crazy-8",
            "mom-test",
            "cocd",
        ):
            if needle in blob:
                bad.append(f"{m['id']}: CT-technique leakage")
    if bad:
        raise SystemExit("validation failed:\n" + "\n".join(bad[:40]))


def build_profield_map(methods: list[dict]) -> dict:
    by_run: dict[str, list[str]] = {}
    for m in methods:
        for run in m.get("profield_runs") or []:
            by_run.setdefault(run, []).append(m["id"])
    return {
        "schema": "dc-fashion-craft-profield-map/v1",
        "phase": "EX7",
        "note": (
            "Maps catalogue method ids → Profield runs named in "
            "PROFIELD-AND-INFRA.md. Discovery only; citations still need Ahmes."
        ),
        "by_profield_run": {k: sorted(v) for k, v in sorted(by_run.items())},
        "sandra_act_methods": {
            "ACT1": sorted(
                m["id"] for m in methods if "ACT1" in (m.get("sandra_acts") or [])
            ),
            "ACT2": sorted(
                m["id"] for m in methods if "ACT2" in (m.get("sandra_acts") or [])
            ),
        },
        "findings_closed": ["C4"],
        "findings_partial": ["C3"],
    }


def public_seed(methods: list[dict]) -> dict:
    """Public-safe seed for EX10 method cards — no URNs, no gap_work prose claims."""
    cards = []
    for m in methods:
        # Seed includes ACT anchors + verified-source methods only (conservative).
        if m["id"] in REQUIRED_IDS or m["source_status"] == "verified":
            src_line = "Classroom adaptation (studio craft)."
            if m["source_status"] == "verified" and m["primary_source"] != "gap":
                src_line = (
                    f"Classroom adaptation; source line may cite "
                    f"`{m['primary_source']}` once EX10 cards hydrate references."
                )
            cards.append(
                {
                    "id": m["id"],
                    "title": m["name"],
                    "family": m["family"],
                    "units": m["units"],
                    "sandra_acts": m.get("sandra_acts") or [],
                    "summary": m["summary"],
                    "steps": m["steps"],
                    "time_min": m["time_min"],
                    "group_size": m["group_size"],
                    "materials": m["materials"],
                    "source_line": src_line,
                    "source_status": m["source_status"],
                    "card_ready": False,
                    "built_by_phase": "EX10",
                }
            )
    return {
        "schema": "dc-fashion-craft-method-cards-seed/v1",
        "phase": "EX7",
        "publication_note": (
            "Seed only. EX10 may build printable cards under docs/methods/en/cards/. "
            "Do not dump CT technique ids. Gap attributions must not appear as "
            "student-facing Source lines."
        ),
        "cards": cards,
    }


def reading_md(methods: list[dict], profield_map: dict) -> str:
    lines = [
        "# Canonical fashion-craft methods (PRIVATE)",
        "",
        "> Generated by `catalogue/emit_catalogue.py` / `build.py`. Never publish.",
        "> FINDINGS C4. Not a copy of CT techniques.",
        "",
        f"**Count:** {len(methods)} methods · **Required ACT anchors:** "
        + ", ".join(REQUIRED_IDS),
        "",
        "## By family",
        "",
        "| Family | Count |",
        "| --- | ---: |",
    ]
    from collections import Counter

    fam = Counter(m["family"] for m in methods)
    for k, v in sorted(fam.items()):
        lines.append(f"| {k} | {v} |")
    lines += [
        "",
        "## Sandra ACT map",
        "",
        f"- ACT1: {', '.join(profield_map['sandra_act_methods']['ACT1'])}",
        f"- ACT2: {', '.join(profield_map['sandra_act_methods']['ACT2'])}",
        "",
        "## Methods",
        "",
    ]
    for m in methods:
        lines.append(f"### `{m['id']}` — {m['name']}")
        lines.append("")
        lines.append(
            f"- **family/mode:** {m['family']} · {m['craft_mode']}"
        )
        lines.append(
            f"- **source:** {m['source_status']} · `{m['primary_source']}`"
            + (f" · {m['source_locator']}" if m.get("source_locator") else "")
        )
        if m.get("sandra_acts"):
            lines.append(f"- **Sandra:** {', '.join(m['sandra_acts'])}")
        lines.append(f"- **units:** {', '.join(m['units'])}")
        lines.append(f"- **time / group:** {m['time_min']} min · {m['group_size']}")
        lines.append(f"- **evidence:** {m['evidence']}")
        lines.append("- **steps:**")
        for s in m["steps"]:
            lines.append(f"  1. {s}")
        lines.append("")
    return "\n".join(lines) + "\n"


def strip_nulls(obj):
    if isinstance(obj, dict):
        return {k: strip_nulls(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [strip_nulls(x) for x in obj]
    return obj


def main() -> None:
    ref_keys = load_ref_keys()
    methods = [strip_nulls(m) for m in METHODS]
    validate(methods, ref_keys)

    base = {
        "schema": "dc-fashion-craft-methods/v1",
        "phase": "EX7",
        "publication_allowed": False,
        "note": (
            "Hand-authored fashion-craft studio methods for Creación Digital. "
            "NOT Creativity Techniques. Edit via emit_catalogue.py METHODS list "
            "or this file, then run build.py."
        ),
        "families": list(FAMILIES),
        "craft_modes": list(CRAFT_MODES),
        "required_ids": list(REQUIRED_IDS),
        "methods": methods,
    }
    (CAT / "methods.base.yml").write_text(
        yaml.dump(base, sort_keys=False, allow_unicode=True, width=96),
        encoding="utf-8",
    )

    canonical = {
        **base,
        "generated_by": "digital-creativity-pedagogy/catalogue/build.py",
        "findings": {"closes": ["C4"], "partial": ["C3"]},
    }
    (CAT / "CANONICAL-METHODS.yml").write_text(
        yaml.dump(canonical, sort_keys=False, allow_unicode=True, width=96),
        encoding="utf-8",
    )

    pmap = build_profield_map(methods)
    (CAT / "profield-map.yml").write_text(
        yaml.dump(pmap, sort_keys=False, allow_unicode=True, width=96),
        encoding="utf-8",
    )

    (CAT / "CANONICAL-METHODS.md").write_text(
        reading_md(methods, pmap), encoding="utf-8"
    )

    by_unit: dict[str, list[str]] = {}
    for m in methods:
        for u in m["units"]:
            by_unit.setdefault(u, []).append(m["id"])
    (CAT / "CANONICAL-METHODS-BY-UNIT.yml").write_text(
        yaml.dump(
            {
                "schema": "dc-fashion-craft-methods-by-unit/v1",
                "phase": "EX7",
                "by_unit": {k: sorted(v) for k, v in sorted(by_unit.items())},
            },
            sort_keys=False,
            allow_unicode=True,
            width=96,
        ),
        encoding="utf-8",
    )

    seed = public_seed(methods)
    SEED.parent.mkdir(parents=True, exist_ok=True)
    SEED.write_text(
        yaml.dump(seed, sort_keys=False, allow_unicode=True, width=96),
        encoding="utf-8",
    )

    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    (CARDS_DIR / "SEED.md").write_text(
        "---\n"
        "layout: default\n"
        "title: Fashion-craft method cards (seed)\n"
        "permalink: /methods/en/cards/\n"
        "lang: en\n"
        "---\n\n"
        "# Fashion-craft method cards — seed\n\n"
        "This path is the **EX7 public seed** for printable fashion-craft method cards.\n"
        "Cards are **not** built yet; a later assessment phase hydrates them from the\n"
        "seed dataset committed with this cascade.\n\n"
        "Studio methods only (figurín, photobash, Gestalt composition, and related craft).\n"
        "This page must **not** import Creativity Techniques catalogue IDs.\n",
        encoding="utf-8",
    )

    stats = {
        "method_count": len(methods),
        "verified": sum(1 for m in methods if m["source_status"] == "verified"),
        "held": sum(1 for m in methods if m["source_status"] == "held"),
        "gap": sum(1 for m in methods if m["source_status"] == "gap"),
        "seed_cards": len(seed["cards"]),
        "required_ids_present": list(REQUIRED_IDS),
    }
    (CAT / "catalogue-stats.json").write_text(
        json.dumps(stats, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
