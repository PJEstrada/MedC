# settings/local.py

from .base import *


DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'medc_db',
        'USER': 'medc_user',
        'PASSWORD': 'medc',
        'HOST': 'localhost',
        'PORT': '',
    }
}


INSTALLED_APPS += ("debug_toolbar", )
