from django.db import models

from .user import User


class Seler(User):
    name = models.CharField(blank=False, max_length=200)
