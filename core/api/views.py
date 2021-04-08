from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Song
from .serializers import SongSerializer, ArtistSerializer, GenreSerializer


class HomeViewAPI(APIView):
    def get(self, request, format=None):
        song_queryset = Song.objects.all()
        serializer = SongSerializer(data=song_queryset, many=True, context={'request': request})
        serializer.is_valid()

        return Response({'songs': serializer.data})


class SongsByGenreListAPIView(ListAPIView):
    serializer_class = SongSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        try:
            genre_id = self.kwargs
            return self.model.objects.filter(genre_id=genre_id).order_by('-created_at')
        except:
            return self.model.objects.all().order_by('-created_at')


class ArtistListAPIView(ListAPIView):
    serializer_class = ArtistSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class GenreListAPIView(ListAPIView):
    serializer_class = ArtistSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
