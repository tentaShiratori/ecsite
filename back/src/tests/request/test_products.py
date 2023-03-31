from django.test import TestCase
from src.models import Product, User
from rest_framework.test import APIClient
import json
import shutil
from django.test import override_settings
