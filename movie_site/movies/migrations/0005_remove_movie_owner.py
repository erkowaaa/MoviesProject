# Generated by Django 5.1 on 2024-08-25 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_country_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='owner',
        ),
    ]
