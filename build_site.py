from pathlib import Path
import base64, hashlib, json, re, shutil
from urllib.parse import urlencode
from ux_components import app_breadcrumbs, related_apps, page_breadcrumbs
from image_provenance import provenance
from ux_content import investor_faq, recovery_links
from visual_home import hero_section, closing_scene
from visual_saas import saas_wall, saas_chapters, apps_web_band
from saas_products import SAAS
from visual_sections import feature_grid, founder_card
from visual_team import selected_team, TEAM_MEMBERS
from company_facts import TEAM_DETAILS
from visual_careers import careers_page
from visual_contact import contact_page, founder_vcard
from visual_chrome import site_header, site_footer
from visual_stage import store_badges
from visual_products import product_art, product_page
from visual_catalog import portfolio_page, portfolio_wall
from visual_company_upgrade import strategy_story, investor_evidence, investor_opening, operating_principles, founder_booking, section_index
from visual_strategy import platform_opening
from visual_record import shipping_record, founder_record, program_brief, record_summary, long_date, app_compare, web_compare, company_facts
from visual_press import press_page, press_kit_zip
from visual_policies import accessibility_page, website_data_page
import seo
from templating import render
from optimize_images import ensure_optimized_images, image_record, write_favicon
from performance_build import optimize_page, RUNTIME, WRITTEN_RUNTIME
from site_urls import public_path, normalize_page_links

ROOT = Path(__file__).parent
DIST = ROOT / 'dist'
SOURCE_ASSETS = ROOT / 'source-assets'
ORIGIN = 'https://solarityai.com'
EMAIL = 'ata.turhan@solarityai.com'
FONT_URL = '/assets/fonts/manrope-latin-variable.cfa570d7c3ee.woff2'
DISPLAY_FONT_URL = '/assets/fonts/newsreader-display-latin.16985410e5b5.woff2'
BOOKING = 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ2qgXk0ZfBd6QJf7ef-306in7AI0Kzc-pL3NJFK1fU74vAUGiftVJPF3-DoXp9_RZoyqW_sjSpI'

APPS = [
 dict(slug='looks-max',seo_title='Looks Max: AI face analysis and self-care app',seo_description='Looks Max is an AI appearance and self-care app for iOS and Android: AI facial assessments, personalized grooming suggestions, and a progress journal.',crop_focus='50% 64%',name='Looks Max',category='Appearance & self-care',color='lavender',headline='A more considered approach to self-care.',summary='Personalized appearance insights, daily habits, and a place to follow your progress.',intro='For people making grooming and self-care part of their daily routine. Looks Max brings facial analysis and personalized guidance into a single app.',features=[('Understand your starting point','Explore AI-generated facial assessments and breakdowns across appearance categories.'),('Turn insights into habits','Find personalized grooming suggestions and daily habits you can return to.'),('Keep a record of progress','Use the activity calendar and journal to follow your own routine over time.')],screen='looks-max-screen-4.webp',apple='https://apps.apple.com/us/app/looks-max-look-your-best/id6778990308',google='https://play.google.com/store/apps/details?id=com.solarityai.onlylooksmax',note='Appearance scores are app-generated assessments, not objective measures of personal worth or promises of a particular result.'),
 dict(slug='iq-max',seo_title='IQ Max: daily cognitive exercises app',seo_description='IQ Max is a cognitive practice app for iOS and Android: daily exercises for memory, reaction time, and attention, with adaptive difficulty, stars, and streaks.',crop_focus='50% 68%',hero_screen='iq-max-detail-screen-4.webp',hero_alt='IQ Max official App Store imagery showing the focus selection with memory, processing speed, focus, and overall thinking options.',name='IQ Max',category='Cognitive practice',color='blue',headline='Make room for a daily mental challenge.',summary='Focused cognitive exercises, adaptive difficulty, and a daily routine you control.',intro='For curious people who enjoy a structured mental challenge. Choose exercises, practice regularly, and follow your performance across sessions.',features=[('Choose your daily practice','Explore exercises involving memory, reaction time, and attention.'),('Keep the challenge moving','Adaptive difficulty adjusts the challenge as you practice.'),('See your consistency','Session results, stars, and streaks make your practice visible.')],screen='iq-max-screen-1.webp',apple='https://apps.apple.com/us/app/iq-max-smarter-every-day/id6803826639',google='https://play.google.com/store/apps/details?id=com.solarityai.iqmax',note='Exercise scores describe performance within the app. They are not a clinical assessment or a guarantee of increased intelligence.'),
 dict(slug='sleep-max',factory_note=('Engineering Max, the app engineering web app from Solarity AI, was tested first on Sleep Max.','/platform#engineering-max','See Engineering Max'),seo_title='Sleep Max: sleep diary and AI sleep coach app',seo_description='Sleep Max is a sleep app for iOS and Android: a sleep diary with an app-generated Sleep Score, habit tracking, soundscapes, and an AI sleep coach.',crop_focus='50% 22%',name='Sleep Max',category='Sleep & daily routines',color='indigo',headline='Bring intention to the end of your day.',summary='A sleep diary, habit tracking, and coaching to support a more consistent routine.',intro='For people who want to pay closer attention to their sleep habits. Sleep Max combines personal logging with guidance and tools for winding down.',features=[('Reflect on your nights','Record sleep in a diary and review your app-generated Sleep Score.'),('Build a regular routine','Follow habits, activity, and streaks as part of your personal practice.'),('Make space to wind down','Explore soundscapes and an AI sleep coach for general guidance.')],screen='sleep-max-screen-4.webp',apple='https://apps.apple.com/us/app/sleep-max-rest-best/id6806709872',google='https://play.google.com/store/apps/details?id=com.solarityai.sleepmax',note='Sleep Max is presented here as a general wellness product. Its guidance does not replace individual medical assessment.'),
 dict(slug='fitness-max',seo_title='Fitness Max: AI fitness and nutrition coach',seo_description='Fitness Max, listed in the app stores as Only Fitness, is an AI fitness and nutrition app: photo meal analysis, voice or text logging, and AI coaching.',crop_focus='50% 72%',name='Fitness Max',category='Fitness & nutrition',color='amber',headline='Build a routine you can follow.',summary='Meal insights, training logs, and AI coaching to help you follow your fitness routine.',intro='For people bringing more consistency to training and nutrition. Log your day, explore meal insights, and review progress with goal-focused AI coaching.',features=[('Log your day in your own words','Use voice or text to record training, sleep, and daily updates.'),('Explore your meals','Photo-based meal analysis provides estimated nutrition information to support your food log.'),('Follow your progress','Review coaching reports and progress photos as you work toward your own goals.')],screen='fitness-max-screen-2.webp',screen_width=600,screen_height=1298,store_name='Only Fitness',apple='https://apps.apple.com/us/app/only-fitness-ai-coach/id6789095658',google='https://play.google.com/store/apps/details?id=com.solarityai.onlyfitness',note='Fitness Max is listed in app stores as Only Fitness. Nutrition estimates and AI coaching are general guidance, not medical advice or a guarantee of fitness results.')
]

def contact(kind='Other', product=None):
    return '/contact?' + urlencode({'type':kind, **({'product':product} if product else {})}) + '#prepare-inquiry'

# btn() and product_status() return plain strings: the component modules concatenate them with other strings.
def btn(label,href,style='primary',external=False):
    leaves_site = external or href.startswith(('http','mailto:'))
    return str(render('build_site/button.html.j2',label=label,href=href,style=style,external=external,leaves_site=leaves_site))

def product_status(a,full=False):
    return str(render('build_site/product_status.html.j2',app=a,full=full))

def app_art(a,small=False):
    return product_art(a,small)

def cta(title='A conversation with possibility.',desc='For investors and partners who see the potential in thoughtful consumer products and the systems behind them.',lead='investor',overview=False):
    return closing_scene(title, desc, contact, lead, overview)

def social_for(path):
    """The link-preview image for a route (make_social_images.py), and its alt text."""
    by_slug={a['slug']:a for a in APPS}
    if path.startswith('/apps/') and path[6:] in by_slug:
        a=by_slug[path[6:]]
        return f'social/{a["slug"]}.jpg', f'{a["name"]}, {a["category"]}: the app icon beside official App Store imagery'
    return {'/apps':('social/apps.jpg','The 4 Solarity AI app icons'),
            '/platform':('social/platform.jpg','Engineering Max, Management Max, and Marketing Max product screens'),
            '/investors-partners':('social/investors.jpg','The 4 Solarity AI app icons')}.get(
            path,('social/default.jpg','A person climbing mountain steps toward a golden sunrise above the clouds'))

NAV=[('/apps','Apps'),('/platform','Platform'),('/company','Company'),('/investors-partners','Investors & Partners'),('/careers','Careers')]
# The team for search and AI answers: the roster, roles and LinkedIn shown on Company, with the 480w portrait.
TEAM=[{**m,**TEAM_DETAILS.get(m['name'],{}),'image':next((v['url'] for v in (image_record(m['portrait']) or {}).get('webp',[]) if v['width']==480),'')} for m in TEAM_MEMBERS]
def shell(path,title,desc,body):
    """The complete document, as a plain string for the link and delivery passes that follow."""
    social_image, social_alt = social_for(path)
    from ux_content import FAQ
    full_title=title if 'Solarity AI' in title else title+' | Solarity AI'
    app=next((a for a in APPS if path=='/apps/'+a['slug'] and a.get('apple')),None)
    app_store_id=re.search(r'/id(\d+)',app['apple']).group(1) if app else ''
    data=seo.graph(path,full_title,desc,apps=APPS,saas=SAAS,faq=FAQ,email=EMAIL,logo='/assets/brand/solarity-sun-320.2513ba060440.webp',
                   portrait='/assets/brand/ata-turhan-640.742556487789.webp',social_image=social_image,modified=PAGE_DATES[path],team=TEAM)
    return str(render('build_site/shell.html.j2',path=path,full_title=full_title,desc=desc,body=body,app_store_id=app_store_id,
                      robots='noindex,follow' if path=='/404' else 'index,follow,max-image-preview:large',url=ORIGIN+public_path(path),origin=ORIGIN,
                      social_image=social_image,social_alt=social_alt,font_url=FONT_URL,display_font_url=DISPLAY_FONT_URL,
                      header=site_header(path,NAV,btn),provenance=provenance(),footer=site_footer(EMAIL,path,BOOKING,long_date(PAGE_DATES[path]),PAGE_DATES[path]),json_ld=seo.script_json(data)))

def page(name,**context):
    """A page body from templates/build_site/pages/, as a plain string for the page records."""
    return str(render(f'build_site/pages/{name}.html.j2',apps=APPS,saas=SAAS,btn=btn,contact=contact,cta=cta,**context))

# Page bodies stay plain strings: seo.page_dates() hashes them together with the title and description.
pages={}
pages['/']=('Solarity AI: AI-powered self-improvement apps and web apps','Solarity AI builds AI self-improvement apps for iOS and Android, Looks Max, IQ Max, Sleep Max, and Fitness Max, and 3 web apps for building mobile products.',
            page('home',hero_section=hero_section,portfolio_wall=portfolio_wall,shipping_record=shipping_record,saas_wall=saas_wall))

pages['/apps']=('AI self-improvement apps for iOS and Android','Discover Looks Max, IQ Max, Sleep Max, and Fitness Max, and the Engineering Max, Management Max, and Marketing Max web apps from Solarity AI.',
                page('apps',app_compare=app_compare,portfolio_page=portfolio_page,app_art=app_art,product_status=product_status,apps_web_band=apps_web_band))

for a in APPS:
    status=product_status(a,True)
    stores=store_badges(a, btn('Ask about '+a['name'],contact('Product inquiry',a['name'])))
    features=feature_grid(a)
    pages['/apps/'+a['slug']]=(a['seo_title'],a['seo_description'],str(product_page(a,APPS,btn,contact,stores,status,features,app_breadcrumbs(a),related_apps(a,APPS))))

pages['/platform']=('Engineering Max, Management Max, Marketing Max','Engineering Max, Management Max, and Marketing Max: 3 Solarity AI web apps for engineering, managing, and marketing mobile products.',
                    page('platform',web_compare=web_compare,platform_opening=platform_opening,saas_chapters=saas_chapters,strategy_story=strategy_story))

pages['/company']=('About Solarity AI and founder Ata Turhan','Solarity AI LLC was founded by Ata Turhan in Irving, Texas. Meet the founder and the team building self-improvement apps and web apps for mobile products.',
                   page('company',record=record_summary(),company_facts=company_facts,email=EMAIL,founder_card=founder_card,founder_record=founder_record,selected_team=selected_team,operating_principles=operating_principles))

pages['/investors-partners']=('Invest in or partner with Solarity AI','Explore the Solarity AI product thesis and opportunities for investment, distribution, technology collaboration, and platform design partnerships.',
                              page('investors_partners',investor_opening=investor_opening,section_index=section_index,shipping_record=shipping_record,program_brief=program_brief,investor_evidence=investor_evidence,investor_faq=investor_faq,founder_booking=founder_booking,booking=BOOKING))

pages['/careers']=('Solarity AI careers: remote engineering and marketing roles','Fully remote engineering and marketing roles at Solarity AI: full-time, part-time, or internship, with profit sharing. Help build focused AI-powered apps.',str(careers_page(btn)))

pages['/press']=('Solarity AI press kit: descriptions, facts, and images','Approved descriptions, company facts, the Solarity AI sun mark, founder portrait, and app icons for articles, program pages, and event listings.',press_page(APPS,EMAIL,btn))

pages['/accessibility']=('Accessibility statement','How solarityai.com is built and checked to meet WCAG 2.2 level AA, its known limitations, and how to report an accessibility problem.',accessibility_page(EMAIL))

pages['/website-data']=('How the Solarity AI website handles data','What solarityai.com collects and does not: no cookies, cookieless page counts, email links, the careers form provider, hosting, and security.',website_data_page(EMAIL,APPS))

pages['/contact']=('Contact Solarity AI and founder Ata Turhan','Contact Solarity AI about investment, strategic partnerships or its consumer apps. Reach founder Ata Turhan directly.',str(contact_page(EMAIL,BOOKING,btn)))
pages['/404']=('Page not found','This page is not here. Find your way back to Solarity AI’s apps, app factory platform, company story, investor information, or contact page.',page('not_found',recovery_links=recovery_links,
    routes=json.dumps([[public_path(p),'Home' if p=='/' else next((a['name'] for a in APPS if p=='/apps/'+a['slug']),seo.CRUMB_NAMES.get(p,''))] for p in pages if p!='/404'],ensure_ascii=False,separators=(',',':'))))

style_sources=['design/system/foundation.css', 'design/system/chrome.css', 'design/system/home.css', 'design/system/products.css', 'design/system/company.css', 'design/system/contact.css', 'design/system/careers.css', 'design/system/accessibility.css']
source_css='\n'.join((ROOT/name).read_text(encoding='utf-8') for name in style_sources)
# Generated bundle for build hashing only; pages inline route-specific CSS.
(ROOT/'design/presentation.css').write_text(source_css, encoding='utf-8', newline='\n')
image_manifest=ensure_optimized_images()
write_favicon(DIST/'favicon.ico')
performance_metrics={}
referenced_assets=set()
# This explicit portfolio retirement must also apply to reused build directories.
retired_product = DIST/'apps'/'voice-max'/'index.html'
retired_product.unlink(missing_ok=True)
if retired_product.parent.is_dir() and not any(retired_product.parent.iterdir()):
    retired_product.parent.rmdir()

# Inner pages directly under Home show the same trail as their BreadcrumbList data.
for _path,_name in [('/apps','Apps'),('/platform','Platform'),('/company','Company'),('/investors-partners','Investors & Partners'),
                    ('/careers','Careers'),('/contact','Contact'),('/press','Press kit'),('/accessibility','Accessibility'),('/website-data','Website data')]:
    _title,_desc,_body=pages[_path]
    pages[_path]=(_title,_desc,page_breadcrumbs(_name)+_body)
PAGE_DATES=seo.page_dates(pages)
PAGE_IMAGES={}
# Downloads the pages link to: the press kit archive and the founder's contact card.
(DIST/'assets/press').mkdir(parents=True,exist_ok=True)
(DIST/'assets/press/solarity-ai-press-kit.zip').write_bytes(press_kit_zip(APPS))
(DIST/'assets/contact').mkdir(parents=True,exist_ok=True)
(DIST/'assets/contact/ata-turhan.vcf').write_bytes(founder_vcard(EMAIL).encode('utf-8'))

for path,(title,desc,body) in pages.items():
    dest=DIST/'index.html' if path=='/' else DIST/'404.html' if path=='/404' else DIST/path.strip('/')/'index.html'
    dest.parent.mkdir(parents=True,exist_ok=True)
    document=normalize_page_links(shell(path,title,desc,body),pages)
    document,metrics=optimize_page(document,path,source_css)
    dest.write_text(document, encoding='utf-8', newline='\n')
    performance_metrics[path]=metrics
    main_html=document[document.find('<main'):document.find('</main>')]
    PAGE_IMAGES[path]=list(dict.fromkeys(ORIGIN+src for tag in re.findall(r'<img\b[^>]*>',main_html)
        for src in re.findall(r'\ssrc="(/assets/[^"]+)"',tag)
        if re.search(r'\salt="[^"]+"',tag) and int((re.search(r'\swidth="(\d+)"',tag) or [0,'0'])[1])>=240))
    referenced_assets|=set(re.findall(r'(?:'+re.escape(ORIGIN)+r'|(?<![\w.-]))(/assets/[^"\'\s,)*]+)(?![\w*])',document))
# Search engines and AI assistants may read every public page (seo.py names the AI crawlers).
(DIST/'robots.txt').write_text(seo.robots_txt(), encoding='utf-8', newline='\n')
(DIST/'sitemap.xml').write_text(seo.sitemap_xml(pages,PAGE_DATES,PAGE_IMAGES), encoding='utf-8', newline='\n')
(DIST/'llms.txt').write_text(seo.llms_txt(pages,apps=APPS,saas=SAAS,email=EMAIL,team=TEAM), encoding='utf-8', newline='\n')
(DIST/'llms-full.txt').write_text(seo.llms_txt(pages,apps=APPS,saas=SAAS,email=EMAIL,team=TEAM,full=True), encoding='utf-8', newline='\n')
(DIST/(seo.INDEXNOW_KEY+'.txt')).write_text(seo.INDEXNOW_KEY, encoding='utf-8', newline='\n')
# Previous solarityai.com URLs, redirected by Cloudflare Pages from _redirects.
LEGACY_REDIRECTS=[('/careers.html','/careers/'),('/blog.html','/'),('/legal.html','/contact/'),('/docs/xtract-demo.html','/')]
# RFC 9116: where to report a vulnerability. Expires is a fixed date; renew it before then.
(DIST/'.well-known').mkdir(exist_ok=True)
(DIST/'.well-known/security.txt').write_text('Contact: mailto:'+EMAIL+'\nContact: https://github.com/Solarity-AI/solarityai-landing-page/security/advisories/new\nPolicy: https://github.com/Solarity-AI/solarityai-landing-page/security/policy\nExpires: 2027-10-19T00:00:00.000Z\nPreferred-Languages: en\nCanonical: '+ORIGIN+'/.well-known/security.txt\n', encoding='utf-8', newline='\n')
(DIST/'_redirects').write_text(''.join(f'{old} {new} 301\n' for old,new in LEGACY_REDIRECTS), encoding='utf-8', newline='\n')
def content_security_policy():
    """A strict policy built from the pages just written: every inline script that runs is allowed by its
    hash, so the policy can never go stale. JSON-LD is data and is not executed. Styles stay inline: each
    route inlines its own CSS and a few images set their focus with a style attribute."""
    hashes=set()
    for page in DIST.rglob('*.html'):
        for attrs,body in re.findall(r'<script([^>]*)>(.*?)</script>',page.read_text(encoding='utf-8'),re.S):
            if 'src=' in attrs or 'application/ld+json' in attrs: continue
            hashes.add("'sha256-"+base64.b64encode(hashlib.sha256(body.encode('utf-8')).digest()).decode()+"'")
    return '; '.join([
        "default-src 'self'",
        "script-src 'self' "+' '.join(sorted(hashes))+" https://static.cloudflareinsights.com",
        "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data:",
        "font-src 'self'",
        "connect-src 'self' https://cloudflareinsights.com",
        "form-action 'self' https://formsubmit.co",
        "frame-ancestors 'self'",
        "base-uri 'self'",
        "object-src 'none'",
        "upgrade-insecure-requests",
    ])

SECURITY_HEADERS=('  Content-Security-Policy: '+content_security_policy()+'\n'
                  '  Strict-Transport-Security: max-age=31536000\n'
                  '  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), browsing-topics=()\n')
# No Cross-Origin-Opener-Policy: the site opens no cross-origin popups, and COOP's process swap breaks
# Lighthouse and PageSpeed Insights traces (NO_NAVSTART), measured on 2026-10-19.
(DIST/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n'+SECURITY_HEADERS+'/404\n  X-Robots-Tag: noindex, follow\n/404.html\n  X-Robots-Tag: noindex, follow\n/assets/optimized/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/runtime/*\n  Cache-Control: public, max-age=31536000, immutable\n'+FONT_URL+'\n  Cache-Control: public, max-age=31536000, immutable\n'+DISPLAY_FONT_URL+'\n  Cache-Control: public, max-age=31536000, immutable\n', encoding='utf-8', newline='\n')
# dist/ holds exactly what pages reference. An unpublished approved file in
# source-assets/ is published once a page references it; retired files never are.
for url in sorted(referenced_assets):
    target=DIST/url.lstrip('/')
    source=SOURCE_ASSETS/url.removeprefix('/assets/')
    if source.is_file() and 'retired' not in source.relative_to(SOURCE_ASSETS).parts and (not target.exists() or target.read_bytes()!=source.read_bytes()):
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
# Content-addressed outputs are regenerated by every build; remove stale ones.
optimized_names={Path(variant['url']).name for record in image_manifest['images'].values() for variant in record['webp']+record['avif']}
for folder,current in [(DIST/'assets/optimized',optimized_names),(RUNTIME,WRITTEN_RUNTIME)]:
    for stale in folder.iterdir():
        if stale.is_file() and stale.name not in current:stale.unlink()
(ROOT/'site-pages.json').write_text(json.dumps({p:{'title':v[0],'description':v[1]} for p,v in pages.items()},indent=2), encoding='utf-8', newline='\n')
(ROOT/'research-assets/performance-build.json').write_text(json.dumps({'scope':'Build-time source byte counts, not measured Lighthouse scores or HTTP transfer results','routes':performance_metrics},indent=2), encoding='utf-8', newline='\n')
print(f'Generated {len(pages)-1} content pages and 404.')
