"""Shared product staging: official store badges and the product close (CINEMATIC_PREMIUM_PLAN.md P5b)."""
from templating import render

APP_STORE_BADGE = '/assets/badges/app-store-badge-black.svg'
GOOGLE_PLAY_BADGE = '/assets/badges/google-play-badge.png'


def store_badges(app, fallback=''):
    """Official, unmodified badges. The ↗ sits outside each badge's clear space."""
    if not app.get('apple'):
        return fallback
    return render('visual_stage/store_badges.html.j2', app=app, apple_badge=APP_STORE_BADGE, google_badge=GOOGLE_PLAY_BADGE)


def product_close(app, btn, contact):
    """The product page ends in its own world: icon, statement, badges and one inquiry path."""
    return render('visual_stage/product_close.html.j2', app=app, btn=btn, contact=contact, badges=store_badges(app))
