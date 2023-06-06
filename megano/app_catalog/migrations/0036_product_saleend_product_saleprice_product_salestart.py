# Generated by Django 4.2.1 on 2023-06-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0035_alter_sales_datefrom_alter_sales_dateto'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='saleEnd',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='salePrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='saleStart',
            field=models.DateTimeField(null=True),
        ),
    ]