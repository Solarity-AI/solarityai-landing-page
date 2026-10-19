"""The three web apps on Home and Platform, introduced from their own sites (saas_products.py)."""
from html import escape as e

from saas_products import MOBILE_PLAN

NEW_TAB = '<span class="sr-only"> (opens in a new tab)</span>'


def saas_status(product):
    return '<span class="status"><i aria-hidden="true"></i>' + e(product['status']) + '</span>'


def site_link(product, label=None, cls='text-link saas-site'):
    """The product's own site: it leaves Solarity AI, so ↗ and a new tab."""
    return (f'<a class="{cls}" href="{e(product["url"])}" target="_blank" rel="noopener noreferrer">'
            f'{e(label or product["domain"])} <span aria-hidden="true">↗</span>{NEW_TAB}</a>')


def web_window(product, screen, sizes, eager=False):
    """A real screenshot in a quiet browser frame that names the product's own address."""
    loading = '' if eager else ' loading="lazy"'
    focus = f' style="object-position:{e(screen["focus"])}"' if screen.get('focus') else ''
    tall = ' web-window--tall' if screen['height'] > screen['width'] * 0.9 else ''
    return (f'<span class="web-window{tall}"><span class="web-bar" aria-hidden="true"><i></i><i></i><i></i>'
            f'<span>{e(product["domain"])}</span></span>'
            f'<img class="web-shot"{focus} src="/assets/{e(screen["file"])}" alt="{e(screen["alt"])}" '
            f'width="{screen["width"]}" height="{screen["height"]}" sizes="{sizes}"{loading} decoding="async"></span>')


def saas_wall(saas):
    """Home: the three web apps beside the consumer apps, each a card with its real product screen."""
    cards = []
    for product in saas:
        slug, name = e(product['slug']), e(product['name'])
        cards.append(
            f'<li class="saas-card" id="home-{slug}">'
            f'<a class="saas-card-link" href="/platform#{slug}">'
            f'{web_window(product, product["screens"][0], "(max-width: 850px) 92vw, 400px")}'
            f'<span class="saas-card-copy"><span class="saas-stage">{e(product["stage"])}</span>'
            f'<strong>{name}</strong><small>{e(product["category"])}</small></span></a>'
            f'<p class="saas-card-tagline">{e(product["tagline"])}</p>'
            f'<p class="saas-card-meta">{saas_status(product)}{site_link(product, "Visit site")}</p></li>'
        )
    return f'''<section class="company-strategy saas-wall" id="web-apps" aria-labelledby="strategy-title"><div class="wrap">
      <div class="saas-heading"><div class="strategy-copy"><p class="eyebrow">The app factory</p><h2 id="strategy-title">Build the product. <br><span>Improve the way it gets built.</span></h2></div>
      <div class="saas-heading-copy"><p>Each app starts with a distinct human ambition. Building these products also shaped three web apps for the work behind them: engineering, management and marketing.</p><p class="saas-plan">{MOBILE_PLAN}</p><a class="text-link" href="/platform">Explore the app factory <span aria-hidden="true">→</span></a></div></div>
      <ul class="saas-grid" aria-label="Solarity AI web apps">{''.join(cards)}</ul>
    </div></section>'''


def saas_chapter(product, index):
    """Platform: one numbered chapter per web app, its copy beside its real screens."""
    slug, name = e(product['slug']), e(product['name'])
    facts = ''.join(f'<li>{e(fact)}</li>' for fact in product['facts'])
    screens = product['screens']
    lead = web_window(product, screens[0], '(max-width: 850px) 92vw, 720px')
    extra = ''.join(web_window(product, s, '(max-width: 850px) 92vw, 720px') for s in screens[1:])
    return (f'<section class="saas-chapter{" saas-chapter--flip" if index % 2 else ""}" id="{slug}" aria-labelledby="{slug}-title">'
            f'<span class="module-word" aria-hidden="true">{e(product["stage"])}</span>'
            f'<div class="saas-chapter-copy"><div class="module-num" aria-hidden="true">{e(product["number"])}</div>'
            f'<p class="saas-category">{e(product["category"])}</p><h2 id="{slug}-title">{name}</h2>{saas_status(product)}'
            f'<p class="saas-tagline">{e(product["tagline"])}</p><p>{e(product["summary"])}</p>'
            f'<ul class="saas-facts">{facts}</ul><p class="saas-availability">{e(product["availability"])}</p>'
            f'<div class="actions">{site_link(product, "Visit " + product["domain"], "button outline")}</div></div>'
            f'<figure class="saas-chapter-art">{lead}{extra}<figcaption class="caption">{e(product["caption"])}</figcaption></figure></section>')


def saas_chapters(saas):
    return '<div class="wrap saas-chapters">' + ''.join(saas_chapter(p, i) for i, p in enumerate(saas)) + '</div>'
