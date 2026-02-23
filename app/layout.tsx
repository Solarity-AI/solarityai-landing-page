import type { Metadata, Viewport } from 'next'
import { Plus_Jakarta_Sans, Sora } from 'next/font/google'
import Script from 'next/script'
import './globals.css'
import { LanguageProvider } from '@/context/LanguageContext'

const LOGO_ASSET_VERSION = '20260207'

const inter = Plus_Jakarta_Sans({
  variable: '--font-inter',
  subsets: ['latin'],
  weight: ['400', '500', '600', '700', '800'],
  display: 'swap',
})

const poppins = Sora({
  variable: '--font-poppins',
  subsets: ['latin'],
  weight: ['400', '500', '600', '700', '800'],
  display: 'swap',
})

export const viewport: Viewport = {
  themeColor: '#2563eb',
}

export const metadata: Metadata = {
  metadataBase: new URL('https://solarityai.com'),
  title: 'Solarity AI - AI-Native Software Company',
  description:
    'Solarity AI is an AI-Native Software Company creating high-impact B2B and B2C solutions with world-class quality. Specializing in AI/ML, mobile apps, web applications, enterprise software, and cloud-native solutions.',
  keywords:
    'AI software development, artificial intelligence, enterprise AI solutions, B2B software, B2C applications, machine learning, mobile app development, web application development, cloud-native applications',
  authors: [{ name: 'Solarity AI' }],
  robots: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1',
  openGraph: {
    type: 'website',
    url: 'https://solarityai.com',
    title: 'Solarity AI - AI-Native Software Company',
    description:
      'Solarity AI is an AI-Native Software Company creating high-impact B2B and B2C solutions with world-class quality.',
    siteName: 'Solarity AI',
    images: [{ url: `/assets/logo/logo.webp?v=${LOGO_ASSET_VERSION}` }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Solarity AI - AI-Native Software Company',
    description: 'Creating High-Impact B2B and B2C Solutions with World-Class Quality',
    images: [`/assets/logo/logo.webp?v=${LOGO_ASSET_VERSION}`],
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${poppins.variable}`}>
      <head>
        {/* Safari detection — adds 'is-safari' class to <html> for CSS-scoped overrides */}
        <script dangerouslySetInnerHTML={{ __html: `try{if(/^((?!chrome|android).)*safari/i.test(navigator.userAgent))document.documentElement.classList.add('is-safari')}catch(e){}` }} />
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-KPPM46EHP9"
          strategy="afterInteractive"
        />
        <Script id="ga-init" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-KPPM46EHP9');
          `}
        </Script>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              '@context': 'https://schema.org',
              '@type': 'Organization',
              name: 'Solarity AI',
              url: 'https://solarityai.com',
              logo: `https://solarityai.com/assets/logo/logo.webp?v=${LOGO_ASSET_VERSION}`,
              sameAs: ['https://www.linkedin.com/company/solarityai-llc'],
              contactPoint: {
                '@type': 'ContactPoint',
                email: 'info@solarityai.com',
                contactType: 'customer service',
              },
            }),
          }}
        />
      </head>
        <body className="bg-bg text-text-1 antialiased" suppressHydrationWarning>
        <LanguageProvider>{children}</LanguageProvider>
      </body>
    </html>
  )
}
