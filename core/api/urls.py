from django.urls import path

from core.api import views

urlpatterns = [
    path('', views.HomeViewAPI.as_view()),
    path('artists', views.ArtistListAPIView.as_view()),
    path('genres', views.GenreListAPIView.as_view()),
    path('genres/<int:pk>/songs', views.SongsByGenreListAPIView.as_view()),
]
