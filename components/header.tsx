"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Menu, X, Globe } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useLanguage } from "@/lib/language-context";

export function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const { language, setLanguage, t } = useLanguage();

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const navLinks = [
    { href: "/#services", label: t.nav.services },
    { href: "/#projects", label: t.nav.work },
    { href: "/#partners", label: t.nav.partners },
    { href: "/#team", label: t.nav.team },
    { href: "/#contact", label: t.nav.contact },
  ];

  return (
    <header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
        scrolled
          ? "bg-background/90 backdrop-blur-xl border-b border-border/50"
          : ""
      }`}
    >
      <nav className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="flex h-20 items-center justify-between">
          <Link href="/" className="flex items-center gap-3">
            <Image
              src="/logo.png"
              alt="Solarity"
              width={48}
              height={48}
              className="w-12 h-12 object-contain"
            />
            <div className="hidden sm:block">
              <span className="text-xl font-bold text-primary tracking-tight">
                SOLARITY
              </span>
              <p className="text-[10px] text-accent tracking-[0.2em] -mt-0.5">
                ALWAYS BETTER
              </p>
            </div>
          </Link>

          <div className="hidden lg:flex lg:items-center lg:gap-1">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className="px-4 py-2 text-sm text-foreground/70 hover:text-primary transition-colors rounded-full hover:bg-primary/10"
              >
                {link.label}
              </Link>
            ))}
          </div>

          <div className="hidden lg:flex lg:items-center lg:gap-3">
            {/* Language Switcher */}
            <button
              type="button"
              onClick={() => setLanguage(language === "en" ? "tr" : "en")}
              className="flex items-center gap-2 px-3 py-2 rounded-full text-sm text-foreground/70 hover:text-primary hover:bg-primary/10 transition-colors"
            >
              <Globe className="w-4 h-4" />
              <span className="font-medium">
                {language === "en" ? "TR" : "EN"}
              </span>
            </button>
            <Button
              asChild
              size="sm"
              className="rounded-full px-6 bg-primary text-primary-foreground hover:bg-primary/90 font-semibold"
            >
              <Link href="/#contact">{t.nav.getStarted}</Link>
            </Button>
          </div>

          <div className="flex items-center gap-2 lg:hidden">
            {/* Mobile Language Switcher */}
            <button
              type="button"
              onClick={() => setLanguage(language === "en" ? "tr" : "en")}
              className="flex items-center gap-1.5 px-3 py-2 rounded-full text-sm text-foreground/70 hover:text-primary"
            >
              <Globe className="w-4 h-4" />
              <span className="font-medium">
                {language === "en" ? "TR" : "EN"}
              </span>
            </button>
            <button
              type="button"
              className="p-2 -mr-2 text-foreground/70 hover:text-primary"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? (
                <X className="h-6 w-6" />
              ) : (
                <Menu className="h-6 w-6" />
              )}
            </button>
          </div>
        </div>
      </nav>

      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="lg:hidden absolute inset-x-0 top-20 bg-background/95 backdrop-blur-xl border-b border-border"
          >
            <div className="px-6 py-6 space-y-1">
              {navLinks.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className="block py-3 text-lg text-foreground/70 hover:text-primary transition-colors"
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {link.label}
                </Link>
              ))}
              <div className="pt-6">
                <Button
                  asChild
                  className="w-full rounded-full bg-primary text-primary-foreground"
                  onClick={() => setMobileMenuOpen(false)}
                >
                  <Link href="/#contact">{t.nav.getStarted}</Link>
                </Button>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
