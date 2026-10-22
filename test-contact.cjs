const test = require('node:test');
const assert = require('node:assert/strict');
const { readInquiryContext, buildContactMailto, contactContextLabel, CONTEXT_TOPICS } = require('./scripts/contact.js');

test('product and partnership arrivals retain context without collecting unrelated URL data', () => {
  assert.deepEqual(readInquiryContext('?type=Product+inquiry&product=Fitness+Max&email=personal@example.com'), { type: 'Product inquiry', product: 'Fitness Max' });
  assert.deepEqual(readInquiryContext('?type=Strategic+partner&product=Distribution'), { type: 'Strategic partner', product: 'Distribution' });
  assert.deepEqual(readInquiryContext('?type=Investor&product=Fitness+Max'), { type: 'Investor', product: '' });
  assert.deepEqual(readInquiryContext('?type=%3Cscript%3E&product=Wrong'), { type: 'Other', product: '' });
  assert.deepEqual(readInquiryContext(''), { type: 'Other', product: '' });
});

test('email destinations carry a known topic without adding mail headers', () => {
  const context = { type: 'Strategic partner', product: 'Technology collaboration' };
  const url = new URL(buildContactMailto(context));
  assert.equal(url.pathname, 'ata.turhan@solarityai.com');
  assert.deepEqual([...url.searchParams.keys()], ['subject']);
  assert.equal(url.searchParams.get('subject'), 'Solarity AI | Strategic partner | Technology collaboration');
  assert.equal(contactContextLabel(context), 'A potential partnership: Technology collaboration.');
});

test('only the site\'s own topics are shown, so a crafted link cannot put its text on the page', () => {
  for (const crafted of ['Send your password to x', 'Çağrı & R&D / A+B #2', '<img src=x onerror=alert(1)>', 'Looks Max!', 'Looks Max Pro']) {
    const context = readInquiryContext('?type=Product+inquiry&product=' + encodeURIComponent(crafted));
    assert.equal(context.product, '', crafted);
    assert.equal(contactContextLabel({ type: 'Product inquiry', product: crafted }), 'A product conversation.', crafted);
    assert.equal(new URL(buildContactMailto({ type: 'Product inquiry', product: crafted })).searchParams.get('subject'), 'Solarity AI | Product inquiry', crafted);
  }
  // Known topics keep their canonical spelling, whatever the case or spacing in the link.
  assert.equal(readInquiryContext('?type=Product+inquiry&product=looks%20%20max').product, 'Looks Max');
  assert.equal(readInquiryContext('?type=Strategic+partner&product=WEB+APPS').product, 'Web apps');
  assert.deepEqual([...CONTEXT_TOPICS].sort(), ['App factory', 'Distribution', 'Fitness Max', 'IQ Max', 'Looks Max', 'Sleep Max', 'Technology collaboration', 'Web apps']);
});

test('untrusted type and line breaks cannot create email recipients or headers', () => {
  const url = new URL(buildContactMailto({ type: 'Investor\r\nBcc: other@example.com', product: 'Ignored' }));
  assert.equal(url.searchParams.get('subject'), 'Solarity AI | Other');
  const injected = new URL(buildContactMailto({ type: 'Product inquiry', product: 'IQ Max\r\nBcc: nope&bcc=bad@example.com' }));
  assert.doesNotMatch(injected.searchParams.get('subject'), /[\r\n]/);
  assert.deepEqual([...injected.searchParams.keys()], ['subject']);
});

test('context labels use established inquiry categories and omit stale product context', () => {
  assert.equal(contactContextLabel({ type: 'Investor', product: 'Fitness Max' }), 'An investment conversation.');
  assert.equal(contactContextLabel({ type: 'Product inquiry', product: 'Sleep Max' }), 'A product conversation: Sleep Max.');
  assert.equal(contactContextLabel({ type: '<script>' }), 'Start with an introduction.');
  assert.equal(new URL(buildContactMailto({ type: 'Other', product: 'Ignored' })).searchParams.get('subject'), 'Solarity AI | Other');
});

test('long, broken or header-like input cannot crash email links or add headers', () => {
  assert.equal(readInquiryContext('?type=Product+inquiry&product=' + encodeURIComponent('A'.repeat(5000) + '🌞')).product, '');
  assert.equal(readInquiryContext('?type=Product+inquiry&product=%E0%A4%A').product, '');
  const url = new URL(buildContactMailto({ type: 'Product inquiry', product: '\uD800&bcc=other@example.com' }));
  assert.equal(url.searchParams.get('subject'), 'Solarity AI | Product inquiry');
  assert.deepEqual([...url.searchParams.keys()], ['subject']);
});

test('program reviewers get their own subject and never carry a product', () => {
  assert.deepEqual(readInquiryContext('?type=Program&product=Anything'), { type: 'Program', product: '' });
  assert.equal(new URL(buildContactMailto({ type: 'Program', product: 'Ignored' })).searchParams.get('subject'), 'Solarity AI | Program');
  assert.equal(contactContextLabel({ type: 'Program' }), 'An accelerator, incubator, or grant program.');
  // Press requests have their own subject, so they are not filed as Other
  assert.deepEqual(readInquiryContext('?type=Press'), { type: 'Press', product: '' });
  assert.equal(new URL(buildContactMailto({ type: 'Press' })).searchParams.get('subject'), 'Solarity AI | Press');
  assert.equal(contactContextLabel({ type: 'Press' }), 'A press or media request.');
});
