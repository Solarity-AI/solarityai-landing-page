import type { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: 'Privacy Policy — Solarity AI',
  description: 'Privacy Policy for Solarity AI LLC.',
}

export default function PrivacyPage() {
  return (
    <main className="min-h-screen bg-bg text-text-1">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <h1 className="text-4xl font-bold font-display mb-4">Privacy Policy</h1>
        <p className="text-text-2 mb-10 text-sm">Last updated: February 2026</p>

        <div className="prose prose-invert max-w-none space-y-8 text-text-2 leading-relaxed">
          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">1. Introduction</h2>
            <p>
              Solarity AI LLC (&quot;Solarity AI&quot;, &quot;we&quot;, &quot;us&quot;, or &quot;our&quot;) is committed to protecting
              your personal information. This Privacy Policy explains how we collect, use, and
              safeguard information when you visit our website or use our services.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">2. Information We Collect</h2>
            <p>We may collect the following types of information:</p>
            <ul className="list-disc list-inside mt-2 space-y-1">
              <li>Contact details (name, email, company) submitted via our contact or careers forms</li>
              <li>Usage data collected via Google Analytics (anonymized)</li>
              <li>Technical data such as browser type and IP address</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">3. How We Use Your Information</h2>
            <p>We use collected information to:</p>
            <ul className="list-disc list-inside mt-2 space-y-1">
              <li>Respond to your inquiries and service requests</li>
              <li>Process job applications</li>
              <li>Improve our website and user experience</li>
              <li>Comply with legal obligations</li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">4. Data Sharing</h2>
            <p>
              We do not sell or rent your personal data. We may share information with trusted
              third-party service providers (e.g., form submission services, analytics) solely to
              operate our website and services.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">5. Cookies</h2>
            <p>
              Our website uses cookies for analytics purposes via Google Analytics. You can disable
              cookies in your browser settings at any time.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">6. Contact</h2>
            <p>
              For privacy-related questions, please contact us at{' '}
              <a href="mailto:info@solarityai.com" className="text-accent hover:underline">
                info@solarityai.com
              </a>
              .
            </p>
          </section>
        </div>

        <div className="mt-12 pt-8 border-t border-border">
          <Link href="/" className="text-sm text-accent hover:underline">
            ← Back to Home
          </Link>
        </div>
      </div>
    </main>
  )
}
