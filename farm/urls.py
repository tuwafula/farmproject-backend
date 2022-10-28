from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('services/', include('services.urls')),
    path('user-profile/', include("userprofile.urls")),
    path('auth/', include('djoser.urls.jwt')),
]
