# Generated by Django 3.1.5 on 2021-01-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0002_auto_20210105_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Movie Title'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='synopsis',
            field=models.TextField(verbose_name='Synopsis'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(verbose_name='User Review'),
        ),
    ]