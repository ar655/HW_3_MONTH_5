# Generated by Django 4.1.1 on 2022-09-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rename_review1_movie_movie1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie1',
            new_name='movies',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='reviews',
        ),
    ]
