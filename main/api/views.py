from django.contrib.auth.models import AnonymousUser

from ..models import contest, user, contest_user, task, submission
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
        cont = [el.id_contest for el in cu]
        conts = []
        for i in cont:
            conts.append(contest.Contest.get(id_contest=i.id_contest))
        data = serializers.ContestSerializer(conts, many=True).data
        return Response(data)


class MyTasksListView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = task.Task.all()

    def get(self, request):
        user = self.request.user
        if user == AnonymousUser():
            # return HttpResponse(f"USER IS ANONIMUS")
            user = 1
        tsks = task.Task.all()
        data = serializers.TaskSerializer(tsks, many=True).data
        return Response(data)


class MySubmissionsListView(generics.ListAPIView):
    serializer_class = serializers.SumbissionSerializer
    queryset = submission.Submission.all()

    def get(self, request):
        user = self.request.user
        if user == AnonymousUser():
            # return HttpResponse(f"USER IS ANONIMUS")
            user = 1
        submissions = submission.Submission.filter(id_user_id=user)
        data = serializers.SumbissionSerializer(submissions, many=True).data
        return Response(data)
