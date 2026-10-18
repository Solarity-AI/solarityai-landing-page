"""Editorial app discovery, with authentic assets and native navigation."""
from html import escape as e
from visual_products import voice_symbol


def store_name_note(app):
    return ('<p class="product-store-name">Listed in app stores as '+e(app['store_name'])+'.</p>') if app.get('store_name') else ''


def home_portfolio(apps, btn):
    """A store-listed product gallery with optional product-vision entries."""
    cards = []
    for app in apps:
        if not app.get('screen') or not app.get('apple'):
            continue
        cards.append(f'''<a class="catalog-card" data-product-accent="{e(app['color'])}" href="/apps/{e(app['slug'])}">
          <div class="catalog-card-copy"><div class="catalog-card-heading"><img src="/assets/{e(app['slug'])}-icon.webp" width="40" height="40" alt="" loading="lazy"><div class="catalog-card-identity"><p class="catalog-category">{e(app['category'])}</p><h3>{e(app['name'])}</h3></div></div><span class="catalog-availability">iOS &amp; Android</span><p class="catalog-card-summary">{e(app['summary'])}</p>{store_name_note(app)}</div>
          <div class="catalog-image-stage"><img src="/assets/{e(app['screen'])}" alt="{e(app['name'])} official promotional screenshot with sample app content" width="{app.get('screen_width',600)}" height="{app.get('screen_height',1298)}" loading="lazy"></div>
          <span class="catalog-card-action">Explore {e(app['name'])}<span aria-hidden="true">→</span></span>
        </a>''')
    visions = []
    for app in apps:
        if app.get('screen') and app.get('apple'):
            continue
        visions.append(f'''<a class="catalog-vision-link" data-product-accent="{e(app['color'])}" href="/apps/{e(app['slug'])}"><span class="catalog-vision-symbol">{voice_symbol(52)}</span><div><span class="catalog-vision-label">PRODUCT VISION</span><h3>{e(app['name'])}</h3><p>{e(app['summary'])}</p></div><span class="catalog-vision-action">Explore the direction <span aria-hidden="true">→</span></span></a>''')
    vision_markup = '<div class="catalog-vision-list">'+''.join(visions)+'</div>' if visions else ''
    return f'''<section class="catalog-home wrap" id="our-products" aria-labelledby="catalog-home-title"><div class="catalog-section-heading"><div><p class="eyebrow">THE APP PORTFOLIO</p><h2 id="catalog-home-title">Everyday ambitions.<br><span class="muted">Focused experiences.</span></h2></div><p>From self-care to cognitive practice, sleep, and fitness, explore the products behind our company strategy.</p></div><div class="catalog-gallery">{''.join(cards)}</div><p class="catalog-image-note">Official app imagery · sample content</p>{vision_markup}<div class="catalog-section-footer"><span>Individual products. A shared ambition.</span>{btn('View the full portfolio','/apps','text')}</div></section>'''


def portfolio_page(apps, btn, app_art, product_status):
    """A concise image-led collection. The detail pages own the full stories."""
    links = []
    rows = []
    for app in apps:
        slug = e(app['slug'])
        name = e(app['name'])
        links.append(f'<a href="#{slug}"><span>{name}</span><span aria-hidden="true">↓</span></a>')
        rows.append(f'''<article class="catalog-product-row" id="{slug}" data-product-accent="{e(app['color'])}" aria-labelledby="catalog-{slug}-title">
          <header class="catalog-product-masthead"><p class="catalog-category">{e(app['category'])}</p><h2 id="catalog-{slug}-title">{name}</h2></header>
          <div class="catalog-product-art">{app_art(app,True)}</div>
          <div class="catalog-product-copy"><p class="catalog-product-summary">{e(app['summary'])}</p>{store_name_note(app)}<div class="catalog-product-status">{product_status(app,True)}</div><div class="catalog-product-actions">{btn('Explore '+app['name'],'/apps/'+app['slug'],'text')}</div></div>
        </article>''')
    return f'''<section class="catalog-page-intro wrap"><div class="catalog-intro-heading"><p class="eyebrow">THE CONSUMER PORTFOLIO</p><h1>One ambition.<br><span class="muted">Your next step.</span></h1></div><p class="catalog-intro-description">Self-care, cognitive practice, sleep, and fitness. Four focused apps for the routines you choose to build.</p></section><nav class="catalog-anchor-nav wrap" aria-label="Explore the apps">{''.join(links)}</nav><section class="catalog-product-list wrap" aria-label="Solarity AI apps">{''.join(rows)}</section>'''
