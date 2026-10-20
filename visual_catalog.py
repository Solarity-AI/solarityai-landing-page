"""Editorial app discovery, with authentic assets and native navigation."""
from image_provenance import provenance
from company_facts import APP_STORE_RELEASES
from templating import render
from visual_record import app_store_since


def _window(app, sizes, low=False):
    return str(render('visual_catalog/window.html.j2', app=app, sizes=sizes, low=low))


def portfolio_wall(apps):
    """Home: all four apps at once, each in its own world, each a single link to its page.
    Each card offers compact text links to both stores; the product pages carry the official badges."""
    cards = [{'app': app,
              'window': _window(app, '(max-width: 560px) 31vw, (max-width: 850px) 39vw, (max-width: 1100px) 22vw, 250px', low=True)}
             for app in apps if app.get('screen') and app.get('apple')]
    return str(render('visual_catalog/portfolio_wall.html.j2', cards=cards, provenance=provenance()))


def portfolio_page(apps, btn, app_art, product_status):
    """Apps: a lineup of the four icons, then one world band per app. The detail pages own the stories."""
    from visual_stage import store_badges
    bands = [{'app': app, 'badges': store_badges(app), 'window': _window(app, '(max-width: 560px) 70vw, 340px'),
              'since': app_store_since(app['slug']), 'since_iso': dict(APP_STORE_RELEASES).get(app['slug'], '')}
             for app in apps]
    return str(render('visual_catalog/portfolio_page.html.j2', bands=bands))
