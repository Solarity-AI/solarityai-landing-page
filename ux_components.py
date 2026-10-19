"""Shared discovery and contact markup. Product facts remain in APPS."""
from html import escape as e
from visual_products import voice_symbol


def discovery_symbol(app):
    """Use store-sourced icons; any future unlisted direction gets decoration."""
    if app['apple']:
        return f'<span class="discovery-symbol" aria-hidden="true"><img src="/assets/{e(app["slug"])}-icon.webp" alt="" width="48" height="48" loading="lazy"></span>'
    return '<span class="discovery-symbol discovery-concept" aria-hidden="true">'+voice_symbol(48)+'</span>'


def app_chooser(apps):
    goals = ['Build a self-care routine', 'Practice cognitive exercises', 'Reflect on sleep habits', 'Build a fitness routine']
    rows = []
    for app, goal in zip(apps, goals):
        availability = 'iOS & Android' if app['apple'] else 'Product vision · inquire for details'
        rows.append(f'<a href="/apps/{app["slug"]}" class="goal-choice" data-product-accent="{e(app["color"])}">{discovery_symbol(app)}<span class="goal-purpose">{goal}</span><strong>{app["name"]}</strong><span class="goal-availability">{availability}</span><span class="goal-action">Explore this app <span aria-hidden="true">→</span></span></a>')
    return '<section class="app-chooser wrap" aria-labelledby="chooser-title"><div class="chooser-heading"><h2 id="chooser-title">Find your starting point.</h2><p>Compare the focus of each app, then explore the one that fits your interest.</p></div><div class="goal-grid">'+''.join(rows)+'</div></section>'


def app_breadcrumbs(app):
    return f'<nav class="wrap breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/apps#{e(app["slug"])}">Apps</a></li><li><span aria-current="page">{e(app["name"])}</span></li></ol><span class="breadcrumb-context">{e(app["category"])}</span></nav>'


def related_apps(current, apps):
    links = ''.join(f'<a href="/apps/{e(a["slug"])}" data-product-accent="{e(a["color"])}">{discovery_symbol(a)}<span class="related-identity"><strong>{e(a["name"])}</strong><span class="related-category">{e(a["category"])}</span></span><small class="related-availability">{"iOS&nbsp;&amp;&nbsp;Android" if a["apple"] else "Product vision"}</small><span aria-hidden="true" class="related-arrow">→</span></a>' for a in apps if a['slug'] != current['slug'])
    return '<section class="related-apps wrap" aria-labelledby="related-title"><div class="related-intro"><h2 id="related-title">Another ambition in mind?</h2><p>Explore the other products in the Solarity AI portfolio.</p></div><nav aria-label="Other Solarity AI apps">'+links+'</nav></section>'


def inquiry_panel(intent_picker, email):
    return f'''<div class="contact-panel" id="prepare-inquiry" tabindex="-1">
      <div class="composer-intro">
      <p class="eyebrow inquiry-kicker">Email the founder</p>
      <h2 id="inquiry-heading">What brings you here?</h2>
      <p class="muted" id="inquiry-description">Prepare an email to the founder.</p>
      <p class="handoff-note composer-handoff">Review here, then send from your email app. This website does not send messages.</p>
      </div>
      <form id="inquiry-form">
        <fieldset id="inquiry-fields" disabled>
          <legend class="sr-only">Prepare your inquiry</legend>
          <div id="error-summary" class="error-summary" tabindex="-1" aria-labelledby="error-title" hidden><h3 id="error-title">Please check these details.</h3><ul id="error-list"></ul></div>
          <div class="inquiry-group inquiry-interest" role="group" aria-labelledby="interest-group-title">
          <h3 class="inquiry-group-title" id="interest-group-title"><span class="inquiry-step" aria-hidden="true">01</span>Topic</h3>
          <div id="type-fallback"><label for="inquiry-type">I’m reaching out about</label><select id="inquiry-type" name="type"><option>Investor</option><option>Strategic partner</option><option>Product inquiry</option><option>Other</option></select></div>
          {intent_picker()}
          <label for="product-context">Product or topic <span>(optional)</span></label>
          <input id="product-context" name="product" maxlength="100" autocomplete="off" list="topic-options" aria-describedby="topic-help product-context-error"><datalist id="topic-options"></datalist>
          <p class="field-help" id="topic-help">Choose a suggestion or write your own topic.</p><p class="field-error" id="product-context-error" hidden></p>
          </div>
          <div class="inquiry-group inquiry-introduction" role="group" aria-labelledby="introduction-group-title">
          <h3 class="inquiry-group-title" id="introduction-group-title"><span class="inquiry-step" aria-hidden="true">02</span>Introduction</h3>
          <label for="name">Your name <span>(required)</span></label><input id="name" name="name" required maxlength="100" autocomplete="name" aria-describedby="name-error"><p class="field-error" id="name-error" hidden></p>
          <details class="optional-details" id="optional-details"><summary>Add contact details <span>(optional)</span></summary><p>Your email app already identifies the sender. Add another reply address or organization if useful.</p>
          <label for="email">Reply email <span>(optional)</span></label><input id="email" name="email" type="email" maxlength="254" autocomplete="email" inputmode="email" spellcheck="false" autocapitalize="none" aria-describedby="email-error"><p class="field-error" id="email-error" hidden></p>
          <label for="organization">Organization <span>(optional)</span></label><input id="organization" name="organization" maxlength="150" autocomplete="organization" aria-describedby="organization-error"><p class="field-error" id="organization-error" hidden></p>
          </details>
          </div>
          <div class="inquiry-group inquiry-message" role="group" aria-labelledby="message-group-title">
          <h3 class="inquiry-group-title" id="message-group-title"><span class="inquiry-step" aria-hidden="true">03</span>Message</h3>
          <label for="message">What would you like to explore? <span>(required)</span></label>
          <textarea id="message" name="message" aria-describedby="message-help message-count message-error" required minlength="10" maxlength="2500" rows="5" placeholder="A little context makes for a better first conversation."></textarea>
          <div class="message-meta"><span id="message-help">A short introduction is enough. Use at least 10 characters.</span><span id="message-count">0 / 2500</span></div><p class="field-error" id="message-error" hidden></p>
          </div>
          <div class="inquiry-action">
          <button class="button primary" id="review-inquiry" type="submit" disabled>Review email draft <span aria-hidden="true">→</span></button>
          </div>
        </fieldset>
      </form>
      <noscript><p class="handoff-note">JavaScript is needed for the draft composer. <a href="mailto:{email}">Email {email} directly</a> or use the booking link.</p></noscript>
      <section id="inquiry-review" class="inquiry-review" aria-labelledby="review-heading" hidden>
        <div class="review-heading-row"><p class="eyebrow">YOUR EMAIL DRAFT</p><span class="draft-state">Draft not sent</span></div><h3 id="review-heading" tabindex="-1">Review, then send.</h3>
        <dl class="review-meta"><div><dt>To</dt><dd id="review-to"></dd></div><div><dt>Subject</dt><dd id="review-subject"></dd></div></dl>
        <label for="review-body">Full draft to review or copy</label><textarea id="review-body" readonly rows="10" spellcheck="false"></textarea>
        <p id="long-draft-note" class="handoff-note" hidden>This is a long draft. If your email app does not include all of it, copy the full draft below instead.</p>
        <a id="review-open-email" class="button primary" href="mailto:{email}">Open in email app <span aria-hidden="true">↗</span></a>
        <div class="review-tools"><button id="copy-inquiry" type="button"><svg class="draft-tool-icon" viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true" focusable="false"><rect x="7" y="6" width="10" height="11" rx="1.5"/><path d="M12 6V3H3v10h4"/></svg>Copy full draft</button><button id="select-inquiry" type="button"><svg class="draft-tool-icon" viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true" focusable="false"><path d="M3 6V3h3m8 0h3v3m0 8v3h-3M6 17H3v-3M7 7h6M7 10h6M7 13h4"/></svg>Select draft text</button><button id="edit-inquiry" type="button"><svg class="draft-tool-icon" viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true" focusable="false"><path d="m13 3 4 4-9 9-5 1 1-5 9-9Zm-2 2 4 4M4 12l4 4"/></svg>Edit details</button></div>
        <p class="fineprint manual-send-note"><span class="send-reminder">You still need to press Send in your email app.</span> <span class="webmail-note">Prefer webmail? Copy the draft and email <a href="mailto:{email}">{email}</a>.</span></p>
      </section>
      <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
      <div class="data-note" id="data-note"><h3>About this contact experience</h3><p>Your draft stays in this page while it is open. The website does not submit or save it. When you send the email, your email provider handles delivery. The booking link opens Google Calendar.</p></div>
    </div>'''


def copy_button(address, status_id):
    """Copy-to-clipboard fallback for an email address; scripts/copy.js reveals it."""
    return ('<span class="copy-row"><button type="button" class="copy-button" data-copy="' + e(address, quote=True)
            + '" data-copy-status="' + e(status_id, quote=True) + '" hidden>Copy address</button>'
            + '<span class="copy-status" id="' + e(status_id, quote=True) + '" role="status" aria-live="polite"></span></span>')
