from django.urls import path
from . import views as vws
from .api import views

urlpatterns = [
    path("", views.ContestListView.as_view(), name=None),
    path("add_cont", vws.add_contest),
    path("my-contests", views.MyContestsListView.as_view(), name=None),
    path("my-tasks", views.MyTasksListView.as_view(), name=None),
]
