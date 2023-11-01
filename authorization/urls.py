from django.contrib import admin
from django.urls import include, path
from authorization.api.views import show, UserAPIView

urlpatterns = [
    path('sign-in', UserAPIView.as_view(), name='login'),
    path('', show),
]
