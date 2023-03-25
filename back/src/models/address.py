from django.db import models
from .user import User


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    zipcode1 = models.CharField(blank=False, max_length=200)
    zipcode2 = models.CharField(blank=False, max_length=200)
    address1 = models.CharField(blank=False, max_length=200)
    address2 = models.CharField(blank=False, max_length=200)
