"""The press kit: approved descriptions, company facts and images for articles, programs and event pages."""
from saas_products import SAAS
from templating import render
from ux_components import copy_button
from visual_record import record_summary

ONE_LINE = 'Solarity AI builds AI self-improvement apps and the tools that let its small team ship them fast.'
SHORT = ('Solarity AI LLC, based in Irving, Texas, builds AI-powered self-improvement apps: Looks Max, IQ Max, Sleep Max, '
         'and Fitness Max (listed in the app stores as Only Fitness), all on iOS and Android. Building them shaped three web apps '
         'for teams that build mobile products: Engineering Max, Management Max, and Marketing Max. Founder: Ata Turhan.')

# Approved images only: the official sun mark (make_press_assets.py), the founder portrait from the company's own
# site, and the official app icons from the store listings (research-assets/downloaded-assets.json).
IMAGES = [
    ('/assets/press/solarity-sun-mark.png', '/assets/press/solarity-sun-mark.png', 'Solarity AI sun mark', 'PNG · 1024 × 1026 · transparent', 'mark'),
    ('/assets/brand/ata-turhan-original.webp', '/assets/brand/ata-turhan-640.742556487789.webp', 'Ata Turhan, founder', 'WebP · 800 × 800', 'portrait'),
]


def press_page(apps, email, btn):
    icons = [(f'/assets/{a["slug"]}-icon.webp', a['name']) for a in apps if a.get('apple')]
    return str(render('visual_press/page.html.j2', one_line=ONE_LINE, short=SHORT, images=IMAGES, icons=icons,
                      copy_one=copy_button(ONE_LINE, 'press-one-line-status', 'Copy', 'The one-line description'),
                      copy_short=copy_button(SHORT, 'press-short-status', 'Copy', 'The short description'),
                      record=record_summary(), saas=SAAS, email=email,
                      contact_button=btn('Press inquiries', '/contact?type=Other#prepare-inquiry', 'outline')))
