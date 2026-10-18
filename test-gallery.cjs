'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, 'scripts/gallery.js'), 'utf8');

// A source-level event harness, not a browser or native-dialog rendering test.
function harness({ supported = true, missingDialog = false, failOpen = false, href = '/assets/app-screen.webp' } = {}) {
  const classes = new Set();
  const document = {
    activeElement: null,
    body: { classList: { add: (name) => classes.add(name), remove: (name) => classes.delete(name) } },
    getElementById(id) { return nodes[id] || null; },
    querySelectorAll(selector) { return selector === 'a.screenshot-open' ? [link] : []; },
  };
  function element() {
    const listeners = new Map();
    return {
      isConnected: true,
      textContent: '',
      addEventListener(type, listener) {
        const entries = listeners.get(type) || [];
        entries.push(listener);
        listeners.set(type, entries);
      },
      emit(type, properties = {}) {
        const event = {
          target: this, button: 0, defaultPrevented: false,
          preventDefault() { this.defaultPrevented = true; },
          ...properties,
        };
        for (const listener of listeners.get(type) || []) listener(event);
        return event;
      },
      focus() { document.activeElement = this; },
    };
  }
  const link = { ...element(), href, dataset: { imageTitle: 'Looks Max screenshot', imageAlt: 'Official app preview' } };
  const closeButton = element();
  const image = element();
  const title = element();
  const dialog = {
    ...element(), open: false, closeCalls: 0,
    getBoundingClientRect() { return { left: 100, right: 700, top: 50, bottom: 700 }; },
    close() { this.open = false; this.closeCalls += 1; this.emit('close'); },
  };
  if (supported) dialog.showModal = function () {
    if (failOpen) throw new Error('Dialog unavailable');
    this.open = true;
  };
  const nodes = {
    'image-dialog': missingDialog ? null : dialog,
    'image-dialog-image': image,
    'image-dialog-title': title,
    'image-dialog-close': closeButton,
  };
  const window = { location: { href: 'https://example.com/apps/looks-max', origin: 'https://example.com' } };
  vm.runInNewContext(source, { document, window, URL }, { filename: 'scripts/gallery.js' });
  return { document, link, closeButton, image, title, dialog, classes };
}

test('unmodified screenshot activation opens the preview and moves focus to Close', () => {
  const view = harness();
  const event = view.link.emit('click');
  assert.equal(event.defaultPrevented, true);
  assert.equal(view.dialog.open, true);
  assert.equal(view.image.src, 'https://example.com/assets/app-screen.webp');
  assert.equal(view.image.alt, 'Official app preview');
  assert.equal(view.title.textContent, 'Looks Max screenshot');
  assert.equal(view.document.activeElement, view.closeButton);
  assert.equal(view.classes.has('image-preview-open'), true);
});

test('Close cleans up page state and returns focus to the opening link', () => {
  const view = harness();
  view.link.emit('click');
  view.closeButton.emit('click');
  assert.equal(view.dialog.open, false);
  assert.equal(view.classes.has('image-preview-open'), false);
  assert.equal(view.document.activeElement, view.link);
});

test('the native close event uses the same cleanup and does not focus a removed trigger', () => {
  const view = harness();
  view.link.emit('click');
  view.dialog.open = false;
  view.dialog.emit('close');
  assert.equal(view.classes.has('image-preview-open'), false);
  assert.equal(view.document.activeElement, view.link);
  view.link.emit('click');
  view.link.isConnected = false;
  view.dialog.emit('close');
  assert.equal(view.classes.has('image-preview-open'), false);
  assert.equal(view.document.activeElement, view.closeButton);
});

test('modifier keys and non-primary clicks retain native image navigation', () => {
  for (const properties of [{ metaKey: true }, { ctrlKey: true }, { shiftKey: true }, { altKey: true }, { button: 1 }, { button: 2 }]) {
    const view = harness();
    assert.equal(view.link.emit('click', properties).defaultPrevented, false);
    assert.equal(view.dialog.open, false);
    assert.equal(view.image.src, undefined);
    assert.equal(view.classes.has('image-preview-open'), false);
  }
});

test('unsupported or missing dialogs leave screenshot anchors as normal links', () => {
  for (const options of [{ supported: false }, { missingDialog: true }]) {
    const view = harness(options);
    assert.equal(view.link.emit('click').defaultPrevented, false);
    assert.equal(view.dialog.open, false);
    assert.equal(view.image.src, undefined);
  }
});

test('showModal failure preserves the image link and does not lock the page', () => {
  const view = harness({ failOpen: true });
  assert.equal(view.link.emit('click').defaultPrevented, false);
  assert.equal(view.dialog.open, false);
  assert.equal(view.classes.has('image-preview-open'), false);
  assert.equal(view.document.activeElement, null);
});

test('clicks inside the dialog preserve it and only backdrop coordinates dismiss it', () => {
  const view = harness();
  view.link.emit('click');
  view.dialog.emit('click', { target: view.image, clientX: 20, clientY: 20 });
  view.dialog.emit('click', { clientX: 150, clientY: 100 });
  assert.equal(view.dialog.closeCalls, 0);
  assert.equal(view.dialog.open, true);
  view.dialog.emit('click', { clientX: 20, clientY: 100 });
  assert.equal(view.dialog.closeCalls, 1);
  assert.equal(view.dialog.open, false);
  assert.equal(view.document.activeElement, view.link);
});

test('cross-origin image links are never intercepted by the local preview', () => {
  const view = harness({ href: 'https://images.example.org/screen.webp' });
  assert.equal(view.link.emit('click').defaultPrevented, false);
  assert.equal(view.dialog.open, false);
  assert.equal(view.image.src, undefined);
  assert.equal(view.classes.has('image-preview-open'), false);
});

test('missing per-image descriptions use meaningful preview text', () => {
  const view = harness();
  view.link.dataset = {};
  view.link.emit('click');
  assert.equal(view.title.textContent, 'App preview');
  assert.equal(view.image.alt, 'Official app promotional screenshot with sample content');
});
