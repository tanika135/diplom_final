# Generated by Django 4.2.1 on 2023-06-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0030_alter_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.BooleanField(default=False),
        ),
    ]
