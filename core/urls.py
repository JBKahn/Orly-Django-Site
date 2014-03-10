from django.conf.urls import patterns, url
from core.views import GeneraetSprite, ResetBridalPortfolio, ResetSpecialEffectsPortfolio, ResetRevews

urlpatterns = patterns(
    '',
    url(r'^generate_sprites/$', GeneraetSprite.as_view(), name='generate_sprites'),
    url(r'^reset_portfolio/$', ResetBridalPortfolio.as_view(), name='reset_bridal_portfolio'),
    url(r'^reset_special_effects/$', ResetSpecialEffectsPortfolio.as_view(), name='reset_special_effects'),
    url(r'^reset_reviews/$', ResetRevews.as_view(), name='reset_reviews'),
)
