'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, 'scripts/sections.js'), 'utf8');

// A page with three answers, a "Show all answers" button, and a sticky index over two sections.
function harness({ hash = '', frames = true } = {}) {
  const listeners = {};
  const elements = {};
  const details = ['faq-one', 'faq-two', 'faq-three'].map((id) => {
    const item = { id, open: false, closest: (selector) => (selector === 'details' ? item : null) };
    elements[id] = item;
    return item;
  });
  const answer = { closest: (selector) => (selector === 'details' ? details[1] : null) };
  elements['answer-text'] = answer;
  const list = { querySelectorAll: () => details, addEventListener(type, callback) { listeners['list-' + type] = callback; } };
  elements['investor-answers'] = list;
  const attributes = { 'aria-controls': 'investor-answers' };
  const button = {
    hidden: true, textContent: 'Show all answers',
    getAttribute: (name) => attributes[name] ?? null,
    setAttribute(name, value) { attributes[name] = value; },
    addEventListener(type, callback) { listeners['button-' + type] = callback; },
  };
  const links = ['#record', '#founder'].map((href) => {
    const own = { href };
    return { own, getAttribute: (name) => own[name] ?? null, setAttribute(name, value) { own[name] = value; }, removeAttribute(name) { delete own[name]; } };
  });
  const boxes = { record: { top: 900, bottom: 1800 }, founder: { top: 1800, bottom: 2400 } };
  const sections = ['record', 'founder'].map((id) => (elements[id] = { id, getBoundingClientRect: () => boxes[id] }));
  const nav = { querySelectorAll: () => links };
  const window = {
    innerHeight: 900,
    location: { hash, pathname: '/investors-partners/' },
    addEventListener(type, callback) { listeners['window-' + type] = callback; },
  };
  // Frames run later, as in a browser: scrollTo() flushes them.
  const queue = [];
  if (frames) window.requestAnimationFrame = (callback) => queue.push(callback);
  const document = {
    readyState: 'complete',
    documentElement: { classList: { add() {}, remove() {}, toggle() {} } },
    querySelector: () => null,
    querySelectorAll: (selector) => (selector === 'button[data-answers-toggle]' ? [button] : selector === 'nav.saas-index' ? [nav] : []),
    getElementById: (id) => elements[id] || null,
  };
  vm.runInNewContext(source, { window, document });
  // Scroll so the page's sections sit at the given window positions.
  function scrollTo(record, founder) {
    boxes.record = { top: record, bottom: record + 900 };
    boxes.founder = { top: founder, bottom: founder + 600 };
    listeners['window-scroll']();
    while (queue.length) queue.shift()();
  }
  const current = () => links.map((link) => link.own['aria-current'] ?? null);
  while (queue.length) queue.shift()();
  return { window, details, button, attributes, links, sections, listeners, scrollTo, current };
}

test('arriving at an answer link opens that answer only', () => {
  const page = harness({ hash: '#faq-two' });
  assert.deepEqual(page.details.map((item) => item.open), [false, true, false]);
});

test('a link to text inside an answer opens its answer, and later links open theirs', () => {
  const page = harness({ hash: '#answer-text' });
  assert.equal(page.details[1].open, true);
  page.window.location.hash = '#faq-three';
  page.listeners['window-hashchange']();
  assert.equal(page.details[2].open, true);
});

test('a malformed or unknown fragment changes nothing', () => {
  for (const hash of ['#%E0%A4%A', '#missing', '']) {
    const page = harness({ hash });
    assert.deepEqual(page.details.map((item) => item.open), [false, false, false]);
  }
});

test('show all answers appears with JavaScript and toggles every answer', () => {
  const page = harness();
  assert.equal(page.button.hidden, false);
  assert.equal(page.attributes['aria-expanded'], 'false');
  page.listeners['button-click']();
  assert.deepEqual(page.details.map((item) => item.open), [true, true, true]);
  assert.equal(page.button.textContent, 'Hide all answers');
  assert.equal(page.attributes['aria-expanded'], 'true');
  page.details[0].open = false;
  page.listeners['list-toggle']();
  assert.equal(page.button.textContent, 'Show all answers');
  page.listeners['button-click']();
  assert.ok(page.details.every((item) => item.open));
  page.listeners['button-click']();
  assert.ok(page.details.every((item) => !item.open));
});

test('the sticky index marks the section crossing the reading line', () => {
  const page = harness();
  assert.deepEqual(page.current(), [null, null]);
  page.scrollTo(100, 1000);
  assert.deepEqual(page.current(), ['location', null]);
  page.scrollTo(-700, 200);
  assert.deepEqual(page.current(), [null, 'location']);
  page.scrollTo(-2000, -1100);
  assert.deepEqual(page.current(), [null, null]);
});

test('without animation frames the index stays plain', () => {
  const page = harness({ frames: false });
  assert.equal(page.listeners['window-scroll'], undefined);
  assert.deepEqual(page.current(), [null, null]);
});
