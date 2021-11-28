# Generated by Django 3.2.8 on 2021-11-25 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0003_auto_20211125_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='setvisitortarget',
            options={'verbose_name': 'تعریف هدف', 'verbose_name_plural': 'تعریف اهداف'},
        ),
        migrations.AlterModelOptions(
            name='superviser',
            options={'verbose_name': 'سرپرست', 'verbose_name_plural': 'سرپرست ها'},
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'verbose_name': 'فروشنده', 'verbose_name_plural': 'فروشندگان'},
        ),
        migrations.AlterField(
            model_name='superviser',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
