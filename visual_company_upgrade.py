"""Evidence-led editorial sections adapted from the reference-site review.

The app list remains data-driven. Platform descriptions express company strategy,
not deployed integrations, customer traction, or external commercial availability.
"""
from html import escape
from urllib.parse import urlencode


def investor_opening(apps, btn, contact):
    """Place authentic, linked product evidence next to the company thesis."""
    products = []
    for app in apps:
        if not app.get('apple') or not app.get('google') or not app.get('screen'):
            continue
        alias = ('<span class="investor-opening-alias">In stores as '
                 + escape(app['store_name']) + '</span>') if app.get('store_name') else ''
        products.append(
            '<li><a class="investor-opening-product" href="/apps/'
            + escape(app['slug'], quote=True) + '" data-product-accent="'
            + escape(app['color'], quote=True) + '"><span class="investor-opening-screen">'
            + '<img src="/assets/' + escape(app['screen'], quote=True)
            + '" alt="" width="' + str(app.get('screen_width', 600))
            + '" height="' + str(app.get('screen_height', 1298))
            + '" sizes="(max-width: 560px) calc(50vw - 52px), (max-width: 850px) calc(50vw - 100px), (max-width: 1356px) 18vw, 216px" decoding="async"></span><span class="investor-opening-product-name">'
            + escape(app['name']) + '<span aria-hidden="true">↗</span></span>'
            + alias + '</a></li>'
        )
    return (
        '<section class="investor-opening wrap" aria-labelledby="investor-opening-title">'
        '<div class="investor-opening-copy"><p class="eyebrow">INVESTORS &amp; STRATEGIC PARTNERS</p>'
        '<h1 id="investor-opening-title">Products today.<br><span>Possibility ahead.</span></h1>'
        '<p class="lede">Focused consumer apps. A vision for the systems behind them. '
        'Explore the products, then the company direction.</p>'
        '<div class="actions">' + btn('Investor inquiries', contact('Investor'))
        + btn('Discuss a partnership', contact('Strategic partner'), 'outline')
        + '</div><a class="text-link faq-shortcut" href="#investor-questions">'
        'Read common questions <span aria-hidden="true">↓</span></a></div>'
        '<div class="investor-opening-proof"><div class="investor-opening-proof-heading">'
        '<p class="eyebrow">THE CONSUMER PORTFOLIO</p><span>' + str(len(products))
        + ' store-listed apps</span></div><ul class="investor-opening-products">'
        + ''.join(products) + '</ul><p class="investor-opening-caption">'
        'Official promotional imagery with sample content. Explore each product '
        'for its purpose, context, and store links.</p></div></section>'
    )


def strategy_story(btn, contact):
    """Replace the platform-bottom section with a readable strategy sequence."""
    return '''<section class="strategy-story wrap" aria-labelledby="strategy-story-title">
<div class="strategy-story-intro"><p class="eyebrow">WHY THE TWO PRODUCT LINES BELONG TOGETHER</p>
<h2 id="strategy-story-title">The products<br>ground the possibility.</h2>
<p>Focused apps give the company a practical context for exploring better ways to build, operate, and grow mobile products.</p>
<a class="text-link" href="/apps">Meet the consumer portfolio <span aria-hidden="true">→</span></a></div>
<ol class="strategy-story-steps">
<li><span class="strategy-story-number" aria-hidden="true">01</span><div><h3>Start with a specific human need.</h3><p>Self-care, cognitive practice, sleep, and fitness each call for a focused experience. Product choices start with that distinct purpose.</p></div></li>
<li><span class="strategy-story-number" aria-hidden="true">02</span><div><h3>Learn from the work behind it.</h3><p>Requirements, priorities, releases, and product storytelling are part of bringing an app to people. These disciplines inform the app factory direction.</p></div></li>
<li><span class="strategy-story-number" aria-hidden="true">03</span><div><h3>Develop patterns worth reusing.</h3><p>The ambition is to carry useful workflows into future products while preserving the judgment each one needs.</p><div class="strategy-story-disciplines"><a href="#engineering-max">Build <span aria-hidden="true">↗</span></a><a href="#management-max">Operate <span aria-hidden="true">↗</span></a><a href="#marketing-max">Grow <span aria-hidden="true">↗</span></a></div></div></li>
</ol>
<div class="strategy-story-bottom"><p><strong>People remain responsible for the decisions.</strong><span>Architecture, product priorities, and releases need deliberate judgment. Reusable systems should support that work.</span></p>''' + btn('Discuss the platform direction', contact('Strategic partner', 'App factory vision'), 'outline') + '''</div>
</section>'''


def investor_evidence(apps):
    """Current product evidence and precise partnership paths, without repeated CTAs."""
    topics = [
        ('Distribution', 'Discuss an audience, channel, or distribution opportunity for one of the apps.', 'Distribution'),
        ('Technology collaboration', 'Explore a specific integration or product collaboration around shared interests.', 'Technology collaboration'),
        ('Platform design partnership', 'Discuss product-building workflows that could inform the app factory vision.', 'Platform design partnership'),
    ]
    topic_rows = []
    for index, (title, detail, context) in enumerate(topics, 1):
        href = '/contact?' + urlencode({'type': 'Strategic partner', 'product': context}) + '#prepare-inquiry'
        topic_rows.append(
            '<li><a class="partnership-topic" href="' + escape(href, quote=True)
            + '"><span class="partnership-topic-number" aria-hidden="true">' + f'{index:02}'
            + '</span><span class="partnership-topic-copy"><strong>' + escape(title)
            + '</strong><span class="partnership-topic-detail">' + escape(detail)
            + '</span></span><span class="partnership-topic-arrow" aria-hidden="true">→</span></a></li>'
        )
    count = sum(bool(app.get('apple') and app.get('google')) for app in apps)
    return '''<section class="investor-evidence wrap" aria-labelledby="investor-evidence-title">
<div class="investor-evidence-heading"><div><p class="eyebrow">PRODUCT EVIDENCE. COMPANY DIRECTION.</p>
<h2 id="investor-evidence-title">Build the product.<br>Learn from the work.</h2></div>
<p>Develop focused consumer experiences while exploring more repeatable ways to build, operate, and grow mobile products.</p></div>
<div class="investor-evidence-body"><div class="investor-evidence-current"><p class="investor-evidence-label"><span>The product thesis</span><span>''' + str(count) + ''' store-listed apps</span></p>
<ol class="investor-thesis-list"><li><span aria-hidden="true">01</span><div><h3>Start with an everyday ambition.</h3><p>Self-care, cognitive practice, sleep, and fitness give each app a distinct purpose and audience.</p></div></li>
<li><span aria-hidden="true">02</span><div><h3>Learn through focused products.</h3><p>The practical work of bringing apps to people provides a context for exploring better product workflows.</p></div></li>
<li><span aria-hidden="true">03</span><div><h3>Develop useful patterns.</h3><p>The platform ambition is to make more of that work reusable, while keeping product decisions deliberate.</p></div></li></ol></div>
<aside class="investor-evidence-vision" aria-labelledby="investor-vision-title"><p class="eyebrow">THE PLATFORM VISION</p><h3 id="investor-vision-title">The work behind<br>the next product.</h3><p>Engineering Max, Management Max, and Marketing Max organize the intended direction for reusable product workflows.</p>
<dl class="investor-vision-disciplines"><div><dt>Build</dt><dd>Engineering Max</dd></div><div><dt>Operate</dt><dd>Management Max</dd></div><div><dt>Grow</dt><dd>Marketing Max</dd></div></dl>
<a class="text-link" href="/platform">Explore the platform direction <span aria-hidden="true">→</span></a></aside></div>
<div class="investor-commercial"><div><p class="eyebrow">CONSUMER MODEL</p><h3>Subscriptions and in-app purchases.</h3><p>The apps have live listings with in-app purchases. Current plans, prices, and terms are available through their official store pages.</p></div><div><p class="eyebrow">PLATFORM STRATEGY</p><h3>Potential commercialization.</h3><p>External commercial availability, connected capabilities, and partnership scope remain topics for discussion. They are not presented here as established platform services.</p></div></div>
</section>
<section class="partnership-agenda wrap" id="conversation-paths" aria-labelledby="partnership-agenda-title"><div class="partnership-agenda-heading"><p class="eyebrow">WAYS TO WORK TOGETHER</p><h2 id="partnership-agenda-title">Where we can<br>build together.</h2><p>A useful conversation starts with a product, a shared problem, or a relevant audience.</p></div>
<ul class="partnership-topic-list">''' + ''.join(topic_rows) + '''</ul></section>'''

def founder_booking(btn, booking):
    """A single, genuine external scheduling path after the investor FAQ."""
    return '''<section class="founder-booking wrap" aria-labelledby="founder-booking-title"><div><p class="eyebrow">A DIRECT CONVERSATION</p><h2 id="founder-booking-title">Compare perspectives<br>with the founder.</h2><p>Speak with Ata Turhan about the portfolio, company direction, or a potential collaboration.</p></div><div class="founder-booking-action">''' + btn('View available times', booking, 'primary', True) + '''<p>Opens Ata’s booking page on Google Calendar in a new tab.</p></div></section>'''


def operating_principles():
    """Optional replacement for the company feature-grid principles section."""
    return '''<section class="operating-principles wrap" aria-labelledby="operating-principles-title"><div class="operating-principles-heading"><p class="eyebrow">OUR PRODUCT PHILOSOPHY</p><h2 id="operating-principles-title">Broad ambition.<br>Specific choices.</h2></div><ol>
<li><span aria-hidden="true">01</span><h3>Give every product a clear purpose.</h3><p>Begin with a defined audience and a useful place in everyday life. Let that purpose guide what belongs in the experience.</p></li>
<li><span aria-hidden="true">02</span><h3>Make the next useful action clear.</h3><p>Treat design as part of how the product works. Clarity and consistency matter as much as visual character.</p></li>
<li><span aria-hidden="true">03</span><h3>Reuse the work. Keep the judgment.</h3><p>Develop workflows that may serve more than one product, while preserving the decisions each audience and problem needs.</p></li>
</ol></section>'''
