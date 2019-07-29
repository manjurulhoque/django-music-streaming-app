from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('register', register, name='register'),
]
