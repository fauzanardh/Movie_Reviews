# Generated by Django 3.1.5 on 2021-01-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='movies',
            new_name='movie',
        ),
    ]
