"""Shared discovery and contact markup. Product facts remain in APPS."""
from html import escape as e
from visual_products import voice_symbol


def discovery_symbol(app):
    """Use store-sourced icons; any future unlisted direction gets decoration."""
    if app['apple']:
        return f'<span class="discovery-symbol" aria-hidden="true"><img src="/assets/{e(app["slug"])}-icon.webp" alt="" width="48" height="48" loading="lazy"></span>'
    return '<span class="discovery-symbol discovery-concept" aria-hidden="true">'+voice_symbol(48)+'</span>'



def app_breadcrumbs(app):
    return f'<nav class="wrap breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/apps#{e(app["slug"])}">Apps</a></li><li><span aria-current="page">{e(app["name"])}</span></li></ol><span class="breadcrumb-context">{e(app["category"])}</span></nav>'


def related_apps(current, apps):
    links = ''.join(f'<a href="/apps/{e(a["slug"])}" data-product-accent="{e(a["color"])}">{discovery_symbol(a)}<span class="related-identity"><strong>{e(a["name"])}</strong><span class="related-category">{e(a["category"])}</span></span><small class="related-availability">{"iOS&nbsp;&amp;&nbsp;Android" if a["apple"] else "Product vision"}</small><span aria-hidden="true" class="related-arrow">→</span></a>' for a in apps if a['slug'] != current['slug'])
    return '<section class="related-apps wrap" aria-labelledby="related-title"><div class="related-intro"><h2 id="related-title">Another ambition in mind?</h2><p>Explore the other products in the Solarity AI portfolio.</p></div><nav aria-label="Other Solarity AI apps">'+links+'</nav></section>'



def copy_button(address, status_id):
    """Copy-to-clipboard fallback for an email address; scripts/copy.js reveals it."""
    return ('<span class="copy-row"><button type="button" class="copy-button" data-copy="' + e(address, quote=True)
            + '" data-copy-status="' + e(status_id, quote=True) + '" hidden>Copy address</button>'
            + '<span class="copy-status" id="' + e(status_id, quote=True) + '" role="status" aria-live="polite"></span></span>')
