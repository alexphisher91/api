from django.db import models
from base.models import Uuid


class Product(Uuid):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
