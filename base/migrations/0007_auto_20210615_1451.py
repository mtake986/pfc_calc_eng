# Generated by Django 3.1.7 on 2021-06-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210615_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='eaten_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
