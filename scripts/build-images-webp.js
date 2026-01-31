#!/usr/bin/env node
/**
 * Convert brand PNG images to WebP (smaller size, same visual).
 * Run: node scripts/build-images-webp.js
 * Requires: npm install sharp --save-dev
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const BRANDS_DIR = path.join(ROOT, 'assets', 'images', 'brands');
const MAX_WIDTH = 120;
const WEBP_QUALITY = 80;

let sharp;
try {
  sharp = require('sharp');
} catch (e) {
  console.warn('Optional: run "npm install sharp --save-dev" to generate WebP images.');
  process.exit(0);
}

const pngs = ['akuakare.png', 'kpm-labs.png', 'techsign.png', 'everva.png', 'isis.png'];

async function main() {
  for (const name of pngs) {
    const src = path.join(BRANDS_DIR, name);
    if (!fs.existsSync(src)) continue;
    const base = name.replace(/\.png$/i, '');
    const dest = path.join(BRANDS_DIR, base + '.webp');
    try {
      await sharp(src)
        .resize(MAX_WIDTH, null, { withoutEnlargement: true })
        .webp({ quality: WEBP_QUALITY })
        .toFile(dest);
      console.log('Created:', path.relative(ROOT, dest));
    } catch (err) {
      console.error('Error', name, err.message);
    }
  }
}

main();
