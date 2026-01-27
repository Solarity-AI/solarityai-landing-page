"use client";

import { motion } from "framer-motion";
import { useLanguage } from "@/lib/language-context";

const accentColors = ["text-primary", "text-accent", "text-primary", "text-accent"];

export function Projects() {
  const { t } = useLanguage();

  return (
    <section id="projects" className="py-32 sm:py-40 relative overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-b from-card/50 to-transparent" />
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-accent/10 rounded-full blur-[150px]" />

      <div className="mx-auto max-w-7xl px-6 lg:px-8 relative">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-8 mb-20"
        >
          <div className="max-w-2xl">
            <p className="text-sm font-semibold text-accent uppercase tracking-wider mb-4">{t.projects.label}</p>
            <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-foreground leading-[1.1]">
              {t.projects.title} <span className="text-accent">{t.projects.titleHighlight}</span>
            </h2>
          </div>
          <p className="text-foreground/60 max-w-md leading-relaxed">
            {t.projects.subtitle}
          </p>
        </motion.div>

        <div className="space-y-2">
          {t.projects.items.map((project, index) => (
            <motion.div
              key={project.title}
              initial={{ opacity: 0 }}
              whileInView={{ opacity: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="group"
            >
              <div className="py-10 border-t border-border/50 -mx-6 px-6 rounded-xl">
                <div className="grid lg:grid-cols-12 gap-6 lg:gap-8 items-start">
                  {/* Number */}
                  <div className="lg:col-span-1">
                    <span className={`text-sm font-semibold ${accentColors[index]}`}>{String(index + 1).padStart(2, '0')}</span>
                  </div>

                  {/* Title & Client */}
                  <div className="lg:col-span-4">
                    <p className="text-xs text-foreground/50 uppercase tracking-wider mb-2">
                      {project.client}
                    </p>
                    <h3 className="text-2xl font-semibold text-foreground">
                      {project.title}
                    </h3>
                  </div>

                  {/* Description */}
                  <div className="lg:col-span-7">
                    <p className="text-foreground/60 leading-relaxed mb-4">
                      {project.description}
                    </p>
                    <div className="flex flex-wrap gap-2">
                      {project.tags.map((tag) => (
                        <span 
                          key={tag} 
                          className="text-xs text-foreground/60 bg-secondary px-3 py-1.5 rounded-full border border-border/50"
                        >
                          {tag}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
