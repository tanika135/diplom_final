from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from app_catalog.models import Product


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    phone = PhoneNumberField(unique=False, default='')


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
