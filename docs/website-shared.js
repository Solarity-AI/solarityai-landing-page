// Shared interactions for all website-* pages.
// Depends on website-translations.js (window.WEBSITE_TRANSLATIONS).

// 1. Page-load animations
window.addEventListener('DOMContentLoaded', function() {
  requestAnimationFrame(function() {
    document.body.classList.add('loaded');
  });
});

// 2. Mobile menu toggle
(function() {
  function init() {
    var toggle = document.getElementById('mobileToggle');
    var menu = document.getElementById('mobileMenu');
    if (!toggle || !menu) return;

    function setOpen(open) {
      menu.classList.toggle('is-open', open);
      document.body.classList.toggle('menu-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      menu.setAttribute('aria-hidden', open ? 'false' : 'true');
      toggle.innerHTML = open ? '&times;' : '&#9776;';
    }

    toggle.addEventListener('click', function() {
      setOpen(!menu.classList.contains('is-open'));
    });

    menu.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() { setOpen(false); });
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) setOpen(false);
    });

    window.addEventListener('resize', function() {
      if (window.innerWidth > 900 && menu.classList.contains('is-open')) setOpen(false);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

// 3. Scroll-triggered reveal animations
(function() {
  function showAll() {
    document.querySelectorAll('.reveal').forEach(function(el) { el.classList.add('visible'); });
  }
  function init() {
    if (!('IntersectionObserver' in window)) {
      showAll();
      return;
    }
    // threshold: 0 + rootMargin -80px so any pixel entering viewport triggers reveal
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0, rootMargin: '0px 0px -80px 0px' });
    document.querySelectorAll('.reveal').forEach(function(el) { observer.observe(el); });
    // Safety net: force-show anything still hidden after 3s
    setTimeout(showAll, 3000);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

// 4. Language switcher + i18n
(function() {
  'use strict';

  var translations = window.WEBSITE_TRANSLATIONS || { en: {}, tr: {} };
  var currentLang = 'en';
  try { currentLang = localStorage.getItem('solarityai-lang') || 'en'; } catch (e) {}

  function applyTranslations(lang) {
    var locale = translations[lang];
    if (!locale) return;

    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      var key = el.getAttribute('data-i18n');
      if (key && locale[key]) el.textContent = locale[key];
    });

    document.querySelectorAll('.team-member-name[data-name-en][data-name-tr]').forEach(function(el) {
      el.textContent = lang === 'en' ? el.getAttribute('data-name-en') : el.getAttribute('data-name-tr');
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
      var key = el.getAttribute('data-i18n-placeholder');
      if (key && locale[key]) el.setAttribute('placeholder', locale[key]);
    });

    document.querySelectorAll('img[data-alt-en][data-alt-tr]').forEach(function(img) {
      img.alt = lang === 'en' ? img.getAttribute('data-alt-en') : img.getAttribute('data-alt-tr');
    });

    document.documentElement.lang = lang;
  }

  function updateSwitcherUI() {
    document.querySelectorAll('.ud-lang-btn[data-lang]').forEach(function(btn) {
      if (btn.getAttribute('data-lang') === currentLang) {
        btn.classList.add('is-active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('is-active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
  }

  function setLanguage(lang) {
    currentLang = lang;
    try { localStorage.setItem('solarityai-lang', lang); } catch (e) {}
    applyTranslations(lang);
    updateSwitcherUI();
  }

  function init() {
    document.querySelectorAll('.ud-lang-btn[data-lang]').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var lang = btn.getAttribute('data-lang');
        if (lang && lang !== currentLang) setLanguage(lang);
      });
    });

    if (currentLang === 'tr') applyTranslations('tr');
    updateSwitcherUI();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

// 5. Logo marquee — duplicate for seamless loop (only if marquee exists)
(function() {
  function init() {
    var track = document.getElementById('marquee-track');
    if (!track) return;
    track.innerHTML = track.innerHTML + track.innerHTML;
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

// 6. Star particles (only if canvas exists — typically hero only)
(function() {
  function init() {
    var canvas = document.getElementById('stars-canvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var stars = [];
    var COUNT = 120;

    function resize() {
      canvas.width = canvas.offsetWidth * devicePixelRatio;
      canvas.height = canvas.offsetHeight * devicePixelRatio;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(devicePixelRatio, devicePixelRatio);
      buildStars();
    }

    function buildStars() {
      stars = [];
      var w = canvas.offsetWidth, h = canvas.offsetHeight;
      for (var i = 0; i < COUNT; i++) {
        stars.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 1.2 + 0.3,
          a: Math.random(),
          da: (Math.random() - 0.5) * 0.008,
          dy: Math.random() * 0.15 + 0.02
        });
      }
    }

    function draw() {
      var w = canvas.offsetWidth, h = canvas.offsetHeight;
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        s.a += s.da;
        if (s.a <= 0 || s.a >= 1) s.da *= -1;
        s.y += s.dy;
        if (s.y > h) { s.y = 0; s.x = Math.random() * w; }
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,' + Math.max(0, Math.min(1, s.a)) + ')';
        ctx.fill();
      }
      requestAnimationFrame(draw);
    }

    window.addEventListener('resize', resize);
    resize();
    draw();
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
