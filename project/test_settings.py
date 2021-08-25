import os
from project.settings import *  # noqa: F401, F403

SECRET_KEY = os.getenv("TEST_SECRET")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test_db",
    }
}
