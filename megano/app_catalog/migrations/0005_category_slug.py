# Generated by Django 4.2.1 on 2023-05-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0004_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]