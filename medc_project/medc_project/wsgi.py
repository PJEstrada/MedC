"""
WSGI config for medc_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medc_project.settings")

application = get_wsgi_application()

# Heroku live settings

try:
    from dj_static import Cling

    aplication = Cling(get_wsgi_application())
except:
    pass

try:
    from whitenoise.django import DjangoWhiteNoise

    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)
