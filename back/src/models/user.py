from django.db import models
from polymorphic.models import PolymorphicModel


class User(PolymorphicModel):
    sub = models.CharField(blank=False, max_length=36, primary_key=True)
    email = models.CharField(blank=False, max_length=255, unique=True)
