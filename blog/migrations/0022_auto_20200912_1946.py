# Generated by Django 2.2.13 on 2020-09-12 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200912_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 14, 16, 45, 791416, tzinfo=utc)),
        ),
    ]
