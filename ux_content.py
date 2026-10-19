"""Evidence-grounded FAQ and recovery fragments for the corporate site.

Keep these answers aligned with build_site.APPS and CONTENT_REGISTER.md.
These helpers return static HTML and require no JavaScript.
"""


def investor_faq():
    """Answer common investor and partner questions with native disclosures."""
    questions = [
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
            "Is the app factory available to external teams?",
            '<p>Engineering Max, Management Max, and Marketing Max represent '
            'our platform vision. Specific capabilities, integrations, and '
            'external commercial availability are topics for discussion with '
            'prospective partners.</p>'
            '<p><a href="/platform">Explore the three platform focus areas</a> '
            'or <a href="/contact?type=Strategic+partner&amp;product=Platform+design+partnership#prepare-inquiry">'
            'discuss a platform design partnership</a>.</p>',
        ),
        (
            "What is the business model direction?",
            '<p>The consumer product direction includes subscriptions and '
            'in-app purchases. Looks Max, IQ Max, Sleep Max, and Fitness Max have store '
            'listings with in-app purchases; consult each listing for current '
            'plans and terms.</p>'
            '<p>Potential commercialization of the app factory is part of the '
            'company strategy. The platform is presented here as a vision, '
            'with commercial scope to be discussed.</p>',
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
    disclosures = "".join(
        '<details class="faq-item"><summary><span class="faq-question">'
        + question
        + '</span><span class="faq-marker" aria-hidden="true">+</span></summary>'
        + '<div class="faq-answer">'
        + answer
        + '</div></details>'
        for number, (question, answer) in enumerate(questions, 1)
    )
    return (
        '<section class="investor-faq section wrap" id="investor-questions" '
        'aria-labelledby="investor-questions-title">'
        '<div class="section-heading"><div>'
        '<h2 id="investor-questions-title">A few useful&nbsp;answers.</h2></div>'
        '<p class="section-lede">A clear starting point for exploring the '
        'products, the platform, and a potential collaboration.</p></div>'
        '<div class="faq-list">'
        + disclosures
        + '</div></section>'
    )


def recovery_links():
    """Offer reliable destinations without depending on browser history."""
    return (
        '<nav class="recovery-nav" aria-label="More ways to continue">'
        '<a href="/platform">'
        '<span class="recovery-destination"><strong>Explore the platform</strong>'
        '<span>Engineering, management, and marketing.</span></span>'
        '<span class="recovery-arrow" aria-hidden="true">→</span></a>'
        '<a href="/investors-partners">'
        '<span class="recovery-destination"><strong>Investors &amp; partners</strong>'
        '<span>The company thesis and collaboration paths.</span></span>'
        '<span class="recovery-arrow" aria-hidden="true">→</span></a>'
        '<a href="/contact">'
        '<span class="recovery-destination"><strong>Contact Solarity AI</strong>'
        '<span>Reach the founder about your question.</span></span>'
        '<span class="recovery-arrow" aria-hidden="true">→</span></a>'
        '</nav>'
    )


def recovery_art():
    """A decorative, code-native orbital motif for the error page only."""
    return ('<div class="recovery-art" aria-hidden="true">'
            '<svg viewBox="0 0 360 300" fill="none" focusable="false">'
            '<circle cx="180" cy="150" r="110" stroke="currentColor" opacity=".35"/>'
            '<circle cx="180" cy="150" r="83" stroke="currentColor" opacity=".16"/>'
            '<ellipse cx="180" cy="150" rx="160" ry="42" transform="rotate(-28 180 150)" stroke="currentColor" opacity=".55"/>'
            '<circle cx="302" cy="83" r="6" fill="currentColor"/>'
            '<text x="180" y="170" text-anchor="middle" fill="currentColor" font-family="Arial,sans-serif" font-size="60" letter-spacing="-3">404</text>'
            '</svg></div>')
