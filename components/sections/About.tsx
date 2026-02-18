'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import { Brain, Smartphone, Globe, Building2, Cloud, Lightbulb } from 'lucide-react'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'
import { TranslationKey } from '@/lib/translations'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.08 } },
}

type ServiceColor = 'violet' | 'emerald' | 'cyan' | 'orange' | 'rose' | 'amber'

interface Service {
  icon: React.ElementType
  titleKey: TranslationKey
  descKey: TranslationKey
  tags: TranslationKey[]
  color: ServiceColor
}

const colorStyles: Record<ServiceColor, { icon: string; iconBg: string; hover: string; tag: string }> = {
  violet: {
    icon: 'text-violet-400',
    iconBg: 'bg-violet-500/10 border-violet-500/20 group-hover:bg-violet-500/20',
    hover: 'hover:border-violet-500/30 hover:bg-violet-500/5',
    tag: 'bg-violet-500/10 border-violet-500/20 text-violet-400',
  },
  emerald: {
    icon: 'text-emerald-400',
    iconBg: 'bg-emerald-500/10 border-emerald-500/20 group-hover:bg-emerald-500/20',
    hover: 'hover:border-emerald-500/30 hover:bg-emerald-500/5',
    tag: 'bg-emerald-500/10 border-emerald-500/20 text-emerald-400',
  },
  cyan: {
    icon: 'text-cyan-400',
    iconBg: 'bg-cyan-500/10 border-cyan-500/20 group-hover:bg-cyan-500/20',
    hover: 'hover:border-cyan-500/30 hover:bg-cyan-500/5',
    tag: 'bg-cyan-500/10 border-cyan-500/20 text-cyan-400',
  },
  orange: {
    icon: 'text-orange-400',
    iconBg: 'bg-orange-500/10 border-orange-500/20 group-hover:bg-orange-500/20',
    hover: 'hover:border-orange-500/30 hover:bg-orange-500/5',
    tag: 'bg-orange-500/10 border-orange-500/20 text-orange-400',
  },
  rose: {
    icon: 'text-rose-400',
    iconBg: 'bg-rose-500/10 border-rose-500/20 group-hover:bg-rose-500/20',
    hover: 'hover:border-rose-500/30 hover:bg-rose-500/5',
    tag: 'bg-rose-500/10 border-rose-500/20 text-rose-400',
  },
  amber: {
    icon: 'text-amber-400',
    iconBg: 'bg-amber-500/10 border-amber-500/20 group-hover:bg-amber-500/20',
    hover: 'hover:border-amber-500/30 hover:bg-amber-500/5',
    tag: 'bg-amber-500/10 border-amber-500/20 text-amber-400',
  },
}

const services: Service[] = [
  {
    icon: Brain,
    titleKey: 'serviceAI',
    descKey: 'serviceAIDesc',
    tags: ['tagGenAI', 'tagLLM', 'tagRAG', 'tagComputerVision', 'tagMultimodalAI'],
    color: 'violet',
  },
  {
    icon: Building2,
    titleKey: 'serviceEnterprise',
    descKey: 'serviceEnterpriseDesc',
    tags: ['tagERP', 'tagCRM', 'tagCustomApps', 'tagIntegration', 'tagWorkflow'],
    color: 'emerald',
  },
  {
    icon: Cloud,
    titleKey: 'serviceCloud',
    descKey: 'serviceCloudDesc',
    tags: ['tagAWS', 'tagAzure', 'tagGCP', 'tagServerless', 'tagKubernetes'],
    color: 'cyan',
  },
  {
    icon: Globe,
    titleKey: 'serviceWeb',
    descKey: 'serviceWebDesc',
    tags: ['tagReact', 'tagVue', 'tagNextJS', 'tagTypeScript', 'tagResponsive'],
    color: 'orange',
  },
  {
    icon: Smartphone,
    titleKey: 'serviceMobile',
    descKey: 'serviceMobileDesc',
    tags: ['tagReactNative', 'tagFlutter', 'tagiOS', 'tagAndroid', 'tagKotlin'],
    color: 'rose',
  },
  {
    icon: Lightbulb,
    titleKey: 'serviceConsulting',
    descKey: 'serviceConsultingDesc',
    tags: ['tagStrategy', 'tagDigitalTransform', 'tagProcessOpt', 'tagAdvisory', 'tagChangeMgmt'],
    color: 'amber',
  },
]

export default function About() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })

  return (
    <section id="services" className="py-24 bg-bg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          ref={ref}
          variants={stagger}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
        >
          <SectionHeader
            label={t('about')}
            title={t('servicesTitle')}
            description={t('aboutSubtitle')}
          />

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {services.map(({ icon: Icon, titleKey, descKey, tags, color }) => {
              const styles = colorStyles[color]
              return (
                <motion.div
                  key={titleKey}
                  variants={fadeInUp}
                  whileHover={{ y: -4 }}
                  transition={{ duration: 0.2 }}
                  className={`group flex flex-col p-6 rounded-2xl border border-border bg-surface ${styles.hover} transition-all duration-300 shadow-lg shadow-black/10 hover:shadow-xl hover:shadow-black/20`}
                >
                  <div className={`w-12 h-12 rounded-xl border flex items-center justify-center mb-4 ${styles.iconBg} transition-colors duration-300 shrink-0`}>
                    <Icon size={22} className={styles.icon} />
                  </div>
                  <h3 className="text-base font-semibold text-text-1 mb-2 font-display">
                    {t(titleKey)}
                  </h3>
                  <p className="text-base text-text-2 leading-relaxed mb-4 flex-1">{t(descKey)}</p>
                  <div className="flex flex-wrap gap-1.5">
                    {tags.map(tag => (
                      <span
                        key={tag}
                        className={`text-xs font-medium px-2.5 py-1 rounded-lg border ${styles.tag}`}
                      >
                        {t(tag)}
                      </span>
                    ))}
                  </div>
                </motion.div>
              )
            })}
          </div>
        </motion.div>
      </div>
    </section>
  )
}
