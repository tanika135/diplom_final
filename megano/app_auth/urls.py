from django.urls import path, include
from app_auth import views

app_name = 'app_auth'

urlpatterns = [
    path('sign-in', views.signIn),
    path('sign-up', views.signUp),
    path('sign-out', views.signOut),
]