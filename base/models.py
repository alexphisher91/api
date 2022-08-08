from statistics import mode
from django.contrib.auth import get_user_model
from django.db import models
import uuid


User = get_user_model()


class Uuid(models.Model):
    uuid = models.UUIDField(primary_key=True, verbose_name='uuid', default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Document(Uuid):
    number = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True
