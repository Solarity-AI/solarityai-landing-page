"""Editorial strategy sections with explicit evidence and ambition boundaries."""
from visual_sections import platform_map


def platform_opening(apps, btn, contact):
    """Show the strategic relationship without implying deployed integrations."""
    return (
        '<section class="platform-opening wrap" aria-labelledby="platform-opening-title">'
        '<div class="platform-opening-copy"><p class="eyebrow">The app factory</p>'
        '<h1 id="platform-opening-title">The work behind <span>what comes next.</span></h1>'
        '<p class="lede">A vision for the engineering, management, and marketing work '
        'behind focused mobile products.</p><span class="status vision"><i aria-hidden="true"></i>Vision</span><div class="actions">'
        + btn('Partnership inquiries', contact('Strategic partner', 'App factory vision'))
        + '</div><a class="text-link platform-portfolio-link" href="/apps">'
        'Meet the products informing the direction <span aria-hidden="true">→</span></a></div>'
        + platform_map(apps, 'platform') + '</section>'
    )
