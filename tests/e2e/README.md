# Solarity Static Rewrite - AC Test Suite

Bu klasor, static rewrite issue'sundaki acceptance criteria'leri Playwright ile test eder.

## Komutlar

- `npm run test:e2e` - tum AC testleri (visual haric)
- `npm run test:e2e:headed` - headed mod
- `npm run test:e2e:report` - HTML raporu
- `npm run test:e2e:install` - browser binary kurulumu
- `npm run test:e2e:visual` - AC01 visual regression (baseline compare)
- `npm run test:e2e:visual:update` - visual baseline olusturma/guncelleme

## AC kapsama matrisi

- AC01: `ac.static-and-ui.spec.js` (page load) + `ac.visual.spec.js` (snapshot karşılaştırma)
- AC02: `ac.static-and-ui.spec.js` (EN/TR toggle + localStorage persistence + 6 sayfa)
- AC03: `ac.static-and-ui.spec.js` (navbar scroll, active link, mobile menu)
- AC04: `ac.static-and-ui.spec.js` (fade-in-up observer görünürlük)
- AC05: `ac.static-and-ui.spec.js` (hero orb float keyframe)
- AC06: `ac.static-and-ui.spec.js` (partner logo hover filter değişimi)
- AC07: `ac.integrations.spec.js` (contact form + turnstile + formsubmit)
- AC08: `ac.integrations.spec.js` (careers form + CV upload + turnstile + formsubmit)
- AC09: `ac.integrations.spec.js` (form submit event + social click event)
- AC10: `ac.static-and-ui.spec.js` (Google Maps iframe)
- AC11: `ac.responsive.spec.js` (375/768/1024/1440 responsive tarama)
- AC12: `ac.static-and-ui.spec.js` (Next.js runtime marker yok + static asset scriptleri)
- AC13: `ac.static-and-ui.spec.js` (prefers-reduced-motion)
- AC14: `ac.static-and-ui.spec.js` (WebKit/Safari override)
- AC15: `ac.static-and-ui.spec.js` (hash load + hash click scroll)

## Notlar

- Form testlerinde gercek FormSubmit istegi atilmaz; request Playwright route ile mock'lanir.
- Turnstile script'i testte mock edilir (`window.turnstile`) ve token enjekte edilir.
- AC01 "identical" beklentisi icin visual snapshot testi `PLAYWRIGHT_VISUAL=1` ile aktiftir.
