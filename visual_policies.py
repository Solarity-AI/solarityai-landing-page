"""Plain statements about the website itself: its accessibility and how it handles data."""
from templating import render


def accessibility_page(email):
    return str(render('visual_policies/accessibility.html.j2', email=email))


def website_data_page(email):
    return str(render('visual_policies/website_data.html.j2', email=email))
