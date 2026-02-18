'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import { MessageCircleHeart, GraduationCap } from 'lucide-react'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'
import { TranslationKey } from '@/lib/translations'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.12 } },
}

interface Product {
  icon: React.ElementType
  nameKey: TranslationKey
  descKey: TranslationKey
  gradient: string
  iconColor: string
}

const products: Product[] = [
  {
    icon: MessageCircleHeart,
    nameKey: 'productChatTherapy',
    descKey: 'productChatTherapyDesc',
    gradient: 'from-rose-500/50 via-accent/30 to-transparent',
    iconColor: 'text-rose-400',
  },
  {
    icon: GraduationCap,
    nameKey: 'productOnlyCampus',
    descKey: 'productOnlyCampusDesc',
    gradient: 'from-emerald-500/50 via-accent/30 to-transparent',
    iconColor: 'text-emerald-400',
  },
]

export default function Products() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })

  return (
    <section id="products" className="py-24 bg-surface">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          ref={ref}
          variants={stagger}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
        >
          <SectionHeader
            label={t('products')}
            title={t('productsTitle')}
          />

          <motion.div variants={stagger} className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {products.map(({ icon: Icon, nameKey, descKey, gradient, iconColor }) => (
              <motion.div
                key={nameKey}
                variants={fadeInUp}
                whileHover={{ y: -4 }}
                transition={{ duration: 0.2 }}
                className="group relative p-8 rounded-2xl border border-border bg-bg hover:border-accent/30 transition-all duration-300 overflow-hidden shadow-lg shadow-black/10 hover:shadow-xl hover:shadow-black/20"
              >
                <div className={`absolute top-0 left-0 right-0 h-0.5 bg-gradient-to-r ${gradient}`} />

                <div className="w-14 h-14 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 group-hover:bg-white/10 transition-colors duration-300">
                  <Icon size={26} className={iconColor} />
                </div>

                <h3 className="text-xl font-bold text-text-1 mb-3 font-display">
                  {t(nameKey)}
                </h3>
                <p className="text-base text-text-2 leading-relaxed">{t(descKey)}</p>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </div>
    </section>
  )
}
