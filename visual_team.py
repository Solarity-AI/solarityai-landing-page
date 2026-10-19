"""Founder-approved roster. Add people only after explicit selection by the founder."""
from html import escape


TEAM_MEMBERS = (
    {'slug': 'emrecan-ozkan', 'name': 'Emrecan Özkan', 'initials': 'EÖ'},
    {'slug': 'ali-yilmaz', 'name': 'Ali Yılmaz', 'initials': 'AY'},
    {'slug': 'hasan-ak', 'name': 'Hasan Ak', 'initials': 'HA'},
    {'slug': 'eren-oz', 'name': 'Eren Öz', 'initials': 'EÖ'},
    {'slug': 'batuhan-yuceturk', 'name': 'Batuhan Yücetürk', 'initials': 'BY'},
    {'slug': 'melik-kaplan', 'name': 'Melik Kaplan', 'initials': 'MK'},
)

# Only identity-matched portraits from the official company website belong here.
TEAM_PORTRAITS = {
    'emrecan-ozkan': {
        'src': '/assets/team/emrecan-ozkan-240-d1df701b3489.webp',
        'srcset': '/assets/team/emrecan-ozkan-240-d1df701b3489.webp 240w, /assets/team/emrecan-ozkan-480-d117500c13c0.webp 480w',
        'width': 240, 'height': 274,
    },
    'ali-yilmaz': {
        'src': '/assets/team/ali-yilmaz-240-6a90dfff30ac.webp',
        'srcset': '/assets/team/ali-yilmaz-240-6a90dfff30ac.webp 240w, /assets/team/ali-yilmaz-480-65556168df49.webp 480w',
        'width': 240, 'height': 308,
    },
    'hasan-ak': {
        'src': '/assets/team/hasan-ak-240-d70bfaf3c656.webp',
        'srcset': '/assets/team/hasan-ak-240-d70bfaf3c656.webp 240w, /assets/team/hasan-ak-480-866549c99e7b.webp 480w',
        'width': 240, 'height': 308,
    },
}


def selected_team():
    """A complete typographic roster, without partial portraits or invented roles."""
    entries = []
    for member in TEAM_MEMBERS:
        entries.append('<li class="selected-team-member" data-member="' + member['slug']
                       + '"><h3>' + escape(member['name']) + '</h3></li>')
    return ('<section class="selected-team wrap" id="team" aria-labelledby="selected-team-heading">'
            '<div class="selected-team-intro"><div><p class="eyebrow">The team</p>'
            '<h2 id="selected-team-heading">Individual talent.<br>Shared ambition.</h2></div>'
            '<p>Meet the team helping bring Solarity AI’s products and company vision to life.</p></div>'
            '<ul class="selected-team-list">' + ''.join(entries) + '</ul></section>')
