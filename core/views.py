from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .forms import *


def home(request):
    return render(request, "home.html", {})


class SongUploadView(CreateView):
    form_class = SongUploadForm
    template_name = "songs/create.html"

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
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
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        data = {
            'message': "Successfully submitted form data."
        }
        return JsonResponse(data)
