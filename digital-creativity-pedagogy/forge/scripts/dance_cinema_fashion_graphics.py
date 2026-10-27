#!/usr/bin/env python3
"""Course-generated diagrams for the Dance–Cinema–Fashion master lecture.

Writes EN and ES SVGs into docs/assets/images/master-lectures/dance-cinema-fashion/.
Hand-authored geometry, no generative AI, no third-party imagery. Palette and type
follow the existing master-lecture quick-card SVGs (fia-reading-order.svg).

    python3 digital-creativity-pedagogy/forge/scripts/dance_cinema_fashion_graphics.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs/assets/images/master-lectures/dance-cinema-fashion"

BG, PANEL, INK, MUTED, PAPER, ACCENT, ACCENT2 = "#F7F2E8", "#EFE6D6", "#111111", "#6B645C", "#FFFCF7", "#B4442C", "#2C5F8A"
FONT = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif"


def t(x, y, s, size=13, fill=INK, anchor="start", weight="400", style=""):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}"{" font-style=%s" % chr(34) + style + chr(34) if style else ""}>{escape(s)}</text>')


def lines(x, y, rows, size=12, fill=INK, anchor="start", lh=None, weight="400"):
    lh = lh or size + 4
    return "".join(t(x, y + i * lh, r, size, fill, anchor, weight) for i, r in enumerate(rows))


def svg(w, h, title, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">'
            f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
            f'<rect width="{w}" height="{h}" fill="{BG}"/><g font-family="{FONT}">{body}</g></svg>\n')


# ---------------------------------------------------------------- 1 · affordance map
AFF = {
    "en": dict(
        title="What a garment does to a moving body",
        desc=("Course diagram, a two-by-two map. Horizontal axis: the garment follows the body, or redesigns the body. "
              "Vertical axis: the garment amplifies motion, or restricts it. Top left, drape: Duncan tunics and Fortuny's "
              "Delphos follow and lengthen gesture. Top right, extension: Fuller's silk, wands and electric light turn the "
              "costume into the image. Bottom right, reorganisation: Schlemmer's Triadic figures let geometry dictate the step. "
              "Bottom left, tension: Graham's jersey tube makes the body push against cloth. All four are hypotheses to test "
              "against the clips."),
        head="What does the garment do to movement?", sub="Course hypothesis · test it against the clips",
        x0="follows the body", x1="redesigns the body", y0="amplifies motion", y1="restricts motion",
        q=[("DRAPE", ["Duncan tunic · Fortuny Delphos", "cloth follows and lengthens", "the gesture"]),
           ("EXTENSION", ["Fuller: silk + wands + electric light", "the costume becomes", "the image"]),
           ("TENSION", ["Graham's jersey tube", "the body pushes against", "the cloth"]),
           ("REORGANISATION", ["Schlemmer's Triadic figures", "geometry dictates", "the step"])]),
    "es": dict(
        title="Qué le hace una prenda a un cuerpo en movimiento",
        desc=("Diagrama del curso, un mapa de dos por dos. Eje horizontal: la prenda sigue al cuerpo, o rediseña el cuerpo. "
              "Eje vertical: la prenda amplifica el movimiento, o lo restringe. Arriba a la izquierda, drapeado: túnicas de "
              "Duncan y el Delphos de Fortuny siguen y alargan el gesto. Arriba a la derecha, extensión: la seda, las varillas "
              "y la luz eléctrica de Fuller convierten el vestuario en imagen. Abajo a la derecha, reorganización: las figuras "
              "triádicas de Schlemmer dejan que la geometría dicte el paso. Abajo a la izquierda, tensión: el tubo de punto de "
              "Graham hace que el cuerpo empuje contra la tela. Las cuatro son hipótesis que se contrastan con los vídeos."),
        head="¿Qué le hace la prenda al movimiento?", sub="Hipótesis del curso · contrástala con los vídeos",
        x0="sigue al cuerpo", x1="rediseña el cuerpo", y0="amplifica el movimiento", y1="restringe el movimiento",
        q=[("DRAPEADO", ["Túnica Duncan · Delphos de Fortuny", "la tela sigue y alarga", "el gesto"]),
           ("EXTENSIÓN", ["Fuller: seda + varillas + luz eléctrica", "el vestuario se vuelve", "imagen"]),
           ("TENSIÓN", ["El tubo de punto de Graham", "el cuerpo empuja contra", "la tela"]),
           ("REORGANIZACIÓN", ["Figuras triádicas de Schlemmer", "la geometría dicta", "el paso"])]),
}


def affordance(L):
    w, h = 760, 470
    b = [t(24, 36, L["head"], 20, INK, weight="700"), t(24, 58, L["sub"], 12, MUTED, style="italic")]
    cx, cy, qw, qh = 380, 262, 300, 150
    boxes = [(cx - qw - 8, cy - qh - 8), (cx + 8, cy - qh - 8), (cx - qw - 8, cy + 8), (cx + 8, cy + 8)]
    for i, ((x, y), (label, body)) in enumerate(zip(boxes, L["q"])):
        b.append(f'<rect x="{x}" y="{y}" width="{qw}" height="{qh}" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>')
        b.append(t(x + 16, y + 30, label, 14, ACCENT if i in (1, 2) else ACCENT2, weight="700"))
        b.append(lines(x + 16, y + 58, body, 13, INK, lh=20))
    # glyphs: drape wave, extension spiral, tension tube, reorganisation polygon
    gx = [(boxes[0][0] + qw - 54, boxes[0][1] + 20), (boxes[1][0] + qw - 54, boxes[1][1] + 20),
          (boxes[2][0] + qw - 54, boxes[2][1] + 20), (boxes[3][0] + qw - 54, boxes[3][1] + 20)]
    s = f'fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"'
    b.append(f'<path {s} d="M{gx[0][0]} {gx[0][1]+8} q10 30 20 0 t20 0 M{gx[0][0]} {gx[0][1]+22} q10 30 20 0 t20 0"/>')
    b.append(f'<path {s} d="M{gx[1][0]+20} {gx[1][1]+20} m-2 0 a6 6 0 1 1 6 6 a12 12 0 1 1 -12 -14 a18 18 0 1 1 18 22"/>')
    b.append(f'<rect {s} x="{gx[2][0]+8}" y="{gx[2][1]}" width="22" height="36" rx="10"/>')
    b.append(f'<path {s} d="M{gx[3][0]+20} {gx[3][1]} l18 12 l-6 22 h-24 l-6 -22 z"/>')
    # axes
    a = f'stroke="{INK}" stroke-width="1.5" fill="none"'
    b.append(f'<path {a} d="M70 {cy} H{w-70}"/><path {a} d="M{cx} 84 V{h-24}"/>')
    b.append(t(66, cy + 4, L["x0"], 12, MUTED, "end") if False else "")
    b.append(t(cx - qw - 8, cy + qh + 34, "← " + L["x0"], 12, MUTED))
    b.append(t(cx + qw + 8, cy + qh + 34, L["x1"] + " →", 12, MUTED, "end"))
    b.append(t(cx + 8, 80, "↑ " + L["y0"], 12, MUTED))
    b.append(t(cx + 8, h - 8, "↓ " + L["y1"], 12, MUTED))
    return svg(w, h, L["title"], L["desc"], "".join(b))


# ---------------------------------------------------------------- 2 · framing
FRM = {
    "en": dict(
        title="Framing and cutting a dancing, dressed body",
        desc=("Course diagram. A standing figure in a long skirt is overlaid with three camera frames: full figure, medium shot "
              "from the waist up, and close-up on face and hands. Beside it, two timelines of the same thirty seconds: one "
              "uninterrupted take, and six cuts. Questions: what does each frame show of the garment's movement, and what does "
              "each cut hide?"),
        head="Same dance, different film", sub="Frame size decides what the garment can show",
        f=["FULL FIGURE", "MEDIUM", "CLOSE-UP"], tl="30 seconds of the same routine",
        a="A · one take", bb="B · six cuts",
        qs=["Are the feet and the hem in frame?", "Who chooses the cut: dancer, director, editor?",
            "What does the close-up sell: the dress or the star?"]),
    "es": dict(
        title="Encuadrar y montar un cuerpo vestido que baila",
        desc=("Diagrama del curso. Una figura de pie con falda larga aparece con tres encuadres de cámara: figura entera, plano "
              "medio de cintura arriba, y primer plano de cara y manos. Al lado, dos líneas de tiempo de los mismos treinta "
              "segundos: una toma continua y seis cortes. Preguntas: qué muestra cada encuadre del movimiento de la prenda, y "
              "qué oculta cada corte."),
        head="El mismo baile, otra película", sub="El tamaño del plano decide qué puede mostrar la prenda",
        f=["FIGURA ENTERA", "PLANO MEDIO", "PRIMER PLANO"], tl="30 segundos de la misma coreografía",
        a="A · una toma", bb="B · seis cortes",
        qs=["¿Están los pies y el bajo dentro del plano?", "¿Quién decide el corte: bailarina, dirección, montaje?",
            "¿Qué vende el primer plano: el vestido o la estrella?"]),
}


def framing(L):
    w, h = 760, 456
    b = [t(24, 36, L["head"], 20, INK, weight="700"), t(24, 58, L["sub"], 12, MUTED, style="italic")]
    # figure (abstract, garment-forward silhouette)
    fx, fy = 150, 92
    b.append(f'<circle cx="{fx}" cy="{fy+26}" r="16" fill="{INK}"/>')
    b.append(f'<path fill="{INK}" d="M{fx-14} {fy+48} h28 l6 70 l-40 0 z"/>')
    b.append(f'<path fill="{ACCENT}" opacity=".85" d="M{fx-20} {fy+116} h40 l52 170 q-72 22 -144 0 z"/>')
    b.append(f'<path stroke="{INK}" stroke-width="7" stroke-linecap="round" d="M{fx-14} {fy+56} l-46 -38 M{fx+14} {fy+56} l44 34"/>')
    b.append(f'<path stroke="{INK}" stroke-width="7" stroke-linecap="round" d="M{fx-10} {fy+284} l-8 26 M{fx+10} {fy+284} l14 24"/>')
    frames = [(fx - 110, fy - 2, 220, 326, L["f"][0], ACCENT2), (fx - 78, fy - 2, 156, 140, L["f"][1], INK),
              (fx - 40, fy + 4, 80, 60, L["f"][2], ACCENT)]
    for x, y, fw, fh, lab, col in frames:
        b.append(f'<rect x="{x}" y="{y}" width="{fw}" height="{fh}" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="6 4"/>')
    b.append(t(fx - 110, fy + 344, L["f"][0], 11, ACCENT2, weight="700"))
    b.append(t(fx + 82, fy + 150, L["f"][1], 11, INK, weight="700"))
    b.append(t(fx + 44, fy + 18, L["f"][2], 11, ACCENT, weight="700"))
    # timelines
    x0, x1 = 330, 730
    b.append(t(x0, 112, L["tl"], 13, MUTED))
    b.append(t(x0, 146, L["a"], 13, INK, weight="700"))
    b.append(f'<rect x="{x0}" y="156" width="{x1-x0}" height="26" rx="3" fill="{ACCENT2}"/>')
    b.append(t(x0, 216, L["bb"], 13, INK, weight="700"))
    cuts = [0, .18, .31, .52, .63, .82, 1]
    cols = [ACCENT2, ACCENT, INK, ACCENT2, ACCENT, INK]
    for i in range(6):
        a, c = x0 + cuts[i] * (x1 - x0), x0 + cuts[i + 1] * (x1 - x0)
        b.append(f'<rect x="{a+1:.0f}" y="226" width="{c-a-2:.0f}" height="26" rx="3" fill="{cols[i]}"/>')
    for i, q in enumerate(L["qs"]):
        b.append(f'<circle cx="{x0+8}" cy="{292+i*34}" r="9" fill="{PANEL}" stroke="{INK}"/>')
        b.append(t(x0 + 8, 296 + i * 34, str(i + 1), 11, INK, "middle", "700"))
        b.append(t(x0 + 26, 297 + i * 34, q, 13))
    return svg(w, h, L["title"], L["desc"], "".join(b))


# ---------------------------------------------------------------- 3 · evidence ladder
LAD = {
    "en": dict(
        title="Evidence ladder for a movement that travels",
        desc=("Course diagram, a ladder of four rungs from weakest to strongest evidence. Rung 1, visual analogy: it looks "
              "like; needs only eyes; never enough on its own. Rung 2, quotation: a title, credit or statement names the "
              "source. Rung 3, exchange: a dated record shows people worked together. Rung 4, documented influence: testimony, "
              "dates and works line up. Two examples: Kazuo Ohno's 1977 solo is titled after the Spanish dancer La Argentina, "
              "whom he saw dance decades earlier, sources give 1926, 1927 or 1929. Issey Miyake's pleated costumes for "
              "William Forsythe's Frankfurt Ballet, 1991 or 1992, are described as the prototype of Pleats Please, launched "
              "1993. A side panel says appropriation is a question of power, not a rung: who is credited, paid or displaced."),
        head="How do we know a movement travelled?", sub="Climb only as high as your evidence",
        r=[("1 · VISUAL ANALOGY", "“It looks like…” — needs only eyes. Never enough alone."),
           ("2 · QUOTATION", "A title, credit or statement names the source."),
           ("3 · EXCHANGE", "A dated record shows people worked together."),
           ("4 · DOCUMENTED INFLUENCE", "Testimony + dates + works line up.")],
        ex=[["Kazuo Ohno,", "Admiring La Argentina (1977)", "Title names Antonia Mercé (rung 2).", "When did he see her dance?", "1926? 1927? 1929? Sources disagree."],
            ["Forsythe × Miyake", "Frankfurt Ballet, 1991 or 1992", "Pleated costumes for dancers", "→ Pleats Please, 1993 (rung 3)."]],
        side=["APPROPRIATION", "is not a rung.", "It is a question", "of power:", "who is credited,", "paid, displaced?"]),
    "es": dict(
        title="Escalera de evidencia para un movimiento que viaja",
        desc=("Diagrama del curso, una escalera de cuatro peldaños de la evidencia más débil a la más fuerte. Peldaño 1, "
              "analogía visual: se parece; solo necesita ojos; nunca basta sola. Peldaño 2, cita: un título, crédito o "
              "declaración nombra la fuente. Peldaño 3, intercambio: un registro fechado muestra que las personas trabajaron "
              "juntas. Peldaño 4, influencia documentada: testimonio, fechas y obras coinciden. Dos ejemplos: el solo de Kazuo "
              "Ohno de 1977 lleva el nombre de la bailarina La Argentina, a quien vio bailar décadas antes; las fuentes dan 1926, "
              "1927 o 1929. Los plisados de Issey Miyake para el Ballet de Frankfurt de William Forsythe, 1991 o 1992, se "
              "describen como prototipo de Pleats Please, lanzado en 1993. Un panel lateral dice que la apropiación no es un "
              "peldaño sino una cuestión de poder: a quién se acredita, se paga o se desplaza."),
        head="¿Cómo sabemos que un movimiento viajó?", sub="Sube solo hasta donde llegue tu evidencia",
        r=[("1 · ANALOGÍA VISUAL", "«Se parece a…» — solo pide ojos. Nunca basta sola."),
           ("2 · CITA", "Un título, crédito o declaración nombra la fuente."),
           ("3 · INTERCAMBIO", "Un registro fechado muestra que trabajaron juntos."),
           ("4 · INFLUENCIA DOCUMENTADA", "Testimonio + fechas + obras coinciden.")],
        ex=[["Kazuo Ohno,", "Admiring La Argentina (1977)", "El título nombra a Antonia Mercé (2).", "¿Cuándo la vio bailar?", "¿1926? ¿1927? ¿1929? No coinciden."],
            ["Forsythe × Miyake", "Ballet de Fráncfort, 1991 o 1992", "Plisados para bailarines", "→ Pleats Please, 1993 (peldaño 3)."]],
        side=["LA APROPIACIÓN", "no es un peldaño.", "Es una cuestión", "de poder: ¿a quién", "se acredita, se paga,", "se desplaza?"]),
}


def ladder(L):
    w, h = 760, 470
    b = [t(24, 36, L["head"], 20, INK, weight="700"), t(24, 58, L["sub"], 12, MUTED, style="italic")]
    rail = f'stroke="{INK}" stroke-width="3"'
    b.append(f'<path {rail} d="M40 446 V90 M64 446 V90"/>')
    for i, (lab, txt) in enumerate(L["r"]):
        y = 400 - i * 86
        b.append(f'<path {rail} d="M40 {y+18} H64"/>')
        b.append(f'<rect x="80" y="{y-6}" width="372" height="54" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>')
        b.append(t(94, y + 15, lab, 13, ACCENT2 if i == 3 else (ACCENT if i == 0 else INK), weight="700"))
        b.append(t(94, y + 36, txt, 11.5, INK))
    b.append(f'<rect x="468" y="84" width="272" height="232" rx="6" fill="{PANEL}"/>')
    yy = 108
    for ex in L["ex"]:
        b.append(t(482, yy, ex[0], 12, INK, weight="700"))
        b.append(t(482, yy + 17, ex[1], 12, INK, weight="700", style="italic"))
        b.append(lines(482, yy + 36, ex[2:], 11.5, INK, lh=16))
        yy += 112
    b.append(f'<rect x="468" y="330" width="272" height="116" rx="6" fill="{PAPER}" stroke="{ACCENT}" stroke-width="2"/>')
    b.append(lines(484, 354, L["side"][:1], 13, ACCENT, weight="700"))
    b.append(lines(484, 374, [" ".join(L["side"][1:3]), " ".join(L["side"][3:5]), L["side"][5]], 12, INK, lh=17))
    return svg(w, h, L["title"], L["desc"], "".join(b))


# ---------------------------------------------------------------- 4 · session flow
FLOW = {
    # one 120-minute plan per part of the cycle
    ("1", "en"): dict(title="Part 1 session flow, 120 minutes",
               desc=("Course diagram of Part 1. Minutes 0 to 15, Analysis of one film still. 15 to 55, Masterclass: three "
                     "ideas with films. 55 to 60, Lab opener. 60 to 85, Exercise 1, capture movement with the phone camera. "
                     "85 to 110, Exercise 2, one image of time in Photoshop and the movement card. 110 to 120, share."),
               head="Part 1 · 120′ · how the session runs",
               seg=[(0, 15, "Analysis", "1 still · 8 steps"), (15, 55, "Masterclass", "3 ideas · films"), (55, 60, "Lab", "opener"),
                    (60, 85, "Ex 1 · Capture", "phone camera"), (85, 110, "Ex 2 · Image of time", "layers · movement card"),
                    (110, 120, "Share", "portfolio")]),
    ("2", "en"): dict(title="Part 2 session flow, 120 minutes",
               desc=("Course diagram of Part 2. Minutes 0 to 15, Analysis of one painting. 15 to 55, Masterclass: three "
                     "ideas on travel, strangeness and butoh. 55 to 60, Lab opener. 60 to 85, Exercise 1, transform a capture "
                     "in Photoshop or Firefly. 85 to 110, Exercise 2, audit what the machine assumes. 110 to 120, share and AI declaration."),
               head="Part 2 · 120′ · how the session runs",
               seg=[(0, 15, "Analysis", "1 painting · 8 steps"), (15, 55, "Masterclass", "3 ideas · evidence"), (55, 60, "Lab", "opener"),
                    (60, 85, "Ex 1 · Transform", "Photoshop · Firefly"), (85, 110, "Ex 2 · Audit", "what the AI assumes"),
                    (110, 120, "Share", "+ AI declaration")]),
    ("1", "es"): dict(title="Ritmo de la parte 1, 120 minutos",
               desc=("Diagrama del curso de la parte 1. Minutos 0 a 15, análisis de un fotograma. 15 a 55, masterclass: tres "
                     "ideas con películas. 55 a 60, apertura del Lab. 60 a 85, ejercicio 1, capturar movimiento con la cámara "
                     "del móvil. 85 a 110, ejercicio 2, una imagen del tiempo en Photoshop y la tarjeta de movimiento. 110 a 120, compartir."),
               head="Parte 1 · 120′ · cómo corre la sesión",
               seg=[(0, 15, "Análisis", "1 fotograma · 8 pasos"), (15, 55, "Masterclass", "3 ideas · películas"), (55, 60, "Lab", "apertura"),
                    (60, 85, "Ej 1 · Capturar", "cámara del móvil"), (85, 110, "Ej 2 · Imagen del tiempo", "capas · tarjeta"),
                    (110, 120, "Compartir", "portfolio")]),
    ("2", "es"): dict(title="Ritmo de la parte 2, 120 minutos",
               desc=("Diagrama del curso de la parte 2. Minutos 0 a 15, análisis de un cuadro. 15 a 55, masterclass: tres ideas "
                     "sobre viaje, extrañeza y butoh. 55 a 60, apertura del Lab. 60 a 85, ejercicio 1, transformar una captura en "
                     "Photoshop o Firefly. 85 a 110, ejercicio 2, auditar lo que supone la máquina. 110 a 120, compartir y declaración de IA."),
               head="Parte 2 · 120′ · cómo corre la sesión",
               seg=[(0, 15, "Análisis", "1 cuadro · 8 pasos"), (15, 55, "Masterclass", "3 ideas · evidencia"), (55, 60, "Lab", "apertura"),
                    (60, 85, "Ej 1 · Transformar", "Photoshop · Firefly"), (85, 110, "Ej 2 · Auditar", "qué supone la IA"),
                    (110, 120, "Compartir", "+ declaración IA")]),
}


def flow(L):
    w, h = 760, 200
    b = [t(24, 36, L["head"], 20, INK, weight="700")]
    x0, x1 = 24, 736
    cols = [PANEL, ACCENT2, INK, ACCENT, ACCENT, PANEL]
    for i, (a, c, lab, sub) in enumerate(L["seg"]):
        xa, xc = x0 + a / 120 * (x1 - x0), x0 + c / 120 * (x1 - x0)
        dark = cols[i] in (ACCENT2, INK, ACCENT)
        b.append(f'<rect x="{xa+1:.1f}" y="60" width="{xc-xa-2:.1f}" height="54" rx="4" fill="{cols[i]}" stroke="{INK}" stroke-width="1"/>')
        if c - a >= 20:
            b.append(t(xa + 8, 82, lab, 12.5, PAPER if dark else INK, weight="700"))
            b.append(t(xa + 8, 102, sub, 11, PAPER if dark else INK))
        else:
            anchor = "start" if a == 0 else ("end" if c == 120 else "middle")
            x = xa + 2 if a == 0 else (xc - 2 if c == 120 else (xa + xc) / 2)
            b.append(t(x, 150, lab, 11.5, INK, anchor, "700"))
            b.append(t(x, 166, sub, 10.5, MUTED, anchor))
        b.append(t(xa + 1, 130, f"{a}′", 10.5, MUTED))
    b.append(t(x1, 130, "120′", 10.5, MUTED, "end"))
    return svg(w, h, L["title"], L["desc"], "".join(b))


# ---------------------------------------------------------------- 5 · onion skin method
ONION = {
    "en": dict(title="From burst to one image of time",
               desc=("Course diagram of the Lab method. Step 1, shoot a burst of a turn with the phone, about twelve frames. "
                     "Step 2, pick six frames. Step 3, stack them as Photoshop layers at about twenty-five percent opacity, or use "
                     "the Lighten blend mode. Step 4, one image shows how the garment travelled through time, like a "
                     "chronophotograph."),
               head="Burst → layers → one image of time",
               st=["1 · burst (≈12 frames)", "2 · keep 6", "3 · layers · 25% / Lighten", "4 · one image of time"]),
    "es": dict(title="De la ráfaga a una imagen del tiempo",
               desc=("Diagrama del curso del método del Lab. Paso 1, dispara una ráfaga de un giro con el móvil, unas doce "
                     "fotos. Paso 2, elige seis. Paso 3, apílalas como capas de Photoshop al veinticinco por ciento de opacidad, "
                     "o con el modo de fusión Aclarar. Paso 4, una sola imagen muestra cómo viajó la prenda en el tiempo, como "
                     "una cronofotografía."),
               head="Ráfaga → capas → una imagen del tiempo",
               st=["1 · ráfaga (≈12 fotos)", "2 · quédate 6", "3 · capas · 25% / Aclarar", "4 · una imagen del tiempo"]),
}


def onion(L):
    w, h = 760, 250
    b = [t(24, 36, L["head"], 20, INK, weight="700")]

    def skirt(cx, cy, size, flare, op=1):
        r, top, hgt = size * .16, size * .32, size * .58
        sw = size * (.18 + .1 * flare)
        return (f'<g opacity="{op}"><circle cx="{cx:.1f}" cy="{cy + r:.1f}" r="{r:.1f}" fill="{INK}"/>'
                f'<path fill="{ACCENT}" d="M{cx - size * .08:.1f} {cy + top:.1f} h{size * .16:.1f} '
                f'l{sw:.1f} {hgt:.1f} h{-(2 * sw + size * .16):.1f} z"/></g>')
    for i in range(12):
        x, y = 30 + (i % 4) * 36, 62 + (i // 4) * 48
        b.append(f'<rect x="{x}" y="{y}" width="32" height="44" fill="{PAPER}" stroke="{MUTED}"/>')
        b.append(skirt(x + 16, y + 3, 38, (i % 6) / 5))
    for i in range(6):
        x, y = 206 + (i % 3) * 44, 70 + (i // 3) * 66
        b.append(f'<rect x="{x}" y="{y}" width="40" height="60" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>')
        b.append(skirt(x + 20, y + 4, 52, i / 5))
    for i in range(6):
        b.append(f'<rect x="{366 + i * 10}" y="{62 + i * 12}" width="96" height="96" fill="{PAPER}" stroke="{INK}" opacity=".9"/>')
    b.append(f'<rect x="560" y="60" width="176" height="136" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    for i in range(6):
        b.append(skirt(600 + i * 18, 76, 84, i / 5, .25 + i * .12))
    for i, s_ in enumerate(L["st"]):
        b.append(t([30, 206, 366, 560][i], 226, s_, 12.5, INK, weight="700"))
    return svg(w, h, L["title"], L["desc"], "".join(b))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lang in ("en", "es"):
        for name, fn, data in (("affordance-map", affordance, AFF), ("framing", framing, FRM),
                               ("evidence-ladder", ladder, LAD), ("onion-skin", onion, ONION)):
            path = OUT / f"dcf-{name}.{lang}.svg"
            path.write_text(fn(data[lang]), encoding="utf-8")
            print(path.relative_to(ROOT))
        for part in ("1", "2"):
            path = OUT / f"dcf-session-flow-{part}.{lang}.svg"
            path.write_text(flow(FLOW[(part, lang)]), encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
