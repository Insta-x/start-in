# Generated by Django 4.1 on 2022-10-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='current_donation',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
