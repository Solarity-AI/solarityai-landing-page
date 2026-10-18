const test = require('node:test');
const assert = require('node:assert/strict');
const { readCareerRole, parseWebUrl, isLinkedInProfile, isEmailAddress, validateCareerApplication, isPlainActivation } = require('./scripts/careers.js');

const application = {
  fullName: 'Çağrı O’Neil', email: 'person.name+careers@gmail.com',
  linkedin: 'https://www.linkedin.com/in/person-name/',
  portfolio: 'https://github.com/person-name', position: 'full-stack-engineer', workType: 'full-time'
};

test('a complete application accepts Unicode names, email plus-addressing, and real profile URLs', () => {
  assert.deepEqual(validateCareerApplication(application), {});
  assert.deepEqual(validateCareerApplication({ ...application, fullName: '  Ada Lovelace  ', email: 'Person.Name@GMAIL.COM', linkedin: 'https://linkedin.com/in/ada?trk=profile', portfolio: 'http://example.com/work', position: 'marketing-specialist', workType: 'part-time' }), {});
  assert.deepEqual(validateCareerApplication({ ...application, position: 'business-development-manager', workType: 'intern' }), {});
});

test('required fields report every problem without accepting unknown role or work-type values', () => {
  assert.deepEqual(Object.keys(validateCareerApplication({})), ['fullName', 'email', 'position', 'workType']);
  const errors = validateCareerApplication({ ...application, fullName: ' \t ', position: 'CEO', workType: 'contractor' });
  assert.deepEqual(Object.keys(errors), ['fullName', 'position', 'workType']);
});

test('email validation accepts different providers and rejects headers and malformed domains', () => {
  for (const email of ['person@example.com', 'person@googlemail.com', 'person@solarityai.com', 'PERSON+work@EXAMPLE.ORG']) assert.equal(isEmailAddress(email), true, email);
  for (const email of ['person', 'person@', '@example.com', 'person@example.com,other@example.com', 'Person <person@example.com>', 'person@example.com\r\nBcc:other@example.com', 'person@-example.com', 'person@example..com', 'a'.repeat(243) + '@example.com']) assert.equal(isEmailAddress(email), false, email);
});

test('optional work links can be omitted but still receive validation when supplied', () => {
  assert.deepEqual(validateCareerApplication({ ...application, linkedin: '', portfolio: '' }), {});
  assert.deepEqual(validateCareerApplication({ ...application, linkedin: undefined, portfolio: '   ' }), {});
  assert.deepEqual(Object.keys(validateCareerApplication({ ...application, linkedin: 'invalid', portfolio: 'invalid' })), ['linkedin', 'portfolio']);
});

test('LinkedIn validation requires HTTPS and a personal-profile path on the exact host', () => {
  for (const linkedin of ['http://www.linkedin.com/in/person', 'https://linkedin.com.evil.test/in/person', 'https://linkedin.com@evil.test/in/person', 'https://user@linkedin.com/in/person', 'https://linkedin.com/company/solarity', 'https://linkedin.com/in/', 'https://linkedin.com/in/person/extra', 'https://linkedin.com:8443/in/person', 'https://linkedin.com/in/%2Fperson', 'https://linkedin.com/in/%5Cperson', 'https://linkedin.com/in/%00', 'https://linkedin.com/in/%ZZ', 'https://linkedin.com/in/person name']) {
    assert.equal(isLinkedInProfile(linkedin), false, linkedin);
  }
  assert.equal(isLinkedInProfile('https://WWW.LINKEDIN.COM/in/person-name/'), true);
  assert.equal(isLinkedInProfile('https://linkedin.com/in/cagri-%C3%B6z'), true);
});

test('portfolio validation permits HTTP and HTTPS while rejecting unsafe, malformed, or credential-bearing destinations', () => {
  for (const portfolio of ['javascript:alert(1)', 'data:text/html,hello', 'ftp://example.com', 'example.com', 'https://', 'https:example.com', 'http:/example.com', '//example.com', 'https://user:password@example.com', 'https://example.com/path with spaces', 'https://example.com\\@evil.test', 'https://exam\nple.com']) {
    assert.equal(parseWebUrl(portfolio), null, portfolio);
  }
  for (const portfolio of ['https://linktr.ee/name', 'https://example.com/work?project=1&view=full#details', 'http://example.com', 'https://例え.テスト/作品']) {
    assert.ok(parseWebUrl(portfolio), portfolio);
  }
});

test('name and URL limits are enforced without silently truncating submitted information', () => {
  assert.ok(validateCareerApplication({ ...application, fullName: ' A ' }).fullName);
  assert.deepEqual(validateCareerApplication({ ...application, fullName: 'Li' }), {});
  assert.deepEqual(validateCareerApplication({ ...application, fullName: 'A'.repeat(100) }), {});
  assert.ok(validateCareerApplication({ ...application, fullName: 'A'.repeat(101) }).fullName);
  assert.ok(validateCareerApplication({ ...application, fullName: 'Ada\nLovelace' }).fullName);
  const urlAtLimit = 'https://example.com/' + 'a'.repeat(480);
  assert.equal(urlAtLimit.length, 500);
  assert.ok(parseWebUrl(urlAtLimit));
  assert.equal(parseWebUrl(urlAtLimit + 'a'), null);
  assert.ok(validateCareerApplication({ ...application, portfolio: urlAtLimit + 'a' }).portfolio);
});

test('role query context is allowlisted and unrelated or personal URL parameters have no effect', () => {
  assert.equal(readCareerRole('?role=full-stack-engineer'), 'full-stack-engineer');
  assert.equal(readCareerRole('?role=marketing-specialist&email=someone%40gmail.com&success=true'), 'marketing-specialist');
  assert.equal(readCareerRole('?role=business-development-manager'), 'business-development-manager');
  for (const query of ['', '?role=CEO', '?role=%3Cscript%3E', '?role=FULL-STACK-ENGINEER', '?success=true&name=Someone']) assert.equal(readCareerRole(query), '');
});

test('role enhancement preserves modified clicks, other buttons, downloads, and new-tab targets', () => {
  const link = { target: '', hasAttribute: () => false };
  assert.equal(isPlainActivation({ button: 0 }, link), true);
  assert.equal(isPlainActivation({}, link), true);
  for (const event of [{ button: 1 }, { button: 2 }, { ctrlKey: true }, { metaKey: true }, { shiftKey: true }, { altKey: true }, { defaultPrevented: true }]) assert.equal(isPlainActivation(event, link), false);
  assert.equal(isPlainActivation({ button: 0 }, { ...link, target: '_blank' }), false);
  assert.equal(isPlainActivation({ button: 0 }, { ...link, target: '_self' }), true);
  assert.equal(isPlainActivation({ button: 0 }, { ...link, hasAttribute: (name) => name === 'download' }), false);
});
