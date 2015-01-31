import os

import dj_database_url


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

DIRNAME = os.path.join(os.path.dirname(__file__), '../')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/sitestatic/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), os.path.join(DIRNAME, 'static')]
STATIC_ROOT = 'sitestatic'
# MEDIA_ROOT = 'media'

# NEVER EVER EVER EVER DO THIS AGAIN.
CORE_UPLOAD_TO = 'static'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Database
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': dj_database_url.config(default='postgres://orlywald:orlywald@localhost/orlywald'),
}

# Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'orlykahnmakeupartist@gmail.com'
EMAIL_HOST_PASSWORD = 'testpassword'
DEFAULT_FROM_EMAIL = 'orlykahnmakeupartist@gmail.com'

# Security
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'u=^)5nuz)f)*svbu22kxg^(g+w2q*zk!x##o^hk7((_+87dsoc'
DEBUG = True
TEMPLATE_DEBUG = True
