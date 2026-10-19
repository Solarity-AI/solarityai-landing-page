"""Direct, verified contact paths with lightweight inquiry context enhancement."""
from html import escape
from urllib.parse import quote, urlencode

from ux_components import copy_button
from visual_sections import symbol

TOPIC_ICONS = {'Investor': 'invest', 'Strategic partner': 'partner', 'Product inquiry': 'apps', 'Other': 'message'}


CONTACT_TOPICS = (
    ('Investor', 'Investment conversations', 'The portfolio, company strategy, and future priorities.'),
    ('Strategic partner', 'Strategic partnerships', 'Distribution, technology, and the web apps for your team.'),
    ('Product inquiry', 'Product questions', 'The four mobile apps, or Engineering Max, Management Max, and Marketing Max.'),
    ('Other', 'Something else in mind?', 'A clear introduction is a good place to start.'),
)


def contact_page(email, booking, btn):
    """All destinations work without JavaScript. Context enhances the email subject."""
    topics = []
    for kind, title, description in CONTACT_TOPICS:
        href = 'mailto:' + email + '?' + urlencode({'subject': 'Solarity AI | ' + kind}, quote_via=quote)
        topics.append(
            '<a class="contact-topic" data-inquiry-type="' + escape(kind, quote=True)
            + '" href="' + escape(href, quote=True) + '"><span class="contact-topic-icon">' + symbol(TOPIC_ICONS[kind]) + '</span><span><strong>'
            + escape(title) + '</strong><span>' + escape(description)
            + '</span></span><span class="contact-topic-arrow" aria-hidden="true">↗</span></a>'
        )
    return '''<section class="contact-opening wrap" aria-labelledby="contact-title">

<h1 id="contact-title">A shared ambition.<br>A <em>real conversation.</em></h1>
<p class="lede">Explore the products, discuss a partnership, or speak with the founder about the company’s direction.</p>
</section>
<section class="contact-destination wrap" id="prepare-inquiry" aria-labelledby="contact-person-title" tabindex="-1">
<div class="contact-direct"><p id="contact-context" class="contact-context">Start with an introduction.</p><a id="contact-email" class="contact-email" href="mailto:''' + escape(email) + '''?subject=Solarity%20AI%20%7C%20Other"><span>''' + escape(email) + '''</span><span aria-hidden="true">↗</span></a>''' + copy_button(email, 'contact-email-copy-status') + '''<p class="contact-direct-help">Write directly to Ata in your email app. A little context and the next step you have in mind are enough.</p><div class="contact-booking">''' + btn('Book a conversation', booking, 'outline', True) + '''<span>Choose a time on Google Calendar.</span></div></div>
<div class="contact-person"><p class="eyebrow">Your point of contact</p><h2 id="contact-person-title">Ata Turhan</h2><p class="contact-person-role">Founder, Solarity AI</p><p>Irving, Texas, United States</p><a class="text-link" href="/company">Meet the company <span aria-hidden="true">→</span></a></div>
</section>
<section class="contact-topics wrap" aria-labelledby="contact-topics-title"><div class="contact-topics-heading"><h2 id="contact-topics-title">What would you like to explore?</h2><p>Choose a topic to open an email with the subject ready.</p></div><div class="contact-topic-list">''' + ''.join(topics) + '''</div></section>
<div class="contact-data-note wrap" id="data-note"><h2>About this contact experience</h2><p>Email links open your email app. You review and send the message there. This website does not collect or submit contact messages. Booking opens Google Calendar.</p><p>For job opportunities, visit <a href="/careers">careers</a> or email <a href="mailto:careers@solarityai.com">careers@solarityai.com</a>.</p></div>'''
