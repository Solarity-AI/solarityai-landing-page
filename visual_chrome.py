"""Shared navigation, footer, and verified contact method presentation."""

from html import escape

from saas_products import SAAS


def _wordmark():
    # Original-color sun recovered from the official company lockup.
    return ('<a class="wordmark brand-wordmark" href="/" aria-label="Solarity AI home">'
            '<img class="brand-sun" src="/assets/brand/solarity-sun-48.9bc99afc73e8.webp" '
            'srcset="/assets/brand/solarity-sun-48.9bc99afc73e8.webp 48w, /assets/brand/solarity-sun-96.da9c18cba138.webp 96w" '
            'sizes="34px" width="48" height="48" alt="" decoding="async">'
            '<b>SOLARITY <span>AI</span></b></a>')


def site_header(path, nav_items, btn):
    """Keep the existing disclosure-navigation IDs and JS class contracts."""
    descriptions = {'/apps': 'The consumer portfolio', '/platform': 'The app factory: three web apps',
                    '/company': 'Our purpose and founder', '/investors-partners': 'Thesis and collaboration', '/careers': 'Roles and applications'}
    links = []
    for url, label in nav_items:
        current = (' aria-current="page"' if path == url else
                   ' aria-current="location"' if url == '/apps' and path.startswith('/apps/') else '')
        links.append(f'<a href="{escape(url)}"{current}><span class="nav-link-label">{escape(label)}<small class="nav-link-description">{escape(descriptions[url])}</small></span><span class="nav-link-arrow" aria-hidden="true">→</span></a>')
    contact_button = btn('Contact', '/contact', 'small')
    if path == '/contact':
        contact_button = contact_button.replace(' href=', ' aria-current="page" href=', 1)
    return (
        '<header class="site-header chrome-header"><div class="header-inner wrap">'
        + _wordmark()
        + '<button class="menu-toggle" type="button" aria-controls="site-nav" '
          'aria-expanded="false" aria-label="Open navigation">'
          '<span class="sr-only">Menu</span><span class="menu-lines" aria-hidden="true"></span>'
          '</button>'
        + '<nav id="site-nav" aria-label="Primary navigation">' + ''.join(links) + '</nav>'
        + '<div class="header-actions">' + contact_button + '</div></div></header>'
    )


def site_footer(email, path='/', booking=''):
    """Footer directory: the whole portfolio (mobile and web apps), the company routes and direct contact."""
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
    directory = []
    for heading, links in groups:
        directory.append('<div class="footer-group"><h2>' + escape(heading) + '</h2><ul>')
        for href, label in links:
            leaves = href.startswith(('mailto:', 'https:'))
            arrow = '<span aria-hidden="true">↗</span>' if leaves else ''
            new_tab = ' target="_blank" rel="noopener noreferrer"' if href.startswith('https:') else ''
            note = '<span class="sr-only"> (opens in a new tab)</span>' if new_tab else ''
            current = ' aria-current="page"' if href == path else ''
            directory.append(f'<li><a href="{escape(href)}"{current}{new_tab}>{escape(label)}{arrow}{note}</a></li>')
        directory.append('</ul></div>')
    return (
        '<footer class="site-footer chrome-footer"><div class="wrap">'
        '<nav class="footer-directory" aria-label="Footer navigation">' + ''.join(directory) + '</nav>'
          '<div class="footer-signature" aria-hidden="true"><img class="footer-sun" src="/assets/brand/solarity-sun-320.2513ba060440.webp" '
          'srcset="/assets/brand/solarity-sun-192.91c59bec3b73.webp 192w, /assets/brand/solarity-sun-320.2513ba060440.webp 320w" '
          'sizes="(max-width: 560px) 56px, 13cqi" width="320" height="320" alt="" loading="lazy" decoding="async">'
          '<span class="footer-signature-word">SOLARITY<span>AI</span></span></div>'
          '<div class="footer-legal"><p>© 2026 Solarity AI LLC · Irving, Texas, United States · '
          '<a href="/contact#data-note">About this contact experience</a></p>'
          '<p>App Store is a trademark of Apple Inc. Google Play is a trademark of Google LLC.</p></div></div></footer>'
    )


