'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, 'scripts/gallery.js'), 'utf8');

// A source-level event harness, not a browser or native-dialog rendering test.
function harness({ supported = true, missingDialog = false, failOpen = false, href = '/assets/app-screen.webp', count = 1, nav = false, caption = false, linkCaption } = {}) {
  const classes = new Set();
  const document = {
    activeElement: null,
    body: { classList: { add: (name) => classes.add(name), remove: (name) => classes.delete(name) } },
    getElementById(id) { return nodes[id] || null; },
    querySelectorAll(selector) { return selector === 'a.screenshot-open' ? links : []; },
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
  const link = { ...element(), href, dataset: { imageTitle: 'Looks Max screenshot', imageAlt: 'Official app preview', ...(linkCaption ? { imageCaption: linkCaption } : {}) } };
  const links = [link];
  for (let index = 2; index <= count; index += 1) {
    links.push({ ...element(), href: '/assets/app-screen-' + index + '.webp', dataset: { imageTitle: 'Screen ' + index, imageAlt: 'Preview ' + index } });
  }
  const navigation = { ...element(), hidden: true };
  const previous = element();
  const next = element();
  const counter = element();
  const closeButton = element();
  const image = element();
  const title = element();
  const captionNode = { ...element(), textContent: 'Official App Store imagery with sample content.' };
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
    ...(caption ? { 'image-dialog-caption': captionNode } : {}),
    ...(nav ? { 'image-dialog-nav': navigation, 'image-dialog-prev': previous, 'image-dialog-next': next, 'image-dialog-count': counter } : {}),
  };
  const window = { location: { href: 'https://example.com/apps/looks-max', origin: 'https://example.com' } };
  vm.runInNewContext(source, { document, window, URL }, { filename: 'scripts/gallery.js' });
  return { document, link, links, closeButton, image, title, dialog, classes, navigation, previous, next, counter, captionNode };
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

test('a single screenshot keeps the sequence controls hidden', () => {
  const view = harness({ nav: true });
  view.link.emit('click');
  assert.equal(view.dialog.open, true);
  assert.equal(view.navigation.hidden, true);
});

test('several screenshots can be browsed with previous and next, wrapping at the ends', () => {
  const view = harness({ nav: true, count: 3 });
  view.links[1].emit('click');
  assert.equal(view.navigation.hidden, false);
  assert.equal(view.counter.textContent, '2 of 3');
  assert.equal(view.title.textContent, 'Screen 2');
  view.next.emit('click');
  assert.equal(view.counter.textContent, '3 of 3');
  assert.equal(view.image.src, 'https://example.com/assets/app-screen-3.webp');
  assert.equal(view.image.alt, 'Preview 3');
  view.next.emit('click');
  assert.equal(view.counter.textContent, '1 of 3');
  assert.equal(view.title.textContent, 'Looks Max screenshot');
  view.previous.emit('click');
  assert.equal(view.counter.textContent, '3 of 3');
});

test('arrow keys browse only while the preview is open, and closing returns to the opener', () => {
  const view = harness({ nav: true, count: 2 });
  const closed = view.dialog.emit('keydown', { key: 'ArrowRight' });
  assert.equal(closed.defaultPrevented, false);
  view.link.emit('click');
  const forward = view.dialog.emit('keydown', { key: 'ArrowRight' });
  assert.equal(forward.defaultPrevented, true);
  assert.equal(view.counter.textContent, '2 of 2');
  view.dialog.emit('keydown', { key: 'ArrowLeft' });
  assert.equal(view.counter.textContent, '1 of 2');
  assert.equal(view.dialog.emit('keydown', { key: 'ArrowRight', metaKey: true }).defaultPrevented, false);
  view.closeButton.emit('click');
  assert.equal(view.document.activeElement, view.link);
});

test('markup without sequence controls still previews each screenshot on its own', () => {
  const view = harness({ count: 3 });
  view.links[2].emit('click');
  assert.equal(view.dialog.open, true);
  assert.equal(view.title.textContent, 'Screen 3');
  assert.equal(view.dialog.emit('keydown', { key: 'ArrowRight' }).defaultPrevented, false);
});

test('a link with its own caption shows it; others keep the default caption', () => {
  const sourced = harness({ caption: true, linkCaption: 'From managementmax.solarityai.com, with sample apps and figures.' });
  sourced.link.emit('click');
  assert.equal(sourced.captionNode.textContent, 'From managementmax.solarityai.com, with sample apps and figures.');
  const plain = harness({ caption: true });
  plain.link.emit('click');
  assert.equal(plain.captionNode.textContent, 'Official App Store imagery with sample content.');
});
