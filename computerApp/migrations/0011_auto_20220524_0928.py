# Generated by Django 2.2.25 on 2022-05-24 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0010_alter_machine_maintenacedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 24, 9, 28, 47, 452200)),
        ),
    ]
