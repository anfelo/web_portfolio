import dj_database_url

from web_portfolio.settings import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']

SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'