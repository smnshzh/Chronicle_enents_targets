# Generated by Django 3.2.8 on 2022-07-23 16:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='کد')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'مرکز',
                'verbose_name_plural': 'مراکز',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add_visitors_target_without_center_target', models.BooleanField(verbose_name='امکان اضافه کردن اهداف ویزیتورها بدون هدف مرکز')),
            ],
        ),
        migrations.CreateModel(
            name='MessageError',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 23, 21, 4, 22, 679077))),
                ('message', models.TextField(max_length=5000)),
                ('description', models.TextField(blank=True, null=True)),
                ('inprocess', models.BooleanField(default=False)),
                ('processed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='عنوان')),
                ('recordDate', django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 23, 21, 4, 22, 676079), verbose_name='زمان ذخیره')),
                ('eventDate', django_jalali.db.models.jDateTimeField(verbose_name='زمان واقعه')),
                ('description', models.TextField(verbose_name='شرح واقعه تاثیر پذیر')),
                ('description2', models.TextField(blank=True, null=True, verbose_name='شرح واقعه گذار')),
                ('firstAccept', models.BooleanField(default=False, verbose_name='تایید اولیه')),
                ('secendAccept', models.BooleanField(default=False, verbose_name='تایید دوم')),
                ('affected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.center', verbose_name='واحد تاثیر گذار')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('effected', models.ManyToManyField(related_name='effected', to='events.Center', verbose_name='واحدهای تاثیر پذیر')),
            ],
            options={
                'verbose_name': 'واقعه',
                'verbose_name_plural': ' وقایع',
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isManager', models.BooleanField(default=False)),
                ('affect', models.ManyToManyField(to='events.Center', verbose_name='مراکز تاثیر پذیر زیر مجموعه')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='MANAGER', to=settings.AUTH_USER_MODEL, verbose_name='نام مدیر')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربر')),
            ],
        ),
    ]
