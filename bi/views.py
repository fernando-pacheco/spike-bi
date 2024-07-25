from django.shortcuts import render
from rest_framework import viewsets
from .models import FakeUser
from .serializers import FakeUserSerializer


class FakeUserViewSet(viewsets.ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer