from django.urls import path
from . import views as vws
from .api import views

urlpatterns = [
    path("my-contests", views.MyContestsListView.as_view(), name=None),
    path("my-tasks", views.MyTasksListView.as_view(), name=None),
    path("my-submissions", views.MySubmissionsListView.as_view(), name=None),
]
