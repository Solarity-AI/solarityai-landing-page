"""The three Solarity AI SaaS products: Engineering Max, Management Max, and Marketing Max.

Every statement here comes from the product's own site, read on 2026-10-19
(research-assets/saas-evidence.json), or from the founder's instruction of the
same day that the three SaaS products will also be released as mobile apps. The founder set all three
statuses to early access on 2026-10-20. Keep the status lines in step with that and with the sites; never add metrics, customers or prices
that a site does not state.
"""

MOBILE_PLAN = 'SaaS on the web today. Mobile versions are planned.'
# Shown under every row of SaaS product cards: the screens carry figures, and only some are real
SCREEN_NOTE = 'Screens from each SaaS product’s own site. Management Max and Marketing Max show sample apps and figures.'

SAAS = [
    dict(
        slug='engineering-max',
        name='Engineering Max',
        stage='Build',
        number='01',
        url='https://engineeringmax.solarityai.com/',
        domain='engineeringmax.solarityai.com',
        category='App engineering',
        status='SaaS · early access',
        tagline='Find and fix what keeps a mobile app out of the App Store.',
        summary=('Your own Claude Code or Codex writes a read-only report on the app, with no source code. '
                 'Engineering Max checks it against 155 rules across 12 areas, ranks the problems, and returns '
                 '1 focused fix prompt at a time, then checks each fix.'),
        facts=('155 rules across 12 areas, store blockers and security first',
               'For Expo, React Native, Flutter, and native apps',
               'Reads the agent’s report, never the source code',
               'Tested first on Solarity AI’s own Sleep Max'),
        fact_links={'Tested first on Solarity AI’s own Sleep Max': '/apps/sleep-max'},
        availability='Free during early access. Pricing is not set yet.',
        screens=(dict(file='engineering-max-overview.webp', width=1800, height=662, focus='0% 0',
                      alt='Engineering Max overview of a scan of Sleep Max: a health score of 59 out of 100 beside scores by area, from security to cost and efficiency.'),),
        caption='Engineering Max on Solarity AI’s own Sleep Max (repo name somni). From engineeringmax.solarityai.com.',
    ),
    dict(
        slug='management-max',
        name='Management Max',
        stage='Operate',
        number='02',
        url='https://managementmax.solarityai.com/',
        domain='managementmax.solarityai.com',
        category='Metrics for app portfolios',
        status='SaaS · early access',
        tagline='Governed weekly metrics for mobile app companies.',
        summary=('Management Max holds a company’s weekly metric set per app, checks every figure on the way in, '
                 'and combines it across any selection of apps. Where combining would be dishonest, it shows '
                 'the spread instead and names the reason.'),
        facts=('50 metric definitions and 16 validation rules',
               'Syncs from RevenueCat, AppsFlyer, App Store Connect, Google Play, Firebase, GitHub, and YouTube',
               'Roles for the whole team, and every change is signed',
               'Plans count apps, not seats'),
        availability='Free for 1 app and 2 seats, with paid plans for larger portfolios.',
        screens=(dict(file='management-max-overview.webp', width=1160, height=1280,
                      alt='Management Max overview of a sample week: active users, MRR and crash-free sessions across 7 sample apps, and a retention spread it declines to average.'),
                 dict(file='management-max-sources.webp', width=2360, height=760,
                      alt='Management Max sources: RevenueCat, AppsFlyer, App Store Connect, Google Play, Firebase, GitHub, and YouTube feed 4 routes in, which pass 16 rules before the data is stored.')),
        caption='From managementmax.solarityai.com, with sample apps and figures.',
    ),
    dict(
        slug='marketing-max',
        name='Marketing Max',
        stage='Grow',
        number='03',
        url='https://marketingmax.solarityai.com/',
        domain='marketingmax.solarityai.com',
        category='Short-form video marketing',
        status='SaaS · early access',
        tagline='Your next Reel, made from one that already worked.',
        summary=('Marketing Max finds the Reels that performed, writes the caption and the line on the video in '
                 'the brand’s voice, and posts to Instagram at the chosen time. A person approves each of the '
                 '4 steps.'),
        facts=('Built for Solarity AI’s own apps first',
               '4 recorded approvals: video, reason, caption, and send',
               'Line tests and results for every post',
               'Instagram today, with TikTok and YouTube Shorts planned'),
        availability='Pricing is not set yet.',
        screens=(dict(file='marketing-max-home.webp', width=2880, height=1800,
                      alt='Marketing Max Home on a desktop with sample data: 4 posts that need a person, plays for the last 7 days, and new Reels to use.'),
                 dict(file='marketing-max-caption.webp', width=1880, height=1800,
                      alt='Step 3 of a new post in Marketing Max, with sample data: the Instagram preview beside the line and caption written in the brand’s voice.')),
        caption='The real product with sample data, from marketingmax.solarityai.com.',
    ),
]
