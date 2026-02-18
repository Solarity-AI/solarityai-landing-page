'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import Image from 'next/image'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.08 } },
}

const partners = [
  { name: 'Ticaret Bakanlığı', src: '/assets/brands/Ticaret_Bakanligi_logo.svg' },
  { name: 'ISIS', src: '/assets/brands/isis.png' },
  { name: 'Novartis', src: '/assets/brands/Novartis-Logo.svg' },
  { name: 'KPM Labs', src: '/assets/brands/kpm-labs.png' },
  { name: 'Everva', src: '/assets/brands/everva.png' },
  { name: 'Siemens', src: '/assets/brands/Siemens_AG_logo.svg' },
  { name: 'Techsign', src: '/assets/brands/techsign.png' },
  { name: 'TÜBİTAK', src: '/assets/brands/TUBITAK_logo.svg' },
  { name: 'Akuakare', src: '/assets/brands/akuakare.png' },
]

export default function Partnerships() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })

  return (
    <section id="partnerships" className="py-24 bg-surface">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          ref={ref}
          variants={stagger}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
        >
          <SectionHeader
            label={t('partnerships')}
            title={t('partnershipsSubtitle')}
            description={t('partnershipsSubtitleDesc')}
          />

          <motion.div
            variants={stagger}
            className="grid grid-cols-3 gap-5 items-center max-w-4xl mx-auto"
          >
            {partners.map(partner => (
              <motion.div
                key={partner.name}
                variants={fadeInUp}
                className="flex items-center justify-center p-6 rounded-xl border border-border bg-bg h-32 group hover:border-accent/20 hover:shadow-lg hover:shadow-black/10 transition-all duration-300"
              >
                <Image
                  src={partner.src}
                  alt={partner.name}
                  width={160}
                  height={64}
                  className="object-contain max-h-14 opacity-40 group-hover:opacity-100 transition-opacity duration-500"
                />
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}
