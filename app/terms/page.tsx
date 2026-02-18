import type { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: 'Terms of Service — Solarity AI',
  description: 'Terms of Service for Solarity AI LLC.',
}

export default function TermsPage() {
  return (
    <main className="min-h-screen bg-bg text-text-1">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <h1 className="text-4xl font-bold font-display mb-4">Terms of Service</h1>
        <p className="text-text-2 mb-10 text-sm">Last updated: February 2026</p>

        <div className="prose prose-invert max-w-none space-y-8 text-text-2 leading-relaxed">
          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">1. Acceptance of Terms</h2>
            <p>
              By accessing or using the Solarity AI website and services, you agree to be bound
              by these Terms of Service. If you do not agree, please do not use our services.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">2. Services</h2>
            <p>
              Solarity AI LLC provides AI-powered software development, consulting, and related
              technology services. We reserve the right to modify or discontinue any service at
              any time with reasonable notice.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">3. Intellectual Property</h2>
            <p>
              All content on this website, including text, graphics, logos, and software, is the
              property of Solarity AI LLC and is protected by applicable intellectual property laws.
              You may not reproduce or distribute any content without prior written permission.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">4. Limitation of Liability</h2>
            <p>
              Solarity AI LLC shall not be liable for any indirect, incidental, or consequential
              damages arising from your use of this website or our services. Our total liability
              shall not exceed the amount paid by you for the specific service in question.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">5. Governing Law</h2>
            <p>
              These Terms shall be governed by the laws of the State of Texas, USA, without regard
              to its conflict of law provisions.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">6. Contact</h2>
            <p>
              For questions about these Terms, contact us at{' '}
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
