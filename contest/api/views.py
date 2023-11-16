from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, task, submission, contest_user, contest_task, user
from contest.api import serializers
from django.contrib.auth import authenticate, login
from rest_framework import generics


def update_contest(request, contest):
    if len(request.data["name"]) != 0:
        contest.name = request.data["name"]
    if len(request.data["description"]) != 0:
        contest.description = request.data["description"]
    if len(request.data["password"]) > 7 and len(request.data["password"]) < 26:
        contest.password = request.data["description"]
    contest.save()


class CreateContestAPIView(generics.ListAPIView):
    queryset = []
    model = contest

    def post(self, request):
        if request.user is None:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        if 7 < len(request.data["password"]) < 32:
            return Response(status=401, data={"status": "error", "detail": "invalid size of password"})
        created_contest = contest(
            name=request.data["name"],
            password=request.data["password"],
            creator=request.user,
        )
        created_contest.save()
        return Response(status=200, data={"status": "ok"})


class ContestAPIView(generics.ListAPIView):
    serializer_class = serializers.ContestSerializer
    queryset = []

    def get(self, request):
        contest_id = request.GET.get("id", -1)
        user = request.user
        if user is None or request.user.is_anonymous:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        if contest_id == -1:
            user_contests = contest_user.Contest_user.filter(id_user=user)
            data = serializers.ContestSerializer(user_contests, many=True).data
            return Response(status=200, data={"status": "ok", "contests": data})
        try:
            cont = contest.Contest.get(id_contest=contest_id)
            current_contest = contest_user.Contest_user.get(
                id_user=user, id_contest=cont
            )
            return Response(
                status=200,
                data={
                    "status": "ok",
                    "contest": serializers.ContestSerializer(current_contest).data,
                }
            )
        except:
            return Response(status=400, data={"status": "error", "detail": "incorrect contest"})

    def put(self, request):
        user = self.request.user
        if user is None:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        try:
            contest_id = request.GET.get("id", -1)
            cont = contest.Contest.get(id_contest=contest_id)
            current_contest = contest_user.Contest_user.get(
                id_user=user, id_contest=cont
            )
            update_contest(request, current_contest.id_contest)
            return Response(
                status=200,
                data={
                    "status": "ok",
                    "contest": serializers.ContestSerializer(current_contest).data,
                }
            )
        except:
            return Response(status=400, data={"status": "error", "detail": "incorrect contest"})


class TaskAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = task.Task.all()

    def get(self, request):
        contest_id = request.GET.get("id", -1)
        if contest_id == -1:
            return Response(status=400, data={"status": "error", "detail": "contest is not defined"})
        tasks = contest_task.Contest_task.filter(id_contest=contest_id)
        data = serializers.TaskSerializer(tasks, many=True).data
        return Response(status=200, data={"status": "ok", "tasks": data})


class SubmissionAPIView(generics.ListAPIView):
    serializer_class = serializers.SubmissionSerializer
    queryset = submission.Submission.all()

    def get(self, request):
        user = self.request.user
        submissions = submission.Submission.filter(id_user_id=user)
        data = serializers.SubmissionSerializer(submissions, many=True).data
        return Response(data.update({"status": "ok"}))


class HasPermissionToContestAPIView(generics.ListAPIView):
    serializer_class = serializers.ContestPermissionSerializer
    queryset = contest.Contest.all()
