"""The three SaaS products on Home and Platform, introduced from their own sites (saas_products.py)."""
from saas_products import MOBILE_PLAN, SCREEN_NOTE
from templating import render


def saas_status(product):
    return str(render('visual_saas/status.html.j2', product=product))


def site_link(product, label=None, cls='text-link saas-site'):
    """The product's own site: it leaves Solarity AI, so ↗ and a new tab."""
    return str(render('visual_saas/site_link.html.j2', product=product, label=label or product['domain'], cls=cls))


def web_window(product, screen, sizes, eager=False, low=False):
    """A real screenshot in a quiet browser frame that names the product's own address."""
    tall = screen['height'] > screen['width'] * 0.9
    return str(render('visual_saas/web_window.html.j2', product=product, screen=screen, sizes=sizes,
                      eager=eager, low=low, tall=tall))


# Measured rendered widths, so browsers pick a file neither soft nor oversized.
CARD_SIZES = '(max-width: 560px) calc(100vw - 72px), (max-width: 850px) 46vw, (max-width: 1100px) 26vw, 400px'
CHAPTER_SIZES = '(max-width: 850px) 92vw, (max-width: 1100px) 48vw, 720px'
# A tall screen's frame stops at 478 px wide.
TALL_CHAPTER_SIZES = '(max-width: 520px) 92vw, 478px'


def saas_cards(saas, prefix, label='Solarity AI SaaS products', compact=False):
    """The three SaaS products as cards: a real product screen, stage, name, category, status and site link.
    Each card links to its Platform chapter; the site link leaves Solarity AI."""
    cards = [{'product': product,
              'window': web_window(product, product['screens'][0], CARD_SIZES, low=True),
              'status': saas_status(product),
              'link': site_link(product, 'Visit site')} for product in saas]
    return str(render('visual_saas/cards.html.j2', cards=cards, prefix=prefix, label=label, compact=compact, note=SCREEN_NOTE))


def saas_wall(saas):
    """Home: the three SaaS products beside the consumer apps, each a card with its real product screen."""
    return str(render('visual_saas/saas_wall.html.j2', mobile_plan=MOBILE_PLAN, cards=saas_cards(saas, 'home')))


def apps_web_band(saas):
    """Apps: the portfolio page also lists the three SaaS products, after the consumer world bands."""
    return str(render('visual_saas/apps_web_band.html.j2', mobile_plan=MOBILE_PLAN, cards=saas_cards(saas, 'apps')))


def showroom_web(saas):
    """Investors: the SaaS products follow the four framed mobile apps in the opening showroom."""
    return str(render('visual_saas/showroom_web.html.j2', cards=saas_cards(saas, 'investors', compact=True)))


def saas_chapter(product, index):
    """Platform: one numbered chapter per SaaS product, its copy beside its real screens.
    Each screen opens in the page's screenshot viewer, with the full-size image as its native link."""
    shots = [{'screen': screen, 'window': web_window(product, screen, TALL_CHAPTER_SIZES if screen['height'] > screen['width'] * 0.9 else CHAPTER_SIZES)} for screen in product['screens']]
    return str(render('visual_saas/chapter.html.j2', product=product, flip=index % 2, shots=shots,
                      status=saas_status(product),
                      link=site_link(product, 'Visit ' + product['domain'], 'button outline')))


def saas_chapters(saas):
    chapters = ''.join(saas_chapter(p, i) for i, p in enumerate(saas))
    return str(render('visual_saas/chapters.html.j2', saas=saas, chapters=chapters))
