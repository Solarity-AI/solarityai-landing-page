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

# The company's channels, from its official Linktree (https://linktr.ee/solarity_ai, read 2026-10-22), in the
# Linktree's order. Each URL answered live that day (Medium blocks scripted checks); the Linktree's second X
# address, x.com/solarity_ai_company, returns 404 and is left out.
COMPANY_PROFILES = (
    ('LinkedIn', 'https://www.linkedin.com/company/solarity-ai-company'),
    ('Instagram', 'https://www.instagram.com/solarity_ai'),
    ('X', 'https://x.com/solarity_ai'),
    ('WhatsApp', 'https://whatsapp.com/channel/0029Vb6z14n42DcffGUs9x3R'),
    ('Telegram', 'https://t.me/solarity_ai'),
    ('Medium', 'https://medium.com/solarity-ai'),
    ('YouTube', 'https://www.youtube.com/@solarity_ai'),
    ('GitHub', 'https://github.com/Solarity-AI'),
    ('TikTok', 'https://www.tiktok.com/@solarityai'),
    ('Facebook', 'https://www.facebook.com/solarity.ai.company'),
    ('Pinterest', 'https://www.pinterest.com/solarity_ai'),
)

# Google Forms from the same Linktree; titles and purposes as each form describes itself. The Linktree's
# "Book a call with our CEO" is the booking page the site already links (build_site.BOOKING).
COMPANY_FORMS = {
    'feedback': 'https://forms.gle/Xm7uAKg8sRRuRRfc9',     # Product Feedbacks: thoughts on the products
    'mentorship': 'https://forms.gle/8iamagPxXodEzP1ZA',   # Mentorship Program: a pilot for university students
    'certificate': 'https://forms.gle/CPYKbufGrpGn1Em28',  # Certificate of Participation: for event attendees
}

# Founder (recommendation 3). bio: 3-4 plain sentences on background, prior builds and fit for this work.
FOUNDER = {
    'bio': '',
    'why': '',          # one sentence: why he started Solarity AI
    'linkedin': 'https://www.linkedin.com/in/ataturhan/',  # founder: show it (2026-10-20)
}

# Team (recommendation 4), keyed by the approved names in visual_team.py. Fill only what each person
# agreed to show: 'role', 'commitment' ('Full-time', 'Part-time' or 'Adviser') and 'linkedin'.
# Titles and profiles supplied by the founder on 2026-10-21 (Batuhan Yücetürk: no profile given).
TEAM_DETAILS = {
    'Hasan Ak': {'role': 'Engineering manager and principal software engineer', 'linkedin': 'https://www.linkedin.com/in/hasan-erdem-ak/'},
    'Ali Yılmaz': {'role': 'Staff software engineer', 'linkedin': 'https://www.linkedin.com/in/ali-yilmaz2/'},
    'Emrecan Özkan': {'role': 'Staff software engineer', 'linkedin': 'https://www.linkedin.com/in/emrecan-ozkan/'},
    'Eren Öz': {'role': 'Senior software engineer', 'linkedin': 'https://www.linkedin.com/in/ozeren1337/'},
    'Melik Kaplan': {'role': 'Marketing engineer', 'linkedin': 'https://www.linkedin.com/in/egehan-melik-kaplan-5b317a29a/'},
    'Batuhan Yücetürk': {'role': 'Marketing engineer'},
}

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
