'use client'

import { useState, useRef, useEffect, FormEvent, ChangeEvent } from 'react'
import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { Rocket, BookOpen, Users, ExternalLink, Upload, X, CheckCircle } from 'lucide-react'
import Link from 'next/link'
import Script from 'next/script'
import Navbar from '@/components/layout/Navbar'
import Footer from '@/components/layout/Footer'
import { useLanguage } from '@/context/LanguageContext'

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

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.1 } },
}

const POSITIONS = [
  { href: 'https://drive.google.com/drive/folders/1_example', key: 'careersPos1Title' as const, descKey: 'careersPos1Desc' as const },
  { href: 'https://drive.google.com/drive/folders/1_example', key: 'careersPos2Title' as const, descKey: 'careersPos2Desc' as const },
  { href: 'https://drive.google.com/drive/folders/1_example', key: 'careersPos3Title' as const, descKey: 'careersPos3Desc' as const },
  { href: 'https://drive.google.com/drive/folders/1_example', key: 'careersPos4Title' as const, descKey: 'careersPos4Desc' as const },
]

export default function CareersPage() {
  const { t } = useLanguage()

  const turnstileRef = useRef<HTMLDivElement>(null)
  const widgetIdRef = useRef<string | null>(null)
  const [turnstileToken, setTurnstileToken] = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [submitted, setSubmitted] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [cvFile, setCvFile] = useState<File | null>(null)

  const [form, setForm] = useState({
    name: '',
    email: '',
    linkedin: '',
    portfolio: '',
    position: '',
    workType: '',
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

  const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    setForm(prev => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    const allowed = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    if (!allowed.includes(file.type)) {
      setError(t('careersFormFileTypeError'))
      e.target.value = ''
      return
    }
    if (file.size > 5 * 1024 * 1024) {
      setError('File must be smaller than 5MB.')
      e.target.value = ''
      return
    }
    setError(null)
    setCvFile(file)
  }

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    setError(null)

    if (!form.name || !form.email || !form.linkedin || !form.position || !form.workType) {
      setError(t('formErrorRequiredFields'))
      return
    }

    if (form.linkedin && !form.linkedin.includes('linkedin.com/in/')) {
      setError(t('contactLinkedInInvalid'))
      return
    }

    if (form.portfolio && !form.portfolio.startsWith('http')) {
      setError(t('careersPortfolioInvalid'))
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
    data.append('linkedin', form.linkedin)
    if (form.portfolio) data.append('portfolio', form.portfolio)
    data.append('position', form.position)
    data.append('workType', form.workType)
    if (form.message) data.append('message', form.message)
    if (cvFile) data.append('cv', cvFile, cvFile.name)
    data.append('_subject', 'New Job Application - Solarity AI')
    data.append('cf-turnstile-response', turnstileToken)

    try {
      const res = await fetch(`https://formsubmit.co/${FORMSUBMIT_EMAIL}`, {
        method: 'POST',
        body: data,
        headers: { Accept: 'application/json' },
      })

      if (res.ok) {
        setSubmitted(true)
        window.gtag?.('event', 'careers_form_submit', {
          event_category: 'Form',
          event_label: 'Careers',
        })
      } else {
        throw new Error('Submission failed')
      }
    } catch {
      setError(t('careersFormErrorMsg'))
      if (window.turnstile && widgetIdRef.current) {
        window.turnstile.reset(widgetIdRef.current)
        setTurnstileToken('')
      }
    } finally {
      setSubmitting(false)
    }
  }

  const inputClass =
    'w-full px-4 py-3 rounded-xl bg-[#1a1a1a] border border-[#1f1f1f] text-[#f1f5f9] placeholder-[#475569] text-sm focus:outline-none focus:border-[#2563eb]/60 transition-colors'
  const labelClass = 'block text-xs font-semibold text-[#94a3b8] uppercase tracking-wider mb-2'

  return (
    <>
      <Script
        src="https://challenges.cloudflare.com/turnstile/v0/api.js"
        onLoad={renderTurnstile}
        strategy="lazyOnload"
      />
      <Navbar />

      <main className="min-h-screen bg-[#0a0a0a]">
        {/* Hero */}
        <section className="relative pt-32 pb-20 overflow-hidden">
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.015)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.015)_1px,transparent_1px)] bg-[size:64px_64px]" />
          <div className="absolute inset-0 bg-gradient-to-b from-[#2563eb]/5 via-transparent to-transparent" />
          <div className="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <motion.div
              initial="hidden"
              animate="visible"
              variants={stagger}
            >
              <motion.span
                variants={fadeInUp}
                className="inline-block text-xs font-semibold uppercase tracking-widest text-[#2563eb] mb-4 px-3 py-1 rounded-full border border-[#2563eb]/30 bg-[#2563eb]/10"
              >
                {t('careersHeroTag')}
              </motion.span>
              <motion.h1
                variants={fadeInUp}
                className="text-4xl sm:text-5xl font-bold text-[#f1f5f9] mb-6 leading-tight"
                style={{ fontFamily: 'var(--font-poppins)' }}
              >
                {t('careersHeroTitle')}
              </motion.h1>
              <motion.p
                variants={fadeInUp}
                className="text-lg text-[#94a3b8] max-w-2xl mx-auto leading-relaxed"
              >
                {t('careersHeroSubtitle')}
              </motion.p>
            </motion.div>
          </div>
        </section>

        {/* Why Solarity AI */}
        <section className="py-16 bg-[#111111]">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-10">
              <h2
                className="text-2xl sm:text-3xl font-bold text-[#f1f5f9] mb-3"
                style={{ fontFamily: 'var(--font-poppins)' }}
              >
                {t('careersWhyTitle')}
              </h2>
              <p className="text-[#94a3b8] text-sm">{t('careersWhySubtitle')}</p>
            </div>
            <motion.div
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: '-60px' }}
              variants={stagger}
              className="grid grid-cols-1 md:grid-cols-3 gap-6"
            >
              {[
                { icon: Rocket, titleKey: 'careersWhy1Title' as const, descKey: 'careersWhy1Desc' as const },
                { icon: BookOpen, titleKey: 'careersWhy2Title' as const, descKey: 'careersWhy2Desc' as const },
                { icon: Users, titleKey: 'careersWhy3Title' as const, descKey: 'careersWhy3Desc' as const },
              ].map(({ icon: Icon, titleKey, descKey }) => (
                <motion.div
                  key={titleKey}
                  variants={fadeInUp}
                  className="p-6 rounded-2xl border border-[#1f1f1f] bg-[#0a0a0a] hover:border-[#2563eb]/30 transition-colors duration-300"
                >
                  <div className="w-12 h-12 rounded-xl bg-[#2563eb]/10 border border-[#2563eb]/20 flex items-center justify-center mb-4">
                    <Icon size={22} className="text-[#2563eb]" />
                  </div>
                  <h3
                    className="text-base font-semibold text-[#f1f5f9] mb-2"
                    style={{ fontFamily: 'var(--font-poppins)' }}
                  >
                    {t(titleKey)}
                  </h3>
                  <p className="text-sm text-[#94a3b8] leading-relaxed">{t(descKey)}</p>
                </motion.div>
              ))}
            </motion.div>
          </div>
        </section>

        {/* Open Positions */}
        <section className="py-16 bg-[#0a0a0a]">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-10">
              <h2
                className="text-2xl sm:text-3xl font-bold text-[#f1f5f9] mb-3"
                style={{ fontFamily: 'var(--font-poppins)' }}
              >
                {t('careersPositionsTitle')}
              </h2>
              <p className="text-[#94a3b8] text-sm mb-6">{t('careersPositionsSubtitle')}</p>
              <a
                href="https://drive.google.com/drive/folders/1_example"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-sm text-[#2563eb] hover:text-[#1d4ed8] font-semibold transition-colors"
              >
                <ExternalLink size={14} />
                {t('careersDriveLink')}
              </a>
            </div>
            <motion.div
              initial="hidden"
              whileInView="visible"
              viewport={{ once: true, margin: '-60px' }}
              variants={stagger}
              className="grid grid-cols-1 md:grid-cols-2 gap-5"
            >
              {POSITIONS.map(({ href, key, descKey }) => (
                <motion.div
                  key={key}
                  variants={fadeInUp}
                  className="p-6 rounded-2xl border border-[#1f1f1f] bg-[#111111] hover:border-[#2563eb]/30 transition-all duration-300"
                >
                  <div className="flex items-start justify-between gap-4 mb-3">
                    <h3
                      className="text-base font-semibold text-[#f1f5f9]"
                      style={{ fontFamily: 'var(--font-poppins)' }}
                    >
                      {t(key)}
                    </h3>
                    <div className="flex gap-2 shrink-0">
                      <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-[#2563eb]/10 text-[#2563eb] border border-[#2563eb]/20">
                        {t('careersFullTime')}
                      </span>
                      <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-white/5 text-[#94a3b8] border border-white/10">
                        {t('careersPartTime')}
                      </span>
                    </div>
                  </div>
                  <p className="text-sm text-[#94a3b8] leading-relaxed mb-4">{t(descKey)}</p>
                  <a
                    href={href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#2563eb] hover:text-[#1d4ed8] transition-colors"
                  >
                    <ExternalLink size={12} />
                    {t('careersViewJob')}
                  </a>
                </motion.div>
              ))}
            </motion.div>
          </div>
        </section>

        {/* Application Form */}
        <section className="py-16 bg-[#111111]">
          <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-10">
              <h2
                className="text-2xl sm:text-3xl font-bold text-[#f1f5f9] mb-3"
                style={{ fontFamily: 'var(--font-poppins)' }}
              >
                {t('careersFormTitle')}
              </h2>
              <p className="text-[#94a3b8] text-sm">{t('careersFormSubtitle')}</p>
            </div>

            {submitted ? (
              <div className="flex flex-col items-center justify-center p-10 rounded-2xl border border-[#2563eb]/30 bg-[#2563eb]/5 text-center gap-4">
                <div className="w-14 h-14 rounded-full bg-[#2563eb]/20 flex items-center justify-center">
                  <CheckCircle size={24} className="text-[#2563eb]" />
                </div>
                <h3
                  className="text-xl font-bold text-[#f1f5f9]"
                  style={{ fontFamily: 'var(--font-poppins)' }}
                >
                  {t('careersFormSuccess')}
                </h3>
                <p className="text-sm text-[#94a3b8] max-w-sm">{t('careersFormSuccessMsg')}</p>
                <Link
                  href="/"
                  className="mt-2 px-5 py-2.5 text-sm font-semibold rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] text-white transition-colors"
                >
                  Return Home
                </Link>
              </div>
            ) : (
              <form onSubmit={handleSubmit} className="space-y-5">
                {/* Name */}
                <div>
                  <label className={labelClass}>
                    {t('careersFormName')} <span className="text-[#2563eb]">*</span>
                  </label>
                  <input
                    type="text"
                    name="name"
                    required
                    value={form.name}
                    onChange={handleChange}
                    placeholder={t('careersFormNamePlaceholder')}
                    className={inputClass}
                  />
                </div>

                {/* Email */}
                <div>
                  <label className={labelClass}>
                    {t('careersFormEmail')} <span className="text-[#2563eb]">*</span>
                  </label>
                  <input
                    type="email"
                    name="email"
                    required
                    value={form.email}
                    onChange={handleChange}
                    placeholder={t('careersFormEmailPlaceholder')}
                    className={inputClass}
                  />
                </div>

                {/* LinkedIn */}
                <div>
                  <label className={labelClass}>
                    {t('careersLinkedIn')} <span className="text-[#2563eb]">*</span>
                  </label>
                  <input
                    type="url"
                    name="linkedin"
                    required
                    value={form.linkedin}
                    onChange={handleChange}
                    placeholder={t('careersLinkedInPlaceholder')}
                    className={inputClass}
                  />
                </div>

                {/* Portfolio */}
                <div>
                  <label className={labelClass}>{t('careersPortfolio')}</label>
                  <input
                    type="url"
                    name="portfolio"
                    value={form.portfolio}
                    onChange={handleChange}
                    placeholder={t('careersPortfolioPlaceholder')}
                    className={inputClass}
                  />
                </div>

                {/* Position + Work Type */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                  <div>
                    <label className={labelClass}>
                      {t('careersFormPosition')} <span className="text-[#2563eb]">*</span>
                    </label>
                    <select
                      name="position"
                      required
                      value={form.position}
                      onChange={handleChange}
                      className={inputClass}
                    >
                      <option value="">{t('careersFormPositionSelect')}</option>
                      <option value="Full Stack Engineer">{t('careersPos1Title')}</option>
                      <option value="Marketing Specialist">{t('careersPos2Title')}</option>
                      <option value="Business Development Manager">{t('careersPos3Title')}</option>
                      <option value="UI/UX Designer">{t('careersPos4Title')}</option>
                    </select>
                  </div>
                  <div>
                    <label className={labelClass}>
                      {t('careersFormWorkType')} <span className="text-[#2563eb]">*</span>
                    </label>
                    <select
                      name="workType"
                      required
                      value={form.workType}
                      onChange={handleChange}
                      className={inputClass}
                    >
                      <option value="">{t('careersFormWorkTypeSelect')}</option>
                      <option value="full-time">{t('careersFullTime')}</option>
                      <option value="part-time">{t('careersPartTime')}</option>
                    </select>
                  </div>
                </div>

                {/* CV Upload */}
                <div>
                  <label className={labelClass}>{t('careersFormCV')}</label>
                  {cvFile ? (
                    <div className="flex items-center gap-3 px-4 py-3 rounded-xl bg-[#1a1a1a] border border-[#2563eb]/40">
                      <Upload size={16} className="text-[#2563eb] shrink-0" />
                      <span className="text-sm text-[#f1f5f9] flex-1 truncate">{cvFile.name}</span>
                      <button
                        type="button"
                        onClick={() => setCvFile(null)}
                        className="text-[#475569] hover:text-[#f1f5f9] transition-colors"
                        aria-label={t('careersFormCVRemove')}
                      >
                        <X size={16} />
                      </button>
                    </div>
                  ) : (
                    <label className="flex flex-col items-center justify-center px-4 py-6 rounded-xl bg-[#1a1a1a] border border-dashed border-[#1f1f1f] hover:border-[#2563eb]/40 cursor-pointer transition-colors">
                      <Upload size={20} className="text-[#475569] mb-2" />
                      <span className="text-sm text-[#94a3b8]">{t('careersFormCVDrag')}</span>
                      <span className="text-xs text-[#475569] mt-1">{t('careersFormCVFormat')}</span>
                      <input
                        type="file"
                        accept=".pdf,.doc,.docx"
                        onChange={handleFileChange}
                        className="sr-only"
                      />
                    </label>
                  )}
                </div>

                {/* Message */}
                <div>
                  <label className={labelClass}>{t('careersFormMessage')}</label>
                  <textarea
                    name="message"
                    rows={4}
                    value={form.message}
                    onChange={handleChange}
                    placeholder={t('careersFormMessagePlaceholder')}
                    className={`${inputClass} resize-none`}
                  />
                </div>

                {/* Turnstile */}
                <div ref={turnstileRef} />

                {error && (
                  <p className="text-sm text-red-400 bg-red-400/10 border border-red-400/20 rounded-xl px-4 py-3">
                    {error}
                  </p>
                )}

                <button
                  type="submit"
                  disabled={submitting}
                  className="w-full py-3.5 px-6 rounded-xl bg-[#2563eb] hover:bg-[#1d4ed8] disabled:opacity-50 disabled:cursor-not-allowed text-white text-sm font-semibold transition-colors duration-200"
                >
                  {submitting ? t('careersFormSubmitting') : t('careersFormSubmit')}
                </button>
              </form>
            )}
          </div>
        </section>
      </main>

      <Footer />
    </>
  )
}
