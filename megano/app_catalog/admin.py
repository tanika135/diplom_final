from django.contrib import admin
from app_catalog.models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'price']


admin.site.register(Product, ProductsAdmin)

