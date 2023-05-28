from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from app_catalog.models import Product, Category, Images


class ImageInline(admin.TabularInline):
    fk_name = 'product'
    model = Images


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'price']
    inlines = [ImageInline,]


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
