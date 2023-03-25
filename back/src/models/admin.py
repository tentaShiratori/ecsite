from django.db import models


class Admin(models.Model):
    email = models.CharField(blank=False, max_length=200)
    password = models.CharField(blank=False, max_length=200)
