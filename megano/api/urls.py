from django.urls import path
from api import views

urlpatterns = [
    path('banners', views.banners),
    path('categories', views.categories),
    path('catalog', views.catalog),
    path('products/popular', views.productsPopular),
    path('products/limited', views.productsLimited),
    path('sales', views.sales),
    path('basket', views.basket),
    path('orders', views.orders),
    path('product/<int:id>', views.product),
    path('product/<int:id>/reviews', views.productReviews),
    path('tags', views.tags),
    path('profile', views.profile),
    path('profile/password', views.profilePassword),
    path('order/<int:id>', views.order),
    path('payment/<int:id>', views.payment),
]
