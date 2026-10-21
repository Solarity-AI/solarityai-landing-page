"""Facts the site states about the company's record, people and plans.

Every value here is either verified from a public source (noted beside it) or supplied by the founder.
A field left empty (None, '' or an empty list) renders nothing: the page structure for it exists, hidden,
until the founder provides the fact. Record each new fact's source in CONTENT_REGISTER.md.
"""

# App Store Connect provider token (App Analytics > Sources > Campaigns). While empty, App Store links
# carry no campaign tag; Google Play and the web apps are tagged regardless (site_urls.attributed).
APPLE_CAMPAIGN_PROVIDER = ''

# App Store release dates, from Apple's public lookup for each listing (checked 2026-10-20).
# Each app is also on Google Play; its release date there is not stated.
APP_STORE_RELEASES = [
    ('looks-max', '2026-06-23'),
    ('fitness-max', '2026-08-15'),
    ('iq-max', '2026-09-11'),
    ('sleep-max', '2026-09-16'),
]

# Web app milestones for the shipping record, supplied by the founder:
# a list of dicts with 'slug' (from saas_products.SAAS), 'date' (ISO) and 'label' (e.g. 'Private testing opened').
WEB_APP_MILESTONES = []

# Founder (recommendation 3). bio: 3-4 plain sentences on background, prior builds and fit for this work.
FOUNDER = {
    'bio': '',
    'why': '',          # one sentence: why he started Solarity AI
    'linkedin': 'https://www.linkedin.com/in/ataturhan/',  # founder: show it (2026-10-20)
}

# Team (recommendation 4), keyed by the approved names in visual_team.py. Fill only what each person
# agreed to show: 'role', 'commitment' ('Full-time', 'Part-time' or 'Adviser') and 'linkedin'.
TEAM_DETAILS = {}

# Company facts (recommendation 13).
COMPANY = {
    'legal_name': 'Solarity AI LLC',
    'founded': '',           # year, e.g. '2025'
    'registered_in': '',     # e.g. 'Texas'
}

# The brief for programs and investors (recommendation 7).
PROGRAM_BRIEF = {
    'seeking': '',          # what Solarity AI is looking for (program, funding, mentors, credits)
    'use': '',              # what it would do with it
    'why_now': '',          # two sentences, in the founder's words
    'metrics': [],          # dicts: {'value': '12,400', 'label': 'downloads', 'as_of': '2026-10-01'}
    'one_pager': '',        # path of a published PDF one-pager, e.g. '/assets/solarity-ai-one-pager.pdf'
}
