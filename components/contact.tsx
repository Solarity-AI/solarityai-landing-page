"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { ArrowRight, Mail, MapPin, Clock, Zap } from "lucide-react";
import { useLanguage } from "@/lib/language-context";

export function Contact() {
  const { t } = useLanguage();

  return (
    <section id="contact" className="py-32 sm:py-40 relative overflow-hidden">
      {/* Background accents */}
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-primary/10 rounded-full blur-[150px]" />
      <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-accent/10 rounded-full blur-[150px]" />

      <div className="mx-auto max-w-7xl px-6 lg:px-8 relative">
        <div className="grid lg:grid-cols-2 gap-16 lg:gap-24">
          {/* Left Column */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <p className="text-sm font-semibold text-primary uppercase tracking-wider mb-4">
              {t.contact.label}
            </p>
            <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-foreground leading-[1.1]">
              {t.contact.title}{" "}
              <span className="text-primary">{t.contact.titleHighlight}</span>
            </h2>
            <p className="mt-6 text-lg text-foreground/60 leading-relaxed">
              {t.contact.subtitle}
            </p>

            <div className="mt-12 space-y-6">
              <div className="flex items-start gap-4 p-4 rounded-xl bg-card/50 border border-border/50 hover:border-primary/30 transition-colors">
                <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center shrink-0">
                  <Mail className="w-5 h-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-foreground/50 mb-1">
                    {t.contact.email}
                  </p>
                  <a
                    href="mailto:hello@solarity.ai"
                    className="text-lg font-semibold text-foreground hover:text-primary transition-colors"
                  >
                    hello@solarity.ai
                  </a>
                </div>
              </div>

              <div className="flex items-start gap-4 p-4 rounded-xl bg-card/50 border border-border/50 hover:border-accent/30 transition-colors">
                <div className="w-12 h-12 rounded-xl bg-accent/10 flex items-center justify-center shrink-0">
                  <MapPin className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-foreground/50 mb-1">
                    {t.contact.location}
                  </p>
                  <p className="text-lg font-semibold text-foreground">
                    Dallas, Texas, USA
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-4 p-4 rounded-xl bg-card/50 border border-border/50 hover:border-primary/30 transition-colors">
                <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center shrink-0">
                  <Clock className="w-5 h-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-foreground/50 mb-1">
                    {t.contact.responseTime}
                  </p>
                  <p className="text-lg font-semibold text-foreground">
                    {t.contact.responseValue}
                  </p>
                </div>
              </div>
            </div>

            {/* Social Links */}
            <div className="mt-12 pt-8 border-t border-border/50">
              <p className="text-sm text-foreground/50 mb-4">
                {t.contact.followUs}
              </p>
              <div className="flex gap-3">
                {["LinkedIn", "Twitter", "GitHub"].map((social, i) => (
                  <a
                    key={social}
                    href="#"
                    className={`px-5 py-2.5 rounded-full text-sm font-medium transition-colors ${
                      i === 0
                        ? "bg-primary/10 text-primary hover:bg-primary/20"
                        : i === 1
                          ? "bg-accent/10 text-accent hover:bg-accent/20"
                          : "bg-primary/10 text-primary hover:bg-primary/20"
                    }`}
                  >
                    {social}
                  </a>
                ))}
              </div>
            </div>
          </motion.div>

          {/* Right Column - Form */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="bg-card rounded-3xl p-8 lg:p-10 border border-border/50 h-fit"
          >
            <div className="flex items-center gap-3 mb-6">
              <div className="w-10 h-10 rounded-xl bg-primary/10 flex items-center justify-center">
                <Zap className="w-5 h-5 text-primary" />
              </div>
              <div>
                <h3 className="text-xl font-semibold text-foreground">
                  {t.contact.form.title}
                </h3>
                <p className="text-sm text-foreground/50">
                  {t.contact.form.subtitle}
                </p>
              </div>
            </div>

            <form className="space-y-5">
              <div className="grid sm:grid-cols-2 gap-5">
                <div>
                  <label
                    htmlFor="name"
                    className="block text-sm font-medium text-foreground mb-2"
                  >
                    {t.contact.form.name}
                  </label>
                  <Input
                    id="name"
                    placeholder={t.contact.form.namePlaceholder}
                    className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                  />
                </div>
                <div>
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium text-foreground mb-2"
                  >
                    {t.contact.form.email}
                  </label>
                  <Input
                    id="email"
                    type="email"
                    placeholder={t.contact.form.emailPlaceholder}
                    className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="company"
                  className="block text-sm font-medium text-foreground mb-2"
                >
                  {t.contact.form.company}
                </label>
                <Input
                  id="company"
                  placeholder={t.contact.form.companyPlaceholder}
                  className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                />
              </div>

              <div>
                <label
                  htmlFor="budget"
                  className="block text-sm font-medium text-foreground mb-2"
                >
                  {t.contact.form.budget}
                </label>
                <select
                  id="budget"
                  className="w-full h-12 px-4 rounded-lg bg-secondary/50 border border-border/50 text-foreground focus:ring-1 focus:ring-primary/50 focus:border-primary/50"
                >
                  <option value="">{t.contact.form.budgetPlaceholder}</option>
                  <option value="50k-100k">$50,000 - $100,000</option>
                  <option value="100k-250k">$100,000 - $250,000</option>
                  <option value="250k-500k">$250,000 - $500,000</option>
                  <option value="500k+">$500,000+</option>
                </select>
              </div>

              <div>
                <label
                  htmlFor="message"
                  className="block text-sm font-medium text-foreground mb-2"
                >
                  {t.contact.form.message}
                </label>
                <Textarea
                  id="message"
                  placeholder={t.contact.form.messagePlaceholder}
                  rows={4}
                  className="bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50 resize-none"
                />
              </div>

              <Button
                type="submit"
                size="lg"
                className="w-full rounded-full h-14 bg-primary text-primary-foreground hover:bg-primary/90 font-semibold shadow-lg shadow-primary/25"
              >
                {t.contact.form.submit}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>

              <p className="text-xs text-foreground/40 text-center">
                {t.contact.form.privacy}{" "}
                <Link href="/privacy" className="text-primary hover:underline">
                  {t.contact.form.privacyLink}
                </Link>
                .
              </p>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}
