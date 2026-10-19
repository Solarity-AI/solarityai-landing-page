from pathlib import Path
import base64, hashlib, json, html, re, shutil
from urllib.parse import urlencode
from ux_components import app_breadcrumbs, related_apps, inquiry_panel
from image_provenance import provenance
from ux_content import investor_faq, recovery_links
from visual_home import hero_section, closing_scene
from visual_saas import saas_wall, saas_chapters, apps_web_band
from saas_products import SAAS
from visual_sections import feature_grid, founder_card, founder_portrait
from visual_team import selected_team
from visual_careers import careers_page
from visual_contact import contact_page
from visual_chrome import site_header, site_footer, contact_methods
from visual_stage import store_badges
from visual_products import product_art, product_page, voice_symbol
from visual_catalog import portfolio_page, portfolio_wall
from product_story import product_story
from visual_company_upgrade import strategy_story, investor_evidence, investor_opening, operating_principles, founder_booking
from visual_strategy import platform_opening
from optimize_images import ensure_optimized_images, write_favicon
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
e = html.escape
ARROW = '<span aria-hidden="true">→</span>'
EXTERNAL_ARROW = '<span aria-hidden="true">↗</span>'

APPS = [
 dict(slug='looks-max',crop_focus='50% 64%',name='Looks Max',category='Appearance & self-care',color='lavender',headline='A more considered approach to self-care.',summary='Personalized appearance insights, daily habits, and a place to follow your progress.',intro='For people making grooming and self-care part of their daily routine. Looks Max brings facial analysis and personalized guidance into a single app.',features=[('Understand your starting point','Explore AI-generated facial assessments and breakdowns across appearance categories.'),('Turn insights into habits','Find personalized grooming suggestions and daily habits you can return to.'),('Keep a record of progress','Use the activity calendar and journal to follow your own routine over time.')],screen='looks-max-screen-4.webp',apple='https://apps.apple.com/us/app/looks-max-look-your-best/id6778990308',google='https://play.google.com/store/apps/details?id=com.solarityai.onlylooksmax',note='Appearance scores are app-generated assessments, not objective measures of personal worth or promises of a particular result.'),
 dict(slug='iq-max',crop_focus='50% 68%',hero_screen='iq-max-detail-screen-4.webp',hero_alt='IQ Max official App Store imagery showing the focus selection with memory, processing speed, focus, and overall thinking options.',name='IQ Max',category='Cognitive practice',color='blue',headline='Make room for a daily mental challenge.',summary='Focused cognitive exercises, adaptive difficulty, and a daily routine you control.',intro='For curious people who enjoy a structured mental challenge. Choose exercises, practice regularly, and follow your performance across sessions.',features=[('Choose your daily practice','Explore exercises involving memory, reaction time, and attention.'),('Keep the challenge moving','Adaptive difficulty adjusts the challenge as you practice.'),('See your consistency','Session results, stars, and streaks make your practice visible.')],screen='iq-max-screen-1.webp',apple='https://apps.apple.com/us/app/iq-max-smarter-every-day/id6803826639',google='https://play.google.com/store/apps/details?id=com.solarityai.iqmax',note='Exercise scores describe performance within the app. They are not a clinical assessment or a guarantee of increased intelligence.'),
 dict(slug='sleep-max',crop_focus='50% 22%',name='Sleep Max',category='Sleep & daily routines',color='indigo',headline='Bring intention to the end of your day.',summary='A sleep diary, habit tracking, and coaching to support a more consistent routine.',intro='For people who want to pay closer attention to their sleep habits. Sleep Max combines personal logging with guidance and tools for winding down.',features=[('Reflect on your nights','Record sleep in a diary and review your app-generated Sleep Score.'),('Build a regular routine','Follow habits, activity, and streaks as part of your personal practice.'),('Make space to wind down','Explore soundscapes and an AI sleep coach for general guidance.')],screen='sleep-max-screen-4.webp',apple='https://apps.apple.com/us/app/sleep-max-rest-best/id6806709872',google='https://play.google.com/store/apps/details?id=com.solarityai.sleepmax',note='Sleep Max is presented here as a general wellness product. Its guidance does not replace individual medical assessment.'),
 dict(slug='fitness-max',crop_focus='50% 72%',name='Fitness Max',category='Fitness & nutrition',color='amber',headline='Build a routine you can follow.',summary='Meal insights, training logs, and AI coaching to help you follow your fitness routine.',intro='For people bringing more consistency to training and nutrition. Log your day, explore meal insights, and review progress with goal-focused AI coaching.',features=[('Log your day in your own words','Use voice or text to record training, sleep, and daily updates.'),('Explore your meals','Photo-based meal analysis provides estimated nutrition information to support your food log.'),('Follow your progress','Review coaching reports and progress photos as you work toward your own goals.')],screen='fitness-max-screen-2.webp',screen_width=600,screen_height=1298,store_name='Only Fitness',apple='https://apps.apple.com/us/app/only-fitness-ai-coach/id6789095658',google='https://play.google.com/store/apps/details?id=com.solarityai.onlyfitness',note='Fitness Max is listed in app stores as Only Fitness. Nutrition estimates and AI coaching are general guidance, not medical advice or a guarantee of fitness results.')
]

def contact(kind='Other', product=None):
    return '/contact?' + urlencode({'type':kind, **({'product':product} if product else {})}) + '#prepare-inquiry'

def btn(label,href,style='primary',external=False):
    arrow = EXTERNAL_ARROW if external or href.startswith(('http','mailto:')) else ARROW
    new_tab = '<span class="sr-only"> (opens in a new tab)</span>' if external else ''
    return f'<a class="button {style}" href="{e(href)}"'+(' target="_blank" rel="noopener noreferrer"' if external else '')+f'>{e(label)}{arrow}{new_tab}</a>'

def product_status(a,full=False):
    return '<span class="status"><i aria-hidden="true"></i>'+('Available on iOS & Android' if full else 'iOS & Android')+'</span>' if a['apple'] else '<span class="status vision"><i aria-hidden="true"></i>Product vision</span>'

def jump_nav(items,label):
    return '<nav class="section-jump" aria-label="'+label+'"><div class="wrap"><span class="jump-label">'+label+'</span><div>'+''.join(f'<a href="#{slug}">{name}</a>' for slug,name in items)+'</div></div></nav>'

def eyebrow(text): return f'<p class="eyebrow">{text}</p>'
def heading(kicker,title,desc=''):
    return f'<div class="section-heading"><div>{eyebrow(kicker)}<h2>{title}</h2></div>'+ (f'<p class="section-lede">{desc}</p>' if desc else '')+'</div>'
def wave():
    return '<div class="voice-art" aria-hidden="true"><div class="voice-art-mark">'+voice_symbol(220)+'</div><span>A voice for your ambition.</span></div>'

def app_art(a,small=False):
    return product_art(a,small)

def app_card(a,idx):
    icon=f'<img src="/assets/{a["slug"]}-icon.webp" width="44" height="44" alt="" loading="lazy">' if a['apple'] else '<span class="voice-icon" aria-hidden="true">'+voice_symbol(44)+'</span>'
    visual=f'<img src="/assets/{a["screen"]}" alt="" width="600" height="1298" loading="lazy">' if a['screen'] else wave()
    return f'<a class="app-card {a["color"]}" href="/apps/{a["slug"]}"><div class="app-card-content"><div class="card-top">{icon}{product_status(a)}</div><p class="eyebrow">{e(a["category"])}</p><h3>{a["name"]}</h3><p>{e(a["summary"])}</p><span class="text-link">Explore {a["name"]} {ARROW}</span></div><div class="card-preview" aria-hidden="true">{visual}</div></a>'
def cta(title='A conversation with possibility.',desc='For investors and partners who see the potential in thoughtful consumer products and the systems behind them.',lead='investor'):
    return closing_scene(title, desc, contact, lead)

def intent_picker():
    options=[('Investor','Company & investment'),('Strategic partner','Build something together'),('Product inquiry','Talk about an app'),('Other','Start a conversation')]
    return '<fieldset class="intent-picker" id="intent-picker" hidden><legend>I’m reaching out about</legend><div>'+''.join(f'<label><input type="radio" name="inquiry-choice" value="{label}"><span><strong>{label}</strong><small>{desc}</small></span></label>' for label,desc in options)+'</div></fieldset>'

def social_for(path):
    """The link-preview image for a route (make_social_images.py), and its alt text."""
    by_slug={a['slug']:a for a in APPS}
    if path.startswith('/apps/') and path[6:] in by_slug:
        a=by_slug[path[6:]]
        return f'social/{a["slug"]}.jpg', f'{a["name"]}, {a["category"]}: the app icon beside official App Store imagery'
    return {'/apps':('social/apps.jpg','The four Solarity AI app icons'),
            '/platform':('social/platform.jpg','Engineering Max, Management Max and Marketing Max product screens'),
            '/investors-partners':('social/investors.jpg','The four Solarity AI app icons')}.get(
            path,('social/default.jpg','A person climbing mountain steps toward a golden sunrise above the clouds'))

ORGANIZATION={'@type':'Organization','@id':ORIGIN+'/#organization','name':'Solarity AI','legalName':'Solarity AI LLC','url':ORIGIN+'/','logo':ORIGIN+'/assets/brand/solarity-sun-320.2513ba060440.webp','founder':{'@type':'Person','name':'Ata Turhan'},'email':EMAIL,'address':{'@type':'PostalAddress','addressLocality':'Irving','addressRegion':'Texas','addressCountry':'US'}}

def structured_data(path,title,desc):
    """schema.org data for a route: the organization everywhere, plus the products the page presents.
    Only facts already on the page; no ratings, prices or categories the stores have not confirmed."""
    url=ORIGIN+public_path(path)
    graph=[ORGANIZATION]
    publisher={'@id':ORIGIN+'/#organization'}
    def mobile(a):
        return {'@type':'MobileApplication','name':a['name'],'url':ORIGIN+public_path('/apps/'+a['slug']),'description':a['summary'],
                'operatingSystem':'iOS, Android','image':ORIGIN+'/assets/'+a['slug']+'-icon.webp','sameAs':[a['apple'],a['google']],'publisher':publisher}
    if path=='/':
        graph.append({'@type':'WebSite','@id':ORIGIN+'/#website','name':'Solarity AI','url':ORIGIN+'/','publisher':publisher})
    elif path=='/apps':
        graph.append({'@type':'ItemList','name':title,'itemListElement':[{'@type':'ListItem','position':i+1,'item':mobile(a)} for i,a in enumerate(a for a in APPS if a.get('apple'))]})
    elif path.startswith('/apps/'):
        a=next(a for a in APPS if '/apps/'+a['slug']==path)
        graph.append(mobile(a))
        graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':ORIGIN+'/'},{'@type':'ListItem','position':2,'name':'Apps','item':ORIGIN+public_path('/apps')},{'@type':'ListItem','position':3,'name':a['name'],'item':url}]})
    elif path=='/platform':
        graph.append({'@type':'ItemList','name':title,'itemListElement':[{'@type':'ListItem','position':i+1,'item':{'@type':'WebApplication','name':p['name'],'url':p['url'],'description':p['tagline'],'applicationCategory':'BusinessApplication','operatingSystem':'Web','publisher':publisher}} for i,p in enumerate(SAAS)]})
    return {'@context':'https://schema.org','@graph':graph}

NAV=[('/apps','Apps'),('/platform','Platform'),('/company','Company'),('/investors-partners','Investors & Partners'),('/careers','Careers')]
def shell(path,title,desc,body):
    # email_off keeps Cloudflare Email Address Obfuscation from rewriting mailto links
    # and visible addresses, so the domain serves exactly what dist/ contains.
    robots = "noindex,follow" if path == "/404" else "index,follow"
    social_image, social_alt = social_for(path)
    # Preloaded everywhere: with font-display optional it adds no Home LCP cost (2855 vs 2857 ms measured in P2).
    display_preload = f'<link rel="preload" href="{DISPLAY_FONT_URL}" as="font" type="font/woff2" crossorigin>'
    data=structured_data(path,title,desc)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} | Solarity AI</title><meta name="description" content="{e(desc)}"><meta name="robots" content="{robots}"><meta name="referrer" content="strict-origin-when-cross-origin"><meta name="theme-color" content="#0f0d0b"><link rel="canonical" href="{ORIGIN}{public_path(path)}"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | Solarity AI"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{ORIGIN}{public_path(path)}"><meta property="og:image" content="{ORIGIN}/assets/{social_image}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{e(social_alt)}"><meta property="og:site_name" content="Solarity AI"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{ORIGIN}/assets/{social_image}"><link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48"><link rel="icon" href="/assets/brand/solarity-sun-48.9bc99afc73e8.webp" type="image/webp" sizes="48x48"><link rel="preload" href="{FONT_URL}" as="font" type="font/woff2" crossorigin>{display_preload}<link rel="stylesheet" href="/assets/presentation.css"><script src="/assets/site.js" defer></script><script type="application/ld+json">{json.dumps(data)}</script></head>
<body data-page="{path}"><!--email_off--><a class="skip-link" href="#main">Skip to content</a>{site_header(path,NAV,btn)}
<main id="main" tabindex="-1">{body}</main><dialog id="image-dialog" aria-labelledby="image-dialog-title"><div class="image-dialog-bar"><h2 id="image-dialog-title">App screenshot</h2><button type="button" id="image-dialog-close">Close preview <span aria-hidden="true">×</span></button></div><img id="image-dialog-image" alt="" width="600" height="1298"><div class="image-dialog-nav" id="image-dialog-nav" hidden><button type="button" id="image-dialog-prev"><span aria-hidden="true">←</span> Previous<span class="sr-only"> screenshot</span></button><span id="image-dialog-count" aria-live="polite"></span><button type="button" id="image-dialog-next">Next<span class="sr-only"> screenshot</span> <span aria-hidden="true">→</span></button></div><p id="image-dialog-caption" class="caption">{provenance()}</p></dialog>{site_footer(EMAIL,path,BOOKING)}<!--/email_off--></body></html>'''

pages={}
hero=hero_section(APPS,btn,contact)
products=portfolio_wall(APPS)
founder_strip=f'''<section class="founder-strip wrap">{founder_portrait(compact=True)}<div><h2>Ata Turhan</h2><p>Building Solarity AI from Irving, Texas, with a focus on consumer products and the systems behind them.</p></div><a class="text-link" href="/company">Meet the company {ARROW}</a></section>'''
pages['/']=('Building for human potential','AI-powered self-improvement apps, and three web apps for engineering, managing and marketing mobile products. Explore Solarity AI and connect with our founder.',hero+products+saas_wall(SAAS)+founder_strip+cta('Build on a shared ambition.','Explore the portfolio, discuss a partnership, or speak with the founder about the company’s direction.'))

pages['/apps']=('Apps for everyday ambition','Discover Looks Max, IQ Max, Sleep Max and Fitness Max, and the Engineering Max, Management Max and Marketing Max web apps from Solarity AI.',portfolio_page(APPS,btn,app_art,product_status)+apps_web_band(SAAS)+cta('Products with purpose.','Interested in distribution, product collaboration, or the wider Solarity AI story? Let’s start a conversation.'))

for a in APPS:
    status=product_status(a,True)
    stores=store_badges(a, btn('Ask about '+a['name'],contact('Product inquiry',a['name'])))
    features=feature_grid(a)
    pages['/apps/'+a['slug']]=(a['name']+' | '+a['category'],a['summary'],product_page(a,APPS,btn,contact,stores,status,features,app_breadcrumbs(a),related_apps(a,APPS)))

pages['/platform']=('The app factory','Engineering Max, Management Max and Marketing Max: three Solarity AI web apps for engineering, managing and marketing mobile products.',f'''{platform_opening(APPS,SAAS,btn,contact)}{saas_chapters(SAAS)}{strategy_story(btn,contact)}{cta("Shape the next product workflow.","Bring a specific engineering, management, or marketing problem to a conversation about the app factory direction.",lead='partner')}''')

pages['/company']=('The company','Meet founder Ata Turhan and the Solarity AI team building self-improvement apps and the systems behind them.',f'''
<section class="page-intro wrap company-intro"><h1>The people.<br>The purpose.</h1><p class="lede">Founded by Ata Turhan in Irving, Texas, Solarity AI brings focused self-improvement apps together with a vision for more repeatable product development.</p><a class="text-link company-team-shortcut" href="#team">Meet our team <span aria-hidden="true">↓</span></a><a class="text-link company-careers-shortcut" href="/careers">Explore careers <span aria-hidden="true">→</span></a></section>
<section class="founder-section wrap">{founder_card()}<div><h2>Start with the person.<br>Build with purpose.</h2><p>Ata Turhan founded Solarity AI with a focus on AI-powered products. Today, that direction brings four self-improvement apps together with three web apps for the teams who build them.</p><p>The company welcomes investors and collaborators interested in consumer software, product distribution, and systems for the teams creating mobile experiences.</p>{btn('Connect with Ata','/contact','outline')}</div></section>
{selected_team()}{operating_principles()}
{cta("Meet the people. Explore the possibility.","Connect with the founder about Solarity AI’s products, company direction, or a potential partnership.")}''')

pages['/investors-partners']=('Investors & strategic partners','Explore the Solarity AI product thesis and opportunities for investment, distribution, technology collaboration and platform design partnerships.',f'''{investor_opening(APPS,btn,contact)}{investor_evidence(APPS)}{investor_faq()}{founder_booking(btn,BOOKING)}''')

pages['/careers']=('Careers: Build with us','Explore engineering, marketing and business development opportunities at Solarity AI. Apply to help build focused AI-powered mobile products.',careers_page(btn))

pages['/contact']=('Start a conversation','Contact Solarity AI about investment, strategic partnerships or its consumer apps. Reach founder Ata Turhan directly.',contact_page(EMAIL,BOOKING,btn))
pages['/404']=('Page not found','Find your way back to Solarity AI.',f'<section class="page-intro wrap not-found"><div class="recovery-intro">{eyebrow("Error 404")}<h1>This page <span class="muted">is not here.</span></h1><p class="lede">Let’s get you back to the products, the platform, or the conversation.</p><div class="actions">{btn("Back to home","/")}{btn("Explore our apps","/apps","outline")}</div></div>{recovery_links()}</section>')

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

for path,(title,desc,body) in pages.items():
    dest=DIST/'index.html' if path=='/' else DIST/'404.html' if path=='/404' else DIST/path.strip('/')/'index.html'
    dest.parent.mkdir(parents=True,exist_ok=True)
    document=normalize_page_links(shell(path,title,desc,body),pages)
    document,metrics=optimize_page(document,path,source_css)
    dest.write_text(document, encoding='utf-8', newline='\n')
    performance_metrics[path]=metrics
    referenced_assets|=set(re.findall(r'(?:'+re.escape(ORIGIN)+r'|(?<![\w.-]))(/assets/[^"\'\s,)]+)',document))
# Search indexing stays open; AI-training crawlers keep the block solarityai.com already published.
AI_TRAINING_CRAWLERS=['GPTBot','Google-Extended','CCBot','anthropic-ai','Claude-Web','PerplexityBot']
(DIST/'robots.txt').write_text('User-agent: *\nAllow: /\n'+''.join(f'\nUser-agent: {agent}\nDisallow: /\n' for agent in AI_TRAINING_CRAWLERS)+f'\nSitemap: {ORIGIN}/sitemap.xml\n', encoding='utf-8', newline='\n')
(DIST/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}{public_path(p)}</loc></url>' for p in pages if p!='/404')+'</urlset>', encoding='utf-8', newline='\n')
# Previous solarityai.com URLs, redirected by Cloudflare Pages from _redirects.
LEGACY_REDIRECTS=[('/careers.html','/careers/'),('/blog.html','/'),('/legal.html','/contact/'),('/docs/xtract-demo.html','/')]
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
    if not target.exists() and source.is_file() and 'retired' not in source.relative_to(SOURCE_ASSETS).parts:
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
