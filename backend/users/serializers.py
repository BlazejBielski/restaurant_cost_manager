from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password", "username")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "username": {"read_only": True},
        }
