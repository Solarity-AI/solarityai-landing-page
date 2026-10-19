"""Editorial strategy sections with explicit evidence and ambition boundaries."""
from html import escape


def platform_opening(modules, btn, contact):
    """Show the strategic relationship without implying deployed integrations."""
    stages = {
        'engineering-max': ('Build', 'Requirements, implementation, review'),
        'management-max': ('Operate', 'Priorities, ownership, delivery'),
        'marketing-max': ('Grow', 'Planning, storytelling, learning'),
    }
    items = []
    for slug, number, name, *_rest in modules:
        stage, caption = stages[slug]
        items.append(
            '<li><a class="platform-discipline" href="#' + escape(slug, quote=True)
            + '"><span class="platform-discipline-copy">'
            + '<strong>' + stage + '</strong><span class="platform-discipline-name">'
            + escape(name) + '</span><span class="platform-discipline-caption">'
            + escape(caption) + '</span></span>'
            + '<span class="platform-discipline-arrow" aria-hidden="true">↓</span></a></li>'
        )
    return (
        '<section class="platform-opening wrap" aria-labelledby="platform-opening-title">'
        '<div class="platform-opening-copy"><p class="eyebrow">THE APP FACTORY / PLATFORM VISION</p>'
        '<h1 id="platform-opening-title">The work behind <span>what comes next.</span></h1>'
        '<p class="lede">A vision for the engineering, management, and marketing work '
        'behind focused mobile products.</p><div class="actions">'
        + btn('Discuss a partnership', contact('Strategic partner', 'App factory vision'))
        + '</div><a class="text-link platform-portfolio-link" href="/apps">'
        'Meet the products informing the direction <span aria-hidden="true">→</span></a></div>'
        '<figure class="platform-opening-map"><div class="platform-opening-map-heading">'
        '<p class="eyebrow">A PRODUCT-LED DIRECTION</p>'
        '<span class="strategy-vision-label">Platform vision</span></div>'
        '<div class="platform-strategy-visual"><div class="strategy-source">'
        '<span>Consumer portfolio</span><strong>Human<br>potential.</strong>'
        '<span>Focused mobile products</span></div>'
        '<svg class="strategy-connectors" viewBox="0 0 600 96" width="600" height="96" '
        'fill="none" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
        '<path d="M300 0V36M100 96V60Q100 36 124 36H476Q500 36 500 60V96M300 36V96" '
        'stroke="currentColor" stroke-width="1" vector-effect="non-scaling-stroke"/>'
        '<circle cx="300" cy="36" r="4" fill="currentColor"/></svg>'
        '<ol class="platform-disciplines">' + ''.join(items) + '</ol>'
        '<p class="strategy-outcome">Workflows to explore, learn from, and reuse.</p></div>'
        '<figcaption class="platform-opening-note"><strong>Conceptual company strategy.</strong> '
        'Consumer product work informs the intended platform direction. '
        'Connections shown do not represent deployed integrations.</figcaption>'
        '</figure></section>'
    )
