(function () {
  'use strict';
  const CONTACT_EMAIL = 'ata.turhan@solarityai.com';
  const INQUIRY_TYPES = ['Investor', 'Program', 'Strategic partner', 'Product inquiry', 'Press', 'Other'];
  const unicodeText = (value) => String(value || '').replace(/[\uD800-\uDBFF][\uDC00-\uDFFF]|[\uD800-\uDFFF]/g, (character) => character.length === 2 ? character : '\uFFFD');
  const cleanTopic = (value) => unicodeText(value).replace(/[\u0000-\u001f\u007f]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 100).replace(/[\uD800-\uDBFF]$/, '');
  const validType = (value) => INQUIRY_TYPES.includes(value) ? value : 'Other';
  // The topics the site's own links pass (the apps and the partnership topics; check_site.py keeps this in step).
  // Anything else is dropped, so a crafted link cannot put its own text on the page or in the subject.
  const CONTEXT_TOPICS = ['Looks Max', 'IQ Max', 'Sleep Max', 'Fitness Max', 'App factory', 'Distribution', 'Technology collaboration', 'SaaS products'];
  const topicKey = (value) => cleanTopic(value).toLowerCase();
  const knownTopic = (value) => CONTEXT_TOPICS.find((topic) => topic.toLowerCase() === topicKey(value)) || '';

  function readInquiryContext(search) {
    const params = new URLSearchParams(search);
    const type = validType(params.get('type'));
    const acceptsContext = type === 'Product inquiry' || type === 'Strategic partner';
    return { type, product: acceptsContext ? knownTopic(params.get('product')) : '' };
  }

  function buildContactMailto(context) {
    const type = validType(context.type);
    const product = ['Product inquiry', 'Strategic partner'].includes(type) ? knownTopic(context.product) : '';
    const subject = 'Solarity AI | ' + type + (product ? ' | ' + product : '');
    return 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject);
  }

  function contactContextLabel(context) {
    const labels = {
      Investor: 'An investment conversation.',
      Program: 'An accelerator, incubator, or grant program.',
      'Strategic partner': 'A potential partnership.',
      'Product inquiry': 'A product conversation.',
      Press: 'A press or media request.',
      Other: 'Start with an introduction.'
    };
    const type = validType(context.type);
    const product = ['Product inquiry', 'Strategic partner'].includes(type) ? knownTopic(context.product) : '';
    // The topic follows the type's own sentence, as visitors read it, not the internal type name
    return product ? labels[type].replace(/\.$/, '') + ': ' + product + '.' : labels[type];
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { readInquiryContext, buildContactMailto, contactContextLabel, CONTEXT_TOPICS };
  }
  if (typeof document === 'undefined') return;
  const emailLink = document.getElementById('contact-email');
  const contextLabel = document.getElementById('contact-context');
  if (!emailLink || !contextLabel) return;

  function syncContext() {
    const context = readInquiryContext(window.location.search);
    emailLink.href = buildContactMailto(context);
    contextLabel.textContent = contactContextLabel(context);
    contextLabel.title = contactContextLabel(context);
    document.querySelectorAll('a[data-inquiry-type]').forEach((link) => {
      link.href = buildContactMailto({ type: link.getAttribute('data-inquiry-type'), product: context.product });
    });
  }
  syncContext();
  window.addEventListener('popstate', syncContext);
  window.addEventListener('pageshow', syncContext);
})();
