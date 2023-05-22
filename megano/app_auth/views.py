from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
import json
from django.contrib.auth import authenticate, login, logout
from .models import Profile


def sign_in(request):
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


def sign_up(request):
    if request.method == "POST":
        body = json.loads(request.body)
        name = body['name']
        username = body['username']
        password = body['password']

        if len(name) > 3 and len(username) > 3 and len(password) > 3:
            user = User.objects.create_user(username, "", password)
            if user is not None:
                profile = Profile.objects.create(user=user, name=name)
                if profile:
                    login(request, user)
                    return HttpResponse(status=200)

        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def sign_out(request):
    logout(request)
    return HttpResponse(status=200)
