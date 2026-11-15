# PHASE-C3 — Verify hubs, covers, gates

**Depends on:** C1 + C2 DONE

## Do

1. Confirm `http://127.0.0.1:4002/digital-creativity-uem/lessons/` and `:4003/.../lessons/` are site hubs (not WEBrick listings).  
2. Spot-check one DC + one CT lesson cover: `lesson-cover … is-svg-plane-ready` and ambient orbit while idle.  
3. Run each course’s publication / citation verify scripts if present.  
4. `PHASE-C3-REPORT.md`.

## Gate

- Both `/lessons/` return course HTML with hub title  
- Covers orbit (or documented reduced-motion exception)  
- Report status ∈ {DONE, PARTIAL, BLOCKED}
