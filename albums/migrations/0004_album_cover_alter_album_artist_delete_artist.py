# Generated by Django 4.0.5 on 2022-07-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_remove_album_artist_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=300),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]