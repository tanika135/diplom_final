# Generated by Django 4.2.1 on 2023-05-23 20:09

import app_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0004_remove_profile_phone_remove_profile_preview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=app_auth.models.profile_avatar_dir_path),
        ),
    ]
