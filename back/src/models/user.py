from django.db import models


class User(models.Model):
    firstname = models.CharField(blank=False, max_length=200)
    lastname = models.CharField(blank=False, max_length=200)
    email = models.CharField(blank=False, max_length=200)
    password = models.CharField(blank=False, max_length=200)
    image = models.CharField(blank=False, max_length=200)
