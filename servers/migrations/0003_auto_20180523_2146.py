# Generated by Django 2.0.5 on 2018-05-24 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20180523_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='keys.Key'),
        ),
    ]
