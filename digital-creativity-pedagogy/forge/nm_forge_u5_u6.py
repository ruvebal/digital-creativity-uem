#!/usr/bin/env python3
"""NM U5 + U6 cold B1 via lesson-scribe harness (Thessia) — 2026-11-17.

Same harness as nm_forge_u1_u2.py (prompt shape, BRIEF, tuning-memory record,
CI3 citation gate, v2.1 verbatim registry, 4-sentence gate). Quotes are locked
BEFORE generation; every cite below is an Ahmes node with evaluator_safe=yes and
a printed page read on the page (master-lecture-forger/scripts/vault.py).

Writes:
  forge/unit-enrichment/U5-u5-herramientas-datos/MAIN-IDEAS.yml
  forge/unit-enrichment/U6-u6-futuro-comunicacion-digital/MAIN-IDEAS.yml
  registries/nm-u5-u6-verbatims.json
  ~/src/deviac/fine-tuning/thessia-tuning-memory/<date>-<id>-nm-u5|u6-ideaN/
  forge/receipts/NM-U5-U6-THESSIA-RAW.json   (raw paragraphs for human integration)
"""
from __future__ import annotations

import json
import subprocess
import uuid
from datetime import date
from pathlib import Path

DC = Path("/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/digital-creativity-uem")
PED = DC / "digital-creativity-pedagogy"
MEMORY = Path("/Users/ruvebal/src/deviac/fine-tuning/thessia-tuning-memory")
import os
# thessia_generate.py needs `ollama` + `pyyaml`; no studio venv had both on 2026-11-17, so the
# forge used a throwaway venv. Override with THESSIA_PY=/path/to/python.
PY = Path(os.environ.get("THESSIA_PY", "/Users/ruvebal/src/deviac/services/mcp/.venv/bin/python"))
THESSIA = Path("/Users/ruvebal/src/deviac/fine-tuning/scripts/thessia_generate.py")
TODAY = date.today().isoformat()

QUOTES = {
    "unep_measure": dict(text="Measuring the impact of communication and tracking its input on industry progress towards sustainability targets can be a challenge, particularly for complex and long-term social and behaviour change and shifts in values and beliefs.", chicago="(United Nations Environment Programme 2023, 88)", node="a18e3ed5-4cbf-5e0e-8444-840592c5ca64", coat="08e2ea03", pdf_seq=93, printed=88),
    "unep_governance": dict(text="success must not only look like integrating the principles into the communicator's practice, but also into their internal reporting, with an accountability and governance structure created against them.", chicago="(United Nations Environment Programme 2023, 88)", node="7645b330-6b32-5b9b-9738-c762cf381975", coat="08e2ea03", pdf_seq=93, printed=88),
    "unep_tools": dict(text="Some of the measurement tools available are critiqued as not fit for purpose and consequently fraught with controversy", chicago="(United Nations Environment Programme 2023, 33)", node="199227dc-2c3a-5b34-9d4f-2caf3a0d537d", coat="08e2ea03", pdf_seq=38, printed=33),
    "unep_nca": dict(text="not evidence-backed when it comes to comparing the environmental footprint of an organic cotton t-shirt with a conventional cotton one, and thus misleading", chicago="(United Nations Environment Programme 2023, 33)", node="48bfa4fd-0b99-5837-bb54-594d56e131a4", coat="08e2ea03", pdf_seq=38, printed=33),
    "couldry_colonialism": dict(text="Data colonialism combines the predatory extractive practices of historical colonialism with the abstract quantification methods of computing.", chicago="(Couldry and Mejias 2018, 2)", node="4ddbceb0-9a8e-5fce-ae84-ca0939cbd70c", coat="630cb66e", pdf_seq=2, printed=2),
    "sarkis_asymmetry": dict(text="AR can reduce information asymmetry, a common issue in online shopping, by providing real-time, immersive product interactions.", chicago="(Sarkis et al. 2026, 229)", node="ee5acb96-23b5-5fb3-8d55-5e7f7aec3b18", coat="5c35833d", pdf_seq=7, printed=229),
    "bendel_watermarks": dict(text="it was repeatedly noticed that images bore watermarks and fonts", chicago="(Bendel 2025, 440)", node="8120b38b-979f-5799-9d3c-00a468e3cd3c", coat="71d6c25f", pdf_seq=4, printed=440),
    "lamerichs_screenwear": dict(text="This screenwear is an extension of our identity, as users spend more and more of their time online.", chicago="(Lamerichs 2025, 337)", node="3d51f4ed-15c6-5b32-8867-94611ddc26fa", coat="2ebbda3a", pdf_seq=3, printed=337),
    "lamerichs_gated": dict(text="A worst-case scenario is that the Metaverse becomes a highly privatized place (a gated community, as it were) and entirely driven by ads.", chicago="(Lamerichs 2025, 345)", node="21402351-5768-5cc2-a80d-7bea17821284", coat="2ebbda3a", pdf_seq=11, printed=345),
    "lamerichs_neutral": dict(text="The business models behind digital fashion, in particular tokenized fashion, are not neutral.", chicago="(Lamerichs 2025, 337)", node="d426fdfc-8a96-5ff8-815c-fc49a004a1e7", coat="2ebbda3a", pdf_seq=3, printed=337),
    "flavian_dark": dict(text="the 'dark side' of these technologies must also be explored to obtain a full picture of the user experience", chicago="(Flavián et al. 2024, 9)", node="00da3fba-897a-56ae-97ac-64e954c5e210", coat="04888665", pdf_seq=9, printed=9),
    "anpark_images": dict(text="they just give you images; they don't actually support garment construction", chicago="(An and Park 2026, 15)", node="2b8cb50e-4765-5808-badf-dfc55ef6b8d9", coat="c4236068", pdf_seq=15, printed=15),
    "boden_bottleneck": dict(text="This example illustrates the evaluation bottleneck that lies in the way of automated transformational creativity.", chicago="(Boden 2004, 320)", node="0c034f5e-4d9d-5969-8451-c43df0cf5029", coat="c2f1c705", pdf_seq=335, printed=320),
}

UNITS = {
    "U5": dict(
        id="U5", slug="u5-herramientas-datos", title_es="U5 · Herramientas digitales y análisis de datos",
        contenidos="Comunicación digital (herramientas y análisis)", competencies=["CON4", "COMP8"],
        master_idea_es="Cada métrica es una decisión sobre qué cuenta como éxito: medir no es probar, y los datos tienen origen, coste y dueño.",
        ideas=[
            dict(id=1, heading="Una métrica decide qué cuenta", slide="Antes de medir, alguien decidió qué es éxito: alcance, ventas o cambio de conducta no son lo mismo.", thesis="U5 abre separando indicador y efecto: el dashboard llega con una definición de éxito ya escrita.", quotes=["unep_measure"], case="Marco de unidad (sin caso de campaña): la sala de control del Apolo 11 celebra lo que sus pantallas miden.", athanor="Synergy: UNEP 'Measuring success' chapter. Gap: no HE study on teaching KPI critique in fashion communication."),
            dict(id=2, heading="Medir no es probar", slide="Un número en la ficha de producto informa; solo se vuelve prueba si su método aguanta una comparación.", thesis="Las cifras de huella y los índices de sostenibilidad son herramientas de comunicación que necesitan método y verificación.", quotes=["unep_tools", "unep_nca"], case="Reformation RefScale (rank 17, Track A): cifra de huella por prenda con metodología publicada y declaración de verificación independiente. Caso crítico suplementario: Norrøna × Higg MSI — en 2022 la autoridad noruega de consumo consideró engañoso comparar algodón orgánico y convencional con esos datos.", athanor="Synergy: Green Claims, PEF. Gap: no independent evaluation of how consumers read RefScale."),
            dict(id=3, heading="Los datos se extraen de la vida", slide="Tus métricas vienen de vidas convertidas en datos: pregunta de quién son, quién las cobra y quién no consintió.", thesis="Big data en comunicación de moda: la medición también es apropiación; la crítica decolonial de los datos nombra el coste.", quotes=["couldry_colonialism"], case="Marco crítico (sin caso de campaña).", athanor="Synergy: Mejias & Couldry 2024 Data Grab (section cites only). Gap: fashion-specific data-labour study not vaulted."),
            dict(id=4, heading="Los datos también rinden cuentas", slide="Un registro público, una inspección o una sentencia son datos que la marca no controla.", thesis="Contra-datos: periodismo, inspección laboral y tribunales producen evidencia que corrige el relato de marca.", quotes=[], stance="studio_hypothesis", case="Zara Brasil (rank 14, Track B): la fiscalía laboral de São Paulo documentó trabajo esclavo en talleres proveedores y la justicia responsabilizó a la marca (2011–2017); la 'lista suja' es un registro público de empleadores.", athanor="Synergy: Repórter Brasil dossier. Gap: no vault node; teach from primary legal/NGO documents (linked, not quoted)."),
            dict(id=5, heading="Optimizar con criterio", slide="Una prueba A/B mejora lo que mides; decide antes qué no aceptarías optimizar.", thesis="La optimización es una práctica de gobierno: el informe de métricas debe rendir cuentas de principios, no solo de rendimiento.", quotes=["unep_governance"], case="Marco de unidad: la centralita de 1907 como recordatorio del trabajo humano que enruta las señales.", athanor="Synergy: UNEP measuring success + governance. Gap: A/B ethics in fashion marketing not vaulted."),
        ],
    ),
    "U6": dict(
        id="U6", slug="u6-futuro-comunicacion-digital", title_es="U6 · Futuro de la comunicación digital",
        contenidos="Presente y futuro de la comunicación digital", competencies=["CON4", "COMP8", "HAB5"],
        master_idea_es="IA, realidad aumentada y mundos virtuales cambian la escena de la moda; autenticidad, divulgación y propiedad de los datos son problemas de diseño, no letra pequeña.",
        ideas=[
            dict(id=1, heading="Probarse sin tocar", slide="La prueba virtual reduce la duda de comprar online, pero la cifra de éxito suele venir de quien vende la tecnología.", thesis="RA como promesa de tangibilidad: útil para decidir, pero su evidencia de resultados es a menudo del proveedor.", quotes=["sarkis_asymmetry"], case="Dior × Snapchat B27 (2020): lente de RA para probar seis zapatillas y comprarlas desde la app; las cifras de retorno publicadas proceden de un caso de estudio de Snapchat.", athanor="Synergy: AR purchase-intention literature. Gap: independent long-term AR return-rate data."),
            dict(id=2, heading="Modelos que no existen", slide="En 2024 una marca española lanzó su primera campaña con modelos generadas por IA: ¿qué gana y quién deja de posar?", thesis="Modelos sintéticos: ahorro y velocidad para la marca; preguntas de trabajo, diversidad y origen de los datos de entrenamiento.", quotes=["bendel_watermarks"], case="Mango Teen, colección Sunset Dream (julio de 2024, Track B · España): primera campaña generada íntegramente con IA según la nota de prensa de la marca.", athanor="Synergy: image-synthesis ethics. Gap: no study on Spanish model-labour effects."),
            dict(id=3, heading="Declarar es parte del diseño", slide="Una nota diminuta no basta: la divulgación debe verse tanto como la imagen.", thesis="Divulgación de contenido sintético: del aviso legal mínimo a la transparencia como decisión editorial; el Reglamento europeo de IA ya exige etiquetar ciertos contenidos.", quotes=["flavian_dark"], case="Guess × Vogue (agosto de 2025, caso crítico suplementario): anuncio con una modelo generada por IA y un aviso en letra pequeña que muchos lectores no vieron.", athanor="Synergy: AI Act art. 50 transparency. Gap: no vaulted study on disclosure legibility in fashion ads."),
            dict(id=4, heading="El avatar también es un dato", slide="Tu avatar expresa identidad, pero también registra medidas, gestos y gustos.", thesis="Moda digital y avatares: expresión e inclusión posibles, a cambio de cuerpos convertidos en datos.", quotes=["lamerichs_screenwear"], case="Marco crítico: la ficha antropométrica de Bertillon (1890s) como genealogía del cuerpo medido.", athanor="Synergy: Lamerichs on screenwear and posthuman fashion; avatar biometric privacy (GDPR). Gap: none beyond chapter."),
            dict(id=5, heading="Mundos de marca, jardines cerrados", slide="Un videojuego de colección es una plataforma: decide quién entra, qué se posee y quién cobra.", thesis="Plataformas interactivas: la colección como mundo jugable; la economía de plataforma decide propiedad y acceso.", quotes=["lamerichs_gated", "lamerichs_neutral"], case="Balenciaga Afterworld: The Age of Tomorrow (diciembre de 2020, Track A): la colección otoño-invierno 2021 presentada como videojuego gratuito en el navegador.", athanor="Synergy: metaverse dark side (Flavián). Gap: no data on player demographics."),
            dict(id=6, heading="La herramienta propone; tú juzgas", slide="La IA da imágenes, no patrones; decidir qué vale y firmarlo sigue siendo tu trabajo.", thesis="Cierre del curso: colaboración humano–máquina declarada; el juicio de valor y la autoría permanecen humanos.", quotes=["anpark_images", "boden_bottleneck"], case="Marco de unidad: Ada Lovelace y la objeción de que la máquina no origina.", athanor="Synergy: Boden Lovelace questions. Gap: Jang 2026 designer→curator held as BIBLIO-GAP."),
        ],
    ),
}

SIX_AXES = ("Sentence-role fidelity", "Voice", "Concreteness", "Citation shape", "Antilism-in-practice", "Teenager readable")


def allowed(idea):
    out = []
    for k in idea["quotes"]:
        c = QUOTES[k]["chicago"]
        if c not in out:
            out.append(c)
    return out


def write_registry():
    reg = PED / "registries/nm-u5-u6-verbatims.json"
    reg.parent.mkdir(parents=True, exist_ok=True)
    entries = [dict(citation=q["chicago"], node_id=q["node"], coat=q["coat"], printed=q["printed"], verbatims=[q["text"]]) for q in QUOTES.values()]
    reg.write_text(json.dumps({"entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return reg


def write_main_ideas(unit):
    d = PED / "forge/unit-enrichment" / f"{unit['id']}-{unit['slug']}"
    d.mkdir(parents=True, exist_ok=True)
    lines = [f"# Student slideshow payload — ≤ 6 main ideas · {unit['id']}", f"unit_id: {unit['id']}", f"title_es: {unit['title_es']}",
             "max_ideas: 6", "teaching_language: es", "forge: master-lecture-forger + nm-unit-forge (2026-11-17)",
             "grounding:", "  creativity: \"Boden 2004, 320 (evaluation bottleneck) · evaluator-safe\"",
             "  fashion_image: \"Lamerichs 2025, 337 (screenwear / digital fashion identity) · evaluator-safe\"" if unit['id'] == 'U6' else "  fashion_image: \"UNEP 2023, 33 (measurement tools and scorecards) · evaluator-safe\"",
             "  public_use_boundary: \"campaign images linked, never copied; campaign metrics taught as source claims\"", "ideas:"]
    for i in unit["ideas"]:
        lines += [f"  - id: {i['id']}", f"    heading: {i['heading']}", f"    sentence: \"{i['slide']}\"", f"    case: \"{i['case']}\""]
        if i["quotes"]:
            lines.append(f"    chicago: \"{' · '.join(allowed(i))}\"")
        else:
            lines.append(f"    stance: {i.get('stance', 'studio_hypothesis')}")
    (d / "MAIN-IDEAS.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(unit, idea, registry):
    rid = f"{TODAY}-{uuid.uuid4().hex[:8]}-nm-{unit['id'].lower()}-idea{idea['id']}"
    rec = MEMORY / rid
    rec.mkdir(parents=True, exist_ok=True)
    cites = allowed(idea)
    grounded = "\n".join(f"- {QUOTES[k]['chicago']} — \"{QUOTES[k]['text']}\" [SAFE · printed page verified]" for k in idea["quotes"]) or "- Studio stance — no scholarly citation available; do not cite anyone."
    prompt = f"""You are the author of this lesson — Rubén Vega Balbás, PhD, scholar-artist,
writing for a late-secondary / first-year student in Spanish. Voice: concrete, precise,
lyrical when the material warrants, plain the rest of the time. Do not
name your own techniques; do not use academic meta-discourse. Do not
mention "antilism" by name — practice it: refuse the tidy conclusion when
the material earns openness.

Write ONE paragraph in SPANISH on the following Masterclass idea. Four sentences,
maximum five. Mark sentences [S1]…[S4]. Each sentence has a specific job:

1. Surprise — land the claim as an observation, not a topic sentence.
2. Explanation + one concrete example — use the REAL CASE below, never a hypothetical.
3. Explanation + one open question a student could try to answer.
4. Discussion + consolidated idea + counter-critics + a closing that
   refuses to tie the paragraph into a bow.

MAIN IDEA HEADING: {idea['heading']}
SLIDE SENTENCE (do not repeat verbatim; deepen it): {idea['slide']}
UNIT MASTER IDEA: {unit['master_idea_es']}

THESIS (where this idea sits in the course flow):
{idea['thesis']}

REAL CASE (names and dates are verified; do not add facts, figures or results beyond this line):
{idea['case']}

GROUNDED PATH (cite only these (Author Year, page) forms, never invent one; you may paraphrase,
and if you quote, copy the English words exactly):
{grounded}

ATHANOR SYNERGIES / GAPS:
{idea['athanor']}

CITATION RULE — non-negotiable:
Every (Author Year, page) you emit MUST be exactly one of: {' '.join(cites) if cites else '(none — emit no citation)'}.
Do not invent a name, date, page, figure or quotation.

Return ONLY the paragraph (with [S1]… markers). No preamble. No headings.
"""
    brief = f"""# BRIEF — NM {unit['id']} · idea {idea['id']}

**Course:** Nuevos medios: RRSS y plataformas virtuales (UEM)
**Unit:** {unit['id']} · {unit['title_es']}
**CONTENIDOS:** {unit['contenidos']}
**Competencies:** {', '.join(unit['competencies'])}
**project_slug:** profield-nuevos-medios-moda-2026-27

## (a) Thesis
{idea['thesis']}

## (b) Grounded path
{grounded}

## (c) Athanor findings
{idea['athanor']}

## Case
{idea['case']}

## Allowed citation forms
{' '.join(cites) or 'none'}
"""
    (rec / "prompt.md").write_text(prompt, encoding="utf-8")
    (rec / "BRIEF.md").write_text(brief, encoding="utf-8")
    for m in ("thessia-scholar-v3", "thessia-scholar-v3:latest"):
        subprocess.run(["ollama", "stop", m], capture_output=True, text=True)
    out = rec / "thessia-raw.md"
    cmd = [str(PY), str(THESSIA), "--prompt", prompt, "--out", str(out), "--brief", str(rec / "BRIEF.md"),
           "--model", "thessia-scholar-v3", "--num-predict", "640", "--expected-sentences", "4",
           "--verbatim-registry", str(registry)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    (rec / "generate.log").write_text(proc.stdout + "\n---STDERR---\n" + proc.stderr, encoding="utf-8")
    rejected = (rec / "thessia-raw.md.rejected").exists()
    raw = out.read_text(encoding="utf-8") if out.exists() else ((rec / "thessia-raw.md.rejected").read_text(encoding="utf-8") if rejected else "")
    (rec / "provenance.json").write_text(json.dumps(dict(course="nuevos-medios-moda", unit=unit["id"], idea=idea["id"],
        project_slug="profield-nuevos-medios-moda-2026-27", model="thessia-scholar-v3", nodes=[QUOTES[k]["node"] for k in idea["quotes"]],
        exit_code=proc.returncode, rejected=rejected), ensure_ascii=False, indent=2), encoding="utf-8")
    return dict(unit=unit["id"], idea=idea["id"], heading=idea["heading"], record=rid, exit_code=proc.returncode, rejected=rejected, raw=raw)


def main():
    registry = write_registry()
    results = []
    for unit in UNITS.values():
        write_main_ideas(unit)
        for idea in unit["ideas"]:
            r = run(unit, idea, registry)
            # one regeneration if the gates rejected the paragraph (raw kept as training signal)
            if r["rejected"] or r["exit_code"] != 0:
                r2 = run(unit, idea, registry)
                r2["first_attempt"] = r["record"]
                r = r2
            results.append(r)
            print(f"{r['unit']} idea {r['idea']}: exit={r['exit_code']} rejected={r['rejected']} record={r['record']}", flush=True)
    outp = PED / "forge/receipts/NM-U5-U6-THESSIA-RAW.json"
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(outp)


if __name__ == "__main__":
    main()
