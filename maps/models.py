from django.db import models


class Author(models.Model):
    """ Course Author model """
    name = models.CharField(unique=True, max_length=50)

    player = models.ForeignKey(
        'players.Player',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Priority(models.Model):
    """ Priority model """
    name = models.CharField(max_length=30)


class Map(models.Model):
    """ Map model """
    name = models.CharField(unique=True, max_length=50)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True, null=True
    ),
    last_played = models.DateTimeField(),
    added = models.DateTimeField(),
    hours_played = models.FloatField()


class Course(models.Model):
    """ Course model """
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    checkpoints = models.SmallIntegerField()
    difficulty = models.SmallIntegerField(blank=True, default=0)

    priority = models.ForeignKey(
        Priority,
        models.DO_NOTHING,
        blank=True,
        null=True
    )

    BEHAVIOR_CHOICES = (('N', "None"), ('S', "Staged"), ('L', "Linear"))

    behavior = models.CharField(
        max_length=1,
        blank=True,
        choices=BEHAVIOR_CHOICES,
        default='N'
    )


class Zone(models.Model):
    """ Zone model """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.CharField(max_length=60)
    end = models.CharField(max_length=60)
