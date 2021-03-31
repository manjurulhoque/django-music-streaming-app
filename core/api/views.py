from rest_framework.generics import ListAPIView
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


class ArtistListAPIView(ListAPIView):
    serializer_class = ArtistSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class GenreListAPIView(ListAPIView):
    serializer_class = ArtistSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
