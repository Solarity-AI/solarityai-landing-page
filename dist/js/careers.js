/* Solarity AI — careers.js
   Careers form handler: FormSubmit.co + Cloudflare Turnstile + CV upload */

const TURNSTILE_SITE_KEY = '0x4AAAAAACI72SYLbDu1hDf5'
const FORMSUBMIT_EMAIL = 'info@solarityai.com'
const CAREERS_DRIVE = 'https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws'

let careersWidgetId = null
let careersToken = ''
let cvFile = null

function initCareersPage() {
  // Set Drive link href
  const driveLinks = document.querySelectorAll('.js-drive-link')
  driveLinks.forEach(a => { a.href = CAREERS_DRIVE })

  // Init Turnstile
  if (window.turnstile) {
    initCareerstile()
  } else {
    const check = setInterval(() => {
      if (window.turnstile) {
        clearInterval(check)
        initCareerstile()
      }
    }, 300)
    setTimeout(() => clearInterval(check), 10000)
  }

  // CV upload
  const cvInput = document.getElementById('cv-input')
  const cvArea = document.getElementById('cv-upload-area')
  const cvSelected = document.getElementById('cv-selected')
  const cvName = document.getElementById('cv-filename')
  const cvRemove = document.getElementById('cv-remove')

  if (cvInput) {
    cvInput.addEventListener('change', (e) => {
      const file = e.target.files?.[0]
      if (!file) return
      const allowed = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
      if (!allowed.includes(file.type)) {
        showCareersError(t('careersFormFileTypeError'))
        cvInput.value = ''
        return
      }
      if (file.size > 5 * 1024 * 1024) {
        showCareersError('File must be smaller than 5MB.')
        cvInput.value = ''
        return
      }
      cvFile = file
      cvName.textContent = file.name
      cvArea.style.display = 'none'
      cvSelected.style.display = 'flex'
    })

    cvRemove?.addEventListener('click', () => {
      cvFile = null
      cvInput.value = ''
      cvArea.style.display = 'flex'
      cvSelected.style.display = 'none'
    })
  }

  // Form submit
  const form = document.getElementById('careers-form')
  if (!form) return

  form.addEventListener('submit', async (e) => {
    e.preventDefault()
    const errorEl = document.getElementById('careers-error')
    errorEl.style.display = 'none'

    const name = form.querySelector('#c-name').value.trim()
    const email = form.querySelector('#c-email').value.trim()
    const linkedin = form.querySelector('#c-linkedin').value.trim()
    const portfolio = form.querySelector('#c-portfolio').value.trim()
    const position = form.querySelector('#c-position').value
    const workType = form.querySelector('#c-worktype').value
    const message = form.querySelector('#c-message').value.trim()

    if (!name || !email || !linkedin || !position || !workType) {
      showCareersError(t('formErrorRequiredFields'))
      return
    }

    if (linkedin && !linkedin.includes('linkedin.com/in/')) {
      showCareersError(t('contactLinkedInInvalid'))
      return
    }

    if (portfolio && !portfolio.startsWith('http')) {
      showCareersError(t('careersPortfolioInvalid'))
      return
    }

    if (!careersToken) {
      showCareersError(t('formCaptchaError'))
      return
    }

    setCareersSubmitting(true)

    const data = new FormData()
    data.append('name', name)
    data.append('email', email)
    data.append('linkedin', linkedin)
    if (portfolio) data.append('portfolio', portfolio)
    data.append('position', position)
    data.append('workType', workType)
    if (message) data.append('message', message)
    if (cvFile) data.append('cv', cvFile, cvFile.name)
    data.append('_subject', 'New Job Application - Solarity AI')
    data.append('cf-turnstile-response', careersToken)

    try {
      const res = await fetch(`https://formsubmit.co/${FORMSUBMIT_EMAIL}`, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' },
      })

      if (res.ok) {
        form.style.display = 'none'
        document.getElementById('careers-success').style.display = 'flex'
        window.gtag?.('event', 'careers_form_submit', {
          event_category: 'Form',
          event_label: 'Careers',
        })
      } else {
        throw new Error('Submission failed')
      }
    } catch {
      showCareersError(t('careersFormErrorMsg'))
      if (window.turnstile && careersWidgetId) {
        window.turnstile.reset(careersWidgetId)
        careersToken = ''
      }
    } finally {
      setCareersSubmitting(false)
    }
  })
}

function initCareerstile() {
  const container = document.getElementById('careers-turnstile')
  if (!container || !window.turnstile || careersWidgetId) return
  careersWidgetId = window.turnstile.render(container, {
    sitekey: TURNSTILE_SITE_KEY,
    theme: 'dark',
    callback: (token) => { careersToken = token },
    'expired-callback': () => { careersToken = '' },
  })
}

function showCareersError(msg) {
  const el = document.getElementById('careers-error')
  if (el) {
    el.textContent = msg
    el.style.display = 'block'
  }
}

function setCareersSubmitting(isSubmitting) {
  const btn = document.getElementById('careers-submit')
  if (!btn) return
  btn.disabled = isSubmitting
  const span = btn.querySelector('span')
  if (span) {
    span.textContent = isSubmitting ? t('careersFormSubmitting') : t('careersFormSubmit')
  }
}

document.addEventListener('DOMContentLoaded', initCareersPage)
