# Generated by Django 3.0.1 on 2020-01-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0002_auto_20200116_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration_form',
            name='pin_code',
            field=models.CharField(default='', max_length=20),
        ),
    ]