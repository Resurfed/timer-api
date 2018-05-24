from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    """ Course Author model """
    name = models.CharField(unique=True, max_length=50)

    player = models.ForeignKey(
        'players.Player',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Priority(models.Model):
    """ Priority model """
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Behavior(models.Model):
    """ Behavior model """
    name = models.CharField(unique=True, max_length=30)
    staged = models.BooleanField()

    PREHOP_CHOICES = (
        ('NO', "None"),
        ('SP', "Spawns"),
        ('FS', "First Spawn"),
        ('GL', "Global")
    )

    prehop = models.CharField(
        max_length=2,
        choices=PREHOP_CHOICES,
        blank=True,
        default='NO'
    )

    def __str__(self):
        return self.name


class Map(models.Model):
    """ Map model """
    name = models.CharField(unique=True, max_length=50)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    last_played = models.DateTimeField(default=now, blank=True)
    added = models.DateTimeField(default=now, blank=True)
    hours_played = models.FloatField()

    def __str__(self):
        return self.name


class Course(models.Model):
    """ Course model """
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    difficulty = models.SmallIntegerField(blank=True, default=0)
    checkpoints = models.SmallIntegerField()

    priority = models.ForeignKey(
        Priority,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    behavior = models.ForeignKey(
        Behavior,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    def __str__(self):
        return "{} course {}".format(self.map, self.pk)


class Zone(models.Model):
    """ Zone model """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.CharField(max_length=60)
    end = models.CharField(max_length=60)

    def __str__(self):
        return "{} [{}], [{}]".format(self.course, self.start, self.end)
