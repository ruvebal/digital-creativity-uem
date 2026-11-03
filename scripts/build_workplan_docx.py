from pathlib import Path
from shutil import copy2
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from copy import deepcopy

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path('/Users/ruvebal/projects/ruvebal/scholar/universidadeuropea/26-27/DC-WORKPLAN/ruvebal-PlanTrabajo-digitalCreation-I-26-27_ING-TEMPLATE.docx')
OUT = ROOT / 'outputs/workplan/ruvebal-PlanTrabajo-digitalCreation-I-26-27_ING-COMPLETED.docx'
OUT.parent.mkdir(parents=True, exist_ok=True)
copy2(TEMPLATE, OUT)

doc = Document(OUT)

def clear_cell(cell):
    cell.text = ''
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    return p

def set_cell(cell, text, size=8.5, bold=False):
    p = clear_cell(cell)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text)
    r.bold = bold
    r.font.name = 'Calibri'
    r.font.size = Pt(size)

def set_para(p, text):
    p.clear()
    p.add_run(text)

def set_list(p, title, items):
    p.clear()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    heading = p.add_run(title)
    heading.bold = True
    for item in items:
        p.add_run().add_break()
        p.add_run(f'• {item}')

# Course identity table
identity = [
    ('Course', 'Digital Creativity I (Creación Digital I)'),
    ('Degree program', "Bachelor's Degree in Fashion Communication and Management (Grado en Comunicación y Gestión de Moda)"),
    ('School', 'Faculty of Design and Creative Technologies'),
    ('Year', '1'),
    ('ECTS', '6'),
    ('Credit type', 'Basic'),
    ('Language(s)', 'English'),
    ('Delivery mode', 'On campus'),
    ('Semester', 'S1'),
    ('Academic year', '2026-2027'),
    ('Coordinating professor', 'Marta Quintana de Juan'),
    ('Professor', 'Rubén Vega Balbás, PhD'),
]
for row, (label, value) in zip(doc.tables[0].rows, identity):
    set_cell(row.cells[0], label, size=10, bold=True)
    set_cell(row.cells[1], value, size=9)

# Intro and section text
for p in doc.paragraphs:
    if p.text.strip() == 'SCHEDULE ACTIVITIES':
        set_para(p, 'SCHEDULE ACTIVITIES / CRONOGRAMA DE ACTIVIDADES')
    elif p.text.strip() == 'Whenever you have a question about the content or activities, don’t forget to post it to your course forum so that your classmates can read it.':
        set_para(p, 'Whenever you have a question about the content or activities, please post it to the course forum so that the cohort can learn from the answer.')
    elif p.text.strip() == 'You might not be the only one with the same question!':
        set_para(p, 'You might not be the only person with the same question.')
    elif p.text.strip() == 'If you have a question that you only want to ask your professor, you can send him/her a private message from the Campus Virtual. And if you need to discuss something in more detail, you can arrange an advisory session with your professor.':
        set_para(p, 'For a private question, send a message through Campus Virtual or email ruben.vega@universidadeuropea.com. If you need a longer discussion, arrange an academic tutorial with your professor; tutorial-meeting indications and the available scheduling window are published in Campus Virtual.')
    elif p.text.strip() == 'It’s a good idea to check the course forum on a regular basis and read the messages posted by your classmates and professors, as this can be another way to learn.':
        set_para(p, 'Check the course forum regularly: questions and replies are part of the course learning environment.')
    elif p.text.strip() == 'This table shows the delivery deadline for each assessable activity in the course, as well as the delivery dates:':
        set_para(p, 'This table gives the pedagogical sequence and the D1–D5 track assessment activities. Campus Virtual deadlines and the institutional academic calendar remain binding. Tutorial-meeting indications and the available scheduling window are published in Campus Virtual; students may request a tutorial at ruben.vega@universidadeuropea.com.')
    elif p.text.strip() == 'This schedule may be subject to changes for logistical reasons relating to the activities. The student will be notified of any change as and when appropriate.':
        set_para(p, 'This pedagogical sequence may be adjusted for logistical reasons. Students will be notified through Campus Virtual. It does not invent institutional dates. Official course evaluation: in-person assessment tests 55%; case/problem 15%; research and projects 20%; laboratory/workshop practice notebook 10%. Official course load: 150 hours and 6 ECTS, including 80 contact hours plus independent work, tutoring and assessment time.')

# Schedule table. The original template has a five-cell grid with merged visual columns.
schedule = [
    ('1', 'Course introduction and I.1 Introduction to Digital Images', 'Course orientation; forum and Campus Virtual orientation; fashion-image reading; open the portfolio index.', '0%'),
    ('2', 'I.1 Introduction to Digital Images', 'Image field, provenance and authorship exercise; modelled fashion-image analysis; Lab trace added to the portfolio.', '0%'),
    ('3', 'I.2 2D Digital Technology: Drawing Tools', 'Vector drawing Lab; figure, contour and anchor-point studies; D1 preparation begins.', '0%'),
    ('4', 'I.3 Colour, Bitmap Images; I.4 Effects', 'Bitmap modes, colour relations, compositing and traceable before/after edits; Fashion image analysis master session.', '0%'),
    ('5', 'I.5 Three-Dimensional Form; I.6 Volume', 'Spatial literacy, 2D-to-3D translation, material/volume study and critique.', '0%'),
    ('6', 'I.7 Compositional Sources and References in Fashion Design', 'Reference lineage, moodboard and image ethics; Image morphology master session; source audit.', '0%'),
    ('7', 'I.3 Colour, Bitmap Images; I.4 Effects; I.7 Compositional Sources and References in Fashion Design', 'D1 Live fashion-image analysis: one image, eight-step method, navigable slideshow, live defence and Q&A.', '10%'),
    ('8', 'I.8 Creating Animated Digital Images', 'Sequence of stills, timing and motion; individual animation exercise; process note.', '0%'),
    ('9', 'I.9 Digital Still Lifes', 'Synthesis composition combining image, colour, effects, reference and text; studio critique.', '0%'),
    ('10', 'I.5–I.9 synthesis', 'D2 Transposition: cartel or image series from a song, film, poem, literary work or theatre piece; source and process trail; Dance, Cinema and Fashion master cycle.', '10%'),
    ('11', 'Global course contents', 'D3 Atrium development: technical script, audience, visual communication and “What is fashion for you?”.', '0%'),
    ('12', 'Global course contents', 'Dignity Day special, 21 October 2026, using https://ruvebal.github.io/digital-creativity-uem/dignity/en/; continuation in Dignity Week on Friday 23 October 2026; What Does a Garment Do When the Body Moves?', '0%'),
    ('13', 'Global course contents', 'Who Shapes a Dance: the Costume or the Camera?; Who Owns a Movement When It Travels?; D2 revision, D3 production and D1 defences where scheduled.', '0%'),
    ('14', 'Global course contents', 'D3 Atrium live defence and final event “What is fashion for you?”.', '15%'),
    ('14', 'Global course contents', 'D4 Final Digital Portfolio Notebook submission; AI/material declarations checked.', '10%'),
    ('15', 'Course integration and assessment', 'D5 Exam: critical demonstration and portfolio self-review in the official assessment period.', '55%'),
    ('TOTAL', 'Official evaluation weights', 'Case/problem 15%; Research and projects 20%; laboratory/workshop practice notebook 10%; in-person assessment tests 55%.', '100%'),
]
t = doc.tables[1]
headers = ['Week', 'Contents', 'Learning activities / Assessables', 'Weight']
set_cell(t.rows[0].cells[0], headers[0], size=8.5, bold=True)
set_cell(t.rows[0].cells[0], headers[0], size=8.5, bold=True)
set_cell(t.rows[0].cells[1], headers[1], size=8.5, bold=True)
set_cell(t.rows[0].cells[2], headers[2], size=8.5, bold=True)
set_cell(t.rows[0].cells[4], headers[3], size=8.5, bold=True)

while len(t.rows) < len(schedule) + 1:
    row = t.add_row()
    try:
        row.cells[2].merge(row.cells[3])
    except Exception:
        pass
for idx, item in enumerate(schedule, start=1):
    row = t.rows[idx]
    tr_pr = row._tr.get_or_add_trPr()
    cant_split = OxmlElement('w:cantSplit')
    tr_pr.append(cant_split)
    set_cell(row.cells[0], item[0], size=7.5)
    set_cell(row.cells[1], item[1], size=7.2)
    # In the retained template rows 1–10, cells 1/2 are aliases for the
    # contents span; cell 3 is the visible activities column. Added rows use
    # the same visible position after merging 2/3.
    set_cell(row.cells[3], item[2], size=7.2)
    set_cell(row.cells[4], item[3], size=7.2)

# Assessment descriptions
descriptions = {
    'Activity 1.': ('Activity 1 — D1 Live fashion-image analysis (Research and projects 10%).', [
        'Method: analyse one fashion image related to a Madrid exhibition piece with the eight-step Master Lecture method.',
        'Format: live, navigable slideshow; maximum 15 minutes including questions and feedback.',
        'Submit: selected image and source/permission record, eight-step analysis card, editable and exported slideshow, process trail, and authorship / AI declaration slide.',
        'Local rubric: presentation 70%, deliverable support 20%, peer debate 10%; not an additional course percentage.',
    ]),
    'Activity 2.': ('Activity 2 — D2 Transposition (Research and projects 10%).', [
        'Brief: complete the same bilingual transposition brief as ACT3.',
        'Outcome: transform a song, film, poem, literary work or theatre piece into a cartel; an image series is acceptable when it functions as the cartel proposal.',
        'Submit: source and credits, concept rationale, reference lineage, sketches/tests, editable file, final export and process trail.',
    ]),
    'Activity 3.': ('Activity 3 — D3 Atrium (Case/problem 15%).', [
        'Theme: “What is fashion for you?”',
        'Develop: technical script, audience, event sequence, visual and technical communication, roles/credits and accessibility decisions.',
        'Submit: script, production or rehearsal evidence, final communication artefacts and live-defence materials.',
    ]),
    'Activity 4.': ('Activity 4 — D4 Final Digital Portfolio Notebook (practice notebook 10%).', [
        'Format: one navigable digital portfolio notebook.',
        'Include: one substantive exercise entry for every Lab time/lesson, evidence of all nine Digital Creativity I contents, and D1–D3.',
        'Document: dated process traces, feedback and revisions, final synthesis, source/credit record, technical/accessibility check, and authorship, AI and material declaration for every piece.',
    ]),
    '…': ('Activity 5 — D5 Exam (in-person assessment tests 55%).', [
        'Format: critical demonstration using the portfolio as evidence.',
        'Explain and defend: technical choices, formal decisions, references, revisions, feedback and authorship.',
        'Timing: official assessment period; no institutional exam date is invented here.',
    ]),
}
for p in doc.paragraphs:
    for key, (title, items) in descriptions.items():
        if p.text.strip() == key:
            set_list(p, title, items)

# Compact rubric matrix in the template's rubric table.
rubric = doc.tables[2]
rubric_rows = [
    ('Activity', 'Excellent', 'Good', 'Pass', 'Insufficient'),
    ('D1 Live analysis', 'Eight-step trail, critical judgement, evidence, clear live delivery, reliable slideshow and complete declaration.', 'Almost complete trail with clear evidence and minor craft or timing issues.', 'Understandable but missing steps, thin critique or incomplete declaration.', 'Description only, no critique, broken deck or missing authorship.'),
    ('D2 Transposition', 'Original transformation with strong hierarchy, source credits, reference lineage and complete process.', 'Clear transformation with good organisation and minor technical or conceptual gaps.', 'Recognisable source relation but superficial concept or incomplete process.', 'Copies references, lacks a clear transposition or omits process evidence.'),
    ('D3 Atrium', 'Compelling technical script, audience fit, visual communication and confident live defence.', 'Coherent proposal with workable script and minor presentation weaknesses.', 'Basic proposal with limited audience or technical justification.', 'Incomplete, unclear or non-functional event proposal.'),
    ('D4 Portfolio / D5 Exam', 'Complete Lab evidence, D1–D3, synthesis, accessibility, declarations and critical self-review.', 'Nearly complete portfolio and defensible critical response with minor gaps.', 'Thin process evidence, weak navigation or descriptive exam response.', 'Major omissions, broken submission or no defensible account of authorship.'),
]
if len(rubric.rows) < len(rubric_rows):
    # Clone the final styled row rather than using add_row, which loses the
    # template's fills and borders in LibreOffice rendering.
    new_tr = deepcopy(rubric.rows[-1]._tr)
    rubric._tbl.append(new_tr)
for ri, vals in enumerate(rubric_rows):
    row = rubric.rows[ri]
    for ci, val in enumerate(vals):
        set_cell(row.cells[ci], val, size=7.1, bold=(ri == 0))

# Replace plagiarism and AI paragraphs with course-specific English guidance.
for p in doc.paragraphs:
    if p.text.strip().startswith('In accordance with the current student disciplinary regulations'):
        set_para(p, 'In accordance with the current student disciplinary regulations at Universidad Europea, plagiarism in whole or in part and the use of fraudulent means in assessment are very serious offences. The corresponding assessment period and academic record consequences apply.')
    elif p.text.strip() == 'The student must be the author of his/her work/activities.':
        set_para(p, 'Students must be the authors of their work and activities.')
    elif p.text.strip().startswith('The use of Artificial Intelligence tools'):
        set_para(p, 'See the AI usage declaration at https://ruvebal.github.io/digital-creativity-uem/ai-declaration/. It does not prohibit AI; it requires transparent documentation of Tools used, Purpose of use, Human contribution and Source material for every submission. “No AI tools used” is valid. AI may assist concept development, technical assistance, media enhancement or language support, but cannot replace core creative decisions, technical understanding, critical judgement or final responsibility. Traditional citations, collaboration credit, permissions and accessibility standards still apply.')
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        for run in p.runs:
            run.font.size = Pt(10.5)
    elif p.text.strip() == '…':
        p.clear()

# Keep section headings with the first paragraph that follows them.
for p in doc.paragraphs:
    if p.text.strip() in {'PLAGIARISM REGULATION', 'USE OF AI REGULATION'}:
        p.paragraph_format.keep_with_next = True
    if p.text.strip() == 'RUBRICS FOR ASSESSMENT ACTIVITIES':
        p.paragraph_format.page_break_before = True

# Remove the template's trailing empty paragraph; after the expanded activity
# descriptions it can otherwise create an entirely blank final page.
while doc.paragraphs and not doc.paragraphs[-1].text.strip():
    trailing = doc.paragraphs[-1]._element
    trailing.getparent().remove(trailing)

doc.save(OUT)
print(OUT)
