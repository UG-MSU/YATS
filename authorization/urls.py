from django.contrib import admin
from django.urls import include, path
import authorization.api.views as views

urlpatterns = [
    path('sign-in', views.AuthUserAPIView.as_view(), name='login'),
    path('', views.show),
]
