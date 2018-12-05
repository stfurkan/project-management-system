# Generated by Django 2.0.4 on 2018-05-07 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prmanage', '0010_auto_20180507_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 20, 56, 27, 505980)),
        ),
        migrations.AlterUniqueTogether(
            name='employeetask',
            unique_together={('task_id', 'employee_id')},
        ),
    ]