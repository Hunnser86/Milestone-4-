# Generated by Django 3.2 on 2022-04-19 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0009_music'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='image_url',
            new_name='url',
        ),
    ]
