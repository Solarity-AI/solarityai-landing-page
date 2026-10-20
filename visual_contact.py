"""Direct, verified contact paths with lightweight inquiry context enhancement."""
from urllib.parse import quote, urlencode

from templating import render
from ux_components import copy_button
from visual_sections import symbol

TOPIC_ICONS = {'Investor': 'invest', 'Program': 'spark', 'Strategic partner': 'partner', 'Product inquiry': 'apps', 'Press': 'share', 'Other': 'message'}


CONTACT_TOPICS = (
    ('Investor', 'Investment conversations', 'The portfolio, company strategy, and future priorities.'),
    ('Program', 'Accelerators, incubators, and grants', 'Application reviews, program questions, and introductions.'),
    ('Strategic partner', 'Strategic partnerships', 'Distribution, technology, and the web apps for your team.'),
    ('Product inquiry', 'Product questions', 'The four mobile apps, or Engineering Max, Management Max, and Marketing Max.'),
    ('Press', 'Press and media', 'Articles, program pages, and event listings. The press kit has approved descriptions and images.'),
    ('Other', 'Something else in mind?', 'A clear introduction is a good place to start.'),
)


VCARD_PATH = '/assets/contact/ata-turhan.vcf'


def founder_vcard(email):
    """vCard 3.0 for the founder, from facts the Contact page states (RFC 2426 asks for CRLF line ends)."""
    lines = ['BEGIN:VCARD', 'VERSION:3.0', 'N:Turhan;Ata;;;', 'FN:Ata Turhan', 'ORG:Solarity AI LLC', 'TITLE:Founder',
             'EMAIL;TYPE=INTERNET,WORK:' + email, 'URL:https://solarityai.com/',
             'ADR;TYPE=WORK:;;;Irving;Texas;;United States', 'END:VCARD']
    return '\r\n'.join(lines) + '\r\n'


def contact_page(email, booking, btn):
    """All destinations work without JavaScript. Context enhances the email subject."""
    topics = [
        {
            'kind': kind,
            'href': 'mailto:' + email + '?' + urlencode({'subject': 'Solarity AI | ' + kind}, quote_via=quote),
            'icon': TOPIC_ICONS[kind],
            'title': title,
            'description': description,
        }
        for kind, title, description in CONTACT_TOPICS
    ]
    # A plain str, like the other page bodies: seo.page_dates prepends a str, which Markup would escape.
    return str(render('visual_contact/page.html.j2', vcard=VCARD_PATH, email=email, booking=booking, topics=topics,
                      btn=btn, symbol=symbol, copy_button=copy_button))
