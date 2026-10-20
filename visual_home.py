"""Solar-inspired company opening, product evidence, and an explicit strategy."""
from templating import render
from visual_record import record_summary


def hero_section(apps, btn, contact):
    return render('visual_home/hero.html.j2', apps=apps, btn=btn, contact=contact, record=record_summary())


def closing_scene(statement, desc, contact, lead='investor', overview=False):
    """The one close per page: a statement and two inquiry paths in golden light. Pages before the
    investor overview also offer it, so an investor can read it before writing."""
    investor, partner = ('Investor inquiries', 'Investor'), ('Partnership inquiries', 'Strategic partner')
    first, second = (partner, investor) if lead == 'partner' else (investor, partner)
    actions = [(*first, 'primary'), (*second, 'outline')]
    return render('visual_home/closing_scene.html.j2', statement=statement, desc=desc, contact=contact, actions=actions, overview=overview)
