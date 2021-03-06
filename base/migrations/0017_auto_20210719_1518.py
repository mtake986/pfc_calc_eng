# Generated by Django 3.1.7 on 2021-07-19 06:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_favorite_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='carb',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='carb'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='category',
            field=models.CharField(choices=[('朝食', '朝食'), ('昼食', '昼食'), ('夕食', '夕食'), ('間食', '間食')], max_length=200, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='fat',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='fat'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='kcal',
            field=models.PositiveSmallIntegerField(verbose_name='kcal'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)], verbose_name='protein'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
