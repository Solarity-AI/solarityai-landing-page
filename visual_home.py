"""Solar-inspired company opening, product evidence, and an explicit strategy."""
from html import escape as e
from visual_sections import platform_map


def hero_section(apps, btn, contact):
    products = ''.join(
        f'<a class="hero-product" data-product-accent="{e(a["color"])}" href="/apps/{e(a["slug"])}">'
        f'<img src="/assets/{e(a["slug"])}-icon.webp" alt="" width="48" height="48">'
        f'<span><strong>{e(a["name"])}</strong><small>{e(a["category"])}</small></span>'
        '<span class="rail-arrow" aria-hidden="true">→</span></a>'
        for a in apps if a.get('apple')
    )
    return f'''<section class="vision-hero" aria-labelledby="hero-title">
      <figure class="solar-hero-art" aria-labelledby="hero-image-caption">
        <img class="progress-hero-image" src="/assets/solar-ascent.webp" alt="A person climbing mountain steps toward a golden sunrise above the clouds" width="1860" height="845" sizes="(max-width: 560px) 1233px, 2113px" fetchpriority="high" loading="eager">
        <figcaption id="hero-image-caption">Conceptual brand artwork</figcaption>
      </figure>
      <div class="vision-story wrap">
        <div class="vision-copy">
          <h1 id="hero-title">Building for<br>human <em>potential.</em></h1>
          <p class="vision-description">AI-powered self-improvement apps, and the systems we are developing to build, operate, and grow them.</p>
        </div>
        <div class="vision-actions">
          <div class="actions">{btn('Investor inquiries',contact('Investor'))}{btn('Partnership inquiries',contact('Strategic partner'),'outline')}</div>
        </div>
      </div>
      <div class="hero-credits wrap">
        <nav class="hero-evidence-products" aria-label="Store-listed Solarity AI apps">{products}</nav>
        <div class="hero-credits-aside"><p class="hero-credits-meta">Four apps · iOS&nbsp;&amp;&nbsp;Android</p><a class="text-link vision-explore" href="#our-products">Explore the portfolio <span aria-hidden="true">↓</span></a></div>
      </div>
    </section>'''


def company_strategy(apps, btn, contact):
    """Describe the strategic relationship without implying deployed integration."""
    return f'''<section class="company-strategy" aria-labelledby="strategy-title"><div class="strategy-layout wrap">
      <div class="strategy-copy"><p class="eyebrow">The app factory</p><h2 id="strategy-title">Build the product. <br><span>Improve the way it gets built.</span></h2><p>Each app starts with a distinct human ambition. Building these products also informs the workflows we want to make more repeatable.</p><p>Our app factory vision connects this experience with a longer-term focus on engineering, operations, and marketing.</p><a class="text-link" href="/platform">Explore the app factory <span aria-hidden="true">→</span></a></div>
      {platform_map(apps, 'home')}
    </div></section>'''


def closing_scene(statement, desc, contact, lead='investor'):
    """The one close per page: a statement and two inquiry paths in golden light."""
    def action(label, kind, style):
        return f'<a class="button {style}" href="{e(contact(kind))}">{label} <span aria-hidden="true">→</span></a>'
    investor, partner = ('Investor inquiries', 'Investor'), ('Partnership inquiries', 'Strategic partner')
    first, second = (partner, investor) if lead == 'partner' else (investor, partner)
    actions = action(*first, 'primary') + action(*second, 'outline')
    return f'''<section class="conversation-band wrap" aria-label="Connect with Solarity AI"><div><h2>{statement}</h2><p>{desc}</p></div><nav class="conversation-actions" aria-label="Inquiry paths">{actions}</nav></section>'''
