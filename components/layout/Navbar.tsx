'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { motion, AnimatePresence } from 'framer-motion'
import { Menu, X } from 'lucide-react'
import { useLanguage } from '@/context/LanguageContext'

const ASSET_VERSION = '20260207'

const navLinks = [
  { key: 'navAboutUs' as const, href: '/#about' },
  { key: 'navAbout' as const, href: '/#services' },
  { key: 'navPartnerships' as const, href: '/#partnerships' },
  { key: 'products' as const, href: '/#products' },
  { key: 'navProjects' as const, href: '/#projects' },
  { key: 'navTeam' as const, href: '/#team' },
  { key: 'navContact' as const, href: '/#contact' },
]

export default function Navbar() {
  const { t, lang, toggle } = useLanguage()
  const [scrolled, setScrolled] = useState(false)
  const [mobileOpen, setMobileOpen] = useState(false)
  const [activeSection, setActiveSection] = useState('')

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20)
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  useEffect(() => {
    const sections = document.querySelectorAll('section[id]')
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveSection(entry.target.id)
          }
        })
      },
      { rootMargin: '-50% 0px -50% 0px' }
    )
    sections.forEach((section) => observer.observe(section))
    return () => observer.disconnect()
  }, [])

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 768) setMobileOpen(false)
    }
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  useEffect(() => {
    if (mobileOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
    return () => { document.body.style.overflow = '' }
  }, [mobileOpen])

  return (
    <>
      <header
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          scrolled
            ? 'backdrop-blur-xl bg-bg/80 border-b border-border-subtle shadow-lg shadow-black/10'
            : 'bg-transparent'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-[60px] md:h-[72px]">
            <Link href="/" className="flex items-center gap-2 shrink-0">
              <Image
                src={`/assets/logo/logo.webp?v=${ASSET_VERSION}`}
                alt="Solarity AI"
                width={44}
                height={44}
                className="rounded-xl"
                priority
              />
              <span
                className="font-bold text-xl text-gold tracking-[0.01em] font-display"
                style={{
                  textShadow: '0 0 10px rgba(245, 197, 24, 0.25)',
                }}
              >
                Solarity AI
              </span>
            </Link>

            <nav className="hidden md:flex h-full items-center gap-8">
              {navLinks.map(link => {
                const sectionId = link.href.replace('/#', '')
                const isActive = activeSection === sectionId
                return (
                  <a
                    key={link.key}
                    href={link.href}
                    className={`relative inline-flex h-full items-center text-sm py-1 transition-colors duration-200 ${
                      isActive ? 'text-text-1 font-medium' : 'text-text-2 hover:text-text-1'
                    }`}
                  >
                    {t(link.key)}
                    {isActive && (
                      <motion.div
                        layoutId="nav-indicator"
                        className="absolute bottom-0 left-0 right-0 h-0.5 bg-accent rounded-full"
                        transition={{ type: 'spring', stiffness: 380, damping: 30 }}
                      />
                    )}
                  </a>
                )
              })}
            </nav>

            <div className="flex items-center gap-3">
              <button
                onClick={toggle}
                className="hidden md:flex items-center gap-1 text-xs font-semibold text-text-2 hover:text-text-1 transition-colors duration-200 bg-white/5 hover:bg-white/10 rounded-full px-3 py-1.5 border border-border-subtle"
                aria-label="Toggle language"
              >
                <span className={lang === 'en' ? 'text-text-1' : 'text-text-2'}>EN</span>
                <span className="text-text-3">|</span>
                <span className={lang === 'tr' ? 'text-text-1' : 'text-text-2'}>TR</span>
              </button>

              <Link
                href="/careers"
                className="hidden md:inline-flex items-center px-4 py-1.5 text-sm font-semibold rounded-lg bg-accent hover:bg-accent-soft text-white transition-all duration-200"
              >
                {t('navCareers')}
              </Link>

              <button
                onClick={() => setMobileOpen(v => !v)}
                className="md:hidden p-2 text-text-2 hover:text-text-1 transition-colors"
                aria-label={t('navToggleMenu')}
              >
                {mobileOpen ? <X size={22} /> : <Menu size={22} />}
              </button>
            </div>
          </div>
        </div>
      </header>

      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="fixed inset-0 z-40 bg-bg/95 backdrop-blur-lg md:hidden"
          >
            <motion.div
              initial={{ opacity: 0, y: -20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.25, delay: 0.05 }}
              className="flex flex-col items-center justify-center h-full gap-8 px-6"
            >
              {navLinks.map((link, i) => (
                <motion.a
                  key={link.key}
                  href={link.href}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 + i * 0.06 }}
                  onClick={() => setMobileOpen(false)}
                  className="text-2xl font-semibold text-text-1 hover:text-accent transition-colors font-display"
                >
                  {t(link.key)}
                </motion.a>
              ))}

              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 + navLinks.length * 0.06 }}
                className="flex items-center gap-4 mt-4"
              >
                <button
                  onClick={toggle}
                  className="flex items-center gap-1 text-sm font-semibold text-text-2 bg-white/5 rounded-full px-4 py-2 border border-border-subtle"
                >
                  <span className={lang === 'en' ? 'text-text-1' : 'text-text-2'}>EN</span>
                  <span className="text-text-3">|</span>
                  <span className={lang === 'tr' ? 'text-text-1' : 'text-text-2'}>TR</span>
                </button>

                <Link
                  href="/careers"
                  onClick={() => setMobileOpen(false)}
                  className="px-5 py-2 text-sm font-semibold rounded-xl bg-accent hover:bg-accent-soft text-white transition-colors"
                >
                  {t('navCareers')}
                </Link>
              </motion.div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}
