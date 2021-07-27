from django.contrib.auth.models import User
from rest_framework import serializers

from app.user.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ["id", "viziboll"]
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        #fields = ["id", "viziboll"]
        fields = '__all__'

