from statistics import mode
from django.db import models
import uuid


class Uuid(models.Model):
    uuid = models.UUIDField(primary_key=True, verbose_name='uuid', default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True