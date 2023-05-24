# Generated by Django 4.2.1 on 2023-05-24 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0008_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='app_auth.avatar'),
        ),
    ]
