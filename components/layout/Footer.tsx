'use client'

import Link from 'next/link'
import Image from 'next/image'
import {
  BookText,
  Facebook,
  Github,
  Instagram,
  Link2,
  Linkedin,
  MessageCircle,
  Music2,
  Pin,
  Send,
  Twitter,
  Youtube,
  type LucideIcon,
} from 'lucide-react'
import { useLanguage } from '@/context/LanguageContext'

const ASSET_VERSION = '20260207'
type SocialLink = { label: string; href: string; icon: LucideIcon }
const SOCIAL_LINKS = [
  { label: 'Linktree', href: 'https://linktr.ee/solarity_ai', icon: Link2 },
  { label: 'Instagram', href: 'https://www.instagram.com/solarity_ai', icon: Instagram },
  { label: 'Facebook', href: 'https://www.facebook.com/solarity.ai.company', icon: Facebook },
  { label: 'TikTok', href: 'https://www.tiktok.com/@solarityai', icon: Music2 },
  { label: 'YouTube', href: 'https://www.youtube.com/@solarity_ai', icon: Youtube },
  { label: 'X', href: 'https://x.com/solarity_ai', icon: Twitter },
  { label: 'LinkedIn', href: 'https://www.linkedin.com/company/solarity-ai-company/posts/?feedView=all', icon: Linkedin },
  { label: 'GitHub', href: 'https://github.com/Solarity-AI', icon: Github },
  { label: 'WhatsApp', href: 'https://www.whatsapp.com/channel/0029Vb6z14n42DcffGUs9x3R', icon: MessageCircle },
  { label: 'Telegram', href: 'https://t.me/solarity_ai', icon: Send },
  { label: 'Medium', href: 'https://medium.com/solarity-ai', icon: BookText },
  { label: 'Pinterest', href: 'https://tr.pinterest.com/solarity_ai/', icon: Pin },
] satisfies SocialLink[]

export default function Footer() {
  const { t } = useLanguage()

  return (
    <footer className="border-t border-border bg-bg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="mx-auto max-w-2xl text-center">
          <div className="space-y-5">
            <Link href="/" className="flex items-center justify-center gap-3">
              <Image
                src={`/assets/logo/logo.webp?v=${ASSET_VERSION}`}
                alt="Solarity AI"
                width={56}
                height={56}
                className="rounded-lg"
              />
              <span className="text-3xl font-bold text-text-1 font-display">
                Solarity AI
              </span>
            </Link>
            <p className="mx-auto max-w-xl text-base text-text-2 leading-relaxed">
              {t('footerDescription')}
            </p>
          </div>
        </div>

        <div className="mt-10">
          <h4 className="text-sm font-semibold text-text-1 uppercase tracking-widest mb-3 font-display text-center">
            {t('footerFollowUs')}
          </h4>
          <div className="flex flex-wrap justify-center gap-2">
            {SOCIAL_LINKS.map(({ label, href, icon: Icon }) => (
              <a
                key={label}
                href={href}
                target="_blank"
                rel="noopener noreferrer"
                aria-label={label}
                title={label}
                className="inline-flex h-9 w-9 items-center justify-center rounded-lg border border-border text-text-2 hover:text-accent hover:border-accent/40 transition-colors"
                onClick={() =>
                  (window as unknown as { gtag?: (...args: unknown[]) => void }).gtag?.(
                    'event',
                    'click',
                    { event_category: 'Social', event_label: `${label} Footer` }
                  )
                }
              >
                <Icon size={14} aria-hidden="true" />
              </a>
            ))}
          </div>
        </div>

        {/* Bottom bar */}
        <div className="mt-12 pt-8 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-text-3">{t('footerCopyright')}</p>
          <nav className="flex flex-wrap justify-center gap-x-5 gap-y-1" aria-label="Legal links">
            {([
              ['footerPrivacy', '/privacy'],
              ['footerTerms', '/terms'],
              ['footerLegal', '/legal'],
              ['footerBlog', '/blog'],
            ] as const).map(([key, href]) => (
              <Link
                key={href}
                href={href}
                className="text-xs text-text-3 hover:text-text-2 transition-colors"
              >
                {t(key)}
              </Link>
            ))}
          </nav>
        </div>
      </div>
    </footer>
  )
}
