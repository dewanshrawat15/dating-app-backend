# Generated by Django 3.1.5 on 2021-01-30 20:06

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210130_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphoto',
            name='photo',
            field=models.FileField(max_length=1024, upload_to=photos.models.user_directory_path),
        ),
    ]