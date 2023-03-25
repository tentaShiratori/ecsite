import os

SECRET_KEY = "django-insecure-x=vp85446@^np0s@k!h3_cw_nc-5qa8)j99+5^^@p(jb0ecgum"

DEBUG = True

ALLOWED_HOSTS = ["10.0.2.2", "localhost", "127.0.0.1"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}
