# Generated by Django 4.1 on 2022-10-22 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 22, 15, 48, 12, 904475)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 22, 15, 48, 12, 904475)),
        ),
    ]
