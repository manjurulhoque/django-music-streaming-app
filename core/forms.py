from django import forms

from .models import *


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("title", "description", "type", "genre", "thumbnail", "song")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SongUploadForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        return self.user


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ("song",)

    def clean_song(self):
        pass
