from django.db import models

from app_catalog.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    cart_id = models.CharField(max_length=100, blank=False, null=False)
