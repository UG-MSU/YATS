from django.contrib import admin
from django.urls import include, path
import authorization.api.views as views

urlpatterns = [
    path("sign-in", views.AuthUserAPIView.as_view(), name="login"),
    path("sign-up", views.RegUserAPIView.as_view(), name="reg"),
    path("role", views.RoleUserAPIView.as_view(), name="role"),
    path("update", views.UpdateUserAPIView.as_view(), name="update"),
    path("", views.show),
]
