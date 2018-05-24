from django.db import models
import uuid


class Key(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    level = models.IntegerField()
    description = models.CharField(max_length=1000)
