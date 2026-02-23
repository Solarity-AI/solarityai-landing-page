'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { ArrowRight } from 'lucide-react'
import { useLanguage } from '@/context/LanguageContext'
import type { TranslationKey } from '@/lib/translations'

const container: Variants = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.15 },
  },
}

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 32 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: 'easeOut' } },
}

interface HeroStat {
  value?: string
  valueKey?: TranslationKey
  labelKey: TranslationKey
}

const heroStats: HeroStat[] = [
  { value: '20+', labelKey: 'statsProjects' },
  { value: '200%', labelKey: 'statsSatisfaction' },
  { valueKey: 'statsSupportNumber', labelKey: 'statsSupport' },
  { value: '100M+', labelKey: 'statsRevenue' },
  { value: '10+', labelKey: 'statsGlobalPartners' },
]

export default function Hero() {
  const { t } = useLanguage()

  return (
    <section id="about" className="relative flex items-center justify-center min-h-screen overflow-hidden bg-bg">
      {/* Animated gradient orbs */}
      <div
        className="hero-orb absolute top-[-20%] left-[-10%] w-[600px] h-[600px] rounded-full opacity-30 blur-[120px] pointer-events-none"
        style={{
          background: 'radial-gradient(circle, rgba(37,99,235,0.4) 0%, transparent 70%)',
          animation: 'float 20s ease-in-out infinite',
          willChange: 'transform',
        }}
      />
      <div
        className="hero-orb absolute bottom-[-10%] right-[-10%] w-[500px] h-[500px] rounded-full opacity-20 blur-[120px] pointer-events-none"
        style={{
          background: 'radial-gradient(circle, rgba(139,92,246,0.4) 0%, transparent 70%)',
          animation: 'float 25s ease-in-out infinite reverse',
          willChange: 'transform',
        }}
      />

      {/* Grid pattern */}
      <div
        className="absolute inset-0 opacity-[0.04]"
        style={{
          backgroundImage: `linear-gradient(rgba(37,99,235,0.5) 1px, transparent 1px),
            linear-gradient(90deg, rgba(37,99,235,0.5) 1px, transparent 1px)`,
          backgroundSize: '60px 60px',
        }}
      />

      {/* Radial glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 80% 50% at 50% -10%, rgba(37,99,235,0.15) 0%, transparent 60%)',
        }}
      />

      <motion.div
        variants={container}
        initial="hidden"
        animate="visible"
        className="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center"
      >
        <motion.div variants={fadeInUp}>
          <span className="inline-block text-xs font-semibold uppercase tracking-widest text-accent mb-6 px-4 py-1.5 rounded-full border border-accent/20 bg-accent/5 backdrop-blur-sm">
            {t('heroBadge')}
          </span>
        </motion.div>

        <motion.h1
          variants={fadeInUp}
          className="text-5xl sm:text-6xl lg:text-7xl font-extrabold leading-tight mb-6 font-display"
          style={{
            backgroundImage: 'linear-gradient(135deg, #f1f5f9 0%, #f1f5f9 50%, #2563eb 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}
        >
          {t('aboutTitle')}
        </motion.h1>

        <motion.p
          variants={fadeInUp}
          className="text-lg sm:text-xl text-text-2 mb-10 max-w-2xl mx-auto leading-relaxed"
        >
          {t('aboutSubtitle')}
        </motion.p>

        <motion.div
          variants={fadeInUp}
          className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 sm:gap-4 mb-12"
        >
          {heroStats.map((stat) => (
            <div
              key={stat.labelKey}
              className="group rounded-2xl border border-border bg-surface/80 backdrop-blur-sm px-4 py-5 text-center hover:border-accent/30 hover:bg-accent/5 transition-all duration-300"
            >
              <div
                className="text-2xl sm:text-3xl font-extrabold leading-none font-display"
                style={{
                  backgroundImage: 'linear-gradient(135deg, #f1f5f9 0%, #f1f5f9 30%, #2563eb 100%)',
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  backgroundClip: 'text',
                }}
              >
                {stat.valueKey ? t(stat.valueKey) : stat.value}
              </div>
              <p className="mt-2 text-xs sm:text-sm text-text-2 leading-tight">
                {t(stat.labelKey)}
              </p>
            </div>
          ))}
        </motion.div>

        <motion.div variants={fadeInUp} className="flex justify-center">
          <a
            href="#contact"
            className="inline-flex items-center justify-center gap-2 px-8 py-2.5 text-sm font-semibold rounded-xl bg-accent hover:bg-accent-soft text-white transition-all duration-300 active:scale-[0.98]"
          >
            {t('heroGetInTouch')}
            <ArrowRight size={16} />
          </a>
        </motion.div>
      </motion.div>

      {/* Bottom fade */}
      <div className="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-bg to-transparent pointer-events-none" />
    </section>
  )
}
