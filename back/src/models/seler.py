from django.db import models


class Seler(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.CharField(blank=False, max_length=200)
    password = models.CharField(blank=False, max_length=200)
