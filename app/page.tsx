import dynamic from 'next/dynamic'
import Navbar from '@/components/layout/Navbar'
import Footer from '@/components/layout/Footer'
import Hero from '@/components/sections/Hero'
import HashScroller from '@/components/HashScroller'

const About        = dynamic(() => import('@/components/sections/About'))
const Partnerships = dynamic(() => import('@/components/sections/Partnerships'))
const Products     = dynamic(() => import('@/components/sections/Products'))
const Projects     = dynamic(() => import('@/components/sections/Projects'))
const Team         = dynamic(() => import('@/components/sections/Team'))
const Contact      = dynamic(() => import('@/components/sections/Contact'))

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
