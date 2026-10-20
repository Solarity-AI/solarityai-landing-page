"""Editorial strategy sections with explicit evidence and ambition boundaries."""
from visual_sections import platform_map
from saas_products import MOBILE_PLAN
from templating import render


def platform_opening(apps, saas, btn, contact):
    """The app factory today: three web apps, shaped by the consumer apps, each with its own status."""
    return render('visual_strategy/platform_opening.html.j2', apps=apps, saas=saas, btn=btn, contact=contact,
                  platform_map=platform_map, mobile_plan=MOBILE_PLAN.split('. ')[-1])
