# Generated by Django 4.0.4 on 2022-05-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]