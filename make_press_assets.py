"""Write the press kit's sun mark into source-assets/press/ (run by hand, then commit).

The mark is the documented narrow crop of the official lockup (optimize_images.FAVICON_CROP): the existing
sun/lightning symbol, not redrawn or recolored, resized with Lanczos to 1024 px with its transparency kept.
The original lockup also carries an older "Always Better" wordmark, so the kit offers the mark alone.

It also writes widely accepted copies of the approved WebP images, because many publishing tools refuse WebP:
the founder portrait and the product screens as JPEG, and the app icons as PNG (lossless, transparency kept).
They are re-encodings of the published files, never edited.

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
JPEG_QUALITY = 90
# Published WebP originals (source-assets/ when a build input, otherwise dist/assets/) -> press copies.
COPIES = {
    'brand/ata-turhan-original.webp': 'ata-turhan-founder.jpg',
    **{f'{slug}-icon.webp': f'{slug}-icon.png' for slug in ('looks-max', 'iq-max', 'sleep-max', 'fitness-max')},
    'looks-max-screen-4.webp': 'looks-max-screen.jpg',
    'iq-max-screen-1.webp': 'iq-max-screen.jpg',
    'sleep-max-screen-4.webp': 'sleep-max-screen.jpg',
    'fitness-max-screen-2.webp': 'fitness-max-screen.jpg',
    'engineering-max-overview.webp': 'engineering-max-screen.jpg',
    'management-max-overview.webp': 'management-max-screen.jpg',
    'marketing-max-home.webp': 'marketing-max-screen.jpg',
}


def published(relative):
    for base in (ROOT / 'source-assets', ROOT / 'dist' / 'assets'):
        if (base / relative).is_file():
            return base / relative
    raise FileNotFoundError(relative)


def write_copies(files):
    for source, name in COPIES.items():
        target = OUT / name
        with Image.open(published(source)) as image:
            if name.endswith('.png'):
                image.convert('RGBA' if 'A' in image.getbands() else 'RGB').save(target, format='PNG', optimize=True)
            else:
                image.convert('RGB').save(target, format='JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
            size = list(image.size)
        data = target.read_bytes()
        files[f'/assets/press/{name}'] = {'from': f'/assets/{source}', 'size': size, 'bytes': len(data),
                                          'sha256': hashlib.sha256(data).hexdigest()}
        print(target.relative_to(ROOT), size, len(data))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as image:
        mark = image.convert('RGBA').crop(FAVICON_CROP)
    mark = mark.resize((SIZE, round(SIZE * mark.height / mark.width)), Image.Resampling.LANCZOS)
    target = OUT / 'solarity-sun-mark.png'
    mark.save(target, format='PNG', optimize=True)
    data = target.read_bytes()
    files = {'/assets/press/solarity-sun-mark.png': {'size': list(mark.size), 'bytes': len(data),
                                                     'sha256': hashlib.sha256(data).hexdigest()}}
    write_copies(files)
    REPORT.write_text(json.dumps({
        'note': __doc__.strip().splitlines()[0],
        'source': 'source-assets/brand/solarity-lockup-original.png (official lockup, see brand-evidence.json)',
        'crop_box': list(FAVICON_CROP),
        'copies': f'Re-encodings of the published WebP files: JPEG quality {JPEG_QUALITY}, PNG lossless',
        'files': files,
    }, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(target.relative_to(ROOT), mark.size, len(data))


if __name__ == '__main__':
    main()
