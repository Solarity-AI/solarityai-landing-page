// Language Switcher for Solarity AI Website
(function() {
  'use strict';
  var noop = function() {};
  var log = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { log.apply(console, arguments); } : noop;
  var warn = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { warn.apply(console, arguments); } : noop;
  var err = (typeof window !== 'undefined' && window.DEBUG_LANG) ? function() { err.apply(console, arguments); } : noop;

  // Get current language from localStorage or default to 'en' (ENGLISH)
  let currentLang = localStorage.getItem('solarityai-lang') || 'en';

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
        '#about': '#services',
        '#hakkimizda': '#services',
        '#partnerships': '#ortakliklar',
        '#products': '#urunler',
        '#urunler': '#urunler',
        '#projects': '#projeler',
        '#team': '#ekip',
        '#contact': '#iletisim'
      },
      en: {
        '#services': '#services',
        '#about': '#services',
        '#hakkimizda': '#services',
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


    // Also update section IDs (only if on same page)
    updateSectionIds(lang);
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
    var parent = iframe.parentNode;
    var newIframe = document.createElement('iframe');
    newIframe.id = 'contactMapEmbed';
    newIframe.title = iframe.title || 'Solarity AI - Dallas Office';
    newIframe.setAttribute('data-src-tr', srcTr || '');
    newIframe.setAttribute('data-src-en', srcEn || '');
    newIframe.className = iframe.className || 'w-full h-full min-h-[260px] md:min-h-[320px]';
    newIframe.style.border = '0';
    newIframe.setAttribute('allowfullscreen', '');
    newIframe.setAttribute('referrerpolicy', iframe.getAttribute('referrerpolicy') || 'no-referrer-when-downgrade');
    parent.replaceChild(newIframe, iframe);
    var sep = url.indexOf('?') >= 0 ? '&' : '?';
    newIframe.src = url + sep + '_=' + Date.now();
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

  // TR ve EN birebir aynı kart/fotoğraf boyutu – CSS’te #team/#ekip ortak; inline stil kaldırıldı
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

  // Initialize language on page load (tek sefer çalışsın – long task azaltma)
  var _languageInitialized = false;
  function initLanguage() {
    if (_languageInitialized) return;
    _languageInitialized = true;
    setupLanguageSwitcher();
    setLanguage(currentLang);
    updateLanguageSwitcher();
  }

  // Set language and update all translatable elements
  function setLanguage(lang) {
    const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
    if (!translationsObj) {
      err('❌ Translations object not loaded yet!');
      setTimeout(function() { setLanguage(lang); }, 100);
      return;
    }
    // Dil degisince sayfa ayni yerde kalsin: scroll (mutlak + oran) ve hash kaydet
    // Tıklamadan önce (mousedown/touchstart) kaydedilen pozisyon varsa onu kullan – focus scroll’u bozmasın
    var prior = window._langScrollBeforeSwitch;
    var savedScrollY, savedScrollRatio;
    if (prior && typeof prior.y === 'number') {
      savedScrollY = prior.y;
      savedScrollRatio = prior.ratio;
      window._langScrollBeforeSwitch = null;
    } else {
      savedScrollY = window.scrollY !== undefined ? window.scrollY : (window.pageYOffset || document.documentElement.scrollTop || 0);
      var doc = document.documentElement;
      var maxScroll = Math.max(0, (doc.scrollHeight - (window.innerHeight || doc.clientHeight)));
      savedScrollRatio = maxScroll > 0 ? savedScrollY / maxScroll : 0;
    }
    if (savedScrollRatio > 1) savedScrollRatio = 1;
    if (savedScrollRatio < 0) savedScrollRatio = 0;
    var hadHash = window.location.hash || "";
    if (hadHash) {
      try { window.history.replaceState(null, "", window.location.pathname + window.location.search); } catch (e) {}
    }
    document.documentElement.style.scrollBehavior = 'auto';
    // Scroll bar'ı korumak için body'yi kilitlemiyoruz - sadece scroll'u kaydedip restore ediyoruz
    // position: fixed KULLANMIYORUZ çünkü scroll bar'ı kaybettirir

    function unlockScrollAndRestore() {
      // Hiçbir şey yapmıyoruz - body zaten kilitli değil, sadece scroll restore edilecek
      requestAnimationFrame(function() {
        var d = document.documentElement;
        var max = Math.max(0, d.scrollHeight - (window.innerHeight || d.clientHeight));
        var targetY = savedScrollRatio * max;
        if (targetY > max) targetY = max;
        window.scrollTo(0, targetY);
      });
    }

    // Bolum id'lerini guncelle (hash yok artik, scroll tetiklenmez)
    updateSectionIds(lang);
    // Güvenlik: çeviri hiç yüklenmezse 3 saniye sonra yine de body'yi göster
    if (window._langLoadingFallback) clearTimeout(window._langLoadingFallback);
    function restoreScroll() {
      requestAnimationFrame(function() {
        var d = document.documentElement;
        var max = Math.max(0, d.scrollHeight - (window.innerHeight || d.clientHeight));
        var targetY = savedScrollRatio * max;
        if (targetY > max) targetY = max;
        window.scrollTo(0, targetY);
      });
    }
    // Scroll pin loop devre dışı - scroll takılmasını önler
    var scrollPinEnd = 0;
    function restoreScrollAbsolute() {
      window.scrollTo(0, savedScrollY);
    }
    window._langLoadingFallback = setTimeout(function() {
      document.documentElement.classList.remove('lang-loading');
      if (typeof unlockScrollAndRestore === 'function') unlockScrollAndRestore();
      else restoreScroll();
    }, 3000);
    
    currentLang = lang;
    localStorage.setItem('solarityai-lang', lang);
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Body sınıfı – TR/EN stilleri için (id’den bağımsız)
    document.body.classList.remove('lang-tr', 'lang-en');
    document.body.classList.add(lang === 'tr' ? 'lang-tr' : 'lang-en');
    
    // Hash guncellemesi finishI18n'de yapilacak (scroll restore'dan sonra)

    setTimeout(function() {
      updateNavigationLinks(lang);
      updateMapEmbedLang(lang);
      fixTeamPhotoSize(lang);
      if (lang === 'tr') setTimeout(function() { fixTeamPhotoSize('tr'); }, 80);
      updateTeamMemberNames(lang);
    }, 0);

    setTimeout(function doHeavyI18n() {
    log('🌐 Setting language to:', lang);
    if (!translationsObj || !translationsObj[lang]) {
      err('❌ Cannot translate - translations object or language not available!');
      return;
    }
    // Uzun ana iş parçacığı görevini kır: querySelectorAll ayrı tick'te
    var elements = document.querySelectorAll('[data-i18n]');
    log('Found', elements.length, 'elements with data-i18n attribute');
    if (!elements.length) {
      setTimeout(doRestI18n, 0);
      return;
    }

    var applyOne = function(element) {
      var key = element.getAttribute('data-i18n');
      if (translationsObj[lang] && translationsObj[lang][key]) {
        var translation = translationsObj[lang][key];
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
          element.innerHTML = translation;
          element.textContent = translation;
          element.innerText = translation;
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
      } else {
        warn('Translation not found for key:', key, 'in language:', lang);
      }
    };

    var idx = 0;
    var CHUNK = 1;
    function runChunk() {
      var end = Math.min(idx + CHUNK, elements.length);
      for (; idx < end; idx++) applyOne(elements[idx]);
      if (idx < elements.length) {
        if (typeof requestAnimationFrame !== 'undefined') requestAnimationFrame(runChunk);
        else setTimeout(runChunk, 0);
      } else {
        doRestI18n();
      }
    }
    // Uzun görevleri kır: runChunk'ı bir sonraki tick'te başlat
    setTimeout(runChunk, 0);

    function doRestI18n() {
      var placeholders = document.querySelectorAll('[data-i18n-placeholder]');
      var chunkSize = 4;
      var pHIdx = 0;
      function runPlaceholderChunk() {
        var end = Math.min(pHIdx + chunkSize, placeholders.length);
        for (; pHIdx < end; pHIdx++) {
          var el = placeholders[pHIdx];
          var k = el.getAttribute('data-i18n-placeholder');
          if (translationsObj[lang] && translationsObj[lang][k]) el.placeholder = translationsObj[lang][k];
        }
        if (pHIdx < placeholders.length) {
          setTimeout(runPlaceholderChunk, 0);
        } else {
          setTimeout(step2, 0);
        }
      }
      runPlaceholderChunk();
    }
    function step2() {
      var htmlEls = document.querySelectorAll('[data-i18n-html]');
      var chunkSize = 4;
      var idx = 0;
      function runChunk() {
        var end = Math.min(idx + chunkSize, htmlEls.length);
        for (; idx < end; idx++) {
          var el = htmlEls[idx];
          var k = el.getAttribute('data-i18n-html');
          if (translationsObj[lang] && translationsObj[lang][k]) el.innerHTML = translationsObj[lang][k];
        }
        if (idx < htmlEls.length) setTimeout(runChunk, 0);
        else setTimeout(step3, 0);
      }
      runChunk();
    }
    function step3() {
      var ariaEls = document.querySelectorAll('[data-i18n-aria-label]');
      var chunkSize = 4;
      var idx = 0;
      function runChunk() {
        var end = Math.min(idx + chunkSize, ariaEls.length);
        for (; idx < end; idx++) {
          var el = ariaEls[idx];
          var k = el.getAttribute('data-i18n-aria-label');
          if (translationsObj[lang] && translationsObj[lang][k]) el.setAttribute('aria-label', translationsObj[lang][k]);
        }
        if (idx < ariaEls.length) setTimeout(runChunk, 0);
        else setTimeout(step4, 0);
      }
      runChunk();
    }
    function step4() {
      var titleEls = document.querySelectorAll('[data-i18n-title]');
      var chunkSize = 4;
      var idx = 0;
      function runChunk() {
        var end = Math.min(idx + chunkSize, titleEls.length);
        for (; idx < end; idx++) {
          var el = titleEls[idx];
          var k = el.getAttribute('data-i18n-title');
          if (translationsObj[lang] && translationsObj[lang][k]) el.setAttribute('title', translationsObj[lang][k]);
        }
        if (idx < titleEls.length) setTimeout(runChunk, 0);
        else setTimeout(step5, 0);
      }
      runChunk();
    }
    function step5() {
      try {
        var sk = 'statsSupportNumber';
        if (translationsObj[lang] && translationsObj[lang][sk]) {
          document.querySelectorAll('[data-i18n="' + sk + '"]').forEach(function(el) { el.textContent = translationsObj[lang][sk]; });
        }
      } catch (e) {}
      var path = window.location.pathname;
      var isCareer = path.indexOf("career") !== -1 || path.indexOf("kariyer") !== -1 || path.indexOf("careers") !== -1;
      var titleText = isCareer
        ? (lang === "tr" ? "Solarity AI - Kariyer" : "Solarity AI - Career")
        : (lang === "tr" ? "Solarity AI - Ana Sayfa" : "Solarity AI - Home");
      document.title = titleText;
      var cfs = document.getElementById("contactFormSubject");
      if (cfs && translationsObj[lang] && translationsObj[lang]["contactFormSubject"]) cfs.value = translationsObj[lang]["contactFormSubject"];
      var cfsub = document.getElementById("careersFormSubject");
      if (cfsub && translationsObj[lang] && translationsObj[lang]["careersFormSubject"]) cfsub.value = translationsObj[lang]["careersFormSubject"];
      var cfar = document.getElementById("careersFormAutoresponse");
      if (cfar && translationsObj[lang] && translationsObj[lang]["careersFormAutoresponse"]) cfar.value = translationsObj[lang]["careersFormAutoresponse"];
      setTimeout(function finishI18n() {
        scrollPinEnd = 0;
        if (window._langLoadingFallback) { clearTimeout(window._langLoadingFallback); window._langLoadingFallback = null; }
        document.documentElement.classList.remove("lang-loading");
        log("Translation complete! Updated", elements.length, "elements");
        updateMetaTags(lang, window.location.pathname);
        updateMapEmbedLang(lang);
        if (typeof unlockScrollAndRestore === "function") {
          // Zorunlu reflow’u azalt: layout okuyan unlockScrollAndRestore/restoreScroll’u bir sonraki frame’e ertele
          var doUnlock = function() {
            unlockScrollAndRestore();
            if (typeof restoreScroll === "function") restoreScroll();
          };
          if (typeof requestAnimationFrame !== "undefined") requestAnimationFrame(doUnlock);
          else setTimeout(doUnlock, 0);
          setTimeout(function() { if (typeof restoreScroll === "function") restoreScroll(); }, 50);
          // Scroll lock devre dışı - scroll takılmasını önler
          if (hadHash) {
            var newHash = translateHash(hadHash, lang);
            if (newHash) {
              setTimeout(function() {
                try { window.history.replaceState(null, "", newHash); } catch (e) {}
                if (typeof restoreScroll === "function") restoreScroll();
              }, 100);
            }
          }
        } else if (hadHash) {
          var newHash = translateHash(hadHash, lang);
          if (newHash) try { window.history.replaceState(null, "", newHash); } catch (e) {}
        }
      }, 0);
    }
    }, 0);
  }

  // Track if button listener is set up
  let buttonListenerSetup = false;

  // Setup language switcher button event listener
  function setupLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    if (switcher) {
      log('🔘 Setting up language switcher button');
      
      // Keep inline onclick as backup, but also add event listeners
      // Don't remove onclick - it works as a fallback
      
      // Only set up listener once to avoid duplicates
      if (!buttonListenerSetup) {
        // mousedown/touchstart: tıklamadan önce scroll pozisyonunu kaydet – focus scroll’u bozmasın
        function saveScrollBeforeSwitch(e) {
          const target = e.target;
          if (target && (target.id === 'languageSwitcher' || target.closest('#languageSwitcher') || target.id === 'languageSwitcherMobile' || target.closest('#languageSwitcherMobile'))) {
            var y = window.scrollY !== undefined ? window.scrollY : (window.pageYOffset || document.documentElement.scrollTop || 0);
            var doc = document.documentElement;
            var maxScroll = Math.max(0, (doc.scrollHeight - (window.innerHeight || doc.clientHeight)));
            var ratio = maxScroll > 0 ? y / maxScroll : 0;
            if (ratio > 1) ratio = 1;
            if (ratio < 0) ratio = 0;
            window._langScrollBeforeSwitch = { y: y, ratio: ratio };
          }
        }
        document.body.addEventListener('mousedown', saveScrollBeforeSwitch, true);
        document.body.addEventListener('touchstart', saveScrollBeforeSwitch, true);

        // Use event delegation on document body for maximum reliability
        document.body.addEventListener('click', function languageButtonHandler(e) {
          const target = e.target;
          if (target && (target.id === 'languageSwitcher' || target.closest('#languageSwitcher') || target.id === 'languageSwitcherMobile' || target.closest('#languageSwitcherMobile'))) {
            e.preventDefault();
            e.stopPropagation();
            if (target.blur) target.blur();
            if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
            log('🔘 Language button clicked via delegation! (desktop or mobile)');
            toggleLanguage();
            return false;
          }
        }, true); // Use capture phase for better reliability

        buttonListenerSetup = true;
        log('✅ Language switcher button event delegation attached');
      }
      // Direct listener’ları ayrı tick’te ekle (uzun görev kırma)
      function attachDirectListeners() {
        var directHandler = function(e) {
          e.preventDefault();
          e.stopPropagation();
          if (e.target && e.target.blur) e.target.blur();
          if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
          log('🔘 Language button clicked via direct listener!');
          toggleLanguage();
          return false;
        };
        switcher.removeEventListener('click', directHandler);
        switcher.addEventListener('click', directHandler);
        var mobileSwitcher = document.getElementById('languageSwitcherMobile');
        if (mobileSwitcher) {
          try { mobileSwitcher.removeEventListener('click', directHandler); } catch (e) {}
          mobileSwitcher.addEventListener('click', directHandler);
          log('✅ Language switcher mobile direct listener attached');
        }
        log('✅ Language switcher button direct listener attached');
      }
      if (typeof requestAnimationFrame !== 'undefined') requestAnimationFrame(attachDirectListeners);
      else setTimeout(attachDirectListeners, 0);
      return switcher;
    } else {
      warn('⚠️ Language switcher button not found! Will retry...');
    }
    return null;
  }

  // Update language switcher button
  
  // SVG sadece Windows; macOS, Linux, iOS, Android vb. için emoji kullan
  if (typeof window.USE_SVG_FLAGS === 'undefined') {
    const isWindows = /Win/.test(navigator.userAgent || navigator.platform || '');
    window.USE_SVG_FLAGS = isWindows;
  }
  const useEmojiFlags = !window.USE_SVG_FLAGS;
  
  function updateLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    const switcherMobile = document.getElementById('languageSwitcherMobile');

    // Compute the target language (the one the button should switch TO)
    const targetLang = currentLang === 'tr' ? 'en' : 'tr';
    // Buton mevcut dili gösterir (geçilecek dili değil)
    const langCodeForButton = currentLang === 'tr' ? 'TR' : 'EN';
    const flagEmojiForButton = currentLang === 'tr' ? '🇹🇷' : '🇺🇸';
    const flagSvgForButton = currentLang === 'tr' ? 'assets/images/flags/flag-tr.svg?v=2' : 'assets/images/flags/flag-us.svg?v=2';

    if (switcher) {
      const flagEl = document.getElementById('flagIcon');
      const codeEl = document.getElementById('currentLang');

      if (flagEl) {
        if (useEmojiFlags) {
          // Emoji (iOS, macOS, Android) – kutuyla orantılı 44x32
          if (flagEl.tagName === 'IMG') {
            const newSpan = document.createElement('span');
            newSpan.id = 'flagIcon';
            newSpan.textContent = flagEmojiForButton;
            newSpan.style.display = 'inline-flex';
            newSpan.style.alignItems = 'center';
            newSpan.style.justifyContent = 'center';
            newSpan.style.width = '56px';
            newSpan.style.height = '40px';
            newSpan.style.fontSize = '2.25rem';
            newSpan.style.lineHeight = '1';
            flagEl.parentNode.replaceChild(newSpan, flagEl);
            log('✅ Desktop flag converted to emoji:', flagEmojiForButton);
          } else {
            flagEl.textContent = flagEmojiForButton;
            flagEl.style.display = 'inline-flex';
            flagEl.style.alignItems = 'center';
            flagEl.style.justifyContent = 'center';
            flagEl.style.width = '56px';
            flagEl.style.height = '40px';
            flagEl.style.fontSize = '2.25rem';
            flagEl.style.lineHeight = '1';
            log('✅ Desktop flag emoji:', flagEmojiForButton);
          }
        } else {
          // Windows: SVG fallback
          if (flagEl.tagName === 'IMG') {
            flagEl.src = flagSvgForButton;
            flagEl.alt = currentLang.toUpperCase();
            log('✅ Desktop flag SVG (Windows):', flagSvgForButton);
          } else {
            // SPAN ise IMG'ye çevir
            const newImg = document.createElement('img');
            newImg.id = 'flagIcon';
            newImg.src = flagSvgForButton;
            newImg.alt = currentLang.toUpperCase();
            newImg.width = 56;
            newImg.height = 40;
            newImg.style.objectFit = 'cover';
            newImg.style.borderRadius = '5px';
            newImg.style.boxShadow = '0 1px 3px rgba(0,0,0,0.2)';
            flagEl.parentNode.replaceChild(newImg, flagEl);
            log('✅ Desktop flag converted to SVG:', flagSvgForButton);
          }
        }
      } else {
        warn('⚠️ flagIcon element not found (desktop)');
      }

      if (codeEl) codeEl.textContent = langCodeForButton;
      // keep data attribute with current language for other logic, but expose target too
      switcher.setAttribute('data-lang-current', currentLang);
      switcher.setAttribute('data-lang-target', targetLang);
    }

    if (switcherMobile) {
      const flagElMobile = document.getElementById('flagIconMobile');
      const codeElMobile = document.getElementById('currentLangMobile');

      if (flagElMobile) {
        if (useEmojiFlags) {
          // Emoji (iOS, macOS, Android) – kutuyla orantılı 48x34
          if (flagElMobile.tagName === 'IMG') {
            const newSpan = document.createElement('span');
            newSpan.id = 'flagIconMobile';
            newSpan.textContent = flagEmojiForButton;
            newSpan.style.display = 'inline-flex';
            newSpan.style.alignItems = 'center';
            newSpan.style.justifyContent = 'center';
            newSpan.style.width = '60px';
            newSpan.style.height = '44px';
            newSpan.style.fontSize = '2.5rem';
            newSpan.style.lineHeight = '1';
            flagElMobile.parentNode.replaceChild(newSpan, flagElMobile);
            log('✅ Mobile flag converted to emoji:', flagEmojiForButton);
          } else {
            flagElMobile.textContent = flagEmojiForButton;
            flagElMobile.style.display = 'inline-flex';
            flagElMobile.style.alignItems = 'center';
            flagElMobile.style.justifyContent = 'center';
            flagElMobile.style.width = '60px';
            flagElMobile.style.height = '44px';
            flagElMobile.style.fontSize = '2.5rem';
            flagElMobile.style.lineHeight = '1';
            log('✅ Mobile flag emoji:', flagEmojiForButton);
          }
        } else {
          // Windows: SVG fallback
          if (flagElMobile.tagName === 'IMG') {
            flagElMobile.src = flagSvgForButton;
            flagElMobile.alt = currentLang.toUpperCase();
            log('✅ Mobile flag SVG (Windows):', flagSvgForButton);
          } else {
            // SPAN ise IMG'ye çevir
            const newImg = document.createElement('img');
            newImg.id = 'flagIconMobile';
            newImg.src = flagSvgForButton;
            newImg.alt = currentLang.toUpperCase();
            newImg.width = 60;
            newImg.height = 44;
            newImg.style.objectFit = 'cover';
            newImg.style.borderRadius = '4px';
            newImg.style.boxShadow = '0 1px 2px rgba(0,0,0,0.2)';
            flagElMobile.parentNode.replaceChild(newImg, flagElMobile);
            log('✅ Mobile flag converted to SVG:', flagSvgForButton);
          }
        }
      }

      if (codeElMobile) codeElMobile.textContent = langCodeForButton;
      switcherMobile.setAttribute('data-lang-current', currentLang);
      switcherMobile.setAttribute('data-lang-target', targetLang);
    }
  }

  // Toggle language
  function toggleLanguage() {
    log('🔄 Toggling language from', currentLang);
    const newLang = currentLang === 'tr' ? 'en' : 'tr';
    log('🔄 Switching to', newLang);
    setLanguage(newLang);
    updateMapEmbedLang(newLang);
    updateLanguageSwitcher();
    log('✅ Language toggled successfully');
  }

  // Expose toggle function globally IMMEDIATELY so inline onclick handlers work
  window.toggleLanguage = toggleLanguage;
  window.invokeToggleLanguage = function() {
    if (typeof window.toggleLanguage === 'function') return window.toggleLanguage();
  };

  // Initialize on DOM ready – iki tick’e bölünür: TBT / uzun ana iş parçacığı görevinden kaçın
  function initialize() {
    log('=== LANGUAGE SYSTEM INITIALIZING ===');
    log('Current language:', currentLang);
    log('Translations object exists:', typeof translations !== 'undefined');
    
    const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
    if (!translationsObj) {
      log('⏳ Waiting for translations to load...');
      setTimeout(initialize, 50);
      return;
    }
    
    log('✅ Translations loaded! Available languages:', Object.keys(translationsObj));
    log('✅ Turkish translations available:', !!translationsObj['tr']);
    log('✅ Sample Turkish navAbout:', translationsObj['tr'] ? translationsObj['tr']['navAbout'] : 'NOT FOUND');
    
    // 1. tick: sadece buton dinleyicisi (setupLanguageSwitcher + attachDirectListeners ertelenir)
    setupLanguageSwitcher();
    // 2.–3. tick: setLanguage + updateLanguageSwitcher (initLanguage bir frame sonra, uzun görevi böler)
    function runInitLanguage() {
      log('=== RUNNING INITIAL TRANSLATION ===');
      log('Language:', currentLang);
      initLanguage();
    }
    if (typeof requestAnimationFrame !== 'undefined') {
      requestAnimationFrame(function() { requestAnimationFrame(runInitLanguage); });
    } else {
      setTimeout(runInitLanguage, 0);
    }
  }

  function runInitialize() {
    if (typeof requestIdleCallback !== 'undefined') {
      requestIdleCallback(initialize, { timeout: 500 });
    } else {
      setTimeout(initialize, 150);
    }
  }
  // Script yüklendiğinde hemen yield: uzun görev ilk tick’te bitmesin
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      setTimeout(runInitialize, 0);
    });
  } else {
    setTimeout(runInitialize, 0);
  }

  window.addEventListener('load', function() {
    if (_languageInitialized) return;
    if (typeof requestIdleCallback !== 'undefined') {
      requestIdleCallback(function() {
        const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
        if (translationsObj) initLanguage();
        else err('❌ Translations still not loaded on window load!');
      }, { timeout: 700 });
    } else {
      setTimeout(function() {
        const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
        if (translationsObj) initLanguage();
      }, 500);
    }
  });
  
  // Watch for dynamically added elements (like footer with animations)
  if (typeof MutationObserver !== 'undefined') {
    const observer = new MutationObserver(function(mutations) {
      let shouldRetranslate = false;
      let buttonAdded = false;
      
      mutations.forEach(function(mutation) {
        if (mutation.addedNodes.length > 0) {
          mutation.addedNodes.forEach(function(node) {
            if (node.nodeType === 1) {
              // Check if language button was added
              if (node.id === 'languageSwitcher' || node.querySelector && node.querySelector('#languageSwitcher')) {
                buttonAdded = true;
              }
              // Check if translatable elements were added
              if (node.hasAttribute('data-i18n') || (node.querySelector && node.querySelector('[data-i18n]'))) {
                shouldRetranslate = true;
              }
            }
          });
        }
      });
      
      // If button was added, set it up
      if (buttonAdded) {
        log('🔘 Language button detected in DOM, setting up...');
        setupLanguageSwitcher();
      }
      
      const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
      if (shouldRetranslate && translationsObj) {
        setTimeout(function() {
          log('🔄 Retranslating due to DOM changes');
          setLanguage(currentLang);
        }, 100);
      }
    });
    
    // Start observing after a delay
    setTimeout(function() {
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });
    }, 1000);
  }
  
  // Force retranslation after animations (WOW.js typically finishes around 1-2 seconds)
  setTimeout(function() {
    const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
    if (translationsObj) {
      log('=== FINAL TRANSLATION CHECK AFTER ANIMATIONS ===');
      setLanguage(currentLang);
    } else {
      err('❌ Translations not available for final check!');
    }
  }, 2000);

  // Expose other functions globally (toggleLanguage already exposed above)
  window.setLanguage = setLanguage;
  window.getCurrentLanguage = () => currentLang;

})();
