"""Evidence-led editorial sections adapted from the reference-site review.

The app lists remain data-driven. The web apps are described from their own sites
(saas_products.py): no customer traction, prices or integrations beyond what those sites state.
"""
from html import escape
from urllib.parse import urlencode

from image_provenance import provenance
from saas_products import SAAS
from visual_saas import showroom_web


def page_index(sections):
    """An "On this page" index for long pages: one in-page link per chapter."""
    links = ''.join('<li><a href="#' + escape(anchor, quote=True) + '">' + escape(label)
                    + ' <span aria-hidden="true">↓</span></a></li>' for anchor, label in sections)
    return ('<nav class="page-index" aria-labelledby="page-index-title">'
            '<p class="page-index-title" id="page-index-title">On this page</p><ul>' + links + '</ul></nav>')


def investor_opening(apps, btn, contact):
    """The screening room: the thesis beside its actions, then the four apps framed under one light."""
    note = '<span class="sr-only"> (opens in a new tab)</span>'
    frames = []
    for app in apps:
        if not app.get('apple') or not app.get('google') or not app.get('screen'):
            continue
        slug = escape(app['slug'], quote=True)
        focus = (' style="object-position:' + escape(app['crop_focus'], quote=True) + '"') if app.get('crop_focus') else ''
        frames.append(
            '<li class="showroom-frame" data-product-accent="' + escape(app['color'], quote=True) + '">'
            '<a class="showroom-link" href="/apps/' + slug + '"><span class="showroom-window screenshot-stage">'
            '<img class="store-screen plate--window"' + focus + ' src="/assets/' + escape(app['screen'], quote=True)
            + '" alt="' + escape(app['name']) + ' official App Store imagery with sample app content" width="'
            + str(app.get('screen_width', 600)) + '" height="' + str(app.get('screen_height', 1298))
            + '" sizes="(max-width: 560px) 47vw, (max-width: 1100px) 18vw, 180px"' + (' fetchpriority="high"' if not frames else '') + ' decoding="async"></span>'
            '<span class="showroom-identity"><img src="/assets/' + slug + '-icon.webp" width="40" height="40" alt="" loading="lazy" decoding="async">'
            '<span><strong>' + escape(app['name']) + '</strong><small>' + escape(app['category']) + '</small></span></span></a>'
            '<p class="showroom-stores"><a href="' + escape(app['apple'], quote=True) + '" target="_blank" rel="noopener noreferrer">App Store <span aria-hidden="true">↗</span>' + note + '</a>'
            '<a href="' + escape(app['google'], quote=True) + '" target="_blank" rel="noopener noreferrer">Google Play <span aria-hidden="true">↗</span>' + note + '</a></p></li>'
        )
    return (
        '<section class="investor-opening wrap" aria-labelledby="investor-opening-title">'
        '<div class="investor-opening-copy"><p class="eyebrow">Investors &amp; partners</p>'
        '<h1 id="investor-opening-title">Products today.<br><span>Possibility ahead.</span></h1>'
        '<div class="investor-opening-aside"><p class="lede">Four consumer apps, and three web apps for the work behind them. '
        'Explore the products, then the company direction.</p>'
        '<div class="actions">' + btn('Investor inquiries', contact('Investor'))
        + btn('Partnership inquiries', contact('Strategic partner'), 'outline')
        + '</div>' + page_index((('portfolio', 'Portfolio'), ('at-a-glance', 'At a glance'),
                                 ('conversation-paths', 'Partnerships'),
                                 ('investor-questions', 'Questions'),
                                 ('booking', 'Founder'))) + '</div></div>'
        '<div class="showroom" id="portfolio"><ul class="showroom-frames" tabindex="0" aria-label="Consumer portfolio: '
        + str(len(frames)) + ' store-listed apps">' + ''.join(frames) + '</ul>'
        '<p class="caption showroom-caption">' + provenance() + '</p>' + showroom_web(SAAS) + '</div></section>'
    )


def strategy_story(btn, contact):
    """Replace the platform-bottom section with a readable strategy sequence."""
    return '''<section class="strategy-story wrap" aria-labelledby="strategy-story-title">
<div class="strategy-story-intro">
<h2 id="strategy-story-title">The products ground the possibility.</h2>
<p>Focused apps give the company a practical context for exploring better ways to build, operate, and grow mobile products.</p>
<a class="text-link" href="/apps">Meet the consumer portfolio <span aria-hidden="true">→</span></a></div>
<ol class="strategy-story-steps">
<li><div><h3>Start with a specific human need.</h3><p>Self-care, cognitive practice, sleep, and fitness each call for a focused experience. Product choices start with that distinct purpose.</p></div></li>
<li><div><h3>Learn from the work behind it.</h3><p>Requirements, priorities, releases, and product storytelling are part of bringing an app to people. These disciplines inform the app factory direction.</p></div></li>
<li><div><h3>Develop patterns worth reusing.</h3><p>The ambition is to carry useful workflows into future products while preserving the judgment each one needs.</p></div></li>
</ol>
<div class="strategy-story-bottom"><p><strong>People remain responsible for the decisions.</strong><span>Architecture, product priorities, and releases need deliberate judgment. Reusable systems should support that work.</span></p></div>
</section>'''


def investor_evidence(apps):
    """Verified facts first; then what exists today and what lies ahead, in two registers."""
    topics = [
        ('Distribution', 'Discuss an audience, channel, or distribution opportunity for one of the apps.', 'Distribution'),
        ('Technology collaboration', 'Explore a specific integration or product collaboration around shared interests.', 'Technology collaboration'),
        ('Web app partnership', 'Discuss Engineering Max, Management Max, or Marketing Max for your team or portfolio.', 'Web apps'),
    ]
    topic_rows = []
    for index, (title, detail, context) in enumerate(topics, 1):
        href = '/contact?' + urlencode({'type': 'Strategic partner', 'product': context}) + '#prepare-inquiry'
        topic_rows.append(
            '<li><a class="partnership-topic" href="' + escape(href, quote=True)
            + '"><span class="partnership-topic-copy"><strong>' + escape(title)
            + '</strong><span class="partnership-topic-detail">' + escape(detail)
            + '</span></span><span class="partnership-topic-arrow" aria-hidden="true">→</span></a></li>'
        )
    listed = [app for app in apps if app.get('apple') and app.get('google')]
    icons = ''.join('<img src="/assets/' + escape(app['slug'], quote=True) + '-icon.webp" width="48" height="48" alt="" loading="lazy" decoding="async">' for app in listed)
    return '''<section class="investor-ledger wrap" id="at-a-glance" aria-labelledby="investor-ledger-title">
<h2 class="sr-only" id="investor-ledger-title">At a glance</h2>
<dl class="ledger">
<div><dt>Company</dt><dd>Solarity AI LLC · Irving, Texas</dd></div>
<div class="ledger-founder"><dt>Founder</dt><dd><a href="/company"><img class="ledger-print" src="/assets/brand/ata-turhan-320.db6d27d9b9b3.webp" width="96" height="120" alt="" loading="lazy" decoding="async"><span>Ata Turhan</span></a></dd></div>
<div><dt>Portfolio</dt><dd><a href="/apps">''' + str(len(listed)) + ''' mobile apps</a> on the App Store and Google Play, and <a href="/platform">''' + str(len(SAAS)) + ''' web apps</a></dd></div>
</dl>
</section>
<section class="investor-evidence wrap" id="thesis" aria-labelledby="investor-evidence-title">
<div class="investor-evidence-heading"><div>
<h2 id="investor-evidence-title">Build the product.<br>Learn from the work.</h2></div>
<p>Develop focused consumer experiences while exploring more repeatable ways to build, operate, and grow mobile products.</p></div>
<div class="today-ahead">
<article class="today-card" aria-labelledby="today-title"><p class="eyebrow">Today</p><h3 id="today-title">Four consumer apps. Three web apps.</h3><p>Self-care, cognitive practice, sleep, and fitness on iOS and Android, and Engineering Max, Management Max, and Marketing Max on the web.</p><div class="today-icons">''' + icons + '''</div><span class="status"><i aria-hidden="true"></i>Available on iOS&nbsp;&amp;&nbsp;Android</span></article>
<article class="ahead-card" aria-labelledby="investor-vision-title"><p class="eyebrow">Ahead</p><h3 id="investor-vision-title">The web apps, on mobile.</h3><p>Engineering Max, Management Max, and Marketing Max run on the web today. Mobile versions are planned, and Marketing Max plans a commercial version for other teams.</p><span class="status vision"><i aria-hidden="true"></i>Planned</span><a class="text-link" href="/platform">Explore the app factory <span aria-hidden="true">→</span></a></article>
</div>
''' + '''<div class="investor-commercial"><div><p class="eyebrow">Consumer model</p><h3>Subscriptions and in-app purchases.</h3><p>The apps have live listings with in-app purchases. Current plans, prices, and terms are available through their official store pages.</p></div><div><p class="eyebrow">Web apps</p><h3>Plans set by each product.</h3><p>Management Max has a free plan for one app and paid plans for larger portfolios. Engineering Max is free during private testing, and Marketing Max is in early access. Neither has a price yet.</p></div></div>

</section>
<section class="partnership-agenda wrap" id="conversation-paths" aria-labelledby="partnership-agenda-title"><div class="partnership-agenda-heading"><h2 id="partnership-agenda-title">Where we can build together.</h2><p>A useful conversation starts with a product, a shared problem, or a relevant audience.</p></div>
<ul class="partnership-topic-list">''' + ''.join(topic_rows) + '''</ul></section>'''

def founder_booking(btn, booking, email='ata.turhan@solarityai.com'):
    """The close: speak with the founder, beside the one reprise of the approved sunrise."""
    return ('<section class="founder-booking wrap" id="booking" aria-labelledby="founder-booking-title"><div class="founder-booking-copy">'
            '<h2 id="founder-booking-title">Compare perspectives with the founder.</h2>'
            '<p>Speak with Ata Turhan about the portfolio, company direction, or a potential collaboration.</p>'
            '<div class="founder-booking-action">' + btn('View available times', booking, 'primary', True)
            + btn('Email Ata', 'mailto:' + email, 'outline') + '</div></div>'
            '<figure class="booking-reprise"><img src="/assets/solar-ascent.webp" alt="A person climbing mountain steps toward a golden sunrise above the clouds" '
            'width="3720" height="1690" sizes="(max-width: 850px) 92vw, 600px" loading="lazy" decoding="async">'
            '<figcaption>Conceptual brand artwork</figcaption></figure></section>')


def operating_principles():
    """Optional replacement for the company feature-grid principles section."""
    return '''<section class="operating-principles wrap" aria-labelledby="operating-principles-title"><div class="operating-principles-heading"><h2 id="operating-principles-title">Broad ambition.<br>Specific choices.</h2></div><ol>
<li><h3>Give every product a clear purpose.</h3><p>Begin with a defined audience and a useful place in everyday life. Let that purpose guide what belongs in the experience.</p></li>
<li><h3>Make the next useful action clear.</h3><p>Treat design as part of how the product works. Clarity and consistency matter as much as visual character.</p></li>
<li><h3>Reuse the work. Keep the judgment.</h3><p>Develop workflows that may serve more than one product, while preserving the decisions each audience and problem needs.</p></li>
</ol></section>'''
