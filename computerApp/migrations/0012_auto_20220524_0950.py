# Generated by Django 2.2.25 on 2022-05-24 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0011_auto_20220524_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 24, 9, 50, 32, 857154)),
        ),
    ]
