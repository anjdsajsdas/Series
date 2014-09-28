from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = '-w3wju=s7nzsdlb_7n^e^g22dwbu1gsm6$f3sbb6f@eqg#_1#*'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.videos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'series.urls'
WSGI_APPLICATION = 'series.wsgi.application'

LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



TEMPLATE_DIRS = [BASE_DIR.child('templates')]