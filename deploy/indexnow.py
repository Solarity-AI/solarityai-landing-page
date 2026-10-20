"""Tell IndexNow search engines (Bing, Yandex, Seznam, Naver) which pages changed in a deploy.

Run after a push to develop. It waits until solarityai.com serves the committed sitemap, so engines
fetch the new pages, then submits every URL whose <lastmod> differs from the previous commit's sitemap.

    python deploy/indexnow.py [--previous <git rev>] [--all] [--dry-run]
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import seo  # noqa: E402

NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
ENDPOINT = 'https://api.indexnow.org/indexnow'


def lastmods(xml):
    root = ET.fromstring(xml)
    return {u.findtext(NS + 'loc'): u.findtext(NS + 'lastmod') for u in root.findall(NS + 'url')}


def fetch(url):
    request = urllib.request.Request(url + ('&' if '?' in url else '?') + f't={time.time():.0f}', headers={'User-Agent': 'solarityai-indexnow'})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', default='HEAD~1', help='git revision to compare the sitemap against')
    parser.add_argument('--all', action='store_true', help='submit every sitemap URL')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--wait', type=int, default=600, help='seconds to wait for the deploy')
    args = parser.parse_args()

    local = (ROOT / 'dist' / 'sitemap.xml').read_bytes()
    current = lastmods(local)
    try:
        previous = lastmods(subprocess.run(['git', 'show', f'{args.previous}:dist/sitemap.xml'], cwd=ROOT,
                                           capture_output=True, check=True).stdout)
    except (subprocess.CalledProcessError, ET.ParseError):
        previous = {}
    urls = sorted(current) if args.all else sorted(u for u, mod in current.items() if previous.get(u) != mod)
    if not urls:
        print('No page changed its lastmod; nothing to submit.')
        return 0
    print(f'{len(urls)} changed URL(s):', *urls, sep='\n  ')
    if args.dry_run:
        return 0

    deadline = time.time() + args.wait
    while True:
        try:
            if fetch(seo.ORIGIN + '/sitemap.xml') == local and fetch(f'{seo.ORIGIN}/{seo.INDEXNOW_KEY}.txt').decode().strip() == seo.INDEXNOW_KEY:
                break
        except OSError as exc:
            print('waiting:', exc)
        if time.time() > deadline:
            print('solarityai.com did not serve this sitemap in time; not submitting.')
            return 1
        time.sleep(20)

    body = json.dumps({'host': 'solarityai.com', 'key': seo.INDEXNOW_KEY,
                       'keyLocation': f'{seo.ORIGIN}/{seo.INDEXNOW_KEY}.txt', 'urlList': urls}).encode()
    request = urllib.request.Request(ENDPOINT, data=body, method='POST',
                                     headers={'Content-Type': 'application/json; charset=utf-8'})
    with urllib.request.urlopen(request, timeout=30) as response:
        print('IndexNow responded', response.status)
        return 0 if response.status in (200, 202) else 1


if __name__ == '__main__':
    sys.exit(main())
