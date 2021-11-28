# Generated by Django 3.2.8 on 2021-11-10 17:11

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20211110_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='access',
            name='affect',
        ),
        migrations.AddField(
            model_name='access',
            name='affect',
            field=models.ManyToManyField(to='events.Center'),
        ),
        migrations.AlterField(
            model_name='event',
            name='recordDate',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2021, 11, 10, 20, 41, 38, 446559), verbose_name='زمان ذخیره'),
        ),
    ]
