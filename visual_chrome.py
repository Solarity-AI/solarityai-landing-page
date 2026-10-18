"""Shared navigation, footer, and verified contact method presentation."""

from html import escape


def _wordmark():
    # Original-color sun recovered from the official company lockup.
    return ('<a class="wordmark brand-wordmark" href="/" aria-label="Solarity AI home">'
            '<img class="brand-sun" src="/assets/brand/solarity-sun-48.9bc99afc73e8.webp" '
            'srcset="/assets/brand/solarity-sun-48.9bc99afc73e8.webp 48w, /assets/brand/solarity-sun-96.da9c18cba138.webp 96w" '
            'sizes="34px" width="48" height="48" alt="" decoding="async">'
            '<b>SOLARITY <span>AI</span></b></a>')


def site_header(path, nav_items, btn):
    """Keep the existing disclosure-navigation IDs and JS class contracts."""
    descriptions = {'/apps': 'The consumer portfolio', '/platform': 'The app factory vision',
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


def site_footer(email, path='/'):
    """Footer directory with complete core-app routes and approved company context."""
    groups = [
        ('The portfolio', [('/apps/looks-max', 'Looks Max'), ('/apps/iq-max', 'IQ Max'),
                           ('/apps/sleep-max', 'Sleep Max'), ('/apps/fitness-max', 'Fitness Max')]),
        ('The company', [('/apps', 'App portfolio'), ('/platform', 'App factory vision'),
                         ('/company', 'About Solarity AI'), ('/investors-partners', 'Investors & partners'), ('/careers', 'Careers')]),
        ('Start a conversation', [('/contact?type=Investor#prepare-inquiry', 'Investor inquiries'),
                                  ('/contact?type=Strategic+partner#prepare-inquiry', 'Partnership inquiries'),
                                  ('/contact', 'Contact'), ('mailto:' + email, 'Email Ata')]),
    ]
    directory = []
    for heading, links in groups:
        directory.append('<div class="footer-group"><h2>' + escape(heading) + '</h2><ul>')
        for href, label in links:
            arrow = '<span aria-hidden="true">↗</span>' if href.startswith('mailto:') else ''
            current = ' aria-current="page"' if href == path else ''
            directory.append(f'<li><a href="{escape(href)}"{current}>{escape(label)}{arrow}</a></li>')
        directory.append('</ul></div>')
    return (
        '<footer class="site-footer chrome-footer"><div class="wrap">'
        '<div class="footer-introduction"><div><p>Human potential.<br>Thoughtfully built.</p></div>'
          '<p class="footer-positioning">Focused consumer apps.<br>Systems for what comes next.</p></div>'
          '<nav class="footer-directory" aria-label="Footer navigation">' + ''.join(directory) + '</nav>'
          '<div class="footer-signature" aria-hidden="true">SOLARITY<span>AI</span></div>'
          '<div class="footer-legal"><span>© 2026 Solarity AI LLC</span>'
          '<span>Irving, Texas, United States</span>'
          '<a href="/contact#data-note">About this contact experience</a></div></div></footer>'
    )


def _method_icon(kind):
    paths = ('<rect x="3" y="5" width="18" height="14" rx="2"/>'
             '<path d="m4 7 8 6 8-6"/>') if kind == 'email' else (
             '<rect x="3" y="5" width="18" height="16" rx="2"/>'
             '<path d="M7 3v4m10-4v4M3 11h18m-14 4h3m4 0h3"/>')
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + paths + '</svg>'


def contact_methods(email, booking):
    """Direct verified destinations, without implying message delivery or a response SLA."""
    return (
        '<div class="contact-methods" aria-label="Direct contact options">'
        '<a class="contact-method" href="mailto:' + escape(email) + '">'
        '<span class="method-icon">' + _method_icon('email') + '</span>'
        '<span class="method-copy"><strong>Email Ata</strong><span>' + escape(email) + '</span></span>'
        '<span class="method-arrow" aria-hidden="true">↗</span></a>'
        '<a class="contact-method" href="' + escape(booking) + '" target="_blank" rel="noopener noreferrer">'
        '<span class="method-icon">' + _method_icon('calendar') + '</span>'
        '<span class="method-copy"><strong>Book a conversation</strong><span>Choose a time on Google Calendar</span></span>'
        '<span class="method-arrow" aria-hidden="true">↗</span></a></div>'
    )
