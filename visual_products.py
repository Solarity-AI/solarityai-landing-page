"""Product presentation built around authentic assets, without synthetic app screens."""
from image_provenance import provenance
from visual_stage import product_close
from html import escape as e


def voice_symbol(size=44):
    """A decorative waveform, deliberately distinct from an official app icon."""
    size = max(16, int(size))
    return f'<svg class="voice-symbol" aria-hidden="true" focusable="false" viewBox="0 0 48 48" width="{size}" height="{size}" fill="none"><path d="M6 22v4m6-10v16m6-23v30m6-27v24m6-31v38m6-29v20m6-12v4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


_EXPAND_ICON = '<svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def product_art(app, small=False, hero=False):
    """A full, unaltered store image, with an accessible native zoom link."""
    color = e(app['color'])
    screen = app.get('hero_screen') if hero else None
    screen = screen or app.get('screen')
    if not screen:
        return ''
    title = e(app['name']) + ' screenshot'
    alt = e(app.get('hero_alt') if hero and app.get('hero_alt') else app['name'] + ' official App Store imagery with sample app content')
    image = '/assets/' + e(screen)
    sizes = ('(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, (max-width: 1024px) 300px, 440px' if hero else
             '(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, '
             '(max-width: 1024px) 290px, ' + ('320px' if small else '340px'))
    return f'''<figure class="app-art screenshot-art" data-product-accent="{color}">
      <a class="screenshot-open" href="{image}" data-image-title="{title}" data-image-alt="{alt}" target="_blank" rel="noopener">
        <span class="screenshot-stage"><img class="store-screen{' plate--window' if hero else ''}"{(' style="object-position:' + e(app['crop_focus']) + '"') if hero and app.get('crop_focus') else ''} src="{image}" alt="{alt}" width="{app.get('screen_width',600)}" height="{app.get('screen_height',1298)}" sizes="{sizes}" loading="lazy" decoding="async"></span>
        <span class="screenshot-enlarge">{_EXPAND_ICON}<span>Enlarge<span class="sr-only"> {e(app['name'])} screenshot</span></span></span>
      </a>
      <figcaption class="asset-caption caption">{provenance()}</figcaption>
    </figure>'''


def product_page(app, apps, btn, contact, stores, status, feature_markup, breadcrumbs, related_markup):
    """Opening: the product's name as title in its world, real imagery staged beside it."""
    from product_story import product_story
    slug = e(app['slug'])
    name = e(app['name'])
    store_note = ('<p class="product-store-name">On the App Store and Google Play as ' + e(app['store_name']) + '.</p>') if app.get('store_name') else ''
    fineprint = '<p class="fineprint">In-app purchases. See the stores for current plans and regional availability.</p>' if app.get('apple') else ''
    return f'''<div class="product-world" data-product="{slug}" data-product-accent="{e(app['color'])}">
      {breadcrumbs}
      <section class="product-hero wrap" aria-labelledby="product-title">
        <header class="product-hero-heading"><div class="product-identity"><img class="detail-icon" src="/assets/{slug}-icon.webp" width="104" height="104" alt=""><p class="eyebrow">{e(app['category'])}</p></div><h1 id="product-title">{name}</h1><p class="product-deck">{e(app['headline'])}</p></header>
        <div class="product-hero-art">{product_art(app, hero=True)}</div>
        <div class="product-hero-copy"><p class="lede">{e(app['intro'])}</p><div class="product-get" id="get-app">{stores}</div>{store_note}{fineprint}</div>
      </section>
      {product_story(app)}
      {feature_markup}
      <aside class="product-note wrap" aria-label="Product context"><p><strong>Product context.</strong> {e(app['note'])}</p></aside>
      {product_close(app, btn, contact)}
      {related_markup}
    </div>'''

