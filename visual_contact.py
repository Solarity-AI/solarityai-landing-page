"""Direct, verified contact paths with lightweight inquiry context enhancement."""
from urllib.parse import quote, urlencode

from templating import render
from ux_components import copy_button
from visual_sections import symbol

TOPIC_ICONS = {'Investor': 'invest', 'Program': 'spark', 'Strategic partner': 'partner', 'Product inquiry': 'apps', 'Other': 'message'}


CONTACT_TOPICS = (
    ('Investor', 'Investment conversations', 'The portfolio, company strategy, and future priorities.'),
    ('Program', 'Accelerators, incubators, and grants', 'Application reviews, program questions, and introductions.'),
    ('Strategic partner', 'Strategic partnerships', 'Distribution, technology, and the web apps for your team.'),
    ('Product inquiry', 'Product questions', 'The four mobile apps, or Engineering Max, Management Max, and Marketing Max.'),
    ('Other', 'Something else in mind?', 'A clear introduction is a good place to start.'),
)


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
    return str(render('visual_contact/page.html.j2', email=email, booking=booking, topics=topics,
                      btn=btn, symbol=symbol, copy_button=copy_button))
