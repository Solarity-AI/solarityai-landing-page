"use client";

import { Button } from "@/components/ui/button";
import { ArrowRight, Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import Image from "next/image";
import { useLanguage } from "@/lib/language-context";

export function Hero() {
  const { t } = useLanguage();

  const scrollToContact = () => {
    const contactSection = document.getElementById("contact");
    if (contactSection) {
      contactSection.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  };

  const stats = [
    { value: "$2B+", label: t.hero.stats.revenue },
    { value: "50+", label: t.hero.stats.projects },
    { value: "99.9%", label: t.hero.stats.uptime },
    { value: "15+", label: t.hero.stats.partners },
  ];

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Animated gradient background */}
      <div className="absolute inset-0">
        <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-primary/20 rounded-full blur-[150px] -translate-y-1/2 translate-x-1/2" />
        <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-accent/20 rounded-full blur-[150px] translate-y-1/2 -translate-x-1/2" />
      </div>

      {/* Grid pattern */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(255,200,0,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(255,200,0,0.03)_1px,transparent_1px)] bg-[size:80px_80px]" />

      <div className="relative mx-auto max-w-7xl px-6 lg:px-8 py-32 sm:py-40">
        <div className="text-center max-w-4xl mx-auto">
          {/* Badge */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/30 mb-8"
          >
            <Sparkles className="w-4 h-4 text-primary" />
            <span className="text-sm text-primary font-medium">
              {t.hero.badge}
            </span>
          </motion.div>

          {/* Main headline */}
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-5xl sm:text-6xl lg:text-7xl font-bold tracking-tight leading-[1.1]"
          >
            <span className="text-foreground">{t.hero.title1}</span>
            <br />
            <span className="text-primary">{t.hero.title2}</span>
          </motion.h1>

          {/* Subheadline */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.3 }}
            className="mt-8 text-lg sm:text-xl text-foreground/70 max-w-2xl mx-auto leading-relaxed"
          >
            {t.hero.subtitle}
          </motion.p>

          {/* CTAs */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="mt-10 flex items-center justify-center"
          >
            <Button
              size="lg"
              onClick={scrollToContact}
              className="rounded-full px-8 h-14 text-base bg-primary text-primary-foreground hover:bg-primary/90 font-semibold shadow-lg shadow-primary/25"
            >
              {t.hero.cta}
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
          </motion.div>

          {/* Trust indicators */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="mt-20"
          >
            <p className="text-sm text-foreground/50 mb-6">
              {t.hero.trustedBy}
            </p>
            <div className="flex flex-wrap items-center justify-center gap-x-10 gap-y-6">
              {["IBM", "HPE", "Broadcom", "HashiCorp", "Elastic"].map(
                (company) => (
                  <span
                    key={company}
                    className="text-lg font-semibold text-foreground/40 hover:text-primary/80 transition-colors cursor-default"
                  >
                    {company}
                  </span>
                ),
              )}
            </div>
          </motion.div>
        </div>

        {/* Stats row */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.7 }}
          className="mt-24 grid grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-4 border-t border-primary/20 pt-12"
        >
          {stats.map((stat, i) => (
            <div key={stat.label} className="text-center lg:text-left">
              <div
                className={`text-3xl sm:text-4xl font-bold ${i % 2 === 0 ? "text-primary" : "text-accent"}`}
              >
                {stat.value}
              </div>
              <div className="text-sm text-foreground/60 mt-1">
                {stat.label}
              </div>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
