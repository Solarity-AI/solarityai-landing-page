"""Shared discovery and contact markup. Product facts remain in APPS."""
from templating import render
from visual_products import voice_symbol


def discovery_symbol(app):
    """Use store-sourced icons; any future unlisted direction gets decoration."""
    return render('ux_components/discovery_symbol.html.j2', app=app, voice_symbol=voice_symbol)



def app_breadcrumbs(app):
    return render('ux_components/breadcrumbs.html.j2', app=app)


def related_apps(current, apps):
    return render('ux_components/related_apps.html.j2', current=current, apps=apps,
                  discovery_symbol=discovery_symbol)



def copy_button(address, status_id, label='Copy address', name=''):
    """Copy-to-clipboard button; scripts/copy.js reveals it. name, when given, is what the status announces
    instead of reading the copied text aloud (for long passages)."""
    return render('ux_components/copy_button.html.j2', address=address, status_id=status_id, label=label, name=name)
