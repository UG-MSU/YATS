from django.contrib import admin
from django.urls import path, include
from contest.api import views

urlpatterns = [
    path("create-contest/", views.CreateContestAPIView.as_view()),
    path("user-contests/", views.ContestAPIView.as_view()),
    path("contest-tasks/", views.TaskAPIView.as_view()),
    path("has-permission-to-create-contest/", views.HasPermissionToCreateContestAPIEView.as_view()),
]