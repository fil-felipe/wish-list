from .default import *

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = "test_secret"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

STATIC_ROOT= BASE_DIR / 'static/'