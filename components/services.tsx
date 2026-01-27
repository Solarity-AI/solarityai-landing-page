"use client";

import { motion } from "framer-motion";
import { Brain, Server, Cloud, Globe, Smartphone, BarChart3 } from "lucide-react";
import { useLanguage } from "@/lib/language-context";

const icons = [Brain, Server, Cloud, Globe, Smartphone, BarChart3];
const colors = [
  { color: "text-primary", bgColor: "bg-primary/10" },
  { color: "text-accent", bgColor: "bg-accent/10" },
  { color: "text-primary", bgColor: "bg-primary/10" },
  { color: "text-accent", bgColor: "bg-accent/10" },
  { color: "text-primary", bgColor: "bg-primary/10" },
  { color: "text-accent", bgColor: "bg-accent/10" },
];

export function Services() {
  const { t } = useLanguage();

  return (
    <section id="services" className="py-32 sm:py-40 relative">
      {/* Background accent */}
      <div className="absolute top-1/2 left-0 w-[400px] h-[400px] bg-primary/10 rounded-full blur-[150px] -translate-y-1/2 -translate-x-1/2" />

      <div className="mx-auto max-w-7xl px-6 lg:px-8 relative">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="max-w-2xl"
        >
          <p className="text-sm font-semibold text-primary uppercase tracking-wider mb-4">{t.services.label}</p>
          <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-foreground leading-[1.1]">
            {t.services.title} <span className="text-primary">{t.services.titleHighlight}</span>
          </h2>
          <p className="mt-6 text-lg text-foreground/70 leading-relaxed">
            {t.services.subtitle}
          </p>
        </motion.div>

        <div className="mt-20 grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {t.services.items.map((service, index) => {
            const Icon = icons[index];
            const colorStyle = colors[index];
            return (
              <motion.div
                key={service.title}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="relative p-8 rounded-2xl bg-card border border-border"
              >
                <div className="mb-6">
                  <div className={`w-14 h-14 rounded-xl ${colorStyle.bgColor} flex items-center justify-center`}>
                    <Icon className={`w-7 h-7 ${colorStyle.color}`} />
                  </div>
                </div>

                <h3 className="text-xl font-semibold text-foreground mb-3">{service.title}</h3>
                <p className="text-foreground/60 leading-relaxed mb-6">{service.description}</p>

                <ul className="space-y-2">
                  {service.features.map((feature) => (
                    <li key={feature} className="flex items-center gap-2 text-sm text-foreground/60">
                      <div className={`w-1.5 h-1.5 rounded-full ${colorStyle.color.replace('text-', 'bg-')}`} />
                      {feature}
                    </li>
                  ))}
                </ul>
              </motion.div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
