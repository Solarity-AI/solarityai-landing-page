const test = require('node:test');
const assert = require('node:assert/strict');
const { readInquiryContext, buildContactMailto, contactContextLabel } = require('./scripts/contact.js');

test('product and partnership arrivals retain context without collecting unrelated URL data', () => {
  assert.deepEqual(readInquiryContext('?type=Product+inquiry&product=Fitness+Max&email=personal@example.com'), { type: 'Product inquiry', product: 'Fitness Max' });
  assert.deepEqual(readInquiryContext('?type=Strategic+partner&product=Distribution'), { type: 'Strategic partner', product: 'Distribution' });
  assert.deepEqual(readInquiryContext('?type=Investor&product=Fitness+Max'), { type: 'Investor', product: '' });
  assert.deepEqual(readInquiryContext('?type=%3Cscript%3E&product=Wrong'), { type: 'Other', product: '' });
  assert.deepEqual(readInquiryContext(''), { type: 'Other', product: '' });
});

test('email destinations preserve Unicode and punctuation without adding mail headers', () => {
  const context = { type: 'Strategic partner', product: 'Çağrı & R&D / A+B #2' };
  const url = new URL(buildContactMailto(context));
  assert.equal(url.pathname, 'ata.turhan@solarityai.com');
  assert.deepEqual([...url.searchParams.keys()], ['subject']);
  assert.equal(url.searchParams.get('subject'), 'Solarity AI | Strategic partner | Çağrı & R&D / A+B #2');
  assert.equal(contactContextLabel(context), 'Strategic partner: Çağrı & R&D / A+B #2');
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
  assert.equal(contactContextLabel({ type: 'Product inquiry', product: 'Sleep Max' }), 'Product inquiry: Sleep Max');
  assert.equal(contactContextLabel({ type: '<script>' }), 'Start with an introduction.');
  assert.equal(new URL(buildContactMailto({ type: 'Other', product: 'Ignored' })).searchParams.get('subject'), 'Solarity AI | Other');
});

test('topic length limits keep Unicode pairs intact and malformed input cannot crash email links', () => {
  const truncated = readInquiryContext('?type=Product+inquiry&product=' + encodeURIComponent('A'.repeat(99) + '🌞'));
  assert.equal(truncated.product, 'A'.repeat(99));
  const preserved = readInquiryContext('?type=Product+inquiry&product=' + encodeURIComponent('A'.repeat(98) + '🌞'));
  assert.equal(preserved.product, 'A'.repeat(98) + '🌞');
  const url = new URL(buildContactMailto({ type: 'Product inquiry', product: '\uD800&bcc=other@example.com' }));
  assert.equal(url.searchParams.get('subject'), 'Solarity AI | Product inquiry | �&bcc=other@example.com');
  assert.deepEqual([...url.searchParams.keys()], ['subject']);
});

test('program reviewers get their own subject and never carry a product', () => {
  assert.deepEqual(readInquiryContext('?type=Program&product=Anything'), { type: 'Program', product: '' });
  assert.equal(new URL(buildContactMailto({ type: 'Program', product: 'Ignored' })).searchParams.get('subject'), 'Solarity AI | Program');
  assert.equal(contactContextLabel({ type: 'Program' }), 'An accelerator, incubator, or grant program.');
});
