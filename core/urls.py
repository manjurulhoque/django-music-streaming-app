from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('songs/', include([
        path('make-favorite', favoriteunfavorite, name='song-favorite'),
        path('upload', SongUploadView.as_view(), name='upload'),
        path('<slug:audio_id>', SongDetailsView.as_view(), name='upload-details'),
    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
