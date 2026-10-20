"""Write the press kit's sun mark into source-assets/press/ (run by hand, then commit).

The mark is the documented narrow crop of the official lockup (optimize_images.FAVICON_CROP): the existing
sun/lightning symbol, not redrawn or recolored, resized with Lanczos to 1024 px with its transparency kept.
The original lockup also carries an older "Always Better" wordmark, so the kit offers the mark alone.

    python make_press_assets.py
"""
import hashlib
import json
from pathlib import Path

from PIL import Image

from optimize_images import FAVICON_CROP

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source-assets' / 'brand' / 'solarity-lockup-original.png'
OUT = ROOT / 'source-assets' / 'press'
REPORT = ROOT / 'research-assets' / 'press-assets.json'
SIZE = 1024


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as image:
        mark = image.convert('RGBA').crop(FAVICON_CROP)
    mark = mark.resize((SIZE, round(SIZE * mark.height / mark.width)), Image.Resampling.LANCZOS)
    target = OUT / 'solarity-sun-mark.png'
    mark.save(target, format='PNG', optimize=True)
    data = target.read_bytes()
    REPORT.write_text(json.dumps({
        'note': __doc__.strip().splitlines()[0],
        'source': 'source-assets/brand/solarity-lockup-original.png (official lockup, see brand-evidence.json)',
        'crop_box': list(FAVICON_CROP),
        'files': {'/assets/press/solarity-sun-mark.png': {'size': list(mark.size), 'bytes': len(data),
                                                          'sha256': hashlib.sha256(data).hexdigest()}},
    }, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(target.relative_to(ROOT), mark.size, len(data))


if __name__ == '__main__':
    main()
