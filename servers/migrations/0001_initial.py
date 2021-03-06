# Generated by Django 2.0.5 on 2018-05-28 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('keys', '0001_initial'),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('host_name', models.CharField(max_length=50)),
                ('current_map', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='maps.Map')),
                ('key', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='keys.Key')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='server',
            unique_together={('key',)},
        ),
    ]
