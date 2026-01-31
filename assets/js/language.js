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
        '#projeler': '#projects',
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

  // Initialize language on page load
  function initLanguage() {
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
    // Güvenlik: çeviri hiç yüklenmezse 3 saniye sonra yine de body'yi göster
    if (window._langLoadingFallback) clearTimeout(window._langLoadingFallback);
    window._langLoadingFallback = setTimeout(function() {
      document.documentElement.classList.remove('lang-loading');
    }, 3000);
    
    currentLang = lang;
    localStorage.setItem('solarityai-lang', lang);
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Body sınıfı – TR/EN stilleri için (id’den bağımsız)
    document.body.classList.remove('lang-tr', 'lang-en');
    document.body.classList.add(lang === 'tr' ? 'lang-tr' : 'lang-en');
    
    // Update URL based on language (EN: /en/, TR: /)
    updateUrlForLanguage(lang);

    setTimeout(function() {
      updateNavigationLinks(lang);
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
        if (window._langLoadingFallback) { clearTimeout(window._langLoadingFallback); window._langLoadingFallback = null; }
        document.documentElement.classList.remove("lang-loading");
        log("Translation complete! Updated", elements.length, "elements");
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
        // Use event delegation on document body for maximum reliability
        // This works even if the button is replaced or recreated
        document.body.addEventListener('click', function languageButtonHandler(e) {
          const target = e.target;
          if (target && (target.id === 'languageSwitcher' || target.closest('#languageSwitcher') || target.id === 'languageSwitcherMobile' || target.closest('#languageSwitcherMobile'))) {
            e.preventDefault();
            e.stopPropagation();
            log('🔘 Language button clicked via delegation! (desktop or mobile)');
            toggleLanguage();
            return false;
          }
        }, true); // Use capture phase for better reliability
        
        buttonListenerSetup = true;
        log('✅ Language switcher button event delegation attached');
      }
      
      // Also ensure direct listener is attached to the current button
      // Remove any existing listeners by cloning (but keep the element reference)
      const directHandler = function(e) {
        e.preventDefault();
        e.stopPropagation();
        log('🔘 Language button clicked via direct listener!');
        toggleLanguage();
        return false;
      };
      
      // Remove old listener if exists and add new one
      switcher.removeEventListener('click', directHandler);
      switcher.addEventListener('click', directHandler);
      
      // Also attach direct listener to mobile switcher if present
      const mobileSwitcher = document.getElementById('languageSwitcherMobile');
      if (mobileSwitcher) {
        try {
          mobileSwitcher.removeEventListener('click', directHandler);
        } catch (e) {}
        mobileSwitcher.addEventListener('click', directHandler);
        log('✅ Language switcher mobile direct listener attached');
      }

      log('✅ Language switcher button direct listener attached');
      return switcher;
    } else {
      warn('⚠️ Language switcher button not found! Will retry...');
    }
    return null;
  }

  // Update language switcher button
  function updateLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    const switcherMobile = document.getElementById('languageSwitcherMobile');

    // Compute the target language (the one the button should switch TO)
    const targetLang = currentLang === 'tr' ? 'en' : 'tr';
    const langCodeForButton = targetLang === 'tr' ? 'TR' : 'EN';
    const flagSrcForButton = targetLang === 'tr' ? 'assets/images/flags/flag-tr.svg?v=1' : 'assets/images/flags/flag-us.svg?v=1';

    if (switcher) {
      const flagEl = document.getElementById('flagIcon');
      const codeEl = document.getElementById('currentLang');

      if (flagEl && flagEl.tagName === 'IMG') {
        // show the flag of the language we will switch TO
        flagEl.src = flagSrcForButton;
        flagEl.alt = targetLang === 'tr' ? 'Türkçe' : 'English';
        flagEl.title = targetLang === 'tr' ? 'Türkçe' : 'English';
        log('✅ Language.js set desktop <img> src to (target):', flagSrcForButton);
      } else if (flagEl) {
        // fallback if not an img element
        flagEl.style.background = targetLang === 'tr' ? '#E30A17' : 'linear-gradient(to bottom, #012169 0%, #012169 33%, white 33%, white 67%, #C8102E 67%, #C8102E 100%)';
        warn('⚠️ flagIcon is not an <img>, applied background fallback for target flag');
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

      if (flagElMobile && flagElMobile.tagName === 'IMG') {
        flagElMobile.src = flagSrcForButton;
        flagElMobile.alt = targetLang === 'tr' ? 'Türkçe' : 'English';
        flagElMobile.title = targetLang === 'tr' ? 'Türkçe' : 'English';
        log('✅ Language.js set mobile <img> src to (target):', flagSrcForButton);
      } else if (flagElMobile) {
        flagElMobile.style.background = targetLang === 'tr' ? '#E30A17' : 'linear-gradient(to bottom, #012169 0%, #012169 33%, white 33%, white 67%, #C8102E 67%, #C8102E 100%)';
        warn('⚠️ flagIconMobile is not an <img>, applied background fallback for target flag');
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
    updateLanguageSwitcher();
    log('✅ Language toggled successfully');
  }

  // Expose toggle function globally IMMEDIATELY so inline onclick handlers work
  window.toggleLanguage = toggleLanguage;
  window.invokeToggleLanguage = function() {
    if (typeof window.toggleLanguage === 'function') return window.toggleLanguage();
  };

  // Initialize on DOM ready
  function initialize() {
    log('=== LANGUAGE SYSTEM INITIALIZING ===');
    log('Current language:', currentLang);
    log('Translations object exists:', typeof translations !== 'undefined');
    
    // Wait for translations to be loaded (check both window.translations and translations)
    const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
    if (!translationsObj) {
      log('⏳ Waiting for translations to load...');
      setTimeout(initialize, 50);
      return;
    }
    
    log('✅ Translations loaded! Available languages:', Object.keys(translationsObj));
    log('✅ Turkish translations available:', !!translationsObj['tr']);
    log('✅ Sample Turkish navAbout:', translationsObj['tr'] ? translationsObj['tr']['navAbout'] : 'NOT FOUND');
    
    setTimeout(function() {
      log('=== RUNNING INITIAL TRANSLATION ===');
      log('Language:', currentLang);
      setupLanguageSwitcher();
      initLanguage();
    }, 0);
  }

  function runInitialize() {
    if (typeof requestIdleCallback !== 'undefined') {
      requestIdleCallback(initialize, { timeout: 500 });
    } else {
      setTimeout(initialize, 150);
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runInitialize);
  } else {
    runInitialize();
  }

  window.addEventListener('load', function() {
    if (typeof requestIdleCallback !== 'undefined') {
      requestIdleCallback(function() {
        const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
        if (translationsObj) {
          log('=== WINDOW LOAD - RUNNING TRANSLATION ===');
          setupLanguageSwitcher();
          setLanguage(currentLang);
          updateLanguageSwitcher();
        } else {
          err('❌ Translations still not loaded on window load!');
        }
      }, { timeout: 700 });
    } else {
      setTimeout(function() {
        const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
        if (translationsObj) {
          setupLanguageSwitcher();
          setLanguage(currentLang);
          updateLanguageSwitcher();
        }
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
