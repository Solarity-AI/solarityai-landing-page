'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, 'scripts/copy.js'), 'utf8');

// A source-level harness: buttons, status regions, a clipboard, and timers.
function harness({ clipboard = 'resolves', addresses = ['ata.turhan@solarityai.com'] } = {}) {
  const timers = [];
  const statuses = {};
  const writes = [];
  const buttons = addresses.map((address, index) => {
    const listeners = {};
    const statusId = 'status-' + index;
    statuses[statusId] = { textContent: '' };
    return {
      hidden: true,
      textContent: 'Copy address',
      getAttribute(name) {
        const value = typeof address === 'string' ? { text: address } : address;
        return { 'data-copy': value.text, 'data-copy-status': statusId, 'data-copy-name': value.name ?? null }[name] ?? null;
      },
      addEventListener(type, listener) { listeners[type] = listener; },
      click() { return listeners.click(); },
    };
  });
  const document = {
    querySelectorAll(selector) { return selector === 'button[data-copy]' ? buttons : []; },
    getElementById(id) { return statuses[id] || null; },
  };
  let navigator = {};
  if (clipboard !== 'missing') {
    navigator = {
      clipboard: {
        writeText(text) {
          writes.push(text);
          return clipboard === 'resolves' ? Promise.resolve() : Promise.reject(new Error('Denied'));
        },
      },
    };
  }
  const context = {
    document, navigator,
    setTimeout(callback) { timers.push(callback); return timers.length; },
    clearTimeout() {},
  };
  vm.runInNewContext(source, context, { filename: 'scripts/copy.js' });
  return { buttons, statuses, writes, timers };
}

const settle = () => new Promise((resolve) => setImmediate(resolve));

test('buttons stay hidden when the clipboard is unavailable', () => {
  const view = harness({ clipboard: 'missing' });
  assert.equal(view.buttons[0].hidden, true);
});

test('available clipboard reveals the button and copies its exact address', async () => {
  const view = harness();
  assert.equal(view.buttons[0].hidden, false);
  view.buttons[0].click();
  await settle();
  assert.deepEqual(view.writes, ['ata.turhan@solarityai.com']);
  assert.equal(view.buttons[0].textContent, 'Copied');
  assert.equal(view.statuses['status-0'].textContent, 'ata.turhan@solarityai.com copied to your clipboard.');
});

test('confirmation clears and the label returns after a pause', async () => {
  const view = harness();
  view.buttons[0].click();
  await settle();
  view.timers.at(-1)();
  assert.equal(view.buttons[0].textContent, 'Copy address');
  assert.equal(view.statuses['status-0'].textContent, '');
});

test('a refused clipboard reports it honestly and never claims success', async () => {
  const view = harness({ clipboard: 'rejects' });
  view.buttons[0].click();
  await settle();
  assert.equal(view.buttons[0].textContent, 'Copy address');
  assert.match(view.statuses['status-0'].textContent, /not available/);
  assert.doesNotMatch(view.statuses['status-0'].textContent, /copied/);
});

test('each button copies its own address into its own status', async () => {
  const view = harness({ addresses: ['ata.turhan@solarityai.com', 'careers@solarityai.com'] });
  view.buttons[1].click();
  await settle();
  assert.deepEqual(view.writes, ['careers@solarityai.com']);
  assert.equal(view.statuses['status-0'].textContent, '');
  assert.match(view.statuses['status-1'].textContent, /^careers@solarityai\.com copied/);
});

test('a named button announces its name instead of reading a long passage aloud', async () => {
  const passage = 'Solarity AI LLC, based in Irving, Texas, builds apps. '.repeat(4);
  const view = harness({ clipboard: 'resolves', addresses: [{ text: passage, name: 'The short description' }] });
  view.buttons[0].click();
  await settle();
  assert.equal(view.writes[0], passage);
  assert.equal(view.statuses['status-0'].textContent, 'The short description copied to your clipboard.');
});

test('a named button that cannot copy asks for the text, not an address', async () => {
  const view = harness({ clipboard: 'rejects', addresses: [{ text: 'Long text', name: 'The one-line description' }] });
  view.buttons[0].click();
  await settle();
  assert.equal(view.statuses['status-0'].textContent, 'Copying is not available here. Select the text to copy it.');
});
