"""Semantic, source-authored visual sections for the Solarity AI site.

These symbols are decorative UI illustrations. They do not represent app screens,
product results, a company emblem, or a deployed platform architecture.
"""

from markupsafe import Markup

from templating import render


_ICONS = {
    'face': '<path d="M8 4H5a1 1 0 0 0-1 1v3M16 4h3a1 1 0 0 1 1 1v3M4 16v3a1 1 0 0 0 1 1h3M20 16v3a1 1 0 0 1-1 1h-3"/><path d="M8 9c0-3 8-3 8 0v4c0 3-2 5-4 5s-4-2-4-5Z"/><path d="M10 11h.01M14 11h.01M10.5 14.5c1 .7 2 .7 3 0"/>',
    'habits': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2M15 4V2M8 10l1.5 1.5L12 8.5M14 10h2M8 16l1.5 1.5L12 14.5M14 16h2"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4M17 3v4M3 10h18M7 14h2M12 14h2M7 18h2M16 17l1 1 2-2"/>',
    'practice': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M17.5 14v7M14 17.5h7"/>',
    'adaptive': '<path d="M5 3v4M5 11v10M12 3v10M12 17v4M19 3v2M19 9v12"/><rect x="3" y="7" width="4" height="4" rx="1"/><rect x="10" y="13" width="4" height="4" rx="1"/><rect x="17" y="5" width="4" height="4" rx="1"/>',
    'consistency': '<path d="M4 21V3M4 21h17M8 17v-4M13 17V9M18 17V5"/><path d="m16 5 2-2 2 2"/>',
    'diary': '<path d="M5 3h13a1 1 0 0 1 1 1v17H6a3 3 0 0 1-3-3V5a2 2 0 0 1 2-2ZM6 3v14M3 18a2 2 0 0 1 2-2h14M10 7h5M10 11h4"/>',
    'routine': '<circle cx="12" cy="12" r="8"/><path d="M12 7v5l3 2M5 3 3 5M19 3l2 2M8 21l-1 1M16 21l1 1"/>',
    'wind-down': '<path d="M15 3a7 7 0 0 0 6 10 8 8 0 1 1-6-10Z"/><path d="M4 19c2-1 3-1 5 0s3 1 5 0 3-1 5 0"/>',
    'training': '<path d="M3 8v8M6 6v12M18 6v12M21 8v8M6 12h12M3 12h3M18 12h3"/>',
    'invest': '<path d="M3 20h18"/><path d="m4 15 5-5 4 4 7-7"/><path d="M15 7h5v5"/>',
    'partner': '<circle cx="9" cy="12" r="5.5"/><circle cx="15" cy="12" r="5.5"/>',
    'apps': '<rect x="4" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.6"/>',
    'message': '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    'share': '<circle cx="12" cy="12" r="8"/><path d="M12 4v8l6 5"/>',
    'globe': '<circle cx="12" cy="12" r="8"/><path d="M4 12h16M12 4c2.4 2.3 3.6 5 3.6 8s-1.2 5.7-3.6 8c-2.4-2.3-3.6-5-3.6-8s1.2-5.7 3.6-8z"/>',
    'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/><circle cx="12" cy="12" r="2.2"/>',
    'nutrition': '<path d="M12 7c-5-4-10 1-8 7 2 6 5 7 8 5 3 2 6 1 8-5 2-6-3-11-8-7ZM12 7c-1-3 1-5 4-5"/>',
}

_FEATURE_SYMBOLS = {
    'looks-max': ('face', 'habits', 'calendar'),
    'iq-max': ('practice', 'adaptive', 'consistency'),
    'sleep-max': ('diary', 'routine', 'wind-down'),
    'fitness-max': ('training', 'nutrition', 'consistency'),
}


def symbol(name):
    """Public access to the decorative icon set, as a plain HTML string for concatenating callers."""
    return str(_symbol(name))


def _symbol(name):
    return render('visual_sections/symbol.html.j2', paths=_ICONS[name])


def feature_grid(app):
    """Return the complete product feature section, preserving supplied copy."""
    features = app.get('features', ())
    if not features:
        return ''
    symbols = _FEATURE_SYMBOLS.get(app['slug'], ('practice', 'habits', 'calendar'))
    cards = [{'title': title, 'description': description, 'icon': _symbol(symbols[index % len(symbols)])}
             for index, (title, description) in enumerate(features)]
    return str(render('visual_sections/feature_grid.html.j2',
                      color=app.get('color', ''), app_name=app['name'], cards=cards))


MAP_NOTE = ('Engineering Max and Marketing Max were built and tried first on Solarity AI’s own apps. '
            'The lines show where the work comes from; they are not data integrations.')


def _status_label(status):
    """The last part of a SaaS product's status, with its first letter capitalized."""
    label = status.split(' · ')[-1]
    return label[:1].upper() + label[1:]


def platform_map(apps, saas):
    """The app factory as light: the store-listed apps are the lit source on a horizon, and the three SaaS products
    they shaped sit below, each with its own status from its site. The dashed connectors read as "informs",
    never as integrations. The icons link to the apps and the nodes to the Platform chapters.
    """
    listed = [app for app in apps if app.get('apple') and app.get('google')]
    nodes = [{'slug': product['slug'], 'stage': product['stage'], 'name': product['name'],
              'category': product['category'], 'label': _status_label(product['status'])} for product in saas]
    return str(render('visual_sections/platform_map.html.j2', listed=listed, nodes=nodes, saas=saas, note=MAP_NOTE))


# The founder's published portrait files, shared by every page that shows him at a photo size.
FOUNDER_PORTRAIT = {'src': '/assets/brand/ata-turhan-640.742556487789.webp',
                    'srcset': '/assets/brand/ata-turhan-320.db6d27d9b9b3.webp 320w, /assets/brand/ata-turhan-640.742556487789.webp 640w, /assets/brand/ata-turhan-original.webp 800w'}


def founder_portrait():
    """Official company portrait, uncropped and with reserved square geometry (Company only)."""
    return str(render('visual_sections/founder_portrait.html.j2', portrait=FOUNDER_PORTRAIT))


def founder_card():
    """Return the verified portrait and a concise founder identity panel."""
    return str(render('visual_sections/founder_card.html.j2', portrait=Markup(founder_portrait())))
