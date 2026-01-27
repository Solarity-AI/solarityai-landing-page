"use client";

import Link from "next/link";
import { useState } from "react";
import { motion } from "framer-motion";
import {
  Code,
  Megaphone,
  Handshake,
  Palette,
  ArrowRight,
  CheckCircle,
  Upload,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Header } from "@/components/header";
import { Footer } from "@/components/footer";

export default function CareersPage() {
  const [selectedFile, setSelectedFile] = useState<string>("");
  const [showSuccess, setShowSuccess] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const positions = [
    {
      title: "Full Stack Engineer",
      icon: Code,
      link: "https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws",
    },
    {
      title: "Marketing Specialist",
      icon: Megaphone,
      link: "https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws",
    },
    {
      title: "Business Development Manager",
      icon: Handshake,
      link: "https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws",
    },
    {
      title: "UI/UX Designer",
      icon: Palette,
      link: "https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws",
    },
  ];

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0].name);
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsSubmitting(true);

    // Simulate form submission
    setTimeout(() => {
      setShowSuccess(true);
      setIsSubmitting(false);
      window.scrollTo({ top: 0, behavior: "smooth" });
    }, 1500);
  };

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
        {/* Hero Section */}
        <section className="relative pt-32 pb-16 overflow-hidden">
          <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-primary/10 rounded-full blur-[150px]" />
          <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-accent/10 rounded-full blur-[150px]" />

          <div className="mx-auto max-w-7xl px-6 lg:px-8 relative">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="text-center max-w-4xl mx-auto"
            >
              <h1 className="text-5xl sm:text-6xl font-bold tracking-tight mb-6">
                Join{" "}
                <span className="text-primary" aria-label="emphasis">
                  Our Team
                </span>
              </h1>
              <p className="text-xl text-foreground/70 leading-relaxed">
                We're building the future of AI-powered software solutions. Join
                us in creating innovative products that make a real impact.
              </p>
            </motion.div>
          </div>
        </section>

        {/* Open Positions Section */}
        <section className="py-20 border-t border-border/50">
          <div className="mx-auto max-w-7xl px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center mb-12"
              role="region"
              aria-labelledby="open-positions-heading"
            >
              <h2
                id="open-positions-heading"
                className="text-4xl font-bold mb-4"
              >
                Open Positions
              </h2>
              <p className="text-lg text-foreground/60 mb-4">
                View detailed job descriptions for our current openings
              </p>
              <a
                href="https://drive.google.com/drive/folders/1iOew815DHxi_TDBWtbpUp_433V-bamws"
                target="_blank"
                rel="noopener noreferrer"
                className="text-primary hover:underline font-medium"
              >
                View all job posters (Drive folder) →
              </a>
            </motion.div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {positions.map((position, index) => (
                <motion.a
                  key={position.title}
                  href={position.link}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={`View ${position.title} job description (opens in new tab)`}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.6, delay: index * 0.1 }}
                  className="group relative bg-card rounded-2xl p-6 border border-border/50 hover:border-primary/50 transition-all hover:-translate-y-2"
                >
                  <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-primary to-accent rounded-t-2xl transform scale-x-0 group-hover:scale-x-100 transition-transform" />
                  <div className="w-16 h-16 rounded-xl bg-primary/10 flex items-center justify-center mb-4">
                    <position.icon className="w-8 h-8 text-primary" />
                  </div>
                  <h3 className="text-lg font-semibold mb-2">
                    {position.title}
                  </h3>
                  <p className="text-sm text-foreground/60 mb-4">
                    View Job Description
                  </p>
                  <ArrowRight className="w-5 h-5 text-primary transform group-hover:translate-x-1 transition-transform" />
                </motion.a>
              ))}
            </div>
          </div>
        </section>

        {/* Application Form Section */}
        <section className="py-20 border-t border-border/50">
          <div className="mx-auto max-w-4xl px-6 lg:px-8">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="bg-card rounded-3xl p-8 lg:p-12 border border-border/50"
              role="form"
              aria-labelledby="application-form-heading"
            >
              {/* Success Message */}
              {showSuccess && (
                <div className="mb-8 bg-green-500/10 border border-green-500/30 rounded-xl p-6 text-center">
                  <CheckCircle className="w-16 h-16 text-green-500 mx-auto mb-4" />
                  <h4 className="text-xl font-semibold text-green-500 mb-2">
                    Application Submitted Successfully!
                  </h4>
                  <p className="text-foreground/70">
                    Thank you for your interest in joining Solarity AI. We've
                    received your application and will review it shortly.
                  </p>
                </div>
              )}

              {!showSuccess && (
                <form onSubmit={handleSubmit} className="space-y-8">
                  {/* Personal Information */}
                  <div>
                    <div className="mb-6 pb-4 border-b border-border/50">
                      <h3
                        id="application-form-heading"
                        className="text-2xl font-semibold mb-2"
                      >
                        Personal Information
                      </h3>
                      <p className="text-sm text-foreground/60">
                        Please provide your basic contact details
                      </p>
                    </div>

                    <div className="grid sm:grid-cols-2 gap-5">
                      <div>
                        <label
                          htmlFor="firstName"
                          className="block text-sm font-medium mb-2"
                        >
                          First Name <span className="text-red-500">*</span>
                        </label>
                        <Input
                          id="firstName"
                          name="First Name"
                          required
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>
                      <div>
                        <label
                          htmlFor="lastName"
                          className="block text-sm font-medium mb-2"
                        >
                          Last Name <span className="text-red-500">*</span>
                        </label>
                        <Input
                          id="lastName"
                          name="Last Name"
                          required
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>
                    </div>

                    <div className="grid sm:grid-cols-2 gap-5 mt-5">
                      <div>
                        <label
                          htmlFor="email"
                          className="block text-sm font-medium mb-2"
                        >
                          Email Address <span className="text-red-500">*</span>
                        </label>
                        <Input
                          id="email"
                          name="Email"
                          type="email"
                          required
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                        <p className="text-xs text-foreground/50 mt-1">
                          We'll use this to contact you
                        </p>
                      </div>
                      <div>
                        <label
                          htmlFor="phone"
                          className="block text-sm font-medium mb-2"
                        >
                          Phone Number <span className="text-red-500">*</span>
                        </label>
                        <Input
                          id="phone"
                          name="Phone"
                          type="tel"
                          required
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>
                    </div>

                    <div className="mt-5">
                      <label
                        htmlFor="location"
                        className="block text-sm font-medium mb-2"
                      >
                        Location
                      </label>
                      <Input
                        id="location"
                        name="Location"
                        placeholder="City, State/Country"
                        className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                      />
                    </div>
                  </div>

                  {/* Professional Information */}
                  <div>
                    <div className="mb-6 pb-4 border-b border-border/50">
                      <h3 className="text-2xl font-semibold mb-2">
                        Professional Information
                      </h3>
                      <p className="text-sm text-foreground/60">
                        Tell us about your professional background
                      </p>
                    </div>

                    <div className="space-y-5">
                      <div>
                        <label
                          htmlFor="position"
                          className="block text-sm font-medium mb-2"
                        >
                          Position Applying For{" "}
                          <span className="text-red-500">*</span>
                        </label>
                        <select
                          id="position"
                          name="Position"
                          required
                          className="w-full h-12 px-4 rounded-lg bg-secondary/50 border border-border/50 text-foreground focus:ring-1 focus:ring-primary/50 focus:border-primary/50"
                        >
                          <option value="">Select a position</option>
                          <option value="Full Stack Engineer">
                            Full Stack Engineer
                          </option>
                          <option value="Marketing Specialist">
                            Marketing Specialist
                          </option>
                          <option value="Business Development Manager">
                            Business Development Manager
                          </option>
                          <option value="UI/UX Designer">UI/UX Designer</option>
                          <option value="Other">Other</option>
                        </select>
                      </div>

                      <div>
                        <label
                          htmlFor="linkedin"
                          className="block text-sm font-medium mb-2"
                        >
                          LinkedIn Profile
                        </label>
                        <Input
                          id="linkedin"
                          name="LinkedIn"
                          type="url"
                          placeholder="https://linkedin.com/in/yourprofile"
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>

                      <div>
                        <label
                          htmlFor="experience"
                          className="block text-sm font-medium mb-2"
                        >
                          Years of Experience{" "}
                          <span className="text-red-500">*</span>
                        </label>
                        <select
                          id="experience"
                          name="Experience"
                          required
                          className="w-full h-12 px-4 rounded-lg bg-secondary/50 border border-border/50 text-foreground focus:ring-1 focus:ring-primary/50 focus:border-primary/50"
                        >
                          <option value="">Select experience level</option>
                          <option value="0-1 years">0-1 years</option>
                          <option value="2-3 years">2-3 years</option>
                          <option value="4-5 years">4-5 years</option>
                          <option value="6-8 years">6-8 years</option>
                          <option value="9+ years">9+ years</option>
                        </select>
                      </div>
                    </div>
                  </div>

                  {/* Education Information */}
                  <div>
                    <div className="mb-6 pb-4 border-b border-border/50">
                      <h3 className="text-2xl font-semibold mb-2">
                        Education Information
                      </h3>
                      <p className="text-sm text-foreground/60">
                        Tell us about your educational background
                      </p>
                    </div>

                    <div className="space-y-5">
                      <div>
                        <label
                          htmlFor="university"
                          className="block text-sm font-medium mb-2"
                        >
                          University/Institution{" "}
                          <span className="text-red-500">*</span>
                        </label>
                        <Input
                          id="university"
                          name="University"
                          required
                          placeholder="e.g., University of Texas at Dallas"
                          className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>

                      <div className="grid sm:grid-cols-2 gap-5">
                        <div>
                          <label
                            htmlFor="degree"
                            className="block text-sm font-medium mb-2"
                          >
                            Degree Level <span className="text-red-500">*</span>
                          </label>
                          <select
                            id="degree"
                            name="Degree"
                            required
                            className="w-full h-12 px-4 rounded-lg bg-secondary/50 border border-border/50 text-foreground focus:ring-1 focus:ring-primary/50 focus:border-primary/50"
                          >
                            <option value="">Select degree level</option>
                            <option value="High School">High School</option>
                            <option value="Associate's Degree">
                              Associate's Degree
                            </option>
                            <option value="Bachelor's Degree">
                              Bachelor's Degree
                            </option>
                            <option value="Master's Degree">
                              Master's Degree
                            </option>
                            <option value="PhD/Doctorate">PhD/Doctorate</option>
                          </select>
                        </div>
                        <div>
                          <label
                            htmlFor="fieldOfStudy"
                            className="block text-sm font-medium mb-2"
                          >
                            Field of Study{" "}
                            <span className="text-red-500">*</span>
                          </label>
                          <Input
                            id="fieldOfStudy"
                            name="Field of Study"
                            required
                            placeholder="e.g., Computer Science"
                            className="h-12 bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                          />
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Application Details */}
                  <div>
                    <div className="mb-6 pb-4 border-b border-border/50">
                      <h3 className="text-2xl font-semibold mb-2">
                        Application Details
                      </h3>
                      <p className="text-sm text-foreground/60">
                        Help us understand why you'd be a great fit
                      </p>
                    </div>

                    <div className="space-y-5">
                      <div>
                        <label
                          htmlFor="coverLetter"
                          className="block text-sm font-medium mb-2"
                        >
                          Cover Letter <span className="text-red-500">*</span>
                        </label>
                        <Textarea
                          id="coverLetter"
                          name="Cover Letter"
                          required
                          rows={6}
                          placeholder="Tell us about yourself, why you're interested in this position, and what you can bring to our team..."
                          className="bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                        <p className="text-xs text-foreground/50 mt-1">
                          Minimum 200 characters
                        </p>
                      </div>

                      <div>
                        <label
                          htmlFor="resume"
                          className="block text-sm font-medium mb-2"
                        >
                          Resume/CV <span className="text-red-500">*</span>
                        </label>
                        <div className="flex items-center gap-4 p-4 rounded-lg bg-secondary/50 border border-border/50">
                          <label
                            htmlFor="resume"
                            className="inline-flex items-center gap-2 px-6 py-2 bg-primary text-primary-foreground rounded-lg cursor-pointer hover:opacity-90 transition-opacity"
                          >
                            <Upload className="w-4 h-4" />
                            Choose File
                          </label>
                          <input
                            type="file"
                            id="resume"
                            name="Resume"
                            accept=".pdf,.doc,.docx"
                            required
                            onChange={handleFileChange}
                            className="hidden"
                            aria-describedby="resume-help"
                          />
                          <span className="text-sm text-foreground/60">
                            {selectedFile || "No file chosen"}
                          </span>
                        </div>
                        <p
                          id="resume-help"
                          className="text-xs text-foreground/50 mt-1"
                        >
                          Accepted formats: PDF, DOC, DOCX (Max 5MB)
                        </p>
                      </div>

                      <div>
                        <label
                          htmlFor="additionalInfo"
                          className="block text-sm font-medium mb-2"
                        >
                          Additional Information
                        </label>
                        <Textarea
                          id="additionalInfo"
                          name="Additional Information"
                          rows={4}
                          placeholder="Any additional information you'd like to share (optional)"
                          className="bg-secondary/50 border-border/50 focus-visible:ring-1 focus-visible:ring-primary/50 focus-visible:border-primary/50"
                        />
                      </div>
                    </div>
                  </div>

                  {/* Submit Button */}
                  <Button
                    type="submit"
                    size="lg"
                    disabled={isSubmitting}
                    className="w-full rounded-full h-14 text-base bg-primary text-primary-foreground hover:bg-primary/90 font-semibold shadow-lg shadow-primary/25"
                  >
                    {isSubmitting ? "Submitting..." : "Submit Application"}
                    {!isSubmitting && <ArrowRight className="ml-2 h-5 w-5" />}
                  </Button>

                  <p className="text-xs text-center text-foreground/40 mt-4">
                    By submitting this form, you agree to our{" "}
                    <Link
                      href="/privacy"
                      className="text-primary hover:underline"
                    >
                      Privacy Policy
                    </Link>
                    .
                  </p>
                </form>
              )}
            </motion.div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
