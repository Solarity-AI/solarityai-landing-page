"""Founder-approved roster. Add people only after explicit selection by the founder."""
from templating import render
from visual_record import team_detail


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
    return render('visual_team/selected_team.html.j2', members=TEAM_MEMBERS, team_detail=team_detail)
