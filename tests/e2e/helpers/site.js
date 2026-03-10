const PAGE_PATHS = ['/', '/careers.html', '/blog.html', '/privacy.html', '/terms.html', '/legal.html']

const BREAKPOINTS = [
  { name: 'mobile-375', width: 375, height: 812 },
  { name: 'tablet-768', width: 768, height: 1024 },
  { name: 'desktop-1024', width: 1024, height: 768 },
  { name: 'desktop-1440', width: 1440, height: 900 },
]

function slugForPath(route) {
  if (route === '/') {
    return 'index'
  }

  return route
    .replace(/^\//, '')
    .replace(/\.html$/, '')
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}

function isMobileProject(testInfo) {
  return testInfo.project.name.includes('mobile')
}

function isChromiumDesktop(testInfo) {
  return testInfo.project.name === 'chromium-desktop'
}

async function installTurnstileMock(page, token = 'pw-turnstile-token') {
  await page.addInitScript((mockToken) => {
    let widgetCount = 0

    window.__turnstileRenders = []
    window.turnstile = {
      render(container, options = {}) {
        widgetCount += 1
        const widgetId = `pw-turnstile-${widgetCount}`

        if (container) {
          container.setAttribute('data-turnstile-rendered', 'true')
          if (options.sitekey) {
            container.setAttribute('data-turnstile-sitekey', options.sitekey)
          }
        }

        window.__turnstileRenders.push({
          widgetId,
          sitekey: options.sitekey || null,
        })

        if (typeof options.callback === 'function') {
          Promise.resolve().then(() => options.callback(mockToken))
        }

        return widgetId
      },
      reset() {
        return undefined
      },
    }
  }, token)
}

async function clickVisibleLanguageToggle(page) {
  await page.evaluate(() => {
    const buttons = Array.from(
      document.querySelectorAll('#languageSwitcher, #languageSwitcherMobile')
    )
    const visibleButton = buttons.find((button) => {
      const style = window.getComputedStyle(button)
      return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0'
    })

    visibleButton?.click()
  })
}

async function readDataLayerEvents(page) {
  return page.evaluate(() => {
    return (window.dataLayer || [])
      .filter((entry) => Array.isArray(entry))
      .map((entry) => ({
        command: entry[0],
        name: entry[1],
        params: entry[2] || null,
      }))
  })
}

module.exports = {
  BREAKPOINTS,
  PAGE_PATHS,
  clickVisibleLanguageToggle,
  installTurnstileMock,
  isChromiumDesktop,
  isMobileProject,
  readDataLayerEvents,
  slugForPath,
}
