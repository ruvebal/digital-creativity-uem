#!/usr/bin/env node
/**
 * DC Excellence probe — Wave-1 readiness measurements.
 * EX0 expands metrics; --self-check proves the harness can run the probe.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "../../..");

const args = new Set(process.argv.slice(2));

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walk(p, acc);
    else acc.push(p);
  }
  return acc;
}

function countMatches(files, re) {
  let n = 0;
  const hits = [];
  for (const f of files) {
    if (!/\.(md|html|json)$/i.test(f)) continue;
    const text = fs.readFileSync(f, "utf8");
    if (re.test(text)) {
      n += 1;
      if (hits.length < 12) hits.push(path.relative(ROOT, f));
    }
  }
  return { n, hits };
}

function measure() {
  const lessonRoot = path.join(ROOT, "docs/lessons/en/digital-creativity-i");
  const lessons = walk(lessonRoot).filter((f) => f.endsWith("index.md"));
  const decks = walk(path.join(ROOT, "docs/tracks/en/uem/2627-dci")).filter((f) =>
    f.endsWith("content.json"),
  );
  const cacheDir = path.join(ROOT, "docs/assets/images/profield-cache");
  const cacheFiles = walk(cacheDir);
  const php = cacheFiles.filter((f) => f.endsWith(".php"));
  const leakRe =
    /\b(Ahmes|Athanor|lesson-scribe|profield-cache|extraction\.db|DevIAC)\b/i;
  const lessonLeak = countMatches(lessons, leakRe);

  return {
    measured_at: new Date().toISOString(),
    root: ROOT,
    wave1: {
      lessons_en_cd_i: lessons.length,
      decks_content_json: decks.length,
      profield_cache_files: cacheFiles.length,
      php_cache_files: php.length,
      lesson_infra_vocab_files: lessonLeak.n,
      lesson_infra_vocab_sample: lessonLeak.hits,
    },
    guia_weights_expected: {
      tests: 55,
      caso: 15,
      proyectos: 20,
      cuaderno: 10,
    },
    sandra_act_weights_expected: { each_percent: 11.2, count: 4 },
    coordination: {
      d2_equals_act3: true,
      plan_pdf:
        "digital-creativity-pedagogy/cv/sources/Plan_de_trabajo_2026-27_Creacion_Digital_I-Sandra_Jimenez.pdf",
    },
  };
}

if (args.has("--self-check")) {
  const m = measure();
  if (!m.wave1 || typeof m.wave1.lessons_en_cd_i !== "number") {
    console.error("self-check failed: malformed measure");
    process.exit(1);
  }
  console.log(JSON.stringify({ self_check: true, lessons: m.wave1.lessons_en_cd_i }, null, 2));
  process.exit(0);
}

if (args.has("--targets")) {
  // EX11 will define hard targets; until then report structure only.
  const m = measure();
  const unmet = [];
  if (m.wave1.php_cache_files !== 0) unmet.push("php_cache_files");
  const out = { targets_met: unmet.length === 0, unmet_count: unmet.length, unmet, measure: m };
  console.log(JSON.stringify(out, null, 2));
  process.exit(unmet.length === 0 ? 0 : 1);
}

const out = measure();
console.log(JSON.stringify(out, null, 2));
const outPath = args.has("--write")
  ? path.join(__dirname, "../evidence", String([...args].find((a) => a.endsWith(".json")) || "head-EX0.json"))
  : null;
if (args.has("--write-baseline")) {
  fs.mkdirSync(path.join(__dirname, "../evidence"), { recursive: true });
  fs.writeFileSync(
    path.join(__dirname, "../evidence/baseline-EX0.json"),
    JSON.stringify(out, null, 2) + "\n",
  );
}
