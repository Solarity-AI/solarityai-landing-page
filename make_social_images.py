"""Write the 1200x630 link-preview images into source-assets/social/ (run by hand, then commit).

Each image is composed only from published, approved material: the hero master, the official app
icons and store screenshots, the web app screenshots (research-assets/saas-evidence.json), the
official sun mark and the site's own fonts. The text is limited to product and page names. The
build publishes these files when a page references them, so the committed bytes are what deploys.

    python make_social_images.py
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from saas_products import SAAS

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source-assets'
PUBLISHED = ROOT / 'dist' / 'assets'
OUT = SOURCE / 'social'
REPORT = ROOT / 'research-assets' / 'social-images.json'
W, H = 1200, 630
DISPLAY = PUBLISHED / 'fonts' / 'newsreader-display-latin.16985410e5b5.woff2'
BODY = PUBLISHED / 'fonts' / 'manrope-latin-variable.cfa570d7c3ee.woff2'
IVORY, SAND, MUTED = (245, 241, 232), (214, 191, 154), (201, 192, 178)
BG = (15, 13, 11)

# The four mobile apps, as on their pages (build_site.APPS): name, category, world colours, hero screen and focus.
APPS = [
    ('looks-max', 'Looks Max', 'Appearance & self-care', (30, 15, 48), (122, 53, 201), 'looks-max-screen-4.webp', (0.5, 0.64)),
    ('iq-max', 'IQ Max', 'Cognitive practice', (12, 24, 56), (42, 79, 208), 'iq-max-detail-screen-4.webp', (0.5, 0.68)),
    ('sleep-max', 'Sleep Max', 'Sleep & daily routines', (15, 18, 48), (58, 66, 176), 'sleep-max-screen-4.webp', (0.5, 0.22)),
    ('fitness-max', 'Fitness Max', 'Fitness & nutrition', (22, 11, 6), (255, 90, 31), 'fitness-max-screen-2.webp', (0.5, 0.72)),
]


def asset(name: str) -> Image.Image:
    path = PUBLISHED / name if (PUBLISHED / name).exists() else SOURCE / name
    return Image.open(path).convert('RGB')


def font(path: Path, size: int, weight: int | None = None) -> ImageFont.FreeTypeFont:
    face = ImageFont.truetype(str(path), size)
    if weight is not None:
        try:
            face.set_variation_by_axes([weight])
        except (OSError, ValueError):
            pass
    return face


def cover(image: Image.Image, size: tuple[int, int], focus=(0.5, 0.5)) -> Image.Image:
    """Scale to fill, then crop around the focus point; never stretch."""
    scale = max(size[0] / image.width, size[1] / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = round((resized.width - size[0]) * focus[0])
    top = round((resized.height - size[1]) * focus[1])
    return resized.crop((left, top, left + size[0], top + size[1]))


def rounded(image: Image.Image, radius: int) -> tuple[Image.Image, Image.Image]:
    mask = Image.new('L', image.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, image.width - 1, image.height - 1), radius, fill=255)
    return image, mask


def glow(canvas: Image.Image, centre, radius, colour, strength):
    layer = Image.new('RGB', canvas.size, (0, 0, 0))
    ImageDraw.Draw(layer).ellipse((centre[0] - radius, centre[1] - radius, centre[0] + radius, centre[1] + radius), fill=colour)
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 0.55))
    return Image.blend(canvas, Image.composite(layer, canvas, layer.convert('L')), strength)


def place(canvas: Image.Image, image: Image.Image, xy, radius=18, shadow=True):
    image, mask = rounded(image, radius)
    if shadow:
        shade = Image.new('L', canvas.size, 0)
        ImageDraw.Draw(shade).rounded_rectangle((xy[0], xy[1] + 18, xy[0] + image.width, xy[1] + image.height + 18), radius, fill=170)
        shade = shade.filter(ImageFilter.GaussianBlur(26))
        canvas.paste(Image.new('RGB', canvas.size, (0, 0, 0)), (0, 0), shade)
    canvas.paste(image, xy, mask)


def signature(canvas: Image.Image, xy=(72, 556)):
    sun = Image.open(PUBLISHED / 'brand' / 'solarity-sun-96.da9c18cba138.webp').convert('RGBA').resize((40, 40), Image.Resampling.LANCZOS)
    canvas.paste(sun, xy, sun)
    draw = ImageDraw.Draw(canvas)
    word = font(BODY, 24, 700)
    draw.text((xy[0] + 54, xy[1] + 7), 'SOLARITY', font=word, fill=IVORY)
    draw.text((xy[0] + 54 + draw.textlength('SOLARITY ', font=word), xy[1] + 7), 'AI', font=word, fill=SAND)


def gradient(deep) -> Image.Image:
    canvas = Image.new('RGB', (W, H), BG)
    top = Image.new('RGB', (W, H), deep)
    mask = Image.linear_gradient('L').rotate(90).resize((W, H))
    return Image.composite(top, canvas, mask)


def product_card(slug, name, category, deep, world, screen, focus) -> Image.Image:
    canvas = gradient(deep)
    canvas = glow(canvas, (880, 330), 300, world, 0.55)
    window = cover(asset(screen), (330, 440), focus)
    place(canvas, window, (715, 95), radius=22)
    icon = asset(f'{slug}-icon.webp').resize((112, 112), Image.Resampling.LANCZOS)
    place(canvas, icon, (72, 120), radius=27, shadow=False)
    draw = ImageDraw.Draw(canvas)
    draw.text((72, 262), name, font=font(DISPLAY, 96), fill=IVORY)
    draw.text((76, 392), category, font=font(BODY, 30, 500), fill=SAND)
    draw.text((76, 438), 'iOS & Android', font=font(BODY, 24, 500), fill=MUTED)
    signature(canvas)
    return canvas


def platform_card() -> Image.Image:
    canvas = gradient((13, 16, 20))
    canvas = glow(canvas, (860, 300), 320, (255, 190, 110), 0.22)
    shots = [(product, product['screens'][0]) for product in SAAS]
    for index, (product, screen) in enumerate(shots):
        image = cover(asset(screen['file']), (420, 250), (0.0, 0.0) if product['slug'] == 'engineering-max' else (0.5, 0.0))
        place(canvas, image, (650 + index * 54, 60 + index * 140), radius=14)
    draw = ImageDraw.Draw(canvas)
    draw.text((72, 150), 'The app', font=font(DISPLAY, 100), fill=IVORY)
    draw.text((72, 262), 'factory.', font=font(DISPLAY, 100), fill=(255, 207, 122))
    draw.text((76, 404), 'Engineering Max · Management Max', font=font(BODY, 27, 500), fill=SAND)
    draw.text((76, 442), 'Marketing Max', font=font(BODY, 27, 500), fill=SAND)
    signature(canvas)
    return canvas


def portfolio_card(title_lines, kicker) -> Image.Image:
    canvas = gradient((23, 17, 12))
    canvas = glow(canvas, (870, 315), 330, (255, 190, 110), 0.25)
    for index, (slug, _name, _category, _deep, world, _screen, _focus) in enumerate(APPS):
        x, y = 790 + (index % 2) * 176, 130 + (index // 2) * 176
        canvas = glow(canvas, (x + 70, y + 70), 100, world, 0.45)
        icon = asset(f'{slug}-icon.webp').resize((140, 140), Image.Resampling.LANCZOS)
        place(canvas, icon, (x, y), radius=34)
    draw = ImageDraw.Draw(canvas)
    # The title fits the left column: it never runs into the icons.
    size = 80
    while size > 48 and max(draw.textlength(line, font=font(DISPLAY, size)) for line in title_lines) > 640:
        size -= 2
    for index, line in enumerate(title_lines):
        draw.text((72, 168 + index * round(size * 1.2)), line, font=font(DISPLAY, size), fill=IVORY if index == 0 else (255, 207, 122))
    draw.text((76, 404), kicker, font=font(BODY, 27, 500), fill=SAND)
    signature(canvas)
    return canvas


def default_card() -> Image.Image:
    """The approved sunrise at link-preview proportions, with the sun mark; no added text beyond the name."""
    canvas = cover(asset('solar-ascent.webp'), (W, H), (0.78, 0.42))
    shade = Image.linear_gradient('L').rotate(-90).resize((W, H)).point(lambda v: int(v * 0.55))
    canvas.paste(Image.new('RGB', (W, H), (12, 9, 6)), (0, 0), shade)
    signature(canvas, (72, 72))
    return canvas


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    cards = {'default': default_card(), 'platform': platform_card(),
             'apps': portfolio_card(['Apps for', 'everyday ambition.'], 'Four mobile apps · three web apps'),
             'investors': portfolio_card(['Products today.', 'Possibility ahead.'], 'Investors & partners')}
    for app in APPS:
        cards[app[0]] = product_card(*app)
    record = {'size': [W, H], 'note': __doc__.strip().splitlines()[0], 'files': {}}
    for name, image in cards.items():
        target = OUT / f'{name}.jpg'
        image.save(target, format='JPEG', quality=88, optimize=True, progressive=True)
        record['files'][f'/assets/social/{name}.jpg'] = {'bytes': target.stat().st_size, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}
        print(target.relative_to(ROOT), target.stat().st_size)
    REPORT.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
