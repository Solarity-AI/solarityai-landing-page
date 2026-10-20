"""Evidence-grounded FAQ and recovery fragments for the corporate site.

Keep these answers aligned with build_site.APPS and CONTENT_REGISTER.md.
These helpers return static HTML and require no JavaScript.
"""
import re

from company_facts import APP_STORE_RELEASES
from templating import render
from visual_record import long_date, record_summary
from visual_team import TEAM_MEMBERS

_NAMES = {'looks-max': 'Looks Max', 'fitness-max': 'Fitness Max (listed as Only Fitness)', 'iq-max': 'IQ Max', 'sleep-max': 'Sleep Max'}
_RECORD = record_summary()
_LAUNCHES = [f'{_NAMES[slug]} on {long_date(iso)}' for slug, iso in APP_STORE_RELEASES]
_TEAM = [f'<span lang="tr">{member["name"]}</span>' for member in TEAM_MEMBERS]


FAQ = [
    (
        "What is Solarity AI?",
        '<p>Solarity AI LLC, based in Irving, Texas, builds AI self-improvement apps for iOS and Android: '
        '<a href="/apps/looks-max">Looks Max</a>, <a href="/apps/iq-max">IQ Max</a>, <a href="/apps/sleep-max">Sleep Max</a>, '
        'and <a href="/apps/fitness-max">Fitness Max</a>. Building them shaped three web apps for teams that build mobile '
        'products: <a href="/platform">Engineering Max, Management Max, and Marketing Max</a>. Ata Turhan is the founder.</p>',
    ),
    (
        "Which products can I explore today?",
        '<p><a href="/apps/looks-max">Looks Max</a>, '
        '<a href="/apps/iq-max">IQ Max</a>, '
        '<a href="/apps/sleep-max">Sleep Max</a>, and '
        '<a href="/apps/fitness-max">Fitness Max</a> have live App Store and '
        'Google Play listings. Fitness Max is listed in app stores as Only Fitness. '
        'Their product pages link to the stores for current offers and '
        'availability in your region.</p>',
    ),
    (
        "How quickly has Solarity AI shipped?",
        f'<p>{_RECORD["count_word"].capitalize()} apps launched on the App Store in {_RECORD["weeks_word"]} weeks: '
        + ', '.join(_LAUNCHES[:-1]) + ', and ' + _LAUNCHES[-1] + '. Each is also on Google Play. '
        '<a href="/investors-partners#shipping-record">See the shipping record</a>.</p>',
    ),
    (
        "Who builds Solarity AI?",
        '<p>Founder Ata Turhan leads Solarity AI from Irving, Texas, with '
        + ', '.join(_TEAM[:-1]) + ', and ' + _TEAM[-1] + '. '
        '<a href="/company#team">Meet the team</a>.</p>',
    ),
    (
        "Can other teams use the web apps?",
        '<p>Yes, at different stages. <a href="/platform#management-max">Management Max</a> '
        'is open with a free plan for one app. <a href="/platform#engineering-max">Engineering Max</a> '
        'is in private testing and <a href="/platform#marketing-max">Marketing Max</a> is in early access; '
        'both take requests on their own sites. Mobile versions of all three are planned.</p>'
        '<p><a href="/platform">Explore the app factory</a> '
        'or <a href="/contact?type=Strategic+partner&amp;product=Web+apps#prepare-inquiry">'
        'discuss the web apps for your team</a>.</p>',
    ),
    (
        "What is the business model direction?",
        '<p>The consumer apps use subscriptions and in-app purchases. Looks Max, IQ Max, '
        'Sleep Max, and Fitness Max have store listings with in-app purchases; consult each '
        'listing for current plans and terms.</p>'
        '<p>Management Max offers a free plan and paid plans that count apps, not seats. '
        'Engineering Max and Marketing Max have no price yet.</p>',
    ),
    (
        "What kinds of partnerships are relevant?",
        '<p>We welcome conversations about product distribution, '
        'technology collaboration, and platform design partnerships. '
        'A useful introduction describes your audience or team, the '
        'product or workflow involved, and the collaboration you have in mind.</p>'
        '<p><a href="/contact?type=Strategic+partner#prepare-inquiry">Start a partnership inquiry</a>.</p>',
    ),
    (
        "How do I start a conversation?",
        '<p>Choose an <a href="/contact?type=Investor#prepare-inquiry">investor inquiry</a> '
        'or <a href="/contact?type=Strategic+partner#prepare-inquiry">partnership inquiry</a>. '
        'The contact page opens your email app with the relevant subject, '
        'so you can write directly to the founder.</p>'
        '<p>You can also email '
        '<a href="mailto:ata.turhan@solarityai.com">ata.turhan@solarityai.com</a> '
        'directly or use the founder’s booking link on the '
        '<a href="/contact">contact page</a>.</p>',
    ),
]


def answer_id(question):
    """A stable fragment for an answer, from its question: "What is Solarity AI?" is #faq-what-is-solarity-ai."""
    words = re.sub(r'<[^>]+>', '', question).lower()
    return 'faq-' + re.sub(r'[^a-z0-9]+', '-', words).strip('-')


def investor_faq():
    """Answer common investor and partner questions with native disclosures, each one linkable."""
    return render('ux_content/investor_faq.html.j2', questions=[(answer_id(q), q, a) for q, a in FAQ])


def recovery_links():
    """Offer reliable destinations without depending on browser history."""
    return render('ux_content/recovery_links.html.j2')
