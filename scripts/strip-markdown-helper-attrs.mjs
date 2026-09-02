import fs from 'node:fs';
import path from 'node:path';

const siteDir = path.resolve('_site');

function walk(dir) {
	if (!fs.existsSync(dir)) return [];
	return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
		const full = path.join(dir, entry.name);
		return entry.isDirectory() ? walk(full) : [full];
	});
}

let changed = 0;
for (const file of walk(siteDir)) {
	if (!/\.(html|backup)$/i.test(file)) continue;
	const before = fs.readFileSync(file, 'utf8');
	const after = before.replace(/\smarkdown="0"/g, '');
	if (after !== before) {
		fs.writeFileSync(file, after);
		changed += 1;
	}
}

console.log(`Stripped markdown helper attributes from ${changed} HTML files`);
