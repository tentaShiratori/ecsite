import environ
import os

ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (hokan_api_v3/hokan_api_v3/settings/__init__.py - 3 = suitebook/)

# Load operating system environment variables and then prepare to use them
env = environ.Env()
env.read_env(".env")

from .base import *

if env("APP_ENV") == "production":
    from .production import *

elif env("APP_ENV") == "development":
    from .development import *
