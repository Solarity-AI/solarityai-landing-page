import Navbar from '@/components/layout/Navbar'
import Footer from '@/components/layout/Footer'
import Hero from '@/components/sections/Hero'
import About from '@/components/sections/About'
import Partnerships from '@/components/sections/Partnerships'
import Products from '@/components/sections/Products'
import Projects from '@/components/sections/Projects'
import Team from '@/components/sections/Team'
import Contact from '@/components/sections/Contact'
import HashScroller from '@/components/HashScroller'

function SectionDivider() {
  return (
    <div className="h-px bg-gradient-to-r from-transparent via-accent/20 to-transparent" />
  )
}

export default function HomePage() {
  return (
    <>
      <HashScroller />
      <Navbar />
      <main>
        <Hero />
        <SectionDivider />
        <About />
        <SectionDivider />
        <Partnerships />
        <SectionDivider />
        <Products />
        <SectionDivider />
        <Projects />
        <SectionDivider />
        <Team />
        <SectionDivider />
        <Contact />
      </main>
      <Footer />
    </>
  )
}
