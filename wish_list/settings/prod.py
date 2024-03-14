import os
from .base import *

DEBUG=False

ADMINS = [
    ('Filip A', 'filip.adamek@outlook.com')
]

ALLOWED_HOSTS = ['prezent.filip-adamek.pl', 'www.prezent.filip-adamek.pl']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}