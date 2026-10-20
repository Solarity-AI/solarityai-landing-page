"""The shipping record and the hidden-until-supplied company facts (company_facts.py)."""
from datetime import date

from company_facts import APP_STORE_RELEASES, COMPANY, FOUNDER, PROGRAM_BRIEF, TEAM_DETAILS, WEB_APP_MILESTONES
from saas_products import SAAS
from templating import render

_WORDS = {2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen'}


def long_date(iso):
    """'June 23, 2026' from an ISO date."""
    d = date.fromisoformat(iso)
    return f'{d.strftime("%B")} {d.day}, {d.year}'


def _short_date(iso):
    d = date.fromisoformat(iso)
    return f'{d.strftime("%b")} {d.day}'


def shipping_record(apps):
    """Four store launches in order, each linked to its public listing: progress against time, verifiable."""
    by_slug = {a['slug']: a for a in apps}
    launches = [dict(app=by_slug[slug], iso=iso, label=_short_date(iso)) for slug, iso in APP_STORE_RELEASES]
    first, last = date.fromisoformat(launches[0]['iso']), date.fromisoformat(launches[-1]['iso'])
    weeks = round((last - first).days / 7)
    saas = {p['slug']: p for p in SAAS}
    web = [dict(product=saas[m['slug']], iso=m['date'], label=_short_date(m['date']), text=m['label'])
           for m in WEB_APP_MILESTONES if m.get('slug') in saas and m.get('date') and m.get('label')]
    return str(render('visual_record/shipping_record.html.j2', launches=launches, web=web,
                      count=_WORDS.get(len(launches), str(len(launches))).capitalize(),
                      weeks=_WORDS.get(weeks, str(weeks)),
                      first=long_date(launches[0]['iso']), last=long_date(launches[-1]['iso'])))


def app_store_since(slug):
    """'June 23, 2026' for an app with a recorded App Store release, otherwise ''."""
    return next((long_date(iso) for s, iso in APP_STORE_RELEASES if s == slug), '')


def record_summary():
    """Launch count, weeks between the first and latest launch, and the first launch date."""
    dates = [date.fromisoformat(iso) for _, iso in APP_STORE_RELEASES]
    return {'count': len(dates), 'weeks': round((max(dates) - min(dates)).days / 7),
            'count_word': _WORDS.get(len(dates), str(len(dates))),
            'weeks_word': _WORDS.get(round((max(dates) - min(dates)).days / 7), ''),
            'first': long_date(min(dates).isoformat())}


def app_compare(apps):
    """The four store-listed apps in one table: focus, what each does, and its App Store release date."""
    releases = dict(APP_STORE_RELEASES)
    rows = [dict(app=a, since=app_store_since(a['slug']), since_iso=releases.get(a['slug'], ''))
            for a in apps if a.get('apple')]
    return str(render('visual_record/app_compare.html.j2', rows=rows))


def web_compare(saas):
    """The three web apps in one table: stage, who each is for, and its plans, from their own sites."""
    return str(render('visual_record/web_compare.html.j2', saas=saas))


def company_facts(email):
    """Verified company facts in one list; the founding year and state appear once supplied."""
    return str(render('visual_record/company_facts.html.j2', legal_name=COMPANY['legal_name'],
                      founded=COMPANY.get('founded', ''), registered_in=COMPANY.get('registered_in', ''),
                      record=record_summary(), saas=SAAS, email=email))


def founder_record():
    """Founder bio, motivation and profile link. Empty until supplied."""
    if not (FOUNDER.get('bio') or FOUNDER.get('why') or FOUNDER.get('linkedin')):
        return ''
    return str(render('visual_record/founder_record.html.j2', founder=FOUNDER))


def team_detail(name):
    """Role, commitment and profile link for one approved team member. Empty until supplied."""
    detail = TEAM_DETAILS.get(name) or {}
    if not any(detail.get(k) for k in ('role', 'commitment', 'linkedin')):
        return ''
    return str(render('visual_record/team_detail.html.j2', name=name, detail=detail))


def company_line():
    """'Solarity AI LLC · founded 2025 · registered in Texas', or '' until a fact beyond the name exists."""
    parts = [COMPANY['legal_name']]
    if COMPANY.get('founded'):
        parts.append('founded ' + COMPANY['founded'])
    if COMPANY.get('registered_in'):
        parts.append('registered in ' + COMPANY['registered_in'])
    return ' · '.join(parts) if len(parts) > 1 else ''


def program_brief():
    """What Solarity AI is looking for, why now, real numbers and the one-pager. Empty until supplied."""
    brief = PROGRAM_BRIEF
    metrics = [m for m in brief.get('metrics', []) if m.get('value') and m.get('label') and m.get('as_of')]
    if not (brief.get('seeking') or brief.get('why_now') or metrics or brief.get('one_pager')):
        return ''
    return str(render('visual_record/program_brief.html.j2', brief=brief, metrics=metrics,
                      as_of=long_date(max(m['as_of'] for m in metrics)) if metrics else ''))
