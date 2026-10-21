"""The press kit: approved descriptions, company facts and images for articles, programs and event pages."""
import io
import zipfile
from pathlib import Path

from saas_products import SAAS
from templating import render
from ux_components import copy_button
from visual_record import record_summary
from visual_team import TEAM_MEMBERS

ONE_LINE = 'Solarity AI builds AI self-improvement apps and the tools that let its small team ship them fast.'
SHORT = ('Solarity AI LLC, based in Irving, Texas, builds AI-powered self-improvement apps: Looks Max, IQ Max, Sleep Max, '
         'and Fitness Max (listed in the app stores as Only Fitness), all on iOS and Android. Building them shaped three web apps '
         'for teams that build mobile products: Engineering Max, Management Max, and Marketing Max. Founder: Ata Turhan.')

# Approved images only: the official sun mark (make_press_assets.py), the founder portrait from the company's own
# site, and the official app icons from the store listings (research-assets/downloaded-assets.json).
ROOT = Path(__file__).resolve().parent

# Each image: main download, preview, label, format note, kind, and the WebP original when the main one is a copy
# (make_press_assets.py writes the JPEG and PNG copies: many publishing tools refuse WebP).
IMAGES = [
    ('/assets/press/solarity-sun-mark.png', '/assets/press/solarity-sun-mark.png', 'Solarity AI sun mark', 'PNG · 1024 × 1026 · transparent', 'mark', ''),
    ('/assets/press/ata-turhan-founder.jpg', '/assets/brand/ata-turhan-640.742556487789.webp', 'Ata Turhan, founder', 'JPEG · 800 × 800', 'portrait',
     '/assets/brand/ata-turhan-original.webp'),
]
# Product screens, each with the caption its evidence supports (CONTENT_REGISTER.md).
SCREENS = [
    ('looks-max-screen-4.webp', 'looks-max-screen.jpg', 'Looks Max', 1284, 2778, 'Official App Store image with sample content'),
    ('iq-max-screen-1.webp', 'iq-max-screen.jpg', 'IQ Max', 1284, 2778, 'Official App Store image with sample content'),
    ('sleep-max-screen-4.webp', 'sleep-max-screen.jpg', 'Sleep Max', 1284, 2778, 'Official App Store image with sample content'),
    ('fitness-max-screen-2.webp', 'fitness-max-screen.jpg', 'Fitness Max', 1284, 2778, 'Official App Store image with sample content'),
    ('engineering-max-overview.webp', 'engineering-max-screen.jpg', 'Engineering Max', 1800, 662, 'From its own site: its scan of Solarity AI’s Sleep Max'),
    ('management-max-overview.webp', 'management-max-screen.jpg', 'Management Max', 1160, 1280, 'From its own site, with sample apps and figures'),
    ('marketing-max-home.webp', 'marketing-max-screen.jpg', 'Marketing Max', 2880, 1800, 'From its own site, with sample data'),
]


KIT_PATH = '/assets/press/solarity-ai-press-kit.zip'


def _asset_bytes(public):
    """A published asset's bytes, from source-assets/ when it is a build input, otherwise from dist/."""
    relative = public.removeprefix('/assets/')
    for base in (ROOT / 'source-assets', ROOT / 'dist' / 'assets'):
        if (base / relative).is_file():
            return (base / relative).read_bytes()
    raise FileNotFoundError(public)


def press_kit_zip(apps):
    """Every press image and the approved descriptions, stored (not recompressed) with fixed metadata,
    so the archive is byte-identical on every machine."""
    files = [('solarity-sun-mark.png', IMAGES[0][0]), ('ata-turhan-founder.jpg', IMAGES[1][0])]
    files += [(f'{a["slug"]}-icon.png', f'/assets/press/{a["slug"]}-icon.png') for a in apps if a.get('apple')]
    files += [(f'screens/{copy}', f'/assets/press/{copy}') for _, copy, *_ in SCREENS]
    text = (f'Solarity AI press kit\n\nOne line\n{ONE_LINE}\n\nShort description\n{SHORT}\n\n'
            'Write the name as Solarity AI. Use the sun mark as supplied; do not recolor, stretch, or redraw it.\n'
            'Fitness Max appears in the app stores as Only Fitness.\n'
            'Product screens show sample content: app screens are official App Store images; web app screens come from each\n'
            'product\'s own site (Engineering Max shows its scan of Solarity AI\'s Sleep Max).\n\nSource: https://solarityai.com/press/\n')
    entries = [('README.txt', text.encode('utf-8'))] + [(name, _asset_bytes(public)) for name, public in files]
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_STORED) as archive:
        for name, data in entries:
            info = zipfile.ZipInfo('solarity-ai-press-kit/' + name, date_time=(2026, 10, 20, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def press_page(apps, email, btn):
    icons = [(f'/assets/press/{a["slug"]}-icon.png', f'/assets/{a["slug"]}-icon.webp', a['name']) for a in apps if a.get('apple')]
    screens = [{'preview': '/assets/' + original, 'href': '/assets/press/' + copy, 'original': '/assets/' + original, 'name': name,
                'width': width, 'height': height, 'caption': caption} for original, copy, name, width, height, caption in SCREENS]
    return str(render('visual_press/page.html.j2', one_line=ONE_LINE, short=SHORT, images=IMAGES, icons=icons, screens=screens,
                      copy_one=copy_button(ONE_LINE, 'press-one-line-status', 'Copy', 'The one-line description'),
                      copy_short=copy_button(SHORT, 'press-short-status', 'Copy', 'The short description'),
                      record=record_summary(), saas=SAAS, email=email, team=TEAM_MEMBERS,
                      copy_link=copy_button('https://solarityai.com/press/', 'press-link-status', 'Copy page link', 'The page link'),
                      contact_button=btn('Press inquiries', '/contact?type=Press#prepare-inquiry', 'outline'),
                      kit_href=KIT_PATH, kit_size=f'{len(press_kit_zip(apps)) / 1_000_000:.1f} MB'))
