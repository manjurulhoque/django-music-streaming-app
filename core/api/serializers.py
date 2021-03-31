from rest_framework import serializers

from core.models import Song, Artist, Genre


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Song
        fields = "__all__"
