# Generated by Django 4.0.3 on 2022-06-13 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0033_alter_machine_maintenacedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 11, 46, 9, 996408)),
        ),
    ]
