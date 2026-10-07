/**
 * Node 22 treats `node --test scripts/tests/` as a module path. This shim
 * loads every `*.test.mjs` so the EX3 exit gate command works.
 */
import { readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const dir = dirname(fileURLToPath(import.meta.url));
for (const name of readdirSync(dir).filter((n) => n.endsWith('.test.mjs')).sort()) {
  await import(pathToFileURL(join(dir, name)).href);
}
