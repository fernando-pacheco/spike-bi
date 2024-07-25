from rest_framework import serializers
from .models import FakeUser


class FakeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeUser
        fields = '__all__'