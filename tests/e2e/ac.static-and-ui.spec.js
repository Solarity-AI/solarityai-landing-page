const fs = require('node:fs')
const path = require('node:path')
const { test, expect } = require('@playwright/test')

const {
  PAGE_PATHS,
  clickVisibleLanguageToggle,
  isMobileProject,
} = require('./helpers/site')

const DIST_DIR = path.resolve(__dirname, '../../dist')
const HTML_FILES = ['index.html', 'careers.html', 'blog.html', 'privacy.html', 'terms.html', 'legal.html']

test.describe('Acceptance Criteria - static output and UI behaviors', () => {
  for (const route of PAGE_PATHS) {
    test(`AC01 serves ${route}`, async ({ page }) => {
      const response = await page.goto(route)
      expect(response, `Missing response for ${route}`).toBeTruthy()
      expect(response.ok(), `Expected ${route} to load with HTTP 2xx`).toBeTruthy()

      await expect(page.locator('header.site-header')).toBeVisible()
      await expect(page.locator('footer.site-footer')).toBeVisible()
      await expect(page.locator('main')).toBeVisible()
    })
  }

  test('AC12 static HTML does not include Next.js runtime markers', async () => {
    const runtimeMarkers = [
      '__NEXT_DATA__',
      'id="__next"',
      '/_next/',
      'next-route-announcer',
      'react-refresh',
    ]

    for (const fileName of HTML_FILES) {
      const filePath = path.join(DIST_DIR, fileName)
      const html = fs.readFileSync(filePath, 'utf8')

      for (const marker of runtimeMarkers) {
        expect(html.includes(marker), `${fileName} should not include ${marker}`).toBeFalsy()
      }

      expect(html.includes('<script src="/js/main.js"></script>'), `${fileName} should use static JS assets`).toBeTruthy()
    }
  })

  test('AC13/AC14 CSS keeps reduced-motion and Safari override blocks', async () => {
    const cssPath = path.join(DIST_DIR, 'css/style.css')
    const css = fs.readFileSync(cssPath, 'utf8')

    expect(css.includes('@media (prefers-reduced-motion: reduce)'), 'Missing reduced-motion media query').toBeTruthy()
    expect(css.includes('.is-safari .hero-orb'), 'Missing Safari hero-orb override').toBeTruthy()
    expect(css.includes('.is-safari .site-header'), 'Missing Safari header override').toBeTruthy()
  })

  test('AC02 EN/TR toggle works and persists across all 6 pages', async ({ page }) => {
    await page.goto('/')

    await expect(page.locator('html')).toHaveAttribute('lang', 'en')
    await clickVisibleLanguageToggle(page)

    await expect(page.locator('html')).toHaveAttribute('lang', 'tr')
    await expect(page.locator('[data-i18n="navAboutUs"]').first()).toContainText('Hakkımızda')
    await expect.poll(() => page.evaluate(() => localStorage.getItem('solarityai-lang'))).toBe('tr')

    for (const route of PAGE_PATHS) {
      await page.goto(route)
      await expect(page.locator('html')).toHaveAttribute('lang', 'tr')
      await expect(page.locator('[data-i18n="navAboutUs"]').first()).toContainText('Hakkımızda')
    }

    await clickVisibleLanguageToggle(page)
    await expect(page.locator('html')).toHaveAttribute('lang', 'en')
    await expect.poll(() => page.evaluate(() => localStorage.getItem('solarityai-lang'))).toBe('en')
  })

  test('AC03 desktop navbar scroll state and active section tracking work', async ({ page }, testInfo) => {
    test.skip(isMobileProject(testInfo), 'Desktop-only nav state check.')

    await page.goto('/')

    const header = page.locator('.site-header')
    await page.evaluate(() => window.scrollTo(0, 0))
    await expect(header).not.toHaveClass(/scrolled/)

    await page.evaluate(() => window.scrollTo(0, 700))
    await expect(header).toHaveClass(/scrolled/)

    await page.locator('#team').scrollIntoViewIfNeeded()
    await expect(page.locator('.nav-links a[href="#team"]')).toHaveClass(/active/)

    await page.locator('#contact').scrollIntoViewIfNeeded()
    await expect(page.locator('.nav-links a[href="#contact"]')).toHaveClass(/active/)
  })

  test('AC03 mobile menu opens/closes and locks scroll', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 812 })
    await page.goto('/')

    const mobileMenu = page.locator('#mobile-menu')

    await expect(mobileMenu).not.toHaveClass(/open/)
    await page.click('#nav-hamburger')
    await expect(mobileMenu).toHaveClass(/open/)
    await expect.poll(() => page.evaluate(() => getComputedStyle(document.body).overflow)).toBe('hidden')

    await page.locator('#mobile-menu a[href="#team"]').click()
    await expect(mobileMenu).not.toHaveClass(/open/)
    await expect.poll(() => page.evaluate(() => getComputedStyle(document.body).overflow)).toBe('visible')
  })

  test('AC04 scroll-triggered fade-in-up animations become visible per section', async ({ page }) => {
    await page.goto('/')

    const sections = ['services', 'partnerships', 'products', 'projects', 'team', 'contact']

    for (const sectionId of sections) {
      await page.locator(`#${sectionId}`).scrollIntoViewIfNeeded()
      const target = page.locator(`#${sectionId} .fade-in-up`).first()
      await expect(target).toHaveClass(/visible/)
    }
  })

  test('AC05 hero gradient orbs use float keyframe animation', async ({ page }) => {
    await page.goto('/')

    const orbAnimation = await page.evaluate(() => {
      const orb1 = getComputedStyle(document.querySelector('.hero-orb-1'))
      const orb2 = getComputedStyle(document.querySelector('.hero-orb-2'))

      return {
        orb1Name: orb1.animationName,
        orb2Name: orb2.animationName,
        orb1Duration: orb1.animationDuration,
        orb2Duration: orb2.animationDuration,
      }
    })

    expect(orbAnimation.orb1Name).toContain('float')
    expect(orbAnimation.orb2Name).toContain('float')
    expect(orbAnimation.orb1Duration).toBe('20s')
    expect(orbAnimation.orb2Duration).toBe('25s')
  })

  test('AC06 partner logos transition from grayscale to color on hover', async ({ page }, testInfo) => {
    test.skip(isMobileProject(testInfo), 'Hover interaction is desktop-oriented.')

    await page.goto('/')

    const card = page.locator('.partner-card').first()
    const logo = card.locator('.partner-logo').first()

    const beforeFilter = await logo.evaluate((el) => getComputedStyle(el).filter)
    await card.hover()
    await page.waitForTimeout(200)
    const afterFilter = await logo.evaluate((el) => getComputedStyle(el).filter)

    expect(beforeFilter).not.toBe('none')
    expect(afterFilter).not.toBe(beforeFilter)
  })

  test('AC10 Google Maps iframe exists and points to Google Maps embed', async ({ page }) => {
    await page.goto('/')

    const map = page.locator('.contact-map iframe')
    await expect(map).toBeVisible()
    await expect(map).toHaveAttribute('src', /maps\.google\.com\/maps/)
  })

  test('AC13 prefers-reduced-motion disables animations', async ({ page }) => {
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/')

    const reducedMotion = await page.evaluate(() => {
      const orb = getComputedStyle(document.querySelector('.hero-orb-1'))
      const fade = getComputedStyle(document.querySelector('.fade-in-up'))

      return {
        animationDuration: orb.animationDuration,
        fadeOpacity: fade.opacity,
        fadeTransform: fade.transform,
      }
    })

    expect(reducedMotion.animationDuration).toBe('0.01ms')
    expect(reducedMotion.fadeOpacity).toBe('1')
    expect(reducedMotion.fadeTransform).toBe('none')
  })

  test('AC14 Safari-specific overrides are active in WebKit', async ({ page, browserName }) => {
    test.skip(browserName !== 'webkit', 'Safari override is validated in WebKit only.')

    await page.goto('/')

    const safariState = await page.evaluate(() => {
      const root = document.documentElement
      const heroOrb = getComputedStyle(document.querySelector('.hero-orb-1'))
      const header = getComputedStyle(document.querySelector('.site-header'))

      return {
        hasSafariClass: root.classList.contains('is-safari'),
        orbAnimationName: heroOrb.animationName,
        orbFilter: heroOrb.filter,
        headerBackdropFilter: header.backdropFilter,
      }
    })

    expect(safariState.hasSafariClass).toBeTruthy()
    expect(safariState.orbAnimationName).toBe('none')
    expect(safariState.orbFilter.includes('40px')).toBeTruthy()
    expect(['none', ''].includes(safariState.headerBackdropFilter)).toBeTruthy()
  })

  test('AC15 hash navigation scrolls to correct section on load and click', async ({ page }) => {
    await page.goto('/#contact')

    await expect.poll(() => page.evaluate(() => Math.abs(document.querySelector('#contact').getBoundingClientRect().top))).toBeLessThan(180)

    await page.goto('/')
    await page.locator('a.btn-primary[href="#contact"]').click()

    await expect(page).toHaveURL(/#contact$/)
    await expect.poll(() => page.evaluate(() => Math.abs(document.querySelector('#contact').getBoundingClientRect().top))).toBeLessThan(180)
  })
})
