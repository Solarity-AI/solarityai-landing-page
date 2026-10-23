'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { normalize, distance, suggest } = require('./scripts/not-found.js');

// The routes the 404 page carries in data-routes.
const ROUTES = [['/', 'Home'], ['/apps/', 'Apps'], ['/apps/looks-max/', 'Looks Max'], ['/apps/iq-max/', 'IQ Max'],
  ['/apps/sleep-max/', 'Sleep Max'], ['/apps/fitness-max/', 'Fitness Max'], ['/platform/', 'Platform'],
  ['/company/', 'Company'], ['/investors-partners/', 'Investors & partners'], ['/careers/', 'Careers'],
  ['/contact/', 'Contact'], ['/press/', 'Press kit'], ['/accessibility/', 'Accessibility'], ['/privacy/', 'Privacy'], ['/website-data/', 'Website data']];
const target = (path) => (suggest(path, ROUTES) || [null])[0];

test('normalizes case, file names, encoding and slashes', () => {
  assert.equal(normalize('/Apps/Sleep-Max/index.html'), '/apps/sleep-max');
  assert.equal(normalize('//careers.html'), '/careers');
  assert.equal(normalize('/%41pps/'), '/apps');
  assert.equal(normalize('/%E0%A4%A'), '/%e0%a4%a');
  assert.equal(normalize(''), '/');
});

test('edit distance counts single changes', () => {
  assert.equal(distance('sleep', 'sleep'), 0);
  assert.equal(distance('sleepmax', 'sleep-max'), 1);
  assert.equal(distance('kitten', 'sitting'), 3);
});

test('suggests the page a typo or shortcut meant', () => {
  assert.equal(target('/apps/sleepmax'), '/apps/sleep-max/');
  assert.equal(target('/app/iq-max/'), '/apps/iq-max/');
  assert.equal(target('/sleep-max'), '/apps/sleep-max/');
  assert.equal(target('/fitnes-max'), '/apps/fitness-max/');
  assert.equal(target('/investors'), '/investors-partners/');
  assert.equal(target('/carrers/'), '/careers/');
  assert.equal(target('/Platform.html'), '/platform/');
  assert.equal(target('/about'), '/company/');
  assert.equal(target('/privacy'), '/privacy/');
  assert.equal(target('/cookies'), '/website-data/');
});

test('an address under a real page suggests that page', () => {
  assert.equal(target('/apps/looks-max/extra'), '/apps/looks-max/');
  assert.equal(target('/company/team/hasan'), '/company/');
  assert.equal(target('/careers/full-stack-engineer'), '/careers/');
  assert.equal(target('/about-us'), '/company/');
});

test('stays quiet when nothing is close', () => {
  assert.equal(suggest('/wp-login.php', ROUTES), null);
  assert.equal(suggest('/blog/2019/hello-world', ROUTES), null);
  assert.equal(suggest('/', ROUTES), null);
  assert.equal(suggest('/xyz', ROUTES), null);
});

test('only plain same-site paths become links', () => {
  const { safePath } = require('./scripts/not-found.js');
  for (const route of ROUTES) assert.equal(safePath(route[0]), route[0]);
  for (const bad of ['javascript:alert(1)', 'https://example.com/', '//example.com/', '/apps/<b>', '/apps?x=1', '', null]) {
    assert.equal(safePath(bad), null, String(bad));
  }
});
