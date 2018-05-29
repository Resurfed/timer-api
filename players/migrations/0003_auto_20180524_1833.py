# Generated by Django 2.0.5 on 2018-05-24 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20180523_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipaddress',
            name='player',
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='player',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ip_addresses', to='players.Player'),
            preserve_default=False,
        ),
    ]