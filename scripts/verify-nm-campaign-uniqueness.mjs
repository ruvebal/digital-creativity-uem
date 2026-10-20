import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const indexPath = path.join(
  root,
  "digital-creativity-pedagogy/forge/NM-CAMPAIGN-ALLOCATION-INDEX.md",
);
const lessonRoot = path.join(root, "docs/lessons/es/nuevos-medios-moda");
const deckRoot = path.join(root, "docs/tracks/es/uem/2627-nm");
const guideFiles = ["docs/dignity/index.md", "docs/dignity/es/index.md"]
  .map((file) => path.join(root, file))
  .filter((file) => fs.existsSync(file));

function fail(message) {
  console.error(`NM campaign allocation failed: ${message}`);
  process.exitCode = 1;
}

function parseIndex(markdown) {
  const rows = new Map();
  for (const line of markdown.split(/\r?\n/)) {
    if (!line.startsWith("| ")) continue;
    const cells = line
      .split("|")
      .slice(1, -1)
      .map((cell) => cell.trim());
    if (cells.length < 5 || cells[0] === "campaign_id" || /^-+$/.test(cells[0])) {
      continue;
    }
    const [id, unit, , labelText] = cells;
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(id) || !/^(?:U[1-6]|DIGNITY)$/.test(unit)) {
      continue;
    }
    if (rows.has(id)) fail(`campaign ID “${id}” appears more than once in the allocation index.`);
    const aliases = labelText
      .split(/;\s*/)
      .map((label) => label.trim())
      .filter(Boolean);
    if (!aliases.length) fail(`campaign ID “${id}” has no searchable labels.`);
    rows.set(id, { id, unit, aliases });
  }
  return rows;
}

function lessonRecords() {
  const records = [];
  for (const entry of fs.readdirSync(lessonRoot, { withFileTypes: true })) {
    if (!entry.isDirectory() || !/^u[1-6]-/.test(entry.name)) continue;
    const file = path.join(lessonRoot, entry.name, "index.md");
    if (!fs.existsSync(file)) continue;
    const content = fs.readFileSync(file, "utf8");
    const frontmatter = content.match(/^---\s*\n([\s\S]*?)\n---/);
    if (!frontmatter) continue;
    const status = frontmatter[1].match(/^status:\s*([^\r\n]+)/m)?.[1]?.trim() ?? "";
    if (!status.startsWith("forged")) continue;
    const unit = entry.name.match(/^u([1-6])-i?/i)?.[1];
    const campaignLine = frontmatter[1].match(/^campaign_ids:\s*\[([^\]]*)\]\s*$/m);
    const ids = campaignLine
      ? campaignLine[1]
          .split(",")
          .map((id) => id.trim())
          .filter(Boolean)
      : [];
    if (!ids.length) fail(`${file} is forged but has no campaign_ids allocation.`);
    records.push({ unit: `U${unit}`, file, ids, content });
  }
  if (guideFiles.length) {
    const content = fs.readFileSync(guideFiles[0], "utf8");
    const campaignLine = content.match(/^campaign_ids:\s*\[([^\]]*)\]\s*$/m);
    const ids = campaignLine ? campaignLine[1].split(",").map((id) => id.trim()).filter(Boolean) : [];
    if (!ids.length) fail("The shared dignity guide must declare its reserved campaign_ids.");
    for (const file of guideFiles.slice(1)) {
      const mirrorLine = fs.readFileSync(file, "utf8").match(/^campaign_ids:\s*\[([^\]]*)\]\s*$/m);
      const mirrorIds = mirrorLine ? mirrorLine[1].split(",").map((id) => id.trim()).filter(Boolean) : [];
      if (JSON.stringify([...ids].sort()) !== JSON.stringify([...mirrorIds].sort())) {
        fail(`${file} must mirror the canonical dignity guide's case ownership.`);
      }
    }
    records.push({ unit: "DIGNITY", file: guideFiles[0], ids, content });
  }
  return records;
}

const index = parseIndex(fs.readFileSync(indexPath, "utf8"));
const lessons = lessonRecords();
const assigned = new Map();

for (const lesson of lessons) {
  for (const id of lesson.ids) {
    const row = index.get(id);
    if (!row) {
      fail(`${lesson.file} assigns unknown campaign ID “${id}”; add it to the allocation index.`);
      continue;
    }
    if (row.unit !== lesson.unit) {
      fail(`${id} is allocated to ${row.unit} in the index but appears in ${lesson.unit}.`);
    }
    if (assigned.has(id)) {
      fail(`${id} is assigned in both ${assigned.get(id)} and ${lesson.unit}.`);
    } else {
      assigned.set(id, lesson.unit);
    }
  }
}

for (const [id, row] of index) {
  if (assigned.get(id) !== row.unit) {
    fail(`${id} is indexed for ${row.unit} but is not declared in that lesson’s campaign_ids.`);
  }
}

for (const row of index.values()) {
  const unitNumber = row.unit.slice(1);
  const otherUnitFiles = [];
  if (row.unit !== "DIGNITY") otherUnitFiles.push(...guideFiles);
  for (let n = 1; n <= 6; n += 1) {
    if (String(n) === unitNumber) continue;
    const lessonDir = fs
      .readdirSync(lessonRoot, { withFileTypes: true })
      .find((entry) => entry.isDirectory() && new RegExp(`^u${n}-`).test(entry.name));
    if (lessonDir) {
      const lessonFile = path.join(lessonRoot, lessonDir.name, "index.md");
      if (fs.existsSync(lessonFile)) otherUnitFiles.push(lessonFile);
    }
    const deckDir = fs
      .readdirSync(deckRoot, { withFileTypes: true })
      .find((entry) => entry.isDirectory() && new RegExp(`^u${n}-`).test(entry.name));
    if (deckDir) {
      const deckFile = path.join(deckRoot, deckDir.name, "data/content.json");
      if (fs.existsSync(deckFile)) otherUnitFiles.push(deckFile);
    }
  }
  for (const file of otherUnitFiles) {
    const content = fs.readFileSync(file, "utf8").toLocaleLowerCase();
    for (const alias of row.aliases) {
      if (content.includes(alias.toLocaleLowerCase())) {
        fail(`“${alias}” from ${row.unit} (${row.id}) also appears in ${file}.`);
      }
    }
  }
}

if (process.exitCode) process.exit(process.exitCode);
console.log(
  `NM campaign allocation passed: ${index.size} unique cases assigned across ${lessons.length} canonical teaching pages; no cross-unit lesson/deck/guide reuse found.`,
);
