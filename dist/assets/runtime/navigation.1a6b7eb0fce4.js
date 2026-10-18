(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  if (toggle && nav) {
    document.documentElement.classList.add('nav-enhanced');
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
})();
