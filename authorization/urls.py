from django.contrib import admin
from django.urls import include, path
import authorization.api.views as views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("sign-in", views.AuthUserAPIView.as_view(), name="login"),
    path("sign-up", views.RegUserAPIView.as_view(), name="reg"),
    path("role", views.RoleUserAPIView.as_view(), name="role"),
    path("update", views.UpdateUserAPIView.as_view(), name="update"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("", views.show),
]
