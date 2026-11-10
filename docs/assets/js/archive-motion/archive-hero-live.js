import { createGeometryField } from './geometry-field.js';
import { bindFaviconBackgroundMotion } from '../favicon-motion/hero-coordinator.js';

const FAMILIES = {
	'dc-i': {
		palette: ['--dc-i-gold', '--dc-i-coral', '--dc-i-mint', '--hero-fg'],
	},
	'dc-ii': {
		palette: ['--dc-ii-lime', '--dc-ii-violet', '--dc-ii-rose', '--hero-fg'],
	},
};

function themePalette(names) {
	const styles = getComputedStyle(document.documentElement);
	return names.map((name) => styles.getPropertyValue(name).trim()).filter(Boolean);
}

export function mountArchiveHero(hero, { family = 'dc-i', asset = 'archive-home' } = {}) {
	if (!hero) return null;
	const plane = hero.querySelector('.hero-section__inner') || hero;
	plane.classList.add(plane === hero ? 'hero-foreground-plane--self' : 'hero-foreground-plane');
	if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return null;

	const canvas = document.createElement('canvas');
	canvas.className = 'geometry-live-bg';
	canvas.setAttribute('aria-hidden', 'true');
	hero.prepend(canvas);
	hero.classList.add('has-geometry-live');

	const theme = FAMILIES[family] || FAMILIES['dc-i'];
	const field = createGeometryField(canvas, {
		shape: 'hexagon',
		seed: asset,
		palette: themePalette(theme.palette),
		maxCells: window.matchMedia('(max-width: 640px)').matches ? 86 : 132,
		dprCap: 1.2,
		fov: 760,
		floatDepth: 26,
		pointerRoot: hero,
	});
	const unbindFavicon = bindFaviconBackgroundMotion(hero, field, { selector: '#favicon-hero-icon' });
	const destroy = () => {
		unbindFavicon();
		field?.destroy();
	};
	window.addEventListener('pagehide', destroy, { once: true });
	return { canvas, destroy };
}
