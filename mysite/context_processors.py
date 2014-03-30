from django.core.urlresolvers import reverse


def navigation(request):
    '''
    A context processor to add navigation the current Context
    '''
    pages = [
        {"name": "Home", "path": reverse('home:home_page')},
        {"name": "Bridal Portfolio", "path": reverse('portfolio:portfolio')},
        {"name": "Reviews", "path": reverse('reviews:reviews')},
        # {"name": "Services", "path": reverse('services:services')},
        {"name": "FX Portfolio", "path": reverse('special_effects:portfolio')},
        {"name": "The Artist", "path": reverse('artist:about')},
        {"name": "Contact", "path": reverse('contact:form')},
        {"name": "Community", "path": reverse('community:community')},
    ]
    return {"pages": pages}
