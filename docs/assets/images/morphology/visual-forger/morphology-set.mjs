// visual-forger 1.2.0 · deterministic SVG study set
// Prompts mirrored from the morphology masterclass brief; seed is explicit.
import fs from 'node:fs';
import path from 'node:path';

const out = path.dirname(new URL(import.meta.url).pathname);
const paper = '#F7F2E8';
const ink = '#111111';
const accent = '#C44536';
const files = {
  dot: `<rect width="1600" height="900" fill="${paper}"/><circle cx="800" cy="450" r="74" fill="${ink}"/><circle cx="800" cy="450" r="145" fill="none" stroke="${accent}" stroke-width="3" opacity=".65"/><circle cx="800" cy="450" r="230" fill="none" stroke="${ink}" stroke-width="2" opacity=".25"/>`,
  line: `<rect width="1600" height="900" fill="${paper}"/><path d="M150 690 C430 650 520 260 790 450 S1180 720 1450 180" fill="none" stroke="${ink}" stroke-width="18" stroke-linecap="round"/>`,
  plane: `<rect width="1600" height="900" fill="${paper}"/><path d="M180 170 L1010 120 L1370 360 L520 430 Z" fill="#C44536" opacity=".72"/><path d="M260 430 L1100 280 L1450 690 L610 800 Z" fill="#26547C" opacity=".72"/><path d="M470 250 L1240 440 L900 760 L210 570 Z" fill="#111111" opacity=".18"/>`,
  form: `<rect width="1600" height="900" fill="${paper}"/><path d="M430 650 L430 330 L690 190 L980 290 L1120 560 L850 710 Z" fill="#C44536" opacity=".85"/><path d="M690 190 L980 290 L980 610 L850 710 L850 400 Z" fill="#26547C" opacity=".85"/><path d="M430 330 L690 190 L850 400 L850 710 L430 650 Z" fill="#F0C36A" opacity=".78"/>`,
  colour: `<rect width="1600" height="900" fill="${paper}"/><rect x="170" y="180" width="300" height="540" fill="#C44536"/><rect x="470" y="180" width="300" height="540" fill="#F0C36A"/><rect x="770" y="180" width="300" height="540" fill="#26547C"/><rect x="1070" y="180" width="360" height="540" fill="#111111" opacity=".86"/>`,
  composition: `<rect width="1600" height="900" fill="${paper}"/><path d="M180 180 H1420 M180 360 H1420 M180 540 H1420 M180 720 H1420 M360 120 V780 M650 120 V780 M940 120 V780 M1230 120 V780" stroke="${ink}" stroke-width="2" opacity=".16"/><rect x="260" y="220" width="540" height="390" fill="#26547C" opacity=".82"/><circle cx="1120" cy="500" r="180" fill="#C44536" opacity=".8"/><path d="M980 170 L1400 760" stroke="${ink}" stroke-width="22" opacity=".8"/>`
};
for (const [name, body] of Object.entries(files)) {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" role="img" aria-label="Visual-forger morphology study: ${name}">${body}</svg>\n`;
  fs.writeFileSync(path.join(out, `vf-${name}.svg`), svg);
}
