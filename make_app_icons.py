"""Write the home-screen icons into source-assets/icons/ (run by hand, then commit).

The icons are the official sun mark (the documented favicon crop of the original lockup,
research-assets/brand-evidence.json) centred on the site's charcoal: the iOS home-screen icon and a
192px icon for Android shortcuts. The build publishes them when a page references them, so the
committed bytes are what deploys, identical on every machine.

    python make_app_icons.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image

from optimize_images import FAVICON_CROP, FAVICON_SOURCE

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'source-assets' / 'icons'
REPORT = ROOT / 'research-assets' / 'app-icons.json'
BACKGROUND = (15, 13, 11)
# name: (size, share of the canvas the mark may fill).
# No web manifest: fetching one during load cost Lighthouse LCP 70 ms on every page (measured 2026-10-19).
ICONS = {
    'apple-touch-icon.png': (180, 0.70),
    'icon-192.png': (192, 0.72),
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with Image.open(FAVICON_SOURCE) as source:
        mark = source.convert('RGBA').crop(FAVICON_CROP)
    record = {'source': 'source-assets/brand/solarity-lockup-original.png', 'crop': list(FAVICON_CROP), 'background': '#0f0d0b', 'files': {}}
    for name, (size, share) in ICONS.items():
        canvas = Image.new('RGBA', (size, size), BACKGROUND + (255,))
        side = round(size * share)
        scale = side / max(mark.size)
        resized = mark.resize((round(mark.width * scale), round(mark.height * scale)), Image.Resampling.LANCZOS)
        canvas.alpha_composite(resized, ((size - resized.width) // 2, (size - resized.height) // 2))
        target = OUT / name
        canvas.convert('RGB').save(target, format='PNG', optimize=True)
        data = target.read_bytes()
        record['files'][f'/assets/icons/{name}'] = {'size': size, 'mark_share': share, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
        print(target.relative_to(ROOT), len(data))
    REPORT.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
