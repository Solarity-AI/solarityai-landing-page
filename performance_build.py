"""Build-time delivery optimization. No runtime framework or external requests."""
from hashlib import sha256
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import gzip
import re

from optimize_images import responsive_image_attrs, avif_source_attrs
from optimize_styles import optimize_css

ROOT = Path(__file__).parent
RUNTIME = ROOT / 'dist/assets/runtime'


class _ImageTag(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.attrs = dict(attrs)


def _attributes(attrs):
    return ' '.join(name if value is None else f'{name}="{escape(str(value), quote=True)}"'
                    for name, value in attrs.items())


def _script_asset(name):
    source = (ROOT / 'scripts' / f'{name}.js').read_bytes()
    digest = sha256(source).hexdigest()[:12]
    target = RUNTIME / f'{name}.{digest}.js'
    RUNTIME.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source)
    return '/assets/runtime/' + target.name, len(source)


def optimize_page(document, path, css):
    """Return a completed document and exact source-byte measurements."""
    has_gallery = 'class="screenshot-open"' in document
    if not has_gallery:
        document = re.sub(r'<dialog\b[^>]*>.*?</dialog>', '', document, flags=re.S)

    preload = ''
    def image(match):
        nonlocal preload
        parser = _ImageTag()
        parser.feed(match.group())
        attrs = parser.attrs
        source = attrs.get('src')
        if not source:
            return match.group()
        classes = attrs.get('class', '').split()
        is_hero = 'progress-hero-image' in classes
        is_product_hero = 'hero-product-screen-primary' in classes
        if attrs.get('sizes'):
            # Component-specific layouts own their actual rendered image width.
            sizes = attrs['sizes']
        elif '-icon.webp' in source:
            sizes = attrs.get('width', '48') + 'px'
        elif '-screen-' in source:
            if '-detail-screen-' in source:
                sizes = '(max-width: 640px) 220px, (max-width: 1100px) 230px, 264px'
            elif path == '/':
                sizes = '(max-width: 560px) 168px, (max-width: 850px) 190px, (max-width: 1100px) 168px, 196px'
            elif path == '/apps':
                sizes = '(max-width: 640px) 220px, (max-width: 850px) 210px, (max-width: 1100px) 240px, 270px'
            else:
                sizes = '(max-width: 640px) 220px, (max-width: 1100px) 240px, 280px'
        elif path == '/company':
            sizes = '(max-width: 500px) calc(100vw - 40px), (max-width: 650px) 92vw, (max-width: 850px) calc(50.6vw - 17.6px), (max-width: 1356px) calc(50.6vw - 26.4px), 660px'
        else:
            sizes = '100vw'
        attrs.update(responsive_image_attrs(source, sizes=sizes))
        if is_product_hero:
            attrs['loading'] = 'eager'
            attrs['fetchpriority'] = 'high'
            preload = '<link ' + _attributes({
                'rel': 'preload', 'as': 'image', 'type': 'image/webp',
                'imagesrcset': attrs['srcset'], 'imagesizes': attrs['sizes'],
                'fetchpriority': 'high',
            }) + '>'
        if path.startswith('/apps/') and 'store-screen' in classes:
            attrs['loading'] = 'eager'
            attrs['fetchpriority'] = 'high'
        # The founder now opens Company; conceptual artwork is below the team.
        if path == '/company' and 'founder-photo' in classes:
            attrs['loading'] = 'eager'
        if is_hero:
            attrs['loading'] = 'eager'
            attrs['fetchpriority'] = 'high'
            avif = avif_source_attrs(source, sizes=sizes)
            preload = '<link ' + _attributes({
                'rel': 'preload', 'as': 'image', 'type': 'image/avif',
                'imagesrcset': avif['srcset'], 'imagesizes': avif['sizes'],
                'fetchpriority': 'high',
            }) + '>'
            return '<picture class="hero-picture"><source ' + _attributes(avif) + '><img ' + _attributes(attrs) + '></picture>'
        return '<img ' + _attributes(attrs) + '>'

    document = re.sub(r'<img\b[^>]*>', image, document)
    # Navigation affects the initial mobile header height. Inline it before CSS
    # and body parsing so slow/failed runtime requests cannot collapse a painted
    # fallback menu. With JavaScript disabled, the expanded CSS fallback remains.
    navigation = (ROOT / 'scripts/navigation.js').read_text(encoding='utf-8')
    assert '</script' not in navigation.lower()
    navigation_hash = sha256(navigation.encode()).hexdigest()
    navigation_tag = f'<script id="navigation-startup" data-source-sha256="{navigation_hash}">{navigation}</script>'
    scripts = []
    if has_gallery:
        scripts.append('gallery')
    if path == '/contact':
        scripts.append('contact')
    if path == '/careers':
        scripts.append('careers')
    script_tags, script_bytes = [], len(navigation.encode())
    for name in scripts:
        url, size = _script_asset(name)
        script_tags.append(f'<script src="{url}" defer></script>')
        script_bytes += size
    old_script = '<script src="/assets/site.js" defer></script>'
    assert document.count(old_script) == 1
    document = document.replace(old_script, ''.join(script_tags))

    compact, metrics = optimize_css(css, document)
    # HTML already declares UTF-8; @charset belongs only in external CSS files.
    compact = re.sub(r'^@charset\s+[\'\"][^\'\"]+[\'\"]\s*;', '', compact, flags=re.I)
    metrics['output_bytes'] = len(compact.encode())
    metrics['bytes_removed'] = metrics['source_bytes'] - metrics['output_bytes']
    assert '</style' not in compact.lower()
    source_hash = sha256(css.encode()).hexdigest()
    style = f'<style id="page-styles" data-source-sha256="{source_hash}">{compact}</style>'
    old_styles = '<link rel="stylesheet" href="/assets/presentation.css">'
    assert document.count(old_styles) == 1
    document = document.replace(old_styles, navigation_tag + preload + style)
    metrics.update({
        'css_gzip_bytes': len(gzip.compress(compact.encode(), mtime=0)),
        'css_delivery': 'Inline route-specific CSS; no blocking stylesheet request',
        'scripts': ['navigation'] + scripts,
        'inline_scripts': ['navigation'],
        'external_scripts': scripts,
        'javascript_bytes': script_bytes,
        'html_bytes': len(document.encode()),
        'html_gzip_bytes': len(gzip.compress(document.encode(), mtime=0)),
    })
    return document, metrics
