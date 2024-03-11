from django.contrib import admin
from django.urls import path, include
from contest.api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create-contest/", views.CreateContestAPIView.as_view()),
    path("user-contests/", views.ContestAPIView.as_view()),
    path("user-contests/archived/", views.ArchivedContestAPIView.as_view()),
    path("contest-tasks/", views.TaskAPIView.as_view()),
    path("has-permission-to-contest/", views.HasPermissionToContestAPIView.as_view()),
    path("user-submissions/", views.SubmissionAPIView.as_view())
]
