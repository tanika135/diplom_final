# Generated by Django 4.2.1 on 2023-05-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fullDescription',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
