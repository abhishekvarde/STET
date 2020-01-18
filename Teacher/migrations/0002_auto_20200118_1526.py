# Generated by Django 2.2.7 on 2020-01-18 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='no_of_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(default='1234', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_generated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 18, 15, 26, 31, 332981)),
        ),
    ]