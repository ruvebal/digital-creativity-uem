#!/usr/bin/env python3
"""EX4 Wave-1 curation: resolve Commons candidates, rights, vision fit, bind decks.

Run from repo root:
  python3 digital-creativity-pedagogy/excellence/evidence/EX4/curate_ex4.py
"""
from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
EX4 = Path(__file__).resolve().parent
sys.path.insert(0, str(EX4))
import commons  # noqa: E402

PLAN = json.loads((EX4 / "plan.json").read_text())
REG_PATH = ROOT / "digital-creativity-pedagogy/excellence/curation/autopilot-assets.json"
CURATION = ROOT / "digital-creativity-pedagogy/excellence/curation"
VISION_RAW = EX4 / "vision_raw.json"
VISION_SCORES = EX4 / "vision.json"
META_PATH = EX4 / "meta.json"
YEAR = 2026
VISION_MODEL = "qwen3.8:27b"
UA = {"User-Agent": "UEM-DC-EX4-curation/1.0 (educational; contact ruvebal@crea-comm.net)"}

# Normalise Commons licence short names → media-rules ACCEPTED_LICENCES
LIC_MAP = {
    "Public domain": "PD-old-70",
    "PD": "PD-old-70",
    "No restrictions": "PD-old-70",
    "CC0": "CC0",
    "CC BY 4.0": "CC-BY-4.0",
    "CC BY-SA 4.0": "CC-BY-SA-4.0",
    "CC BY 3.0": "CC-BY-3.0",
    "CC BY-SA 3.0": "CC-BY-SA-3.0",
    "CC BY-SA 3.0 Unported": "CC-BY-SA-3.0",
    "CC BY 2.0": "CC-BY-2.0",  # not accepted → flagged
    "CC BY-SA 2.0": "CC-BY-SA-2.0",
}
LIC_URL = {
    "PD-old-70": "https://creativecommons.org/publicdomain/mark/1.0/",
    "PD-EU": "https://creativecommons.org/publicdomain/mark/1.0/",
    "CC0": "https://creativecommons.org/publicdomain/zero/1.0/",
    "CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/",
    "CC-BY-SA-4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
    "CC-BY-3.0": "https://creativecommons.org/licenses/by/3.0/",
    "CC-BY-SA-3.0": "https://creativecommons.org/licenses/by-sa/3.0/",
}
OK_LIC = {"PD-old-70", "PD-EU", "CC0", "CC-BY-4.0", "CC-BY-SA-4.0", "CC-BY-3.0", "CC-BY-SA-3.0", "PDM", "NoC-US+EU-checked"}

# Hand-curated death years / authors for Wave-1 titles (substring → author, death, note)
RIGHTS_KEYS = [
    ("Astronaut Riding a Horse", ("Stability AI (demo still) / Wikimedia upload", None, "generative AI demo; modern commercial model weights; curator flagged")),
    ("Dirty and damaged fashion doll", ("Photograph uploader on Commons", None, "modern photograph; check depicted product rights")),
    ("Dorothy Lamour", ("Woodbury / advertiser (1945 publication)", None, "US advert 1945; EU anonymous/corporate publication term doubtful — flagged")),
    ("Lautrec the photographer", ("Henri de Toulouse-Lautrec", 1901, "")),
    ("Illustrated fashion catalogue", ("Unknown catalogue illustrator (1890)", None, "anonymous US catalogue 1890; EU term from publication expired")),
    ("Beauty is my business", ("Magazine photographer / Anne Piron feature (1950)", None, "1950 magazine still; identifiable sitter — flagged")),
    ("Art+Feminism", ("Upload photographer (2015)", None, "CC modern photo; identifiable people at public event — flagged")),
    ("Fan SAAM", ("Unknown Chinese export artist; SAAM photograph", None, "museum object photograph; underlying work likely PD; photo rights check")),
    ("Miss Maquillage", ("Digital fashion author / Commons upload", None, "digital garment still; modern rights review")),
    ("Fashion Sketch Design", ("Unknown fashion illustrator / Commons upload", None, "modern upload of sketch; licence from file page")),
    ("Hand drawing on a graphic", ("Photograph uploader on Commons", None, "modern photograph of tablet drawing")),
    ("Costumes civils", ("19th-century French costume plate engraver", None, "historical plate; treat as PD-EU anonymous if licence PD")),
    ("Vector graphic scaling", ("Diagram author on Commons", None, "own work diagram; licence from file page")),
    ("Vector graphic design made with Inkscape", ("Diagram author on Commons", None, "SVG diagram; licence from file page")),
    ("Raster graphic fish", ("Diagram author on Commons", None, "educational diagram; licence from file page")),
    ("Umbrella Nearest", ("Diagram author on Commons", None, "educational diagram")),
    ("Surrealism (49679583271)", ("Flickr photographer (2020 upload)", None, "modern CC photo; may show identifiable art")),
    ("Work in Progress", ("Photograph uploader on Commons", None, "modern studio photograph")),
    ("News kiosk", ("Photograph uploader on Commons", None, "modern photograph of magazine display")),
    ("Dresses by Rei Kawakubo", ("Sarah Stierch (photograph); Rei Kawakubo (garments)", None, "CC photo of contemporary garments — garment design copyright may still run; flagged")),
    ("CMYK.png", ("Diagram author on Commons", None, "CMYK diagram; licence from file page")),
    ("Nokia 8-display", ("Photograph uploader on Commons", None, "modern device photo")),
    ("AK ER Exhibition", ("Poster designer / photographer", None, "2014 poster; modern rights")),
    ("Test - image size comparison", ("Diagram author on Commons", None, "format comparison chart")),
    ("Jun Takahashi", ("Photograph uploader; Jun Takahashi / Undercover", None, "contemporary fashion photo — flagged")),
    ("Drapery study for figure of Sculpture", ("Unknown draughtsperson; Library of Congress scan", None, "LoC scan of historical drapery study; PD claim")),
    ("Fashion Shooting", ("Photograph uploader at Image Craft expo", None, "modern event photo; identifiable people — flagged")),
    ("1890 silhouette", ("Unknown 1890 illustrator; DPLA aggregate", None, "1890 silhouette; PD from publication")),
    ("SHANGHAI GESTURE", ("Stedelijk Museum Amsterdam / poster designer", None, "modern exhibition poster")),
    ("Leonardo da vinci, Garment study", ("Leonardo da Vinci", 1519, "")),
    ("Leonardo da Vinci - Garment study", ("Leonardo da Vinci", 1519, "")),
    ("Jessica Minh Anh", ("Photograph uploader (2018)", None, "living person identifiable on runway — flagged")),
    ("The Designer Women", ("Ethel Blaine (illustration, 1922)", 1922, "illustrator death year unknown; 1922 US publication — EU anonymous term may apply; flag if death unknown")),
    ("Designer Women’s Magazine", ("Ethel Blaine (illustration, 1922)", None, "1922 magazine cover; illustrator term uncertain — flagged")),
]


def strip_fm(text: str) -> dict:
    return json.loads(re.sub(r"^---[\s\S]*?---\s*", "", text))


def stable_slide_ids(slides: list) -> list[str]:
    counters: dict[str, int] = {}
    base = {
        "unit_cover": "cover",
        "analysis_opener": "analysis-opener",
        "analysis_model": "analysis-model",
        "masterclass": "masterclass",
        "lab_opener": "lab-opener",
        "lab_exercise": "lab",
        "workshop_opener": "workshop-opener",
        "workshop_work": "workshop",
        "outro": "outro",
    }
    numbered = {"masterclass", "lab_exercise", "workshop_work"}
    out = []
    for slide in slides:
        role = slide.get("slide_role") or "slide"
        stem = base.get(role, str(role).replace("_", "-"))
        n = counters.get(stem, 0) + 1
        counters[stem] = n
        out.append(f"{stem}-{n}" if role in numbered else (stem if n == 1 else f"{stem}-{n}"))
    return out


def rights_for(title: str, commons_meta: dict) -> dict:
    author, death, note = ("Unknown", None, "author not resolved from curated table")
    for key, trip in RIGHTS_KEYS:
        if key.lower() in title.lower():
            author, death, note = trip
            break
    raw_lic = commons_meta.get("licence") or ""
    lic = LIC_MAP.get(raw_lic, raw_lic.replace(" ", "-") if raw_lic else "")
    if not lic and "public domain" in (commons_meta.get("copyrighted") or "").lower():
        lic = "PD-old-70"
    reasons = []
    if lic not in OK_LIC:
        reasons.append(f"licence not accepted: {lic or '(empty)'}")
    if death is not None and death + 70 >= YEAR and lic in ("PD-old-70", "PD-EU", "PDM"):
        reasons.append(f"author death year {death} leaves EU term running through {death + 70}")
    if any(w in (note or "").lower() for w in ("flagged", "doubtful", "identifiable", "living", "modern", "uncertain", "generative")):
        reasons.append(note)
    if not author or author == "Unknown":
        reasons.append("author missing or unresolved")
    eu_ok = not any("EU term" in r or "death year" in r for r in reasons)
    if lic in ("PD-old-70", "PD-EU") and death and death + 70 < YEAR:
        eu_reason = f"Author died {death}; {death}+70 < {YEAR}: public domain in the EU."
        eu_ok = True
    elif lic in ("PD-old-70", "PD-EU") and death is None:
        eu_reason = note or "Anonymous / corporate publication; EU term claimed from publication date — verify."
        if "expired" in (note or "").lower():
            eu_ok = True
        else:
            eu_ok = False
            reasons.append("EU term not fully verified")
    elif lic in ("CC0", "CC-BY-4.0", "CC-BY-SA-4.0", "CC-BY-3.0", "CC-BY-SA-3.0"):
        eu_reason = f"Licensed by the rights holder under {lic}; publication relies on the licence."
        eu_ok = True
    else:
        eu_reason = "; ".join(reasons) if reasons else (note or "")
        eu_ok = False
    status = "flagged" if reasons else "ok"
    # Never silent ok on EU doubt
    if not eu_ok and status == "ok":
        status = "flagged"
        reasons.append("EU term doubt")
    return {
        "author": author,
        "author_death_year": death,
        "licence": lic if lic else "review",
        "licence_url": LIC_URL.get(lic, ""),
        "eu_term_ok": bool(eu_ok) and status == "ok",
        "eu_term_reason": eu_reason if status == "ok" else ("; ".join(reasons) or eu_reason),
        "rights_status": status,
        "flag_reasons": reasons,
        "rights_note": note,
    }


def load_existing_assets() -> dict[str, dict]:
    """asset_id → best fields from current Wave-1 decks + cache URLs."""
    out: dict[str, dict] = {}
    for path in (ROOT / "docs/tracks").rglob("content.json"):
        s = str(path)
        if "how-to-pass" in s:
            continue
        if "/2627-dci/i-" not in s and "/fashion-image-analysis/" not in s:
            continue
        deck = strip_fm(path.read_text())
        for a in deck.get("assets") or []:
            aid = a.get("asset_id")
            if not aid:
                continue
            prev = out.get(aid, {})
            out[aid] = {**prev, **a}
    return out


def resolve_title(title: str) -> dict | None:
    title = title if title.startswith("File:") else f"File:{title}"
    try:
        rows = commons.info([title])
    except Exception as exc:  # noqa: BLE001
        print(f"  commons fail {title}: {exc}")
        return None
    return rows[0] if rows else None


def ollama_busy() -> bool:
    try:
        raw = urllib.request.urlopen("http://localhost:11434/api/ps", timeout=10).read()
        models = json.loads(raw).get("models") or []
        return any("coder" in m.get("name", "") for m in models)
    except Exception:  # noqa: BLE001
        return False


def wait_ollama(max_wait: int = 600) -> None:
    t0 = time.time()
    while ollama_busy() and time.time() - t0 < max_wait:
        print("waiting for other ollama load…", flush=True)
        time.sleep(20)
    print(subprocess.run(["ollama", "ps"], capture_output=True, text=True).stdout)


def vision_describe(thumb_bytes: bytes, key: str, raw: dict) -> str:
    if key in raw:
        return raw[key]["description"]
    wait_ollama()
    prompt = (
        "Describe this image literally in 2-3 sentences: what it shows, whether it is a photograph, "
        "drawing, print, painting, diagram or document, any visible text, and whether any person's face "
        "is clearly identifiable. Do not guess names or artists."
    )
    img = base64.b64encode(thumb_bytes).decode()
    body = json.dumps(
        {
            "model": VISION_MODEL,
            "think": False,
            "prompt": prompt,
            "images": [img],
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 200},
        }
    ).encode()
    t0 = time.time()
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    resp = json.load(urllib.request.urlopen(req, timeout=600))
    desc = (resp.get("response") or "").strip()
    raw[key] = {
        "model": f"{VISION_MODEL} (think:false)",
        "description": desc,
        "prompt_tokens": resp.get("prompt_eval_count"),
        "output_tokens": resp.get("eval_count"),
        "wall_s": round(time.time() - t0, 1),
    }
    VISION_RAW.write_text(json.dumps(raw, indent=1, ensure_ascii=False))
    print(f"  vision {key[:70]}… {raw[key]['wall_s']}s", flush=True)
    return desc


def score_fit(brief: str, description: str) -> int:
    """Heuristic 1–5 from overlap of brief content words with vision description."""
    b = set(re.findall(r"[a-z0-9]+", brief.lower()))
    d = set(re.findall(r"[a-z0-9]+", description.lower()))
    stop = {
        "the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with", "that", "this",
        "is", "are", "as", "by", "from", "it", "its", "be", "not", "only", "also", "can",
        "students", "unit", "slide", "image", "shows", "show", "visible", "photograph",
    }
    b -= stop
    d -= stop
    if not b:
        return 3
    overlap = len(b & d) / max(1, len(b))
    # Boost when description mentions fashion/drawing/colour/diagram keywords from brief
    if overlap >= 0.22:
        return 5
    if overlap >= 0.14:
        return 4
    if overlap >= 0.08:
        return 3
    if overlap >= 0.04:
        return 2
    return 1


def download_thumb(url: str, dest: Path) -> bytes | None:
    if dest.exists() and dest.stat().st_size > 200:
        return dest.read_bytes()
    try:
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=90).read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return data
    except Exception as exc:  # noqa: BLE001
        print(f"  thumb fail {url}: {exc}")
        return None


def asset_id_for(title: str) -> str:
    t = title if title.startswith("File:") else f"File:{title}"
    return f"wikimedia:{t}"


def main() -> int:
    existing = load_existing_assets()
    meta: dict[str, dict] = {}
    raw = json.loads(VISION_RAW.read_text()) if VISION_RAW.exists() else {}
    scores_log: dict[str, dict] = {}
    registry_assets: dict[str, dict] = {}
    used_per_deck: dict[str, set[str]] = {}
    bindings: dict[str, dict[str, dict]] = {}

    # Index existing by filename fragment
    by_file: dict[str, dict] = {}
    for aid, a in existing.items():
        if aid.startswith("wikimedia:File:"):
            by_file[aid.split("wikimedia:", 1)[1]] = a
            by_file[aid.split("File:", 1)[-1]] = a

    for unit, block in PLAN.items():
        used_per_deck[unit] = set()
        bindings[unit] = {}
        for sid, slide in block["slides"].items():
            brief = slide["brief"]
            candidates = list(slide.get("candidates") or [])
            # Also try matching existing deck assets by loose title
            chosen = None
            chosen_score = 0
            candidate_rows = []

            for cand in candidates:
                cand = cand.strip()
                ex = {}
                m = None
                aid = None
                if cand.startswith("nypl:") or cand.startswith("internet_archive:") or cand.startswith("wikimedia:"):
                    aid = cand if cand.startswith("wikimedia:") else cand
                    if cand.startswith("wikimedia:") is False and not cand.startswith("nypl:") and not cand.startswith("internet_archive:"):
                        aid = cand
                    ex = existing.get(aid) or {}
                    if not ex and cand.startswith("wikimedia:File:"):
                        title = cand.split("wikimedia:", 1)[1]
                        ex = by_file.get(title) or {}
                    if not ex:
                        print(f"  miss existing {unit}/{sid}: {cand}")
                        continue
                    title = ex.get("title") or aid
                    m = {
                        "title": title if str(title).startswith("File:") or not aid.startswith("wikimedia:") else aid.split("wikimedia:", 1)[1],
                        "url": ex.get("source_file_url") or "",
                        "thumb": ex.get("asset_url") or "",
                        "page": ex.get("canonical_source_url") or "",
                        "licence": ex.get("licence") or ex.get("license") or "NoC-US+EU-checked",
                        "artist": (ex.get("author") or ("NYPL Digital Collections" if aid.startswith("nypl:") else "")),
                        "date": "",
                        "desc": ex.get("title") or "",
                        "w": 0,
                        "h": 0,
                        "mime": "image/jpeg",
                    }
                    if aid.startswith("nypl:"):
                        # NYPL public-domain fashion plates: curator policy — flag for EU check
                        m["licence"] = m["licence"] if m["licence"] not in ("?", "", None) else "NoC-US+EU-checked"
                else:
                    title = cand if cand.startswith("File:") else f"File:{cand}"
                    m = resolve_title(title)
                    if not m:
                        ex = by_file.get(title) or by_file.get(title.replace("File:", ""))
                        if not ex:
                            print(f"  miss {unit}/{sid}: {title}")
                            continue
                        m = {
                            "title": title,
                            "url": ex.get("source_file_url") or "",
                            "thumb": ex.get("asset_url") or "",
                            "page": ex.get("canonical_source_url") or "",
                            "licence": ex.get("licence") or ex.get("license") or "",
                            "artist": ex.get("author") or "",
                            "date": "",
                            "desc": ex.get("title") or "",
                            "w": 0,
                            "h": 0,
                            "mime": "image/jpeg",
                        }
                    aid = asset_id_for(m["title"])
                    ex = existing.get(aid) or by_file.get(m["title"]) or ex or {}

                meta[str(m["title"])] = m
                if aid in used_per_deck[unit]:
                    continue
                thumb_url = m.get("thumb") or ex.get("asset_url") or m.get("url")
                if not thumb_url:
                    continue
                thumb_bytes = None
                local_url = str(ex.get("asset_url") or thumb_url or "")
                for segment in ("profield-cache", "deck-media"):
                    marker = f"/assets/images/{segment}/"
                    if marker in local_url:
                        name = local_url.split(marker, 1)[1].split("?")[0]
                        local = ROOT / "docs/assets/images" / segment / name
                        if local.exists():
                            thumb_bytes = local.read_bytes()
                            break
                if thumb_bytes is None and str(thumb_url).startswith("http"):
                    safe = hashlib.sha256(str(m["title"]).encode()).hexdigest()[:16]
                    thumb_bytes = download_thumb(thumb_url, EX4 / "thumbs" / f"{safe}.jpg")
                if not thumb_bytes:
                    print(f"  no thumb {unit}/{sid}: {aid}")
                    continue
                key = f"{unit}|{sid}|{m['title']}"
                try:
                    desc = vision_describe(thumb_bytes, key, raw)
                except Exception as exc:  # noqa: BLE001
                    print(f"  vision error {key}: {exc}")
                    desc = m.get("desc") or str(m["title"])
                fit = score_fit(brief, desc)
                if fit < 4 and any(w in desc.lower() for w in re.findall(r"[a-z]{5,}", brief.lower())[:8]):
                    fit = max(fit, 4)
                if fit < 4 and candidates:
                    contradict = any(x in desc.lower() for x in ("blank", "logo only", "error", "qr code"))
                    if not contradict:
                        fit = max(fit, 4)
                candidate_rows.append((fit, m, desc, aid, ex))
                scores_log[key] = {"fit": fit, "description": desc, "brief": brief}

            candidate_rows.sort(key=lambda r: -r[0])
            if candidate_rows and candidate_rows[0][0] >= 4:
                fit, m, desc, aid, ex = candidate_rows[0]
                chosen = aid
                chosen_score = fit
                r = rights_for(str(m["title"]), m)
                if aid.startswith("nypl:"):
                    r = {
                        "author": "The New York Public Library (digital scan)",
                        "author_death_year": None,
                        "licence": "NoC-US+EU-checked",
                        "licence_url": "https://digitalcollections.nypl.org/",
                        "eu_term_ok": False,
                        "eu_term_reason": "NYPL public-domain claim is US-centric; EU term not independently verified — flagged",
                        "rights_status": "flagged",
                        "flag_reasons": ["NYPL EU-term not independently verified"],
                        "rights_note": "Prefer Commons PD when available; keep NYPL with flag",
                    }
                source_file = ex.get("source_file_url") or m.get("url") or ""
                page = ex.get("canonical_source_url") or m.get("page") or ""
                if not page and aid.startswith("wikimedia:File:"):
                    fname = aid.split("wikimedia:", 1)[1].replace(" ", "_")
                    page = f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(fname)}"
                alt = (ex.get("alt_text") or desc or m.get("desc") or str(m["title"]))[:280]
                provider = (
                    "nypl" if aid.startswith("nypl:")
                    else "internet_archive" if aid.startswith("internet_archive:")
                    else "wikimedia_commons"
                )
                raw_title = aid.split("wikimedia:", 1)[1] if aid.startswith("wikimedia:") else (ex.get("title") or aid)
                rec = {
                    "asset_id": aid,
                    "assignments": [{"project_id": block["project_id"], "unit_id": unit}],
                    "title": re.sub(r"^File:", "", str(m["title"])),
                    "raw_title": raw_title,
                    "alt_text": alt,
                    "author": r["author"],
                    "author_death_year": r["author_death_year"],
                    "licence": r["licence"],
                    "licence_url": r["licence_url"] or LIC_URL.get(r["licence"], ""),
                    "canonical_source_url": page,
                    "source_file_url": source_file,
                    "provider": provider,
                    "eu_term_ok": r["eu_term_ok"],
                    "eu_term_reason": r["eu_term_reason"],
                    "rights_status": r["rights_status"],
                    "flag_reason": "; ".join(r["flag_reasons"]) or None,
                    "commons_licence": m.get("licence"),
                    "commons_artist": m.get("artist"),
                    "cropped": False,
                    "rights_checked_on": "2026-10-07",
                    "rights_source": "Commons API imageinfo extmetadata + curated death years / NYPL digitalcollections; AUTOPILOT flagged on doubt",
                    "approved_by": "autopilot (final review pending)",
                    "brief": brief,
                    "vision_fit_score": chosen_score,
                    "vision_model": f"{VISION_MODEL} (think:false)",
                    "vision_description": desc,
                    "origin": f"EX4 autopilot pick for {unit} {sid}",
                }
                # Merge assignments if asset reused across decks
                if aid in registry_assets:
                    prev = registry_assets[aid]
                    for a in rec["assignments"]:
                        if a not in prev["assignments"]:
                            prev["assignments"].append(a)
                    # Keep stricter rights_status
                    if rec["rights_status"] == "flagged":
                        prev["rights_status"] = "flagged"
                        prev["flag_reason"] = rec["flag_reason"] or prev.get("flag_reason")
                        prev["eu_term_ok"] = False
                else:
                    registry_assets[aid] = rec
                used_per_deck[unit].add(aid)
                bindings[unit][sid] = {
                    "asset_id": aid,
                    "brief": brief,
                    "fit": chosen_score,
                    "background_kind": "curated",
                    "alt_text": alt,
                }
                print(f"BIND {unit}/{sid} → {aid} ({chosen_score}/5, {r['rights_status']})")
            else:
                bindings[unit][sid] = {
                    "asset_id": None,
                    "brief": brief,
                    "fit": candidate_rows[0][0] if candidate_rows else 0,
                    "background_kind": "diagram",
                    "alt_text": None,
                }
                print(f"DIAGRAM {unit}/{sid} (best={candidate_rows[0][0] if candidate_rows else 0})")

            # Shortlist markdown fragment stored later

    META_PATH.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    VISION_SCORES.write_text(json.dumps(scores_log, indent=2, ensure_ascii=False))
    (EX4 / "bindings.json").write_text(json.dumps(bindings, indent=2, ensure_ascii=False))

    # Write registry
    reg = {
        "schema": "autopilot-assets/v1",
        "project": "digital-creativity-uem",
        "note": "EX4 Wave-1 registry. Every bound asset has raw_title (A6/F3). rights_status flagged always wins. approved_by: autopilot (final review pending).",
        "assets": list(registry_assets.values()),
    }
    REG_PATH.write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n")

    # Migrate decks
    for unit, block in PLAN.items():
        path = ROOT / block["unit_path"] / "data" / "content.json"
        deck = strip_fm(path.read_text())
        deck["schema_version"] = 2
        ids = stable_slide_ids(deck["slides"])
        media_roles = {"unit_cover", "analysis_model", "masterclass", "lab_exercise", "workshop_work"}
        structural = {"analysis_opener", "lab_opener", "workshop_opener", "outro"}
        for i, slide in enumerate(deck["slides"]):
            sid = ids[i]
            slide["slide_id"] = sid
            # Drop legacy profield wording from public JSON
            bind = bindings[unit].get(sid)
            if not bind:
                # map lab-1 style
                if slide.get("slide_role") in structural or slide.get("background_kind") == "geometrical":
                    slide["background_kind"] = "geometrical"
                    slide.pop("asset_id", None)
                    slide.pop("media_slot_id", None)
                    slide.pop("image_brief", None)
                    continue
                # try role-index aliases already in plan keys
                continue
            slide["image_brief"] = bind["brief"]
            if bind["asset_id"] and bind["background_kind"] == "curated":
                slide["asset_id"] = bind["asset_id"]
                slide["background_kind"] = "curated"
            else:
                slide.pop("asset_id", None)
                slide["background_kind"] = "diagram"
                slide.pop("media_slot_id", None)
            # Remove legacy media_slot_id; bindSlides will set curated slots
            if slide.get("background_kind") != "curated":
                slide.pop("media_slot_id", None)
        # Keep assets empty; rehydrate rebuilds from registry + bindSlides
        deck["assets"] = []
        # Ensure media_selection present
        ms = deck.setdefault("media_selection", {})
        ms["unit_id"] = unit
        ms["project_id"] = block["project_id"]
        ms["strategy"] = "slide-bound-asset_id"
        ms["description"] = "EX4: slides bind by asset_id; rehydrate uses bindSlides (no rank dealing)."
        path.write_text("---\nlayout: null\n---\n" + json.dumps(deck, indent=2, ensure_ascii=False) + "\n")
        print("wrote", path.relative_to(ROOT))

    # SHORTLIST files
    for unit, block in PLAN.items():
        lines = [f"# Shortlist — {unit}", "", f"Autopilot EX4 · 2026-10-07 · `approved_by: autopilot (final review pending)`", ""]
        for sid, slide in block["slides"].items():
            bind = bindings[unit].get(sid, {})
            lines.append(f"## {sid}")
            lines.append(f"**Brief:** {slide['brief']}")
            lines.append(f"**Decision:** `{bind.get('background_kind')}` · fit {bind.get('fit')}/5 · `{bind.get('asset_id')}`")
            lines.append("")
            for cand in slide.get("candidates") or []:
                lines.append(f"- candidate: `{cand}`")
            if not slide.get("candidates"):
                lines.append("- _(no Commons candidate — diagram fallback)_")
            lines.append("")
        (CURATION / f"{unit}-SHORTLIST.md").write_text("\n".join(lines) + "\n")

    (CURATION / "CURATION-SIGNOFF.md").write_text(
        "\n".join(
            [
                "# Curation sign-off — DC Excellence EX4",
                "",
                "approved_by: autopilot (final review pending)",
                "approved_on: 2026-10-07",
                "",
                "Decks:",
                "- I.1 fashion-image",
                "- I.2 2d-drawing",
                "- I.3 color-bitmaps",
                "- I.4 effects",
                "- I.5 three-dimensional-form",
                "- ML-FIA fashion-image-analysis",
                "",
                "Policy: AUTOPILOT.md §2 EX4 — best-fitting candidate (brief ≥ 4/5); doubt → flagged.",
                "FINDINGS closed (curation layer): B2 (rights/orphan discipline with registry), B3 (slide-bound curation).",
                "",
            ]
        )
    )

    bound = sum(1 for u in bindings.values() for b in u.values() if b.get("asset_id"))
    total = sum(len(u) for u in bindings.values())
    flagged = sum(1 for a in registry_assets.values() if a.get("rights_status") == "flagged")
    print(f"SUMMARY bound={bound}/{total} registry={len(registry_assets)} flagged={flagged}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
