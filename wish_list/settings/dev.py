from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

from .default import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = "test_secret"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_wish_list",
        "USER": "test_user",
        "PASSWORD": "test1",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
INSTALLED_APPS.append("django_extensions")

STATIC_ROOT = BASE_DIR / "static/"
