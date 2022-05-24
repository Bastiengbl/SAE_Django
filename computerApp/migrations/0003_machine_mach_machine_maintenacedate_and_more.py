# Generated by Django 4.0.3 on 2022-05-05 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0002_personnel'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'Mac - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintain and connect servers')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenaceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 8, 21, 6, 166728)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='num_secu',
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
    ]
