/* Solarity AI — contact.js
   Contact form handler: FormSubmit.co + Cloudflare Turnstile */

const TURNSTILE_SITE_KEY = '0x4AAAAAACI72SYLbDu1hDf5'
const FORMSUBMIT_EMAIL = 'info@solarityai.com'

let contactWidgetId = null
let contactToken = ''

function initContactTurnstile() {
  const container = document.getElementById('contact-turnstile')
  if (!container || !window.turnstile || contactWidgetId) return
  contactWidgetId = window.turnstile.render(container, {
    sitekey: TURNSTILE_SITE_KEY,
    theme: 'dark',
    callback: (token) => { contactToken = token },
    'expired-callback': () => { contactToken = '' },
  })
}

document.addEventListener('DOMContentLoaded', () => {
  // Turnstile may already be loaded
  if (window.turnstile) {
    initContactTurnstile()
  } else {
    // Wait for Turnstile to load (max 10s)
    const checkInterval = setInterval(() => {
      if (window.turnstile) {
        clearInterval(checkInterval)
        initContactTurnstile()
      }
    }, 300)
    setTimeout(() => clearInterval(checkInterval), 10000)
  }

  const form = document.getElementById('contact-form')
  const errorEl = document.getElementById('contact-error')
  const successEl = document.getElementById('contact-success')
  const submitBtn = document.getElementById('contact-submit')

  if (!form) return

  form.addEventListener('submit', async (e) => {
    e.preventDefault()
    errorEl.style.display = 'none'

    const name = form.querySelector('#contact-name').value.trim()
    const email = form.querySelector('#contact-email').value.trim()
    const linkedin = form.querySelector('#contact-linkedin').value.trim()
    const company = form.querySelector('#contact-company').value.trim()
    const subject = form.querySelector('#contact-subject').value.trim()
    const message = form.querySelector('#contact-message').value.trim()

    if (!name || !email || !message) {
      showError(t('formErrorRequiredFields'))
      return
    }

    if (linkedin && !linkedin.includes('linkedin.com/in/')) {
      showError(t('contactLinkedInInvalid'))
      return
    }

    if (!contactToken) {
      showError(t('formCaptchaError'))
      return
    }

    setSubmitting(true)

    const data = new FormData()
    data.append('name', name)
    data.append('email', email)
    if (linkedin) data.append('linkedin', linkedin)
    if (company) data.append('company', company)
    data.append('_subject', subject || t('contactFormSubject'))
    data.append('message', message)
    data.append('cf-turnstile-response', contactToken)

    try {
      const res = await fetch(`https://formsubmit.co/${FORMSUBMIT_EMAIL}`, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' },
      })

      if (res.ok) {
        form.style.display = 'none'
        successEl.style.display = 'flex'
        window.gtag?.('event', 'contact_form_submit', {
          event_category: 'Form',
          event_label: 'Contact',
        })
      } else {
        throw new Error('Submission failed')
      }
    } catch {
      showError('Something went wrong. Please try again.')
      if (window.turnstile && contactWidgetId) {
        window.turnstile.reset(contactWidgetId)
        contactToken = ''
      }
    } finally {
      setSubmitting(false)
    }
  })

  function showError(msg) {
    errorEl.textContent = msg
    errorEl.style.display = 'block'
  }

  function setSubmitting(isSubmitting) {
    submitBtn.disabled = isSubmitting
    const span = submitBtn.querySelector('span')
    if (span) {
      span.textContent = isSubmitting ? '...' : t('contactSend')
    }
  }
})
