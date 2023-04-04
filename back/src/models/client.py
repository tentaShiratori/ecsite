from django.db import models
from .user import User


class Client(User):
    first_name = models.CharField(max_length=255)
