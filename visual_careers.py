"""Careers content adapted from the company's published careers page.

The native form hands off to the founder-selected recruiting address via FormSubmit.
The provider, rather than this page, confirms verification and acceptance.
"""
from templating import render
from visual_sections import FOUNDER_PORTRAIT
from ux_components import copy_button
from visual_sections import symbol


CAREER_ROLES = (
    (
        'full-stack-engineer',
        'Full Stack Engineer',
        'Engineering',
        'Interested in the work behind a focused digital product? Show us what '
        'you have built and tell us where you would like to contribute.',
    ),
    (
        'marketing-specialist',
        'Marketing Specialist',
        'Marketing',
        'Help connect products with the people they are built for. Share work '
        'that shows how you approach a message, an audience, or a campaign.',
    ),
)

POSTERS_URL = 'https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws'


def careers_page(btn):
    """Return the /careers content inside the site's shared page shell."""
    # A plain str, like the other page bodies: seo.page_dates prepends a str, which Markup would escape.
    return str(render('visual_careers/page.html.j2', roles=CAREER_ROLES, posters_url=POSTERS_URL,
                      btn=btn, symbol=symbol, copy_button=copy_button, portrait=FOUNDER_PORTRAIT))
