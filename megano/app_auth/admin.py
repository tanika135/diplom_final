from django.contrib import admin

from app_auth.models import Profile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Profile, ProfilesAdmin)
