from django.db import models
from .user import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    image = models.CharField(blank=False, max_length=200)
    price = models.FloatField()
