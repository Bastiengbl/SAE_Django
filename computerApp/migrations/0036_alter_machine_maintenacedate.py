# Generated by Django 4.0.3 on 2022-06-13 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0035_alter_machine_maintenacedate_alter_machine_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 11, 52, 55, 13073)),
        ),
    ]
