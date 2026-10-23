"""Plain statements about the website itself: its accessibility and how it handles data."""
from templating import render


def accessibility_page(email):
    return str(render('visual_policies/accessibility.html.j2', email=email))


def privacy_page(email):
    return str(render('visual_policies/privacy.html.j2', email=email, effective='October 23, 2026', effective_iso='2026-10-23'))


def website_data_page(email, apps=()):
    return str(render('visual_policies/website_data.html.j2', email=email,
                      apps=[a for a in apps if a.get('apple')]))
