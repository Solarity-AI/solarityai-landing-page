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
        '<p>Solarity AI LLC, based in Dallas, Texas, builds AI self-improvement apps for iOS and Android: '
        '<a href="/apps/looks-max">Looks Max</a>, <a href="/apps/iq-max">IQ Max</a>, <a href="/apps/sleep-max">Sleep Max</a>, '
        'and <a href="/apps/fitness-max">Fitness Max</a>. Building them shaped 3 SaaS products for teams that build mobile '
        'apps: <a href="/platform">Engineering Max, Management Max, and Marketing Max</a>.</p>',
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
        f'<p>{_RECORD["count"]} apps launched on the App Store in {_RECORD["weeks"]} weeks: '
        + ', '.join(_LAUNCHES[:-1]) + ', and ' + _LAUNCHES[-1] + '. Each is also on Google Play. '
        '<a href="/investors-partners#shipping-record">See the shipping record</a>.</p>',
    ),
    (
        "Who builds Solarity AI?",
        '<p>Founder Ata Turhan leads Solarity AI from Dallas, Texas, with '
        + ', '.join(_TEAM[:-1]) + ', and ' + _TEAM[-1] + '. '
        '<a href="/company#team">Meet the team</a>.</p>',
    ),
    (
        "Can other teams use the SaaS products?",
        '<p>Yes. All 3 are in early access. <a href="/platform#management-max">Management Max</a> '
        'has a free plan for 1 app; <a href="/platform#engineering-max">Engineering Max</a> and '
        '<a href="/platform#marketing-max">Marketing Max</a> take requests on their own sites. '
        'Mobile versions of all 3 are planned.</p>'
        '<p><a href="/platform">Explore the app factory</a> '
        'or <a href="/contact?type=Strategic+partner&amp;product=SaaS+products#prepare-inquiry">'
        'discuss the SaaS products for your team</a>.</p>',
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
        'technology collaboration, and SaaS partnerships around Engineering Max, '
        'Management Max, or Marketing Max. '
        'A useful introduction describes your audience or team, the '
        'product or workflow involved, and the collaboration you have in mind.</p>'
        '<p><a href="/contact?type=Strategic+partner#prepare-inquiry">Start a partnership inquiry</a>.</p>',
    ),
    (
        "How do I start a conversation?",
        '<p>Choose an <a href="/contact?type=Investor#prepare-inquiry">investor inquiry</a>, '
        'a <a href="/contact?type=Strategic+partner#prepare-inquiry">partnership inquiry</a>, '
        'or, when you are reviewing an application, a '
        '<a href="/contact?type=Program#prepare-inquiry">program inquiry</a>. '
        'The contact page opens your email app with the relevant subject, '
        'so you can write directly to the founder.</p>'
        '<p>You can also email '
        '<a href="mailto:ata.turhan@solarityai.com">ata.turhan@solarityai.com</a> '
        'directly or use the founder’s booking link on the '
        '<a href="/contact">contact page</a>.</p>',
    ),
]


# Answers whose question was reworded keep their earlier fragment, so links already shared still open them.
LEGACY_ANSWER_IDS = {'faq-can-other-teams-use-the-saas-products': 'faq-can-other-teams-use-the-web-apps'}


def answer_id(question):
    """A stable fragment for an answer, from its question: "What is Solarity AI?" is #faq-what-is-solarity-ai."""
    words = re.sub(r'<[^>]+>', '', question).lower()
    return 'faq-' + re.sub(r'[^a-z0-9]+', '-', words).strip('-')


def investor_faq():
    """Answer common investor and partner questions with native disclosures, each one linkable."""
    return render('ux_content/investor_faq.html.j2', questions=[(answer_id(q), q, a) for q, a in FAQ], legacy=LEGACY_ANSWER_IDS)


def recovery_links():
    """Offer reliable destinations without depending on browser history."""
    return render('ux_content/recovery_links.html.j2')
