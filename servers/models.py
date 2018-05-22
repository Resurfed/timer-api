from django.db import models


class Server(models.Model):
    """ Server model """
    token = models.CharField(50)  # docker makes IP an unreliable unique key
    ip = models.IPAddressField()
    host_name = models.CharField(50)
    current_map = models.ForeignKey('maps.Map', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('token'),)
