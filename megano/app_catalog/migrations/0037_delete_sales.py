# Generated by Django 4.2.1 on 2023-06-06 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0036_product_saleend_product_saleprice_product_salestart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
