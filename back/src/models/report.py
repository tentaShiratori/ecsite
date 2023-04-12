from django.db import models

from .cart import Cart
from .product import Product


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    product = models.OneToOneField(Product, null=True, on_delete=models.SET_NULL)
