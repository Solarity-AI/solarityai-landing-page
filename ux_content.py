"""Evidence-grounded FAQ and recovery fragments for the corporate site.

Keep these answers aligned with build_site.APPS and CONTENT_REGISTER.md.
These helpers return static HTML and require no JavaScript.
"""
from templating import render


FAQ = [
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


def investor_faq():
    """Answer common investor and partner questions with native disclosures."""
    return render('ux_content/investor_faq.html.j2', questions=FAQ)


def recovery_links():
    """Offer reliable destinations without depending on browser history."""
    return render('ux_content/recovery_links.html.j2')
