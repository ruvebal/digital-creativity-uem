"""Copy native generated images; record their dimensions and content hashes."""
from pathlib import Path
import hashlib
import json
import shutil
import struct

ROOT = Path(__file__).resolve().parents[3]
SOURCE = Path('/Users/ruvebal/.codex/generated_images/01a134ec-c278-72a0-85e6-79a471930f26')
GENERATED = {
    '01-worth': 'exec-b5f39c5e-237d-45e1-9e4b-63a6f1d5d0ec.png',
    '02-agency': 'exec-8639c945-7dcb-4f45-8cce-2e0872b6ce5c.png',
    '03-history': 'exec-528245ff-24ff-46ac-a338-ce0907bc902b.png',
    '04-labour': 'exec-b829eb96-1837-4051-8a80-43ed9daa8d48.png',
    '05-citizen': 'exec-8ebe064c-7f8a-400f-9614-cae2b9bc68f6.png',
    '06-dialogue': 'exec-bdba6e20-7df5-4e56-89bd-a197ec04e240.png',
}
scenes = json.loads((Path(__file__).parent / 'CAPTIONS.json').read_text())
for scene in scenes:
    source = SOURCE / GENERATED[scene['id']]
    data = source.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    scene['asset'] = f"/assets/images/dignity/scenes/dignity-{scene['id']}-{sha[:12]}.png"
    target = ROOT / 'docs' / scene['asset'].lstrip('/')
    if target.exists() and target.read_bytes() != data:
        raise RuntimeError('Immutable asset collision')
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    scene['width'], scene['height'] = struct.unpack('>II', data[16:24])
    scene['sha256'] = sha
    scene['authorship'] = 'AI-generated fictional illustration under @ruvebal art direction'
    scene['created'] = '2026-10-20'
    for lang in ['en','es']:
        scene[lang]['open'] = 'Open the original image' if lang == 'en' else 'Abrir la imagen original'
        scene[lang]['credit'] = 'Fictional scene generated with AI · @ruvebal · 2026. This image is a discussion prompt, not documentary evidence.' if lang == 'en' else 'Escena ficticia generada con IA · @ruvebal · 2026. Imagen para el debate, no prueba documental.'
manifest = {
    'schema': 'dignity.visual-pack/1',
    'release': '2026-10-20.1',
    'display_aspect_ratio': '2.39:1',
    'native_files': 'Unmodified; open each image for its complete native frame.',
    'backgrounds': {
        'light': '/assets/images/dignity/backgrounds/dignity-dc-folds-light-c27a722d8d12.svg',
        'dark': '/assets/images/dignity/backgrounds/dignity-dc-folds-dark-aa8cf2a51fc8.svg',
    },
    'scenes': scenes,
}
serialized = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
(ROOT / 'docs/_data/dignity_visuals.json').write_text(serialized)
(ROOT / 'docs/assets/images/dignity/scenes/index-20261020-r1.json').write_text(serialized)
print('Saved six native scenes and their publication-safe manifest.')
