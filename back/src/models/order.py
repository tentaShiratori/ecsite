from django.db import models
from .product import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=200)
    price = models.FloatField()
