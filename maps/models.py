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
    name = models.CharField(max_length=30)


class CourseType(models.Model):
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
        blank=True, null=True
    )

    checkpoints = models.SmallIntegerField()
    difficulty = models.SmallIntegerField(blank=True, default=0)
    course_type = models.ForeignKey(CourseType, on_delete=models.DO_NOTHING)
    priority = models.ForeignKey(Priority, models.DO_NOTHING)


class Zone(models.Model):
    """ Zone model """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_x = models.FloatField()
    start_y = models.FloatField()
    start_z = models.FloatField()
    end_x = models.FloatField()
    end_y = models.FloatField()
    end_z = models.FloatField()
