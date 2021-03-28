from django.urls import path

from core.api import views

urlpatterns = [
    path('', views.HomeViewAPI.as_view()),
]
