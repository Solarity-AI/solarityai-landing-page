"""Product presentation built around authentic assets, without synthetic app screens."""
from image_provenance import provenance
from html import escape as e


def voice_symbol(size=44):
    """A decorative waveform, deliberately distinct from an official app icon."""
    size = max(16, int(size))
    return f'<svg class="voice-symbol" aria-hidden="true" focusable="false" viewBox="0 0 48 48" width="{size}" height="{size}" fill="none"><path d="M6 22v4m6-10v16m6-23v30m6-27v24m6-31v38m6-29v20m6-12v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


_EXPAND_ICON = '<svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def product_art(app, small=False):
    """A full, unaltered store image, with an accessible native zoom link."""
    color = e(app['color'])
    if not app.get('screen'):
        return ''
    title = e(app['name']) + ' screenshot'
    alt = e(app['name']) + ' official App Store imagery with sample app content'
    image = '/assets/' + e(app['screen'])
    sizes = ('(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, '
             '(max-width: 1024px) 290px, ' + ('320px' if small else '340px'))
    return f'''<figure class="app-art screenshot-art" data-product-accent="{color}">
      <a class="screenshot-open" href="{image}" data-image-title="{title}" data-image-alt="{alt}" target="_blank" rel="noopener">
        <span class="screenshot-stage"><img class="store-screen" src="{image}" alt="{alt}" width="{app.get('screen_width',600)}" height="{app.get('screen_height',1298)}" sizes="{sizes}" loading="lazy" decoding="async"></span>
        <span class="screenshot-enlarge">{_EXPAND_ICON}<span>Enlarge<span class="sr-only"> {e(app['name'])} screenshot</span></span></span>
      </a>
      <figcaption class="asset-caption caption">{provenance()}</figcaption>
    </figure>'''


def product_page(app, apps, btn, contact, stores, status, feature_markup, breadcrumbs, related_markup):
    """A product-specific composition with genuine imagery early in mobile order."""
    from product_story import product_story
    slug = e(app['slug'])
    name = e(app['name'])
    store_note = ('<p class="product-store-name">Listed in app stores as ' + e(app['store_name']) + '.</p>') if app.get('store_name') else ''
    quick_link = f'<a class="product-quick-link" href="#get-app">Get {name}<span aria-hidden="true">↓</span></a>' if app.get('apple') else ''
    fineprint = '<p class="fineprint">In-app purchases. See the stores for current plans and regional availability.</p>' if app.get('apple') else ''
    return f'''<div class="product-world" data-product="{slug}" data-product-accent="{e(app['color'])}">
      {breadcrumbs}
      <section class="product-hero wrap" aria-labelledby="product-title">
        <header class="product-hero-heading"><div class="product-identity"><img class="detail-icon" src="/assets/{slug}-icon.webp" width="56" height="56" alt=""><p class="eyebrow">{name}</p></div><h1 id="product-title">{e(app['headline'])}</h1>{quick_link}</header>
        <div class="product-hero-art">{product_art(app)}</div>
        <div class="product-hero-copy"><p class="lede">{e(app['intro'])}</p>{store_note}{status}<div class="actions" id="get-app">{stores}</div>{fineprint}</div>
      </section>
      {product_story(app)}
      {feature_markup}
      <aside class="product-note wrap" aria-label="Product context"><p><strong>Product context.</strong> {e(app['note'])}</p></aside>
      <section class="product-connect wrap"><div><h2>Let’s talk about {name}.</h2><p>For product questions, distribution opportunities, or a potential collaboration.</p></div><div class="actions">{btn('Ask about '+app['name'],contact('Product inquiry',app['name']),'outline')}{btn('All apps','/apps#'+app['slug'],'text')}</div></section>
      {related_markup}
    </div>'''


def evidence_band(apps, btn):
    """Make store-listed product evidence immediately identifiable."""
    links = []
    for app in apps:
        if not app.get('apple'):
            continue
        links.append(f'''<a class="evidence-product" href="/apps/{e(app['slug'])}" data-product-accent="{e(app['color'])}">
          <img src="/assets/{e(app['slug'])}-icon.webp" alt="" width="48" height="48" loading="lazy">
          <span><strong>{e(app['name'])}</strong><small>{e(app['category'])}</small><span class="evidence-product-status">iOS&nbsp;&amp;&nbsp;Android</span></span>
          <span class="evidence-product-arrow" aria-hidden="true">→</span>
        </a>''')
    return f'''<section class="proof-strip product-evidence-band wrap" aria-labelledby="product-evidence-title">
      <div class="product-evidence-intro"><p class="eyebrow">START WITH THE PRODUCTS</p><h2 id="product-evidence-title">Explore what is already in the stores.</h2><p>Review the app experiences, then talk with us about the company behind them.</p>{btn('View our apps','/apps','outline')}</div>
      <nav class="evidence-products" aria-label="Store-listed Solarity AI products">{''.join(links)}</nav>
    </section>'''
