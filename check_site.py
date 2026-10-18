"""Static artifact audit only. Does not run a server or claim browser coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from collections import Counter
import ast,json,re
from hashlib import sha256
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
from site_urls import public_path

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
    if canonical!=[expected_url]:errors.append(f'{rel}: unexpected canonical {canonical}')
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
    actual_scripts=[]
    for script in runtime_scripts:
        match=re.fullmatch(r'/assets/runtime/(gallery|contact|careers)\.([a-f0-9]{12})\.js',script)
        if not match:errors.append(f'{rel}: unexpected runtime script {script}');continue
        actual_scripts.append(match.group(1))
        script_file=DIST/script.lstrip('/')
        if script_file.is_file() and sha256(script_file.read_bytes()).hexdigest()[:12]!=match.group(2):errors.append(f'{rel}: script filename hash does not match its content')
    if actual_scripts!=expected_scripts:errors.append(f'{rel}: incorrect route-specific scripts {actual_scripts}')
    startup=re.search(r'<script\b[^>]*id="navigation-startup"[^>]*>(.*?)</script>',text,re.S)
    navigation_source=(ROOT/'scripts/navigation.js').read_text(encoding='utf-8')
    startup_tags=[a for t,a in d.tags if t=='script' and a.get('id')=='navigation-startup']
    if len(startup_tags)!=1 or not startup or startup.group(1)!=navigation_source:
        errors.append(f'{rel}: missing or stale inline navigation startup')
    elif startup.end()>text.index('<style id="page-styles"') or startup.end()>text.index('</head>'):
        errors.append(f'{rel}: navigation layout must be selected before styles and body painting')
    if startup_tags and (any(key in startup_tags[0] for key in ['src','defer','async']) or startup_tags[0].get('type','') not in ['', 'text/javascript']):
        errors.append(f'{rel}: navigation startup must execute synchronously without a network dependency')
    if startup_tags and startup_tags[0].get('data-source-sha256')!=sha256(navigation_source.encode()).hexdigest():
        errors.append(f'{rel}: stale navigation source hash')
    expected_robots={'noindex','follow'} if rel=='404.html' else {'index','follow'}
    actual_robots={directive.strip().lower() for directive in meta.get('robots','').split(',')}
    if actual_robots!=expected_robots:errors.append(f'{rel}: incorrect public-site indexing directive {meta.get("robots", "")}')
    for t,a in d.tags:
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
    if rel=='index.html':
        previews=[a for t,a in d.tags if t=='input' and a.get('name')=='portfolio-preview']
        if len(previews)!=4 or any(a.get('type')!='radio' for a in previews):errors.append(f'{rel}: portfolio preview must use four native radios')
        if [a.get('value') for a in previews if 'checked' in a]!=['looks-max']:errors.append(f'{rel}: native product preview must have one initial selection')
        for control in previews:
            target=by_id.get(control.get('aria-controls'),('',{}))
            if target[0]!='article' or 'explorer-panel' not in target[1].get('class','').split():errors.append(f'{rel}: product preview must control its own semantic panel')
            if sum(t=='label' and a.get('for')==control.get('id') for t,a in d.tags)!=1:errors.append(f'{rel}: product preview must have exactly one associated label')
            if '#'+control.get('id','')+':checked~.explorer-layout' not in text:errors.append(f'{rel}: product selector lost its CSS-only behavior during optimization')
        hero_links=[a.get('href') for t,a in d.tags if t=='a' and 'hero-product' in a.get('class','').split()]
        if hero_links!=['/apps/looks-max/','/apps/iq-max/','/apps/sleep-max/','/apps/fitness-max/']:errors.append(f'{rel}: hero must feature only the four verified store-listed apps')
        primary_images=[a for t,a in d.tags if t=='img' and 'progress-hero-image' in a.get('class','').split()]
        hero_sources=[a for t,a in d.tags if t=='source' and a.get('type')=='image/avif' and 'solar-ascent-' in a.get('srcset','')]
        if len(primary_images)!=1 or 'solar-ascent-' not in primary_images[0].get('src',''):errors.append(f'{rel}: hero must use the founder-approved atmospheric sunrise artwork')
        if primary_images and (primary_images[0].get('width')!='1860' or primary_images[0].get('height')!='845'):errors.append(f'{rel}: hero must reserve the correct intrinsic dimensions')
        if len(primary_images)!=1 or primary_images[0].get('loading')!='eager' or primary_images[0].get('fetchpriority')!='high':errors.append(f'{rel}: hero artwork must load eagerly at high priority')
        if len(hero_sources)!=1 or not primary_images or hero_sources[0].get('sizes')!=primary_images[0].get('sizes'):errors.append(f'{rel}: hero AVIF and WebP must share the rendered image-size contract')
        if 'Conceptual brand artwork' not in text:errors.append(f'{rel}: hero must identify its illustrative role')
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
        expected_roles=['full-stack-engineer','marketing-specialist','business-development-manager']
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
        if [a['data-inquiry-type'] for a in topics]!=['Investor','Strategic partner','Product inquiry','Other']:errors.append(f'{rel}: direct contact must retain all four inquiry types')
        if any(not a.get('href','').startswith('mailto:ata.turhan@solarityai.com?subject=') for a in topics):errors.append(f'{rel}: inquiry topics must work as native email links')
        if any(t=='form' for t,a in d.tags):errors.append(f'{rel}: direct contact should not imply an unconfigured submission form')
        if not any(t=='a' and a.get('href','').startswith('https://calendar.google.com/calendar/appointments/schedules/') for t,a in d.tags):errors.append(f'{rel}: missing verified booking alternative')
        if 'This website does not collect or submit contact messages.' not in text:errors.append(f'{rel}: missing truthful contact behavior disclosure')
    if rel=='investors-partners/index.html':
        if 'investor-questions' not in by_id:errors.append(f'{rel}: missing investor FAQ')
        if sum(t=='details' and 'faq-item' in a.get('class','').split() for t,a in d.tags)!=5:errors.append(f'{rel}: expected five native FAQ disclosures')
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
    for agent in ['*','Googlebot','Googlebot-Mobile']:
        if any(not robots.can_fetch(agent,url) for url in expected_public_urls):errors.append(f'Robots blocks a public content page for {agent}')
except OSError as exc:
    errors.append(f'Missing robots file: {exc}')
header_rules={};current_rule=None
for line in (DIST/'_headers').read_text(encoding='utf-8').splitlines():
    if line and not line[0].isspace():
        current_rule=line;header_rules[current_rule]={}
    elif line.strip() and current_rule:
        name,value=line.strip().split(':',1);header_rules[current_rule][name.lower()]=value.strip()
if 'x-robots-tag' in header_rules.get('/*',{}):errors.append('Global crawler exclusion must not apply to public content')
for error_path in ['/404','/404.html']:
    if header_rules.get(error_path,{}).get('x-robots-tag')!='noindex, follow':errors.append(f'{error_path}: missing error-page noindex header')
fingerprinted_fonts=['/assets/fonts/'+font.name for font in (DIST/'assets/fonts').glob('*.woff2')]
for font_url in fingerprinted_fonts:
    font_file=DIST/font_url.lstrip('/')
    if not re.search(r'\.'+sha256(font_file.read_bytes()).hexdigest()[:12]+r'\.woff2$',font_url):errors.append(f'{font_url}: font hash does not match its content')
for asset_path in ['/assets/optimized/*','/assets/runtime/*']+fingerprinted_fonts:
    if header_rules.get(asset_path,{}).get('cache-control')!='public, max-age=31536000, immutable':errors.append(f'{asset_path}: missing immutable public cache directive')
for path,headers in header_rules.items():
    if 'immutable' in headers.get('cache-control','') and path not in ['/assets/optimized/*','/assets/runtime/*']+fingerprinted_fonts:errors.append(f'{path}: immutable caching must be scoped to fingerprinted assets')

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
HOST_FILES={'_headers','robots.txt','sitemap.xml','favicon.ico','assets/fonts/OFL-Manrope.txt'}
referenced=set()
for file in docs:
    referenced|={url.lstrip('/') for url in re.findall(r'(?:'+re.escape(ORIGIN)+r'|(?<![\w.-]))(/assets/[^"\'\s,)]+)',file.read_text(encoding='utf-8'))}
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
for breakpoint in [1150,850,560]:
    if f'max-width:{breakpoint}px' not in css:warnings.append(f'Missing expected CSS breakpoint {breakpoint}')
if 'prefers-reduced-motion:reduce' not in css:errors.append('Missing reduced-motion rule')
if ':focus-visible' not in css:errors.append('Missing explicit focus-visible rule')
report={'pages':len(docs),'internal_links_and_fragments_checked':links_checked,'local_asset_references_checked':assets_checked,'errors':errors,'warnings':warnings,'scope':'Static HTML, generated routes/fragments/assets, metadata, labels and CSS source checks. No browser, measured layout, contact delivery, HTTP routing, or performance results.'}
print(json.dumps(report,indent=2))
(ROOT/'static-audit.json').write_text(json.dumps(report,indent=2), encoding='utf-8', newline='\n')
raise SystemExit(bool(errors))
