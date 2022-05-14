# Generated by Django 3.1.7 on 2021-06-25 06:56

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20210620_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='eaten_date',
            field=models.DateField(default=datetime.date.today, help_text='※yyyy-mm-dd', verbose_name='食べた日付'),
        ),
        migrations.AlterField(
            model_name='target',
            name='carb',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='炭水化物'),
        ),
        migrations.AlterField(
            model_name='target',
            name='fat',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='脂質'),
        ),
        migrations.AlterField(
            model_name='target',
            name='protein',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='タンパク質'),
        ),
    ]