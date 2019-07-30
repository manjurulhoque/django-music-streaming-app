from django.db import models
from django.template.defaultfilters import slugify
from django.utils.datetime_safe import time

from accounts.models import User


class Artist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="genres", default="default.jpeg")


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_id = models.TextField()
    title = models.CharField(max_length=200, verbose_name="Song name")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False)
    audio_location = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    artists = models.ManyToManyField(Artist)
    size = models.IntegerField(default=0)
    playtime = models.CharField(max_length=10, default="0.00")
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=time)
