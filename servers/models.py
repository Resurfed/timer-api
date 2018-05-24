from django.db import models
from keys.models import Key
import uuid


class Server(models.Model):
    """ Server model """
    key = models.OneToOneField(Key, on_delete=models.DO_NOTHING)  # IP is unreliable as key
    ip = models.GenericIPAddressField()  # this should be the external IP and not dynamically updated
    host_name = models.CharField(max_length=50)
    current_map = models.ForeignKey('maps.Map', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('key'),)
