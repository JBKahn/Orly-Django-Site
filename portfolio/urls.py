from django.conf.urls import patterns, url
from portfolio.views import PortfolioView

urlpatterns = patterns(
    '',
    url(r'^$', PortfolioView.as_view(), name='portfolio'),
)
