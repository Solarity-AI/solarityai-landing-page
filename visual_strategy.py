"""Editorial strategy sections with explicit evidence and ambition boundaries."""
from visual_sections import platform_map
from saas_products import MOBILE_PLAN


def platform_opening(apps, saas, btn, contact):
    """The app factory today: three web apps, shaped by the consumer apps, each with its own status."""
    return (
        '<section class="platform-opening wrap" aria-labelledby="platform-opening-title">'
        '<div class="platform-opening-copy"><p class="eyebrow">The app factory</p>'
        '<h1 id="platform-opening-title">The work behind <span>what comes next.</span></h1>'
        '<p class="lede">Three web apps for the engineering, management, and marketing work '
        'behind mobile products, built alongside Solarity AI’s own apps.</p>'
        '<p class="platform-plan"><span class="status"><i aria-hidden="true"></i>' + str(len(saas)) + ' web apps</span>'
        '<span class="status vision"><i aria-hidden="true"></i>' + MOBILE_PLAN.split('. ')[1] + '</span></p><div class="actions">'
        + btn('Partnership inquiries', contact('Strategic partner', 'App factory'))
        + '</div><a class="text-link platform-portfolio-link" href="/apps">'
        'Meet the products informing the direction <span aria-hidden="true">→</span></a></div>'
        + platform_map(apps, saas) + '</section>'
    )
