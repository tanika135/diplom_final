# Generated by Django 4.2.1 on 2023-06-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0033_sales_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product',
        ),
    ]
