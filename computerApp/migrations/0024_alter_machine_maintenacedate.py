# Generated by Django 4.0.3 on 2022-05-30 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0023_alter_machine_maintenacedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 30, 10, 2, 50, 359548)),
        ),
    ]
