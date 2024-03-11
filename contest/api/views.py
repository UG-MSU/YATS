from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, task, submission, contest_user, contest_task, user, test
from contest.api import serializers
from django.contrib.auth import authenticate, login
from rest_framework import generics
from contest.api.serializers import ContestPagination, TaskPagination, SubmissionPagination
from rest_framework.parsers import FileUploadParser
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
import subprocess
import json
import logging
from container.container-lib import solve
logger = logging.getLogger(__name__)


def update_contest(request, contest):
    if len(request.data["name"]) != 0:
        contest.name = request.data["name"]
    if len(request.data["description"]) != 0:
        contest.description = request.data["description"]
    if len(request.data["password"]) > 7 and len(request.data["password"]) < 26:
        contest.password = request.data["description"]
    try:
        contest.archived = request.data["archived"]
        contest.save()
    except:
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
        paginator = ContestPagination()
        print(request.user.username)
        if user is None or request.user.is_anonymous:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        if contest_id == -1:
            user_contests = contest_user.Contest_user.filter(id_user=user, id_contest__archived=False)
            paginated_user_contests = paginator.paginate_queryset(user_contests, request)
            serializer = serializers.ContestSerializer(paginated_user_contests, many=True)
            return paginator.get_paginated_response(serializer.data)
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
            print(user.username)
            print(contest_id)
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

class ArchivedContestAPIView(generics.ListAPIView):
    serializer_class = serializers.ContestSerializer
    queryset = []
    def get(self, request):
        contest_id = request.GET.get("id", -1)
        user = request.user
        paginator = ContestPagination()
        print(request.user.username)
        if user is None or request.user.is_anonymous:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        user_contests = contest_user.Contest_user.filter(id_user=user, id_contest__archived=True)
        paginated_user_contests = paginator.paginate_queryset(user_contests, request)
        serializer = serializers.ContestSerializer(paginated_user_contests, many=True)
        return paginator.get_paginated_response(serializer.data)

class TaskAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer
    queryset = task.Task.all()

    def get(self, request):
        paginator = TaskPagination()
        contest_id = request.GET.get("id", -1)
        if contest_id == -1:
            return Response(status=400, data={"status": "error", "detail": "contest is not defined"})
        tasks = contest_task.Contest_task.filter(id_contest=contest_id)
        paginated_tasks = paginator.paginate_queryset(tasks, request)
        serializer = serializers.TaskSerializer(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)


class SubmissionAPIView(generics.ListAPIView):
    serializer_class = serializers.SubmissionSerializer
    queryset = submission.Submission.all()

    def get(self, request):
        paginator = SubmissionPagination()
        user = self.request.user
        submissions = submission.Submission.filter(id_user_id=user)
        paginated_submissions = paginator.paginate_queryset(submissions, request)
        serializer = serializers.TaskSerializer(paginated_submissions, many=True)
        return paginator.get_paginated_response(serializer.data)
    def post(self, request):
        if request.user is None:
            return Response(status=401, data={"status": "error", "detail": "user is not authenticated"})
        up_file = request.FILES['file']
        cont_id = request.data["id_contest"]
        task_id = request.data["id_task"]
        user = request.user
        user_id = user.id
        now = datetime.now()
        tm = now.strftime("%d-%m-%Y-%H-%M-%S")
        destination = open(f'files/submissions/{cont_id}/{task_id}/{user_id}/{tm}_{up_file.name}', 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()
        lang = request.data["language"]
        filename = f'files/submissions/{cont_id}/{task_id}/{user_id}/{tm}_{up_file.name}'
        try:
            b = ('.'.join(filename.split('.')[:-1])) + '.out'

            if lang[0] == 'c++':
                subprocess.call(["g++", filename, f'-o{b}'])
            elif lang[0] == 'c':
                subprocess.call(["gcc", filename, f'-o{b}'])
            elif lang[0] == 'pascal':
                subprocess.call(["gcc", filename, f'-o{b}'])
        except:
            sub = submission(id_user=user,
                             id_task=task.Task.get(id_task=task_id),
                             id_contest=contest.Contest.get(id_contest=cont_id), timestamp=now, status="CE",
                             executable_path=filename, lang=lang)
            sub.save()
            paginator = SubmissionPagination()
            submissions = submission.Submission.filter(id_user_id=user)
            paginated_submissions = paginator.paginate_queryset(submissions, request)
            serializer = serializers.TaskSerializer(paginated_submissions, many=True)
            return paginator.get_paginated_response(serializer.data)
        tt = test.Test.get(id_task=task.Task.get(id_task=task_id))
        json_file = tt.pathToFileWithTests
        with open(json_file) as json_data:
            data = json.load(json_data)
        counter = 0
        for i in range(len(data["tests"])):
            try:
                out_dict = solve(b, data["tests"][i]["input"], data["tests"][i]["time"], 8, data["tests"][i]["memory"])
            except:
                out_dict = dict()
                out_dict["status"] = "run_failed"
            if out_dict["status"] == "ok" and out_dict["container_output"]["out_buffer"] == data["tests"][i]["output"]:
                counter += 1
        try:
            subprocess.call(["rm", b])
        except:
            logger.info('ERROR with STEP5')

        if counter == len(data["tests"]):
            logger.info('All answers is correct')
        else:
            logger.info(f'Correct answers: {counter}/{len(data["tests"])}')

        if counter == len(data["tests"]):
            sub = submission(id_user=user,
                             id_task=task.Task.get(id_task=task_id),
                             id_contest=contest.Contest.get(id_contest=cont_id), timestamp=now, status="OK",
                             executable_path=filename, lang=lang)
            sub.save()
            paginator = SubmissionPagination()
            submissions = submission.Submission.filter(id_user_id=user)
            paginated_submissions = paginator.paginate_queryset(submissions, request)
            serializer = serializers.TaskSerializer(paginated_submissions, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            sub = submission(id_user=user,
                             id_task=task.Task.get(id_task=task_id),
                             id_contest=contest.Contest.get(id_contest=cont_id), timestamp=now, status="WA",
                             executable_path=filename, lang=lang)
            sub.save()
            paginator = SubmissionPagination()
            submissions = submission.Submission.filter(id_user_id=user)
            paginated_submissions = paginator.paginate_queryset(submissions, request)
            serializer = serializers.TaskSerializer(paginated_submissions, many=True)
            return paginator.get_paginated_response(serializer.data)


class HasPermissionToContestAPIView(generics.ListAPIView):
    serializer_class = serializers.ContestPermissionSerializer
    queryset = contest.Contest.all()
