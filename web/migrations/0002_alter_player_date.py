# Generated by Django 4.0.4 on 2022-05-06 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]