'use client'

import { createContext, useContext, useState, useEffect, ReactNode } from 'react'
import { translations, Lang, TranslationKey } from '@/lib/translations'

interface LanguageContextType {
  lang: Lang
  toggle: () => void
  t: (key: TranslationKey) => string
}

const LanguageContext = createContext<LanguageContextType | null>(null)

export function LanguageProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>('en')

  useEffect(() => {
    const saved = localStorage.getItem('lang') as Lang | null
    if (saved && (saved === 'en' || saved === 'tr')) {
      setLang(saved)
    }
  }, [])

  const toggle = () => {
    setLang(prev => {
      const next: Lang = prev === 'en' ? 'tr' : 'en'
      localStorage.setItem('lang', next)
      return next
    })
  }

  const t = (key: TranslationKey): string => {
    return translations[lang][key] as string
  }

  return (
    <LanguageContext.Provider value={{ lang, toggle, t }}>
      {children}
    </LanguageContext.Provider>
  )
}

export function useLanguage() {
  const ctx = useContext(LanguageContext)
  if (!ctx) throw new Error('useLanguage must be used within LanguageProvider')
  return ctx
}
