# Generated by Django 2.0.5 on 2018-05-24 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('first_used', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('last_used', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='ip',
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='player',
            field=models.ManyToManyField(to='players.Player'),
        ),
    ]