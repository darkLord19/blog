# Generated by Django 2.1.7 on 2019-06-01 16:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190601_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 31, 59, 904164, tzinfo=utc)),
        ),
    ]
