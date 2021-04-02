import os

from celery import current_app
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from utils.song_utils import generate_key
from .forms import *
from tinytag import TinyTag
from .tasks import download_audio_from_youtube


def home(request):
    context = {
        'artists': Artist.objects.all(),
        'genres': Genre.objects.all()[:6],
        'latest_songs': Song.objects.exclude(song__isnull=True)[:6]
    }
    return render(request, "home.html", context)


class SongUploadView(CreateView):
    form_class = SongUploadForm
    template_name = "songs/create.html"

    @method_decorator(login_required(login_url=reverse_lazy('core:home')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SongUploadView, self).get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        context['genres'] = Genre.objects.all()
        return context

    def get_form_kwargs(self):
        kwargs = super(SongUploadView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=200)

    def form_valid(self, form):
        youtube_url = form.cleaned_data['youtube_url']
        if youtube_url:
            task = download_audio_from_youtube.delay(form.cleaned_data['youtube_url'])
            form.instance.user = self.request.user
            form.save()

            artists = []
            for a in self.request.POST.getlist('artists[]'):
                try:
                    artists.append(int(a))
                except:
                    artist = Artist.objects.create(name=a)
                    artists.append(artist)
            form.instance.artists.set(artists)
            new_song = form.save()
        else:
            task = None
            song = TinyTag.get(self.request.FILES['song'].file.name)
            form.instance.audio_id = generate_key(15, 15)
            form.instance.user = self.request.user
            form.instance.playtime = int(song.duration)
            form.instance.size = song.filesize

            artists = []
            for a in self.request.POST.getlist('artists[]'):
                try:
                    artists.append(int(a))
                except:
                    artist = Artist.objects.create(name=a)
                    artists.append(artist)
            form.save()
            form.instance.artists.set(artists)
            new_song = form.save()

        data = {
            'status': True,
            'song_id': new_song.id,
            'task_id': task.id if task else None,
            'task_status': task.status if task else None,
            'message': "Successfully submitted form data.",
            'redirect': reverse_lazy('core:upload-details', kwargs={'audio_id': form.instance.audio_id})
        }
        return JsonResponse(data)


class TaskView(View):
    def get(self, request, task_id, song_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            print(task.get())
            title, url, size, description = task.get()
            response_data['title'] = title
            response_data['url'] = url
            response_data['size'] = size
            response_data['description'] = description

            song = Song.objects.get(id=song_id)
            try:
                if os.path.isfile(song.song.path):
                    os.remove(song.song.path)
            except Exception as e:
                print(e)
            print(song)

        return JsonResponse(response_data)


class SongDetailsView(DetailView):
    model = Song
    template_name = 'songs/show.html'
    context_object_name = 'song'
    slug_field = 'audio_id'
    slug_url_kwarg = 'audio_id'


class GenreListView(ListView):
    model = Genre
    template_name = 'genres/index.html'
    context_object_name = 'genres'


class SongsByGenreListView(DetailView):
    model = Genre
    template_name = 'genres/songs-by-genre.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super(SongsByGenreListView, self).get_context_data(**kwargs)
        context['songs'] = self.get_object().song_set.all
        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/index.html'
    context_object_name = 'artists'


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artists/show.html'
    context_object_name = 'artist'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['songs'] = self.get_object().songs.all()
        return context


class FavoriteCreateView(CreateView):
    form_class = FavoriteForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FavoriteCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {
                'status': True,
                'message': "Please login first",
                'redirect': None
            }
            return JsonResponse(data=data)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def favoriteunfavorite(request):
    if request.method == "POST":
        if request.POST.get('decision') == 'make':
            song = Song.objects.get(id=request.POST.get('song_id'))
            if not Favorite.objects.filter(user=request.user, song=song).exists():
                Favorite.objects.create(user=request.user, song=song)
                data = {
                    'status': True,
                    'message': "Song marked as favorite",
                    'redirect': None
                }
                return JsonResponse(data)
            else:
                data = {
                    'status': True,
                    'message': "Already favorite",
                    'redirect': None
                }

                return JsonResponse(data)
        else:
            song = Song.objects.get(id=request.POST.get('song_id'))
            Favorite.objects.filter(user=request.user, song=song).delete()
            data = {
                'status': True,
                'message': "Song unfavorited",
                'redirect': None
            }
            return JsonResponse(data)
    else:
        data = {
            'status': False,
            'message': "Method not allowed",
            'redirect': None
        }

        return JsonResponse(data)


class UnFavoriteView(DeleteView):
    model = Favorite

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        data = {
            'status': True,
            'message': "Song unfavorited.",
            'redirect': None
        }

        return JsonResponse(data)
