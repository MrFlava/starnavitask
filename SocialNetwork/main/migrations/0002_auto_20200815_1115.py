# Generated by Django 3.1 on 2020-08-15 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 11, 15, 16, 545356), verbose_name='date published'),
        ),
    ]
