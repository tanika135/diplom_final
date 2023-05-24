from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
import json
from django.contrib.auth import authenticate, login, logout

from .forms import AvatarForm
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


def get_profile(request):
    user = request.user
    if user is None:
        return None

    profile = Profile.objects.get(user=user)
    if not profile:
        return None

    return profile


@login_required(redirect_field_name='next', login_url='/sign-up/')
def profile(request):

    profile = get_profile(request)
    if not profile:
        return HttpResponse(status=400)

    elif request.method == 'GET':

        data = {
            "fullName": profile.name,
            "email": profile.email,
            "phone": profile.phone_number.as_e164,
            "avatar": {
                "src": profile.avatar.avatar.url,
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
                "src": profile.avatar.avatar.url,
                "alt": "hello alt",
            }
        }
        return JsonResponse(data)

    return HttpResponse(status=405)


@login_required(redirect_field_name='next', login_url='/sign-up/')
def profile_password(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        new_password = body['password']
        if new_password:
            user = User.objects.get(id=request.user.id)
            user.set_password(new_password)
            user.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    return HttpResponse(status=405)


@login_required(redirect_field_name='next', login_url='/sign-up/')
def profile_avatar(request):
    profile = get_profile(request)
    if not profile:
        return HttpResponse(status=400)
    elif request.method == 'POST':

        avatar_form = AvatarForm(request.POST, request.FILES)
        if avatar_form.is_valid():
            if profile.avatar:
                profile.avatar.delete()
            profile.avatar = avatar_form.save()
            profile.save()

            data = {
                "src": profile.avatar.avatar.url,
                "alt": profile.name,
            }
            return JsonResponse(data)
        else:
            print(avatar_form.errors)
            return HttpResponse(status=400)

    return HttpResponse(status=405)

