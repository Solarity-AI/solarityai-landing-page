"""Product presentation built around authentic assets, without synthetic app screens."""
from image_provenance import provenance
from company_facts import APP_STORE_RELEASES, COMPANY_FORMS
from templating import render
from visual_record import app_store_since
from visual_stage import product_close


def voice_symbol(size=44):
    """A decorative waveform, deliberately distinct from an official app icon."""
    return str(render('visual_products/voice_symbol.html.j2', size=max(16, int(size))))


def product_art(app, small=False, hero=False):
    """A full, unaltered store image, with an accessible native zoom link."""
    screen = app.get('hero_screen') if hero else None
    screen = screen or app.get('screen')
    if not screen:
        return ''
    alt = app.get('hero_alt') if hero and app.get('hero_alt') else app['name'] + ' official App Store imagery with sample app content'
    sizes = ('(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, (max-width: 1024px) 300px, 440px' if hero else
             '(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, '
             '(max-width: 1024px) 290px, ' + ('320px' if small else '340px'))
    return str(render('visual_products/product_art.html.j2', app=app, hero=hero, image='/assets/' + screen, alt=alt,
                      focus=app.get('crop_focus') if hero else None, width=app.get('screen_width', 600),
                      height=app.get('screen_height', 1298), sizes=sizes, provenance=provenance()))


def product_page(app, apps, btn, contact, stores, status, feature_markup, breadcrumbs, related_markup):
    """Opening: the product's name as title in its world, real imagery staged beside it."""
    from product_story import product_story
    return str(render('visual_products/product_page.html.j2', app=app, breadcrumbs=breadcrumbs,
                      art=product_art(app, hero=True), stores=stores, story=product_story(app),
                      feature_markup=feature_markup, close=product_close(app, btn, contact),
                      related_markup=related_markup, since=app_store_since(app['slug']),
                      since_iso=dict(APP_STORE_RELEASES).get(app['slug'], ''), feedback_url=COMPANY_FORMS['feedback']))
