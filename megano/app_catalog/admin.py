from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from app_catalog.models import Product, Category, Images, Tag, ProductReviews


class ImageInline(admin.TabularInline):
    fk_name = 'product'
    model = Images


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'price']
    inlines = [ImageInline, ]


class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'text', 'rate', 'date', 'product']


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(Category, CategoryAdmin)
