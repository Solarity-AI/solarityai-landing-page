(function () {
  'use strict';

  const CONTACT_EMAIL = 'ata.turhan@solarityai.com';
  const INQUIRY_TYPES = ['Investor', 'Strategic partner', 'Product inquiry', 'Other'];
  const line = (value, limit) => String(value || '').replace(/[\r\n\t]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, limit);
  const validType = (value) => INQUIRY_TYPES.includes(value) ? value : 'Other';

  function formatInquiry(input) {
    const type = validType(input.type);
    const product = line(input.product, 100);
    const name = line(input.name, 100);
    const email = line(input.email, 254);
    const organization = line(input.organization, 150);
    const message = String(input.message || '').replace(/\r\n?/g, '\n').trim().slice(0, 2500);
    const subject = 'Solarity AI | ' + type + (product ? ' | ' + product : '');
    const body = [
      'Inquiry: ' + type,
      ...(product ? ['Product or topic: ' + product] : []),
      'Name: ' + name,
      ...(email ? ['Email: ' + email] : []),
      ...(organization ? ['Organization: ' + organization] : []),
      '',
      message
    ].join('\n');
    return { to: CONTACT_EMAIL, subject, body, text: 'To: ' + CONTACT_EMAIL + '\nSubject: ' + subject + '\n\n' + body };
  }

  function buildMailto(inquiry) {
    return 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(inquiry.subject) + '&body=' + encodeURIComponent(inquiry.body);
  }

  function readInquiryContext(search) {
    const params = new URLSearchParams(search);
    const type = validType(params.get('type'));
    const acceptsContext = type === 'Product inquiry' || type === 'Strategic partner';
    return { type, product: acceptsContext ? line(params.get('product'), 100) : '' };
  }

  const PRODUCT_TOPICS = ['Looks Max', 'IQ Max', 'Sleep Max', 'Fitness Max', 'Engineering Max', 'Management Max', 'Marketing Max'];

  function validateInquiry(input) {
    const errors = {};
    const name = String(input.name || '').trim();
    const email = String(input.email || '').trim();
    const message = String(input.message || '').trim();
    if (!name) errors.name = 'Enter your name.';
    else if (name.length > 100) errors.name = 'Use 100 characters or fewer for your name.';
    if (email && (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))) errors.email = 'Enter a complete email address, or leave this optional field blank.';
    if (String(input.organization || '').trim().length > 150) errors.organization = 'Use 150 characters or fewer for your organization.';
    if (String(input.product || '').trim().length > 100) errors.product = 'Use 100 characters or fewer for the product or topic.';
    if (message.length < 10) errors.message = 'Add at least 10 characters about what you would like to explore.';
    else if (message.length > 2500) errors.message = 'Keep your message to 2,500 characters or fewer.';
    return errors;
  }

  function transitionInquiryContext(state, nextType, currentTopic) {
    const type = validType(nextType);
    const previousType = validType(state.type);
    const topics = { ...(state.topics || {}), [previousType]: String(currentTopic || '') };
    const connectsProducts = [previousType, type].every((value) => value === 'Product inquiry' || value === 'Strategic partner');
    const knownProduct = PRODUCT_TOPICS.some((value) => value.toLowerCase() === String(currentTopic || '').trim().toLowerCase());
    const product = Object.prototype.hasOwnProperty.call(topics, type)
      ? topics[type]
      : connectsProducts && knownProduct ? String(currentTopic || '') : '';
    return { type, product, topics: { ...topics, [type]: product } };
  }

  function topicSuggestions(type) {
    if (type === 'Product inquiry') return PRODUCT_TOPICS.slice();
    if (type === 'Strategic partner') return ['Distribution', 'Technology collaboration', 'Platform design partnership', ...PRODUCT_TOPICS];
    if (type === 'Investor') return ['Company strategy', 'Consumer app portfolio', 'App factory strategy'];
    return [];
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { formatInquiry, buildMailto, readInquiryContext, validateInquiry, transitionInquiryContext, topicSuggestions };
  }
  if (typeof document === 'undefined') return;

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  if (toggle && nav) {
    document.documentElement.classList.add('nav-enhanced');
    let open = false;
    let wasMobile = null;
    const isMobile = () => window.getComputedStyle(toggle).display !== 'none';

    function renderMenu() {
      const mobile = isMobile();
      toggle.setAttribute('aria-expanded', String(mobile && open));
      toggle.setAttribute('aria-label', mobile && open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', mobile && open);
      document.body.classList.toggle('nav-open', mobile && open);
      // This is a navigation disclosure, not a modal. Keep the normal Tab order.
      nav.inert = mobile && !open;
      if (mobile && !open) nav.setAttribute('aria-hidden', 'true');
      else nav.removeAttribute('aria-hidden');
    }

    function closeMenu(restoreFocus) {
      const hadFocus = nav.contains(document.activeElement) || document.activeElement === toggle;
      open = false;
      renderMenu();
      if (restoreFocus && hadFocus && isMobile()) toggle.focus();
    }

    toggle.addEventListener('click', () => {
      open = !open;
      renderMenu();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && open && isMobile()) {
        event.preventDefault();
        closeMenu(true);
      }
    });
    document.addEventListener('pointerdown', (event) => {
      if (open && isMobile() && !nav.contains(event.target) && !toggle.contains(event.target)) closeMenu(true);
    });
    document.addEventListener('focusin', (event) => {
      if (open && isMobile() && !nav.contains(event.target) && !toggle.contains(event.target)) closeMenu(false);
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu(false);
    });
    function syncViewport() {
      const mobile = isMobile();
      if (mobile !== wasMobile) {
        if (mobile && nav.contains(document.activeElement)) toggle.focus();
        open = false;
        wasMobile = mobile;
      }
      renderMenu();
    }
    window.addEventListener('resize', syncViewport, { passive: true });
    syncViewport();
  }

  const imageDialog = document.getElementById('image-dialog');
  const previewImage = document.getElementById('image-dialog-image');
  const previewTitle = document.getElementById('image-dialog-title');
  const previewClose = document.getElementById('image-dialog-close');
  if (imageDialog && previewImage && previewTitle && previewClose && typeof imageDialog.showModal === 'function') {
    let previewTrigger = null;
    document.querySelectorAll('a.screenshot-open').forEach((link) => {
      link.addEventListener('click', (event) => {
        // Preserve the link's native open-in-new-tab and image fallback behavior.
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        const imageUrl = new URL(link.href, window.location.href);
        if (imageUrl.origin !== window.location.origin) return;
        previewTitle.textContent = link.dataset.imageTitle || 'App preview';
        previewImage.alt = link.dataset.imageAlt || 'Official app promotional screenshot with sample content';
        previewImage.src = imageUrl.href;
        try {
          imageDialog.showModal();
          previewTrigger = link;
          document.body.classList.add('image-preview-open');
          previewClose.focus();
          event.preventDefault();
        } catch (_) {
          // If a dialog cannot open, the original anchor still opens the image.
          document.body.classList.remove('image-preview-open');
        }
      });
    });
    previewClose.addEventListener('click', () => imageDialog.close());
    imageDialog.addEventListener('click', (event) => {
      if (event.target !== imageDialog) return;
      const rect = imageDialog.getBoundingClientRect();
      const outside = event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
      if (outside) imageDialog.close();
    });
    // Native Escape/cancel closes the dialog and reaches this same cleanup path.
    imageDialog.addEventListener('close', () => {
      document.body.classList.remove('image-preview-open');
      if (previewTrigger && previewTrigger.isConnected) previewTrigger.focus();
      previewTrigger = null;
    });
  }

  if (typeof IntersectionObserver !== 'undefined') {
    document.querySelectorAll('.section-jump').forEach((jumpNav) => {
      const links = Array.from(jumpNav.querySelectorAll('a[href^="#"]'));
      const targets = links.map((link) => ({
        link,
        section: document.getElementById(link.getAttribute('href').slice(1))
      })).filter((item) => item.section);
      if (!targets.length) return;
      const visible = new Set();
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) visible.add(entry.target);
          else visible.delete(entry.target);
        });
        const active = targets.filter((item) => visible.has(item.section))
          .sort((a, b) => Math.abs(a.section.getBoundingClientRect().top - 140) - Math.abs(b.section.getBoundingClientRect().top - 140))[0];
        if (!active) return;
        targets.forEach((item) => {
          if (item === active) item.link.setAttribute('aria-current', 'location');
          else item.link.removeAttribute('aria-current');
        });
      }, { rootMargin: '-120px 0px -50% 0px', threshold: 0 });
      targets.forEach((item) => observer.observe(item.section));
    });
  }

  const form = document.getElementById('inquiry-form');
  if (!form) return;
  const type = document.getElementById('inquiry-type');
  const product = document.getElementById('product-context');
  const status = document.getElementById('form-status');
  const messageInput = document.getElementById('message');
  const review = document.getElementById('inquiry-review');
  const reviewBody = document.getElementById('review-body');
  const reviewHeading = document.getElementById('review-heading');
  const openEmail = document.getElementById('review-open-email');
  const copyButton = document.getElementById('copy-inquiry');
  const errorSummary = document.getElementById('error-summary');
  const errorList = document.getElementById('error-list');
  if (!type || !product || !status || !messageInput || !review || !reviewBody || !reviewHeading || !openEmail || !copyButton || !errorSummary || !errorList) return;

  const fields = {
    name: document.getElementById('name'),
    email: document.getElementById('email'),
    organization: document.getElementById('organization'),
    product,
    message: messageInput
  };
  if (Object.values(fields).some((field) => !field)) return;
  const fieldErrors = Object.fromEntries(Object.entries(fields).map(([key, field]) => [key, document.getElementById(field.id + '-error')]));
  if (Object.values(fieldErrors).some((error) => !error)) return;
  const touched = new Set();
  let attemptedReview = false;
  let revision = 0;
  let reviewedDraft = null;
  const context = readInquiryContext(window.location.search);
  let categoryState = { ...context, topics: { [context.type]: context.product } };
  type.value = context.type;
  product.value = context.product;

  const intentPicker = document.getElementById('intent-picker');
  const typeFallback = document.getElementById('type-fallback');
  const intentChoices = intentPicker ? Array.from(intentPicker.querySelectorAll('input[type="radio"][name="inquiry-choice"]')) : [];
  const inquiryHeading = document.getElementById('inquiry-heading');
  const inquiryDescription = document.getElementById('inquiry-description');
  const messageHelp = document.getElementById('message-help');
  const messageCount = document.getElementById('message-count');
  const topicOptions = document.getElementById('topic-options');
  const intentCopy = {
    Investor: ['Explore the company.', 'Ask about our products, company strategy, and future priorities.', 'Share your investment focus and what you would like to understand. At least 10 characters.', 'I am interested in your product strategy. My investment focus is…'],
    'Strategic partner': ['Explore a partnership.', 'Tell us about the collaboration you have in mind.', 'Describe the collaboration, what you bring, and a useful next step. At least 10 characters.', 'We would like to explore a distribution or technology partnership…'],
    'Product inquiry': ['Let’s talk products.', 'Ask about a specific app or its place in the portfolio.', 'Tell us which product interests you and what you would like to know. At least 10 characters.', 'I have a question about this product…'],
    Other: ['Start a conversation.', 'Share a little context so we can understand your inquiry.', 'A short introduction and a clear question are enough. At least 10 characters.', 'I would like to discuss…']
  };

  function values() {
    return { type: type.value, ...Object.fromEntries(Object.entries(fields).map(([key, field]) => [key, field.value])) };
  }

  function syncIntent() {
    const selected = validType(type.value);
    intentChoices.forEach((choice) => { choice.checked = choice.value === selected; });
    if (inquiryHeading) inquiryHeading.textContent = intentCopy[selected][0];
    if (inquiryDescription) inquiryDescription.textContent = intentCopy[selected][1];
    if (messageHelp) messageHelp.textContent = intentCopy[selected][2];
    messageInput.placeholder = intentCopy[selected][3];
    if (topicOptions) {
      topicOptions.replaceChildren(...topicSuggestions(selected).map((suggestion) => {
        const option = document.createElement('option');
        option.value = suggestion;
        return option;
      }));
    }
  }

  function renderErrors(errors) {
    Object.entries(fields).forEach(([key, field]) => {
      const error = (attemptedReview || touched.has(key)) ? errors[key] : '';
      fieldErrors[key].textContent = error || '';
      fieldErrors[key].hidden = !error;
      if (error) field.setAttribute('aria-invalid', 'true');
      else field.removeAttribute('aria-invalid');
    });
    errorList.replaceChildren();
    if (attemptedReview) {
      Object.entries(errors).forEach(([key, text]) => {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = '#' + fields[key].id;
        link.textContent = text;
        link.addEventListener('click', (event) => {
          event.preventDefault();
          let ancestor = fields[key].parentElement;
          while (ancestor && ancestor !== form) {
            if (ancestor.tagName === 'DETAILS') ancestor.open = true;
            ancestor = ancestor.parentElement;
          }
          fields[key].focus();
        });
        item.append(link);
        errorList.append(item);
      });
    }
    errorSummary.hidden = !attemptedReview || !Object.keys(errors).length;
  }

  function invalidateReview() {
    revision += 1;
    reviewedDraft = null;
    review.hidden = true;
    reviewBody.value = '';
    openEmail.removeAttribute('href');
    copyButton.disabled = false;
    status.textContent = '';
  }

  function updateMessageCount() {
    if (messageCount) messageCount.textContent = messageInput.value.length + ' / 2500';
  }

  if (intentPicker && typeFallback && INQUIRY_TYPES.every((value) => intentChoices.some((choice) => choice.value === value))) {
    intentChoices.forEach((choice) => {
      choice.addEventListener('change', () => {
        if (!choice.checked) return;
        type.value = validType(choice.value);
        type.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
    intentPicker.hidden = false;
    typeFallback.hidden = true;
  }

  type.addEventListener('change', () => {
    categoryState = transitionInquiryContext(categoryState, type.value, product.value);
    type.value = categoryState.type;
    product.value = categoryState.product;
    syncIntent();
    invalidateReview();
    renderErrors(validateInquiry(values()));
  });

  Object.entries(fields).forEach(([key, field]) => {
    field.addEventListener('blur', () => {
      touched.add(key);
      renderErrors(validateInquiry(values()));
    });
  });
  form.addEventListener('input', (event) => {
    // The readonly review is not source input and should never invalidate itself.
    if (event.target === reviewBody) return;
    invalidateReview();
    updateMessageCount();
    renderErrors(validateInquiry(values()));
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    attemptedReview = true;
    const input = values();
    const errors = validateInquiry(input);
    renderErrors(errors);
    if (Object.keys(errors).length) {
      invalidateReview();
      errorSummary.focus();
      return;
    }
    revision += 1;
    reviewedDraft = formatInquiry(input);
    const mailto = buildMailto(reviewedDraft);
    document.getElementById('review-to').textContent = reviewedDraft.to;
    document.getElementById('review-subject').textContent = reviewedDraft.subject;
    reviewBody.value = reviewedDraft.text;
    openEmail.href = mailto;
    const longDraftNote = document.getElementById('long-draft-note');
    if (longDraftNote) longDraftNote.hidden = mailto.length <= 1800;
    copyButton.disabled = false;
    review.hidden = false;
    status.textContent = 'Draft ready to review. Open your email app or copy the draft to send it yourself.';
    reviewHeading.focus();
  });

  document.getElementById('edit-inquiry').addEventListener('click', () => {
    invalidateReview();
    messageInput.focus();
  });

  function selectDraft() {
    if (!reviewedDraft) return;
    reviewBody.focus();
    reviewBody.select();
    status.textContent = 'Draft selected. Copy it, paste it into your email app, and send it there.';
  }
  document.getElementById('select-inquiry').addEventListener('click', selectDraft);

  copyButton.addEventListener('click', async () => {
    if (!reviewedDraft) return;
    const draft = reviewedDraft;
    const currentRevision = revision;
    copyButton.disabled = true;
    status.textContent = 'Copying your reviewed draft…';
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(draft.text);
      if (revision !== currentRevision || reviewedDraft !== draft) return;
      status.textContent = 'Draft copied. Paste it into an email to ' + CONTACT_EMAIL + ' and send it there. Nothing has been sent by this website.';
    } catch (_) {
      if (revision !== currentRevision || reviewedDraft !== draft) return;
      reviewBody.focus();
      reviewBody.select();
      status.textContent = 'Automatic copying is unavailable. Your draft is selected below. Copy it manually, then paste it into your email app.';
    } finally {
      if (revision === currentRevision && reviewedDraft === draft) copyButton.disabled = false;
    }
  });

  openEmail.addEventListener('click', (event) => {
    if (!reviewedDraft) {
      event.preventDefault();
      return;
    }
    status.textContent = 'Your browser was asked to open an email draft. Review and send it in your email app. If it does not open, copy the draft. Nothing has been sent by this website.';
  });

  syncIntent();
  updateMessageCount();
  // Keep native validation until the accessible custom flow is fully initialized.
  form.noValidate = true;
  form.querySelectorAll('button').forEach((button) => { button.disabled = false; });
  const inquiryFields = document.getElementById('inquiry-fields');
  if (inquiryFields) inquiryFields.disabled = false;
})();
