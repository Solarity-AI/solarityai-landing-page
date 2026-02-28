/* Solarity AI — main.js
   Navbar, scroll animations, hash scroller, i18n init */

const ASSET_VERSION = '20260207'

/* ============================================================
   1. Safari detection
   ============================================================ */
if (/^((?!chrome|android).)*safari/i.test(navigator.userAgent)) {
  document.documentElement.classList.add('is-safari')
}

/* ============================================================
   2. i18n init (translations.js must be loaded before this)
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
  applyTranslations()
  updateLangToggles()

  // Language toggle buttons
  document.querySelectorAll('.js-lang-toggle').forEach(btn => {
    btn.addEventListener('click', toggleLanguage)
  })

  /* ============================================================
     3. Navbar scroll style
     ============================================================ */
  const header = document.querySelector('.site-header')
  const onScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled')
    } else {
      header.classList.remove('scrolled')
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll() // init

  /* ============================================================
     4. Active nav section (IntersectionObserver)
     ============================================================ */
  const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a[data-section]')
  const sections = document.querySelectorAll('section[id]')

  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id
          navLinks.forEach(link => {
            const linkSection = link.getAttribute('href').replace('/#', '').replace('#', '')
            link.classList.toggle('active', linkSection === id)
          })
        }
      })
    },
    { rootMargin: '-50% 0px -50% 0px' }
  )

  sections.forEach(s => sectionObserver.observe(s))

  /* ============================================================
     5. Mobile menu
     ============================================================ */
  const mobileMenu = document.getElementById('mobile-menu')
  const hamburger = document.getElementById('nav-hamburger')
  const menuIconOpen = document.getElementById('menu-icon-open')
  const menuIconClose = document.getElementById('menu-icon-close')

  function openMobileMenu() {
    mobileMenu.classList.add('open')
    hamburger.setAttribute('aria-expanded', 'true')
    document.body.style.overflow = 'hidden'
    menuIconOpen.style.display = 'none'
    menuIconClose.style.display = 'block'
    // Stagger animation
    mobileMenu.querySelectorAll('a').forEach((link, i) => {
      link.style.transitionDelay = `${0.1 + i * 0.06}s`
    })
  }

  function closeMobileMenu() {
    mobileMenu.classList.remove('open')
    hamburger.setAttribute('aria-expanded', 'false')
    document.body.style.overflow = ''
    menuIconOpen.style.display = 'block'
    menuIconClose.style.display = 'none'
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.style.transitionDelay = '0s'
    })
  }

  hamburger.addEventListener('click', () => {
    if (mobileMenu.classList.contains('open')) {
      closeMobileMenu()
    } else {
      openMobileMenu()
    }
  })

  // Close on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMobileMenu)
  })

  // Close on resize
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) closeMobileMenu()
  })

  /* ============================================================
     6. Hash scroller — smooth scroll to section on page load
     ============================================================ */
  const hash = window.location.hash
  if (hash) {
    const target = document.querySelector(hash)
    if (target) {
      setTimeout(() => {
        const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--navbar-h') || '72')
        const top = target.getBoundingClientRect().top + window.scrollY - offset
        window.scrollTo({ top, behavior: 'smooth' })
      }, 100)
    }
  }

  // Smooth scroll for internal anchor links
  document.querySelectorAll('a[href^="#"], a[href^="/#"]').forEach(link => {
    link.addEventListener('click', e => {
      const href = link.getAttribute('href')
      const hash = href.startsWith('/') ? href.slice(1) : href
      if (!hash) return
      const target = document.querySelector(hash)
      if (target) {
        e.preventDefault()
        const navH = header ? header.offsetHeight : 72
        const top = target.getBoundingClientRect().top + window.scrollY - navH
        window.scrollTo({ top, behavior: 'smooth' })
        // Update URL without jump
        history.pushState(null, '', hash)
      }
    })
  })

  /* ============================================================
     7. Scroll-triggered fade-in-up animations (IntersectionObserver)
     ============================================================ */
  const animObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          animObserver.unobserve(entry.target)
        }
      })
    },
    { rootMargin: '-80px 0px -80px 0px' }
  )

  document.querySelectorAll('.fade-in-up').forEach(el => animObserver.observe(el))
})
