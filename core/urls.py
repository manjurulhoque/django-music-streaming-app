from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [
    path('', home, name='home'),
    path('artists', ArtistListView.as_view(), name='artists'),
    path('artists/<slug:slug>', ArtistDetailView.as_view(), name='artist-details'),
    path('genres', GenreListView.as_view(), name='genres'),
    path('genres/<int:pk>', SongsByGenreListView.as_view(), name='songs-by-genre'),
    path('songs/', include([
        path('make-favorite', favoriteunfavorite, name='song-favorite'),
        path('upload', SongUploadView.as_view(), name='upload'),
        path('<slug:audio_id>', SongDetailsView.as_view(), name='upload-details'),
    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
