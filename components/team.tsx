"use client";

import { motion } from "framer-motion";
import { Linkedin, Twitter } from "lucide-react";
import { useLanguage } from "@/lib/language-context";

const leadership = [
  {
    name: "Ata Turhan",
    role: "Chief Executive Officer",
    roleKey: "ceo",
    bio: "15+ years building enterprise software companies",
  },
  {
    name: "Umur Inan",
    role: "Chief Technology Officer",
    roleKey: "cto",
    bio: "Former tech lead at Fortune 500 companies",
  },
  {
    name: "Burak Hamuryen",
    role: "Chief Information Officer",
    roleKey: "cio",
    bio: "Enterprise architecture and digital transformation expert",
  },
];

const team = {
  business: [
    { name: "Gokberk Serin", role: "Business Development" },
    { name: "Ali Yilmaz", role: "Business Development" },
    { name: "Remzi Mert Tehneldere", role: "BD Associate" },
    { name: "Batuhan Kestek", role: "BD Associate" },
  ],
  engineering: [
    { name: "Hasan Erdem Ak", role: "Senior Full-Stack Engineer" },
    { name: "Mehmet Begun", role: "Backend Engineer" },
    { name: "Eren Can Donertas", role: "Frontend Engineer" },
  ],
  design: [
    { name: "Lara Sen", role: "Design Lead" },
    { name: "Beril Damaci", role: "Visual Designer" },
    { name: "Hilal Genc", role: "UX Designer" },
  ],
};

export function Team() {
  const { t } = useLanguage();

  return (
    <section id="team" className="py-32 sm:py-40 relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-card/50 to-transparent" />
      <div className="absolute bottom-0 left-1/2 w-[600px] h-[600px] bg-accent/10 rounded-full blur-[150px] -translate-x-1/2 translate-y-1/2" />

      <div className="mx-auto max-w-7xl px-6 lg:px-8 relative">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="max-w-2xl mb-20"
        >
          <p className="text-sm font-semibold text-primary uppercase tracking-wider mb-4">
            {t.team.label}
          </p>
          <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-foreground leading-[1.1]">
            {t.team.title}{" "}
            <span className="text-primary">{t.team.titleHighlight}</span>
          </h2>
          <p className="mt-6 text-lg text-foreground/60 leading-relaxed">
            {t.team.subtitle}
          </p>
        </motion.div>

        {/* Leadership */}
        <div className="mb-24">
          <motion.p
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            className="text-xs font-semibold text-accent uppercase tracking-wider mb-8"
          >
            {t.team.leadership}
          </motion.p>
          <div className="grid md:grid-cols-3 gap-8">
            {leadership.map((member, index) => (
              <motion.div
                key={member.name}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="group"
              >
                <div className="aspect-[4/5] bg-gradient-to-br from-card to-secondary rounded-2xl mb-6 overflow-hidden relative border border-border/50 group-hover:border-primary/30 transition-colors">
                  <div className="absolute inset-0 bg-gradient-to-t from-background/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-7xl font-bold text-primary/20 group-hover:text-primary/40 transition-colors">
                      {member.name
                        .split(" ")
                        .map((n) => n[0])
                        .join("")}
                    </span>
                  </div>
                  <div className="absolute bottom-4 left-4 right-4 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button
                      type="button"
                      className="p-2 rounded-full bg-primary/20 hover:bg-primary/30 transition-colors"
                    >
                      <Linkedin className="w-4 h-4 text-primary" />
                    </button>
                    <button
                      type="button"
                      className="p-2 rounded-full bg-primary/20 hover:bg-primary/30 transition-colors"
                    >
                      <Twitter className="w-4 h-4 text-primary" />
                    </button>
                  </div>
                </div>
                <h3 className="text-xl font-semibold text-foreground">
                  {member.name}
                </h3>
                <p className="text-sm text-primary mt-1">{member.role}</p>
                <p className="text-sm text-foreground/50 mt-2">{member.bio}</p>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Team Grid */}
        <div className="grid lg:grid-cols-3 gap-16">
          {Object.entries(team).map(([department, members], deptIndex) => (
            <motion.div
              key={department}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: deptIndex * 0.1 }}
            >
              <p
                className={`text-xs font-semibold uppercase tracking-wider mb-8 ${deptIndex === 0 ? "text-primary" : deptIndex === 1 ? "text-accent" : "text-primary"}`}
              >
                {department === "business"
                  ? t.team.departments.business
                  : department === "engineering"
                    ? t.team.departments.engineering
                    : t.team.departments.design}
              </p>
              <div className="space-y-6">
                {members.map((member) => (
                  <div
                    key={member.name}
                    className="flex items-center gap-4 group"
                  >
                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-primary/20 to-accent/20 flex items-center justify-center shrink-0 border border-border/50 group-hover:border-primary/30 transition-colors">
                      <span className="text-sm font-medium text-primary">
                        {member.name
                          .split(" ")
                          .map((n) => n[0])
                          .join("")}
                      </span>
                    </div>
                    <div>
                      <h4 className="text-base font-medium text-foreground group-hover:text-primary transition-colors">
                        {member.name}
                      </h4>
                      <p className="text-sm text-foreground/50">
                        {member.role}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>

        {/* Hiring CTA */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="mt-24 p-8 lg:p-12 rounded-2xl bg-gradient-to-r from-primary/10 to-accent/10 border border-primary/20"
        >
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-6">
            <div>
              <h3 className="text-2xl font-bold text-foreground mb-2">
                {t.team.hiring.title}
              </h3>
              <p className="text-foreground/60">{t.team.hiring.subtitle}</p>
            </div>
            <a
              href="/careers"
              className="inline-flex items-center justify-center px-8 py-4 rounded-full bg-primary text-primary-foreground font-semibold hover:bg-primary/90 transition-colors shadow-lg shadow-primary/25"
            >
              {t.team.hiring.cta}
            </a>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
