from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('users/', views.CreateCustomUserView.as_view(), name='create-user'),
    path('users/<int:pk>', views.UserUpdateAPIView.as_view(), name='update-user'),
    path('users/<int:pk>', views.GetCustomUserView.as_view(), name='retrieve-user'),
]
