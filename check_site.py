"""Static artifact audit only. Does not run a server or claim browser coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
from performance_build import compact_script
import ast,html,json,re
from hashlib import sha256
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
from site_urls import public_path
import seo

ROOT=Path(__file__).parent
DIST=ROOT/'dist'
BUNDLE=ROOT/'design/presentation.css'
ORIGIN='https://solarityai.com'
class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.tags=[];self.ids=[];self.title=[];self.h1=[];self.headings=[];self.in_title=False;self.in_h1=False;self.label_depth=0;self.implicit_labeled_controls=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.tags.append((tag,a))
        if tag=='label':self.label_depth+=1
        if tag in ['input','select','textarea'] and self.label_depth:self.implicit_labeled_controls.add(len(self.tags)-1)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='title':self.in_title=True
        if tag=='h1':self.in_h1=True;self.h1.append('')
        if re.fullmatch(r'h[1-6]',tag):self.headings.append(int(tag[1]))
    def handle_endtag(self,tag):
        if tag=='label':self.label_depth=max(0,self.label_depth-1)
        if tag=='title':self.in_title=False
        if tag=='h1':self.in_h1=False
    def handle_data(self,data):
        if self.in_title:self.title.append(data)
        if self.in_h1:self.h1[-1]+=data

docs={};errors=[];warnings=[];links_checked=0;assets_checked=0
for file in sorted(DIST.rglob('*.html')):
    d=Document();d.feed(file.read_text(encoding='utf-8'));docs[file]=d
for file,d in docs.items():
    rel=file.relative_to(DIST).as_posix()
    if len(d.h1)!=1:errors.append(f'{rel}: {len(d.h1)} H1 elements')
    for previous,current in zip(d.headings,d.headings[1:]):
        if current>previous+1:errors.append(f'{rel}: heading level skips from H{previous} to H{current}')
    if not ''.join(d.title).strip():errors.append(f'{rel}: missing title')
    for value,n in Counter(d.ids).items():
        if n>1:errors.append(f'{rel}: duplicate id {value}')
    meta={a.get('name') or a.get('property'):a.get('content','') for t,a in d.tags if t=='meta'}
    for name in ['description','viewport','og:title','og:description','og:url','og:image']:
        if not meta.get(name):errors.append(f'{rel}: missing {name}')
    canonical=[a.get('href','') for t,a in d.tags if t=='link' and a.get('rel')=='canonical']
    route='/' if file==DIST/'index.html' else '/404' if file==DIST/'404.html' else '/'+file.parent.relative_to(DIST).as_posix()
    expected_url=ORIGIN+public_path(route)
    # The error page is noindex and names no canonical: it is not a page search engines should keep.
    if canonical!=([] if route=='/404' else [expected_url]):errors.append(f'{rel}: unexpected canonical {canonical}')
    if meta.get('og:url')!=expected_url:errors.append(f'{rel}: Open Graph URL must match the final canonical URL')
    if meta.get('referrer')!='strict-origin-when-cross-origin':errors.append(f'{rel}: missing browser referrer policy')
    labels={a['for'] for t,a in d.tags if t=='label' and a.get('for')}
    for tag_index,(t,a) in enumerate(d.tags):
        if t in ['input','select','textarea'] and a.get('type') not in ['hidden','submit','button'] and a.get('id') not in labels and not a.get('aria-label') and not a.get('aria-labelledby') and tag_index not in d.implicit_labeled_controls:errors.append(f'{rel}: unlabeled {t} {a.get("id")}')
        for reference in ['aria-labelledby','aria-describedby','aria-controls']:
            for target_id in a.get(reference,'').split():
                if target_id not in d.ids:errors.append(f'{rel}: {reference} references missing id {target_id}')
        if t in ['img','source']:
            if t=='img' and 'alt' not in a:errors.append(f'{rel}: image missing alt {a.get("src")}')
            if t=='img' and (not a.get('width') or not a.get('height')):errors.append(f'{rel}: image missing dimensions {a.get("src")}')
            for candidate in a.get('srcset','').split(','):
                if not candidate.strip():continue
                candidate_url=candidate.strip().split()[0]
                candidate_parts=urlsplit(candidate_url)
                if candidate_parts.scheme or candidate_parts.netloc:continue
                candidate_file=DIST/unquote(candidate_parts.path.lstrip('/')) if candidate_parts.path.startswith('/') else file.parent/unquote(candidate_parts.path)
                if not candidate_file.is_file():errors.append(f'{rel}: missing responsive image candidate {candidate_url}')
                else:assets_checked+=1
        if t=='a' and a.get('target')=='_blank' and 'noopener' not in a.get('rel',''):errors.append(f'{rel}: unsafe external target')
        attr='href' if t in ['a','link'] else 'src' if t in ['script','img'] else None
        if not attr or attr not in a:continue
        url=a[attr];u=urlsplit(url)
        if u.scheme or u.netloc:continue
        target=DIST/unquote(u.path.lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path) if u.path else file
        if target.is_dir():target=target/'index.html'
        elif not target.exists() and not target.suffix:target=target/'index.html'
        if not target.is_file():errors.append(f'{rel}: missing target {url}');continue
        if target.suffix=='.html':
            links_checked+=1
            if u.fragment and unquote(u.fragment) not in docs.get(target,Document()).ids:errors.append(f'{rel}: missing fragment {url}')
            if t=='a' and u.path.startswith('/'):
                target_route='/' if target==DIST/'index.html' else '/404' if target==DIST/'404.html' else '/'+target.parent.relative_to(DIST).as_posix()
                if u.path!=public_path(target_route):errors.append(f'{rel}: internal link requires a host redirect: {url}')
        else:assets_checked+=1
    text=file.read_text(encoding='utf-8')
    if '\u2014' in text:errors.append(f'{rel}: long dash')
    # Cloudflare skips Email Address Obfuscation inside email_off, keeping mailto links intact.
    if not re.search(r'<body\b[^>]*><!--email_off-->.*<!--/email_off--></body>',text,re.S):errors.append(f'{rel}: page body must be wrapped in email_off')
    if re.search(r'lorem ipsum|href=[\"\x27]#(?:[\"\x27])',text,re.I):errors.append(f'{rel}: placeholder content/link')

    # Static integration contracts for the progressively enhanced UX.
    by_id={a['id']:(t,a) for t,a in d.tags if 'id' in a}
    main=by_id.get('main')
    if not main or main[0]!='main' or main[1].get('tabindex')!='-1':errors.append(f'{rel}: skip target must be a focusable main landmark')
    stylesheets=[a.get('href') for t,a in d.tags if t=='link' and a.get('rel')=='stylesheet']
    if stylesheets:errors.append(f'{rel}: unexpected render-blocking stylesheet request')
    inline_styles=[a for t,a in d.tags if t=='style' and a.get('id')=='page-styles']
    css_source_hash=sha256(BUNDLE.read_bytes()).hexdigest()
    if len(inline_styles)!=1 or inline_styles[0].get('data-source-sha256')!=css_source_hash:errors.append(f'{rel}: missing or stale route-specific inline CSS')
    runtime_scripts=[a.get('src','') for t,a in d.tags if t=='script' and a.get('src')]
    expected_scripts=[]
    if any(t=='a' and 'screenshot-open' in a.get('class','').split() for t,a in d.tags):expected_scripts.append('gallery')
    if rel=='contact/index.html':expected_scripts.append('contact')
    if rel=='careers/index.html':expected_scripts.append('careers')
    if any('data-copy' in a for t,a in d.tags):expected_scripts.append('copy')
    if rel=='404.html':expected_scripts.append('not-found')
    actual_scripts=[]
    for script in runtime_scripts:
        match=re.fullmatch(r'/assets/runtime/(gallery|contact|careers|copy|not-found)\.([a-f0-9]{12})\.js',script)
        if not match:errors.append(f'{rel}: unexpected runtime script {script}');continue
        actual_scripts.append(match.group(1))
        script_file=DIST/script.lstrip('/')
        if script_file.is_file() and sha256(script_file.read_bytes()).hexdigest()[:12]!=match.group(2):errors.append(f'{rel}: script filename hash does not match its content')
    if actual_scripts!=expected_scripts:errors.append(f'{rel}: incorrect route-specific scripts {actual_scripts}')
    startup=re.search(r'<script\b[^>]*id="navigation-startup"[^>]*>(.*?)</script>',text,re.S)
    navigation_source=(ROOT/'scripts/navigation.js').read_text(encoding='utf-8')
    startup_tags=[a for t,a in d.tags if t=='script' and a.get('id')=='navigation-startup']
    if len(startup_tags)!=1 or not startup or startup.group(1)!=compact_script(navigation_source):
        errors.append(f'{rel}: missing or stale inline navigation startup')
    elif '<style id="page-styles"' not in text or startup.end()>text.index('<style id="page-styles"') or startup.end()>text.index('</head>'):
        errors.append(f'{rel}: navigation layout must be selected before styles and body painting')
    if startup_tags and (any(key in startup_tags[0] for key in ['src','defer','async']) or startup_tags[0].get('type','') not in ['', 'text/javascript']):
        errors.append(f'{rel}: navigation startup must execute synchronously without a network dependency')
    if startup_tags and startup_tags[0].get('data-source-sha256')!=sha256(navigation_source.encode()).hexdigest():
        errors.append(f'{rel}: stale navigation source hash')
    sections_startup=re.search(r'<script\b[^>]*id="sections-startup"[^>]*>(.*?)</script>',text,re.S)
    wants_sections='data-answers-toggle' in text or 'class="saas-index' in text
    if wants_sections!=bool(sections_startup) or (sections_startup and sections_startup.group(1)!=compact_script((ROOT/'scripts/sections.js').read_text(encoding='utf-8'))):
        errors.append(f'{rel}: sections script must be inlined, current, exactly where answers or a section index appear')
    # Intent-based prefetch speeds page-to-page moves; prerender would run analytics for unseen visits.
    speculation=[m.group(2) for m in re.finditer(r'<script\b([^>]*)>(.*?)</script>',text,re.S) if re.search(r'\btype="speculationrules"',m.group(1))]
    try:rules=json.loads(speculation[0]) if len(speculation)==1 else None
    except ValueError:rules=None
    if not isinstance(rules,dict) or set(rules)!={'prefetch'} or not rules['prefetch']:errors.append(f'{rel}: expected one prefetch-only speculation rules block')
    elif any(rule.get('eagerness') not in ['moderate','conservative'] or {'not':{'href_matches':'/assets/*'}} not in rule.get('where',{}).get('and',[]) for rule in rules['prefetch']):
        errors.append(f'{rel}: speculation rules must wait for visitor intent and skip asset files')
    expected_robots={'noindex','follow'} if rel=='404.html' else {'index','follow','max-image-preview:large'}
    actual_robots={directive.strip().lower() for directive in meta.get('robots','').split(',')}
    if actual_robots!=expected_robots:errors.append(f'{rel}: incorrect public-site indexing directive {meta.get("robots", "")}')
    for t,a in d.tags:
        # sizes is evaluated against the viewport: container and percentage units make browsers discard it.
        if t in ('img','source') and re.search(r'\d(?:cq(?:i|b|w|h|min|max)|%)',a.get('sizes','')):errors.append(f'{rel}: sizes uses a unit browsers reject: {a.get("sizes")}')
        if t=='img' and a.get('src','').startswith('/assets/optimized/') and not a.get('srcset'):errors.append(f'{rel}: optimized image missing responsive candidates')
    # Preserve the approved brand opening and progressive image/navigation contracts.
    if 'human-potential-' in text:errors.append(f'{rel}: retired symbolic hero artwork is still referenced')
    if 'Voice Max' in text or '/apps/voice-max' in text:errors.append(f'{rel}: retired Voice Max product is still referenced')
    header_match=re.search(r'<header\b[^>]*>(.*?)</header>',text,re.S)
    if header_match:
        header=header_match.group(1)
        nav_match=re.search(r'<nav\b[^>]*id="site-nav"[^>]*>(.*?)</nav>',header,re.S)
        toggle_match=re.search(r'<button\b[^>]*class="menu-toggle"',header)
        if not nav_match or not toggle_match or toggle_match.start()>nav_match.start():errors.append(f'{rel}: navigation toggle must precede its controlled links')
        if nav_match and 'href="/contact/"' not in header[nav_match.end():]:errors.append(f'{rel}: persistent Contact action must remain outside the collapsible navigation')
    else:errors.append(f'{rel}: missing shared header')
    footer_match=re.search(r'<footer\b[^>]*>(.*?)</footer>',text,re.S)
    for slug in ['looks-max','iq-max','sleep-max','fitness-max']:
        if not footer_match or f'href="/apps/{slug}/"' not in footer_match.group(1):errors.append(f'{rel}: footer is missing the {slug} product route')
    for t,a in d.tags:
        if t=='a' and 'screenshot-open' in a.get('class','').split():
            if not a.get('data-image-title') or not a.get('data-image-alt'):errors.append(f'{rel}: screenshot enlargement is missing descriptive dialog data')
            if not a.get('href','').startswith('/assets/') or a.get('target')!='_blank':errors.append(f'{rel}: screenshot enlargement lost its native direct-image fallback')
    # The app factory map: each web app node states its own status, and the legend says the lines are not integrations.
    saas_slugs=['engineering-max','management-max','marketing-max']
    for figure in re.findall(r'<figure class="pmap[^"]*">(.*?)</figure>',text,re.S):
        nodes=re.findall(r'class="pmap-node" href="#([\w-]+)">(.*?)</a></li>',figure,re.S)
        if [n[0] for n in nodes]!=saas_slugs or any('class="status"><i aria-hidden="true"></i>' not in n[1] for n in nodes):errors.append(f'{rel}: each app factory map node needs its web app status')
        if 'they are not data integrations' not in figure:errors.append(f'{rel}: the app factory map needs its legend')
    if rel=='platform/index.html':
        if 'class="pmap' not in text:errors.append(f'{rel}: missing the app factory map')
        # One chapter per web app, each with a real screen from its own site and a link to that site.
        for slug in saas_slugs:
            chapter=re.search(r'<section class="saas-chapter[^"]*" id="'+slug+r'"[^>]*>(.*?)</section>',text,re.S)
            if not chapter:errors.append(f'{rel}: missing the {slug} chapter');continue
            if not re.search(r'<img class="web-shot"[^>]*src="/assets/optimized/'+slug+r'-',chapter.group(1)):errors.append(f'{rel}: the {slug} chapter needs its product screenshot')
            # The link may carry the site's campaign tag (site_urls.attributed), so only the origin is fixed.
            if not re.search(r'href="https://'+slug.replace('-','')+r'\.solarityai\.com/(\?[^"]*)?"',chapter.group(1)):errors.append(f'{rel}: the {slug} chapter must link to its own site')
    # Every footer lists the whole portfolio: the four mobile apps and the three web apps.
    for slug in saas_slugs:
        if not footer_match or f'href="/platform/#{slug}"' not in footer_match.group(1):errors.append(f'{rel}: footer is missing the {slug} web app')
    if rel=='company/index.html':
        # Each approved team member has one 4:5 portrait or, until a photo is supplied, a monogram in the same frame.
        members=re.findall(r'<li class="selected-team-member"[^>]*>(.*?)</li>',text,re.S)
        if len(members)!=6:errors.append(f'{rel}: the team roster must list the six approved members')
        for member in members:
            if not re.search(r'<img class="team-portrait"[^>]*src="/assets/optimized/[a-z-]+-\d+\.[0-9a-f]{12}\.webp"[^>]*width="480" height="600"',member) and 'class="team-portrait team-monogram"' not in member:errors.append(f'{rel}: each team member needs a portrait or a monogram')
    if rel=='index.html':
        # The web apps follow the consumer wall: three cards in map order, each linking to its chapter and its site.
        saas_cards=re.findall(r'<li class="saas-card" id="home-([\w-]+)">(.*?)</li>',text,re.S)
        if [c[0] for c in saas_cards]!=saas_slugs:errors.append(f'{rel}: Home must introduce the three web apps in order')
        for slug,card in saas_cards:
            if f'href="/platform/#{slug}"' not in card or not re.search(r'href="https://'+slug.replace('-','')+r'\.solarityai\.com/(\?[^"]*)?"',card):errors.append(f'{rel}: each web app card links to its chapter and its site')
            if not re.search(r'<img class="web-shot"[^>]*src="/assets/optimized/'+slug+r'-',card):errors.append(f'{rel}: each web app card needs its product screenshot')
        # The portfolio wall: the four apps in APPS order, each with its icon and both store links.
        wall=re.search(r'<ul class="wall-grid"[^>]*>(.*?)</ul>',text,re.S)
        cards=re.findall(r'<li class="wall-card"[^>]*>(.*?)</li>',wall.group(1),re.S) if wall else []
        expected=['looks-max','iq-max','sleep-max','fitness-max']
        if [re.search(r'class="wall-link" href="/apps/([\w-]+)/"',c).group(1) if re.search(r'class="wall-link" href="/apps/([\w-]+)/"',c) else None for c in cards]!=expected:errors.append(f'{rel}: portfolio wall must link the four apps in order')
        for card in cards:
            if not re.search(r'<img [^>]*src="/assets/optimized/[\w-]+-icon-',card):errors.append(f'{rel}: each portfolio card needs its app icon')
            if 'https://apps.apple.com/' not in card or 'https://play.google.com/' not in card:errors.append(f'{rel}: each portfolio card needs its App Store and Google Play links')
        hero_links=[a.get('href') for t,a in d.tags if t=='a' and 'hero-product' in a.get('class','').split()]
        if hero_links!=['/apps/looks-max/','/apps/iq-max/','/apps/sleep-max/','/apps/fitness-max/']:errors.append(f'{rel}: hero must feature only the four verified store-listed apps')
        primary_images=[a for t,a in d.tags if t=='img' and 'progress-hero-image' in a.get('class','').split()]
        hero_sources=[a for t,a in d.tags if t=='source' and a.get('type')=='image/avif' and 'solar-ascent-' in a.get('srcset','')]
        if len(primary_images)!=1 or 'solar-ascent-' not in primary_images[0].get('src',''):errors.append(f'{rel}: hero must use the founder-approved atmospheric sunrise artwork')
        if primary_images and (primary_images[0].get('width')!='3720' or primary_images[0].get('height')!='1690'):errors.append(f'{rel}: hero must reserve the correct intrinsic dimensions')
        if len(primary_images)!=1 or primary_images[0].get('loading')!='eager' or primary_images[0].get('fetchpriority')!='high':errors.append(f'{rel}: hero artwork must load eagerly at high priority')
        if len(hero_sources)!=1 or not primary_images or hero_sources[0].get('sizes')!=primary_images[0].get('sizes'):errors.append(f'{rel}: hero AVIF and WebP must share the rendered image-size contract')
        # The founder removed the hero caption on 2026-10-19; the artwork keeps its descriptive alt text.
        if 'hero-image-caption' in text:errors.append(f'{rel}: the Home hero carries no caption (founder decision, 2026-10-19)')
        hero_preloads=[a for t,a in d.tags if t=='link' and a.get('rel')=='preload' and a.get('as')=='image']
        if len(hero_preloads)!=1 or not hero_sources or hero_preloads[0].get('type')!='image/avif' or hero_preloads[0].get('imagesrcset')!=hero_sources[0].get('srcset') or hero_preloads[0].get('imagesizes')!=hero_sources[0].get('sizes'):errors.append(f'{rel}: hero preload must match the primary AVIF source exactly')
    if rel.startswith('apps/') and rel!='apps/index.html':
        slug=file.parent.name
        if not any(t=='nav' and a.get('aria-label')=='Breadcrumb' for t,a in d.tags):errors.append(f'{rel}: missing breadcrumb landmark')
        if not any(t=='a' and a.get('href')=='/apps/#'+slug for t,a in d.tags):errors.append(f'{rel}: missing contextual portfolio return')
        if not any(t=='a' and a.get('href')=='/apps/' and a.get('aria-current')=='location' for t,a in d.tags):errors.append(f'{rel}: parent Apps link must identify current section')
        if not any(t=='nav' and a.get('aria-label')=='Other Solarity AI apps' for t,a in d.tags):errors.append(f'{rel}: missing sibling app navigation')
        for t,a in d.tags:
            if t=='img' and 'store-screen' in a.get('class','').split() and (a.get('loading')=='lazy' or a.get('fetchpriority')!='high'):errors.append(f'{rel}: opening product image must not be lazy loaded')
    if rel=='careers/index.html':
        career_form=by_id.get('career-form',('',{}))
        if career_form[0]!='form' or career_form[1].get('action')!='https://formsubmit.co/careers@solarityai.com' or career_form[1].get('method','').lower()!='post':errors.append(f'{rel}: careers must retain the founder-selected native POST destination')
        if 'novalidate' in career_form[1]:errors.append(f'{rel}: no-JavaScript application validation must remain enabled')
        required_fields={'career-name':'fullName','career-email':'email','career-position':'position','career-work-type':'workType'}
        for control_id,name in required_fields.items():
            control=by_id.get(control_id,('',{}))[1]
            if control.get('name')!=name or 'required' not in control:errors.append(f'{rel}: missing required application control {control_id}')
            if control_id+'-error' not in control.get('aria-describedby','').split():errors.append(f'{rel}: application control must reference its error {control_id}')
        for control_id,name in {'career-linkedin':'linkedin','career-portfolio':'portfolio'}.items():
            control=by_id.get(control_id,('',{}))[1]
            if control.get('name')!=name or 'required' in control:errors.append(f'{rel}: {control_id} must be an optional application detail')
        if by_id.get('career-email',('',{}))[1].get('type')!='email':errors.append(f'{rel}: careers email requires native email validation')
        if 'gmail.com' in by_id.get('career-email',('',{}))[1].get('pattern',''):errors.append(f'{rel}: careers must accept non-Gmail applicants')
        hidden={a.get('name'):a.get('value') for t,a in d.tags if t=='input' and a.get('type')=='hidden'}
        if hidden.get('_captcha')!='true' or '_next' in hidden:errors.append(f'{rel}: use provider verification and confirmation without a local success redirect')
        honey=by_id.get('career-honey',('',{}))[1]
        if honey.get('name')!='_honey' or honey.get('tabindex')!='-1':errors.append(f'{rel}: missing application honeypot')
        for control_id in ['career-errors','career-name-error','career-email-error','career-linkedin-error','career-portfolio-error','career-position-error','career-work-type-error']:
            if 'hidden' not in by_id.get(control_id,('',{}))[1]:errors.append(f'{rel}: application error must start hidden: {control_id}')
        expected_roles=['full-stack-engineer','marketing-specialist']
        role_links=[a for t,a in d.tags if t=='a' and 'data-career-role' in a]
        if [a['data-career-role'] for a in role_links]!=expected_roles or any(a.get('href')!='/careers/?role='+a['data-career-role']+'#apply' for a in role_links):errors.append(f'{rel}: careers role actions must retain exact role context')
        if not any(t=='a' and a.get('href')=='https://formsubmit.co/privacy.pdf' for t,a in d.tags):errors.append(f'{rel}: missing form-provider privacy disclosure')
        if not any(t=='a' and a.get('href','').startswith('mailto:careers@solarityai.com') for t,a in d.tags):errors.append(f'{rel}: missing founder-selected recruiting email alternative')
    if rel=='contact/index.html':
        # The contact page must lead to real destinations without a simulated form.
        for control_id,tag in {'prepare-inquiry':'section','contact-context':'p','contact-email':'a','data-note':'div'}.items():
            if by_id.get(control_id,('',{}))[0]!=tag:errors.append(f'{rel}: missing direct-contact control {control_id}')
        primary_email=by_id.get('contact-email',('',{}))[1].get('href','')
        if not primary_email.startswith('mailto:ata.turhan@solarityai.com?'):errors.append(f'{rel}: incorrect founder email destination')
        topics=[a for t,a in d.tags if t=='a' and a.get('data-inquiry-type')]
        if [a['data-inquiry-type'] for a in topics]!=['Investor','Program','Strategic partner','Product inquiry','Press','Other']:errors.append(f'{rel}: direct contact must retain all six inquiry types')
        if any(not a.get('href','').startswith('mailto:ata.turhan@solarityai.com?subject=') for a in topics):errors.append(f'{rel}: inquiry topics must work as native email links')
        if any(t=='form' for t,a in d.tags):errors.append(f'{rel}: direct contact should not imply an unconfigured submission form')
        if not any(t=='a' and a.get('href','').startswith('https://calendar.google.com/calendar/appointments/schedules/') for t,a in d.tags):errors.append(f'{rel}: missing verified booking alternative')
        if 'This website does not collect or submit contact messages.' not in text:errors.append(f'{rel}: missing truthful contact behavior disclosure')
    if rel=='investors-partners/index.html':
        if 'investor-questions' not in by_id:errors.append(f'{rel}: missing investor FAQ')
        if sum(t=='details' and 'faq-item' in a.get('class','').split() for t,a in d.tags)!=len(__import__('ux_content').FAQ):errors.append(f'{rel}: every FAQ entry needs a native disclosure')
    if rel=='404.html':
        if not any(t=='nav' and a.get('aria-label')=='More ways to continue' for t,a in d.tags):errors.append(f'{rel}: missing recovery navigation')
        for destination in ['/platform','/investors-partners','/contact']:
            if not any(t=='a' and a.get('href')==public_path(destination) for t,a in d.tags):errors.append(f'{rel}: missing recovery destination {destination}')

# Public discoverability must cover every real page without indexing the error document.
expected_public_urls={ORIGIN+public_path('/' if file==DIST/'index.html' else '/'+file.parent.relative_to(DIST).as_posix()) for file in docs if file!=DIST/'404.html'}
try:
    sitemap=ET.parse(DIST/'sitemap.xml')
    sitemap_urls=[node.text for node in sitemap.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    if len(sitemap_urls)!=len(set(sitemap_urls)):errors.append('Sitemap contains duplicate URLs')
    if set(sitemap_urls)!=expected_public_urls:errors.append('Sitemap must include every public content route exactly once and exclude the 404 page')
except (OSError,ET.ParseError) as exc:
    errors.append(f'Invalid or missing sitemap: {exc}')
try:
    robots=RobotFileParser();robots.parse((DIST/'robots.txt').read_text(encoding='utf-8').splitlines())
    if robots.site_maps()!=[ORIGIN+'/sitemap.xml']:errors.append('Robots must advertise the deployment-origin sitemap')
    for agent in ['*','Googlebot','Googlebot-Mobile','Bingbot']+seo.AI_CRAWLERS:
        if any(not robots.can_fetch(agent,url) for url in expected_public_urls):errors.append(f'Robots blocks a public content page for {agent}')
except OSError as exc:
    errors.append(f'Missing robots file: {exc}')
# Page markup lives in templates/ (templating.py). Component modules keep data and logic, not HTML elements;
# the icon path data in visual_sections.py and the FAQ answer snippets in ux_content.py are data.
for _module in sorted([ROOT/'build_site.py',ROOT/'product_story.py',ROOT/'saas_products.py',*ROOT.glob('visual_*.py'),ROOT/'ux_components.py']):
    _markup=re.findall(r'<(?:div|section|article|aside|header|footer|nav|main|p|span|a|h[1-6]|ul|ol|li|dl|dt|dd|img|picture|source|figure|figcaption|button|form|input|select|textarea|label|table|strong|em|small|br)[\s>/]',_module.read_text(encoding='utf-8'))
    if _markup:errors.append(f'{_module.name}: {len(_markup)} HTML elements in Python; page markup belongs in templates/')
for _template in sorted((ROOT/'templates').rglob('*')):
    if _template.is_file() and _template.suffix=='.j2' and bytes([13]) in _template.read_bytes():errors.append(f'{_template.relative_to(ROOT).as_posix()}: CRLF line endings change the generated HTML; use LF')
# Search and answer engines: titles, dates, schema.org graph, llms.txt and IndexNow.
lastmods={}
try:
    for node in ET.parse(DIST/'sitemap.xml').findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc=node.findtext('{http://www.sitemaps.org/schemas/sitemap/0.9}loc');mod=node.findtext('{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
        if not mod or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',mod):errors.append(f'Sitemap: {loc} needs a lastmod date')
        lastmods[loc]=mod
except (OSError,ET.ParseError):pass
for file,d in docs.items():
    rel=file.relative_to(DIST).as_posix();text=file.read_text(encoding='utf-8')
    title=html.unescape(''.join(d.title)).strip()
    if not 15<=len(title)<=65:errors.append(f'{rel}: title is {len(title)} characters; search results show about 60')
    if 'Solarity AI' not in title:errors.append(f'{rel}: title must name Solarity AI')
    desc=next((a.get('content','') for t,a in d.tags if t=='meta' and a.get('name')=='description'),'')
    if not 70<=len(html.unescape(desc))<=165:errors.append(f'{rel}: description is {len(html.unescape(desc))} characters; aim for 70-165')
    blocks=re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S)
    try:graph=[n for b in blocks for n in json.loads(b).get('@graph',[])]
    except ValueError as exc:errors.append(f'{rel}: invalid JSON-LD: {exc}');continue
    types={n.get('@type') for n in graph}
    org=next((n for n in graph if n.get('@type')=='Organization'),{})
    if not org.get('sameAs') or not org.get('description') or org.get('founder')!={'@id':seo.FOUNDER_ID}:errors.append(f'{rel}: Organization needs description, founder and official profiles')
    if 'Person' not in types or 'WebSite' not in types:errors.append(f'{rel}: schema.org graph needs the founder and the website')
    if rel=='404.html':continue
    url=ORIGIN+public_path('/' if file==DIST/'index.html' else '/'+file.parent.relative_to(DIST).as_posix())
    page=next((n for n in graph if n.get('@id')==url+'#webpage'),None)
    if not page:errors.append(f'{rel}: schema.org graph has no node for the page itself');continue
    if page.get('dateModified')!=lastmods.get(url):errors.append(f'{rel}: dateModified must match the sitemap lastmod')
    if page.get('name')!=title:errors.append(f'{rel}: schema.org page name must match the title')
    if url!=ORIGIN+'/' and 'BreadcrumbList' not in types:errors.append(f'{rel}: missing BreadcrumbList')
    ids=set(re.findall(r'"@type":\s*"[^"]+",\s*"@id":\s*"([^"]+)"',json.dumps(graph)))
    for ref in re.findall(r'"@id":\s*"([^"]+)"',json.dumps(graph)):
        if ref.startswith(ORIGIN) and ref not in ids and ref!=url+'#breadcrumb':errors.append(f'{rel}: schema.org reference to an undefined node {ref}')
    if '/apps/' in url and url!=ORIGIN+'/apps/':
        app=next((n for n in graph if n.get('@type')=='MobileApplication'),{})
        if len(app.get('sameAs',[]))!=2 or not app.get('featureList') or not app.get('alternateName'):errors.append(f'{rel}: MobileApplication needs store links, features and store name')
    for n in graph:
        for banned in ('aggregateRating','review','offers'):
            if banned in n:errors.append(f'{rel}: schema.org states {banned}, which the pages do not show')
for name in ('llms.txt','llms-full.txt'):
    llm=(DIST/name).read_text(encoding='utf-8') if (DIST/name).is_file() else ''
    if not llm.startswith('# Solarity AI\n\n> '):errors.append(f'{name}: must open with the llmstxt.org title and summary')
    for product in ['Looks Max','IQ Max','Sleep Max','Fitness Max','Only Fitness','Engineering Max','Management Max','Marketing Max']:
        if product not in llm:errors.append(f'{name}: missing {product}')
    for link in re.findall(r'\]\((https://solarityai\.com[^)]*)\)',llm):
        if link not in expected_public_urls and link!=ORIGIN+'/llms-full.txt':errors.append(f'{name}: links to {link}, which is not a public page')
if ((DIST/(seo.INDEXNOW_KEY+'.txt')).read_text(encoding='utf-8') if (DIST/(seo.INDEXNOW_KEY+'.txt')).is_file() else '')!=seo.INDEXNOW_KEY:errors.append('IndexNow key file must contain exactly its key')
header_rules={};current_rule=None
for line in (DIST/'_headers').read_text(encoding='utf-8').splitlines():
    if line and not line[0].isspace():
        current_rule=line;header_rules[current_rule]={}
    elif line.strip() and current_rule:
        name,value=line.strip().split(':',1);header_rules[current_rule][name.lower()]=value.strip()
if 'x-robots-tag' in header_rules.get('/*',{}):errors.append('Global crawler exclusion must not apply to public content')
for error_path in ['/404','/404.html']:
    if header_rules.get(error_path,{}).get('x-robots-tag')!='noindex, follow':errors.append(f'{error_path}: missing error-page noindex header')
# Security headers: a CSP that allows every inline script that runs by its hash, and no script wildcards.
global_headers=header_rules.get('/*',{})
csp=global_headers.get('content-security-policy','')
directives={part.split()[0]:part.split()[1:] for part in csp.split(';') if part.strip()}
if not csp:errors.append('_headers: missing Content-Security-Policy')
script_sources=directives.get('script-src',[])
if any(source in script_sources for source in ("'unsafe-inline'","'unsafe-eval'",'*','https:')):errors.append('CSP script-src must not allow inline, eval or wildcard scripts')
for directive,expected in (('object-src',["'none'"]),('base-uri',["'self'"]),('frame-ancestors',["'self'"])):
    if directives.get(directive)!=expected:errors.append(f'CSP must set {directive} {" ".join(expected)}')
if 'https://formsubmit.co' not in directives.get('form-action',[]):errors.append('CSP form-action must allow the careers form provider')
import base64 as _b64
for page in DIST.rglob('*.html'):
    for attrs,body in re.findall(r'<script([^>]*)>(.*?)</script>',page.read_text(encoding='utf-8'),re.S):
        if 'src=' in attrs or 'application/ld+json' in attrs:continue
        digest="'sha256-"+_b64.b64encode(sha256(body.encode('utf-8')).digest()).decode()+"'"
        if digest not in script_sources:errors.append(f'{page.relative_to(DIST).as_posix()}: inline script is not allowed by the CSP hash list')
# COOP stays off: it breaks Lighthouse and PageSpeed Insights traces (NO_NAVSTART) and the site opens no cross-origin popups.
if 'cross-origin-opener-policy' in global_headers:errors.append('_headers: Cross-Origin-Opener-Policy breaks PageSpeed Insights measurement; leave it off')
for name,expected in (('strict-transport-security','max-age=31536000'),):
    if global_headers.get(name)!=expected:errors.append(f'_headers: {name} must be {expected}')
if 'camera=()' not in global_headers.get('permissions-policy',''):errors.append('_headers: Permissions-Policy must disable unused device features')
fingerprinted_fonts=['/assets/fonts/'+font.name for font in (DIST/'assets/fonts').glob('*.woff2')]
for font_url in fingerprinted_fonts:
    font_file=DIST/font_url.lstrip('/')
    if not re.search(r'\.'+sha256(font_file.read_bytes()).hexdigest()[:12]+r'\.woff2$',font_url):errors.append(f'{font_url}: font hash does not match its content')
for asset_path in ['/assets/optimized/*','/assets/runtime/*']+fingerprinted_fonts:
    if header_rules.get(asset_path,{}).get('cache-control')!='public, max-age=31536000, immutable':errors.append(f'{asset_path}: missing immutable public cache directive')
for path,headers in header_rules.items():
    if 'immutable' in headers.get('cache-control','') and path not in ['/assets/optimized/*','/assets/runtime/*']+fingerprinted_fonts:errors.append(f'{path}: immutable caching must be scoped to fingerprinted assets')

# Links that open a new tab say so to assistive technology. Screenshot links open
# the in-page viewer and only fall back to a tab without JavaScript.
for file,d in docs.items():
    for attrs,label in re.findall(r'<a\b([^>]*)>(.*?)</a>',file.read_text(encoding='utf-8'),re.S):
        if 'target="_blank"' in attrs and 'screenshot-open' not in attrs and 'opens in a new tab' not in label:errors.append(f'{file.relative_to(DIST).as_posix()}: new-tab link does not announce it: {re.sub("<[^>]+>","",label).strip()[:40]}')

# ↗ means the link leaves the site; same-site links use → or an in-page ↓.
for file in docs:
    rel=file.relative_to(DIST).as_posix()
    for attrs,label in re.findall(r'<a\b([^>]*)>(.*?)</a>',file.read_text(encoding='utf-8'),re.S):
        href=re.search(r'\shref="([^"]*)"',' '+attrs)
        parts=urlsplit(href.group(1).replace('&amp;','&') if href else '')
        leaves=parts.scheme in ('mailto','tel') or (parts.scheme in ('http','https') and f'{parts.scheme}://{parts.netloc}'!=ORIGIN)
        if '↗' in label and not leaves:errors.append(f'{rel}: same-site link uses the external arrow: {parts.geturl()}')
        if leaves and parts.scheme!='mailto' and '↗' not in label:errors.append(f'{rel}: external link lacks the external arrow: {parts.geturl()}')

# dist/ is the publish set: every file must be a page, a host file, or referenced by a page.
HOST_FILES={'_headers','_redirects','robots.txt','sitemap.xml','llms.txt','llms-full.txt',seo.INDEXNOW_KEY+'.txt','favicon.ico','.well-known/security.txt','assets/fonts/OFL-Manrope.txt','assets/fonts/OFL-Newsreader.txt'}
# Legacy redirects, applied by Cloudflare Pages from dist/_redirects.
page_routes={'/' if f==DIST/'index.html' else '/'+f.parent.relative_to(DIST).as_posix()+'/' for f in docs if f!=DIST/'404.html'}
for line in (DIST/'_redirects').read_text(encoding='utf-8').splitlines() if (DIST/'_redirects').is_file() else ['missing']:
    parts=line.split()
    if len(parts)!=3 or parts[2]!='301':errors.append(f'_redirects: malformed rule {line!r}');continue
    old,new,_=parts
    if (DIST/old.lstrip('/')).exists():errors.append(f'_redirects: {old} shadows a published file')
    if new not in page_routes:errors.append(f'_redirects: {old} points to {new}, which is not a page')
referenced=set()
for file in docs:
    # A '*' marks a URL pattern (speculation rules), never a published file.
    referenced|={url.lstrip('/') for url in re.findall(r'(?:'+re.escape(ORIGIN)+r'|(?<![\w.-]))(/assets/[^"\'\s,)*]+)',file.read_text(encoding='utf-8'))}
# Home-screen icons: the official sun mark (make_app_icons.py).
for _icon in ('apple-touch-icon.png','icon-192.png'):
    if 'assets/icons/'+_icon not in referenced:errors.append(f'Pages must link /assets/icons/{_icon}')
_security=DIST/'.well-known/security.txt'
if not _security.is_file() or not re.search(r'^Contact: mailto:',_security.read_text(encoding='utf-8'),re.M) or not re.search(r'^Expires: 20\d\d-',_security.read_text(encoding='utf-8'),re.M):errors.append('.well-known/security.txt must name a contact and an expiry')
# RFC 9116: an expired security.txt must be treated as stale. Fail a month ahead so it is renewed in time.
import datetime as _dt
_expires=re.search(r'^Expires: (\d{4}-\d{2}-\d{2})',_security.read_text(encoding='utf-8'),re.M) if _security.is_file() else None
if _expires and _dt.date.fromisoformat(_expires.group(1))-_dt.date.today()<_dt.timedelta(days=30):errors.append(f'.well-known/security.txt expires {_expires.group(1)}; renew the date in build_site.py')

for file in sorted(DIST.rglob('*')):
    rel=file.relative_to(DIST).as_posix()
    if file.is_file() and file.suffix!='.html' and rel not in HOST_FILES and rel not in referenced:errors.append(f'Unreferenced file is published: {rel}')
for url in sorted(referenced):
    if not (DIST/url).is_file():errors.append(f'Referenced asset is missing from dist: /{url}')
favicon=DIST/'favicon.ico'
if not favicon.is_file() or favicon.read_bytes()[:4]!=b'\x00\x00\x01\x00':errors.append('Missing or invalid root favicon.ico')
for file,d in docs.items():
    if not any(t=='link' and a.get('rel')=='icon' and a.get('href')=='/favicon.ico' for t,a in d.tags):errors.append(f'{file.relative_to(DIST).as_posix()}: missing /favicon.ico icon link')

for attr,values in [('title',[''.join(d.title) for d in docs.values()]),('description',[next((a.get('content','') for t,a in d.tags if t=='meta' and a.get('name')=='description'),'') for d in docs.values()])]:
    if len(values)!=len(set(values)):errors.append(f'Duplicate {attr}')
bundle=BUNDLE
css=bundle.read_text(encoding='utf-8') if bundle.is_file() else ''
# Read the maintained build list, so newer styles cannot silently escape QA.
builder=ast.parse((ROOT/'build_site.py').read_text(encoding='utf-8'))
style_sources=next(ast.literal_eval(node.value) for node in builder.body if isinstance(node,ast.Assign) and any(isinstance(target,ast.Name) and target.id=='style_sources' for target in node.targets))
for source in style_sources:
    maintained_source=ROOT/source
    if not maintained_source.is_file():errors.append(f'Missing maintained stylesheet {source}')
    elif maintained_source.read_text(encoding='utf-8') not in css:errors.append(f'Presentation bundle is missing or has stale content from {source}')
# A line break that CSS hides at some widths must not join the adjacent words.
hidden_break_scopes=set(re.findall(r'\.([\w-]+)[^{}]*?\sbr(?::[\w-]+(?:\([^)]*\))?)?\s*\{\s*display\s*:\s*none',css))
for file in docs:
    rel=file.relative_to(DIST).as_posix();text=file.read_text(encoding='utf-8')
    for scope in sorted(hidden_break_scopes):
        for match in re.finditer(r'class="(?:[^"]*\s)?'+re.escape(scope)+r'(?:\s[^"]*)?"[^>]*>(.*?)</h[1-6]>',text,re.S):
            words=re.sub(r'<[^>]+>','',re.sub(r'<br\b[^>]*>','\0',match.group(1)))
            for joined in re.findall(r'\S+\0\S+',words):errors.append(f'{rel}: hidden line break joins words in .{scope}: {joined.replace(chr(0)," / ")}')
    # Display headings must be free to wrap: a non-breaking space pushed the FAQ heading out of its column.
    for level,heading in re.findall(r'<h([1-3])\b[^>]*>(.*?)</h\1>',text,re.S):
        if '&nbsp;' in heading or ' ' in heading:errors.append(f'{rel}: non-breaking space in an h{level} keeps it from wrapping: {re.sub("<[^>]+>","",heading)[:50]}')
# Copy is never cut to one line; only the browser-frame address label may end in an ellipsis.
for selector,body in re.findall(r'([^{}]+)\{([^{}]*text-overflow\s*:\s*ellipsis[^{}]*)\}',css):
    if selector.strip()!='.web-bar span':errors.append(f'Presentation CSS truncates text with an ellipsis: {selector.strip()[:60]}')
# Design tokens: small and body text use the type scale, three weights, and named radii.
for source in style_sources:
    rules=(ROOT/source).read_text(encoding='utf-8') if (ROOT/source).is_file() else ''
    screen=re.split(r'@media\s+print',rules)[0]
    for value in re.findall(r'font-size:\s*([^;}]+)',screen):
        literal=re.fullmatch(r'(\d*\.?\d+)(rem|px|em)',value.strip())
        if literal and (literal.group(2)!='rem' or float(literal.group(1))<1.33):errors.append(f'{source}: text size {value.strip()} must use a --text-* step')
    # Sizes come from the type roles in foundation.css (CINEMATIC_PREMIUM_PLAN.md §3.1); mono is retired.
    if source!='design/system/foundation.css' and re.search(r'font-size:\s*clamp\(',screen):errors.append(f'{source}: fluid font sizes belong to the --type-* tokens in foundation.css')
    if 'var(--font-mono)' in screen:errors.append(f'{source}: the monospace face is retired; use lining tabular numerals')
    for value in re.findall(r'(?<![\w-])font-weight:\s*([^;}]+)',screen):
        if value.strip() not in ('400','500','600','inherit','200 800'):errors.append(f'{source}: font weight {value.strip()} is outside the 400/500/600 system')
    for value in re.findall(r'border-radius:\s*([^;}]+)',screen):
        if not re.fullmatch(r'var\(--radius-(control|plate|panel|pill|icon)\)|0|50%|inherit',value.strip()):errors.append(f'{source}: radius {value.strip()} must use a --radius-control/plate/panel/pill/icon token')
    # Colors live in foundation.css tokens; borders, outlines and shadows never hard-code a hex value.
    if source!='design/system/foundation.css':
        for prop,value in re.findall(r'(?<![\w-])((?:border|outline|box-shadow)[\w-]*)\s*:\s*([^;}]+)',screen):
            if re.search(r'#[0-9a-fA-F]{3,8}\b',value):errors.append(f'{source}: {prop} uses a literal color ({value.strip()[:40]}); use a foundation token')
    for selector,body in re.findall(r'([^{}]*\.eyebrow[^{}]*)\{([^}]*)\}',screen):
        if selector.strip()!='.eyebrow' and '.product-identity' not in selector and ':not(.eyebrow)' not in selector and re.search(r'font-size|letter-spacing',body):errors.append(f'{source}: eyebrow size and tracking belong to the base .eyebrow style ({selector.strip()[:60]})')
# Contrast matrix over the declared tokens (CINEMATIC_PREMIUM_PLAN.md §3.2 and correction 6).
foundation_css=(ROOT/'design/system/foundation.css').read_text(encoding='utf-8')
root_match=re.search(r':root\{(.*?)\}',foundation_css,re.S)
# A page's opening is on the first screen: deferring it with content-visibility gives it a placeholder size and shifts the page.
if 'main>section:not(:first-child):not(.breadcrumbs + section)' not in foundation_css:
    errors.append('design/system/foundation.css: the opening after a breadcrumb trail must be exempt from content-visibility')
tokens=dict(re.findall(r'--([\w-]+):([^;]+)',root_match.group(1))) if root_match else {}
def token_hex(name,seen=()):
    value=tokens.get(name,'').strip()
    ref=re.fullmatch(r'var\(--([\w-]+)\)',value)
    if ref and ref.group(1) not in seen:return token_hex(ref.group(1),seen+(name,))
    return value.lower() if re.fullmatch(r'#[0-9a-fA-F]{6}',value) else None
def rgb(hex_value):return tuple(int(hex_value[i:i+2],16) for i in (1,3,5))
def luminance(color):
    channels=[c/255 for c in color]
    channels=[c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4 for c in channels]
    return .2126*channels[0]+.7152*channels[1]+.0722*channels[2]
def contrast(a,b):
    la,lb=sorted((luminance(a),luminance(b)),reverse=True)
    return (la+.05)/(lb+.05)
def blend(top,bottom,alpha):return tuple(round(top[i]*alpha+bottom[i]*(1-alpha)) for i in range(3))
CONTRAST_PAIRS=[(fg,bg,4.5) for fg in ['text','muted','dim'] for bg in ['bg','surface','raised','tone-blue','tone-first','tone-golden','tone-footer']]
CONTRAST_PAIRS+=[(fg,bg,4.5) for fg in ['sun-core','gold','sand'] for bg in ['bg','surface','raised','tone-golden']]
CONTRAST_PAIRS+=[('ink','sun-core',4.5),('ink','haze',4.5),('bronze','bg',3),('bronze','surface',3),('danger-text','danger-surface',4.5),('danger-ink','danger-surface',4.5),('notice-text','notice-surface',4.5)]
for fg,bg,minimum in CONTRAST_PAIRS:
    a,b=token_hex(fg),token_hex(bg)
    if not a or not b:errors.append(f'Contrast matrix: --{fg} or --{bg} is not a six-digit hex token');continue
    ratio=contrast(rgb(a),rgb(b))
    if ratio<minimum:errors.append(f'Contrast matrix: --{fg} on --{bg} is {ratio:.2f}:1, below {minimum}:1')
# Text inside a product world sits on its deep stage or on at most 35% world light over it, never on the vivid hue.
for product in ['looks','iq','sleep','fitness']:
    deep,world,tint=(token_hex(f'{product}-{part}') for part in ('deep','world','tint'))
    if not (deep and world and tint):errors.append(f'Contrast matrix: --{product}-deep/world/tint must be hex tokens');continue
    for surface_name,surface in [('deep',rgb(deep)),('35% world',blend(rgb(world),rgb(deep),.35))]:
        # --dim is never used inside a lit world stage; it is checked only on the deep surface.
        for fg in ['text','muted']+(['dim'] if surface_name=='deep' else []):
            ratio=contrast(rgb(token_hex(fg)),surface)
            if ratio<4.5:errors.append(f'Contrast matrix: --{fg} on {product} {surface_name} is {ratio:.2f}:1, below 4.5:1')
        ratio=contrast(rgb(tint),surface)
        if ratio<4.5:errors.append(f'Contrast matrix: --{product}-tint on {product} {surface_name} is {ratio:.2f}:1, below 4.5:1')
# Warm neutrals stay on the ember axis (R >= G >= B); cool scene tones stay blue (B >= G >= R), never olive.
for name in ['bg','surface','raised','line','line-soft','ink','tone-base','tone-first','tone-golden','tone-footer']:
    value=token_hex(name)
    if value and not rgb(value)[0]>=rgb(value)[1]>=rgb(value)[2]:errors.append(f'Color axis: --{name} {value} must satisfy R >= G >= B')
for name in ['tone-night','tone-blue']:
    value=token_hex(name)
    if value and not rgb(value)[2]>=rgb(value)[1]>=rgb(value)[0]:errors.append(f'Color axis: --{name} {value} must satisfy B >= G >= R')
if re.search(r'--paper',css):errors.append('Paper surfaces are retired; use the lit panel or outline register')
# Motion is opt-in: keyframes and scroll-driven animations live only under prefers-reduced-motion: no-preference,
# and the hero artwork is never animated.
for css_file in sorted((ROOT/'design/system').glob('*.css')):
    css_text=re.sub(r'/\*.*?\*/','',css_file.read_text(encoding='utf-8'),flags=re.S)
    stack=[];prelude_start=0
    for index,char in enumerate(css_text):
        if char=='{':stack.append(css_text[prelude_start:index].strip());prelude_start=index+1
        elif char=='}':
            if stack:stack.pop()
            prelude_start=index+1
        elif char==';':prelude_start=index+1
        if css_text.startswith('@keyframes',index) or css_text.startswith('animation-timeline',index):
            guarded=any(re.search(r'prefers-reduced-motion:\s*no-preference',p) for p in stack)
            if not guarded:errors.append(f'{css_file.name}: animation outside the prefers-reduced-motion: no-preference guard')
    if re.search(r'(solar-hero-art|progress-hero-image)[^{}]*\{[^}]*animation',css_text):errors.append(f'{css_file.name}: the hero artwork must not be animated')
# Fonts: every route stays within the 60 KiB budget, and display headings only use glyphs the subset carries.
font_sources=json.loads((ROOT/'source-assets/fonts/font-sources.json').read_text(encoding='utf-8'))
FONT_BUDGET=font_sources.get('route_budget_bytes',61440)
def unicode_ranges(spec):
    ranges=[]
    for part in spec.split(','):
        low,_,high=part.strip().removeprefix('U+').partition('-')
        ranges.append((int(low,16),int(high or low,16)))
    return ranges
display_ranges=unicode_ranges(font_sources['display']['unicode_ranges'])+[(0x2190,0x2193),(0x2197,0x2197)]
for file,d in docs.items():
    rel=file.relative_to(DIST).as_posix();text=file.read_text(encoding='utf-8')
    fonts=set(re.findall(r'/assets/fonts/[\w.-]+\.woff2',text))
    total=sum((DIST/font.lstrip('/')).stat().st_size for font in fonts if (DIST/font.lstrip('/')).is_file())
    if total>FONT_BUDGET:errors.append(f'{rel}: font files total {total} bytes, over the {FONT_BUDGET}-byte route budget')
    for heading in re.findall(r'<h[12]\b[^>]*>(.*?)</h[12]>',text,re.S):
        for char in set(html.unescape(re.sub(r'<[^>]+>','',heading))):
            if ord(char)>32 and not any(low<=ord(char)<=high for low,high in display_ranges):errors.append(f'{rel}: heading character {char!r} (U+{ord(char):04X}) is outside the display subset')
# Screenshot derivatives carry no baked-in listing hairlines (CINEMATIC_PREMIUM_PLAN.md P5a).
try:
    from PIL import Image as _Image
    import optimize_images as _oi
    _manifest=json.loads((ROOT/'research-assets/image-optimization.json').read_text(encoding='utf-8'))
    for _source,_record in _manifest['images'].items():
        if _record.get('role')!='screen':continue
        if 'crop' not in _record:errors.append(f'{_source}: image manifest is missing its edge-crop record')
        for _variant in _record['webp']+_record.get('avif',[]):
            _file=DIST/_variant['url'].lstrip('/')
            if not _file.is_file():continue
            with _Image.open(_file) as _image:
                _rgb=_image.convert('RGB');_band=_oi.derivative_edge_band(_rgb.width,_record['derivative_width'])
                _worst=max(_oi.edge_difference(_rgb,_side,band=_band) for _side in ('left','top','right','bottom'))
            if _worst>_oi.EDGE_LIMIT:errors.append(f'{_variant["url"]}: outer edge differs from the interior by {_worst:.0f} levels (limit {_oi.EDGE_LIMIT})')
except ImportError:
    warnings.append('Pillow is unavailable; screenshot edge check skipped')
except (OSError,ValueError,KeyError) as _exc:
    errors.append(f'Screenshot edge check could not run: {_exc}')
for breakpoint in [1150,850,560]:
    if f'max-width:{breakpoint}px' not in css:warnings.append(f'Missing expected CSS breakpoint {breakpoint}')
if 'prefers-reduced-motion:reduce' not in css:errors.append('Missing reduced-motion rule')
if ':focus-visible' not in css:errors.append('Missing explicit focus-visible rule')
report={'pages':len(docs),'internal_links_and_fragments_checked':links_checked,'local_asset_references_checked':assets_checked,'errors':errors,'warnings':warnings,'scope':'Static HTML, generated routes/fragments/assets, metadata, labels and CSS source checks. No browser, measured layout, contact delivery, HTTP routing, or performance results.'}
print(json.dumps(report,indent=2))
(ROOT/'static-audit.json').write_text(json.dumps(report,indent=2), encoding='utf-8', newline='\n')
raise SystemExit(bool(errors))
