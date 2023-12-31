from django.urls import path, include

from .views import (
    categories,
    catalog,
    product,
    product_reviews,
    tags,
    products_popular,
    products_limited,
    banners,
    sales,
)


app_name = 'app_catalog'

urlpatterns = [
    path('categories', categories, name='categories'),
    path('catalog', catalog, name='catalog'),
    path('product/<int:id>', product, name='product'),
    path('product/<int:id>/reviews', product_reviews, name='product_reviews'),
    path('tags', tags, name='tags'),
    path('products/popular', products_popular, name='products_popular'),
    path('products/limited', products_limited, name='products_limited'),
    path('banners', banners, name='banners'),
    path('sales', sales, name='sales'),
]
