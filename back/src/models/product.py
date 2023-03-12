from django.db import models
class Product(models.Model):
    question_text = models.CharField(max_length=200)

