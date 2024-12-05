import os
from .default import *

DEBUG = False

ALLOWED_HOSTS = ["prezent.filip-adamek.pl","prezent.filada.eu"]
SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "wish_list",
        "USER": "wish_list_admin",
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"

LOGGING = {
    "version": 1,
    "disable_exisitng_logger": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{"
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{"
         }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "django_debug.log"),
            "formatter": "verbose"
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "django_error.log"),
            "formatter": "verbose"
        },
        "console": {
             "level": "DEBUG",
             "class": "logging.StreamHandler",
             "formatter": "simple"
        }
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True
        },
        "django.request": {
            "handlers": ["error_file", "console"],
            "level": "ERROR",
            "propagare": False
        }
    }
}
# CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(" ")
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
