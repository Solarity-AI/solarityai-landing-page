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
  { name: 'Ticaret Bakanlığı', src: '/assets/brands/Ticaret_Bakanligi_logo.svg', href: 'https://www.ticaret.gov.tr/' },
  { name: 'ISIS', src: '/assets/brands/isis.png', href: 'https://www.isisdanismanlik.com/' },
  { name: 'Novartis', src: '/assets/brands/Novartis-Logo.svg', href: 'https://www.novartis.com/' },
  { name: 'KPM Labs', src: '/assets/brands/kpm-labs.png', href: 'https://www.kpmlabs.com.tr/' },
  { name: 'Everva', src: '/assets/brands/everva.png', href: 'https://everva.com.tr/' },
  { name: 'Siemens', src: '/assets/brands/Siemens_AG_logo.svg', href: 'https://www.siemens.com/' },
  { name: 'Techsign', src: '/assets/brands/techsign.png', href: 'https://www.techsign.com.tr/' },
  { name: 'TÜBİTAK', src: '/assets/brands/TUBITAK_logo.svg', href: 'https://www.tubitak.gov.tr/' },
  { name: 'Akuakare', src: '/assets/brands/akuakare.webp', whiteSrc: '/assets/brands/akuakare-white.webp', href: 'https://akuakare.com/' },
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
                className="group flex items-center justify-center p-6 rounded-xl border border-border bg-bg h-32 hover:border-accent/20 hover:shadow-lg hover:shadow-black/10 focus-within:border-accent/40 focus-within:shadow-lg focus-within:shadow-black/10 transition-all duration-300"
              >
                <a
                  href={partner.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex h-full w-full items-center justify-center focus-visible:outline-none"
                  aria-label={`${partner.name} website`}
                >
                  {partner.whiteSrc ? (
                    <div className="relative h-14 w-full max-w-[160px]">
                      <Image
                        src={partner.whiteSrc}
                        alt=""
                        aria-hidden="true"
                        width={160}
                        height={64}
                        className="partner-logo-white absolute inset-0 m-auto object-contain max-h-14 h-full w-full"
                      />
                      <Image
                        src={partner.src}
                        alt={partner.name}
                        width={160}
                        height={64}
                        className="partner-logo-color absolute inset-0 m-auto object-contain max-h-14 h-full w-full"
                      />
                    </div>
                  ) : (
                    <Image
                      src={partner.src}
                      alt={partner.name}
                      width={160}
                      height={64}
                      className="partner-logo object-contain max-h-14"
                    />
                  )}
                </a>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}
