from django.urls import path, include

from .views import (
    categories,
    catalog,
)


app_name = 'app_catalog'

urlpatterns = [
    path('categories', categories, name='categories'),
    path('catalog', catalog, name='catalog'),

]
