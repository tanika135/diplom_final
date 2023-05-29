from django.urls import path, include

from .views import (
    categories,
    catalog,
    product,
)


app_name = 'app_catalog'

urlpatterns = [
    path('categories', categories, name='categories'),
    path('catalog', catalog, name='catalog'),
    path('product/<int:id>', product, name='product'),
]
