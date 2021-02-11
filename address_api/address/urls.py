from django.urls import include, path
from rest_framework import routers
from .views import AddressViewSet, AddressApi


router = routers.DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
    path('address/create', AddressApi.as_view()),
    path('api-auth', include(
        'rest_framework.urls', namespace='rest_framework')),
]
