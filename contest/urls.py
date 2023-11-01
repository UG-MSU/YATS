from django.contrib import admin
from django.urls import path, include
from contest.api.views import ContestAPIView

urlpatterns = [
    path("all/", ContestAPIView.as_view()),

]