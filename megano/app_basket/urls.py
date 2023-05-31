from django.urls import path
from .views import (
    basket,
)

urlpatterns = [
    path('basket', basket),
]
