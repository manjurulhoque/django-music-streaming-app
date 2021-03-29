from django.contrib import admin
from .models import *

admin.site.register(Genre)
admin.site.register(Song)


@admin.register(Artist)
class ArtistModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }
