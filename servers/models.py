from django.db import models


class Server(models.Model):
    """ Server model """
    token = models.CharField(max_length=50)  # IP is unreliable as key
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    host_name = models.CharField(max_length=50)
    current_map = models.ForeignKey('maps.Map', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('token'),)
