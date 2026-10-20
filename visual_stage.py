"""Shared product staging: official store badges and the product close (CINEMATIC_PREMIUM_PLAN.md P5b)."""
from html import escape as e

APP_STORE_BADGE = '/assets/badges/app-store-badge-black.svg'
GOOGLE_PLAY_BADGE = '/assets/badges/google-play-badge.png'
_NEW_TAB = '<span class="sr-only"> (opens in a new tab)</span>'


def store_badges(app, fallback=''):
    """Official, unmodified badges. The ↗ sits outside each badge's clear space."""
    if not app.get('apple'):
        return fallback
    apple = (f'<a class="store-badge store-badge--apple" href="{e(app["apple"])}" target="_blank" rel="noopener noreferrer">'
             f'<img src="{APP_STORE_BADGE}" alt="Download {e(app["name"])} on the App Store" width="144" height="48" decoding="async">'
             f'<span class="store-badge-arrow" aria-hidden="true">↗</span>{_NEW_TAB}</a>')
    google = (f'<a class="store-badge store-badge--google" href="{e(app["google"])}" target="_blank" rel="noopener noreferrer">'
              f'<img src="{GOOGLE_PLAY_BADGE}" alt="Get {e(app["name"])} on Google Play" width="181" height="70" sizes="181px" decoding="async">'
              f'<span class="store-badge-arrow" aria-hidden="true">↗</span>{_NEW_TAB}</a>') if app.get('google') else ''
    return f'<div class="store-badges">{apple}{google}</div>'


def product_close(app, btn, contact):
    """The product page ends in its own world: icon, statement, badges and one inquiry path."""
    slug, name = e(app['slug']), e(app['name'])
    return f'''<section class="product-close wrap" aria-labelledby="product-close-title">
      <div class="product-close-copy"><img class="product-close-icon" src="/assets/{slug}-icon.webp" width="64" height="64" alt="" loading="lazy" decoding="async"><h2 id="product-close-title">Let’s talk about {name}.</h2><p>For product questions, distribution opportunities, or a potential collaboration.</p></div>
      <div class="product-close-actions">{store_badges(app)}<div class="actions">{btn('Ask about ' + app['name'], contact('Product inquiry', app['name']), 'outline')}{btn('All apps', '/apps#' + app['slug'], 'text')}</div></div>
    </section>'''
