const { test, expect } = require('@playwright/test')

const {
  BREAKPOINTS,
  PAGE_PATHS,
  isChromiumDesktop,
} = require('./helpers/site')

test.describe('Acceptance Criteria - responsiveness', () => {
  test('AC11 all pages are responsive at 375/768/1024/1440', async ({ page }, testInfo) => {
    test.skip(!isChromiumDesktop(testInfo), 'Responsive sweep runs once on Chromium desktop.')

    for (const viewport of BREAKPOINTS) {
      await page.setViewportSize({ width: viewport.width, height: viewport.height })

      for (const route of PAGE_PATHS) {
        await page.goto(route)

        await expect(page.locator('main')).toBeVisible()

        const overflow = await page.evaluate(() => {
          return document.documentElement.scrollWidth - window.innerWidth
        })

        expect(
          overflow,
          `Horizontal overflow on ${route} @ ${viewport.name} (${viewport.width}x${viewport.height})`
        ).toBeLessThanOrEqual(1)

        if (viewport.width < 768) {
          await expect(page.locator('#nav-hamburger')).toBeVisible()
        } else {
          await expect(page.locator('.nav-links')).toBeVisible()
        }
      }
    }
  })
})
