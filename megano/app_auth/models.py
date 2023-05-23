from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def profile_avatar_dir_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatars/{filename}".format(
        pk=instance.pk,
        filename=filename
    )


class Avatar(models.Model):
    avatar = models.ImageField(upload_to=profile_avatar_dir_path, null=True, max_length=255)


class Profile(models.Model):
    class Meta:
        ordering = ['user']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    phone_number = PhoneNumberField(unique=True, default='')
    email = models.CharField(max_length=100, unique=True, default='')
    # avatar = models.ImageField(null=True, blank=True, upload_to=profile_avatar_dir_path)
    avatar = models.OneToOneField(Avatar, on_delete=models.CASCADE)




