"""Safety boundaries for class-only filtering, independent of site markup."""
import unittest

from optimize_styles import optimize_css


class StyleOptimizerTests(unittest.TestCase):
    def optimize(self, source, html='<div class="present"></div>', dynamic=()):
        return optimize_css(source, html, dynamic)[0]

    def test_positive_absent_selector_pruned_without_reordering_cascade(self):
        css = '.present{color:red}.absent{color:green}.present{color:blue}'
        self.assertEqual(self.optimize(css), '.present{color:red}.present{color:blue}')

    def test_each_selector_branch_is_independent(self):
        css = '.missing,.present:hover,body{color:red}.parent .present{color:blue}'
        self.assertEqual(self.optimize(css), '.present:hover,body{color:red}')

    def test_functional_pseudos_are_opaque_even_with_absent_classes(self):
        css = '.missing:not(.absent){a:b}:is(.absent,.present){c:d}:where(.absent){e:f}:has(.absent){g:h}'
        self.assertEqual(self.optimize(css), css)

    def test_commas_and_braces_inside_attributes_and_strings(self):
        css = '.present[data-label="a,b.{c}"]{content:"keep { },  two spaces";background:url("data:image/svg+xml,a,b")} .gone{a:b}'
        result = self.optimize(css)
        self.assertIn('[data-label="a,b.{c}"]', result)
        self.assertIn('content:"keep { },  two spaces"', result)
        self.assertIn('url("data:image/svg+xml,a,b")', result)
        self.assertNotIn('.gone', result)

    def test_calc_whitespace_and_custom_property_values_are_preserved(self):
        css = ':root { --gap: 12px; --layout: 1fr  2fr; } .present { width: calc(100% - 2 * var(--gap)); margin: 0 auto; }'
        result = self.optimize(css)
        self.assertIn('calc(100% - 2 * var(--gap))', result)
        self.assertIn('--layout: 1fr 2fr;', result)
        self.assertIn('margin: 0 auto;', result)

    def test_media_pruning_keeps_nested_order_and_reduced_motion(self):
        css = '@media(max-width:500px){.gone{a:b}.present{a:c}@supports(display:grid){.present{display:grid}}}@media(min-width:999px){.gone{a:b}}@media(prefers-reduced-motion:reduce){*{animation:none}}'
        result = self.optimize(css)
        self.assertNotIn('999px', result)
        self.assertIn('@media(max-width:500px){.present{a:c}@supports(display:grid){.present{display:grid}}}', result)
        self.assertIn('prefers-reduced-motion:reduce', result)

    def test_keyframes_and_unknown_at_rules_keep_their_content(self):
        css = '@keyframes pulse { 0% { opacity: 0 } 100% { opacity: 1 } }@future foo { .missing { token: "yes" } }@font-face { font-family: test; src: url("font.woff2") }'
        self.assertEqual(self.optimize(css), css)

    def test_dynamic_states_survive_when_not_present_in_static_html(self):
        css = '.nav-enhanced .present{display:block}.is-open{display:flex}.nav-open{overflow:hidden}.image-preview-open{overflow:hidden}.future-state{a:b}'
        self.assertEqual(self.optimize(css, dynamic={'future-state'}), css)

    def test_empty_layer_still_establishes_cascade_order(self):
        css = '@layer first{.absent{color:red}}@layer second{.present{color:blue}}@layer first{.present{color:green}}'
        self.assertEqual(self.optimize(css), '@layer first{}@layer second{.present{color:blue}}@layer first{.present{color:green}}')

    def test_selector_and_function_comments_do_not_merge_or_separate_tokens(self):
        css = '.present/**/.present{font-family:some/**/thing;content:"/* literal */"}/* standalone */.gone{a:b}'
        self.assertEqual(self.optimize(css), '.present/**/.present{font-family:some/**/thing;content:"/* literal */"}')

    def test_escaped_selector_is_retained(self):
        self.assertEqual(self.optimize(r'.other\:state{color:red}'), r'.other\:state{color:red}')

    def test_corrupt_input_fails_instead_of_emitting_partial_css(self):
        for css in ['.present{a:b', '.present{content:"oops}', '.present /*oops']:
            with self.subTest(css=css), self.assertRaises(ValueError):
                self.optimize(css)


if __name__ == '__main__':
    unittest.main()
