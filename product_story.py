"""Evidence-led app stories using selected, unaltered App Store imagery.

Each record explains visible functionality, not an independently tested outcome.
Keep provenance and exclusions in research-assets/product-story-evidence.json.
"""
from image_provenance import provenance
from html import escape as e


PRODUCT_STORIES = {
    'looks-max': {
        'title': 'An assessment. A more considered routine.',
        'layout': 'editorial',
        'intro': 'A closer look at how Looks Max presents its appearance insights and suggestions.',
        'steps': [{
            'phase': 'Assessment to suggestions',
            'title': 'Explore the suggestions behind the score.',
            'copy': 'The dashboard brings together an overall evaluation and styling suggestions, with links to your history and progress.',
            'screen': 'looks-max-detail-screen-6.webp',
            'screen_width': 600,
            'screen_height': 1298,
            'alt': 'Looks Max official App Store imagery showing the overall evaluation and makeup and outfit suggestion cards, with sample app content.',
            'caption': 'Evaluation and suggestions',
        }],
    },
    'iq-max': {
        'title': 'A daily practice shaped around your focus.',
        'layout': 'sequence',
        'intro': 'Choose the areas you want to practice, then decide which exercises belong in your routine.',
        'steps': [{
            'phase': 'Shape your routine',
            'title': 'Make the routine your own.',
            'copy': 'Choose exercises to include in your daily practice. The routine screen makes the available activities and your selections visible together.',
            'screen': 'iq-max-detail-screen-6.webp',
            'screen_width': 600,
            'screen_height': 1298,
            'alt': 'IQ Max official App Store imagery showing exercise selection switches for a daily routine, with sample app content.',
            'caption': 'Daily routine selection',
        }],
    },
    'fitness-max': {
        'title': 'The details of a day. The rhythm of a routine.',
        'layout': 'asymmetric',
        'intro': 'See examples from Only Fitness, the store-listed app presented here as Fitness Max.',
        'steps': [{
            'phase': 'Understand the details',
            'title': 'Review a meal at a glance.',
            'copy': 'Photo-based meal analysis presents estimated energy and macronutrients with a coaching note. The example screen includes detected items to review and adjust.',
            'screen': 'fitness-max-detail-screen-3.webp',
            'screen_width': 600,
            'screen_height': 1298,
            'alt': 'Only Fitness official App Store imagery showing a sample meal nutrition estimate, detected items, and a coaching note.',
            'caption': 'Meal analysis · nutrition estimates',
        }, {
            'phase': 'Follow your consistency',
            'title': 'Make consistency visible.',
            'copy': 'A streak view marks repeated activity within the app. The screen shows an illustrative milestone, not a claim about a user’s fitness results.',
            'screen': 'fitness-max-detail-screen-5.webp',
            'screen_width': 600,
            'screen_height': 1298,
            'alt': 'Only Fitness official App Store imagery showing an illustrative streak celebration with a sample 25-day milestone.',
            'caption': 'Streak celebration',
        }],
    },
}


def product_story(app):
    """A visual product story with quiet, permanently available enlargement."""
    story = PRODUCT_STORIES.get(app['slug'])
    if not story:
        return ''
    cards = []
    for step in story['steps']:
        image = '/assets/' + e(step['screen'])
        title = e(app['name'] + ': ' + step['title'].rstrip('.'))
        alt = e(step['alt'])
        cards.append(f'''<article class="product-story-step">
          <div class="product-story-copy"><p class="product-story-phase">{e(step['phase'])}</p><h3>{e(step['title'])}</h3><p>{e(step['copy'])}</p></div>
          <figure class="product-story-frame">
            <a class="screenshot-open" href="{image}" data-image-title="{title}" data-image-alt="{alt}" target="_blank" rel="noopener">
              <span class="product-story-image"><img src="{image}" alt="{alt}" width="{step['screen_width']}" height="{step['screen_height']}" sizes="(max-width: 390px) calc(100vw - 72px), (max-width: 640px) 318px, (max-width: 1024px) 290px, 320px" loading="lazy" decoding="async"></span>
              <span class="screenshot-enlarge"><svg aria-hidden="true" focusable="false" viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Enlarge<span class="sr-only"> {e(step['title'])}</span></span></span>
            </a>
            <figcaption>{e(step['caption'])}</figcaption>
          </figure>
        </article>''')
    return f'''<section class="product-story wrap" data-story-layout="{e(story['layout'])}" data-product-accent="{e(app['color'])}" aria-labelledby="product-story-title">
      <header class="product-story-heading"><h2 id="product-story-title">{e(story['title'])}</h2><p>{e(story['intro'])}</p></header>
      <div class="product-story-grid">{''.join(cards)}</div>
      <p class="product-story-source caption">{provenance()} <a href="{e(app['apple'])}" target="_blank" rel="noopener">View listing <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a></p>
    </section>'''
