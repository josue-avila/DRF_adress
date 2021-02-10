from django.urls import include,path
from rest_framework import routers
from .views import AdressViewSet, AdressApi


router = routers.DefaultRouter()
router.register(r'adress', AdressViewSet, basename='adress')

urlpatterns = [
    path('', include(router.urls)),
    path('adress/api', AdressApi.as_view()),
    path('api-auth', include(
        'rest_framework.urls', namespace='rest_framework')),
]