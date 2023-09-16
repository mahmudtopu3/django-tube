# Generated by Django 4.2.5 on 2023-09-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_rename_is_processed_video_is_running_video_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails'),
        ),
    ]
