# Verify log — PHASE-EX8.md

**Run by:** cascade-harness.sh (runner process, not the implementing session)
**Worktree:** /Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-8
**Commit:** a49365795655dd3b88c94a710951352cdea3ff34
**Started:** 2026-10-07T15:48:39Z

```
PASS: file digital-creativity-pedagogy/excellence/PHASE-EX8.md
PASS: file digital-creativity-pedagogy/catalogue/CANONICAL-METHODS.yml
PASS: lab sign-off file
PASS: lab sign-off approved_by
PASS: lab sign-off cites D1/D2
PASS: deck lab slides (exactly two + method_id + practises)
PASS: lesson B2 exercise cards
PASS: I.2 has no lab-3
PASS: validator --strict green
PASS: render-decks runs
PASS: jekyll build
FAIL: browser layout check
1280x720 i-1-fashion-image: 13 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 146px
1280x720 i-2-2d-drawing: 13 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 113px
1280x720 i-3-color-bitmaps: 13 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 146px
1280x720 i-4-effects: 12 slides, 3 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 261px
1280x720 i-5-three-dimensional-form: 10 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 261px
1280x720 fashion-image-analysis: 13 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 33.3–33.3px (floor 33.3); exercise headroom 112px
1920x1080 i-1-fashion-image: 13 slides, 2 timer(s), 0 failing; h1 50.4–50.4px (floor 50.4), sentence 38.0–38.0px (floor 38.0); exercise headroom 71px
file:///Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-8/scripts/tests/browser/deck-layout.mjs:107
  if (m.result?.exceptionDetails) throw new Error(JSON.stringify(m.result.exceptionDetails).slice(0, 400));
                                        ^

Error: {"exceptionId":1,"text":"Uncaught (in promise) ReferenceError: Reveal is not defined","lineNumber":0,"columnNumber":0,"exception":{"type":"object","subtype":"error","className":"ReferenceError","description":"ReferenceError: Reveal is not defined\n    at <anonymous>:5:3","objectId":"-5871429559033482208.9.1"}}
    at evaluate (file:///Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-8/scripts/tests/browser/deck-layout.mjs:107:41)
    at async file:///Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem-integration-excellence-8/scripts/tests/browser/deck-layout.mjs:199:19

Node.js v22.22.0
----
failures: 1
```

**Exit code:** 1
**Verdict:** exit-gate FAILED. Do not promote. Return the phase to IN_PROGRESS.
