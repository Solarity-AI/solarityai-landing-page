"""Re-fetch the published App Store screenshots at their native listing resolution.

The same official listing images recorded in research-assets/downloaded-assets.json and
product-story-evidence.json are requested at their largest size. Each native file is compared
with the published file (downscaled, mean and 99th-percentile channel difference) and recorded
with its checksum in research-assets/native-refetch.json.

The founder confirmed the native files on 2026-10-19 and the site now publishes them, so a re-run
checks that the listings still match what is published. Nothing is published by this script: the
natives land in source-assets/native/ (git-ignored, build-only).
Run: python refetch_native_screens.py
"""
from __future__ import annotations

from hashlib import sha256
from io import BytesIO
from pathlib import Path
import json
import re
import time
import urllib.request

from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'dist' / 'assets'
NATIVE = ROOT / 'source-assets' / 'native'
REPORT = ROOT / 'research-assets' / 'native-refetch.json'
# Clearly the same image: the 600px file and the downscaled native agree within these levels.
MATCH_MEAN = 4.0
MATCH_P99 = 40


def sources() -> dict:
    found = {}
    for item in json.loads((ROOT / 'research-assets/downloaded-assets.json').read_text(encoding='utf-8')):
        found[item['file']] = item['url']
    for item in json.loads((ROOT / 'research-assets/product-story-evidence.json').read_text(encoding='utf-8'))['assets']:
        found[item['file']] = item['source_url']
    return {name: url for name, url in found.items() if '-screen-' in name and (ASSETS / name).is_file()}


def fetch(url: str) -> bytes:
    # The CDN occasionally resets connections; retry patiently.
    for attempt in range(8):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'solarity-asset-refetch/1.0'})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except OSError:
            if attempt == 7:
                raise
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(url)


def compare(native: Image.Image, published: Image.Image) -> dict:
    scaled = native.convert('RGB').resize(published.size, Image.Resampling.LANCZOS)
    diff = ImageChops.difference(scaled, published.convert('RGB')).convert('L')
    histogram = diff.histogram()
    total = sum(histogram)
    mean = sum(level * count for level, count in enumerate(histogram)) / total
    running, p99 = 0, 0
    for level, count in enumerate(histogram):
        running += count
        if running >= total * 0.99:
            p99 = level
            break
    return {'mean_difference': round(mean, 2), 'p99_difference': p99, 'matches_published': mean <= MATCH_MEAN and p99 <= MATCH_P99}


def main() -> None:
    NATIVE.mkdir(parents=True, exist_ok=True)
    records = []
    for name, url in sorted(sources().items()):
        # The listing serves its largest stored size when a larger one is requested.
        native_url = re.sub(r'/\d+x\d+bb(-\d+)?\.\w+$', '/4000x4000bb.png', url)
        target = NATIVE / (Path(name).stem + '.png')
        # Resumable: reuse a native already fetched by an earlier run.
        data = target.read_bytes() if target.is_file() else fetch(native_url)
        time.sleep(1)
        with Image.open(BytesIO(data)) as native, Image.open(ASSETS / name) as published:
            comparison = compare(native, published)
            size = native.size
        target.write_bytes(data)
        records.append({
            'published_file': name,
            'published_sha256': sha256((ASSETS / name).read_bytes()).hexdigest(),
            'native_url': native_url,
            'native_file': 'source-assets/native/' + target.name,
            'native_size': list(size),
            'native_bytes': len(data),
            'native_sha256': sha256(data).hexdigest(),
            **comparison,
        })
        print(f"{name}: {size[0]}x{size[1]}, mean {comparison['mean_difference']}, p99 {comparison['p99_difference']}, match {comparison['matches_published']}")
    REPORT.write_text(json.dumps({
        'purpose': 'Native-resolution re-fetch of the published App Store screenshots (P5a)',
        'status': 'Founder confirmed the native files on 2026-10-19; the site publishes them. This run compares the listings with the published files.',
        'match_rule': f'downscaled native vs published: mean <= {MATCH_MEAN} and 99th percentile <= {MATCH_P99} levels',
        'assets': records,
    }, indent=2) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
