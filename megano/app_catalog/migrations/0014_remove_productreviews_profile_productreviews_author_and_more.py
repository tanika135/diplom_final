# Generated by Django 4.2.1 on 2023-05-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0013_productreviews_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreviews',
            name='profile',
        ),
        migrations.AddField(
            model_name='productreviews',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
    ]