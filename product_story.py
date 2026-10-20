"""Evidence-led app stories using selected, unaltered App Store imagery.

Each record explains visible functionality, not an independently tested outcome.
Keep provenance and exclusions in research-assets/product-story-evidence.json.
"""
from image_provenance import provenance
from templating import render


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
    # Each enlarged image is titled with the app and the step, without the step title's full stop.
    cards = [{'step': step, 'title': app['name'] + ': ' + step['title'].rstrip('.')} for step in story['steps']]
    return str(render('product_story/product_story.html.j2', app=app, story=story, cards=cards,
                      provenance=provenance()))
