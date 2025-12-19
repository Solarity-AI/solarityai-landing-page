// Language Switcher for Solarity AI Website
(function() {
  'use strict';

  // Get current language from localStorage or default to 'en'
  let currentLang = localStorage.getItem('solarityai-lang') || 'en';

  // Initialize language on page load
  function initLanguage() {
    setLanguage(currentLang);
    updateLanguageSwitcher();
  }

  // Set language and update all translatable elements
  function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('solarityai-lang', lang);
    
    // Update HTML lang attribute
    document.documentElement.lang = lang;
    
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const key = element.getAttribute('data-i18n');
      if (translations[lang] && translations[lang][key]) {
        // Skip if it's a label with required span - handle separately
        if (element.tagName === 'LABEL' && element.querySelector('.required')) {
          const requiredSpan = element.querySelector('.required');
          const requiredText = requiredSpan.textContent;
          element.innerHTML = translations[lang][key].replace('*', '') + ' ' + requiredSpan.outerHTML;
        } else if (element.tagName === 'INPUT' && (element.type === 'text' || element.type === 'email' || element.type === 'tel' || element.type === 'url')) {
          // Only update placeholder if it's a placeholder attribute
          if (element.hasAttribute('placeholder')) {
            element.placeholder = translations[lang][key];
          } else {
            element.value = translations[lang][key];
          }
        } else if (element.tagName === 'TEXTAREA') {
          if (element.hasAttribute('placeholder')) {
            element.placeholder = translations[lang][key];
          } else {
            element.textContent = translations[lang][key];
          }
        } else if (element.tagName === 'P' && (element.classList.contains('ud-team-bio') || (element.parentElement && element.parentElement.classList.contains('ud-project-content')))) {
          // Handle team bios and project descriptions which may contain HTML
          element.innerHTML = translations[lang][key];
        } else if (element.classList && (element.classList.contains('project-company') || element.classList.contains('project-name'))) {
          // Handle project company and name divs
          element.textContent = translations[lang][key];
        } else if (element.tagName === 'INPUT' && element.type === 'submit' || 
                   element.tagName === 'BUTTON') {
          element.textContent = translations[lang][key];
        } else if (element.tagName === 'OPTION') {
          element.textContent = translations[lang][key];
        } else if (element.tagName === 'LABEL') {
          // Handle labels - preserve required span if exists
          const requiredSpan = element.querySelector('.required');
          if (requiredSpan) {
            const requiredText = requiredSpan.textContent;
            element.innerHTML = translations[lang][key].replace('*', '').trim() + ' ' + requiredSpan.outerHTML;
          } else {
            element.textContent = translations[lang][key];
          }
        } else {
          element.textContent = translations[lang][key];
        }
      }
    });

    // Update all elements with data-i18n-html attribute (for HTML content)
    document.querySelectorAll('[data-i18n-html]').forEach(element => {
      const key = element.getAttribute('data-i18n-html');
      if (translations[lang] && translations[lang][key]) {
        element.innerHTML = translations[lang][key];
      }
    });

    // Update title and meta tags
    if (lang === 'tr') {
      document.title = 'Solarity AI - AI-Odaklı Yazılım Şirketi | Kurumsal Çözümler';
    } else {
      document.title = 'Solarity AI - AI-Native Software Company | Enterprise Solutions';
    }
  }

  // Update language switcher button
  function updateLanguageSwitcher() {
    const switcher = document.getElementById('languageSwitcher');
    if (switcher) {
      switcher.textContent = currentLang === 'en' ? 'TR' : 'EN';
      switcher.setAttribute('data-lang', currentLang);
      switcher.setAttribute('title', currentLang === 'en' ? 'Switch to Turkish' : 'Türkçe\'ye Geç');
    }
  }

  // Toggle language
  function toggleLanguage() {
    const newLang = currentLang === 'en' ? 'tr' : 'en';
    setLanguage(newLang);
    updateLanguageSwitcher();
  }

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLanguage);
  } else {
    initLanguage();
  }

  // Expose toggle function globally
  window.toggleLanguage = toggleLanguage;
  window.setLanguage = setLanguage;
  window.getCurrentLanguage = () => currentLang;

})();

