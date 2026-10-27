import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import sharp from 'sharp';

const sourceDir = path.dirname(new URL(import.meta.url).pathname);
const deliveryDir = path.resolve(sourceDir, '../../../../../docs/assets/images/lesson-media/u3-campaign');
await fs.mkdir(deliveryDir, { recursive: true });
const records = [];
for (const [name, title, description] of [
  ['01-message-metric-outcome.svg', 'De la imagen a la evidencia', 'Mapa de lectura: una campaña formula un mensaje; atención, participación y divulgación son indicadores diferentes; los efectos requieren evidencia propia.'],
  ['02-campaign-forms.svg', 'Cinco formas de comunicar y pedir evidencia', 'Placa ilustrada de los cinco casos asignados a U3 y su pregunta crítica. Los esquemas son didácticos y no reproducen imágenes de campaña.'],
]) {
  const svg = await fs.readFile(path.join(sourceDir, name));
  const hash = crypto.createHash('sha256').update(svg).digest('hex');
  const base = name.replace(/\.svg$/, `-${hash.slice(0, 16)}`);
  const svgPath = `/assets/images/lesson-media/u3-campaign/${base}.svg`;
  const pngPath = `/assets/images/lesson-media/u3-campaign/${base}.png`;
  await fs.writeFile(path.join(deliveryDir, `${base}.svg`), svg);
  await fs.writeFile(path.join(deliveryDir, `${base}.png`), await sharp(svg).png().toBuffer());
  records.push({ uuid: crypto.randomUUID(), fractal_hash256: hash, title, description, authorship: 'Course-generated illustration, Digital Creativity UEM', date: '2026-10-27', delivery_svg: svgPath, delivery_png: pngPath, formulas: [] });
}
await fs.writeFile(path.join(deliveryDir, 'figcaption-data.json'), JSON.stringify({ release_date: '2026-10-27', figures: records }, null, 2) + '\n');
console.log(records.map(x => `${x.delivery_svg}\n${x.delivery_png}\nSHA-256 ${x.fractal_hash256}`).join('\n'));
