"""Solar-inspired company opening, product evidence, and an explicit strategy."""
from html import escape as e


def hero_section(apps, btn, contact):
    products = ''.join(
        f'<a class="hero-product" data-product-accent="{e(a["color"])}" href="/apps/{e(a["slug"])}">'
        f'<img src="/assets/{e(a["slug"])}-icon.webp" alt="" width="48" height="48">'
        f'<span><strong>{e(a["name"])}</strong><small>{e(a["category"])}</small></span>'
        '<span class="rail-arrow" aria-hidden="true">→</span></a>'
        for a in apps if a.get('apple')
    )
    return f'''<section class="vision-hero" aria-labelledby="hero-title">
      <div class="solar-hero-art">
        <img class="progress-hero-image" src="/assets/solar-ascent.webp" alt="A person climbing mountain steps toward a golden sunrise above the clouds" width="3720" height="1690" sizes="(max-width: 560px) 853px, 2113px" fetchpriority="high" loading="eager">
      </div>
      <div class="vision-story wrap">
        <div class="vision-copy">
          <h1 id="hero-title">Building for<br>human <em>potential.</em></h1>
          <p class="vision-description">AI-powered self-improvement apps, and the web apps we built to engineer, run, and grow them.</p>
        </div>
        <div class="vision-actions">
          <div class="actions">{btn('Investor inquiries',contact('Investor'))}{btn('Partnership inquiries',contact('Strategic partner'),'outline')}</div>
        </div>
      </div>
      <div class="hero-credits wrap">
        <nav class="hero-evidence-products" aria-label="Store-listed Solarity AI apps">{products}</nav>
        <div class="hero-credits-aside"><p class="hero-credits-meta">Four mobile apps · iOS&nbsp;&amp;&nbsp;Android</p><a class="text-link vision-explore" href="#our-products">Explore the portfolio <span aria-hidden="true">↓</span></a></div>
      </div>
    </section>'''


def closing_scene(statement, desc, contact, lead='investor'):
    """The one close per page: a statement and two inquiry paths in golden light."""
    def action(label, kind, style):
        return f'<a class="button {style}" href="{e(contact(kind))}">{label} <span aria-hidden="true">→</span></a>'
    investor, partner = ('Investor inquiries', 'Investor'), ('Partnership inquiries', 'Strategic partner')
    first, second = (partner, investor) if lead == 'partner' else (investor, partner)
    actions = action(*first, 'primary') + action(*second, 'outline')
    return f'''<section class="conversation-band wrap" aria-label="Connect with Solarity AI"><div><h2>{statement}</h2><p>{desc}</p></div><nav class="conversation-actions" aria-label="Inquiry paths">{actions}</nav></section>'''
