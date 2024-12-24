# Generated by Django 4.2 on 2024-12-24 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2024, 12, 24, 7, 5, 11, 917877, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
