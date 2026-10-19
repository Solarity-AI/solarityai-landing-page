(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  // This script is inlined in <head>. Select the compact mobile layout before
  // any body content can paint, without waiting for a separate script request.
  document.documentElement.classList.add('nav-enhanced');
  // In-page jumps glide once the visitor interacts. Arriving at a #fragment must
  // land there directly: the browser repeats that jump while loading, and an
  // animated repeat can cancel it.
  function enableSmoothScroll() {
    document.documentElement.classList.add('smooth-scroll');
    window.removeEventListener('pointerdown', enableSmoothScroll);
    window.removeEventListener('keydown', enableSmoothScroll);
  }
  window.addEventListener('pointerdown', enableSmoothScroll, { passive: true });
  window.addEventListener('keydown', enableSmoothScroll, { passive: true });

  // Home: the header floats over the sunrise. Decide before paint, and only for a
  // fresh visit at the top; a restored scroll or #fragment starts with the solid bar.
  // Without JavaScript or IntersectionObserver the header simply stays solid.
  const root = document.documentElement;
  const location = window.location || {};
  const onHome = location.pathname === '/' || location.pathname === '/index.html';
  if (onHome && !location.hash && !(window.scrollY > 0)) root.classList.add('header-over-hero');

  function initializeHeroHeader() {
    if (!onHome) return;
    const hero = document.querySelector('.vision-hero');
    if (!hero || typeof window.IntersectionObserver !== 'function') {
      root.classList.remove('header-over-hero');
      return;
    }
    // Solid once the hero has passed under the 88px header.
    const observer = new window.IntersectionObserver((entries) => {
      entries.forEach((entry) => root.classList.toggle('header-over-hero', entry.isIntersecting));
    }, { rootMargin: '-88px 0px 0px 0px' });
    observer.observe(hero);
  }

  function initializeNavigation() {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.getElementById('site-nav');
    if (!toggle || !nav) {
      document.documentElement.classList.remove('nav-enhanced');
      return;
    }
    let open = false;
    let wasMobile = null;
    const isMobile = () => window.getComputedStyle(toggle).display !== 'none';

    function renderMenu() {
      const mobile = isMobile();
      toggle.setAttribute('aria-expanded', String(mobile && open));
      toggle.setAttribute('aria-label', mobile && open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', mobile && open);
      document.body.classList.toggle('nav-open', mobile && open);
      // This is a navigation disclosure, not a modal. Keep the normal Tab order.
      nav.inert = mobile && !open;
      if (mobile && !open) nav.setAttribute('aria-hidden', 'true');
      else nav.removeAttribute('aria-hidden');
    }

    function closeMenu(restoreFocus) {
      const hadFocus = nav.contains(document.activeElement) || document.activeElement === toggle;
      open = false;
      renderMenu();
      if (restoreFocus && hadFocus && isMobile()) toggle.focus();
    }

    toggle.addEventListener('click', () => {
      open = !open;
      renderMenu();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && open && isMobile()) {
        event.preventDefault();
        closeMenu(true);
      }
    });
    document.addEventListener('pointerdown', (event) => {
      if (open && isMobile() && !nav.contains(event.target) && !toggle.contains(event.target)) closeMenu(true);
    });
    document.addEventListener('focusin', (event) => {
      if (open && isMobile() && !nav.contains(event.target) && !toggle.contains(event.target)) closeMenu(false);
    });
    nav.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu(false);
    });
    function syncViewport() {
      const mobile = isMobile();
      if (mobile !== wasMobile) {
        if (mobile && nav.contains(document.activeElement)) toggle.focus();
        open = false;
        wasMobile = mobile;
      }
      renderMenu();
    }
    window.addEventListener('resize', syncViewport, { passive: true });
    syncViewport();
  }

  function initialize() {
    initializeHeroHeader();
    initializeNavigation();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
