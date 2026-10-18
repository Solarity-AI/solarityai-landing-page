'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, 'scripts/navigation.js'), 'utf8');

function harness({ readyState = 'loading', mobile = true, header = true } = {}) {
  let currentMobile = mobile;
  let headerAvailable = readyState !== 'loading';
  const lookups = [];

  function eventTarget() {
    const listeners = new Map();
    return {
      addEventListener(type, callback, options) {
        const entries = listeners.get(type) || [];
        entries.push({ callback, once: Boolean(options && options.once) });
        listeners.set(type, entries);
      },
      removeEventListener(type, callback) {
        listeners.set(type, (listeners.get(type) || []).filter((entry) => entry.callback !== callback));
      },
      listenerCount(type) {
        return (listeners.get(type) || []).length;
      },
      emit(type, properties = {}) {
        const event = {
          type,
          target: this,
          defaultPrevented: false,
          preventDefault() { this.defaultPrevented = true; },
          ...properties,
        };
        for (const entry of [...(listeners.get(type) || [])]) {
          if (entry.once) {
            listeners.set(type, listeners.get(type).filter((item) => item !== entry));
          }
          entry.callback(event);
        }
        return event;
      },
    };
  }

  function classList() {
    const values = new Set();
    return {
      add(...names) { names.forEach((name) => values.add(name)); },
      remove(...names) { names.forEach((name) => values.delete(name)); },
      contains(name) { return values.has(name); },
      toggle(name, force) {
        const on = force === undefined ? !values.has(name) : Boolean(force);
        if (on) values.add(name);
        else values.delete(name);
        return on;
      },
    };
  }

  const document = {
    ...eventTarget(),
    readyState,
    activeElement: null,
    documentElement: { classList: classList() },
    querySelector(selector) {
      lookups.push(selector);
      return headerAvailable && header && selector === '.menu-toggle' ? toggle : null;
    },
    getElementById(id) {
      lookups.push(id);
      return headerAvailable && header && id === 'site-nav' ? nav : null;
    },
  };

  function element(tagName, parent = null) {
    const attributes = new Map();
    return {
      ...eventTarget(),
      tagName: tagName.toUpperCase(),
      parentElement: parent,
      classList: classList(),
      inert: false,
      setAttribute(name, value) { attributes.set(name, String(value)); },
      getAttribute(name) { return attributes.has(name) ? attributes.get(name) : null; },
      removeAttribute(name) { attributes.delete(name); },
      contains(candidate) {
        for (let item = candidate; item; item = item.parentElement) {
          if (item === this) return true;
        }
        return false;
      },
      closest(selector) {
        for (let item = this; item; item = item.parentElement) {
          if (selector === 'a' && item.tagName === 'A') return item;
        }
        return null;
      },
      focus() {
        document.activeElement = this;
        document.emit('focusin', { target: this });
      },
    };
  }

  const body = element('body');
  document.body = readyState === 'loading' ? null : body;
  const toggle = element('button', body);
  const nav = element('nav', body);
  const link = element('a', nav);
  const linkText = element('span', link);
  const outside = element('button', body);
  const window = {
    ...eventTarget(),
    getComputedStyle(node) {
      assert.equal(node, toggle, 'viewport detection should inspect the real menu toggle');
      return { display: currentMobile ? 'flex' : 'none' };
    },
  };

  vm.runInNewContext(source, { document, window }, { filename: 'scripts/navigation.js' });

  return {
    document, window, body, toggle, nav, link, linkText, outside, lookups,
    ready() {
      headerAvailable = true;
      document.body = body;
      document.readyState = 'interactive';
      document.emit('DOMContentLoaded');
    },
    resize(nextMobile) {
      currentMobile = nextMobile;
      window.emit('resize');
    },
  };
}

function assertClosedMobile(view) {
  assert.equal(view.toggle.getAttribute('aria-expanded'), 'false');
  assert.equal(view.toggle.getAttribute('aria-label'), 'Open navigation');
  assert.equal(view.nav.inert, true);
  assert.equal(view.nav.getAttribute('aria-hidden'), 'true');
  assert.equal(view.nav.classList.contains('is-open'), false);
  assert.equal(view.body.classList.contains('nav-open'), false);
}

function assertOpenMobile(view) {
  assert.equal(view.toggle.getAttribute('aria-expanded'), 'true');
  assert.equal(view.toggle.getAttribute('aria-label'), 'Close navigation');
  assert.equal(view.nav.inert, false);
  assert.equal(view.nav.getAttribute('aria-hidden'), null);
  assert.equal(view.nav.classList.contains('is-open'), true);
  assert.equal(view.body.classList.contains('nav-open'), true);
}

test('smooth in-page scrolling starts with the first interaction, never during load', () => {
  for (const input of ['pointerdown', 'keydown']) {
    const view = harness();
    view.ready();
    view.window.emit('load');
    assert.equal(view.document.documentElement.classList.contains('smooth-scroll'), false);
    view.window.emit(input);
    assert.equal(view.document.documentElement.classList.contains('smooth-scroll'), true);
    // Both one-time listeners are released after the first interaction.
    assert.equal(view.window.listenerCount('pointerdown') + view.window.listenerCount('keydown'), 0);
  }
});

test('head startup establishes mobile CSS before querying a not-yet-parsed header', () => {
  const view = harness();
  assert.equal(view.document.body, null);
  assert.equal(view.document.documentElement.classList.contains('nav-enhanced'), true);
  assert.deepEqual(view.lookups, []);
});

test('DOMContentLoaded initializes a closed, non-focusable mobile menu', () => {
  const view = harness();
  view.ready();
  assertClosedMobile(view);
  // Repeated readiness must not attach duplicate handlers.
  view.document.emit('DOMContentLoaded');
  view.toggle.emit('click');
  assertOpenMobile(view);
});

test('toggle and Escape expose the menu then restore keyboard focus', () => {
  const view = harness();
  view.ready();
  view.toggle.focus();
  view.toggle.emit('click');
  assertOpenMobile(view);
  view.link.focus();
  const event = view.document.emit('keydown', { key: 'Escape' });
  assert.equal(event.defaultPrevented, true);
  assertClosedMobile(view);
  assert.equal(view.document.activeElement, view.toggle);
  assert.equal(view.document.emit('keydown', { key: 'Escape' }).defaultPrevented, false);
});

test('a second toggle click closes the disclosure', () => {
  const view = harness();
  view.ready();
  view.toggle.emit('click');
  view.toggle.emit('click');
  assertClosedMobile(view);
});

test('inside pointer events preserve the menu and outside pointer events close it', () => {
  const view = harness();
  view.ready();
  view.toggle.emit('click');
  view.link.focus();
  view.document.emit('pointerdown', { target: view.linkText });
  assertOpenMobile(view);
  view.document.emit('pointerdown', { target: view.toggle });
  assertOpenMobile(view);
  view.document.emit('pointerdown', { target: view.outside });
  assertClosedMobile(view);
  assert.equal(view.document.activeElement, view.toggle);
});

test('focus leaving the disclosure closes it without stealing the new focus', () => {
  const view = harness();
  view.ready();
  view.toggle.emit('click');
  view.link.focus();
  assertOpenMobile(view);
  view.outside.focus();
  assertClosedMobile(view);
  assert.equal(view.document.activeElement, view.outside);
});

test('activation within a navigation link closes the menu without blocking navigation', () => {
  const view = harness();
  view.ready();
  view.toggle.emit('click');
  const event = view.nav.emit('click', { target: view.linkText });
  assertClosedMobile(view);
  assert.equal(event.defaultPrevented, false);
});

test('crossing the mobile breakpoint preserves desktop access and resets mobile state', () => {
  const view = harness();
  view.ready();
  view.toggle.emit('click');
  view.resize(false);
  assert.equal(view.nav.inert, false);
  assert.equal(view.nav.getAttribute('aria-hidden'), null);
  assert.equal(view.toggle.getAttribute('aria-expanded'), 'false');
  assert.equal(view.nav.classList.contains('is-open'), false);
  assert.equal(view.body.classList.contains('nav-open'), false);
  view.link.focus();
  view.resize(true);
  assertClosedMobile(view);
  assert.equal(view.document.activeElement, view.toggle);
});

test('late execution initializes immediately after the DOM is already ready', () => {
  const view = harness({ readyState: 'complete' });
  assert.equal(view.document.documentElement.classList.contains('nav-enhanced'), true);
  assertClosedMobile(view);
  view.toggle.emit('click');
  assertOpenMobile(view);
});

test('desktop initialization never hides or inerts the navigation', () => {
  const view = harness({ mobile: false });
  view.ready();
  assert.equal(view.nav.inert, false);
  assert.equal(view.nav.getAttribute('aria-hidden'), null);
  assert.equal(view.toggle.getAttribute('aria-expanded'), 'false');
  view.resize(true);
  assertClosedMobile(view);
});

test('a missing header removes enhancement so fallback navigation is not suppressed', () => {
  const view = harness({ header: false });
  assert.equal(view.document.documentElement.classList.contains('nav-enhanced'), true);
  view.ready();
  assert.equal(view.document.documentElement.classList.contains('nav-enhanced'), false);
});
