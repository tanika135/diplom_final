from django.urls import path, include
# from app_auth import views

from .views import (
    sign_in,
    sign_up,
    sign_out,
    profile,
    profile_password,
    profile_avatar,
)


app_name = 'app_auth'

urlpatterns = [
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('sign-out', sign_out, name='sign-out'),
    path('profile', profile, name='profile'),
    path('profile/password', profile_password, name='profile-password'),
    path('profile/avatar', profile_avatar, name='profile-password'),
]
