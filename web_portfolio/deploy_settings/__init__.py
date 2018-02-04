from web_portfolio.settings import *


DEBUG = FALSE
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']

SECRET_KEY = get_env_variable("SECRET_KEY")