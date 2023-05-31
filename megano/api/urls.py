from django.urls import path
from api import views

urlpatterns = [
    path('banners', views.banners),
    path('sales', views.sales),
]
