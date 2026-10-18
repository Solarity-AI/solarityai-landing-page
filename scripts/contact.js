(function () {
  'use strict';
  const CONTACT_EMAIL = 'ata.turhan@solarityai.com';
  const INQUIRY_TYPES = ['Investor', 'Strategic partner', 'Product inquiry', 'Other'];
  const unicodeText = (value) => String(value || '').replace(/[\uD800-\uDBFF][\uDC00-\uDFFF]|[\uD800-\uDFFF]/g, (character) => character.length === 2 ? character : '\uFFFD');
  const cleanTopic = (value) => unicodeText(value).replace(/[\u0000-\u001f\u007f]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 100).replace(/[\uD800-\uDBFF]$/, '');
  const validType = (value) => INQUIRY_TYPES.includes(value) ? value : 'Other';

  function readInquiryContext(search) {
    const params = new URLSearchParams(search);
    const type = validType(params.get('type'));
    const acceptsContext = type === 'Product inquiry' || type === 'Strategic partner';
    return { type, product: acceptsContext ? cleanTopic(params.get('product')) : '' };
  }

  function buildContactMailto(context) {
    const type = validType(context.type);
    const product = ['Product inquiry', 'Strategic partner'].includes(type) ? cleanTopic(context.product) : '';
    const subject = 'Solarity AI | ' + type + (product ? ' | ' + product : '');
    return 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject);
  }

  function contactContextLabel(context) {
    const labels = {
      Investor: 'An investment conversation.',
      'Strategic partner': 'A potential partnership.',
      'Product inquiry': 'A product conversation.',
      Other: 'Start with an introduction.'
    };
    const type = validType(context.type);
    const product = ['Product inquiry', 'Strategic partner'].includes(type) ? cleanTopic(context.product) : '';
    return product ? type + ': ' + product : labels[type];
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { readInquiryContext, buildContactMailto, contactContextLabel };
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
