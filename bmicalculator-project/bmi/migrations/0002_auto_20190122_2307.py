# Generated by Django 2.1.3 on 2019-01-22 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmimeasurement',
            name='measured_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
