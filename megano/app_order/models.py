from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from app_catalog.models import Product


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    phone = PhoneNumberField(unique=False, default='')

    ORDINARY = 'ORD'
    EXPRESS = 'EXP'

    DELIVERY_TYPE_CHOICES = [
        (ORDINARY, 'ordinary'),
        (EXPRESS, 'express'),
    ]
    delivery_type = models.CharField(max_length=4, choices=DELIVERY_TYPE_CHOICES, default=ORDINARY)

    # FREE = 'FREE'
    # PAID = 'PAID'
    #
    # DELIVERY_TYPE_CHOICES = [
    #     (FREE, 'free'),
    #     (PAID, 'paid'),
    # ]
    # delivery_type = models.CharField(max_length=4, choices=DELIVERY_TYPE_CHOICES, default=FREE)

    ONLINE_CARD = 'OC'
    RANDOM_ACCOUNT = 'RA'

    PAYMENT_TYPE_CHOICES = [
        (ONLINE_CARD, 'online'),
        (RANDOM_ACCOUNT, 'random_account')
    ]
    payment_type = models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES, default=ONLINE_CARD)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.ForeignKey('OrderStatus', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1, null=False)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)


class OrderStatus(models.Model):
    title = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.title
