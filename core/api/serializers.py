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
    url = serializers.SerializerMethodField('get_url')
    artist = serializers.SerializerMethodField('get_joined_artist')

    class Meta:
        model = Song
        fields = "__all__"

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.song.url)

    def get_joined_artist(self, obj):
        return ", ".join([a.name for a in obj.artists.all()])


class ArtistSongsSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = "__all__"
