'use client'

import { useEffect } from 'react'

export default function HashScroller() {
  useEffect(() => {
    const hash = window.location.hash
    if (!hash) return

    const scrollToHash = () => {
      const el = document.querySelector(hash)
      if (el) {
        // instant: smooth scroll layout shift'ten etkileniyor
        el.scrollIntoView({ behavior: 'instant' as ScrollBehavior })
      }
    }

    // Tüm görseller yüklenince scroll et — önce scroll edince
    // yüklenmemiş görseller layout shift yapıp section'ı kaydırıyor
    if (document.readyState === 'complete') {
      // Başka sayfadan gelince zaten yüklü, bir sonraki frame'de scroll et
      requestAnimationFrame(() => requestAnimationFrame(scrollToHash))
    } else {
      window.addEventListener('load', () => {
        requestAnimationFrame(() => requestAnimationFrame(scrollToHash))
      }, { once: true })
    }
  }, [])

  return null
}
