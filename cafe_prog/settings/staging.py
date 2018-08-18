from . import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cafe',
        'USER': 'cafe',
        'PASSWORD': '',
        'HOST': 'database',
        'PORT': '5432',
    }
}
