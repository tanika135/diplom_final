from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
import json
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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


@login_required(redirect_field_name='next', login_url='/sign-up/')
def profile(request):
    user = request.user
    if user is None:
        return HttpResponse(status=401)

    profile = Profile.objects.get(user=user)
    if not profile:
        return HttpResponse(status=400)

    elif request.method == 'GET':

        data = {
            "fullName": profile.name,
            "email": profile.email,
            "phone": profile.phone_number.as_e164,
            "avatar": {
                "src": profile.avatar.url,
                "alt": profile.name,
            }
        }

        return JsonResponse(data)

    elif request.method == 'POST':

        body = json.loads(request.body)
        name = body['fullName']
        email = body['email']
        phone = body['phone']
        profile.name = name
        profile.email = email
        profile.phone_number = phone
        profile.save()

        data = {
            "fullName": profile.name,
            "email": profile.email,
            "phone": profile.phone_number.as_e164,
            "avatar": {
                "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
                "alt": "hello alt",
            }
        }
        return JsonResponse(data)

    return HttpResponse(status=405)


def profile_password(request):
    return HttpResponse(status=200)
