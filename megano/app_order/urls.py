from django.urls import path
from .views import (
    orders,
    order,
    payment,
)

urlpatterns = [
    path('orders', orders),
    path('order/<int:id>', order),
    path('payment/<int:id>', payment),
]
