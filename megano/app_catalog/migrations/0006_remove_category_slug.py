# Generated by Django 4.2.1 on 2023-05-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0005_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]