from django import forms
from django.core.files.images import get_image_dimensions

from .models import Avatar


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = "avatar",

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

        except AttributeError:
            pass

        return avatar
