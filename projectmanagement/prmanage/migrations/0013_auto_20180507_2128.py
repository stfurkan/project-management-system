# Generated by Django 2.0.4 on 2018-05-07 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prmanage', '0012_auto_20180507_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 21, 28, 37, 786562)),
        ),
    ]