"""Evidence-led editorial sections adapted from the reference-site review.

The app lists remain data-driven. The SaaS products are described from their own sites
(saas_products.py): no customer traction, prices or integrations beyond what those sites state.
"""
from urllib.parse import urlencode

from image_provenance import provenance
from saas_products import SAAS
from templating import render
from ux_components import copy_button
from visual_saas import showroom_web
from visual_record import company_line, program_brief, record_summary
from visual_team import TEAM_MEMBERS


def page_index(sections):
    """An "On this page" index for long pages: one in-page link per chapter."""
    return str(render('visual_company_upgrade/page_index.html.j2', sections=sections))


def investor_sections():
    """The Investors page chapters, shared by the opening index and the sticky section index."""
    return ((('brief', 'Brief'),) if program_brief() else ()) + (
        ('portfolio', 'Portfolio'), ('shipping-record', 'Record'), ('at-a-glance', 'At a glance'),
        ('conversation-paths', 'Partnerships'), ('investor-questions', 'Questions'), ('booking', 'Founder'))


def section_index():
    """The same chapters in a bar that stays under the header while reading (wide screens only)."""
    return str(render('visual_company_upgrade/section_index.html.j2', sections=investor_sections()))


def investor_opening(apps, btn, contact):
    """The screening room: the thesis beside its actions, then the four apps framed under one light."""
    framed = [app for app in apps if app.get('apple') and app.get('google') and app.get('screen')]
    return str(render(
        'visual_company_upgrade/investor_opening.html.j2',
        apps=framed,
        investor_button=btn('Investor inquiries', contact('Investor')),
        partner_button=btn('Partnership inquiries', contact('Strategic partner'), 'outline'),
        program_href=contact('Program'),
        index=page_index(investor_sections()),
        copy_link=copy_button('https://solarityai.com/investors-partners/', 'investor-link-status', 'Copy page link', 'The page link'),
        caption=provenance(),
        web_apps=showroom_web(SAAS),
    ))


def strategy_story(btn, contact):
    """Replace the platform-bottom section with a readable strategy sequence."""
    return str(render('visual_company_upgrade/strategy_story.html.j2'))


def investor_evidence(apps):
    """Verified facts first; then what exists today and what lies ahead, in two registers."""
    topics = [
        ('Distribution', 'Discuss an audience, channel, or distribution opportunity for one of the apps.', 'Distribution'),
        ('Technology collaboration', 'Explore a specific integration or product collaboration around shared interests.', 'Technology collaboration'),
        ('SaaS partnership', 'Discuss Engineering Max, Management Max, or Marketing Max for your team or portfolio.', 'SaaS products'),
    ]
    topic_links = [{'title': title, 'detail': detail,
                    'href': '/contact?' + urlencode({'type': 'Strategic partner', 'product': context}) + '#prepare-inquiry'}
                   for title, detail, context in topics]
    listed = [app for app in apps if app.get('apple') and app.get('google')]
    return str(render('visual_company_upgrade/investor_evidence.html.j2',
                      listed=listed, web_app_count=len(SAAS), topics=topic_links, company=company_line(), record=record_summary(),
                      team_size=1 + len(TEAM_MEMBERS)))  # the founder and the approved roster


def founder_booking(btn, booking, email='ata.turhan@solarityai.com'):
    """The close: speak with the founder, beside the one reprise of the approved sunrise."""
    return str(render('visual_company_upgrade/founder_booking.html.j2',
                      booking_button=btn('Book a conversation', booking, 'primary', True),
                      email_button=btn('Email us', 'mailto:' + email, 'outline'),
                      email=email, copy=copy_button(email, 'booking-email-copy-status')))


def operating_principles():
    """Optional replacement for the company feature-grid principles section."""
    return str(render('visual_company_upgrade/operating_principles.html.j2'))
