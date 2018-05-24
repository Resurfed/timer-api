# Generated by Django 2.0.5 on 2018-05-23 00:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('auth', models.CharField(max_length=64, unique=True)),
                ('ip', models.GenericIPAddressField()),
                ('last_login', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('first_login', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('connections', models.IntegerField(blank=True, default=0)),
                ('hours_played', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]