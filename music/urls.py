from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),

    # API Urls
    path('v1/api/', include([
        path('', include('core.api.urls')),
        path('accounts/', include('accounts.api.urls')),
    ])),
]
