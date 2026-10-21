"""Generate content-addressed, uncropped variants of the site's authentic images.

Run directly, or call ``ensure_optimized_images()`` before generating HTML.
``responsive_image_attrs(src, sizes=...)`` returns attributes for an ordinary
WebP ``img``. For the hero, wrap that img in a ``picture`` with a ``source``
whose attributes come from ``avif_source_attrs(src, sizes=...)``. Original
screenshot URLs are intentionally retained for native full-size gallery links.

Only local resizing, encoding and recorded edge trimming are performed. No image
content is generated, sharpened, or otherwise altered. Store screenshots carry thin
baked-in listing hairlines at their edges; each derivative trims the smallest inset
(at most EDGE_MAX_INSET px per side) that makes its outer EDGE_BAND px match the
adjacent interior within EDGE_TRIM_LIMIT levels (checked at EDGE_LIMIT). The inset is recorded in the manifest,
and the originals in dist/assets/ are never changed. Filenames include the first twelve
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
SETTINGS_VERSION = 10
# Native-resolution screenshots (1284x2778), confirmed by the founder on 2026-10-19.
# 260 (the smallest width every screen passes the edge check at) and 600 serve the small Home wall and Investors showroom windows on phones (measured 119 and 180 CSS px).
SCREEN_WIDTHS = (260, 400, 600, 800, 1200)
ICON_WIDTHS = (48, 96, 144, 224, 320)
EDGE_BAND = 8
EDGE_LIMIT = 40
# Trim against a stricter limit so resampled derivatives still pass the 40-level check.
EDGE_TRIM_LIMIT = 30
EDGE_MAX_INSET = 32
# The hero master is the approved artwork upscaled 2x (research-assets/solar-ascent-artwork.json).
SUNRISE_WIDTHS = (480, 768, 1200, 1440, 1860, 2560, 3200, 3720)
# The official Google Play badge (646 x 250 PNG) is drawn about 165 CSS px wide: 1x and 2x WebP, resized only.
BADGE_WIDTHS = (181, 362)
# Team portraits: the roster card is at most 405 px wide (about 160 px on phones), up to 2× of each; never enlarged.
PORTRAIT_WIDTHS = (320, 480, 640, 800)
# Web app screenshots from the products' own sites (research-assets/saas-evidence.json).
WEB_WIDTHS = (640, 960, 1440, 1920, 2560)
WEBP_QUALITY = 86
AVIF_QUALITY = 70

SOURCE_ROLES = {
    'looks-max-screen-4.webp': 'screen',
    'looks-max-detail-screen-6.webp': 'screen',
    'iq-max-detail-screen-4.webp': 'screen',
    'iq-max-detail-screen-6.webp': 'screen',
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
    'badges/google-play-badge.png': 'badge',
    'engineering-max-overview.webp': 'web',
    'management-max-overview.webp': 'web',
    'management-max-sources.webp': 'web',
    'marketing-max-home.webp': 'web',
    'marketing-max-caption.webp': 'web',
    'team/ali-yilmaz.webp': 'portrait',
    'team/hasan-ak.webp': 'portrait',
    'team/eren-oz.webp': 'portrait',
    'team/batuhan-yuceturk.webp': 'portrait',
    'team/melik-kaplan.webp': 'portrait',
}

DEFAULT_SIZES = {
    'screen': '(max-width: 560px) 62vw, 244px',
    'icon': '48px',
    'hero': '100vw',
    'web': '(max-width: 850px) 92vw, 640px',
    'badge': '165px',
    'portrait': '(max-width: 560px) calc(50vw - 30px), 405px',
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


def _band_mean(image: Image.Image, side: str, start: int, depth: int) -> tuple:
    width, height = image.size
    box = {
        'left': (start, 0, start + depth, height),
        'right': (width - start - depth, 0, width - start, height),
        'top': (0, start, width, start + depth),
        'bottom': (0, height - start - depth, width, height - start),
    }[side]
    region = image.crop(box).convert('RGB')
    pixels = region.width * region.height
    sums = [0, 0, 0]
    for count, color in region.getcolors(pixels) or []:
        for channel in range(3):
            sums[channel] += count * color[channel]
    return tuple(value / pixels for value in sums)


def edge_difference(image: Image.Image, side: str, inset: int = 0, band: int = EDGE_BAND) -> float:
    """Acceptance check: the outer band's mean against the band just inside it.

    For a resized derivative, pass the source-scale band (EDGE_BAND × width / source width)."""
    outer = _band_mean(image, side, inset, band)
    inner = _band_mean(image, side, inset + band, band)
    return max(abs(a - b) for a, b in zip(outer, inner))


def derivative_edge_band(width: int, source_width: int) -> int:
    return max(3, round(EDGE_BAND * width / source_width))


def _line_edge_difference(image: Image.Image, side: str, inset: int = 0) -> float:
    """Trimming test, line by line, so a 2px hairline cannot hide inside an 8px average."""
    inner = _band_mean(image, side, inset + EDGE_BAND, EDGE_BAND)
    return max(max(abs(a - b) for a, b in zip(_band_mean(image, side, inset + line, 1), inner))
               for line in range(EDGE_BAND))


def edge_insets(image: Image.Image) -> dict:
    """The smallest per-side trim that removes baked-in listing hairlines."""
    insets = {}
    for side in ('left', 'top', 'right', 'bottom'):
        inset = 0
        while inset < EDGE_MAX_INSET and _line_edge_difference(image, side, inset) > EDGE_TRIM_LIMIT:
            inset += 1
        insets[side] = inset
    return insets


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
            'screen_formats': 'WebP only. Measured on the 10 screens at 400w (P5a): WebP q86 221,202 B at mean error 1.02; AVIF q70 231,545 B at 1.22; AVIF q60 191,949 B at 1.41. AVIF is larger or softer for UI text.',
            'edge_trim': f'Screens: smallest inset (max {EDGE_MAX_INSET}px per side) whose outer {EDGE_BAND}px band matches the next band within {EDGE_LIMIT} levels; derivatives only',
        },
        'images': {},
    }
    for filename, role in SOURCE_ROLES.items():
        source = _source(filename)
        original = source.read_bytes()
        with Image.open(source) as image:
            image.load()
            if role == 'badge':
                image = image.convert('RGBA')
            crop = None
            if role == 'screen':
                insets = edge_insets(image)
                if any(insets.values()):
                    crop = insets
                    image = image.crop((insets['left'], insets['top'], image.width - insets['right'], image.height - insets['bottom']))
            widths = {'screen': SCREEN_WIDTHS, 'icon': ICON_WIDTHS, 'hero': SUNRISE_WIDTHS, 'web': WEB_WIDTHS, 'badge': BADGE_WIDTHS, 'portrait': PORTRAIT_WIDTHS}[role]
            if role == 'web':
                # Always end at the screenshot's own width; never enlarge it.
                widths = tuple(w for w in WEB_WIDTHS if w < image.width) + (image.width,)
            stem = source.stem
            record = {
                'source': '/assets/' + filename,
                'role': role,
                'width': image.width,
                'height': image.height,
                'original_bytes': len(original),
                'crop': crop,
                'derivative_width': image.width,
                'derivative_height': image.height,
                'webp': [],
                'avif': [],
            }
            for width in widths:
                if width > image.width:
                    # A trimmed screen is a few pixels narrower than its nominal top width.
                    if not (crop and width == widths[-1]):
                        continue
                    width = image.width
                webp, height = _encode(image, width, 'WEBP')
                if width == image.width and not crop and len(webp) >= len(original):
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
    attrs = {
        'src': fallback['url'],
        'srcset': ', '.join(f'{item["url"]} {item["width"]}w' for item in variants),
        'sizes': sizes or DEFAULT_SIZES[record['role']],
        'decoding': 'async',
    }
    if record.get('crop'):
        # Reserve the trimmed derivative's true aspect ratio.
        attrs['width'] = str(record['derivative_width'])
        attrs['height'] = str(record['derivative_height'])
    return attrs


def avif_source_attrs(src: str, *, sizes: str | None = None) -> dict:
    """Return attrs for the hero AVIF picture source, or {} for other images."""
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
    # Uncompressed BMP frames: PNG frames depend on the platform's zlib build,
    # which would make the committed file differ between machines.
    frames[-1].save(output, format='ICO', sizes=[frame.size for frame in frames],
                    append_images=frames[:-1], bitmap_format='bmp')
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
