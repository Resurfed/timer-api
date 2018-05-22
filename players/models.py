from django.db import models
from django.utils.timezone import now


class Player(models.Model):

    """ Map model """
    name = models.CharField(max_length=50)
    auth = models.CharField(unique=True, max_length=64)
    ip = models.GenericIPAddressField()
    last_login = models.DateTimeField(default=now, blank=True)
    first_login = models.DateTimeField(default=now, blank=True)
    connections = models.IntegerField(blank=True, default=0)
    hours_played = models.FloatField(blank=True, null=True)
