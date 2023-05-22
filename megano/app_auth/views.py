from typing import Callable

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import json
from django.contrib.auth import authenticate, login, logout





def signIn(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)


def signUp(request):
    # def get(self, request: HttpRequest) -> Callable:
    #     form = RegisterForm()
    #     return render(request, 'account/signup.html', context={'form': form})
    #
    # def post(self, request: HttpRequest) -> Callable:
    #     """
    #     Метод переопределен для слияния анонимной корзины
    #     с корзиной аутентифицированного пользователя
    #     """
    #     form = RegisterForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         # old_cart = CartService(self.request)
    #         user = form.save()
    #         reset_phone_format(instance=user)
    #         login(request, get_auth_user(data=form.cleaned_data))
    #         # new_cart = CartService(self.request)
    #         # new_cart.merge_carts(old_cart)
    #         return redirect('/')
    #     return render(request, 'account/signup.html', context={'form': form})

    return HttpResponse(status=200)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)
