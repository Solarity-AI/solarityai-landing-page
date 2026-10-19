"""Native, script-free portfolio preview using the maintained app records."""
from html import escape as e


def product_explorer(apps, btn):
    """Render a four-product selector without creating a second content model."""
    radios, choices, panels = [], [], []
    for index, app in enumerate(apps, 1):
        slug = e(app['slug'])
        choice_id = 'explorer-' + slug
        panel_id = 'explorer-panel-' + slug
        title_id = panel_id + '-title'
        selected = ' checked' if index == 1 else ''
        radios.append(
            f'<input class="explorer-radio" type="radio" name="portfolio-preview" '
            f'id="{choice_id}" value="{slug}" aria-controls="{panel_id}"{selected}>'
        )
        choices.append(f'''<label class="explorer-choice" for="{choice_id}" data-product-accent="{e(app['color'])}">
          <img src="/assets/{slug}-icon.webp" width="44" height="44" alt="" loading="lazy">
          <span class="explorer-choice-copy"><strong>{e(app['name'])}</strong><small>{e(app['category'])}</small></span>
          <span class="explorer-choice-check" aria-hidden="true">✓</span>
        </label>''')
        alias = (f'<p class="explorer-store-name">Listed in app stores as {e(app["store_name"])}.</p>'
                 if app.get('store_name') else '')
        features = ''.join(
            f'<li>{e(title)}</li>'
            for title, _ in app['features']
        )
        panels.append(f'''<article class="explorer-panel" id="{panel_id}" data-product-accent="{e(app['color'])}" aria-labelledby="{title_id}">
          <div class="explorer-panel-copy"><p class="explorer-category">{e(app['category'])}</p><h3 id="{title_id}">{e(app['name'])}</h3><p class="explorer-summary">{e(app['summary'])}</p><ul class="explorer-feature-list" aria-label="{e(app['name'])} features">{features}</ul><div class="explorer-store-context">{alias}</div></div>
          <figure class="explorer-figure"><img src="/assets/{e(app['screen'])}" alt="{e(app['name'])} official promotional screenshot with sample app content" width="{app.get('screen_width', 600)}" height="{app.get('screen_height', 1298)}" sizes="(max-width: 560px) 220px, (max-width: 850px) 250px, (max-width: 1100px) 280px, 300px" loading="lazy"><figcaption>Official app imagery · Sample content</figcaption></figure>
          <div class="explorer-panel-action"><span class="explorer-availability">Available on iOS&nbsp;&amp;&nbsp;Android</span>{btn('Explore '+app['name'], '/apps/'+app['slug'], 'outline')}</div>
        </article>''')
    return f'''<section class="product-explorer wrap" id="our-products" aria-labelledby="product-explorer-title">
      <div class="explorer-heading"><div><p class="eyebrow">THE APP PORTFOLIO</p><h2 id="product-explorer-title">Your ambition.<br><span class="muted">Your daily practice.</span></h2></div><p>Self-care, cognitive practice, sleep, and fitness. Four focused products, each built around a different part of everyday life.</p></div>
      <fieldset class="explorer-fieldset"><legend>Choose a product to preview</legend>{''.join(radios)}<div class="explorer-layout"><div class="explorer-choices">{''.join(choices)}</div><div class="explorer-stage">{''.join(panels)}</div></div></fieldset>
      <div class="explorer-footer"><p>Explore the approach, features, and store links for each app.</p>{btn('View the full portfolio', '/apps', 'text')}</div>
    </section>'''
