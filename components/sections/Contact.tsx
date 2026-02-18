'use client'

import { useState, useRef, useEffect, FormEvent } from 'react'
import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { MapPin, Mail, Briefcase, Linkedin, Clock } from 'lucide-react'
import Link from 'next/link'
import Script from 'next/script'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.1 } },
}

declare global {
  interface Window {
    turnstile?: {
      render: (element: string | HTMLElement, options: Record<string, unknown>) => string
      reset: (widgetId: string) => void
      getResponse: (widgetId: string) => string | undefined
    }
    gtag?: (...args: unknown[]) => void
  }
}

const TURNSTILE_SITE_KEY = '0x4AAAAAACI72SYLbDu1hDf5'
const FORMSUBMIT_EMAIL = 'info@solarityai.com'

export default function Contact() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })
  const turnstileRef = useRef<HTMLDivElement>(null)
  const widgetIdRef = useRef<string | null>(null)
  const [turnstileToken, setTurnstileToken] = useState<string>('')
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [submitted, setSubmitted] = useState(false)

  const [form, setForm] = useState({
    name: '',
    email: '',
    linkedin: '',
    company: '',
    subject: '',
    message: '',
  })

  const renderTurnstile = () => {
    if (!turnstileRef.current || !window.turnstile || widgetIdRef.current) return
    widgetIdRef.current = window.turnstile.render(turnstileRef.current, {
      sitekey: TURNSTILE_SITE_KEY,
      theme: 'dark',
      callback: (token: string) => setTurnstileToken(token),
      'expired-callback': () => setTurnstileToken(''),
    })
  }

  useEffect(() => {
    if (window.turnstile) renderTurnstile()
  }, [])

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm(prev => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setError(null)

    if (!form.name || !form.email || !form.message) {
      setError(t('formErrorRequiredFields'))
      return
    }

    if (form.linkedin && !form.linkedin.includes('linkedin.com/in/')) {
      setError(t('contactLinkedInInvalid'))
      return
    }

    if (!turnstileToken) {
      setError(t('formCaptchaError'))
      return
    }

    setSubmitting(true)

    const data = new FormData()
    data.append('name', form.name)
    data.append('email', form.email)
    if (form.linkedin) data.append('linkedin', form.linkedin)
    if (form.company) data.append('company', form.company)
    data.append('_subject', form.subject || t('contactFormSubject'))
    data.append('message', form.message)
    data.append('cf-turnstile-response', turnstileToken)

    try {
      const res = await fetch(`https://formsubmit.co/${FORMSUBMIT_EMAIL}`, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' },
      })

      if (res.ok) {
        setSubmitted(true)
        window.gtag?.('event', 'contact_form_submit', {
          event_category: 'Form',
          event_label: 'Contact',
        })
      } else {
        throw new Error('Submission failed')
      }
    } catch {
      setError('Something went wrong. Please try again.')
      if (window.turnstile && widgetIdRef.current) {
        window.turnstile.reset(widgetIdRef.current)
        setTurnstileToken('')
      }
    } finally {
      setSubmitting(false)
    }
  }

  const inputClass =
    'w-full px-4 py-3 rounded-xl bg-surface-2 border border-border text-text-1 placeholder-text-3 text-sm focus:outline-none focus:border-accent/60 focus:ring-2 focus:ring-accent/10 transition-all duration-200'
  const labelClass = 'block text-xs font-semibold text-text-2 uppercase tracking-wider mb-2'

  const infoItems = [
    {
      icon: MapPin,
      label: t('contactAddress'),
      value: t('contactAddressValue'),
      href: undefined,
    },
    {
      icon: Clock,
      label: t('contactResponseTime'),
      value: t('contactResponseTimeValue'),
      href: undefined,
    },
    {
      icon: Mail,
      label: t('contactEmail'),
      value: 'info@solarityai.com',
      href: 'mailto:info@solarityai.com',
    },
    {
      icon: Briefcase,
      label: t('contactCareers'),
      value: t('contactViewPositions'),
      href: '/careers',
      isInternal: true,
    },
    {
      icon: Linkedin,
      label: 'LinkedIn',
      value: 'Solarity AI LLC',
      href: 'https://www.linkedin.com/company/solarityai-llc',
    },
  ]

  return (
    <>
      <Script
        src="https://challenges.cloudflare.com/turnstile/v0/api.js"
        onLoad={renderTurnstile}
        strategy="lazyOnload"
      />

      <section id="contact" className="py-24 bg-bg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            ref={ref}
            variants={stagger}
            initial="hidden"
            animate={isInView ? 'visible' : 'hidden'}
          >
            <SectionHeader
              label={t('contact')}
              title={t('contactSubtitle')}
              description={t('contactSubtitleDesc')}
            />

            <div className="grid grid-cols-1 lg:grid-cols-5 gap-12">
              <motion.div variants={fadeInUp} className="lg:col-span-2 space-y-5">
                {infoItems.map(({ icon: Icon, label, value, href, isInternal }) => (
                  <div key={label} className="flex items-start gap-4 group">
                    <div className="w-10 h-10 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center shrink-0 mt-0.5 group-hover:bg-accent/20 transition-colors duration-300">
                      <Icon size={18} className="text-accent" />
                    </div>
                    <div>
                      <h4 className="text-sm font-semibold text-text-1 mb-0.5 font-display">
                        {label}
                      </h4>
                      {href ? (
                        isInternal ? (
                          <Link
                            href={href}
                            className="text-sm text-text-2 hover:text-accent transition-colors"
                          >
                            {value}
                          </Link>
                        ) : (
                          <a
                            href={href}
                            target={href.startsWith('http') ? '_blank' : undefined}
                            rel={href.startsWith('http') ? 'noopener noreferrer' : undefined}
                            className="text-sm text-text-2 hover:text-accent transition-colors"
                            onClick={
                              href.includes('linkedin')
                                ? () =>
                                    window.gtag?.('event', 'click', {
                                      event_category: 'Social',
                                      event_label: 'LinkedIn Contact',
                                    })
                                : undefined
                            }
                          >
                            {value}
                          </a>
                        )
                      ) : (
                        <p className="text-sm text-text-2">{value}</p>
                      )}
                    </div>
                  </div>
                ))}

                {/* Map embed */}
                <div className="overflow-hidden rounded-xl border border-border">
                  <iframe
                    src="https://maps.google.com/maps?q=310+Gran+Via,+Irving,+TX+75039,+USA&output=embed"
                    width="100%"
                    height="220"
                    style={{ border: 0 }}
                    loading="lazy"
                    referrerPolicy="no-referrer-when-downgrade"
                    title="Solarity AI Office Location"
                  />
                </div>
              </motion.div>

              <motion.div variants={fadeInUp} className="lg:col-span-3">
                {submitted ? (
                  <div className="flex flex-col items-center justify-center h-full p-8 rounded-2xl border border-accent/30 bg-accent/5 text-center gap-4">
                    <div className="w-14 h-14 rounded-full bg-accent/20 flex items-center justify-center">
                      <Mail size={24} className="text-accent" />
                    </div>
                    <h3 className="text-xl font-bold text-text-1 font-display">
                      {t('contactFormSuccess')}
                    </h3>
                    <p className="text-sm text-text-2 max-w-sm">{t('contactFormSuccessMsg')}</p>
                  </div>
                ) : (
                  <form onSubmit={handleSubmit} className="space-y-5">
                    <div>
                      <label className={labelClass}>
                        {t('contactName')} <span className="text-accent">*</span>
                      </label>
                      <input
                        type="text"
                        name="name"
                        required
                        value={form.name}
                        onChange={handleChange}
                        placeholder={t('contactNamePlaceholder')}
                        className={inputClass}
                      />
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                      <div>
                        <label className={labelClass}>
                          {t('contactEmailField')} <span className="text-accent">*</span>
                        </label>
                        <input
                          type="email"
                          name="email"
                          required
                          value={form.email}
                          onChange={handleChange}
                          placeholder={t('contactEmailPlaceholder')}
                          className={inputClass}
                        />
                      </div>
                      <div>
                        <label className={labelClass}>{t('contactCompany')}</label>
                        <input
                          type="text"
                          name="company"
                          value={form.company}
                          onChange={handleChange}
                          placeholder={t('contactCompanyPlaceholder')}
                          className={inputClass}
                        />
                      </div>
                    </div>

                    <div>
                      <label className={labelClass}>{t('contactLinkedIn')}</label>
                      <input
                        type="url"
                        name="linkedin"
                        value={form.linkedin}
                        onChange={handleChange}
                        placeholder={t('contactLinkedInPlaceholder')}
                        className={inputClass}
                      />
                    </div>

                    <div>
                      <label className={labelClass}>{t('contactSubject')}</label>
                      <input
                        type="text"
                        name="subject"
                        value={form.subject}
                        onChange={handleChange}
                        className={inputClass}
                      />
                    </div>

                    <div>
                      <label className={labelClass}>
                        {t('contactMessage')} <span className="text-accent">*</span>
                      </label>
                      <textarea
                        name="message"
                        required
                        rows={5}
                        value={form.message}
                        onChange={handleChange}
                        placeholder={t('contactMessagePlaceholder')}
                        className={`${inputClass} resize-none`}
                      />
                    </div>

                    <div ref={turnstileRef} />

                    {error && (
                      <p className="text-sm text-red-400 bg-red-400/10 border border-red-400/20 rounded-xl px-4 py-3">
                        {error}
                      </p>
                    )}

                    <button
                      type="submit"
                      disabled={submitting}
                      className="w-full py-2.5 px-6 rounded-xl bg-accent hover:bg-accent-soft disabled:opacity-50 disabled:cursor-not-allowed text-white text-sm font-semibold transition-all duration-200 active:scale-[0.98]"
                    >
                      {submitting ? '...' : t('contactSend')}
                    </button>
                  </form>
                )}
              </motion.div>
            </div>
          </motion.div>
        </div>
      </section>
    </>
  )
}
