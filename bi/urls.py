from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FakeUserViewSet


router = DefaultRouter()
router.register(r'fake-user', FakeUserViewSet, basename='fake-user')

urlpatterns = [
    path('', include(router.urls))
]
