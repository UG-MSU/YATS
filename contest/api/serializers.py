from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from main.models import contest, task, submission, contest_user, contest_task, user
from rest_framework import pagination
from rest_framework.response import Response


class ContestPagination(pagination.PageNumberPagination):
    page_size = 6
    def get_paginated_response(self, data):
        return Response(
            status=200,
            data={
                'status': 'ok',
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'contests': data
        })


class TaskPagination(pagination.PageNumberPagination):
    page_size=6
    def get_paginated_response(self, data):
        return Response(
            status=200,
            data={
                'status': 'ok',
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'tasks': data
        })


class SubmissionPagination(pagination.PageNumberPagination):
    page_size = 6
    def get_paginated_response(self, data):
        return Response(
            status=200,
            data={
                'status': 'ok',
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'submissions': data
        })


class CreateContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = ("name", "password")
        extra_kwargs = {"password": {"write_only": True}}


class ContestSerializer(serializers.ModelSerializer):
    id_contest = serializers.IntegerField(source="id_contest.id_contest")
    name = serializers.CharField(source="id_contest.name")
    description = serializers.CharField(source="id_contest.description")
    password = serializers.CharField(source="id_contest.password")
    archived = serializers.BooleanField(source="id_contest.archived", default=False)
    class Meta:
        model = contest_user
        fields = ("name", "description", "password", "archived", "id_contest")
        extra_kwargs = {"password": {"write_only": True}}


class TaskSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source="id_task.task_name")
    statement = serializers.CharField(source="id_task.statement")

    class Meta:
        model = contest_task
        fields = ("task_name", "statement")


class SubmissionSerializer(serializers.ModelSerializer):
    id_task = serializers.CharField(source="id_task.id_task")
    id_contest = serializers.CharField(source="id_contest.id_contest")

    class Meta:
        model = submission
        fields = ("status", "lang", "id_task", "id_contest")


class ContestPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = "creator"
