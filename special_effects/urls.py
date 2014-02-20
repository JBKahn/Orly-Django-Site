from django.conf.urls import patterns, url
from special_effects.views import FXPortfolioView

urlpatterns = patterns('',
        url(r'^$', FXPortfolioView.as_view(), name='portfolio'),
)
