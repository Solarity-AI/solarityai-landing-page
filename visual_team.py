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
