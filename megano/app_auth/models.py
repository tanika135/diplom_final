from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    class Meta:
        ordering = ['user']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    # bio = models.TextField(max_length=500, blank=True)
    # agreement_accepted = models.BooleanField(default=False)
    phone_number = PhoneNumberField(unique=True, default='')#, null=False, blank=False
    email = models.CharField(max_length=100, unique=True, default='')
    preview = models.ImageField(null=True, blank=True, upload_to='profile_preview_directory_path')

