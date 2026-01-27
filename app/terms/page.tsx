import { Header } from "@/components/header";
import { Footer } from "@/components/footer";

export default function TermsPage() {
  return (
    <>
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-[100] focus:px-6 focus:py-3 focus:bg-primary focus:text-primary-foreground focus:rounded-lg focus:font-semibold"
      >
        Skip to main content
      </a>
      <Header />
      <main id="main-content" className="min-h-screen bg-background">
        <div className="mx-auto max-w-4xl px-6 pt-32 pb-16 lg:px-8">
          <div className="prose prose-invert max-w-none">
            <h1
              className="text-4xl font-bold text-foreground mb-6"
              id="terms-title"
            >
              Terms of Service
            </h1>

            <p className="text-lg text-foreground/70 mb-8">
              Last updated: January 26, 2026
            </p>

            <div
              className="space-y-8 text-foreground/80"
              role="article"
              aria-labelledby="terms-title"
            >
              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  1. Acceptance of Terms
                </h2>
                <p className="leading-relaxed">[Content will be added soon]</p>
              </section>

              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  2. Use of Services
                </h2>
                <p className="leading-relaxed">[Content will be added soon]</p>
              </section>

              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  3. Intellectual Property
                </h2>
                <p className="leading-relaxed">[Content will be added soon]</p>
              </section>

              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  4. Limitation of Liability
                </h2>
                <p className="leading-relaxed">[Content will be added soon]</p>
              </section>

              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  5. Modifications to Terms
                </h2>
                <p className="leading-relaxed">[Content will be added soon]</p>
              </section>

              <section>
                <h2 className="text-2xl font-semibold text-foreground mb-4">
                  6. Contact Information
                </h2>
                <p className="leading-relaxed">
                  For questions about these Terms of Service, please contact us
                  at{" "}
                  <a
                    href="mailto:legal@solarityai.com"
                    className="text-primary hover:underline"
                  >
                    legal@solarityai.com
                  </a>
                </p>
              </section>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
}
