"""Generate content-addressed, uncropped variants of the site's authentic images.

Run directly, or call ``ensure_optimized_images()`` before generating HTML.
``responsive_image_attrs(src, sizes=...)`` returns attributes for an ordinary
WebP ``img``. For the hero, wrap that img in a ``picture`` with a ``source``
whose attributes come from ``avif_source_attrs(src, sizes=...)``. Original
screenshot URLs are intentionally retained for native full-size gallery links.

Only local resizing and encoding is performed. No image content is generated,
cropped, sharpened, or otherwise altered. Filenames include the first twelve
hexadecimal characters of their actual byte hash so they can safely receive
immutable cache headers.
"""
from __future__ import annotations

from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'dist' / 'assets'
# Build-only masters (icons, hero) are not deployed. Screenshots stay published
# because native gallery links open them at their original URLs.
SOURCE_ASSETS = ROOT / 'source-assets'
DESTINATION = ASSETS / 'optimized'
REPORT = ROOT / 'research-assets' / 'image-optimization.json'
SETTINGS_VERSION = 2
SCREEN_WIDTHS = (240, 400, 600)
ICON_WIDTHS = (48, 96, 144)
SUNRISE_WIDTHS = (480, 768, 1200, 1440, 1860)
WEBP_QUALITY = 86
AVIF_QUALITY = 70

SOURCE_ROLES = {
    'looks-max-screen-4.webp': 'screen',
    'looks-max-detail-screen-6.webp': 'screen',
    'iq-max-detail-screen-4.webp': 'screen',
    'iq-max-detail-screen-6.webp': 'screen',
    'sleep-max-detail-screen-3.webp': 'screen',
    'fitness-max-detail-screen-3.webp': 'screen',
    'fitness-max-detail-screen-5.webp': 'screen',
    'iq-max-screen-1.webp': 'screen',
    'sleep-max-screen-4.webp': 'screen',
    'fitness-max-screen-2.webp': 'screen',
    'looks-max-icon.webp': 'icon',
    'iq-max-icon.webp': 'icon',
    'sleep-max-icon.webp': 'icon',
    'fitness-max-icon.webp': 'icon',
    'solar-ascent.webp': 'hero',
}

DEFAULT_SIZES = {
    'screen': '(max-width: 560px) 62vw, 244px',
    'icon': '48px',
    'hero': '100vw',
}
_manifest: dict | None = None


def _digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def _source(filename: str) -> Path:
    published = ASSETS / filename
    return published if published.exists() else SOURCE_ASSETS / filename


def _file_record(data: bytes, stem: str, width: int, height: int, fmt: str) -> dict:
    checksum = _digest(data)
    suffix = fmt.lower()
    name = f'{stem}-{width}.{checksum[:12]}.{suffix}'
    target = DESTINATION / name
    if not target.exists() or target.read_bytes() != data:
        target.write_bytes(data)
    return {
        'url': f'/assets/optimized/{name}',
        'width': width,
        'height': height,
        'bytes': len(data),
        'sha256': checksum,
        'mime': f'image/{suffix}',
    }


def _encode(image: Image.Image, width: int, fmt: str) -> tuple[bytes, int]:
    height = round(image.height * width / image.width)
    resized = image if width == image.width else image.resize(
        (width, height), Image.Resampling.LANCZOS
    )
    output = BytesIO()
    if fmt == 'WEBP':
        resized.save(output, format='WEBP', quality=WEBP_QUALITY, method=6)
    else:
        resized.save(output, format='AVIF', quality=AVIF_QUALITY, speed=6)
    return output.getvalue(), height


def _cache_valid(report: dict, source_hashes: dict) -> bool:
    if report.get('settings_version') != SETTINGS_VERSION:
        return False
    if report.get('source_hashes') != source_hashes:
        return False
    records = report.get('images', {})
    if len(records) != len(SOURCE_ROLES):
        return False
    for record in records.values():
        for variant in record['webp'] + record.get('avif', []):
            path = ROOT / 'dist' / variant['url'].lstrip('/')
            if not path.exists() or _digest(path.read_bytes()) != variant['sha256']:
                return False
    return True


def ensure_optimized_images() -> dict:
    """Generate missing variants and return the stable source/variant manifest."""
    global _manifest
    if _manifest is not None:
        return _manifest
    source_hashes = {
        name: _digest(_source(name).read_bytes()) for name in SOURCE_ROLES
    }
    if REPORT.exists():
        previous = json.loads(REPORT.read_text(encoding='utf-8'))
        if _cache_valid(previous, source_hashes):
            _manifest = previous
            return previous

    DESTINATION.mkdir(parents=True, exist_ok=True)
    report = {
        'settings_version': SETTINGS_VERSION,
        'source_hashes': source_hashes,
        'encoding': {
            'webp_quality': WEBP_QUALITY,
            'avif_quality': AVIF_QUALITY,
            'resize': 'Lanczos, preserve complete image and aspect ratio',
            'original_full_size_screenshots': 'Preserved at their original URLs',
            'fallback_policy': 'Never enlarge the original full-width WebP by re-encoding',
        },
        'images': {},
    }
    for filename, role in SOURCE_ROLES.items():
        source = _source(filename)
        original = source.read_bytes()
        with Image.open(source) as image:
            image.load()
            widths = {'screen': SCREEN_WIDTHS, 'icon': ICON_WIDTHS, 'hero': SUNRISE_WIDTHS}[role]
            stem = source.stem
            record = {
                'source': '/assets/' + filename,
                'role': role,
                'width': image.width,
                'height': image.height,
                'original_bytes': len(original),
                'webp': [],
                'avif': [],
            }
            for width in widths:
                if width > image.width:
                    continue
                webp, height = _encode(image, width, 'WEBP')
                if width == image.width and len(webp) >= len(original):
                    webp = original
                record['webp'].append(_file_record(webp, stem, width, height, 'WEBP'))
                if role == 'hero':
                    avif, avif_height = _encode(image, width, 'AVIF')
                    record['avif'].append(_file_record(avif, stem, width, avif_height, 'AVIF'))
            report['images'][record['source']] = record
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
    _manifest = report
    return report


def image_record(src: str) -> dict | None:
    """Find the manifest record for a supported local image URL."""
    return ensure_optimized_images()['images'].get(src)


def responsive_image_attrs(src: str, *, sizes: str | None = None) -> dict:
    """Return WebP src/srcset/sizes; leave unsupported image URLs unchanged."""
    record = image_record(src)
    if not record:
        return {'src': src}
    variants = record['webp']
    # A modest fallback is efficient in legacy clients that ignore srcset.
    fallback = variants[1] if len(variants) > 1 else variants[0]
    return {
        'src': fallback['url'],
        'srcset': ', '.join(f'{item["url"]} {item["width"]}w' for item in variants),
        'sizes': sizes or DEFAULT_SIZES[record['role']],
        'decoding': 'async',
    }


def avif_source_attrs(src: str, *, sizes: str | None = None) -> dict:
    """Return attrs for a hero AVIF picture source, or {} for other images."""
    record = image_record(src)
    if not record or not record['avif']:
        return {}
    return {
        'type': 'image/avif',
        'srcset': ', '.join(f'{item["url"]} {item["width"]}w' for item in record['avif']),
        'sizes': sizes or DEFAULT_SIZES[record['role']],
    }


FAVICON_SOURCE = SOURCE_ASSETS / 'brand' / 'solarity-lockup-original.png'
# The documented narrow crop of the official sun/lightning mark
# (research-assets/brand-evidence.json, "solarity-sun").
FAVICON_CROP = (186, 37, 1314, 1167)
FAVICON_SIZES = (16, 32, 48)


def write_favicon(target: Path) -> dict:
    """Write a multi-size ICO of the official sun mark; resize only, never redraw."""
    with Image.open(FAVICON_SOURCE) as image:
        mark = image.convert('RGBA').crop(FAVICON_CROP)
    # Pad the near-square crop with transparency instead of distorting it.
    side = max(mark.size)
    square = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    square.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
    # Resample every frame from the full-resolution crop for the sharpest small sizes.
    frames = [square.resize((size, size), Image.Resampling.LANCZOS) for size in FAVICON_SIZES]
    output = BytesIO()
    frames[-1].save(output, format='ICO', sizes=[frame.size for frame in frames], append_images=frames[:-1])
    data = output.getvalue()
    if not target.exists() or target.read_bytes() != data:
        target.write_bytes(data)
    return {'url': '/' + target.name, 'sizes': list(FAVICON_SIZES), 'bytes': len(data), 'sha256': _digest(data)}


if __name__ == '__main__':
    manifest = ensure_optimized_images()
    for source, item in manifest['images'].items():
        variants = item['webp'] + item['avif']
        print(f'{source}: ' + ', '.join(
            f'{v["width"]}w {v["mime"].split("/")[-1]} {v["bytes"]:,} B' for v in variants
        ))
