# Generated by Django 3.2.8 on 2022-07-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.FloatField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MainGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('maingroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.maingroup')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code1', models.BigIntegerField(unique=True)),
                ('code2', models.BigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('weight', models.BigIntegerField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('lenght', models.FloatField()),
                ('inBox', models.FloatField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productgroup')),
            ],
        ),
    ]