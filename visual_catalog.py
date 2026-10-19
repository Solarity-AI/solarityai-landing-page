"""Editorial app discovery, with authentic assets and native navigation."""
from image_provenance import provenance
from html import escape as e
from visual_products import voice_symbol


def store_name_note(app):
    return ('<p class="product-store-name">Listed in app stores as '+e(app['store_name'])+'.</p>') if app.get('store_name') else ''


def _store_pair(app):
    """Compact text links to both stores; the product pages carry the official badges."""
    note = '<span class="sr-only"> (opens in a new tab)</span>'
    return (f'<a href="{e(app["apple"])}" target="_blank" rel="noopener noreferrer">App Store <span aria-hidden="true">↗</span>{note}</a>'
            f'<a href="{e(app["google"])}" target="_blank" rel="noopener noreferrer">Google Play <span aria-hidden="true">↗</span>{note}</a>')


def _window(app, sizes):
    focus = (' style="object-position:' + e(app['crop_focus']) + '"') if app.get('crop_focus') else ''
    return (f'<img class="store-screen plate--window"{focus} src="/assets/{e(app["screen"])}" '
            f'alt="{e(app["name"])} official App Store imagery with sample app content" '
            f'width="{app.get("screen_width", 600)}" height="{app.get("screen_height", 1298)}" sizes="{sizes}" loading="lazy" decoding="async">')


def portfolio_wall(apps):
    """Home: all four apps at once, each in its own world, each a single link to its page."""
    cards = []
    for app in apps:
        if not app.get('screen') or not app.get('apple'):
            continue
        slug, name = e(app['slug']), e(app['name'])
        cards.append(f'''<li class="wall-card" data-product-accent="{e(app['color'])}">
          <a class="wall-link" href="/apps/{slug}"><span class="wall-window screenshot-stage">{_window(app, '(max-width: 560px) 44vw, (max-width: 1100px) 22vw, 270px')}</span>
            <span class="wall-identity"><img src="/assets/{slug}-icon.webp" width="56" height="56" alt="" loading="lazy" decoding="async"><span><strong>{name}</strong><small>{e(app['category'])}</small></span></span></a>
          <p class="wall-stores">{_store_pair(app)}</p>
        </li>''')
    return f'''<section class="portfolio-wall wrap" id="our-products" aria-labelledby="wall-title">
      <div class="wall-heading"><div><p class="eyebrow">The app portfolio</p><h2 id="wall-title">Your ambition.<br><span class="muted">Your daily practice.</span></h2></div><p>Self-care, cognitive practice, sleep, and fitness. Four focused products, each built around a different part of everyday life.</p></div>
      <ul class="wall-grid" aria-label="Solarity AI apps">{''.join(cards)}</ul>
      <p class="caption wall-caption">{provenance()}</p>
    </section>'''


def portfolio_page(apps, btn, app_art, product_status):
    """Apps: a lineup of the four icons, then one world band per app. The detail pages own the stories."""
    from visual_stage import store_badges
    lineup = []
    bands = []
    for index, app in enumerate(apps):
        slug = e(app['slug'])
        name = e(app['name'])
        lineup.append(f'<a class="lineup-app" href="#{slug}" data-product-accent="{e(app["color"])}"><img src="/assets/{slug}-icon.webp" width="112" height="112" alt="" decoding="async"><span><strong>{name}</strong><small>{e(app["category"])}</small></span><span class="lineup-arrow" aria-hidden="true">↓</span></a>')
        disclosure = ('<p class="product-store-name">On the App Store and Google Play as ' + e(app['store_name']) + '.</p>') if app.get('store_name') else ''
        bands.append(f'''<article class="world-band{' world-band--flip' if index % 2 else ''}" id="{slug}" data-product-accent="{e(app['color'])}" aria-labelledby="catalog-{slug}-title">
          <div class="world-band-copy">
            <img class="world-band-icon" src="/assets/{slug}-icon.webp" width="64" height="64" alt="" loading="lazy" decoding="async">
            <p class="catalog-category">{e(app['category'])}</p>
            <h2 id="catalog-{slug}-title"><a class="catalog-product-link" href="/apps/{slug}">{name}</a></h2>
            <p class="world-band-summary">{e(app['summary'])}</p>
            <div class="world-band-stores">{store_badges(app)}{disclosure}</div>
            <a class="world-band-explore" href="/apps/{slug}">Explore {name} <span aria-hidden="true">→</span></a>
          </div>
          <div class="world-band-art"><span class="screenshot-stage">{_window(app, '(max-width: 560px) 70vw, 340px')}</span></div>
        </article>''')
    return f'''<section class="catalog-page-intro wrap"><div class="catalog-intro-heading"><p class="eyebrow">Consumer portfolio</p><h1>One ambition.<br><span class="muted">Your next step.</span></h1></div><p class="catalog-intro-description">Self-care, cognitive practice, sleep, and fitness. Four focused apps for the routines you choose to build.</p></section>
    <nav class="app-lineup wrap" aria-label="Explore the apps">{''.join(lineup)}</nav>
    <section class="world-bands" aria-label="Solarity AI apps">{''.join(bands)}</section>'''
