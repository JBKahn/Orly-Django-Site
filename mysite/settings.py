"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u=^)5nuz)f)*svbu22kxg^(g+w2q*zk!x##o^hk7((_+87dsoc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["orlywaldman.com"]

# Email
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = os.getenv("EMAIL_HOST", "testemailhost")
EMAIL_PORT = 26
EMAIL_HOST_USER = 'automaticreply@orlywaldman.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "testpassword")
DEFAULT_FROM_EMAIL = 'orly@orlywaldman.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'rest_framework',
    'django_extensions',
    'core',
    'home',
    'portfolio',
    'reviews',
    'services',
    'special_effects',
    'artist',
    'contact',
    'community',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "mysite.context_processors.navigation",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'test_db_setting'),
        'USER': os.getenv('DB_USER', 'test_db_setting'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'test_db_setting'),
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home3/orlywald/public_html/static"
MEDIA_ROOT = "/home3/orlywald/public_html"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

GRAPPELLI_ADMIN_TITLE = 'Orly Kahn Makeup Artist Admin'
