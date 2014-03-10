from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('home.urls', namespace="home")),
    url(r'^core/', include('core.urls', namespace="core")),
    url(r'^portfolio/', include('portfolio.urls', namespace="portfolio")),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^services/', include('services.urls', namespace="services")),
    url(r'^special_effects/', include('special_effects.urls', namespace="special_effects")),
    url(r'^artist/', include('artist.urls', namespace="artist")),
    url(r'^contact/', include('contact.urls', namespace="contact")),
    url(r'^community/', include('community.urls', namespace="community")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
