from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'Series',
        'USER': 'postgres',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_ROOT = BASE_DIR.child('media')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]