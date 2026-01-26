// Language Switcher for Solarity AI Website
(function() {
  'use strict';

  // Get current language from localStorage or default to 'en' (ENGLISH)
  let currentLang = localStorage.getItem('solarityai-lang') || 'en';

  // Initialize language on page load
  function initLanguage() {
    setupLanguageSwitcher();
    setLanguage(currentLang);
    updateLanguageSwitcher();
  }

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
      console.log('🔗 Updating URL hash:', currentHash, '→', newHash);
      window.history.replaceState({}, '', newHash);
    }

    // Update meta tags and lang attribute
    updateMetaTags(lang, window.location.pathname);
  }

  // Translate hash/anchor links based on language
  function translateHash(hash, lang) {
    const hashMap = {
      tr: {
        '#about': '#hakkimizda',
        '#partnerships': '#ortakliklar',
        '#projects': '#projeler',
        '#team': '#ekip',
        '#contact': '#iletisim'
      },
      en: {
        '#hakkimizda': '#about',
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

      console.log('🔗 Nav link updated:', link.href);
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

      console.log('📍 Section ID updated:', section.id);
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
      console.error('❌ Translations object not loaded yet!');
      setTimeout(function() { setLanguage(lang); }, 100);
      return;
    }
    
    currentLang = lang;
    localStorage.setItem('solarityai-lang', lang);
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;
    
    // Update URL based on language (EN: /en/, TR: /)
    updateUrlForLanguage(lang);

    // Update navigation anchor links
    updateNavigationLinks(lang);

    console.log('🌐 Setting language to:', lang);
    console.log('📚 Translations available for this language:', !!translationsObj[lang]);
    if (translationsObj[lang]) {
      console.log('📝 Sample translation (navAbout):', translationsObj[lang]['navAbout']);
    }
    
    // Update all elements with data-i18n attribute
    const elements = document.querySelectorAll('[data-i18n]');
    console.log('=== TRANSLATION START ===');
    console.log('Language:', lang);
    console.log('Found', elements.length, 'elements with data-i18n attribute');
    
    // Specifically check footer links
    const footerLinks = document.querySelectorAll('footer [data-i18n]');
    console.log('Footer elements with data-i18n:', footerLinks.length);
    footerLinks.forEach(function(link) {
      console.log('Footer element:', link.tagName, link.getAttribute('data-i18n'), 'current text:', link.textContent);
    });
    
    if (!translationsObj || !translationsObj[lang]) {
      console.error('❌ Cannot translate - translations object or language not available!');
      return;
    }
    
    elements.forEach(element => {
      const key = element.getAttribute('data-i18n');
      if (translationsObj[lang] && translationsObj[lang][key]) {
        const translation = translationsObj[lang][key];
        const tagName = element.tagName;
        
        // Handle different element types
        if (tagName === 'LABEL' && element.querySelector('.required')) {
          // Labels with required span
          const requiredSpan = element.querySelector('.required');
          element.innerHTML = translation.replace('*', '') + ' ' + requiredSpan.outerHTML;
        } else if (tagName === 'INPUT') {
          if (element.type === 'submit' || element.type === 'button') {
            element.value = translation;
          } else if (element.hasAttribute('placeholder')) {
            element.placeholder = translation;
          } else {
            element.value = translation;
          }
        } else if (tagName === 'TEXTAREA') {
          if (element.hasAttribute('placeholder')) {
            element.placeholder = translation;
          } else {
            element.textContent = translation;
          }
        } else if (tagName === 'BUTTON') {
          element.textContent = translation;
        } else if (tagName === 'OPTION') {
          element.textContent = translation;
        } else if (tagName === 'A') {
          // Anchor tags - CRITICAL: Must update textContent and innerText
          const oldText = element.textContent || element.innerText || element.innerHTML;
          // Force update by replacing innerHTML
          element.innerHTML = translation;
          element.textContent = translation;
          element.innerText = translation;
          console.log('🔗 ANCHOR UPDATE:', key, '| Old:', oldText.trim(), '| New:', translation, '| Actual:', element.textContent.trim());
        } else if (tagName === 'LABEL') {
          // Labels without required span
          const requiredSpan = element.querySelector('.required');
          if (requiredSpan) {
            element.innerHTML = translation.replace('*', '').trim() + ' ' + requiredSpan.outerHTML;
          } else {
            element.textContent = translation;
          }
        } else if (tagName === 'P' && (element.classList.contains('ud-team-bio') || (element.parentElement && element.parentElement.classList.contains('ud-project-content')))) {
          // Team bios and project descriptions with HTML
          element.innerHTML = translation;
        } else if (element.classList && (element.classList.contains('project-company') || element.classList.contains('project-name'))) {
          // Project company and name divs
          element.textContent = translation;
        } else {
          // Default: all other elements (H1-H6, SPAN, P, DIV, etc.)
          const oldText = element.textContent || element.innerText;
          element.textContent = translation;
          if (tagName === 'H5' && (key === 'footerQuickLinks' || key.startsWith('footer'))) {
            console.log('📋 H5 UPDATE:', key, '| Old:', oldText.trim(), '| New:', translation, '| Actual:', element.textContent.trim());
          }
        }
      } else {
        console.warn('Translation not found for key:', key, 'in language:', lang);
      }
    });

    // Update all elements with data-i18n-placeholder attribute (for placeholder text)
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
      const key = element.getAttribute('data-i18n-placeholder');
      if (translationsObj[lang] && translationsObj[lang][key]) {
        element.placeholder = translationsObj[lang][key];
        console.log('📝 PLACEHOLDER UPDATE:', key, '| New:', translationsObj[lang][key]);
      }
    });

    // Update all elements with data-i18n-html attribute (for HTML content)
    document.querySelectorAll('[data-i18n-html]').forEach(element => {
      const key = element.getAttribute('data-i18n-html');
      if (translationsObj[lang] && translationsObj[lang][key]) {
        element.innerHTML = translationsObj[lang][key];
      }
    });

    // Update all elements with data-i18n-aria-label attribute (for aria-label)
    document.querySelectorAll('[data-i18n-aria-label]').forEach(element => {
      const key = element.getAttribute('data-i18n-aria-label');
      if (translationsObj[lang] && translationsObj[lang][key]) {
        element.setAttribute('aria-label', translationsObj[lang][key]);
      }
    });

    // Special-case: ensure big support stat number uses the correct localized format
    try {
      const supportNumberKey = 'statsSupportNumber';
      if (translationsObj[lang] && translationsObj[lang][supportNumberKey]) {
        document.querySelectorAll('[data-i18n="' + supportNumberKey + '"]').forEach(function(el) {
          el.textContent = translationsObj[lang][supportNumberKey];
        });
      }
    } catch (e) {
      console.warn('Unable to apply special-case translation for statsSupportNumber', e);
    }

    // Update title - ALWAYS START WITH "Solarity AI"
    const currentPath = window.location.pathname;

    // Determine page type
    const isCareerPage = currentPath.includes('career') || currentPath.includes('kariyer') || currentPath.includes('careers');

    if (isCareerPage) {
      // Kariyer sayfası title'ları
      if (lang === 'tr') {
        document.title = 'Solarity AI - Kariyer';
      } else {
        document.title = 'Solarity AI - Career';
      }
    } else {
      // Ana sayfa title'ları
      if (lang === 'tr') {
        document.title = 'Solarity AI - Ana Sayfa';
      } else {
        document.title = 'Solarity AI - Home';
      }
    }

    // Update hidden form fields
    const contactFormSubject = document.getElementById('contactFormSubject');
    if (contactFormSubject && translationsObj[lang] && translationsObj[lang]['contactFormSubject']) {
      contactFormSubject.value = translationsObj[lang]['contactFormSubject'];
    }

    const careersFormSubject = document.getElementById('careersFormSubject');
    if (careersFormSubject && translationsObj[lang] && translationsObj[lang]['careersFormSubject']) {
      careersFormSubject.value = translationsObj[lang]['careersFormSubject'];
    }

    const careersFormAutoresponse = document.getElementById('careersFormAutoresponse');
    if (careersFormAutoresponse && translationsObj[lang] && translationsObj[lang]['careersFormAutoresponse']) {
      careersFormAutoresponse.value = translationsObj[lang]['careersFormAutoresponse'];
    }
    
    console.log('✅ Translation complete! Updated', elements.length, 'elements');
  }

  // Track if button listener is set up
  let buttonListenerSetup = false;

  // Setup language switcher button event listener
  function setupLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    if (switcher) {
      console.log('🔘 Setting up language switcher button');
      
      // Keep inline onclick as backup, but also add event listeners
      // Don't remove onclick - it works as a fallback
      
      // Only set up listener once to avoid duplicates
      if (!buttonListenerSetup) {
        // Use event delegation on document body for maximum reliability
        // This works even if the button is replaced or recreated
        document.body.addEventListener('click', function languageButtonHandler(e) {
          const target = e.target;
          if (target && (target.id === 'languageSwitcher' || target.closest('#languageSwitcher'))) {
            e.preventDefault();
            e.stopPropagation();
            console.log('🔘 Language button clicked via delegation!');
            toggleLanguage();
            return false;
          }
        }, true); // Use capture phase for better reliability
        
        buttonListenerSetup = true;
        console.log('✅ Language switcher button event delegation attached');
      }
      
      // Also ensure direct listener is attached to the current button
      // Remove any existing listeners by cloning (but keep the element reference)
      const directHandler = function(e) {
        e.preventDefault();
        e.stopPropagation();
        console.log('🔘 Language button clicked via direct listener!');
        toggleLanguage();
        return false;
      };
      
      // Remove old listener if exists and add new one
      switcher.removeEventListener('click', directHandler);
      switcher.addEventListener('click', directHandler);
      
      console.log('✅ Language switcher button direct listener attached');
      return switcher;
    } else {
      console.warn('⚠️ Language switcher button not found! Will retry...');
    }
    return null;
  }

  // Update language switcher button
  function updateLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    if (switcher) {
      // Show flag and language code for the language that will be switched TO
      const nextLang = currentLang === 'tr' ? 'en' : 'tr';
      const langCode = nextLang === 'tr' ? 'TR' : 'EN';
      const flagClass = nextLang === 'tr' ? 'flag-tr' : 'flag-en';
      const flagEl = switcher.querySelector('.language-flag');
      const codeEl = switcher.querySelector('.language-code');

      if (flagEl) {
        flagEl.classList.remove('flag-tr', 'flag-en');
        flagEl.classList.add(flagClass);
      }

      if (codeEl) {
        codeEl.textContent = langCode;
      } else {
        switcher.textContent = langCode;
      }
      switcher.setAttribute('data-lang', currentLang);
      switcher.setAttribute('title', currentLang === 'tr' ? 'İngilizce\'ye Geç' : 'Switch to Turkish');
    }
  }

  // Toggle language
  function toggleLanguage() {
    console.log('🔄 Toggling language from', currentLang);
    const newLang = currentLang === 'tr' ? 'en' : 'tr';
    console.log('🔄 Switching to', newLang);
    setLanguage(newLang);
    updateLanguageSwitcher();
    console.log('✅ Language toggled successfully');
  }

  // Expose toggle function globally IMMEDIATELY so inline onclick handlers work
  window.toggleLanguage = toggleLanguage;

  // Initialize on DOM ready
  function initialize() {
    console.log('=== LANGUAGE SYSTEM INITIALIZING ===');
    console.log('Current language:', currentLang);
    console.log('Translations object exists:', typeof translations !== 'undefined');
    
    // Wait for translations to be loaded (check both window.translations and translations)
    const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
    if (!translationsObj) {
      console.log('⏳ Waiting for translations to load...');
      setTimeout(initialize, 50);
      return;
    }
    
    console.log('✅ Translations loaded! Available languages:', Object.keys(translationsObj));
    console.log('✅ Turkish translations available:', !!translationsObj['tr']);
    console.log('✅ Sample Turkish navAbout:', translationsObj['tr'] ? translationsObj['tr']['navAbout'] : 'NOT FOUND');
    
    // Small delay to ensure all elements are rendered
    setTimeout(function() {
      console.log('=== RUNNING INITIAL TRANSLATION ===');
      console.log('Language:', currentLang);
      // Try to setup button multiple times to ensure it works
      setupLanguageSwitcher();
      setTimeout(setupLanguageSwitcher, 200);
      setTimeout(setupLanguageSwitcher, 500);
      initLanguage();
    }, 100);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize);
  } else {
    initialize();
  }
  
  // Also run on window load as backup
  window.addEventListener('load', function() {
    setTimeout(function() {
      const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
      if (translationsObj) {
        console.log('=== WINDOW LOAD - RUNNING TRANSLATION ===');
        // Re-setup button in case it wasn't ready before
        setupLanguageSwitcher();
        setLanguage(currentLang);
        updateLanguageSwitcher();
      } else {
        console.error('❌ Translations still not loaded on window load!');
      }
    }, 500);
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
        console.log('🔘 Language button detected in DOM, setting up...');
        setupLanguageSwitcher();
      }
      
      const translationsObj = window.translations || (typeof translations !== 'undefined' ? translations : null);
      if (shouldRetranslate && translationsObj) {
        setTimeout(function() {
          console.log('🔄 Retranslating due to DOM changes');
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
      console.log('=== FINAL TRANSLATION CHECK AFTER ANIMATIONS ===');
      setLanguage(currentLang);
    } else {
      console.error('❌ Translations not available for final check!');
    }
  }, 2000);

  // Expose other functions globally (toggleLanguage already exposed above)
  window.setLanguage = setLanguage;
  window.getCurrentLanguage = () => currentLang;

})();
