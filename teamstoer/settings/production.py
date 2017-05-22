from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['.teamstoer.nl']
WWW_HOST = "www.teamstoer.nl"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'teamstoer'),
        'USER': os.getenv('DATABASE_USER', 'teamstoer'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'teamstoer'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}