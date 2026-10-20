"""Shared navigation, footer, and verified contact method presentation."""

from saas_products import SAAS
from templating import render
from visual_record import company_line


def site_header(path, nav_items, btn):
    """Keep the existing disclosure-navigation IDs and JS class contracts."""
    descriptions = {'/apps': 'The consumer portfolio', '/platform': 'The app factory: three web apps',
                    '/company': 'Our purpose and founder', '/investors-partners': 'Thesis and collaboration', '/careers': 'Roles and applications'}
    links = []
    for url, label in nav_items:
        current = ('page' if path == url else
                   'location' if url == '/apps' and path.startswith('/apps/') else None)
        links.append({'url': url, 'label': label, 'description': descriptions[url], 'current': current})
    # str(): Markup.replace would escape the inserted attribute if btn ever returns Markup.
    contact_button = str(btn('Contact', '/contact', 'small'))
    if path == '/contact':
        contact_button = contact_button.replace(' href=', ' aria-current="page" href=', 1)
    return str(render('visual_chrome/site_header.html.j2', links=links, contact_button=contact_button))


def site_footer(email, path='/', booking=''):
    """Footer directory: the whole portfolio (mobile and web apps), the company routes and direct contact.
    Links that leave the Site (mailto:, https:) carry ↗; https: links also open in a new tab."""
    groups = [
        ('Mobile apps', [('/apps/looks-max', 'Looks Max'), ('/apps/iq-max', 'IQ Max'),
                         ('/apps/sleep-max', 'Sleep Max'), ('/apps/fitness-max', 'Fitness Max')]),
        ('Web apps', [('/platform#' + p['slug'], p['name']) for p in SAAS]),
        ('Company', [('/apps', 'Apps'), ('/platform', 'Platform'),
                     ('/company', 'Company'), ('/investors-partners', 'Investors & partners'), ('/careers', 'Careers')]),
        ('Contact', [('/contact?type=Investor#prepare-inquiry', 'Investor inquiries'),
                     ('/contact?type=Strategic+partner#prepare-inquiry', 'Partnership inquiries'),
                     ('mailto:' + email, 'Email Ata')] + ([(booking, 'Book a conversation')] if booking else [])),
    ]
    return str(render('visual_chrome/site_footer.html.j2', groups=groups, path=path, company=company_line()))
