# Generated by Django 5.0.6 on 2024-06-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_review_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
