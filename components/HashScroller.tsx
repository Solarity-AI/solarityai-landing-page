'use client'

import { useEffect } from 'react'

export default function HashScroller() {
  useEffect(() => {
    const hash = window.location.hash
    if (!hash) return

    let attempts = 0
    const maxAttempts = 30

    const tryScroll = () => {
      const el = document.querySelector(hash)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' })
      } else if (attempts < maxAttempts) {
        attempts++
        setTimeout(tryScroll, 100)
      }
    }

    // İlk denemeden önce kısa bir bekleme — layout'un oturması için
    setTimeout(tryScroll, 50)
  }, [])

  return null
}
