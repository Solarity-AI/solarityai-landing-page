(function () {
  'use strict';

  // The 404 page suggests the page a mistyped or outdated address most likely meant.
  // Routes come from the page itself (data-routes), so the suggestion never points at a missing page.
  const ALIASES = { about: '/company/', team: '/company/', jobs: '/careers/', privacy: '/website-data/', cookies: '/website-data/' };

  function normalize(path) {
    let value = String(path || '');
    try { value = decodeURIComponent(value); } catch (error) { /* keep the raw path */ }
    value = value.toLowerCase().replace(/\/index\.html?$/, '/').replace(/\.html?$/, '').replace(/\/{2,}/g, '/');
    return value.replace(/\/+$/, '') || '/';
  }

  function distance(a, b) {
    const row = Array.from({ length: b.length + 1 }, (_, index) => index);
    for (let i = 1; i <= a.length; i += 1) {
      let previous = row[0];
      row[0] = i;
      for (let j = 1; j <= b.length; j += 1) {
        const saved = row[j];
        row[j] = Math.min(row[j] + 1, row[j - 1] + 1, previous + (a[i - 1] === b[j - 1] ? 0 : 1));
        previous = saved;
      }
    }
    return row[b.length];
  }

  const last = (path) => path.split('/').filter(Boolean).pop() || '';
  const letters = (text) => text.replace(/[^a-z0-9]/g, '');

  function suggest(path, routes) {
    const wanted = normalize(path);
    if (wanted === '/') return null;
    const tail = letters(last(wanted));
    const alias = ALIASES[tail];
    if (alias) return routes.find((route) => route[0] === alias) || null;
    let best = null;
    let bestScore = Infinity;
    routes.forEach((route) => {
      const target = normalize(route[0]);
      if (target === '/') return;
      const end = letters(last(target));
      let score = Math.min(distance(wanted, target), tail ? distance(tail, end) : Infinity);
      if (tail.length >= 4 && (end.startsWith(tail) || tail.startsWith(end))) score = Math.min(score, 0.5);
      const limit = Math.max(2, Math.floor(Math.min(tail.length || wanted.length, end.length) / 3));
      if (score <= limit && score < bestScore) {
        best = route;
        bestScore = score;
      }
    });
    return best;
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { normalize, distance, suggest };
  if (typeof document === 'undefined') return;
  const slot = document.querySelector('[data-routes]');
  if (!slot) return;
  let routes = [];
  try { routes = JSON.parse(slot.getAttribute('data-routes') || '[]'); } catch (error) { return; }
  const match = suggest((window.location || {}).pathname, routes);
  if (!match) return;
  const link = document.createElement('a');
  link.href = match[0];
  link.textContent = match[1] + ' ';
  const arrow = document.createElement('span');
  arrow.setAttribute('aria-hidden', 'true');
  arrow.textContent = '→';
  link.appendChild(arrow);
  slot.textContent = 'Closest match: ';
  slot.appendChild(link);
  slot.hidden = false;
})();
