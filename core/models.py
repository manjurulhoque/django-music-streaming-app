import math
from time import strftime, gmtime

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

from accounts.models import User
from utils.song_utils import generate_file_name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="artists", default="artists/default.png")
    bio = models.TextField(verbose_name='Artist Bio', null=True, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="genres", default="genres/default.png")

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)


def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'songs/{0}/{1}'.format(strftime('%Y/%m/%d'), generate_file_name() + '.' + filename.split('.')[-1])


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200, verbose_name="Song name")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False)
    song = models.FileField(upload_to=song_directory_path, max_length=500)
    # audio_location = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    artists = models.ManyToManyField(Artist, related_name='songs')
    size = models.IntegerField(default=0)
    playtime = models.CharField(max_length=10, default="0.00")
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name='Created At', default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def duration(self):
        return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))

    @property
    def file_size(self):
        if self.size == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(self.size, 1024)))
        p = math.pow(1024, i)
        s = round(self.size / p, 2)
        return "%s %s" % (s, size_name[i])
