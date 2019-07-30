from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('songs/upload', SongUploadView.as_view(), name='upload'),
]
