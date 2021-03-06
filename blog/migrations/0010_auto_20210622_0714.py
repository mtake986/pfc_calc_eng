# Generated by Django 3.1.7 on 2021-06-21 22:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210620_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='content_1',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='コンテンツ1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='content_2',
            field=models.TextField(blank=True, null=True, verbose_name='コンテンツ2'),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_3',
            field=models.TextField(blank=True, null=True, verbose_name='コンテンツ3'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='link_1',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='参考文献リンク1'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='link_2',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='参考文献リンク2'),
        ),
    ]
