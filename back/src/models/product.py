from django.db import models


class Product(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    image = models.ImageField(blank=False, upload_to="images")
    price = models.FloatField(blank=False)
