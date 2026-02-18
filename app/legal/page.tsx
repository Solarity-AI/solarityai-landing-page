import type { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: 'Legal — Solarity AI',
  description: 'Legal information for Solarity AI LLC.',
}

export default function LegalPage() {
  return (
    <main className="min-h-screen bg-bg text-text-1">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <h1 className="text-4xl font-bold font-display mb-4">Legal Information</h1>
        <p className="text-text-2 mb-10 text-sm">Last updated: February 2026</p>

        <div className="prose prose-invert max-w-none space-y-8 text-text-2 leading-relaxed">
          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">Company Information</h2>
            <ul className="space-y-1">
              <li><span className="text-text-1 font-medium">Legal Name:</span> Solarity AI LLC</li>
              <li><span className="text-text-1 font-medium">Jurisdiction:</span> State of Texas, USA</li>
              <li><span className="text-text-1 font-medium">Address:</span> 310 Gran Via, Irving, TX 75039, USA</li>
              <li>
                <span className="text-text-1 font-medium">Email:</span>{' '}
                <a href="mailto:info@solarityai.com" className="text-accent hover:underline">
                  info@solarityai.com
                </a>
              </li>
            </ul>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">Disclaimer</h2>
            <p>
              The information provided on this website is for general informational purposes only.
              While we strive to keep information accurate and up to date, we make no warranties
              of any kind, express or implied, about completeness, accuracy, or suitability.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">Third-Party Links</h2>
            <p>
              Our website may contain links to third-party websites. These links are provided for
              convenience only. We have no control over the content of those sites and accept no
              responsibility for them.
            </p>
          </section>

          <section>
            <h2 className="text-xl font-semibold text-text-1 mb-3">Related Policies</h2>
            <ul className="space-y-2">
              <li>
                <Link href="/privacy" className="text-accent hover:underline">
                  Privacy Policy
                </Link>
              </li>
              <li>
                <Link href="/terms" className="text-accent hover:underline">
                  Terms of Service
                </Link>
              </li>
            </ul>
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
