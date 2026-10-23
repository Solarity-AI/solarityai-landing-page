"""Team portraits: small widths for the Careers avatars, without shrinking the image search engines see."""
import re
import unittest
from pathlib import Path

from optimize_images import PORTRAIT_WIDTHS, responsive_image_attrs

ROOT = Path(__file__).resolve().parent


class PortraitTest(unittest.TestCase):
    def test_avatars_get_a_2x_width_and_the_fallback_stays_480(self):
        attrs = responsive_image_attrs('/assets/team/hasan-ak.webp')
        widths = [int(w) for w in re.findall(r' (\d+)w', attrs['srcset'])]
        self.assertEqual(widths, list(PORTRAIT_WIDTHS))
        self.assertLess(widths[0], 2 * 105, 'a phone avatar at 2x must not need the 320w roster size')
        self.assertIn('-480.', attrs['src'])

    def test_careers_avatars_offer_the_small_width(self):
        page = (ROOT / 'dist' / 'careers' / 'index.html').read_text(encoding='utf-8')
        avatars = re.findall(r'<img src="/assets/optimized/[a-z-]+-480\.[0-9a-f]+\.webp"[^>]*srcset="[^"]*-128\.', page)
        self.assertEqual(len(avatars), 5)


if __name__ == '__main__':
    unittest.main()
