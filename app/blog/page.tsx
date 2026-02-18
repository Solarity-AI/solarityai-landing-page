import type { Metadata } from 'next'
import Link from 'next/link'

export const metadata: Metadata = {
  title: 'Blog — Solarity AI',
  description: 'Insights, updates, and stories from the Solarity AI team.',
}

export default function BlogPage() {
  return (
    <main className="min-h-screen bg-bg text-text-1">
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center">
        <span className="inline-block text-xs font-semibold tracking-widest uppercase text-accent bg-accent/10 px-3 py-1 rounded-full mb-6">
          Coming Soon
        </span>
        <h1 className="text-4xl font-bold font-display mb-4">Solarity AI Blog</h1>
        <p className="text-text-2 text-lg max-w-xl mx-auto">
          We&apos;re working on something great. Insights on AI, software development, and
          technology innovation — coming soon.
        </p>

        <div className="mt-12">
          <Link href="/" className="text-sm text-accent hover:underline">
            ← Back to Home
          </Link>
        </div>
      </div>
    </main>
  )
}
