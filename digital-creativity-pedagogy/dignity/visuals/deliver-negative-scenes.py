"""Persist critical counterpart PNGs and publish bilingual pair metadata."""
from pathlib import Path
import hashlib
import json
import shutil
import struct

ROOT = Path(__file__).resolve().parents[3]
SOURCE = Path('/Users/ruvebal/.codex/generated_images/01a134ec-c278-72a0-85e6-79a471930f26')
GENERATED = {
  '01-worth': 'exec-3f287cc7-6a15-497c-b8d5-12d90facecc7.png',
  '02-agency': 'exec-e47bec0f-7e58-40da-befb-8c2e689e8bd1.png',
  '03-history': 'exec-fb3b5ab7-08f0-4c01-a023-5203b54c3a8a.png',
  '04-labour': 'exec-524ac808-55ed-43f5-9e2a-9a54204c19aa.png',
  '05-citizen': 'exec-26d0999f-d644-4276-b52c-4869d239a7c0.png',
  '06-dialogue': 'exec-d4792395-5575-4ca2-bc1f-6b198c85379b.png',
}
NEG_ALT = {
  '01-worth': ('A fictional casting scene uses a narrow silhouette board while adult applicants with different bodies and an adult wheelchair user wait outside the selectors’ focus.', 'Escena ficticia de casting: una tabla de siluetas estrecha concentra la atención mientras esperan aspirantes adultas diversas y una persona usuaria de silla de ruedas.'),
  '02-agency': ('A fictional photo-shoot monitor crops an adult model’s face and raised hand while she stands beside the camera asking to pause.', 'En una sesión ficticia, el monitor recorta la cara y la mano alzada de una modelo adulta que pide detenerse junto a la cámara.'),
  '03-history': ('A fictional runway styling discussion places a woven textile among anonymous mood-board swatches as its designer points to its construction and context.', 'En una conversación ficticia de estilismo, un tejido aparece como muestra anónima mientras su diseñadora señala su construcción y contexto.'),
  '04-labour': ('A fictional oversized finished garment dominates the foreground while skilled adult garment makers work at an atelier table beyond it.', 'Una prenda terminada domina el primer plano ficticio mientras profesionales adultas siguen trabajando en la mesa del taller.'),
  '05-citizen': ('A fictional fitting and repair studio is crowded with packaged garments and retail screens that compete with the visible repair table.', 'Un taller ficticio de pruebas y arreglos se llena de prendas empaquetadas y pantallas comerciales que desplazan la mesa de reparación.'),
  '06-dialogue': ('A fictional retouching review compares a natural portrait with a subtly narrowed and smoothed version while an adult model points out the changes.', 'Una revisión ficticia de retoque compara un retrato natural con una versión sutilmente estrechada y suavizada que señala una modelo adulta.'),
}
FLIP = {
  'en': ('Flip to a dignity-affirming alternative', 'Show the critical framing'),
  'es': ('Ver alternativa centrada en la dignidad', 'Ver la lectura crítica'),
}
manifest_path = ROOT / 'docs/_data/dignity_visuals.json'
data = json.loads(manifest_path.read_text())
for scene in data['scenes']:
    source = SOURCE / GENERATED[scene['id']]
    content = source.read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    scene['negative_asset'] = f"/assets/images/dignity/scenes/dignity-{scene['id']}-critical-{digest[:12]}.png"
    target = ROOT / 'docs' / scene['negative_asset'].lstrip('/')
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != content:
        raise RuntimeError(f'Immutable asset collision: {target}')
    shutil.copyfile(source, target)
    scene['negative_width'], scene['negative_height'] = struct.unpack('>II', content[16:24])
    scene['negative_sha256'] = digest
    scene['negative_authorship'] = 'AI-generated fictional critical illustration, composed against the paired positive scene under @ruvebal art direction'
    scene['en']['negative_alt'], scene['es']['negative_alt'] = NEG_ALT[scene['id']]
    scene['en']['flip_positive'], scene['en']['flip_negative'] = FLIP['en']
    scene['es']['flip_positive'], scene['es']['flip_negative'] = FLIP['es']
    scene['en']['question'] = 'First: a fictional critical reading. Flip to compare a dignity-affirming alternative. ' + scene['en']['question']
    scene['es']['question'] = 'Primero: una lectura crítica ficticia. Gira la imagen para compararla con una alternativa centrada en la dignidad. ' + scene['es']['question']

payload = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
manifest_path.write_text(payload)
release_dir = ROOT / 'docs/assets/images/dignity/scenes'
(release_dir / 'index-20261020-r2.json').write_text(payload)
(release_dir / 'index.json').write_text(json.dumps({
  'schema':'dignity.visual-pack-index/1',
  'releases':['index-20261020-r1.json','index-20261020-r2.json'],
  'current':'index-20261020-r2.json'
}, indent=2) + '\n')
print('Saved six critical counterpart images and the append-only paired release.')
