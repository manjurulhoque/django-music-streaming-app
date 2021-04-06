from django import forms

from .models import *


class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("title", "description", "type", "genre", "thumbnail", "song", "youtube_url")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(SongUploadForm, self).__init__(*args, **kwargs)
        self.fields['song'].required = False
        self.fields['description'].required = False
        self.fields['thumbnail'].required = False
        self.fields['title'].required = False
        self.fields['description'].required = False

    def clean_user(self):
        return self.user


class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ("youtube_url",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(YoutubeForm, self).__init__(*args, **kwargs)

    def clean_user(self):
        return self.user


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ("song",)

    def clean_song(self):
        pass
