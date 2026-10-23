"""Founder-approved roster. Add people only after explicit selection by the founder."""
from company_facts import FOUNDER
from visual_sections import FOUNDER_PORTRAIT
from templating import render
from visual_record import team_detail


# Roster order set by the founder on 2026-10-21.
TEAM_MEMBERS = (
    {'slug': 'hasan-ak', 'name': 'Hasan Ak', 'initials': 'HA', 'portrait': '/assets/team/hasan-ak.webp'},
    {'slug': 'ali-yilmaz', 'name': 'Ali Yılmaz', 'initials': 'AY', 'portrait': '/assets/team/ali-yilmaz.webp'},
    {'slug': 'emrecan-ozkan', 'name': 'Emrecan Özkan', 'initials': 'EÖ', 'portrait': ''},
    {'slug': 'eren-oz', 'name': 'Eren Öz', 'initials': 'EÖ', 'portrait': '/assets/team/eren-oz.webp'},
    {'slug': 'melik-kaplan', 'name': 'Melik Kaplan', 'initials': 'MK', 'portrait': '/assets/team/melik-kaplan.webp'},
    {'slug': 'batuhan-yuceturk', 'name': 'Batuhan Yücetürk', 'initials': 'BY', 'portrait': '/assets/team/batuhan-yuceturk.webp'},
)

# Portraits are the founder-supplied photos (2026-10-21), cropped to one 4:5 frame with the eyes on the 40% line;
# provenance in research-assets/team-portraits.json. A member without one shows a monogram in the same frame.

def selected_team(founder_story=''):
    """The founder's card and story, then the complete roster, without partial portraits or invented roles."""
    return render('visual_team/selected_team.html.j2', members=TEAM_MEMBERS, team_detail=team_detail,
                  founder=FOUNDER_PORTRAIT, founder_linkedin=FOUNDER.get('linkedin', ''), founder_story=founder_story)
