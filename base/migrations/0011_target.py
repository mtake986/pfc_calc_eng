# Generated by Django 3.1.7 on 2021-06-18 04:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_auto_20210616_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcal', models.PositiveSmallIntegerField()),
                ('protein', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)])),
                ('fat', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)])),
                ('carb', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=4, null=True, validators=[django.core.validators.MaxValueValidator(999.9), django.core.validators.MinValueValidator(0.0)])),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
