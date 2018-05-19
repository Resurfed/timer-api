from django.db import models


class Map(models.Model):
    """ Map model """
    name = models.CharField(unique=True, max_length=50)
    author = models.ForeignKey(
        'Maps.Author',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )


class Course(models.Model):
    """ Course model """
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    author = models.ForeignKey(
        'Maps.Author',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    # Stages are a superset of default functionality.
    staged = models.BooleanField()
    checkpoints = models.SmallIntegerField()
    difficulty = models.SmallIntegerField(blank=True, default=0)


class Author(models.Model):
    """ Course Author model """
    name = models.CharField(unique=True, max_length=50)

    player = models.ForeignKey(
        'players.Player',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Zone(models.Model):
    """ Zone model """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    end_x = models.FloatField()
    end_y = models.FloatField()
    end_z = models.FloatField()
