from django.urls import path, re_path

from . import views

app_name = 'users'

urlpatterns = [
    path('users/', views.CustomUserView.as_view(), name='user-list-create'),
    re_path(r'^users/(?P<pk>[0-9a-f-]+)/$', views.CustomUserView.as_view(), name='user-detail-update-delete'),
]
