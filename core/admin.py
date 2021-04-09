from django.contrib import admin

from utils.song_utils import generate_key
from .models import *

admin.site.register(Genre)


@admin.register(Song)
class SongModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(SongModelAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['audio_id'].initial = generate_key(15, 20)
        return form


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }
