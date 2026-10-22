"""Search and answer-engine metadata: schema.org graph, robots.txt, sitemap dates, llms.txt and IndexNow.

Everything here restates facts the pages already show, the official store and developer listings
(REFERENCE_SITE_REVIEW.md), or the web apps' own sites (research-assets/saas-evidence.json).
No ratings, prices, store categories, users or results.
"""
import datetime
import hashlib
import html
import json
import re
from pathlib import Path

from company_facts import APP_STORE_RELEASES, COMPANY_PROFILES
from site_urls import public_path

ORIGIN = 'https://solarityai.com'
ORG_ID = ORIGIN + '/#organization'
SITE_ID = ORIGIN + '/#website'
FOUNDER_ID = ORIGIN + '/company/#ata-turhan'

# Official profiles. Developer listings name Solarity AI LLC and list all four apps (checked 2026-10-19).
STORE_PROFILES = [
    ('the App Store', 'https://apps.apple.com/us/developer/solarity-ai-llc/id1870988348'),
    ('Google Play', 'https://play.google.com/store/apps/developer?id=Solarity+AI+LLC'),
]
# The developer listings, then the company's own channels (company_facts.COMPANY_PROFILES).
ORG_PROFILES = [url for _, url in STORE_PROFILES] + [url for _, url in COMPANY_PROFILES]
# The founder profile the earlier solarityai.com paired with his portrait (research-assets/brand-evidence.json).
FOUNDER_PROFILES = ['https://www.linkedin.com/in/ataturhan/']
# App Store listing names, as the developer listing shows them on 2026-10-19.
STORE_NAMES = {
    'looks-max': 'Looks Max - Look Your Best',
    'iq-max': 'IQ Max: Smarter Every Day',
    'sleep-max': 'Sleep Max - Rest Best',
    'fitness-max': 'Only Fitness: AI Coach',
}
ORG_DESCRIPTION = ('Solarity AI builds AI-powered self-improvement apps for iOS and Android (Looks Max, IQ Max, '
                   'Sleep Max, and Fitness Max) and 3 web apps for engineering, managing, and marketing mobile '
                   'products (Engineering Max, Management Max, and Marketing Max).')

# Crawlers of search engines and AI assistants. All are welcome; robots.txt names them so the intent is explicit.
AI_CRAWLERS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User',
               'anthropic-ai', 'Claude-Web', 'PerplexityBot', 'Perplexity-User', 'Google-Extended',
               'Applebot-Extended', 'Amazonbot', 'Meta-ExternalAgent', 'MistralAI-User', 'DuckAssistBot', 'CCBot']

# IndexNow (Bing, Yandex, Seznam, Naver; Bing feeds ChatGPT search and Copilot). The key is public by design.
INDEXNOW_KEY = '5b1f0c7e9a4d4e2f8c3b6a1d7e0f9c42'

PAGE_TYPES = {'/apps': 'CollectionPage', '/platform': 'CollectionPage', '/company': 'AboutPage',
              '/contact': 'ContactPage', '/investors-partners': 'FAQPage'}
CRUMB_NAMES = {'/apps': 'Apps', '/platform': 'Platform', '/company': 'Company', '/press': 'Press kit', '/accessibility': 'Accessibility', '/website-data': 'Website data',
               '/investors-partners': 'Investors & partners', '/careers': 'Careers', '/contact': 'Contact'}


def plain(markup):
    """Visible text of an HTML fragment."""
    markup = re.sub(r'</p>\s*<p>', ' ', markup)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', markup))).strip()


# ---- page dates -------------------------------------------------------------------------------------
DATES_FILE = Path(__file__).resolve().parent / 'research-assets' / 'page-dates.json'


def script_json(data):
    """JSON for an inline <script> block. "<", ">" and "&" become JSON unicode escapes, so no string in
    the data can close the script element early (for example "</script>"); JSON readers decode them back."""
    return json.dumps(data).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')


def page_dates(pages):
    """Last content change per route. A route's date moves only when its body changes, so rebuilding
    unchanged content is byte-identical on any day (CI compares the rebuild with the committed dist)."""
    stored = json.loads(DATES_FILE.read_text(encoding='utf-8')) if DATES_FILE.is_file() else {}
    today = datetime.date.today().isoformat()
    dates = {}
    for path, (title, desc, body) in pages.items():
        digest = hashlib.sha256((title + '\0' + desc + '\0' + body).encode('utf-8')).hexdigest()[:16]
        record = stored.get(path)
        dates[path] = record if record and record['sha'] == digest else {'sha': digest, 'date': today}
    if dates != stored:
        DATES_FILE.write_text(json.dumps(dates, indent=2) + '\n', encoding='utf-8', newline='\n')
    return {path: record['date'] for path, record in dates.items()}


# ---- schema.org ---------------------------------------------------------------------------------------
def organization(email, logo):
    return {
        '@type': 'Organization', '@id': ORG_ID, 'name': 'Solarity AI', 'legalName': 'Solarity AI LLC',
        'url': ORIGIN + '/', 'logo': {'@type': 'ImageObject', 'url': ORIGIN + logo, 'width': 320, 'height': 320},
        'description': ORG_DESCRIPTION, 'founder': {'@id': FOUNDER_ID}, 'email': email,
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Irving', 'addressRegion': 'Texas', 'addressCountry': 'US'},
        'foundingLocation': {'@type': 'Place', 'name': 'Irving, Texas, United States'},
        'contactPoint': {'@type': 'ContactPoint', 'contactType': 'founder', 'email': email, 'url': ORIGIN + '/contact/',
                         'availableLanguage': 'English'},
        'sameAs': ORG_PROFILES,
    }


def founder(portrait):
    return {'@type': 'Person', '@id': FOUNDER_ID, 'name': 'Ata Turhan', 'jobTitle': 'Founder',
            'worksFor': {'@id': ORG_ID}, 'image': ORIGIN + portrait, 'url': ORIGIN + '/company/',
            'homeLocation': {'@type': 'Place', 'name': 'Irving, Texas, United States'}, 'sameAs': FOUNDER_PROFILES}


def team_member(m):
    """A team member as the Company page shows them: name, role, portrait and LinkedIn, nothing more."""
    node = {'@type': 'Person', '@id': f'{ORIGIN}/company/#{m["slug"]}', 'name': m['name'], 'worksFor': {'@id': ORG_ID},
            'url': ORIGIN + '/company/#team'}
    if m.get('role'):
        node['jobTitle'] = m['role']
    if m.get('image'):
        node['image'] = ORIGIN + m['image']
    if m.get('linkedin'):
        node['sameAs'] = [m['linkedin']]
    return node


def team_line(team):
    """The roster for llms.txt, with each member's role when it is known."""
    named = [m['name'] + (f' ({m["role"][0].lower() + m["role"][1:]})' if m.get('role') else '') for m in team]
    return ' and '.join(named) if len(named) < 3 else ', '.join(named[:-1]) + ', and ' + named[-1]


def mobile_app(a, full=True):
    url = ORIGIN + public_path('/apps/' + a['slug'])
    node = {'@type': 'MobileApplication', '@id': url + '#app', 'name': a['name'], 'url': url}
    if not full:
        return node
    names = [STORE_NAMES[a['slug']]] + (['Only Fitness'] if a['slug'] == 'fitness-max' else [])
    released = dict(APP_STORE_RELEASES).get(a['slug'])
    if released:
        node['datePublished'] = released
    node.update({
        'alternateName': names, 'description': a['intro'], 'abstract': a['summary'],
        'operatingSystem': 'iOS, Android', 'image': ORIGIN + '/assets/' + a['slug'] + '-icon.webp',
        'featureList': [f'{title}: {text}' for title, text in a['features']],
        'installUrl': [a['apple'], a['google']], 'sameAs': [a['apple'], a['google']],
        **({'screenshot': [ORIGIN + '/assets/' + a['screen']]} if a.get('screen') else {}),
        'author': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID},
    })
    return node


def web_app(p, full=True):
    node = {'@type': 'WebApplication', '@id': p['url'] + '#app', 'name': p['name'], 'url': p['url']}
    if not full:
        return node
    node.update({
        'description': p['summary'], 'abstract': p['tagline'], 'applicationCategory': 'BusinessApplication',
        'operatingSystem': 'Web', 'featureList': list(p['facts']), 'creativeWorkStatus': p['status'].split(' · ')[-1],
        'screenshot': [ORIGIN + '/assets/' + s['file'] for s in p.get('screens', [])],
        'author': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID},
    })
    return node


def breadcrumbs(path, name):
    url = ORIGIN + public_path(path)
    items = [('Home', ORIGIN + '/')]
    if path.startswith('/apps/'):
        items.append(('Apps', ORIGIN + '/apps/'))
    items.append((name, url))
    return {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}


def graph(path, title, desc, *, apps, saas, faq, email, logo, portrait, social_image, modified, team=()):
    """The schema.org graph for one route: organization, founder, site, the page itself, and what it presents."""
    url = ORIGIN + public_path(path)
    nodes = [organization(email, logo), founder(portrait),
             {'@type': 'WebSite', '@id': SITE_ID, 'name': 'Solarity AI', 'url': ORIGIN + '/', 'inLanguage': 'en',
              'description': ORG_DESCRIPTION, 'publisher': {'@id': ORG_ID}}]
    page = {'@type': PAGE_TYPES.get(path, 'WebPage'), '@id': url + '#webpage', 'url': url, 'name': title,
            'description': desc, 'inLanguage': 'en', 'isPartOf': {'@id': SITE_ID}, 'about': {'@id': ORG_ID},
            'publisher': {'@id': ORG_ID}, 'dateModified': modified,
            'primaryImageOfPage': {'@type': 'ImageObject', 'url': ORIGIN + '/assets/' + social_image, 'width': 1200, 'height': 630}}
    if path not in ('/', '/404'):
        crumb_name = next((a['name'] for a in apps if '/apps/' + a['slug'] == path), CRUMB_NAMES.get(path, title))
        nodes.append(breadcrumbs(path, crumb_name))
        page['breadcrumb'] = {'@id': url + '#breadcrumb'}
    store_apps = [a for a in apps if a.get('apple')]
    if path == '/':
        page['mainEntity'] = {'@id': ORG_ID}
        nodes.append({'@type': 'ItemList', '@id': url + '#products', 'name': 'Solarity AI products',
                      'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': node} for i, node in
                                          enumerate([mobile_app(a, False) for a in store_apps] + [web_app(p, False) for p in saas])]})
    elif path == '/apps':
        page['mainEntity'] = {'@id': url + '#apps'}
        nodes.append({'@type': 'ItemList', '@id': url + '#apps', 'name': 'Solarity AI mobile apps',
                      'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': mobile_app(a)} for i, a in enumerate(store_apps)]})
    elif path.startswith('/apps/'):
        a = next(a for a in apps if '/apps/' + a['slug'] == path)
        nodes.append(mobile_app(a))
        page['mainEntity'] = {'@id': url + '#app'}
    elif path == '/platform':
        page['mainEntity'] = {'@id': url + '#web-apps'}
        nodes.append({'@type': 'ItemList', '@id': url + '#web-apps', 'name': 'Solarity AI web apps',
                      'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': web_app(p)} for i, p in enumerate(saas)]})
    elif path == '/company':
        page['mainEntity'] = {'@id': ORG_ID}
        people = [team_member(m) for m in team]
        nodes[0]['employee'] = [{'@id': FOUNDER_ID}] + [{'@id': person['@id']} for person in people]
        nodes += people
    elif path == '/contact':
        page['mainEntity'] = {'@id': FOUNDER_ID}
    elif path == '/investors-partners':
        from ux_content import answer_id
        page['mainEntity'] = [{'@type': 'Question', 'url': url + '#' + answer_id(q), 'name': plain(q),
                               'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in faq]
    nodes.insert(3, page)
    return {'@context': 'https://schema.org', '@graph': nodes}


# ---- crawler files -------------------------------------------------------------------------------------
def robots_txt():
    return ('# Solarity AI welcomes search engines and AI assistants.\n'
            'User-agent: *\nAllow: /\n'
            + ''.join(f'\nUser-agent: {agent}\nAllow: /\n' for agent in AI_CRAWLERS)
            + f'\nSitemap: {ORIGIN}/sitemap.xml\n')


def sitemap_xml(pages, dates, images=None):
    """Every content page with its last change, plus the images it shows (Google's image sitemap extension)."""
    images = images or {}
    def row(p):
        pictures = ''.join(f'<image:image><image:loc>{html.escape(src)}</image:loc></image:image>' for src in images.get(p, []))
        return f'<url><loc>{ORIGIN}{public_path(p)}</loc><lastmod>{dates[p]}</lastmod>{pictures}</url>'
    rows = ''.join(row(p) for p in pages if p != '/404')
    return ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">' + rows + '</urlset>')


def llms_txt(pages, *, apps, saas, email, team=(), full=False):
    """llms.txt (llmstxt.org): a plain summary for AI assistants. llms-full.txt adds every product fact,
    the investor FAQ and the context notes, so an assistant can answer from one file."""
    from ux_content import FAQ
    link = lambda p: f'{ORIGIN}{public_path(p)}'
    store_apps = [a for a in apps if a.get('apple')]
    out = ['# Solarity AI', '', f'> {ORG_DESCRIPTION}', '',
           'Solarity AI LLC was founded by Ata Turhan in Irving, Texas, United States. '
           'The 4 mobile apps are listed on the App Store and Google Play. The 3 web apps run on the web today; '
           f'mobile versions are planned. Contact: {email} (founder Ata Turhan).', '']
    out += ['## Mobile apps (iOS and Android)', '']
    for a in store_apps:
        alias = ' Listed in the app stores as Only Fitness.' if a['slug'] == 'fitness-max' else ''
        released = dict(APP_STORE_RELEASES).get(a['slug'])
        alias += f' On the App Store since {released}.' if released else ''
        out.append(f'- [{a["name"]}]({link("/apps/" + a["slug"])}): {a["category"]}. {a["summary"]}{alias} '
                   f'[App Store]({a["apple"]}), [Google Play]({a["google"]})')
        if full:
            out += [f'  - {a["intro"]}'] + [f'  - {t}: {d}' for t, d in a['features']]
            note = a.get('note')
            if note:
                out.append(f'  - Context: {plain(note)}')
    out += ['', '## Web apps', '']
    for p in saas:
        out.append(f'- [{p["name"]}]({p["url"]}): {p["category"]}, {p["status"]}. {p["tagline"]}')
        if full:
            out += [f'  - {p["summary"]}'] + [f'  - {fact}' for fact in p['facts']] + [f'  - {p["availability"]}']
    out += ['', '## Company', '',
            f'- [Company and team]({link("/company")}): founder Ata Turhan, with {team_line(team)}.',
            f'- [App factory platform]({link("/platform")}): how the 3 web apps came from building the consumer apps.',
            f'- [Investors and partners]({link("/investors-partners")}): company thesis, business model and partnership paths.',
            f'- [Press kit]({link("/press")}): approved descriptions, facts, the sun mark, founder portrait, and app icons.',
            f'- [Careers]({link("/careers")}): fully remote roles for a Full Stack Engineer and a Marketing Specialist, full-time, part-time, or as an intern.',
            f'- [Contact]({link("/contact")}): email {email} or book a conversation with the founder.']
    if full:
        out += ['', '## Questions and answers', '']
        from ux_content import answer_id
        for q, a in FAQ:
            out += [f'### {plain(q)}', '', plain(a), '', f'Link: {link("/investors-partners")}#{answer_id(q)}', '']
    else:
        out += ['', '## Optional', '', f'- [Full product facts and FAQ]({ORIGIN}/llms-full.txt)',
                f'- [Website data]({link("/website-data")}): no cookies, cookieless page counts, and the services the site links to.',
                f'- [Accessibility]({link("/accessibility")}): the WCAG 2.2 AA target, how it is checked, and known limitations.']
    return '\n'.join(out).rstrip() + '\n'
