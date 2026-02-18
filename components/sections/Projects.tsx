'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'
import { TranslationKey } from '@/lib/translations'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.1 } },
}

interface Project {
  companyKey: TranslationKey
  nameKey: TranslationKey
  descKey: TranslationKey
}

const projects: Project[] = [
  {
    companyKey: 'projectMinistryTrade',
    nameKey: 'projectEAuction',
    descKey: 'projectEAuctionDesc',
  },
  {
    companyKey: 'projectMinistryTrade',
    nameKey: 'projectCustomsDeclaration',
    descKey: 'projectCustomsDeclarationDesc',
  },
  {
    companyKey: 'projectISIS',
    nameKey: 'projectISISMicroservices',
    descKey: 'projectISISDesc',
  },
  {
    companyKey: 'projectNovartis',
    nameKey: 'projectNovartisScreensaver',
    descKey: 'projectNovartisDesc',
  },
]

export default function Projects() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })

  return (
    <section id="projects" className="py-24 bg-bg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          ref={ref}
          variants={stagger}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
        >
          <SectionHeader
            label={t('projects')}
            title={t('projectsSubtitle')}
            description={t('projectsSubtitleDesc')}
          />

          <motion.div variants={stagger} className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {projects.map(project => (
              <motion.div
                key={`${project.companyKey}-${project.nameKey}`}
                variants={fadeInUp}
                whileHover={{ y: -4 }}
                transition={{ duration: 0.2 }}
                className="group relative p-6 rounded-2xl border border-border bg-surface hover:border-accent/30 transition-all duration-300 overflow-hidden shadow-lg shadow-black/10 hover:shadow-xl hover:shadow-black/20"
              >
                <div className="absolute left-0 top-6 bottom-6 w-0.5 bg-gradient-to-b from-accent to-accent-2 rounded-full" />

                <div className="pl-4">
                  <span className="text-xs font-semibold uppercase tracking-wider text-text-3 mb-2 block">
                    {t(project.companyKey)}
                  </span>
                  <h3 className="text-lg font-bold text-text-1 mb-3 font-display">
                    {t(project.nameKey)}
                  </h3>
                  <p className="text-base text-text-2 leading-relaxed">{t(project.descKey)}</p>
                </div>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}
