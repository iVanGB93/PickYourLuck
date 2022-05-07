# Generated by Django 4.0.4 on 2022-05-06 19:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_player_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('strike', models.PositiveIntegerField()),
                ('box', models.PositiveIntegerField()),
                ('bola', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='dealer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.dealer'),
            preserve_default=False,
        ),
    ]