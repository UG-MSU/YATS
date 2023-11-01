from django.contrib.auth.models import AnonymousUser

from ..models import contest, user, contest_user, task
from . import serializers
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.response import Response


class ContestListView(generics.ListAPIView):
    queryset = contest.Contest.all()
    print(queryset)
    serializer_class = serializers.ContestSerializer


class MyContestsListView(generics.ListAPIView):
    serializer_class = serializers.ContestSerializer
    queryset = contest.Contest.all()

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user == AnonymousUser():
            # return HttpResponse(f"USER IS ANONIMUS")
            user = 1
        cu = contest_user.Contest_user.filter(id_user=user)
        cnt = contest.Contest.all()
        queryset = cnt
        data = serializers.ContestSerializer(cnt).data
        return Response(data)


class MyTasksListView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer

    def get(self, request):
        user = self.request.user
        if user == AnonymousUser():
            # return HttpResponse(f"USER IS ANONIMUS")
            user = 1
        cu = contest_user.Contest_user.filter(id_user=user)
        tsks = task.Task.all()
        queryset = tsks
        serializer = serializers.ContestSerializer(tsks)
        data = serializers.TaskSerializer(tsks).data
        return Response(data)
