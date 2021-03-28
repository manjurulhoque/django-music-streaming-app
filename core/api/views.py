from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Song
from .serializers import SongSerializer


class HomeViewAPI(APIView):
    def get(self, request, format=None):
        song_queryset = Song.objects.all()
        serializer = SongSerializer(data=song_queryset, many=True)
        serializer.is_valid()

        return Response({'songs': serializer.data})
