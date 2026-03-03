const { test, expect } = require('@playwright/test')

const {
  PAGE_PATHS,
  slugForPath,
} = require('./helpers/site')

test.describe('Acceptance Criteria - visual regression (AC01)', () => {
  test.skip(!process.env.PLAYWRIGHT_VISUAL, 'Set PLAYWRIGHT_VISUAL=1 to enable visual baseline assertions.')

  for (const route of PAGE_PATHS) {
    test(`snapshot ${route}`, async ({ page }, testInfo) => {
      await page.goto(route)
      await page.waitForTimeout(500)
      await page.evaluate(() => window.scrollTo(0, 0))

      const snapshotName = `${slugForPath(route)}-${testInfo.project.name}.png`

      await expect(page).toHaveScreenshot(snapshotName, {
        fullPage: true,
        maxDiffPixelRatio: 0.015,
      })
    })
  }
})
