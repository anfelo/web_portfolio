"""
WSGI config for web_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

from whitenoise.django import DjangoWhiteNoise


path = os.path.expanduser('~/web_portfolio')
if path not in sys.path:
    sys.path.append(path)

os.environ["SECRET_KEY"] = '5)j#+erjdz19==6y_6+j802bc#w%=#+ln6#p2+72p=pke&91q@'
os.environ['DJANGO_SETTINGS_MODULE'] = 'web_portfolio.settings'
os.environ['EMAIL_PASSWORD'] = 'capri1801CORNIO'

application = StaticFilesHandler(get_wsgi_application())
application = DjangoWhiteNoise(application)
