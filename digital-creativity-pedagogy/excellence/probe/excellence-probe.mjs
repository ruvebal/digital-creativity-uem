#!/usr/bin/env node
/**
 * DC Excellence probe — Wave-1 (CD I I.1–I.9 + fashion-image-analysis).
 * Facts from the live tree only. EX11 hardens --targets.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "../../..");
const CASCADE = path.join(ROOT, "digital-creativity-pedagogy/excellence");

const args = process.argv.slice(2);
const flag = (name) => args.includes(name);
const argVal = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : null;
};

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walk(p, acc);
    else acc.push(p);
  }
  return acc;
}

function rel(p) {
  return path.relative(ROOT, p);
}

function gitHead() {
  try {
    return execSync("git rev-parse HEAD", { cwd: ROOT, encoding: "utf8" }).trim();
  } catch {
    return null;
  }
}

/** Strip Liquid-gated internal metadata (same switch as publication safety). */
function publicSource(markdown) {
  const out = [];
  let depth = 0;
  for (const line of markdown.split(/\r?\n/)) {
    if (line.includes("{% if site.publication.publish_internal_metadata %}")) {
      depth += 1;
      continue;
    }
    if (depth && line.includes("{% endif %}")) {
      depth -= 1;
      continue;
    }
    if (!depth) out.push(line);
  }
  return out.join("\n");
}

function countMatches(files, re) {
  let n = 0;
  const hits = [];
  for (const f of files) {
    if (!/\.(md|html|json)$/i.test(f)) continue;
    let text;
    try {
      text = fs.readFileSync(f, "utf8");
    } catch {
      continue;
    }
    if (f.endsWith(".md")) text = publicSource(text);
    if (re.test(text)) {
      n += 1;
      if (hits.length < 20) hits.push(rel(f));
    }
  }
  return { n, hits };
}

function labSlideCount(contentPath) {
  try {
    const j = JSON.parse(fs.readFileSync(contentPath, "utf8"));
    const slides = j.slides || j.deck?.slides || [];
    const labs = slides.filter(
      (s) =>
        s.slide_role === "lab_exercise" ||
        (typeof s.id === "string" && /^lab-\d/i.test(s.id)),
    );
    return labs.length;
  } catch {
    return null;
  }
}

function danglingSlots(contentPath) {
  try {
    const j = JSON.parse(fs.readFileSync(contentPath, "utf8"));
    const slides = j.slides || [];
    const assets = new Set((j.assets || []).map((a) => a.id || a.asset_id).filter(Boolean));
    const dang = [];
    for (const s of slides) {
      const id = s.asset_id;
      if (!id) continue;
      if (assets.size && !assets.has(id)) dang.push({ slide: s.id || s.slide_id, asset_id: id });
    }
    return dang;
  } catch {
    return [];
  }
}

function measure() {
  const lessonEn = walk(path.join(ROOT, "docs/lessons/en/digital-creativity-i")).filter((f) =>
    f.endsWith("index.md"),
  );
  const lessonEs = walk(path.join(ROOT, "docs/lessons/es/creacion-digital-i")).filter((f) =>
    f.endsWith("index.md"),
  );
  const specialEn = path.join(
    ROOT,
    "docs/lessons/en/master-lectures/fashion-image-analysis/index.md",
  );
  const decks = walk(path.join(ROOT, "docs/tracks/en/uem/2627-dci")).filter((f) =>
    f.endsWith("content.json"),
  );
  const mlDecks = walk(path.join(ROOT, "docs/tracks/en/uem/2627-ml")).filter((f) =>
    f.endsWith("content.json"),
  );
  const allDecks = [...decks, ...mlDecks];
  const cacheDir = path.join(ROOT, "docs/assets/images/profield-cache");
  const cacheFiles = walk(cacheDir);
  const php = cacheFiles.filter((f) => f.endsWith(".php"));

  const leakRe =
    /\b(Ahmes|Athanor|lesson-scribe|profield-cache|extraction\.db|DevIAC|vault path)\b/i;
  const lessonLeak = countMatches(lessonEn, leakRe);
  const specialLeak = fs.existsSync(specialEn)
    ? countMatches([specialEn], leakRe)
    : { n: 0, hits: [] };

  const labs_by_deck = {};
  const dangling_by_deck = {};
  let decks_ne_2_labs = [];
  for (const d of decks) {
    const key = path.basename(path.dirname(path.dirname(d))) || rel(d);
    const n = labSlideCount(d);
    labs_by_deck[rel(d)] = n;
    if (n !== null && n !== 2) decks_ne_2_labs.push({ deck: rel(d), labs: n });
    dangling_by_deck[rel(d)] = danglingSlots(d);
  }

  const planPdf = path.join(
    ROOT,
    "digital-creativity-pedagogy/cv/sources/Plan_de_trabajo_2026-27_Creacion_Digital_I-Sandra_Jimenez.pdf",
  );
  const guiaI = path.join(ROOT, "digital-creativity-pedagogy/cv/guides/1-creacion-digital-i.json");
  const guiaII = path.join(ROOT, "digital-creativity-pedagogy/cv/guides/3-creacion-digital-ii.json");

  let guia_weights = null;
  try {
    const g = JSON.parse(fs.readFileSync(guiaI, "utf8"));
    const rows = g.evaluation?.["Modalidad presencial"] || [];
    guia_weights = Object.fromEntries(rows.map((r) => [r.name, r.weight_percent]));
  } catch {
    guia_weights = null;
  }

  const evalPage = path.join(ROOT, "docs/evaluation/index.md");
  let public_mentions_55 = false;
  if (fs.existsSync(evalPage)) {
    public_mentions_55 = /55/.test(fs.readFileSync(evalPage, "utf8"));
  }

  return {
    measured_at: new Date().toISOString(),
    commit: gitHead(),
    root: ROOT,
    wave1: {
      lessons_en_cd_i: lessonEn.length,
      lessons_es_cd_i: lessonEs.length,
      en_es_parity_delta: lessonEn.length - lessonEs.length,
      fashion_image_analysis_en: fs.existsSync(specialEn),
      decks_dci_content_json: decks.length,
      decks_ml_content_json: mlDecks.length,
      profield_cache_files: cacheFiles.length,
      php_cache_files: php.length,
      lesson_infra_vocab_files: lessonLeak.n,
      lesson_infra_vocab_sample: lessonLeak.hits,
      special_infra_vocab: specialLeak.n > 0,
      labs_by_deck,
      decks_ne_2_labs,
      dangling_by_deck,
      dangling_total: Object.values(dangling_by_deck).reduce((a, b) => a + b.length, 0),
    },
    contract: {
      guia_i_path: rel(guiaI),
      guia_ii_path: rel(guiaII),
      guia_i_weights: guia_weights,
      guia_weights_expected: { tests: 55, caso: 15, proyectos: 20, cuaderno: 10 },
      evaluation_page_mentions_55: public_mentions_55,
      sandra_plan_pdf_present: fs.existsSync(planPdf),
      sandra_plan_pdf: rel(planPdf),
      coordination_md_present: fs.existsSync(path.join(CASCADE, "COORDINATION-SANDRA.md")),
      d2_equals_act3: true,
      sandra_act_weights_expected: { each_percent: 11.2, count: 4 },
    },
    findings_refs: ["A1", "A2", "A3", "A5", "B1", "B2", "C1", "E3"],
  };
}

function writeEvidence(name, obj) {
  const dir = path.join(CASCADE, "evidence");
  fs.mkdirSync(dir, { recursive: true });
  const p = path.join(dir, name);
  fs.writeFileSync(p, JSON.stringify(obj, null, 2) + "\n");
  return p;
}

const out = measure();

if (flag("--self-check")) {
  if (!out.wave1 || typeof out.wave1.lessons_en_cd_i !== "number") {
    console.error("self-check failed");
    process.exit(1);
  }
  console.log(JSON.stringify({ self_check: true, lessons: out.wave1.lessons_en_cd_i, commit: out.commit }, null, 2));
  process.exit(0);
}

if (flag("--write-baseline")) writeEvidence("baseline-EX0.json", out);
if (flag("--write-head")) writeEvidence("head-EX0.json", out);
const writeAs = argVal("--write");
if (writeAs) writeEvidence(path.basename(writeAs), out);

if (flag("--targets")) {
  const unmet = [];
  if (out.wave1.php_cache_files !== 0) unmet.push("php_cache_files");
  if (!out.contract.sandra_plan_pdf_present) unmet.push("sandra_plan_pdf");
  if (!out.contract.coordination_md_present) unmet.push("coordination_md");
  if (!out.contract.guia_i_weights) unmet.push("guia_i_weights");
  const result = {
    targets_met: unmet.length === 0,
    unmet_count: unmet.length,
    unmet,
    note: "EX0 soft targets; EX11 hardens Wave-1 content targets",
  };
  console.log(JSON.stringify(result, null, 2));
  process.exit(unmet.length === 0 ? 0 : 1);
}

console.log(JSON.stringify(out, null, 2));
