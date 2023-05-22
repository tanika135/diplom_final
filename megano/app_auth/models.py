from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Meta:
        ordering = ['user']

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to='profile_preview_directory_path')

