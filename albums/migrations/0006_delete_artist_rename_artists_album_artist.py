# Generated by Django 4.0.6 on 2022-07-06 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_remove_album_artists_album_artists'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artists',
            new_name='artist',
        ),
    ]
