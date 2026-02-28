'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'
import { useInView } from 'framer-motion'
import { useRef } from 'react'
import Image from 'next/image'
import { Linkedin } from 'lucide-react'
import SectionHeader from '@/components/ui/SectionHeader'
import { useLanguage } from '@/context/LanguageContext'
import { TranslationKey } from '@/lib/translations'

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

const ASSET_VERSION = '20260207'

const stagger: Variants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.08 } },
}

interface TeamMember {
  name: string
  titleKey: TranslationKey
  image: string
  linkedin: string
}

const executives: TeamMember[] = [
  {
    name: 'Ata Turhan',
    titleKey: 'teamCEO',
    image: `/assets/team/AtaTurhan.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/ataturhan/',
  },
  {
    name: 'Umur Inan',
    titleKey: 'teamCTO',
    image: `/assets/team/UmurInan.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/umurinan/',
  },
  {
    name: 'Burak Hamuryen',
    titleKey: 'teamCIO',
    image: `/assets/team/BurakHamuryen.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/burak-hamuryen-07b8b340/',
  },
]

const bdms: TeamMember[] = [
  {
    name: 'Gokberk Serin',
    titleKey: 'teamBDM',
    image: '/assets/team/GokberkSerin.webp',
    linkedin: 'https://www.linkedin.com/in/gokberk-serin/',
  },
  {
    name: 'Ramazan Cinar',
    titleKey: 'teamBDM',
    image: '/assets/team/RamazanCinar.webp',
    linkedin: 'https://www.linkedin.com/in/ramazancinar-/',
  },
  {
    name: 'Ali Yilmaz',
    titleKey: 'teamBDM',
    image: '/assets/team/AliYilmaz.webp',
    linkedin: 'https://www.linkedin.com/in/ali-yilmaz2/',
  },
  {
    name: 'Remzi Mert Tehneldere',
    titleKey: 'teamBDM',
    image: `/assets/team/RemziMertTehneldere.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/remzi-mert-tehneldere-601505286/',
  },
  {
    name: 'Batuhan Kestek',
    titleKey: 'teamBDM',
    image: `/assets/team/BatuhanKestek.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/batuhankestek/',
  },
]

const engineers: TeamMember[] = [
  {
    name: 'Hasan Erdem Ak',
    titleKey: 'teamLeadFullStack',
    image: `/assets/team/HasanErdemAk.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/hasan-erdem-ak',
  },
  {
    name: 'Emrecan Ozkan',
    titleKey: 'teamLeadFullStack',
    image: '/assets/team/Emrecan.webp',
    linkedin: 'https://www.linkedin.com/in/emrecan-ozkan',
  },
  {
    name: 'Cenk Eren Ozbek',
    titleKey: 'teamEngineer',
    image: '/assets/team/Cenk.webp',
    linkedin: 'https://www.linkedin.com/in/cenkerenozbek/',
  },
  {
    name: 'Eren Can Donertas',
    titleKey: 'teamEngineer',
    image: `/assets/team/ErenCanDonertas.webp?v=${ASSET_VERSION}`,
    linkedin: 'https://www.linkedin.com/in/eren-can-donertas/',
  },
]

const marketers: TeamMember[] = [
  {
    name: 'Lara Sen',
    titleKey: 'teamMarketer',
    image: '/assets/team/LaraSen.webp',
    linkedin: 'https://www.linkedin.com/in/lara-%C5%9Fen-409b61353',
  },
  {
    name: 'Hilal Genc',
    titleKey: 'teamMarketer',
    image: '/assets/team/HilalGenc.webp',
    linkedin: 'https://www.linkedin.com/in/hilal--genc/',
  },
]

function MemberCard({ member }: { member: TeamMember }) {
  const { t } = useLanguage()
  return (
    <motion.div variants={fadeInUp} className="group w-[155px] sm:w-[185px] flex-shrink-0">
      <div className="relative rounded-2xl overflow-hidden border border-white/8 bg-surface-2 transition-all duration-300 hover:border-accent/35 hover:shadow-[0_8px_32px_rgba(0,0,0,0.35)] hover:-translate-y-2">
        <div className="relative w-full h-[205px] sm:h-[245px] overflow-hidden">
          <Image
            src={member.image}
            alt={member.name}
            fill
            loading="lazy"
            className="object-cover object-[50%_12%] transition-transform duration-500 group-hover:scale-[1.05]"
            sizes="(max-width: 640px) 155px, 185px"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent" />
          <div className="absolute inset-x-0 bottom-0 px-3.5 pb-3">
            <h4 className="text-[13px] font-semibold text-white font-display leading-snug line-clamp-1">
              {member.name}
            </h4>
          </div>
        </div>
        <div className="flex items-center justify-between gap-2 px-3.5 py-2.5 border-t border-white/6">
          <p className="text-[11px] text-accent font-medium leading-snug">{t(member.titleKey)}</p>
          <a
            href={member.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className="shrink-0 flex items-center justify-center w-7 h-7 rounded-full bg-surface border border-white/10 text-text-3 hover:bg-[#0A66C2] hover:border-[#0A66C2] hover:text-white transition-all duration-200"
            aria-label={`${member.name} LinkedIn`}
          >
            <Linkedin size={13} />
          </a>
        </div>
      </div>
    </motion.div>
  )
}

interface TeamGroupProps {
  label: string
  members: TeamMember[]
}

function TeamGroup({ label, members }: TeamGroupProps) {
  return (
    <div className="mb-14">
      <motion.span
        variants={fadeInUp}
        className="inline-block text-xs font-semibold uppercase tracking-widest text-accent mb-6 px-3 py-1 rounded-full border border-accent/20 bg-accent/5"
      >
        {label}
      </motion.span>
      <motion.div variants={stagger} className="flex flex-wrap justify-center gap-4 sm:gap-5">
        {members.map(member => (
          <MemberCard key={member.name} member={member} />
        ))}
      </motion.div>
    </div>
  )
}

export default function Team() {
  const { t } = useLanguage()
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true, margin: '-80px' })

  return (
    <section id="team" className="py-24 bg-surface">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          ref={ref}
          variants={stagger}
          initial="hidden"
          animate={isInView ? 'visible' : 'hidden'}
        >
          <SectionHeader
            label={t('team')}
            title={t('teamSubtitle')}
            description={t('teamSubtitleDesc')}
          />

          <TeamGroup label={t('teamExecutives')} members={executives} />
          <TeamGroup label={t('teamManagers')} members={bdms} />
          <TeamGroup label={t('teamEngineers')} members={engineers} />
          <TeamGroup label={t('teamMarketers')} members={marketers} />
        </motion.div>
      </div>
    </section>
  )
}
