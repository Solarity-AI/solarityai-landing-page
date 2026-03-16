// Language Switcher for Solarity AI Website
(function() {
  'use strict';
  var noop = function() {};
  var log = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { console.log.apply(console, arguments); } : noop;
  var warn = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { console.warn.apply(console, arguments); } : noop;
  var err = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { console.error.apply(console, arguments); } : noop;

  function getStoredLanguage() {
    try {
      return localStorage.getItem('solarityai-lang') || 'en';
    } catch (e) {
      return 'en';
    }
  }

  function setStoredLanguage(lang) {
    try {
      localStorage.setItem('solarityai-lang', lang);
    } catch (e) {}
  }

  // Get current language from localStorage or default to 'en' (ENGLISH)
  let currentLang = getStoredLanguage();

  // Yenilemede dil yanıp sönmesini önle: script yüklenir yüklenmez lang ve body sınıfını uygula
  try {
    document.documentElement.lang = currentLang;
    if (document.body) {
      document.body.classList.remove('lang-tr', 'lang-en');
      document.body.classList.add(currentLang === 'tr' ? 'lang-tr' : 'lang-en');
    }
  } catch (e) {}

  // NOTE: initLanguage is defined later once. (Removed duplicate here)

  // Update URL based on language - BASIT ÇÖZÜM (SUNUCU OLMADAN)
  function updateUrlForLanguage(lang) {
    const currentHash = window.location.hash;

    // Don't update URL during initial page load
    if (!window.solarityUrlInitialized) {
      window.solarityUrlInitialized = true;
      return;
    }

    // Translate hash anchors
    let newHash = currentHash;
    if (currentHash) {
      newHash = translateHash(currentHash, lang);
    }

    // Ana sayfa için sadece hash'i güncelle
    if (newHash !== currentHash && newHash) {
      log('🔗 Updating URL hash:', currentHash, '→', newHash);
      window.history.replaceState({}, '', newHash);
    }

    // Update meta tags and lang attribute
    updateMetaTags(lang, window.location.pathname);
  }

  // Translate hash/anchor links based on language
  function translateHash(hash, lang) {
    const hashMap = {
      tr: {
        '#services': '#services',
        '#about': '#hakkimizda',
        '#hakkimizda': '#hakkimizda',
        '#partnerships': '#ortakliklar',
        '#products': '#urunler',
        '#urunler': '#urunler',
        '#projects': '#projeler',
        '#team': '#ekip',
        '#contact': '#iletisim'
      },
      en: {
        '#services': '#services',
        '#about': '#about',
        '#hakkimizda': '#about',
        '#hizmetler': '#services',
        '#ortakliklar': '#partnerships',
        '#products': '#products',
        '#urunler': '#products',
        '#projects': '#projects',
        '#ekip': '#team',
        '#iletisim': '#contact'
      }
    };

    return hashMap[lang][hash] || hash;
  }

  // Update all navigation links (navbar, footer) based on language
  function updateNavigationLinks(lang) {
    const navLinks = document.querySelectorAll('.nav-link[data-href-tr][data-href-en]');
    navLinks.forEach(link => {
      const hrefTr = link.getAttribute('data-href-tr');
      const hrefEn = link.getAttribute('data-href-en');

      if (lang === 'tr') {
        link.href = hrefTr;
      } else if (lang === 'en') {
        link.href = hrefEn;
      }

      log('🔗 Nav link updated:', link.href);
    });
  }

  // Update section IDs based on language
  function updateSectionIds(lang) {
    const sections = document.querySelectorAll('section[data-section-tr][data-section-en]');
    sections.forEach(section => {
      const idTr = section.getAttribute('data-section-tr');
      const idEn = section.getAttribute('data-section-en');

      if (lang === 'tr') {
        section.id = idTr;
      } else if (lang === 'en') {
        section.id = idEn;
      }

      log('📍 Section ID updated:', section.id);
    });
  }

  // Google Maps embed: diline göre TR veya EN harita (lazy-load sonrası veya dil değişince replace)
  function updateMapEmbedLang(lang) {
    var iframe = document.getElementById('contactMapEmbed');
    if (!iframe) return;
    var srcTr = iframe.getAttribute('data-src-tr');
    var srcEn = iframe.getAttribute('data-src-en');
    var url = (lang === 'tr' ? srcTr : srcEn) || srcEn;
    if (!url) return;
    var currentSrc = iframe.getAttribute('src') || '';
    if (iframe.getAttribute('data-lang-current') === lang || currentSrc.indexOf(url) !== -1) {
      iframe.setAttribute('data-lang-current', lang);
      return;
    }
    var sep = url.indexOf('?') >= 0 ? '&' : '?';
    iframe.setAttribute('data-lang-current', lang);
    iframe.src = url + sep + '_=' + Date.now();
    log('🗺️ Map embed set to', lang === 'tr' ? 'Turkish' : 'English');
  }

  // Ekip üyesi isimleri: EN'de Türkçe karakter yok, TR'de orijinal
  function updateTeamMemberNames(lang) {
    document.querySelectorAll('.team-member-name[data-name-en][data-name-tr]').forEach(function (el) {
      var en = el.getAttribute('data-name-en');
      var tr = el.getAttribute('data-name-tr');
      el.textContent = lang === 'en' ? (en || el.textContent) : (tr || el.textContent);
    });
    document.querySelectorAll('img[data-alt-en][data-alt-tr]').forEach(function (img) {
      var en = img.getAttribute('data-alt-en');
      var tr = img.getAttribute('data-alt-tr');
      img.alt = lang === 'en' ? (en || img.alt) : (tr || img.alt);
    });
  }

  // TR ve EN birebir aynı kart/fotoğraf boyutu – CSS'te #team/#ekip ortak; inline stil kaldırıldı
  function fixTeamPhotoSize(lang) {
    var teamSection = document.querySelector('section[data-section-tr="ekip"]');
    if (!teamSection) return;
    var cards = teamSection.querySelectorAll('.ud-single-team.team-card');
    var wrappers = teamSection.querySelectorAll('.ud-team-image-wrapper');
    cards.forEach(function (card) {
      card.style.minWidth = '';
      card.style.width = '';
      card.style.maxWidth = '';
    });
    wrappers.forEach(function (el) {
      el.style.minHeight = '';
      el.style.height = '';
      el.style.maxHeight = '';
      el.style.flexShrink = '';
      el.style.flex = '';
      el.style.width = '';
    });
    teamSection.querySelectorAll('.ud-team-image-wrapper .ud-team-image, .ud-team-image-wrapper img').forEach(function (el) {
      el.style.width = '';
      el.style.height = '';
      el.style.minHeight = '';
      el.style.objectFit = '';
    });
  }

  // Update meta tags based on language
  function updateMetaTags(lang, path) {
    const baseUrl = 'https://solarityai.com';
    const fullUrl = baseUrl + path;

    // Update canonical
    const canonical = document.querySelector('link[rel="canonical"]');
    if (canonical) {
      canonical.href = fullUrl;
    }

    // Update og:url
    const ogUrl = document.querySelector('meta[property="og:url"]');
    if (ogUrl) {
      ogUrl.content = fullUrl;
    }

    // Update twitter:url
    const twitterUrl = document.querySelector('meta[property="twitter:url"]');
    if (twitterUrl) {
      twitterUrl.content = fullUrl;
    }

    // Update html lang
    document.documentElement.lang = lang;
  }

  // Initialize language on page load
  var _languageInitialized = false;
  var _translationBindings = null;
  var _translationBindingsDirty = true;
  var _scheduledLanguageRefresh = null;

  function getTranslationsObject() {
    return window.translations || (typeof translations !== 'undefined' ? translations : null);
  }

  function refreshTranslationBindings() {
    _translationBindings = {
      text: Array.from(document.querySelectorAll('[data-i18n]')),
      placeholder: Array.from(document.querySelectorAll('[data-i18n-placeholder]')),
      html: Array.from(document.querySelectorAll('[data-i18n-html]')),
      ariaLabel: Array.from(document.querySelectorAll('[data-i18n-aria-label]')),
      title: Array.from(document.querySelectorAll('[data-i18n-title]'))
    };
    _translationBindingsDirty = false;
    return _translationBindings;
  }

  function getTranslationBindings() {
    if (!_translationBindings || _translationBindingsDirty) return refreshTranslationBindings();
    return _translationBindings;
  }

  function translateTextElement(element, translation) {
    var tagName = element.tagName;
    if (tagName === 'LABEL' && element.querySelector('.required')) {
      var requiredSpan = element.querySelector('.required');
      element.innerHTML = translation.replace('*', '') + ' ' + requiredSpan.outerHTML;
    } else if (tagName === 'INPUT') {
      if (element.type === 'submit' || element.type === 'button') element.value = translation;
      else if (element.hasAttribute('placeholder')) element.placeholder = translation;
      else element.value = translation;
    } else if (tagName === 'TEXTAREA') {
      if (element.hasAttribute('placeholder')) element.placeholder = translation;
      else element.textContent = translation;
    } else if (tagName === 'BUTTON' || tagName === 'OPTION') {
      element.textContent = translation;
    } else if (tagName === 'A') {
      element.textContent = translation;
    } else if (tagName === 'LABEL') {
      var rs = element.querySelector('.required');
      if (rs) element.innerHTML = translation.replace('*', '').trim() + ' ' + rs.outerHTML;
      else element.textContent = translation;
    } else if (tagName === 'P' && (element.classList.contains('ud-team-bio') || (element.parentElement && element.parentElement.classList.contains('ud-project-content')))) {
      element.innerHTML = translation;
    } else if (element.classList && (element.classList.contains('project-company') || element.classList.contains('project-name'))) {
      element.textContent = translation;
    } else {
      element.textContent = translation;
    }
  }

  function applyTranslations(lang, translationsObj) {
    var locale = translationsObj && translationsObj[lang];
    if (!locale) return;

    var bindings = getTranslationBindings();

    bindings.text.forEach(function(element) {
      var key = element.getAttribute('data-i18n');
      if (key && locale[key]) translateTextElement(element, locale[key]);
    });

    bindings.placeholder.forEach(function(element) {
      var key = element.getAttribute('data-i18n-placeholder');
      if (key && locale[key]) element.placeholder = locale[key];
    });

    bindings.html.forEach(function(element) {
      var key = element.getAttribute('data-i18n-html');
      if (key && locale[key]) element.innerHTML = locale[key];
    });

    bindings.ariaLabel.forEach(function(element) {
      var key = element.getAttribute('data-i18n-aria-label');
      if (key && locale[key]) element.setAttribute('aria-label', locale[key]);
    });

    bindings.title.forEach(function(element) {
      var key = element.getAttribute('data-i18n-title');
      if (key && locale[key]) element.setAttribute('title', locale[key]);
    });
  }

  function applyLanguageMetadata(lang, translationsObj) {
    try {
      var sk = 'statsSupportNumber';
      if (translationsObj[lang] && translationsObj[lang][sk]) {
        document.querySelectorAll('[data-i18n="' + sk + '"]').forEach(function(el) {
          el.textContent = translationsObj[lang][sk];
        });
      }
    } catch (e) {}

    var path = window.location.pathname;
    var isCareer = path.indexOf('career') !== -1 || path.indexOf('kariyer') !== -1 || path.indexOf('careers') !== -1;
    document.title = isCareer
      ? (lang === 'tr' ? 'Solarity AI - Kariyer' : 'Solarity AI - Career')
      : (lang === 'tr' ? 'Solarity AI - Ana Sayfa' : 'Solarity AI - Home');

    var cfs = document.getElementById('contactFormSubject');
    if (cfs && translationsObj[lang] && translationsObj[lang].contactFormSubject) cfs.value = translationsObj[lang].contactFormSubject;
    var cfsub = document.getElementById('careersFormSubject');
    if (cfsub && translationsObj[lang] && translationsObj[lang].careersFormSubject) cfsub.value = translationsObj[lang].careersFormSubject;
    var cfar = document.getElementById('careersFormAutoresponse');
    if (cfar && translationsObj[lang] && translationsObj[lang].careersFormAutoresponse) cfar.value = translationsObj[lang].careersFormAutoresponse;
  }

  function getCurrentScrollY() {
    return window.scrollY !== undefined ? window.scrollY : (window.pageYOffset || document.documentElement.scrollTop || 0);
  }

  function getLanguageScrollProbeY() {
    var header = document.querySelector('header');
    var headerHeight = header ? Math.ceil(header.getBoundingClientRect().height) : 0;
    var probeY = headerHeight + 24;
    return Math.max(0, Math.min(probeY, Math.max(0, (window.innerHeight || document.documentElement.clientHeight) - 1)));
  }

  function getLanguageAnchorSectionMeta(element) {
    if (!element || !element.closest) return null;
    var section = element.closest('section[data-section-tr][data-section-en]');
    if (!section) return null;
    return {
      sectionTr: section.getAttribute('data-section-tr'),
      sectionEn: section.getAttribute('data-section-en')
    };
  }

  function resolveLanguageAnchorSection(anchor) {
    if (!anchor || !anchor.sectionTr || !anchor.sectionEn) return null;
    return document.querySelector(
      'section[data-section-tr="' + anchor.sectionTr + '"][data-section-en="' + anchor.sectionEn + '"]'
    );
  }

  function collectLanguageAnchorNodes(scope, attrName, attrValue, tagName) {
    return Array.from((scope || document).querySelectorAll('[' + attrName + ']')).filter(function(node) {
      return node.getAttribute(attrName) === attrValue && (!tagName || node.tagName === tagName);
    });
  }

  function isIgnoredLanguageAnchorId(id) {
    return !id ||
      id === 'languageSwitcher' ||
      id === 'languageSwitcherMobile' ||
      id === 'mobileMenuBtn' ||
      id === 'cookie-consent-banner';
  }

  function findLanguageAnchorElement(startEl) {
    var node = startEl;
    while (node && node !== document.body) {
      if (node.matches && node.matches('section[data-section-tr][data-section-en]')) return node;
      if (node.hasAttribute) {
        if (node.hasAttribute('data-i18n')) return node;
        if (node.hasAttribute('data-i18n-html')) return node;
        if (node.id && !isIgnoredLanguageAnchorId(node.id)) return node;
      }
      node = node.parentElement;
    }
    return null;
  }

  function describeLanguageScrollAnchor(anchorEl) {
    if (!anchorEl || !anchorEl.getBoundingClientRect) return null;

    var rect = anchorEl.getBoundingClientRect();
    var anchor = {
      top: rect.top
    };
    var sectionMeta = getLanguageAnchorSectionMeta(anchorEl);
    var sectionScope = sectionMeta ? resolveLanguageAnchorSection(sectionMeta) : null;
    if (sectionMeta) {
      anchor.sectionTr = sectionMeta.sectionTr;
      anchor.sectionEn = sectionMeta.sectionEn;
    }

    if (anchorEl.matches && anchorEl.matches('section[data-section-tr][data-section-en]')) {
      anchor.kind = 'section';
      return anchor;
    }

    if (anchorEl.hasAttribute && anchorEl.hasAttribute('data-i18n')) {
      anchor.kind = 'data-i18n';
      anchor.key = anchorEl.getAttribute('data-i18n');
      anchor.tag = anchorEl.tagName;
      anchor.index = Math.max(0, collectLanguageAnchorNodes(sectionScope || document, 'data-i18n', anchor.key, anchor.tag).indexOf(anchorEl));
      return anchor;
    }

    if (anchorEl.hasAttribute && anchorEl.hasAttribute('data-i18n-html')) {
      anchor.kind = 'data-i18n-html';
      anchor.key = anchorEl.getAttribute('data-i18n-html');
      anchor.tag = anchorEl.tagName;
      anchor.index = Math.max(0, collectLanguageAnchorNodes(sectionScope || document, 'data-i18n-html', anchor.key, anchor.tag).indexOf(anchorEl));
      return anchor;
    }

    if (anchorEl.id && !isIgnoredLanguageAnchorId(anchorEl.id)) {
      anchor.kind = 'id';
      anchor.id = anchorEl.id;
      return anchor;
    }

    if (sectionMeta) {
      anchor.kind = 'section';
      return anchor;
    }

    return null;
  }

  function captureLanguageScrollAnchor() {
    var probeY = getLanguageScrollProbeY();
    var probeXs = [0.35, 0.5, 0.65].map(function(ratio) {
      return Math.max(0, Math.min(Math.round(window.innerWidth * ratio), Math.max(0, window.innerWidth - 1)));
    });
    var seen = [];

    for (var i = 0; i < probeXs.length; i += 1) {
      var stack = document.elementsFromPoint ? document.elementsFromPoint(probeXs[i], probeY) : [document.elementFromPoint(probeXs[i], probeY)];
      for (var j = 0; j < stack.length; j += 1) {
        var el = stack[j];
        if (!el || !el.closest || el.closest('header') || el.closest('#cookie-consent-banner')) continue;
        var anchorEl = findLanguageAnchorElement(el);
        if (!anchorEl || seen.indexOf(anchorEl) !== -1) continue;
        seen.push(anchorEl);
        var described = describeLanguageScrollAnchor(anchorEl);
        if (described) return described;
      }
    }

    var probeSection = null;
    Array.from(document.querySelectorAll('section[data-section-tr][data-section-en]')).forEach(function(section) {
      if (section.getBoundingClientRect().top <= probeY + 8) probeSection = section;
    });
    return describeLanguageScrollAnchor(probeSection);
  }

  function resolveLanguageScrollAnchor(anchor) {
    if (!anchor) return null;

    var sectionScope = resolveLanguageAnchorSection(anchor);
    if (anchor.kind === 'section') return sectionScope;

    if (anchor.kind === 'data-i18n') {
      var textNodes = collectLanguageAnchorNodes(sectionScope || document, 'data-i18n', anchor.key, anchor.tag);
      return textNodes[anchor.index] || textNodes[0] || sectionScope;
    }

    if (anchor.kind === 'data-i18n-html') {
      var htmlNodes = collectLanguageAnchorNodes(sectionScope || document, 'data-i18n-html', anchor.key, anchor.tag);
      return htmlNodes[anchor.index] || htmlNodes[0] || sectionScope;
    }

    if (anchor.kind === 'id') {
      return document.getElementById(anchor.id) || sectionScope;
    }

    return sectionScope;
  }

  function buildLanguageScrollState() {
    var y = getCurrentScrollY();
    return {
      y: y,
      hash: window.location.hash || '',
      scrollBehavior: document.documentElement.style.scrollBehavior || '',
      anchor: captureLanguageScrollAnchor()
    };
  }

  function captureLanguageScrollState() {
    var prior = window._langScrollBeforeSwitch;
    if (prior && typeof prior.y === 'number') {
      window._langScrollBeforeSwitch = null;
      return prior;
    }
    return buildLanguageScrollState();
  }

  function restoreLanguageScrollState(state, lang) {
    if (!state) {
      document.documentElement.style.scrollBehavior = '';
      return;
    }

    var translatedHash = state.hash ? translateHash(state.hash, lang) : '';
    var attempts = 0;

    function restore() {
      var doc = document.documentElement;
      var max = Math.max(0, doc.scrollHeight - (window.innerHeight || doc.clientHeight));
      var targetY = Math.max(0, Math.min(state.y, max));
      var anchorEl = resolveLanguageScrollAnchor(state.anchor);

      if (anchorEl && anchorEl.getBoundingClientRect) {
        var anchorTop = getCurrentScrollY() + anchorEl.getBoundingClientRect().top;
        if (!isNaN(anchorTop)) targetY = Math.max(0, Math.min(anchorTop - (state.anchor.top || 0), max));
      }

      if (translatedHash) {
        try { window.history.replaceState(null, '', translatedHash); } catch (e) {}
      }

      window.scrollTo(0, targetY);

      attempts += 1;
      if (attempts < 2) requestAnimationFrame(restore);
      else document.documentElement.style.scrollBehavior = state.scrollBehavior || '';
    }

    requestAnimationFrame(restore);
  }

  function setDocumentLanguageState(lang) {
    document.documentElement.lang = lang;
    if (document.body) {
      document.body.classList.remove('lang-tr', 'lang-en');
      document.body.classList.add(lang === 'tr' ? 'lang-tr' : 'lang-en');
    }
  }

  function initLanguage() {
    if (_languageInitialized) return;

    var translationsObj = getTranslationsObject();
    if (!translationsObj) {
      setTimeout(initLanguage, 50);
      return;
    }

    _languageInitialized = true;
    refreshTranslationBindings();
    setupLanguageSwitcher();

    if (currentLang === 'tr') {
      setLanguage(currentLang, { preserveScroll: false, updateStorage: false });
      return;
    }

    setDocumentLanguageState('en');
    updateSectionIds('en');
    updateNavigationLinks('en');
    applyLanguageMetadata('en', translationsObj);
    updateLanguageSwitcher();
    document.documentElement.classList.remove('lang-loading');
    completeLanguageSwitch();
  }

  // Set language and update all translatable elements
  function setLanguage(lang, options) {
    options = options || {};

    var translationsObj = getTranslationsObject();
    if (!translationsObj) {
      if (!options.retryScheduled) {
        var retryOptions = Object.assign({}, options, { retryScheduled: true });
        setTimeout(function() { setLanguage(lang, retryOptions); }, 50);
      }
      return false;
    }

    if (!translationsObj[lang]) {
      err('❌ Cannot translate - translations object or language not available!');
      completeLanguageSwitch();
      return false;
    }

    var scrollState = options.preserveScroll === false ? null : captureLanguageScrollState();
    if (scrollState && scrollState.hash) {
      try { window.history.replaceState(null, '', window.location.pathname + window.location.search); } catch (e) {}
    }

    document.documentElement.style.scrollBehavior = 'auto';
    currentLang = lang;
    if (options.updateStorage !== false) setStoredLanguage(lang);

    if (lang === 'tr') document.documentElement.classList.add('lang-loading');
    setDocumentLanguageState(lang);
    updateSectionIds(lang);
    updateNavigationLinks(lang);

    if (options.translateContent !== false) applyTranslations(lang, translationsObj);

    applyLanguageMetadata(lang, translationsObj);

    if (options.refreshAuxiliary !== false) {
      updateMapEmbedLang(lang);
      fixTeamPhotoSize(lang);
      updateTeamMemberNames(lang);
    }

    document.documentElement.classList.remove('lang-loading');
    updateMetaTags(lang, window.location.pathname);
    updateLanguageSwitcher();
    completeLanguageSwitch();
    restoreLanguageScrollState(scrollState, lang);

    return true;
  }

  function getLanguageSwitcherLabel(uiLang, targetLang) {
    if (uiLang === 'tr') {
      return targetLang === 'tr' ? 'Dili Turkceye cevir' : 'Dili Ingilizceye cevir';
    }
    return targetLang === 'tr' ? 'Switch language to Turkish' : 'Switch language to English';
  }

  function setLanguageSwitcherBusy(isBusy) {
    document.querySelectorAll('.ud-lang-btn').forEach(function(btn) {
      btn.disabled = !!isBusy;
      btn.setAttribute('aria-disabled', isBusy ? 'true' : 'false');
    });
  }

  function completeLanguageSwitch() {
    window._languageToggleInFlight = false;
    setLanguageSwitcherBusy(false);
  }

  function saveScrollBeforeLanguageSwitch() {
    window._langScrollBeforeSwitch = buildLanguageScrollState();
  }

  function handleLangBtnClick(e) {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }
    var btn = e.currentTarget;
    var lang = btn.getAttribute('data-lang');
    if (!lang || lang === currentLang) return false;
    if (btn.blur) btn.blur();
    if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
    if (window._languageToggleInFlight) return false;
    window._languageToggleInFlight = true;
    setLanguageSwitcherBusy(true);
    setLanguage(lang);
    return false;
  }

  function bindLangBtn(btn) {
    if (!btn || btn.getAttribute('data-lang-bound') === 'true') return;
    btn.addEventListener('pointerdown', saveScrollBeforeLanguageSwitch, { passive: true });
    btn.addEventListener('click', handleLangBtnClick);
    btn.setAttribute('data-lang-bound', 'true');
  }

  // Setup language switcher pill toggle event listeners
  function setupLanguageSwitcher() {
    var buttons = document.querySelectorAll('.ud-lang-btn[data-lang]');
    if (!buttons.length) {
      warn('⚠️ Language switcher buttons not found! Will retry...');
      return null;
    }
    buttons.forEach(bindLangBtn);
    return buttons[0];
  }

  // Update language switcher pill toggle – toggle is-active on correct buttons
  function updateLanguageSwitcher() {
    document.querySelectorAll('.ud-lang-btn[data-lang]').forEach(function(btn) {
      var lang = btn.getAttribute('data-lang');
      if (lang === currentLang) {
        btn.classList.add('is-active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('is-active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
  }

  // Toggle language
  function toggleLanguage() {
    if (window._languageToggleInFlight) {
      log('⏳ Language toggle already in progress');
      return false;
    }
    window._languageToggleInFlight = true;
    setLanguageSwitcherBusy(true);
    log('🔄 Toggling language from', currentLang);
    const newLang = currentLang === 'tr' ? 'en' : 'tr';
    log('🔄 Switching to', newLang);
    setLanguage(newLang);
    log('✅ Language toggled successfully');
    return true;
  }

  // Expose toggle function globally IMMEDIATELY so inline onclick handlers work
  window.toggleLanguage = toggleLanguage;
  window.invokeToggleLanguage = function() {
    if (typeof window.toggleLanguage === 'function') return window.toggleLanguage();
  };

  function scheduleCurrentLanguageRefresh() {
    if (_scheduledLanguageRefresh) return;

    _scheduledLanguageRefresh = setTimeout(function() {
      _scheduledLanguageRefresh = null;
      _translationBindingsDirty = true;
      if (!_languageInitialized || currentLang !== 'tr') return;
      setLanguage(currentLang, {
        preserveScroll: false,
        updateStorage: false,
        refreshAuxiliary: false
      });
    }, 0);
  }

  function initialize() {
    if (_languageInitialized) return;
    initLanguage();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize);
  } else {
    initialize();
  }
  
  if (typeof MutationObserver !== 'undefined') {
    var observer = new MutationObserver(function(mutations) {
      var shouldRefreshBindings = false;
      var buttonAdded = false;

      mutations.forEach(function(mutation) {
        if (!mutation.addedNodes.length) return;
        mutation.addedNodes.forEach(function(node) {
          if (node.nodeType !== 1) return;
          if (node.classList && node.classList.contains('ud-lang-btn') ||
              (node.querySelector && node.querySelector('.ud-lang-btn'))) {
            buttonAdded = true;
          }
          if (node.hasAttribute('data-i18n') ||
              node.hasAttribute('data-i18n-placeholder') ||
              node.hasAttribute('data-i18n-html') ||
              node.hasAttribute('data-i18n-aria-label') ||
              node.hasAttribute('data-i18n-title') ||
              (node.querySelector && node.querySelector('[data-i18n], [data-i18n-placeholder], [data-i18n-html], [data-i18n-aria-label], [data-i18n-title]'))) {
            shouldRefreshBindings = true;
          }
        });
      });

      if (buttonAdded) setupLanguageSwitcher();
      if (shouldRefreshBindings) scheduleCurrentLanguageRefresh();
    });

    if (document.body) {
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    } else {
      document.addEventListener('DOMContentLoaded', function() {
        observer.observe(document.body, {
          childList: true,
          subtree: true
        });
      });
    }
  }
  
  // Expose other functions globally (toggleLanguage already exposed above)
  window.setLanguage = setLanguage;
  window.getCurrentLanguage = () => currentLang;

})();
