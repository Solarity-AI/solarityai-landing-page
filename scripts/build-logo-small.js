#!/usr/bin/env node
const path = require('path');
const fs = require('fs');
const ROOT = path.join(__dirname, '..');
const LOGO_DIR = path.join(ROOT, 'assets', 'images', 'logo');
const SRC = path.join(LOGO_DIR, 'CompanyLogo.png');

let sharp;
try {
  sharp = require('sharp');
} catch (e) {
  console.warn('Run "npm install sharp --save-dev" to build logo.');
  process.exit(1);
}

async function main() {
  if (!fs.existsSync(SRC)) {
    console.warn('Source not found:', SRC);
    return;
  }
  for (const w of [120, 180, 360]) {
    const base = path.join(LOGO_DIR, 'CompanyLogo-' + w + 'w');
    const pipeline = sharp(SRC).resize(w, null, { withoutEnlargement: true });
    await pipeline.clone().png({ compressionLevel: 6 }).toFile(base + '.png');
    console.log('Created:', path.relative(ROOT, base + '.png'));
    await pipeline.clone().webp({ quality: 60, alphaQuality: 70 }).toFile(base + '.webp');
    console.log('Created:', path.relative(ROOT, base + '.webp'));
  }
}
main().catch((err) => {
  console.error(err);
  process.exit(1);
});
