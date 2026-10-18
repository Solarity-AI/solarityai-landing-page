"""Careers content adapted from the company's published careers page.

The native form hands off to the founder-selected recruiting address via FormSubmit.
The provider, rather than this page, confirms verification and acceptance.
"""
from html import escape


CAREER_ROLES = (
    (
        'full-stack-engineer',
        'Full Stack Engineer',
        'Engineering',
        'Interested in the work behind a focused digital product? Show us what '
        'you have built and tell us where you would like to contribute.',
    ),
    (
        'marketing-specialist',
        'Marketing Specialist',
        'Marketing',
        'Help connect products with the people they are built for. Share work '
        'that shows how you approach a message, an audience, or a campaign.',
    ),
    (
        'business-development-manager',
        'Business Development Manager',
        'Business development',
        'Interested in building meaningful business relationships? Introduce '
        'your experience and the opportunities you would like to explore.',
    ),
)

POSTERS_URL = 'https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws'


def careers_page(btn):
    """Return the /careers content inside the site's shared page shell."""
    roles = []
    options = ['<option value="">Select a position</option>']
    for slug, title, discipline, detail in CAREER_ROLES:
        roles.append(
            '<article class="career-role" aria-labelledby="role-' + slug + '">'
            '<div class="career-role-meta">' + escape(discipline) + '</div><div class="career-role-copy">'
            '<h3 id="role-' + slug + '">' + escape(title) + '</h3><p>'
            + escape(detail) + '</p><ul class="career-role-tags" '
            'aria-label="Work arrangements"><li>Fully remote</li>'
            '<li>Full-time / Part-time</li></ul></div>'
            '<a class="career-role-action" href="/careers?role=' + slug
            + '#apply" data-career-role="' + slug + '"><span>Apply<span '
            'class="sr-only"> for ' + escape(title) + '</span></span>'
            '<span aria-hidden="true">↓</span></a></article>'
        )
        options.append('<option value="' + slug + '">' + escape(title) + '</option>')

    return '''<section class="careers-opening wrap" aria-labelledby="careers-title">
<div class="careers-opening-copy"><p class="eyebrow">CAREERS AT SOLARITY AI</p>
<h1 id="careers-title">Good work.<br><em>Shared ambition.</em></h1>
<p class="lede">Help build focused products for human potential. Bring your craft to engineering, marketing, or business development at Solarity AI.</p>
<div class="actions">''' + btn('Explore opportunities', '#opportunities') + '''
<a class="text-link" href="/company">Meet the company <span aria-hidden="true">→</span></a></div></div>
<figure class="careers-founder"><img src="/assets/brand/ata-turhan-640.742556487789.webp" srcset="/assets/brand/ata-turhan-320.db6d27d9b9b3.webp 320w, /assets/brand/ata-turhan-640.742556487789.webp 640w" sizes="(max-width: 560px) 200px, (max-width: 850px) 240px, 340px" width="640" height="640" alt="Ata Turhan, founder of Solarity AI" decoding="async"><figcaption><p class="eyebrow">THE PEOPLE BEHIND THE WORK</p><p><strong>Ata Turhan</strong><span>Founder, Solarity AI</span></p><a class="text-link" href="/company#team">Meet the team <span aria-hidden="true">→</span></a></figcaption></figure>
</section>

<section class="career-benefits wrap" aria-labelledby="career-benefits-title">
<div class="career-section-heading"><p class="eyebrow">WHY SOLARITY AI</p><h2 id="career-benefits-title">A place for <br><em>your contribution.</em></h2></div>
<dl class="career-benefit-list">
<div><dt>Generous profit sharing</dt><dd>Share in the value you help create. Discuss the arrangement for your role during the hiring process.</dd></div>
<div><dt>Fully remote</dt><dd>Contribute remotely, with the work and your collaboration at the center of the conversation.</dd></div>
<div><dt>Respect for talent</dt><dd>Bring your perspective, your skills, and the care you put into your work. We want to understand what you can contribute.</dd></div>
</dl></section>

<section class="career-opportunities wrap" id="opportunities" aria-labelledby="career-opportunities-title">
<div class="career-opportunities-heading"><div><p class="eyebrow">FIND YOUR PLACE</p><h2 id="career-opportunities-title">Find your place.</h2></div>
<p>Three disciplines. One product direction. Read the role introductions, then tell us where you could contribute.</p></div>
<div class="career-role-list">''' + ''.join(roles) + '''</div>
<div class="career-posters"><p>Want to learn more before applying?</p><a class="text-link" href="''' + POSTERS_URL + '''" target="_blank" rel="noopener noreferrer">View job posters <span aria-hidden="true">↗</span><span class="sr-only"> on Google Drive, opens in a new tab</span></a></div>
</section>

<section class="career-apply wrap" id="apply" aria-labelledby="career-apply-title">
<div class="career-apply-copy"><p class="eyebrow">START A CONVERSATION</p><h2 id="career-apply-title">Tell us what<br><em>you bring.</em></h2>
<p>Start with your name, email, and the opportunity you have in mind. A LinkedIn profile or a link to your work can add context, if you have one.</p>

<div class="career-email-alternative"><p>Prefer to contact us directly?</p><a href="mailto:careers@solarityai.com?subject=Career%20inquiry%20-%20Solarity%20AI">careers@solarityai.com <span aria-hidden="true">↗</span></a></div></div>

<form id="career-form" class="career-form" action="https://formsubmit.co/careers@solarityai.com" method="POST" aria-labelledby="career-form-title" aria-describedby="career-form-intro career-disclosure">
<div class="career-form-heading"><p class="eyebrow">YOUR APPLICATION</p><h3 id="career-form-title">Introduce yourself.</h3><p id="career-form-intro">Four details to get started. Work links are optional.</p></div>
<input type="hidden" name="_subject" value="New Job Application - Solarity AI">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_template" value="box">
<input type="hidden" name="_url" value="https://solarity-company.the-ata-turhan.chatgpt.site/careers/">
<div hidden><label for="career-honey">Leave this field empty</label><input id="career-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
<div id="career-errors" class="career-errors" tabindex="-1" hidden><h3>Please check your application.</h3><ul id="career-error-list"></ul></div>
<div class="career-fields">
<div class="career-field"><label for="career-name">Full name</label><input id="career-name" name="fullName" type="text" required minlength="2" maxlength="100" autocomplete="name" aria-describedby="career-name-help career-name-error"><p id="career-name-help" class="career-field-help">Use the name you would like us to address you by.</p><p id="career-name-error" class="career-field-error" hidden></p></div>
<div class="career-field"><label for="career-email">Email address</label><input id="career-email" name="email" type="email" required maxlength="254" autocomplete="email" spellcheck="false" autocapitalize="none" aria-describedby="career-email-help career-email-error"><p id="career-email-help" class="career-field-help">Use the address where you would like to hear from us.</p><p id="career-email-error" class="career-field-error" hidden></p></div>
<div class="career-field"><label for="career-position">Position</label><select id="career-position" name="position" required aria-describedby="career-position-help career-position-error">''' + ''.join(options) + '''</select><p id="career-position-help" class="career-field-help">Choose the role you would like to apply for.</p><p id="career-position-error" class="career-field-error" hidden></p></div>
<div class="career-field"><label for="career-work-type">Work arrangement</label><select id="career-work-type" name="workType" required aria-describedby="career-work-type-help career-work-type-error"><option value="">Select an arrangement</option><option value="full-time">Full-time</option><option value="part-time">Part-time</option><option value="intern">Internship</option></select><p id="career-work-type-help" class="career-field-help">Indicate your preference to discuss with the team.</p><p id="career-work-type-error" class="career-field-error" hidden></p></div>
<div class="career-field"><label for="career-linkedin">LinkedIn profile <span>Optional</span></label><input id="career-linkedin" name="linkedin" type="url" maxlength="500" autocomplete="url" spellcheck="false" autocapitalize="none" pattern="https://(www[.])?linkedin[.]com/in/.+" aria-describedby="career-linkedin-help career-linkedin-error"><p id="career-linkedin-help" class="career-field-help">Your personal LinkedIn profile URL, if useful.</p><p id="career-linkedin-error" class="career-field-error" hidden></p></div>
<div class="career-field"><label for="career-portfolio">Portfolio or relevant work <span>Optional</span></label><input id="career-portfolio" name="portfolio" type="url" maxlength="500" autocomplete="url" spellcheck="false" autocapitalize="none" pattern="https?://.+" aria-describedby="career-portfolio-help career-portfolio-error"><p id="career-portfolio-help" class="career-field-help">A website, GitHub profile, or work sample. Include https:// or http://.</p><p id="career-portfolio-error" class="career-field-error" hidden></p></div>
</div>
<div class="career-form-handoff"><p id="career-disclosure">Your application is addressed to <a href="mailto:careers@solarityai.com">careers@solarityai.com</a>. The next step opens FormSubmit for verification and its submission confirmation. <a href="https://formsubmit.co/privacy.pdf" target="_blank" rel="noopener noreferrer">Read FormSubmit’s privacy policy <span aria-hidden="true">↗</span><span class="sr-only">, opens in a new tab</span></a>.</p>
<button id="career-submit" class="button primary" type="submit">Continue application <span aria-hidden="true">↗</span></button>
<p id="career-status" role="status" aria-live="polite" aria-atomic="true"></p></div>
</form></section>'''
