# Generated by Django 2.0.4 on 2018-05-07 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prmanage', '0007_auto_20180507_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 20, 54, 57, 181214)),
        ),
        migrations.AlterUniqueTogether(
            name='employeetask',
            unique_together={('task_id', 'employee_id')},
        ),
    ]
