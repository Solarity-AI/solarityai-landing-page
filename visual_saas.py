"""The three web apps on Home and Platform, introduced from their own sites (saas_products.py)."""
from html import escape as e

from saas_products import MOBILE_PLAN
from visual_products import _EXPAND_ICON as _EXPAND

NEW_TAB = '<span class="sr-only"> (opens in a new tab)</span>'


def saas_status(product):
    return '<span class="status"><i aria-hidden="true"></i>' + e(product['status']) + '</span>'


def site_link(product, label=None, cls='text-link saas-site'):
    """The product's own site: it leaves Solarity AI, so ↗ and a new tab."""
    return (f'<a class="{cls}" href="{e(product["url"])}" target="_blank" rel="noopener noreferrer">'
            f'{e(label or product["domain"])} <span aria-hidden="true">↗</span>{NEW_TAB}</a>')


def web_window(product, screen, sizes, eager=False, low=False):
    """A real screenshot in a quiet browser frame that names the product's own address."""
    loading = ('' if eager else ' loading="lazy"') + (' fetchpriority="low"' if low else '')
    focus = f' style="object-position:{e(screen["focus"])}"' if screen.get('focus') else ''
    tall = ' web-window--tall' if screen['height'] > screen['width'] * 0.9 else ''
    return (f'<span class="web-window{tall}"><span class="web-bar" aria-hidden="true"><i></i><i></i><i></i>'
            f'<span>{e(product["domain"])}</span></span>'
            f'<img class="web-shot"{focus} src="/assets/{e(screen["file"])}" alt="{e(screen["alt"])}" '
            f'width="{screen["width"]}" height="{screen["height"]}" sizes="{sizes}"{loading} decoding="async"></span>')


CARD_SIZES = '(max-width: 560px) calc(100vw - 72px), (max-width: 850px) calc(100vw - 96px), 400px'


def saas_cards(saas, prefix, label='Solarity AI web apps', compact=False):
    """The three web apps as cards: a real product screen, stage, name, category, status and site link.
    Each card links to its Platform chapter; the site link leaves Solarity AI."""
    cards = []
    for product in saas:
        slug, name = e(product['slug']), e(product['name'])
        tagline = '' if compact else f'<p class="saas-card-tagline">{e(product["tagline"])}</p>'
        cards.append(
            f'<li class="saas-card" id="{prefix}-{slug}">'
            f'<a class="saas-card-link" href="/platform#{slug}">'
            f'{web_window(product, product["screens"][0], CARD_SIZES, low=True)}'
            f'<span class="saas-card-copy"><span class="saas-stage">{e(product["stage"])}</span>'
            f'<strong>{name}</strong><small>{e(product["category"])}</small></span></a>{tagline}'
            f'<p class="saas-card-meta">{saas_status(product)}{site_link(product, "Visit site")}</p></li>'
        )
    return f'<ul class="saas-grid{" saas-grid--compact" if compact else ""}" aria-label="{e(label)}">' + ''.join(cards) + '</ul>'


def saas_wall(saas):
    """Home: the three web apps beside the consumer apps, each a card with its real product screen."""
    return f'''<section class="company-strategy saas-wall" id="web-apps" aria-labelledby="strategy-title"><div class="wrap">
      <div class="saas-heading"><div class="strategy-copy"><p class="eyebrow">The app factory</p><h2 id="strategy-title">Build the product. <br><span>Improve the way it gets built.</span></h2></div>
      <div class="saas-heading-copy"><p>Each app starts with a distinct human ambition. Building these products also shaped three web apps for the work behind them: engineering, management, and marketing.</p><p class="saas-plan">{MOBILE_PLAN}</p><a class="text-link" href="/platform">Explore the app factory <span aria-hidden="true">→</span></a></div></div>
      {saas_cards(saas, 'home')}
    </div></section>'''


def apps_web_band(saas):
    """Apps: the portfolio page also lists the three web apps, after the consumer world bands."""
    return f'''<section class="apps-web wrap" id="web-apps" aria-labelledby="apps-web-title">
      <div class="saas-heading"><div><p class="eyebrow">Web apps</p><h2 id="apps-web-title">For the teams who build apps.</h2></div>
      <div class="saas-heading-copy"><p>Engineering Max, Management Max, and Marketing Max, built alongside the consumer apps for the work behind them.</p><p class="saas-plan">{MOBILE_PLAN}</p><a class="text-link" href="/platform">Explore the app factory <span aria-hidden="true">→</span></a></div></div>
      {saas_cards(saas, 'apps')}
    </section>'''


def showroom_web(saas):
    """Investors: the web apps follow the four framed mobile apps in the opening showroom."""
    return (f'<div class="showroom-web" id="web-apps"><p class="eyebrow">Web apps</p>'
            f'{saas_cards(saas, "investors", compact=True)}</div>')


def _enlargeable(product, screen, sizes):
    """A chapter screen that opens in the page's screenshot viewer, with the full-size image as its native link."""
    title = e(product['name'] + ' screenshot')
    return (f'<a class="screenshot-open" href="/assets/{e(screen["file"])}" data-image-title="{title}" '
            f'data-image-alt="{e(screen["alt"])}" data-image-caption="{e(product["caption"])}" target="_blank" rel="noopener">{web_window(product, screen, sizes)}'
            f'<span class="screenshot-enlarge">{_EXPAND}<span>Enlarge<span class="sr-only"> {e(product["name"])} screenshot</span></span></span></a>')


def saas_chapter(product, index):
    """Platform: one numbered chapter per web app, its copy beside its real screens."""
    slug, name = e(product['slug']), e(product['name'])
    facts = ''.join(f'<li>{e(fact)}</li>' for fact in product['facts'])
    screens = product['screens']
    lead = _enlargeable(product, screens[0], '(max-width: 850px) 92vw, 720px')
    extra = ''.join(_enlargeable(product, s, '(max-width: 850px) 92vw, 720px') for s in screens[1:])
    return (f'<section class="saas-chapter{" saas-chapter--flip" if index % 2 else ""}" id="{slug}" aria-labelledby="{slug}-title">'
            f'<div class="saas-chapter-copy"><div class="module-num" aria-hidden="true">{e(product["number"])}</div>'
            f'<p class="saas-category">{e(product["category"])}</p><h2 id="{slug}-title">{name}</h2>{saas_status(product)}'
            f'<p class="saas-tagline">{e(product["tagline"])}</p><p>{e(product["summary"])}</p>'
            f'<ul class="saas-facts">{facts}</ul><p class="saas-availability">{e(product["availability"])}</p>'
            f'<div class="actions">{site_link(product, "Visit " + product["domain"], "button outline")}</div></div>'
            f'<figure class="saas-chapter-art">{lead}{extra}<figcaption class="caption">{e(product["caption"])}</figcaption></figure></section>')


def saas_chapters(saas):
    index = ''.join(f'<a href="#{e(p["slug"])}"><span>{e(p["stage"])}</span>{e(p["name"])}</a>' for p in saas)
    return ('<div class="wrap saas-chapters"><nav class="saas-index" aria-label="Web apps on this page">' + index + '</nav>'
            + ''.join(saas_chapter(p, i) for i, p in enumerate(saas)) + '</div>')
