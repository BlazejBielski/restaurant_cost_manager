from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response

from users import serializers
from users.serializers import CustomUserSerializer


class CreateCustomUserView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = serializers.CustomUserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetCustomUserView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
