# Generated by Django 4.2.1 on 2023-05-23 14:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0002_remove_profile_agreement_accepted_remove_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
