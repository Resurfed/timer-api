from django.db import models


class Time(models.Model):
    time = models.FloatField()
    stage = models.IntegerField()
    course = models.ForeignKey('maps.Course', on_delete=models.CASCADE)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    server = models.ForeignKey('servers.Server', on_delete=models.DO_NOTHING)
    mode = models.SmallIntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    completions = models.IntegerField(blank=True, null=True)
    enter_velocity = models.CharField(max_length=40, blank=True, null=True)
    exit_velocity = models.CharField(max_length=40, blank=True, null=True)
    avg_velocity = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        unique_together = (('course', 'player', 'stage'),)
        index_together = (('course', 'stage'),)


class Checkpoint(models.Model):
    time = models.FloatField()
    stage_time = models.FloatField()
    record = models.ForeignKey(Time, on_delete=models.CASCADE)
    checkpoint = models.IntegerField()
    enter_velocity = models.CharField(max_length=40, blank=True, null=True)
    exit_velocity = models.CharField(max_length=40, blank=True, null=True)
    avg_velocity = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        unique_together = (('record'),)
