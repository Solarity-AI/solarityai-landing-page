(function () {
  'use strict';
  if (typeof document === 'undefined' || typeof window === 'undefined') return;

  // Inlined at the end of <body> on the pages that use it (Investors and Platform), so no other page
  // carries it and none waits for a request.
  // Answers on the Investors page can be linked: arriving at #faq-… opens that answer.
  // "Show all answers" opens or closes every answer at once; without JavaScript it stays hidden.
  function initializeAnswers() {
    if (typeof document.querySelectorAll !== 'function' || typeof document.getElementById !== 'function') return;
    function openTarget() {
      let id = '';
      try { id = decodeURIComponent((window.location.hash || '').slice(1)); } catch (error) { return; }
      const target = id ? document.getElementById(id) : null;
      const item = target && typeof target.closest === 'function' ? target.closest('details') : null;
      if (item && !item.open) item.open = true;
    }
    openTarget();
    window.addEventListener('hashchange', openTarget);
    document.querySelectorAll('button[data-answers-toggle]').forEach((button) => {
      const list = document.getElementById(button.getAttribute('aria-controls') || '');
      if (!list) return;
      const items = () => Array.from(list.querySelectorAll('details'));
      const allOpen = () => items().every((item) => item.open);
      function render() {
        button.textContent = allOpen() ? 'Hide all answers' : 'Show all answers';
        button.setAttribute('aria-expanded', String(allOpen()));
      }
      button.addEventListener('click', () => {
        const open = !allOpen();
        items().forEach((item) => { item.open = open; });
        render();
      });
      list.addEventListener('toggle', render, true);
      button.hidden = false;
      render();
    });
  }

  // Sticky section indexes (Platform, Investors) mark the section being read: the one that crosses a
  // reading line a third of the way down the window. Measured at most once per frame while scrolling.
  function initializeSectionIndex() {
    if (typeof document.querySelectorAll !== 'function' || typeof window.requestAnimationFrame !== 'function') return;
    document.querySelectorAll('nav.saas-index').forEach((nav) => {
      const links = Array.from(nav.querySelectorAll('a[href^="#"]'));
      const sections = links.map((link) => document.getElementById(link.getAttribute('href').slice(1))).filter(Boolean);
      if (!sections.length) return;
      let frame = 0;
      function mark() {
        frame = 0;
        const line = (window.innerHeight || 0) / 3;
        const current = sections.filter((section) => {
          const box = section.getBoundingClientRect();
          return box.top <= line && box.bottom > line;
        }).pop();
        links.forEach((link) => {
          if (current && link.getAttribute('href') === '#' + current.id) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
      window.addEventListener('scroll', () => { if (!frame) frame = window.requestAnimationFrame(mark); }, { passive: true });
      // The first measurement waits for a frame: measuring during load would force an extra layout before first paint.
      frame = window.requestAnimationFrame(mark);
    });
  }

  function initialize() {
    initializeAnswers();
    initializeSectionIndex();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
