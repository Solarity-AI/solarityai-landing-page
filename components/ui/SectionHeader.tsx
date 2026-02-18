'use client'

import { motion } from 'framer-motion'
import type { Variants } from 'framer-motion'

interface SectionHeaderProps {
  label: string
  title: string
  description?: string
  center?: boolean
}

const fadeInUp: Variants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
}

export default function SectionHeader({
  label,
  title,
  description,
  center = true,
}: SectionHeaderProps) {
  return (
    <div className={`mb-14 ${center ? 'text-center' : ''}`}>
      <motion.span
        variants={fadeInUp}
        className="inline-block text-xs font-semibold uppercase tracking-widest text-accent mb-4 px-3.5 py-1 rounded-full border border-accent/20 bg-accent/5"
      >
        {label}
      </motion.span>
      <motion.h2
        variants={fadeInUp}
        className="text-3xl sm:text-4xl font-bold text-text-1 mb-4 leading-tight font-display"
      >
        {title}
      </motion.h2>
      {description && (
        <motion.p
          variants={fadeInUp}
          className={`text-text-2 text-base sm:text-lg leading-relaxed ${center ? 'max-w-2xl mx-auto' : 'max-w-2xl'}`}
        >
          {description}
        </motion.p>
      )}
    </div>
  )
}
