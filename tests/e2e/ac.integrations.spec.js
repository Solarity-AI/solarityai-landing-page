const { test, expect } = require('@playwright/test')

const {
  installTurnstileMock,
  isChromiumDesktop,
  readDataLayerEvents,
} = require('./helpers/site')

test.describe('Acceptance Criteria - forms and integrations', () => {
  test.beforeEach(async ({ page }, testInfo) => {
    test.skip(!isChromiumDesktop(testInfo), 'Form integration tests run once on Chromium desktop.')
    await installTurnstileMock(page)
  })

  test('AC07 + AC09 contact form submits via FormSubmit with Turnstile and emits gtag event', async ({ page }) => {
    let postBody = ''

    await page.route('https://formsubmit.co/**', async (route) => {
      postBody = route.request().postDataBuffer()?.toString('utf8') || ''
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ success: 'true' }),
      })
    })

    await page.goto('/')

    await page.fill('#contact-name', 'Playwright Contact Test')
    await page.fill('#contact-email', 'qa-contact@example.com')
    await page.fill('#contact-company', 'Solarity QA')
    await page.fill('#contact-linkedin', 'https://www.linkedin.com/in/playwright-qa')
    await page.fill('#contact-message', 'This is an automated acceptance test for contact form flow.')

    await page.click('#contact-submit')

    await expect(page.locator('#contact-success')).toBeVisible()
    await expect(page.locator('#contact-form')).toBeHidden()

    expect(postBody.includes('Playwright Contact Test')).toBeTruthy()
    expect(postBody.includes('qa-contact@example.com')).toBeTruthy()
    expect(postBody.includes('cf-turnstile-response')).toBeTruthy()
    expect(postBody.includes('pw-turnstile-token')).toBeTruthy()

    const events = await readDataLayerEvents(page)
    const submitEvent = events.find((entry) => entry.command === 'event' && entry.name === 'contact_form_submit')

    expect(submitEvent).toBeTruthy()
    expect(submitEvent.params.event_category).toBe('Form')
    expect(submitEvent.params.event_label).toBe('Contact')
  })

  test('AC08 + AC09 careers form submits with CV upload and emits gtag event', async ({ page }) => {
    let postBody = ''

    await page.route('https://formsubmit.co/**', async (route) => {
      postBody = route.request().postDataBuffer()?.toString('utf8') || ''
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ success: 'true' }),
      })
    })

    await page.goto('/careers.html')

    await page.fill('#c-name', 'Playwright Careers Test')
    await page.fill('#c-email', 'qa-careers@example.com')
    await page.fill('#c-linkedin', 'https://www.linkedin.com/in/playwright-careers-qa')
    await page.fill('#c-portfolio', 'https://github.com/playwright-qa')
    await page.selectOption('#c-position', 'Full Stack Engineer')
    await page.selectOption('#c-worktype', 'full-time')
    await page.fill('#c-message', 'This is an automated acceptance test for careers form flow.')

    await page.setInputFiles('#cv-input', {
      name: 'cv.pdf',
      mimeType: 'application/pdf',
      buffer: Buffer.from('%PDF-1.4\n% Automated CV test payload\n'),
    })

    await expect(page.locator('#cv-selected')).toBeVisible()
    await expect(page.locator('#cv-filename')).toHaveText('cv.pdf')

    await page.click('#careers-submit')

    await expect(page.locator('#careers-success')).toBeVisible()
    await expect(page.locator('#careers-form')).toBeHidden()

    expect(postBody.includes('Playwright Careers Test')).toBeTruthy()
    expect(postBody.includes('qa-careers@example.com')).toBeTruthy()
    expect(postBody.includes('filename="cv.pdf"')).toBeTruthy()
    expect(postBody.includes('cf-turnstile-response')).toBeTruthy()
    expect(postBody.includes('pw-turnstile-token')).toBeTruthy()

    const events = await readDataLayerEvents(page)
    const submitEvent = events.find((entry) => entry.command === 'event' && entry.name === 'careers_form_submit')

    expect(submitEvent).toBeTruthy()
    expect(submitEvent.params.event_category).toBe('Form')
    expect(submitEvent.params.event_label).toBe('Careers')
  })

  test('AC09 social link click emits GA event', async ({ page }) => {
    await page.goto('/')

    await page.evaluate(() => {
      const socialLink = document.querySelector('.footer-social-link')
      if (!socialLink) {
        return
      }

      socialLink.addEventListener('click', (event) => {
        event.preventDefault()
      }, { capture: true, once: true })

      socialLink.click()
    })

    const events = await readDataLayerEvents(page)
    const socialEvent = events.find(
      (entry) => entry.command === 'event' && entry.name === 'click' && entry.params?.event_category === 'Social'
    )

    expect(socialEvent).toBeTruthy()
  })

  test('AC07/AC08 Turnstile script and container exist on relevant pages', async ({ page }) => {
    await page.goto('/')
    await expect(page.locator('#contact-turnstile')).toBeVisible()
    await expect(page.locator('script[src*="challenges.cloudflare.com/turnstile"]')).toHaveCount(1)

    await page.goto('/careers.html')
    await expect(page.locator('#careers-turnstile')).toBeVisible()
    await expect(page.locator('script[src*="challenges.cloudflare.com/turnstile"]')).toHaveCount(1)
  })
})
