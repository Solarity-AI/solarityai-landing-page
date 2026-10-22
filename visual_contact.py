"""Direct, verified contact paths with lightweight inquiry context enhancement."""
from urllib.parse import quote, urlencode

from company_facts import COMPANY_FORMS, COMPANY_PROFILES, FOUNDER
from templating import render
from ux_components import copy_button
from visual_sections import symbol

TOPIC_ICONS = {'Investor': 'invest', 'Program': 'spark', 'Strategic partner': 'partner', 'Product inquiry': 'apps', 'Press': 'share', 'Other': 'message'}


CONTACT_TOPICS = (
    ('Investor', 'Investment conversations', 'The portfolio, company strategy, and future priorities.'),
    ('Program', 'Accelerators, incubators, and grants', 'Application reviews, program questions, and introductions.'),
    ('Strategic partner', 'Strategic partnerships', 'Distribution, technology, and the SaaS products for your team.'),
    ('Product inquiry', 'Product questions', 'The 4 mobile apps, or Engineering Max, Management Max, and Marketing Max.'),
    ('Press', 'Press and media', 'Articles, program pages, and event listings. The press kit has approved descriptions and images.'),
    ('Other', 'Something else in mind?', 'A clear introduction is a good place to start.'),
)


# The Linktree's Google Forms, described as each form describes itself.
CONTACT_FORMS = (
    ('feedback', 'message', 'Product feedback', 'Share your thoughts on the apps and SaaS products.'),
    ('mentorship', 'spark', 'Mentorship program', 'A pilot program mentoring university students.'),
    ('certificate', 'calendar', 'Certificate of participation', 'Attended a Solarity AI event? Request your certificate.'),
)


VCARD_PATH = '/assets/contact/ata-turhan.vcf'


def founder_vcard(email):
    """vCard 3.0 for the founder, from facts the Contact page states (RFC 2426 asks for CRLF line ends)."""
    lines = ['BEGIN:VCARD', 'VERSION:3.0', 'N:Turhan;Ata;;;', 'FN:Ata Turhan', 'ORG:Solarity AI LLC', 'TITLE:Founder',
             'EMAIL;TYPE=INTERNET,WORK:' + email, 'URL:https://solarityai.com/',
             *(['X-SOCIALPROFILE;TYPE=linkedin:' + FOUNDER['linkedin']] if FOUNDER.get('linkedin') else []),
             'ADR;TYPE=WORK:;;;Dallas;Texas;;United States', 'END:VCARD']
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
    return str(render('visual_contact/page.html.j2', vcard=VCARD_PATH, linkedin=FOUNDER.get('linkedin', ''), email=email, booking=booking, topics=topics,
                      forms=[{'href': COMPANY_FORMS[key], 'icon': icon, 'title': title, 'description': description}
                             for key, icon, title, description in CONTACT_FORMS],
                      profiles=COMPANY_PROFILES, btn=btn, symbol=symbol, copy_button=copy_button))
