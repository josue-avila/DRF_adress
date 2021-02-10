
from django.contrib import admin
from django.urls import path, include
from .views import AdressApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drf_adress.adress.urls')),
]
