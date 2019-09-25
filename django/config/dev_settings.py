from .common_settings import *

DEBUG = True
SECRET_KEY = 'hard to guess string'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES['default'].update({
    'NAME': 'mymdb',
    'USER': 'mymdb',
    'PASSWORD': 'development',
    'HOST': '127.0.0.1',
    'PORT': '5432',
})

CASHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-locmemcache',
        'TIMEOUT': 5  # seconds
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, '../media_root')

# django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]
