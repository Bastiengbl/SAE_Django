# Generated by Django 4.0.3 on 2022-06-13 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0027_alter_machine_maintenacedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 8, 44, 39, 126402)),
        ),
    ]
