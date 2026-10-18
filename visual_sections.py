"""Semantic, source-authored visual sections for the Solarity AI site.

These symbols are decorative UI illustrations. They do not represent app screens,
product results, a company emblem, or a deployed platform architecture.
"""

from html import escape


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
    'build': '<path d="m8 7-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    'operate': '<rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="3" width="6" height="6" rx="1.5"/><rect x="9" y="15" width="6" height="6" rx="1.5"/><path d="M6 9v3h12V9M12 12v3"/>',
    'grow': '<path d="M4 20V4M4 20h16M8 16l4-5 4 2 5-8M16 5h5v5"/>',
    'training': '<path d="M3 8v8M6 6v12M18 6v12M21 8v8M6 12h12M3 12h3M18 12h3"/>',
    'nutrition': '<path d="M12 7c-5-4-10 1-8 7 2 6 5 7 8 5 3 2 6 1 8-5 2-6-3-11-8-7ZM12 7c-1-3 1-5 4-5"/>',
}

_FEATURE_SYMBOLS = {
    'looks-max': ('face', 'habits', 'calendar'),
    'iq-max': ('practice', 'adaptive', 'consistency'),
    'sleep-max': ('diary', 'routine', 'wind-down'),
    'fitness-max': ('training', 'nutrition', 'consistency'),
}


def _symbol(name):
    return ('<svg viewBox="0 0 24 24" width="32" height="32" '
            'fill="none" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" focusable="false">' + _ICONS[name] + '</svg>')


def feature_grid(app):
    """Return the complete product feature section, preserving supplied copy."""
    features = app.get('features', ())
    if not features:
        return ''
    symbols = _FEATURE_SYMBOLS.get(app['slug'], ('practice', 'habits', 'calendar'))
    cards = []
    for index, (title, description) in enumerate(features):
        symbol = symbols[index % len(symbols)]
        cards.append(
            '<article class="feature-tile"><span class="feature-index" aria-hidden="true">'
            + f'{index + 1:02d}' + '</span><span class="feature-symbol">'
            + _symbol(symbol) + '</span><div class="feature-copy"><h3>' + escape(title)
            + '</h3><p>' + escape(description) + '</p></div></article>'
        )
    return (
        '<section class="section wrap product-features '
        + escape(app.get('color', ''), quote=True)
        + '" aria-label="' + escape(app['name'], quote=True) + ' features">'
        '<div class="feature-section-heading"><p class="eyebrow">INSIDE '
        + escape(app['name'].upper()) + '</p><h2>The product experience.</h2></div>'
        '<div class="feature-grid illustrated-features">' + ''.join(cards)
        + '</div></section>'
    )


def platform_map(modules):
    """Return a conceptual lifecycle with ordinary links to module sections."""
    stages = {
        'engineering-max': ('Build', 'From requirements to review', 'build'),
        'management-max': ('Operate', 'Priorities, ownership & delivery', 'operate'),
        'marketing-max': ('Grow', 'Planning, storytelling & learning', 'grow'),
    }
    items = []
    for slug, number, name, _title, _label, _description, _detail in modules:
        stage, caption, icon = stages[slug]
        items.append(
            '<li><a class="lifecycle-stage" href="#' + escape(slug, quote=True)
            + '"><span class="stage-top"><span class="stage-symbol">'
            + _symbol(icon) + '</span><span class="stage-number">'
            + escape(number) + '</span></span><span class="stage-action">'
            + stage + '</span><strong>' + escape(name)
            + '</strong><span class="stage-caption">' + escape(caption)
            + '</span><span class="stage-link">Explore the direction '
            '<span aria-hidden="true">↓</span></span></a></li>'
        )
    return (
        '<section class="platform-map lifecycle-map wrap" '
        'aria-labelledby="platform-map-heading"><div class="lifecycle-heading">'
        '<div><p class="eyebrow">OUR INTENDED PRODUCT LIFECYCLE</p>'
        '<h2 id="platform-map-heading">A connected direction.</h2></div>'
        '<span class="lifecycle-badge">Platform vision</span></div>'
        '<ol class="lifecycle-steps">' + ''.join(items) + '</ol>'
        '<p class="lifecycle-note">Conceptual company strategy, not a depiction '
        'of deployed architecture. Specific capabilities and integrations are '
        'discussed with prospective partners.</p></section>'
    )


def founder_portrait(compact=False):
    """Official company portrait, uncropped and with reserved square geometry."""
    size = '(max-width: 560px) 160px, (max-width: 850px) 220px, 300px' if compact else '(max-width: 650px) calc(100vw - 40px), (max-width: 1356px) 45vw, 600px'
    return ('<img class="founder-photo' + (' founder-photo-compact' if compact else '') + '" '
            'src="/assets/brand/ata-turhan-640.742556487789.webp" '
            'srcset="/assets/brand/ata-turhan-320.db6d27d9b9b3.webp 320w, /assets/brand/ata-turhan-640.742556487789.webp 640w" '
            'sizes="' + size + '" width="640" height="640" alt="Ata Turhan, founder of Solarity AI" loading="lazy" decoding="async">')


def founder_card():
    """Return the verified portrait and a concise founder identity panel."""
    return (
        '<aside class="founder-panel founder-editorial portrait-editorial" aria-labelledby="founder-card-name">'
        + founder_portrait() + '<div class="founder-sheet">'
        '<p class="eyebrow">THE PERSON BEHIND THE COMPANY</p>'
        '<div class="founder-identity"><h2 id="founder-card-name">Ata Turhan<span>.</span></h2>'
        '<p>Founder of Solarity AI</p></div>'
        '<div class="founder-card-footer"><p><span>BASED IN</span>Irving, Texas</p>'
        '<a class="text-link" href="/contact">Connect with Ata '
        '<span aria-hidden="true">→</span></a></div></div></aside>'
    )
