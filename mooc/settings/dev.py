from mooc.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_APPS = [
        'django_extensions',
]

INSTALLED_APPS += THIRD_APPS
